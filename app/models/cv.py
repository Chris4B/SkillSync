from sqlalchemy import Column, Integer, DateTime, JSON
from sqlalchemy.sql import func
from app.database.db import Base
from datetime import datetime

class CV(Base):
    __tablename__ = "cv"

    id = Column(Integer, primary_key=True, index=True)
    content_json = Column(JSON, nullable=False)  # Stockage du CV structuré
    created_at = Column(DateTime, default=datetime.now)  # Date de création
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)  # Date de mise à jour automatique
