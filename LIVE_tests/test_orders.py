import sys
sys.path.insert(0,'./')
from execute_trades.src.execute_trades import createOrder
from database.src.sql_utils import database

from deploy_algorithm.config import cred



######################################## get trade info

client = cred.client
db = database()
db.drop_table(table_name="LIVE_orders")


symbol = 'ETHBTC'
min_qty = str(float(client.get_symbol_info(symbol)['filters'][1]['minQty'])*25)
current_price = float(client.get_order_book(symbol=symbol,limit=1)['bids'][0][0])


stop_loss_price = str(round(current_price*0.96,5))
take_profit_price = str(round(current_price*1.05,5))

stop_loss_small = str(round(current_price*0.9999,5))



######################################## STOP_LOSS_LIMIT


co = createOrder(
    symbol = symbol,
    side = "SELL",
    order_type = "STOP_LOSS_LIMIT",
    quantity = min_qty,
    price = stop_loss_price,
    stop_price = stop_loss_price,
    )

co.send_order()
order_id = co.order_latest_status['order_id']

co.get_order_status(order_id=order_id)
co.cancel_order(order_id=order_id)


print(db.select("select * from LIVE_orders"))


co = createOrder(
    symbol = symbol,
    side = "SELL",
    order_type = "TAKE_PROFIT_LIMIT",
    quantity = min_qty,
    price = take_profit_price,
    stop_price = take_profit_price,
    )

co.send_order()
order_id = co.order_latest_status['order_id']

co.get_order_status(order_id=order_id)
co.cancel_order(order_id=order_id)


print(db.select("select * from LIVE_orders"))


######################################## MARKET
co = createOrder(
    symbol = symbol,
    side = "BUY",
    order_type = "MARKET",
    quantity = min_qty
    )

co.send_order()
order_id = co.order_latest_status['order_id']

co.get_order_status(order_id=order_id)
co.cancel_order(order_id=order_id)


print(db.select("select * from LIVE_orders"))




######################################## LIMIT
co = createOrder(
    symbol = symbol,
    side = "SELL",
    order_type = "LIMIT",
    quantity = min_qty,
    price = take_profit_price,
    )

co.send_order()
order_id = co.order_latest_status['order_id']

co.get_order_status(order_id=order_id)
co.cancel_order(order_id=order_id)


print(db.select("select * from LIVE_orders"))


co = createOrder(
    symbol = symbol,
    side = "BUY",
    order_type = "LIMIT",
    quantity = min_qty,
    price = stop_loss_price,
    )

co.send_order()
order_id = co.order_latest_status['order_id']

co.get_order_status(order_id=order_id)
co.cancel_order(order_id=order_id)


print(db.select("select * from LIVE_orders"))





