import unittest
from src.operations.transfer_opp import TransferOpp
from unittest.mock import patch
from src.models.invoice import Invoice


def get_invoice(amount, name):
    return Invoice(
        status="pending",
        amount=amount,
        name=name
    )


class TestTransferOpp(unittest.TestCase):

    @patch('src.models.invoice.Invoice')
    @patch('starkbank.transfer.create')
    def test_make_standard_transfer(self, mock_get, mock_invoice):

        mock_invoice.return_value = get_invoice(-50000, "Jon Snow")

        with self.assertRaises(ValueError):
            TransferOpp.make_standard_transfer(mock_invoice())

            mock_invoice.return_value = get_invoice(50000, "")

        with self.assertRaises(ValueError):
            TransferOpp.make_standard_transfer(mock_invoice())

        invoice = get_invoice(50000, "Jon Snow")

        TransferOpp.make_standard_transfer(invoice)

        assert mock_get.called
