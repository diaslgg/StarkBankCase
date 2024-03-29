from src.auth.starkbank_auth import StarkbankAuth
import starkbank
from src.models.invoice import Invoice


class TransferOpp:
    """
    Class responsible for POST Transfers on starkbank API.
    """
    @staticmethod
    def make_standard_transfer(invoice: Invoice):
        """
        Standard transfer to Stark Bank S.A as part of an operation.
        :param invoice: Invoice class.
        :return: Successful or Failed message.
        """

        amount = invoice.amount
        name = invoice.name

        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        if not name:
            raise ValueError("Name of payer cannot be empty.")

        try:
            transfer = starkbank.transfer.create([
                starkbank.Transfer(
                    bank_code="20018183",
                    branch_code="0001",
                    account_number="6341320293482496",
                    name="Stark Bank S.A.",
                    tax_id="20.018.183/0001-80",
                    account_type="payment",
                    tags=["Standard transfer", name],
                    amount=amount
                )
            ], StarkbankAuth.auth())
            return transfer

        except Exception as e:
            print(f"Unexpected error: {e}")
