from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="User")

    tenders = relationship("Tender", back_populates="uploaded_by_user")
    ai_interactions = relationship("AIInteraction", back_populates="user")

class Tender(Base):
    __tablename__ = "tenders"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date_uploaded = Column(DateTime, default=datetime.utcnow)
    uploaded_by = Column(Integer, ForeignKey("users.id"))
    description = Column(Text)

    uploaded_by_user = relationship("User", back_populates="tenders")
    documents = relationship("TenderDocument", back_populates="tender")
    specifications = relationship("Specification", back_populates="tender")
    matches = relationship("Match", back_populates="tender")

class TenderDocument(Base):
    __tablename__ = "tender_documents"
    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey("tenders.id"))
    file_name = Column(String)
    file_type = Column(String)
    file_path = Column(String)

    tender = relationship("Tender", back_populates="documents")

class Specification(Base):
    __tablename__ = "specifications"
    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey("tenders.id"))
    type = Column(String)
    section_number = Column(String)
    content = Column(Text)
    approved = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    tender = relationship("Tender", back_populates="specifications")
    ai_interactions = relationship("AIInteraction", back_populates="specification")

class Equipment(Base):
    __tablename__ = "equipment"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    brand = Column(String)
    model_number = Column(String)
    spec_data = Column(Text)  # JSON stored as string
    source_link = Column(String)

    matches = relationship("Match", back_populates="equipment")

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey("tenders.id"))
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    match_score = Column(Float)
    match_date = Column(DateTime, default=datetime.utcnow)

    tender = relationship("Tender", back_populates="matches")
    equipment = relationship("Equipment", back_populates="matches")
    generated_documents = relationship("GeneratedDocument", back_populates="match")

class GeneratedDocument(Base):
    __tablename__ = "generated_documents"
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=True)
    tender_id = Column(Integer, ForeignKey("tenders.id"), nullable=True)
    type = Column(String)
    file_name = Column(String)
    file_path = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)

    match = relationship("Match", back_populates="generated_documents")

class AIInteraction(Base):
    __tablename__ = "ai_interactions"
    id = Column(Integer, primary_key=True, index=True)
    spec_id = Column(Integer, ForeignKey("specifications.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    question = Column(Text)
    response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    specification = relationship("Specification", back_populates="ai_interactions")
    user = relationship("User", back_populates="ai_interactions")
