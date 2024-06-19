# pylint: skip-file
"""Respository Manager."""


from project.service.models import TradeModel
from project.service.repository_manager import RepositoryManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import datetime
import logging


class PostgresRepositoryManager(RepositoryManager):
    """Will use this class to manage the repsoitory, add trades and get trades from database."""

    def __init__(self, user, password, host, port, db):
        self.session_maker = sessionmaker(bind=create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"))

    def get_trade(self, start_date, end_date, market, side, offset):
        start_offset = 0
        for i in range(offset):
            start_offset += 50
        start_date = datetime.datetime.strptime(
            start_date, '%Y-%m-%d %H:%M:%S.%f')
        end_date = datetime.datetime.strptime(
            end_date, '%Y-%m-%d %H:%M:%S.%f')
        with self.session_maker() as session:
            print(market)
            trade_records = session.query(
                TradeModel).filter(TradeModel.market == market).filter(TradeModel.side == side).filter(TradeModel.time <= end_date).filter(TradeModel.time >= start_date).limit(50).offset(start_offset).all()
            logging.info("GETTING TRADE FROM DATABASE.")
            return str(trade_records)

    def post_trade(self, json_data):
        """Uses json_data to post a trade to the database.
        parameters:     (json_data): json data that holds information about a single trade thats been placed."""
        load_json = json.loads(json_data)
        try:
            with self.session_maker() as session:
                datetime_object = datetime.datetime.strptime(
                    load_json["time"], '%Y-%m-%d %H:%M:%S.%f')
                trade = TradeModel(market=load_json["market"], side=load_json["side"],
                                   size=load_json["size"], price=load_json["price"], time=datetime_object)
                session.add(trade)
                session.commit()
                logging.info("TRADE POSTED TO DATABASE.")
                return "OK"
        except:
            return "UNABLE TO POST"
