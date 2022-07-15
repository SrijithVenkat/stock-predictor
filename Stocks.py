import requests
import math
from LinearModel import LinearRegModel
from PolynomialModel import PolyRegModel

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#NOT NECESSARY - Only if you want Firebase Features, put the json in the same folder or put the path
cred = credentials.Certificate("YOUR-SERVICE-ACCOUNT-FIREBASE.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://console.firebase.google.com/u/1/project/stocks-1ec7e/firestore/data/~2F'})

api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXX" #API KEY - Get yours from TwelveData, this code is based on their API


class Stock:

    def __init__(self, ticker, api_key) -> None:
        self.ticker = ticker
        self.day_details = self.get_stock_details(self.ticker, api_key)
        self.real_time_price = float(self.get_stock_realtime(ticker=self.ticker, key=api_key)['price'])
        self.open_data = []
        self.close_data = []
        self.high_data = []
        self.low_data = []
        self.trend_data = []

        for day in self.day_details['values']:
            self.open_data.append(float(day['open']))
            self.close_data.append(float(day['close']))
            self.high_data.append(float(day['high']))
            self.low_data.append(float(day['low']))
            if float(day['close']) - float(day['open']) > 0:
                self.trend_data.append(1)
            else:
                self.trend_data.append(0)
        
        self.saveToDataBase()
        self.LinModel = self.calculateLinModel()
        self.PolyModel = self.calculatePolyModel()

    def get_stock_details(self, ticker, key):
        url = "https://api.twelvedata.com/time_series?&start_date=2022-03-13&end_date=2022-06-13&symbol="+ticker+"&interval=1day&apikey="+key
        res = requests.get(url).json()
        return res

    def get_stock_realtime(self, ticker, key):
        url = "https://api.twelvedata.com/price?symbol="+ticker+"&apikey="+key
        res = requests.get(url).json()
        # print(res)
        return res

    def calculate_trend(self, data, numDays):
        #TRENDS ONLY FOR LONGER THAN 10 DAYS
        trend = ""
        daysTrend = data[-numDays:].count(1)
        if daysTrend > math.floor(numDays * .8):
            trend = f"VERY POSITIVE - {daysTrend} out of the last {numDays} days were positive"
        elif daysTrend > math.floor(numDays * .5): 
            trend = f"POSITIVE - {daysTrend} out of the last {numDays} days were positive"
        elif daysTrend == math.floor(numDays * .5):
            trend = f"VOLATILE"
        elif daysTrend >= math.floor(numDays * .3):
            trend = f"NEGATIVE - {daysTrend} out of the last {numDays} days were negative"
        else:
            trend = f"VERY NEGATIVE - {daysTrend} out of the last {numDays} days were negative"
        return trend

    #Simply added this functionality, if I wanted to compare past versus current data
    def saveToDataBase(self):
        db = firestore.client()
        db.collection(self.ticker).document('open').set({'open' : self.open_data})
        db.collection(self.ticker).document('close').set({'close' : self.close_data})
        db.collection(self.ticker).document('low').set({'low' : self.low_data})
        db.collection(self.ticker).document('high').set({'high' : self.high_data})
    
    def calculateLinModel(self):
        LinRegLow = LinearRegModel(self.low_data)
        LinRegHigh = LinearRegModel(self.high_data)
        LinRegOpen = LinearRegModel(self.open_data)
        LinRegClose = LinearRegModel(self.close_data)

        LinModelResults = [LinRegOpen.predictXDays(1), LinRegClose.predictXDays(1), LinRegLow.predictXDays(1), LinRegHigh.predictXDays(1)]

        return LinModelResults

    
    def calculatePolyModel(self):
        PolyRegLow = PolyRegModel(self.low_data)
        PolyRegHigh = PolyRegModel(self.high_data)
        PolyRegOpen = PolyRegModel(self.open_data)
        PolyRegClose = PolyRegModel(self.close_data)

        PolyModelResults = [PolyRegOpen.predictXDays(1), PolyRegClose.predictXDays(1), PolyRegLow.predictXDays(1), PolyRegHigh.predictXDays(1)]
        return PolyModelResults

    def linModel(self, data):
        ###########TESTING########
        return LinearRegModel(data)
    def polyModel(self, data):
        ###########TESTING########
        return PolyRegModel(data)
    
    def showPredictions(self):

        last10 = self.calculate_trend(self.trend_data, 10)
        last30 = self.calculate_trend(self.trend_data, 30)
        stock_ticker = self.ticker

        print(f"======================================================================")
        print()
        print(f"Stock - {stock_ticker}")
        print("Current Realtime Price - {:.3f}".format(float(self.real_time_price)))
        print()
        print("======================================================================")
        print()
        print(f"Linear Regression Model - {stock_ticker}")
        print()
        print("Open - {:.3f}".format(self.LinModel[0]))
        print("Close - {:.3f}".format(self.LinModel[1]))
        print("Low - {:.3f}".format(self.LinModel[2]))
        print("High - {:.3f}".format(self.LinModel[3]))
        print()
        print("======================================================================")
        print()
        print(f"Polynomial Regression Model - {stock_ticker}")
        print()
        print("Open - {:.3f}".format(self.PolyModel[0]))
        print("Close - {:.3f}".format(self.PolyModel[1]))
        print("Low - {:.3f}".format(self.PolyModel[2]))
        print("High - {:.3f}".format(self.PolyModel[3]))
        print()
        print("======================================================================")
        print()
        print("Trends")
        print()
        print(f"General Trend of Last 10 Days -> {last10}")
        print(f"General Trend of Last 30 Days -> {last30}")
        print()
        print("======================================================================")



#This file wasn't a stock class initially, so this was the testing to see how the functions worked, you can see for yourself if you'd like
#by uncommenting.
# TSLA = Stock(ticker="TSLA", api_key=api_key)
# AMZN = Stock(ticker="AMZN", api_key=api_key)
# NFLX = Stock(ticker="NFLX",api_key=api_key)

# TSLA.showPredictions()
# AMZN.showPredictions()
# NFLX.showPredictions()