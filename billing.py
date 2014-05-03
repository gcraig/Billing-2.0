import sys
import couchdb

from couchdb.mapping import Document, TextField, IntegerField, DateTimeField

class Invoice(Document):
  invoice_number = TextField()

couch = couchdb.Server()
db = couch['billing']

for id in db:
  print id
  invoice = Invoice.load(db, id)
  invoice.invoice_number = str(int(invoice.invoice_number) + 1)
  print invoice
  invoice.store(db)

# invoice.json.tmpl