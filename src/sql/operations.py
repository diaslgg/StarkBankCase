from sqlalchemy.orm import Session
from src.sql.database import engine, SessionLocal
from src.sql.config import get_db
from sqlalchemy import text, MetaData, Column, update
from src.sql.models import Transfer


class DatabaseOpp:
    """
    Class responsible for database manipulation
    """
    @staticmethod
    def query_database(query_statement, model):
        """
        Query tables
        :param query_statement: String with select statement.
        :param model: Model used for the table query.
        :return: List of dictionaries.
        """
        db = SessionLocal()
        try:
            result = db.execute(text(query_statement))
            MetaData()
            table = model.__table__
            table.create(bind=engine, checkfirst=True)
            columns = [Column(name=col.name, type_=col.type) for col in table.columns]
            rows = [dict(zip([col.name for col in columns], row)) for row in result.fetchall()]
            return rows

        except Exception as e:
            print(f"Error: {e}")
        finally:
            db.close()

    @staticmethod
    def update_row(pk_id, data, model):
        """
        Updates table rows.
        :param pk_id: Primary key id.
        :param data: Dictionary with column name and value to be updated [accept more than one value update].
        :param model: Model used for the table query.
        :return:
        """
        db = SessionLocal()
        try:
            query = update(model).where(model.id == pk_id).values(**data)
            db.execute(query)
            db.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            db.close()

    @staticmethod
    def insert_row(data, model):
        """
        Insert new rows at the table.
        :param data: Dictionary with column name and value to be inserted [accept more than one value update].
        :param model: Model used for the table query.
        :return:
        """
        db = SessionLocal()
        try:
            new_object = model(**data)
            db.add(new_object)
            db.commit()
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
        finally:
            db.close()

    @staticmethod
    def create_transfer(db: Session, model: Transfer):
        """
        Update Transfer table with standard transfers.
        :param db: Session Database
        :param model: Model used for the table query.
        :return: 
        """
        new_transfer = Transfer(
            bank_code=model.bank_code,
            branch_code=model.branch_code,
            account_number=model.account_number,
            name=model.name,
            tax_id=model.tax_id,
            account_type=model.account_type,
            amount=model.amount
        )
        db.add(new_transfer)
        db.commit()
        db.refresh(new_transfer)
        return new_transfer
