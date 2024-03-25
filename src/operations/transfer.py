from src.auth.starkbank import StarkbankAuth
import starkbank

from src.models.invoice import Invoice


class Transfer:

    @staticmethod
    def make_standard_transfer(invoice: Invoice, type_of_endpoint: str, project_id: str, private_key: str):
        """
        Standard transfer to Stark Bank S.A as part of an operation.
        :param invoice: Invoice class.
        :return: Successful or Failed message.
        """
        user = starkbank.Project(environment=type_of_endpoint,
                                 id=project_id,
                                 private_key=private_key)
        starkbank.user = user

        amount = invoice.amount
        name = invoice.name
        # if not invoice.amount or invoice.amount == 0:
        #     return {"message": "Amount not available"}

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
        ])

        if transfer[0].id:
            return {"message": "Transfer successful"}
        else:
            return {"message": "Transfer failed"}
