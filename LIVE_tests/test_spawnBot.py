import os
from deploy_algorithm.src.deploy_classes import spawnBot

### SPAWN BOT TEST
sample_details = [['BNBBTC', 0.007191, 0.00719136842105263, -5.1231007933250083e-05, 49.17830265801731, 0.417, 0.007047541052631578, 3, 6]]
path = os.path.join("deploy_algorithm","applications","algo_1","bot.py")
spawnBot.spawn(
    bot_path=path,
    details_list=sample_details
    )

