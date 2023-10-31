import sys
sys.path.insert(0,'./')
from execute_trades.src.execute_trades import marketOrder
from deploy_algorithm.config import cred

client = cred.client



symbol = 'ETHBTC'
min_qty = str(float(client.get_symbol_info(symbol)['filters'][1]['minQty'])*25)
current_price = str(float(client.get_order_book(symbol=symbol,limit=1)['bids'][0][0]))
hold_min = 1




trade_dict = {
    symbol: {
        "SIDE": "BUY",
        "QTY": min_qty
        }
    }
mo = marketOrder(trade_dict=trade_dict)
order_list = mo.execute_trades(test=False)





