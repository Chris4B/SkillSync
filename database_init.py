from app.database.db import engine, Base
from app.models.cv import CV  # Importer le modèle CV

def init_db():
    """Création des tables dans la base de données."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
