# pylint: skip-file
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class TradeModel(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)
    market = Column(String, nullable=False)
    side = Column(String, nullable=False)
    size = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    time = Column(DateTime)

    def __repr__(self):
        return f"market={self.market}, side={self.side}, size={self.size}, price={self.price}, time={self.time}"

    def __eq__(self, other):
        if self.market == other.market and self.side == other.side and self.size == other.size and self.price == other.price and self.time == other.time:
            return True
        return False
