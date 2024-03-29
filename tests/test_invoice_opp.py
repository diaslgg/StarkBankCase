import unittest
from src.operations.invoice_opp import InvoiceOpp
from unittest.mock import patch, Mock


class TestInvoiceOpp(unittest.TestCase):

    @patch('starkbank.invoice.create')
    def test_create_invoice(self, mock_get):
        mock_response = Mock()
        response = None
        mock_response.return_value = response

        mock_get.return_value = mock_response

        invoice = InvoiceOpp.create_invoice(50000, '01234567890', 'Jon Snow')
        mock_get.assert_called()

        self.assertEquals(invoice, response)

        with self.assertRaises(ValueError):
            InvoiceOpp.create_invoice(-50000, '01234567890', 'Jon Snow')

        with self.assertRaises(ValueError):
            InvoiceOpp.create_invoice(0, '01234567890', 'Jon Snow')

        with self.assertRaises(ValueError):
            InvoiceOpp.create_invoice(50000, '', 'Jon Snow')

        with self.assertRaises(ValueError):
            InvoiceOpp.create_invoice(50000, '01234567890', '')
