import sys
import string
import couchdb

from couchdb.mapping import Document, TextField, IntegerField, DateTimeField

class Invoice( Document ):
  invoice_number = TextField()

couch = couchdb.Server()
db = couch['billing']

def read_template( invoice ):
  filein = open( 'invoice.json.tpl' )
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

read_invoice( db )

#for id in db:
#  print id
#  invoice = Invoice.load(db, id)
#  invoice.invoice_number = str(int(invoice.invoice_number) + 1)
#  print invoice
#  invoice.store(db)

# invoice.json.tmpl