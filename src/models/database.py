from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class ListingHistory(Base):
    __tablename__ = "listing_history"
    
    id = Column(String, primary_key=True)  # URL hash
    title = Column(String)
    price = Column(Float)
    url = Column(String)
    site = Column(String, default="eBay UK")
    timestamp = Column(DateTime, default=datetime.utcnow)

# Initialize database
engine = create_engine("sqlite:///data/listings.db")
Base.metadata.create_all(engine)