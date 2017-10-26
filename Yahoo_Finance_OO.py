import requests

class Stock_Downloader(object):


    def __init__(self, symbol):
        self.symbol = symbol
        request = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/' + self.symbol + '?modules=defaultKeyStatistics%2CfinancialData%2CcalendarEvents'
        r = requests.get(request)
        self.data = r.json()
    def download_yahoo(self,statistic):
        #print data
        financial_data = self.data['quoteSummary']['result'][0]['financialData']
        output = financial_data[statistic]["raw"]
        return output
    def current_price(self):
        My_Price=Stock_Downloader.download_yahoo(self,"currentPrice")
        return My_Price
    def return_on_assets(self):
        My_Price=Stock_Downloader.download_yahoo(self,"returnOnAssets")
        return My_Price
    def return_on_equity(self):
        My_Price=Stock_Downloader.download_yahoo(self,"returnOnEquity")
        return My_Price

AAPL = Stock_Downloader('AAPL')
AAPL_ROA=AAPL.return_on_assets()
AAPL_Price=AAPL.current_price()
AAPL_ROE=AAPL.return_on_equity()


print AAPL_ROA
print AAPL_Price
print AAPL_ROE



