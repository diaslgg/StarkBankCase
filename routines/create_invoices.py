import sys
from src.sql.models import Invoice
from src.sql.operations import DatabaseOpp
from src.operations.invoice_opp import InvoiceOpp

# query 12 invoices, not sent yet, to be issued
query = "SELECT * FROM invoices WHERE invoice_sent != True OR invoice_sent IS NULL LIMIT 12"

sql_result = DatabaseOpp.query_database(query, Invoice)

if not sql_result:
    print('No invoices to be sent')
    sys.exit()

# issue the invoices and insert the data into the table
for invoice in sql_result:
    if not invoice['invoice_sent']:
        table_id = invoice['id']
        amount = int(invoice['amount'])
        tax_id = invoice['tax_id']
        name = invoice['name']

        InvoiceOpp.create_invoice(amount, tax_id, name)
        DatabaseOpp.update_row(table_id, {"invoice_sent": True}, Invoice)

