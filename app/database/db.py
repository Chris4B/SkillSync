from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Connexion à PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Création de la session pour interagir avec la BDD
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base pour les futurs modèles
Base = declarative_base()
