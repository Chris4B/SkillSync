from app.database.db import engine, Base

def init_db():
    """Création des tables dans la base de données."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
