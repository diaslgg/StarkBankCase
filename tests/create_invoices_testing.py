import starkbank
from src.auth.starkbank import StarkbankAuth

invoice_list = list()

for i in range(67, 68):
    amount = 1000*1
    temp = [
        starkbank.Invoice(
            amount=10000*i,
            tax_id="319.528.628-92",
            name=f"Background actor {i}",
            tags=["invoice", f"Background actor {i}"]
        )
    ]
    invoice_list.extend(temp)

invoices = starkbank.invoice.create(invoice_list, user=StarkbankAuth.auth())
print(len(invoices))

for invoice in invoices:
    print(invoice)
