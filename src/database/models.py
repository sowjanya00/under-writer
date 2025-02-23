from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime)

class Policy(Base):
    __tablename__ = 'policies'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    policy_type = Column(String, nullable=False)
    premium_amount = Column(Float, nullable=False)
    coverage_amount = Column(Float, nullable=False)
    created_at = Column(DateTime)

class RiskAssessment(Base):
    __tablename__ = 'risk_assessments'
    
    id = Column(Integer, primary_key=True)
    policy_id = Column(Integer, nullable=False)
    risk_score = Column(Float, nullable=False)
    assessment_date = Column(DateTime)