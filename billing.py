import sys
import string
import couchdb

from couchdb.mapping import Document, TextField, IntegerField, DateTimeField

DEBUG = True

class Invoice( Document ):
  invoice_number = TextField()
  def __str__( self ):
    return "{Invoice: id=%s, invoice_number=%s}" % ( id, self.invoice_number )

#internal connection pool is at play
couch = couchdb.Server()
db = couch['billing']

def read_template( invoice ):
  filein = open( 'templates/invoice.json.tpl' )
  tpl = string.Template( filein.read() )
  data =  { 'invoice_number' : invoice.invoice_number }
  result = tpl.substitute( data )
  return result

def increment_invoice_number( invoice ):
  invoice.invoice_number = str( int( invoice.invoice_number ) + 1 )
  return invoice

def read_invoice_test( id ):
  invoice = read_invoice( id )
  invoice = increment_invoice_number( invoice )
  invoice_json = read_template( invoice )
  if DEBUG:
    print invoice_json
  invoice.store( db )
  invoice = read_invoice( id )
  if DEBUG:
    print "New invoice number: " + invoice.invoice_number
  return invoice

def create_invoice():
  invoice = Invoice( invoice_number=4000 )
  invoice.store( db )
  invoice = read_invoice( invoice.id )
  #find latest invoice number by db sequence
  #invoice.save( db )
  return invoice
  #invoice_json = read_template( invoice )

def read_invoice( id ):
  return Invoice.load( db, id )

def update_invoice( id ):
  pass

def delete_invoice( id ):
  pass

def db_init():
  print "Initializing the database ..."

def init():
  print "Initializing billing system ..."
  db_init()

if __name__ == '__main__':
  
  #id = 'a9f88ba1a38ec88771cb5974db0012a3'
  #print read_invoice( id )

  print create_invoice()

  #init()

#for id in db:
# invoice.json.tmpl
