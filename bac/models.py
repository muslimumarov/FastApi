from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    category = Column(String)
    description = Column(String, nullable=True)
    is_income = Column(Boolean, default=False)
    date = Column(String)
