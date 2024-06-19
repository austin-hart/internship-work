# pylint: skip-file
import requests
import json
from statistics import mean
import os
from dotenv import load_dotenv
from price_fetcher import PriceFetcher
from utilities import Utilities
load_dotenv()


class OddsApiEventIdFetcher(PriceFetcher):
    API_KEY = os.environ.get("api-token")
    REGIONS = 'us'  # region of the sporting event
    ODDS_FORMAT = 'american'  # decimal or american
    DATE_FORMAT = 'iso'

    def __init__(self, sport: str, market: str):
        self.sport = sport
        self.market = market

    def __eq__(self, other):
        if self.sport == other.sport and self.markets == other.markets and self.odds_api_event_id == other.odds_api_event_id:
            return True
        return False

    def get_sport(self):
        return self.sport

    def get_markets(self):
        return self.markets

    def get_info(self) -> dict:
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
            elif status_code >= 100 and status_code <= 199:
                return f'Failed to get odds: status_code {status_code}.'
            elif status_code >= 200 and status_code <= 299:
                return f'Failed to get odds: status_code {status_code}.'
            elif status_code >= 300 and status_code <= 399:
                return f'Failed to get odds: status_code {status_code}. Status Code 300-399 = Redirected.'
            elif status_code >= 400 and status_code <= 499:
                return f'Failed to get odds: status_code {status_code}. Status Code 400-499 = Client Error.'
            elif status_code >= 500 and status_code <= 599:
                return f'Failed to get odds: status_code {status_code}. Status Code 500-599 = Servor Error.'
        else:
            # iterates through json object and gets the average market price for each match
            # loads response text into a json format
            odds_json = json.loads(self.response.text)
            i = 0
            z = 0
            result = []
            while i < len(odds_json):  # loops through json object
                k = 0
                # lists to hold odds from different bookmakers
                away_list_prices, home_list_prices = [], []
                first = odds_json[z]
                event_id = first['id']
                for j in odds_json[i]['bookmakers']:  # loops through al bookmakers
                    while k < len(odds_json[i]['bookmakers']):
                        # this is not used, only have it just in case we need
                        away_name = odds_json[i]['bookmakers'][k]['markets'][0]['outcomes'][0]['name']
                        # this is not used, only have it just in case we need
                        home_name = odds_json[i]['bookmakers'][k]['markets'][0]['outcomes'][1]['name']
                        away_price = Utilities.american_to_probability(
                            odds_json[i]['bookmakers'][k]['markets'][0]['outcomes'][0]['price'])  # gets implied probability away
                        home_price = Utilities.american_to_probability(
                            odds_json[i]['bookmakers'][k]['markets'][0]['outcomes'][1]['price'])  # gewts implied probabilty home
                        away_list_prices.append(away_price)
                        home_list_prices.append(home_price)
                        k += 1
                # this is not used, only have it just in case we need
                teams = f"{away_name}|{home_name}"
                prices = [round(mean(away_list_prices), 2),
                          round(mean(home_list_prices), 2)]
                # event_id is an odds api id not uuid
                result.append((event_id, teams, prices))
                i += 1
                z += 1
            # this result is a list of tuples [(odds_api_event_id, [price, price]), (odds_api_event_id, [price, price]), etc.]
            return result


if __name__ == '__main__':
    price_fetcher = OddsApiEventIdFetcher('baseball_mlb', 'h2h')
    id_list = price_fetcher.get_info()
    for id in id_list:
        print(id)
