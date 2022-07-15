import numpy as np
from Stocks import Stock
import math

### Comment this out for Exporting
# import csv
# from itertools import zip_longest

api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXX" 

ticker_name = "MSFT"
tester = Stock(ticker=ticker_name, api_key=api_key)

class StockTester:
     
        def __init__(self, stock, margin_error) -> None:
            self.stock1 = stock
            self.mg_error_allow = margin_error
            self.linResults = []
            self.polyResults = []
        def runTest1(self):
            stock1LinearModel = self.stock1.linModel(self.stock1.open_data)
            stock1PolyModel = self.stock1.polyModel(self.stock1.open_data)
            x = stock1PolyModel.getX()
            stock1LinResults = list(map(stock1LinearModel.modelFunc, x))
            stock1PolyResults = list(map(stock1PolyModel.modelFunc, x))
            actual = self.stock1.open_data
            linear_diff_array = np.subtract(np.array(actual),np.array(stock1LinResults))
            poly_diff_array = np.subtract(np.array(actual),np.array(stock1PolyResults))

            limit = math.floor(self.stock1.real_time_price * self.mg_error_allow)
            lin_win_count = 0
            poly_win_cout = 0
            for lin_diff in linear_diff_array:
                if abs(lin_diff) <= limit:
                    lin_win_count += 1
            for poly_diff in poly_diff_array:
                if abs(poly_diff) <= limit:
                    poly_win_cout += 1
            linear_win_percentage = 100 * (lin_win_count/len(actual))
            self.linResults.append(linear_win_percentage)
            polynomial_win_percentage = 100 * (poly_win_cout/len(actual))
            self.polyResults.append(polynomial_win_percentage)

            print(f"======================================================================")
            print()
            print(f"Accuracy Testing for {self.stock1.ticker} - Open")
            print()
            print("Allowed a Margin of Error - {:2f} - {:2f}".format(self.mg_error_allow, limit))
            print()
            print("Linear Regression Model Accuracy - {:.3f}%".format(linear_win_percentage))
            print()
            print("Polynomial Regression Model Accuracy - {:.3f}%".format(polynomial_win_percentage))
            print()
            print("======================================================================")
        
        def runTest2(self):
            stock1LinearModel = self.stock1.linModel(self.stock1.close_data)
            stock1PolyModel = self.stock1.polyModel(self.stock1.close_data)
            x = stock1PolyModel.getX()
            stock1LinResults = list(map(stock1LinearModel.modelFunc, x))
            stock1PolyResults = list(map(stock1PolyModel.modelFunc, x))
            actual = self.stock1.close_data
            linear_diff_array = np.subtract(np.array(actual),np.array(stock1LinResults))
            poly_diff_array = np.subtract(np.array(actual),np.array(stock1PolyResults))

            limit = math.floor(self.stock1.real_time_price * self.mg_error_allow)
            lin_win_count = 0
            poly_win_cout = 0
            for lin_diff in linear_diff_array:
                if abs(lin_diff) <= limit:
                    lin_win_count += 1
            for poly_diff in poly_diff_array:
                if abs(poly_diff) <= limit:
                    poly_win_cout += 1
            linear_win_percentage = 100 * (lin_win_count/len(actual))
            self.linResults.append(linear_win_percentage)
            polynomial_win_percentage = 100 * (poly_win_cout/len(actual))
            self.polyResults.append(polynomial_win_percentage)

            print(f"======================================================================")
            print()
            print(f"Accuracy Testing for {self.stock1.ticker} - Close")
            print()
            print("Allowed a Margin of Error - {:2f} - {:2f}".format(self.mg_error_allow, limit))
            print()
            print("Linear Regression Model Accuracy - {:.3f}%".format(linear_win_percentage))
            print()
            print("Polynomial Regression Model Accuracy - {:.3f}%".format(polynomial_win_percentage))
            print()
            print("======================================================================")
        
        def runTest3(self):
            stock1LinearModel = self.stock1.linModel(self.stock1.low_data)
            stock1PolyModel = self.stock1.polyModel(self.stock1.low_data)
            x = stock1PolyModel.getX()
            stock1LinResults = list(map(stock1LinearModel.modelFunc, x))
            stock1PolyResults = list(map(stock1PolyModel.modelFunc, x))
            actual = self.stock1.low_data
            linear_diff_array = np.subtract(np.array(actual),np.array(stock1LinResults))
            poly_diff_array = np.subtract(np.array(actual),np.array(stock1PolyResults))

            limit = math.floor(self.stock1.real_time_price * self.mg_error_allow)
            lin_win_count = 0
            poly_win_cout = 0
            for lin_diff in linear_diff_array:
                if abs(lin_diff) <= limit:
                    lin_win_count += 1
            for poly_diff in poly_diff_array:
                if abs(poly_diff) <= limit:
                    poly_win_cout += 1
            linear_win_percentage = 100 * (lin_win_count/len(actual))
            self.linResults.append(linear_win_percentage)
            polynomial_win_percentage = 100 * (poly_win_cout/len(actual))
            self.polyResults.append(polynomial_win_percentage)

            print(f"======================================================================")
            print()
            print(f"Accuracy Testing for {self.stock1.ticker}  - Low")
            print()
            print("Allowed a Margin of Error - {:2f} - {:2f}".format(self.mg_error_allow, limit))
            print()
            print("Linear Regression Model Accuracy - {:.3f}%".format(linear_win_percentage))
            print()
            print("Polynomial Regression Model Accuracy - {:.3f}%".format(polynomial_win_percentage))
            print()
            print("======================================================================")

        def runTest4(self):
            stock1LinearModel = self.stock1.linModel(self.stock1.high_data)
            stock1PolyModel = self.stock1.polyModel(self.stock1.high_data)
            x = stock1PolyModel.getX()
            stock1LinResults = list(map(stock1LinearModel.modelFunc, x))
            stock1PolyResults = list(map(stock1PolyModel.modelFunc, x))
            actual = self.stock1.high_data
            linear_diff_array = np.subtract(np.array(actual),np.array(stock1LinResults))
            poly_diff_array = np.subtract(np.array(actual),np.array(stock1PolyResults))

            limit = math.floor(self.stock1.real_time_price * self.mg_error_allow)
            lin_win_count = 0
            poly_win_cout = 0
            for lin_diff in linear_diff_array:
                if abs(lin_diff) <= limit:
                    lin_win_count += 1
            for poly_diff in poly_diff_array:
                if abs(poly_diff) <= limit:
                    poly_win_cout += 1
            linear_win_percentage = 100 * (lin_win_count/len(actual))
            self.linResults.append(linear_win_percentage)
            polynomial_win_percentage = 100 * (poly_win_cout/len(actual))
            self.polyResults.append(polynomial_win_percentage)

            print(f"======================================================================")
            print()
            print(f"Accuracy Testing for {self.stock1.ticker}  - High")
            print()
            print("Allowed a Margin of Error - {:2f} - {:2f}".format(self.mg_error_allow, limit))
            print()
            print("Linear Regression Model Accuracy - {:.3f}%".format(linear_win_percentage))
            print()
            print("Polynomial Regression Model Accuracy - {:.3f}%".format(polynomial_win_percentage))
            print()
            print("======================================================================")

        def runAllTests(self):
            self.runTest1()
            self.runTest2()
            self.runTest3()
            self.runTest4()

        def getLinearResults(self):
            return self.linResults
        
        def getPolyResults(self):
            return self.polyResults


tester1 = StockTester(stock=tester, margin_error=.05)
tester1.runAllTests()

#TO EXPORT STOCK DATA INTO CSV - SEPARATE NOT ALL AT ONCE
# tester1 = StockTester(stock=tester, margin_error = .01)
# tester1.runAllTests()

# tester2 = StockTester(stock=tester, margin_error = .02)
# tester2.runAllTests()

# tester3 = StockTester(stock=tester, margin_error = .03)
# tester3.runAllTests()

# tester4 = StockTester(stock=tester, margin_error = .04)
# tester4.runAllTests()

# tester5 = StockTester(stock=tester, margin_error = .05)
# tester5.runAllTests()

# linear1 = tester1.getLinearResults()
# polynomial1 = tester1.getPolyResults()

# linear2 = tester2.getLinearResults()
# polynomial2 = tester2.getPolyResults()

# linear3 = tester3.getLinearResults()
# polynomial3 = tester3.getPolyResults()

# linear4 = tester4.getLinearResults()
# polynomial4 = tester4.getPolyResults()

# linear5 = tester5.getLinearResults()
# polynomial5 = tester5.getPolyResults()

# data = [linear1, polynomial1,linear2, polynomial2,linear3, polynomial4,linear4, polynomial4,linear5, polynomial5]
# export_data = zip_longest(*data, fillvalue = '')
# with open('temp.csv', 'w', encoding="ISO-8859-1", newline='') as file:
#       write = csv.writer(file)
#       write.writerow(("Linear - 1% ", "Polynomial - 1%","Linear - 2% ", "Polynomial - 2%","Linear - 3% ", "Polynomial - 3%","Linear - 4% ", "Polynomial - 4%","Linear - 5% ", "Polynomial - 5%"))
#       write.writerows(export_data)
