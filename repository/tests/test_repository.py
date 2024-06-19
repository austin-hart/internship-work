import unittest
import json
import datetime
from project.service.postgres_respository_manager import PostgresRepositoryManager
from unittest import mock
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.service.models import Base, TradeModel


class TestQuery(unittest.TestCase):

    # engine = create_engine(
    #    "postgresql+psycopg2://postgres:password@postgres:5432/{db}")
    engine = create_engine(
        "sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        file = open("project/service/trade3.json", "r")
        json_obj = json.load(file)
        json_data = json.dumps(json_obj)
        print(json_data)
        load_json_3 = json.loads(json_data)
        datetime_object = datetime.datetime.strptime(
            load_json_3["time"], '%Y-%m-%d %H:%M:%S.%f')
        trade = TradeModel(market=load_json_3["market"], side=load_json_3["side"],
                           size=load_json_3["size"], price=load_json_3["price"], time=datetime_object)
        Base.metadata.create_all(self.engine)
        self.session.add(trade)
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_query(self):
        start_date = "2017-06-29 08:15:27.243860"
        end_date = "2018-06-29 08:16:27.243860"
        market = 'brewers-cubs-124331232'
        side = 'buy'
        start_date = datetime.datetime.strptime(
            start_date, '%Y-%m-%d %H:%M:%S.%f')
        end_date = datetime.datetime.strptime(
            end_date, '%Y-%m-%d %H:%M:%S.%f')
        # expected = [TradeModel('brewers-cubs-124331232', 'buy', )]
        result = self.session.query(
            TradeModel).filter(TradeModel.market == market).filter(TradeModel.side == side).filter(TradeModel.time <= end_date).filter(TradeModel.time >= start_date).all()
        datetime_object = datetime.datetime.strptime(
            "2018-06-29 08:15:27.243860", '%Y-%m-%d %H:%M:%S.%f')
        self.assertEqual(result, [TradeModel(
            market="brewers-cubs-124331232", side="buy", size=120.0, price=0.53, time=datetime_object)])
