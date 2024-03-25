import starkbank
from src.auth.starkbank import StarkbankAuth

print(StarkbankAuth.auth())


# transfer = starkbank.transfer.create([
#             starkbank.Transfer(
#                 bank_code="20018183",
#                 branch_code="0001",
#                 account_number="6341320293482496",
#                 name="Stark Bank S.A.",
#                 tax_id="20.018.183/0001-80",
#                 account_type="payment",
#                 tags=["Standard transfer", "invoice/test"],
#                 amount=500000
#             )
#         ])
#
# print(transfer[0])