from dotenv import load_dotenv
import os
import starkbank
from src.auth.starkbank import StarkbankAuth
from datetime import datetime
from src.operations.transfer import Transfer

# print(StarkbankAuth.auth())

# transfer = starkbank.transfer.create([
#             starkbank.Transfer(
#                 bank_code="20018183",
#                 branch_code="0001",
#                 account_number="6341320293482496",
#                 name="Stark Bank S.A.",
#                 tax_id="20.018.183/0001-80",
#                 account_type="payment",
#                 tags=["Standard transfer"],
#                 amount=355555
#             )
#         ])

# transfer = Transfer.make_standard_transfer(500002, 'Background actor test')

# print(transfer)
import requests

base_url = "https://sandbox.api.starkbank.com"
endpoint = f"{base_url}/v2/public-key"

try:
    response = requests.get(endpoint)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    if response.content:
        public_key = response.content.decode("utf-8")
        print(public_key)
    else:
        print("Empty response received")

except requests.exceptions.RequestException as e:
    print(f"Error retrieving public key: {e}")
