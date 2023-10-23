import sys
sys.path.insert(0,'./')
from execute_trades.src.execute_trades import LimitOrder
from deploy_algorithm.config import cred

client = cred.client

"""
make LimitOrder robust before making any other class 
"""

symbol = 'ETHBTC'
min_qty = str(float(client.get_symbol_info(symbol)['filters'][1]['minQty'])*20)
current_price = str(float(client.get_order_book(symbol=symbol,limit=1)['bids'][0][0]))
hold_period = 0.5






class limitOrder:
    def __init__(self):
        self.client = cred.client

        self.orders_dict = {}

        self.last_order = None
        self.qty = None
        self.symbol = None
    
    # DETERMINE WHEN TRADE IS FINISHED
    # trade is finished when all qty has been sold or timer finishes
    # if timer finishes can either leave the order, cancel the order, market buy/sell
    
    
    # CHECK ORDER STATUS
    def get_live_order(self,order_id):
        order_details = client.get_order(symbol = self.symbol, orderId = order_id)
        order_id,details_dict = self.get_order_details(order_details)
        self.orders_dict[order_id] = details_dict

    @staticmethod
    def get_order_details(order):
        order_id = order['orderId']
        order_status = order['status']
        order_price = order['price']
        executed_qty = order['executedQty']
        orig_qty = order['origQty']
        side = order['side']
        order_type = order['type']

        if order_status == 'FILLED' or orig_qty - executed_qty == 0:
            order_complete = True

        return order_id, {
            'order_id':order_id,
            'order_status':order_status,
            'order_price':order_price,
            'orig_qty':orig_qty,
            'executed_qty':executed_qty,
            'side':side,
            'order_type':order_type,
            'order_complete':order_complete
        }

    # PLACE ORDERS
    def place_limit_sell_order(self,price):
        current_order = self.client.order_limit_sell(
            symbol=self.symbol,
            quantity=self.qty,
            price=price)
        order_id,details_dict = self.get_order_details(current_order)
        self.orders_dict[order_id] = details_dict

    def place_limit_buy_order(self,price):
        current_order = self.client.order_limit_buy(
            symbol=self.symbol,
            quantity=self.qty,
            price=price)
        order_id,details_dict = self.get_order_details(current_order)
        self.orders_dict[order_id] = details_dict











lo = LimitOrder()
buy_executed_amt, orders_buy_dict = lo.limit_buy_order_timeout(
    max_buy_price=current_price,
    qty = min_qty,
    symbol = symbol,
    timeout_min = int(15*hold_period),
    check_orderbook_freq_seconds=30
)
print('sell_executed_amt',buy_executed_amt)
print('orders_sell_dict',orders_buy_dict)


lo = LimitOrder()
sell_executed_amt, orders_sell_dict = lo.limit_sell_order_timeout(
    min_sell_price=current_price,
    qty = min_qty,
    symbol = symbol,
    timeout_min = int(15*hold_period),
    check_orderbook_freq_seconds=30
)
print('sell_executed_amt',sell_executed_amt)
print('orders_sell_dict',orders_sell_dict)