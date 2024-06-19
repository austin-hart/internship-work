# pylint: skip-file
class OrderInfo():
    def __init__(self, exchange, market, side, price, size, kind):
        self.exchange = exchange
        self.market = market
        self.side = side
        self.price = price
        self.size = size
        self.kind = kind
        self.exchange_order_id = ''
        self.filled = 0

    def __str__(self):
        return str([self.exchange, self.market, self.side, self.price, self.size, self.kind])
