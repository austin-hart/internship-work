# bot

- Rework app.py so that it starts both the data feed manager and the server
- Add the following endpoints to the server (proto/grpc): `get_value_for_feed`, `register_odds_api_feed`, `get_supported_feeds` (should return just "oddsAPI" and the required fields for it now, this can just be typed out in a configuration file.) `delete_feed`.