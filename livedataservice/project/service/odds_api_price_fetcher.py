# pylint:disable=invalid-name, unused-variable, too-few-public-methods, attribute-defined-outside-init, line-too-long, bare-except
"""Holds OddsApiPriceFetcher."""
import os
import json
from statistics import mean
from dotenv import load_dotenv
import requests
from project.service.utilities import Utilities
from project.service.price_fetcher import PriceFetcher

load_dotenv()


class OddsApiPriceFetcher(PriceFetcher):
    """This class fetches different types of info given a sport,
    market, and an event id"""
    API_KEY = os.environ.get("api-token")
    REGIONS = 'us'
    ODDS_FORMAT = 'american'
    DATE_FORMAT = 'iso'

    def __init__(self, sport: str, market: str, odds_api_event_id: str):
        self.odds_api_event_id = odds_api_event_id
        self.sport = sport
        self.market = market

    def __eq__(self, other):
        if self.sport == other.sport and self.market == other.market and self.odds_api_event_id == other.odds_api_event_id:
            return True
        return False

    def get_sport(self):
        """Returns the specified sport."""
        return self.sport

    def get_market(self):
        """Returns the specified market."""
        return self.market

    def get_info(self) -> list:
        """Returns a list of tuples, each tuple contains an
        event id and the events odds."""
        self.response = requests.get(  # self.response is a requests object
            f'https://api.the-odds-api.com/v4/sports/{self.sport}/odds',
            params={
                'api_key': self.API_KEY,
                'regions': self.REGIONS,
                'markets': self.market,
                'oddsFormat': self.ODDS_FORMAT,
                'dateFormat': self.DATE_FORMAT,
            }
        )
        status_code = self.response.status_code
        if status_code != 200:
            if status_code == 401:
                return f'Failed to get odds: status_code {status_code}. Unauthorized access, invalid API token.'
            if 100 <= status_code <= 299:
                return f'Failed to get odds: status_code {status_code}.'
            if 300 <= status_code <= 399:
                return f'Failed to get odds: status_code {status_code}. Status Code 300-399 = Redirected.'
            if 400 <= status_code <= 499:
                return f'Failed to get odds: status_code {status_code}. Status Code 400-499 = Client Error.'
            if 500 <= status_code <= 599:
                return f'Failed to get odds: status_code {status_code}. Status Code 500-599 = Servor Error.'
        odds_json = json.loads(self.response.text)
        i = 0
        z = 0
        result = []
        while i < len(odds_json):
            k = 0
            away_list_prices, home_list_prices = [], []
            first = odds_json[z]
            event_id = first['id']
            if self.odds_api_event_id == event_id:
                for j in odds_json[i]['bookmakers']:
                    while k < len(odds_json[i]['bookmakers']):
                        away_price = Utilities.american_to_probability(
                            odds_json[i]['bookmakers'][k]['markets'][0]['outcomes'][0]['price'])
                        home_price = Utilities.american_to_probability(
                            odds_json[i]['bookmakers'][k]['markets'][0]['outcomes'][1]['price'])
                        away_list_prices.append(away_price)
                        home_list_prices.append(home_price)
                        k += 1
                prices = [round(mean(away_list_prices), 2),
                          round(mean(home_list_prices), 2)]
                result.append((event_id, prices))
            i += 1
            z += 1
        return result
