import starkbank
from src.auth.starkbank_auth import StarkbankAuth


class InvoiceOpp:
    """
    Class responsible for create invoices to be issued
    """
    @staticmethod
    def create_invoice(amount, tax_id, name):
        """
        POST invoices on starkbank API
        :param amount: Int, in cents, of the amount.
        :param tax_id: String of the document.
        :param name: String with the name of the invoice payer.
        :return:
        """
        if amount <= 0:
            raise ValueError("Invoice amount must be positive.")

        if not tax_id:
            raise ValueError("Tax ID cannot be empty.")

        if not name:
            raise ValueError("Invoice payer name cannot be empty.")

        invoice = starkbank.Invoice(
                amount=amount,
                tax_id=tax_id,
                name=name,
                tags=[name, "Standard invoice"]
            )

        try:
            starkbank.invoice.create([invoice], user=StarkbankAuth.auth())

        except Exception as e:
            print(f"Unexpected error: {e}")
