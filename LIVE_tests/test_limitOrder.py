import sys
sys.path.insert(0,'./')
from execute_trades.src.execute_trades import limitOrder
from deploy_algorithm.config import cred

client = cred.client



symbol = 'ETHBTC'
min_qty = str(float(client.get_symbol_info(symbol)['filters'][1]['minQty'])*25)
current_price = str(float(client.get_order_book(symbol=symbol,limit=1)['bids'][0][0]))
hold_min = 1





lo =  limitOrder(
    order_direction = "BUY",
    price = '0.053',
    qty = min_qty,
    symbol = symbol,
    hold_min = hold_min,
    check_sec = 10,
    timeout_market_order = False,
    timeout_cancel = True
)

order_dict = lo.deploy_timeout_limit_order()


print([(x,order_dict[x]) for x in order_dict])

