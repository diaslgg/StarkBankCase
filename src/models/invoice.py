from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


# BaseModel classes to receive json data from POST endpoint
class Invoice(BaseModel):
    status: str | None = None
    amount: int | None = None
    descriptions: List[Optional[dict]] | None = None
    discounts: List[Optional[dict]] | None = None
    due: datetime | None = None
    expiration: int | None = None
    fine: float | None = None
    interest: float | None = None
    fee: int | None = None
    name: str | None = None
    tags: List[str] | None = None
    tax_id: str | None = None
    line: str | None = None
    rules: List[Optional[dict]] | None = None


class Log(BaseModel):
    id: str | None = None
    created: datetime | None = None
    errors: List[str] | None = None
    type: str | None = None
    invoice: Invoice | None = None


class Event(BaseModel):
    id: str | None = None
    subscription: str | None = None
    created: datetime | None = None
    log: Log | None = None


class RequestPayload(BaseModel):
    event: Event | None = None
