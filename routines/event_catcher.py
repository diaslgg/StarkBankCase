from src.operations.event_opp import EventOpp
from src.sql.operations import DatabaseOpp
from src.sql.models import Events
from datetime import datetime, timedelta
from pytz import timezone

# prepare date to yesterday, in utc and convert to starkbank timezone
now_utc = datetime.utcnow()
yesterday = now_utc - timedelta(days=1)
sao_paulo_tz = timezone('America/Sao_Paulo')
after = yesterday.astimezone(sao_paulo_tz).date()

events = EventOpp.get_non_delivered_events(after)

# get all events not delivered by the webhook and insert it into the table
for event in events:
    if event.subscription == 'invoice' and event.log.invoice.status == 'paid':

        created = event.log.created
        log_id = event.log.id

        data = {
            "created": created,
            "log_id": log_id
        }
        DatabaseOpp.insert_row(data, Events)
