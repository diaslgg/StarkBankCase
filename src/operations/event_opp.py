from datetime import date, timedelta, timezone, datetime
from src.auth.starkbank_auth import StarkbankAuth
import starkbank


class EventOpp:
    """
    Class responsible for retrieving the events not delivered by webhook
    """
    @staticmethod
    def get_non_delivered_events(after):
        """
        Get all events not delivered after determined date.
        :param after: date object.
        :return: Object of the type Event.
        """

        if not isinstance(after, date):
            raise TypeError("Invalid after parameter. Must be a date object.")

        sao_paulo_timezone = timezone(timedelta(hours=-3))
        compare_date = datetime.now(sao_paulo_timezone).date()

        if after > compare_date:
            raise ValueError("Date should be before the current day, in America/São Paulo timezone.")

        try:
            events = starkbank.event.query(is_delivered=False, after=after, user=StarkbankAuth.auth())
            if events:
                return events
            else:
                return []

        except Exception as e:
            print(f"Unexpected error: {e}")
