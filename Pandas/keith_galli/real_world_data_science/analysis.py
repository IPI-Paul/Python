from glob import glob
from charts import Charts
from data import Data
from pandas import to_datetime, DataFrame
from itertools import combinations
from collections import Counter
from numpy import arange
import math


class Analysis(Charts, Data):
    def __init__(self, *args, **kwargs):
        super(Analysis, self).__init__(*args, **kwargs)

    # What was the best month for sales? How much was earned that month?
    def question_1(self, folder_path):
        # print(all_data.groupby('Month').sum())
        all_data = self.get_data(folder_path)
        results = all_data.groupby(['Month', 'Product']).sum().loc[:, ['Quantity Ordered', 'Price Each', 'Sales']].groupby('Month').sum()
        xticks = months = range(1, 13)  
        digits = len(str(results['Sales'].max())) - round(len(str(results['Sales'].max())) / 2.5, 0)
        yticks = arange(0, results['Sales'].max(), math.pow(10 if results['Sales'].max() > 10 else 1, digits))
        ylabels = [f"{int(x):,}" for x in yticks]
        self.bar_chart(results['Sales'], months, title="Best Month for Sales\n", xlabel='Month Number', ylabel=['Sales in USD ($)'], 
                       xticks=xticks, yticks=yticks, ylabels=ylabels, left=0.2, right=0.87)
    
    # What city had the highest number of sales?
    def question_2(self, folder_path):
        all_data = self.get_data(folder_path)
        results = all_data.groupby(['City', 'Product']).sum().loc[:, ['Quantity Ordered', 'Price Each', 'Sales']].groupby('City').sum().sort_values('Sales', ascending=False)
        # cities = [city for city, df in all_data.groupby('City')]
        cities = [city for city in results.reset_index()['City']]
        digits = len(str(results['Sales'].max())) - round(len(str(results['Sales'].max())) / 2.5, 0)
        yticks = arange(0, results['Sales'].max(), math.pow(10 if results['Sales'].max() > 10 else 1, digits))
        ylabels = [f"{int(x):,}" for x in yticks]
        self.bar_chart(results['Sales'], cities, title="Highest Number of Sales by City\n\n", xlabel='City Name', ylabel=['Sales in USD ($)'], 
                       yticks=yticks, ylabels=ylabels, left=0.2, right=0.89, bottom=0.3, top=0.85, rotation='vertical')
    
    # What time should we display advertisements to maximize likelihood of customers buying product?
    def question_3(self, folder_path):
        all_data = self.get_data(folder_path)
    
        # Convert Order Date into a datetime object
        all_data['Order Date'] = to_datetime(all_data['Order Date'], format='mixed', utc=True)

        all_data['Hour'] = all_data['Order Date'].dt.hour
        all_data['Minute'] = all_data['Order Date'].dt.minute
        xticks = hours = [hour for hour, df in all_data.groupby('Hour')]
        results = all_data.groupby('Hour').count()
        self.line_chart(results, hours, title="Peak Advertisement Time\n\n", xlabel="Hour", ylabel=["Number of Orders"], xticks=xticks, top=0.8)
    
    # What products are most often sold together?
    def question_4(self, folder_path):
        all_data = self.get_data(folder_path)
        df = all_data[all_data['Order ID'].duplicated(keep=False)]

        # Create grouped column
        df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

        df = df[['Order ID', 'Grouped']].drop_duplicates()

        combined = []
        counts = []
        labels = {}

        for i in range(2, 6):
            tooltips = {}
            count = Counter()
            for row in df['Grouped']:
                row_list = row.split(',')
                count.update(Counter(combinations(row_list, i)))

            for key, value in count.most_common(20):
                if value != 1:
                    combined += [i]
                    counts += [value]
                    tooltips.update({value: key})

            labels.update({i: tooltips})
        combined_list = DataFrame({"combined": combined, "counts": counts})
        results = combined_list["counts"]
        xvalues = combined_list["combined"]

        digits = len(str(results.max())) - round(len(str(results.max())) / 2.5, 0)
        yticks = arange(0, results.max(), math.pow(10, digits))
        ylabels = [f"{int(x):,}" for x in yticks]
        digits = len(str(xvalues.max())) - round(len(str(xvalues.max())) / 2.5, 0)
        xticks = arange(0, xvalues.max() + 1,  math.pow(10 if xvalues.max() > 10 else 1, digits))
        xlabels = [f"{int(x):,}" for x in xticks]

        self.scatter_plot(results, xvalues, tooltips=labels, title="Products Most Often Sold Together\n\n\n\n", xlabel="Combined Number", ylabel=["Occurence Count"], 
                          xticks=xticks, yticks=yticks, xlabels=xlabels, ylabels=ylabels, right=0.84, top=0.75)
    
    # What product sold the most? Why do you think it sold the most?
    def question_5(self, folder_path):
        all_data = self.get_data(folder_path)
        product_group = all_data.groupby('Product')
        quantity_ordered = product_group.sum()['Quantity Ordered'].sort_values(ascending=False)
        
        # products = [product for product, df in product_group]
        products = [product for product in quantity_ordered.reset_index()['Product']]
        prices = all_data.groupby('Product')['Price Each'].mean()
        prices = prices.reindex(index=products) #.reset_index()
        self.bar_chart(quantity_ordered, products, secondary=prices, title="Sales by Product\n\n\n", ylabel=["Quantity Ordered", "Price ($)"], 
                       xlabel="Product", bottom=0.45, top=0.8, rotation='vertical')
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = Analysis()
    folder_path = "../../../../../Source Files/csv/"
    if glob(f"{folder_path}all_data.csv") != 0:
        win.merge(folder_path)
    win.question_5(folder_path)
    win.show()