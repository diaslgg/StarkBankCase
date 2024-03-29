import unittest
from unittest.mock import patch
import pytest
from src.sql.database import SessionLocal
from src.sql.models import Transfer, Events
from src.sql.operations import DatabaseOpp


class TestDatabaseOpp(unittest.TestCase):

    def test_query_database(self):

        with patch('src.sql.database.get_session_local') as mock_session:
            mock_session.return_value.execute.return_value = []

            result = DatabaseOpp.query_database("SELECT * FROM transfers LIMIT 0", Transfer)

            assert result == []

    def test_update_row(self):

        with patch('src.sql.database.get_session_local') as mock_session:
            # Simulate successful update
            mock_session.return_value.execute.return_value = None

            DatabaseOpp.update_row(1, {'log_id': 6585841606459392}, Events)

            mock_session.side_effect = Exception()

            with pytest.raises(Exception):
                DatabaseOpp.update_row(2, {})

    def test_insert_row(self):

        with patch('src.sql.database.get_session_local') as mock_session:

            mock_session.return_value.add.return_value = None
            mock_session.return_value.commit.return_value = None

            DatabaseOpp.insert_row({'bank_code': '20018183'}, Transfer)

            mock_session.return_value.add.return_value = None
            mock_session.return_value.commit.side_effect = Exception('Insert failed')

            with pytest.raises(Exception):
                DatabaseOpp.insert_row({})
