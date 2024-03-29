from src.sql.database import SessionLocal


# Database start configuration
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
