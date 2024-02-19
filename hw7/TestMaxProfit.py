from max_profit import price_to_profit, max_profit_brute, max_profit, max_profit_crossing
import unittest, random

class TestPriceToProfit(unittest.TestCase):
    # Include at least one non-pdf test (remember the docstring)
    def test_main(self):
        L = [100, 105, 97, 200, 150]   
        self.assertEqual(price_to_profit(L),[0, 5, -8, 103, -50])
    
class TestMaxProfitCrossing(unittest.TestCase):
    def test_left(self):
        #Return correct price for buy/sell in left half
        L = price_to_profit([50, 45, 107, 105, 200, 250])
        self.assertEqual(max_profit_crossing(L, 0, len(L) - 1, (len(L) -1) // 2, 'pa'), 62)
    def test_right(self):
        #Returns correct profit for buy/sell in right half
        L = price_to_profit([50, 45, 107, 105, 200, 250])
        self.assertEqual(max_profit_crossing(L, 0, len(L) - 1, (len(L) -1) // 2, 'pb'), 143)
    def test_crossing(self):
        #Returns correct profit for buy left/sell right
        L = price_to_profit([50, 45, 107, 105, 200, 250])
        self.assertEqual(max_profit_crossing(L, 0, len(L) - 1, (len(L) -1) // 2, 'pc'), 205)

class TestMaxProfit(unittest.TestCase):
    def test_min_max(self):
        L1=[1,2,4,5,1,-8,5,-36,2,4,32,13]
        median = (len(L1) - 1) // 2
        self.assertEqual(max_profit_crossing(L1, left = 0, right = len(L1) - 1, median = (len(L1) - 1) // 2), 25)
    def test_not_min_max(self):
        L1=[1,2,4,5,1,-8,5,-36,2,4,32,13]
        self.assertEqual(max_profit(L1), max_profit_brute(L1), 51)
        
    def test_random(self):
        L1 = price_to_profit([100, 105, 97, 200, 150])
        L2 = price_to_profit([50, 45, 107, 105, 200, 250])
        L3 = price_to_profit([random.randint(0, 100) for i in range(100)])
        for i in range(100):
            L3 = price_to_profit([random.randint(0, 1000) for i in range(1000)])
            self.assertEqual(max_profit_brute(L3), max_profit(L3)) 
        self.assertEqual(max_profit_brute(L1), max_profit(L1),103) 
        self.assertEqual(max_profit_brute(L2), max_profit(L2),205)

        #Tests that random lists give correct result, using brute force to verify

        # 1) define list length n. Use at least 100 items to guarantee your algorithm works,
        #    but you can use a smaller value while debugging

        # 2) for i in range 1000:
            # Create list of n random ints
            # find max profit using brute algorithm (expected result)
            # find max profit using divide-and-conquer algorithm (actual result)
            # assert that expected and actual are the same
        
    # tests from pdf and w/ provided bitcoin csvs are provided below.
    # these are unlikely to be helpful for debugging - take the time
    # to write your own above before trying to debug your code
    def test_pdf(self):
        """Tests from pdf"""
        self.assertEqual(max_profit(price_to_profit([100, 105, 97, 200, 150])), 103)

    # this requires you to be in the same director as the folder "bitcoin_prices"
    def test_bitcoin(self):
        """Tests 5 years of bitcoin"""
        ##### Import and read values from associated csvs, then check if you can become a bitcoin-optimaire
        import csv
        import os

        val_2015 = []
        val_2016 = []
        val_2017 = []
        val_2018 = []
        val_2019 = []
        val_2020 = []

        vals = [val_2015, val_2016, val_2017, val_2018, val_2019, val_2020]

        for file in os.scandir(r'./bitcoin_prices'):
            if (file.path.endswith(".csv")):
                if file.name == "2015.csv": i = 0
                elif file.name == "2016.csv": i = 1
                elif file.name == "2017.csv": i = 2
                elif file.name == "2018.csv": i = 3
                elif file.name == "2019.csv": i = 4
                elif file.name == "2020.csv": i = 5

                with open(file, 'r') as f:
                    reader = csv.reader(f)

                    lst = list(reader)[1:]
                    for j in range(len(lst)):
                        vals[i].append( float(lst[j][1].replace(",","")))


        # find the day-to-day profit list for each year
        year_profits = []
        for year in vals:
            year_profits.append([])
            year_profits[-1] = price_to_profit(year)

        # correct max profits per year, 2015-2020, rounded to ints
        max_profits = [298, 604, 18561, 4476, 9665, 24052]

        # test that max_profit returns the correct profit for each year
        for i, year in enumerate(year_profits):
            self.assertAlmostEqual(max_profit(year), max_profits[i], places=0)

unittest.main()