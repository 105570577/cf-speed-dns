from geckoterminal_api import GeckoTerminalAPI

gt = GeckoTerminalAPI()

trades = gt.network_pool_trades(network="solana", pool="69grLw4PcSypZnn3xpsozCJFT8vs8WA5817VUVnzNGTh")
for trade_data in trades["data"]:
    trade = trade_data["attributes"]
    print(f'{trade["block_timestamp"]} -- {trade["kind"]}: {float(trade["volume_in_usd"]):.2f} USD')
