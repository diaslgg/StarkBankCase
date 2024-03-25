import os
from functools import lru_cache
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
import ssl

from typing_extensions import Annotated

from src.models.invoice import RequestPayload
from src.operations.transfer import Transfer
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    private_key: str
    project_id: str
    type_of_environment: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
app = FastAPI()

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('../../httpsPrivateKey/cert.pem',
                            keyfile='../../httpsPrivateKey/key.pem')


@lru_cache
def get_settings():
    return Settings()


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "private_key": settings.private_key,
        "project_id": settings.project_id,
        "type_of_environment": settings.type_of_environment
    }


@app.post("/")
async def webhook_invoice(payload: RequestPayload):
    if payload.event.log.type == "credited":
        type_of_endpoint = get_settings().type_of_environment
        project_id = get_settings().project_id
        private_key = settings.private_key


        Transfer.make_standard_transfer(payload.event.log.invoice, type_of_endpoint, project_id, private_key)
