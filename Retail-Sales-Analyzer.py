import pandas as pd
import matplotlib.pyplot as plt

class RetailSalesAnalyzer:
    def __init__(self):
        self.data = pd.read_csv("sales_data.csv")
        self.data['Date'] = pd.to_datetime(self.data['Date'])

    def data_clean(self):
        self.data.dropna(inplace=True)

    def total_sales_per_product(self):
        return self.data.groupby('Product')['Sales'].sum()

    def best_selling_product(self):
        return self.total_sales_per_product().sort_values(ascending=False).index[0]

    def average_daily_sales(self):
        return self.data['Sales'].mean()

    def plot_sales_trend(self):
        self.data.groupby('Date')['Sales'].sum().plot(kind='line')
        plt.title('Sales Trend over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.show()

    def plot_sales_per_product(self):
        self.total_sales_per_product().plot(kind='bar')
        plt.title('Sales Per Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.show()


# Create an instance of RetailSalesAnalyzer
analyzer = RetailSalesAnalyzer()

print('Total Sales per product:\n', analyzer.total_sales_per_product())
print('Best Selling Product:', analyzer.best_selling_product())
print('Average Daily Sales:', analyzer.average_daily_sales())

analyzer.plot_sales_per_product()
analyzer.plot_sales_trend()
