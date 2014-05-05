import sys
import string
import couchdb

from couchdb.mapping import Document, TextField, IntegerField, DateTimeField

class Invoice( Document ):
  invoice_number = TextField()

couch = couchdb.Server()
db = couch['billing']

def read_template( invoice ):
  filein = open( 'templates/invoice.json.tpl' )
  tpl = string.Template( filein.read() )
  data =  { 'invoice_number' : invoice.invoice_number }
  result = tpl.substitute( data )
  return result

def read_invoice( db ):
  id = 'a9f88ba1a38ec88771cb5974db0012a3'
  invoice = Invoice.load( db, id )
  invoice.invoice_number = str( int( invoice.invoice_number ) + 1 )
  data = read_template( invoice )
  print data
  invoice.store( db )
  invoice = Invoice.load( db, id )
  print "New invoice number: " + invoice.invoice_number

def db_init():
  print "Initializing the database ..."

def init():
  print "Initializing billing system ..."
  db_init()

if __name__ == '__main__':
  read_invoice( db )
  #init()

#for id in db:
# invoice.json.tmpl
