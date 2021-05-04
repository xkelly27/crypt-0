import c_data as C
import datetime
# yfinance refresher: period ex: 'ytd'
#                     interval ex: '1m'

crypto_list = ["BTC-USD", "ETH-USD", "DOGE-USD"]

C.Data(crypto_list[0]).plot("hist")




