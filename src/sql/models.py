from sqlalchemy import Column, Integer, String, Boolean, Date, BigInteger
from src.sql.database import Base


# ORMs classes
class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    amount = Column(Integer)
    tax_id = Column(String(20))
    invoice_sent = Column(Boolean)


class Transfer(Base):
    __tablename__ = 'transfers'

    id = Column(Integer, primary_key=True, index=True)
    bank_code = Column(String(20), nullable=True)
    branch_code = Column(String(20), nullable=True)
    account_number = Column(String(20), nullable=True)
    name = Column(String(100), nullable=True)
    tax_id = Column(String(20), nullable=True)
    account_type = Column(String(20), nullable=True)
    amount = Column(Integer, nullable=True)


class Events(Base):
    __tablename__ = 'events_not_delivered'

    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(BigInteger, nullable=True)
    created = Column(Date, nullable=True)

