import unittest
from datetime import datetime, timedelta
from pytz import timezone
from src.operations.event_opp import EventOpp
from unittest.mock import patch


class TestEventOpp(unittest.TestCase):

    @patch('starkbank.event.query')
    def test_get_non_delivered_events(self, mock_get):
        now_utc = datetime.utcnow()
        yesterday = now_utc - timedelta(days=1)
        sao_paulo_tz = timezone('America/Sao_Paulo')
        after = yesterday.astimezone(sao_paulo_tz).date()

        EventOpp.get_non_delivered_events(after)
        assert mock_get.called

        tomorrow = now_utc + timedelta(days=1)
        after = tomorrow.astimezone(sao_paulo_tz).date()

        with self.assertRaises(ValueError):
            EventOpp.get_non_delivered_events(after)

        with self.assertRaises(TypeError):
            EventOpp.get_non_delivered_events('date')
