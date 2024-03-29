from typing import Annotated
from fastapi import FastAPI, Depends
import ssl
from src.sql.database import engine
from src.models.invoice import RequestPayload
from src.operations.transfer_opp import TransferOpp
from sqlalchemy.orm import Session
from src.sql import models
from src.sql.operations import DatabaseOpp
from src.sql.config import get_db


app = FastAPI()

# https certificate and private key
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('../httpsKeys/cert.pem',
                            keyfile='../httpsKeys/key.pem')


models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/invoice")
async def webhook_invoice(payload: RequestPayload, db: db_dependency):
    """
    Webhook endpoint to receive all data from starkbank programed events
    :param payload:
    :param db:
    :return:
    """
    if payload.event.log.type == "credited":
        transfer = TransferOpp.make_standard_transfer(payload.event.log.invoice)
        DatabaseOpp.create_transfer(db, transfer[0])
