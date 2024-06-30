import pandas as pd
from os import listdir


class Data():
    def __init__(self) -> None:
        pass
    
    def get_city(self, address):
        return address.split(',')[-2].strip()

    def get_data(self, folder_path):
        # Read in updated dataframe
        all_data = pd.read_csv(f"{folder_path}all_data.csv")

        #Augment data with additional columns
        # Add a month column
        all_data['Month'] = all_data['Order Date'].str[0:2]
        all_data['Month'] = all_data['Month'].astype('int32')

        # Convert columns to the correct type
        all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
        all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

        # Add a sales column
        all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

        return all_data

    def get_state(self, address):
        return address.split(',')[-1].strip().split(' ')[0]
    
    def merge(self, folder_path):
        # Merge the 12 months of sales data into a single CSV file
        # df = pd.read_csv(f'{folder_path}Sales_April_2019.csv')
        files = [file for file in listdir(folder_path)]

        all_months_data = pd.DataFrame()
        for file in files:
            if file.__contains__("Sales_"):
                df = pd.read_csv(f'{folder_path}{file}')
                all_months_data = pd.concat([all_months_data, df])

        # Clean data
        nan_df = all_months_data[all_months_data.isna().any(axis=1)]
        if len(nan_df.iloc[:, 0]) != 0:
            all_months_data = all_months_data.dropna(how='all')
        
        all_months_data = all_months_data[all_months_data['Order Date'].str[0:2] != 'Or']

        # Add a city column
        # Use .apply()
        all_months_data['City'] = all_months_data['Purchase Address'].apply(lambda x: f"{self.get_city(x)} ({self.get_state(x)})")
        # print(all_months_data.head())

        all_months_data.to_csv(f"{folder_path}all_data.csv", index=False)
