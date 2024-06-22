# Tutorial: https://m.youtube.com/watch?v=vmEHCJofslg
# Although tutorial uses Jupyter Notebook, I used PyCharm IDE which is now my preferred IDE on my Linux Distro
# Altered to present in an interactive environment, which also increased learning
import sys
import pandas as pd
import inspect
import re
pd.options.display.width = 0


def example1():
    df = pd.read_csv('csv/pokemon_data.csv')
    return df


def example2():
    df_xlsx = pd.read_excel('xlsx/pokemon_data.xlsx')
    return df_xlsx


def example3():
    df = pd.read_csv('txt/pokemon_data.txt', delimiter='\t')
    return df


def example4():
    dta = None
    return dta


def print_head(df):
    # head() default is 5
    print(df.head(3))


def read_headers(df):
    print(df.columns)


def read_column(df):
    print(df['Name'])
    print(df['Name'][:5])
    # does not work with to functions
    print(df.Name)
    print(df.Name[:5])
    print(df[['Name', 'Type 1', 'HP']])


def read_row(df):
    print(df.iloc[1])
    print(df.iloc[1:4])


def read_specific_location(df):
    print(df.iloc[2, 1])


def read_row_by_row(df):
    for index, row in df.iterrows():
        print(index, row)


def read_row_by_row_column(df):
    for index, row in df.iterrows():
        print(index, row['Name'])


def filter_rows_by_column(df):
    print(df.loc[df['Type 1'] == 'Fire'])


def describe_structure(df):
    print(df.describe())


def sort_by_column(df):
    print(df.sort_values('Name', ascending=True))


def sort_by_columns(df):
    print(df.sort_values(['Type 1', 'Name'], ascending=[False, True]))


def add_total_column_in_memory(df):
    df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
    print(df.head(5))


def drop_total_column_from_memory(df):
    df = df.drop(columns=['Total'])
    print(df.head(5))


def add_total_column_iloc(df):
    df['Total'] = df.iloc[:, 4:10].sum(axis=1)
    print(df.head(5))


def reorder_columns(df):
    cols = list(df.columns.values)
    df = df[cols[0:4] + [cols[-1]] + cols[4:-1]]
    print(df.head(5))


def save_to_csv(df):
    df.to_csv('csv/modified.csv')


def save_to_csv_excl_row_names(df):
    df.to_csv('csv/modified.csv', index=False)


def save_to_excel(df):
    # Does Not Work!!
    df.to_excel('xlsx/modified.xlsx', index=False)


def save_to_tsv(df):
    df.to_csv("tab/modified.tab", index=False, sep="\t")


def filter_rows_multiple_conditions(df):
    print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')], "\n")
    print(df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')])


def filter_rows_multiple_conditions_reset_index(df):
    print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')].reset_index(), "\n\nOr\n")
    print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')].reset_index(drop=True, inplace=True))


def filter_on_rows_containing(df):
    print(df.loc[df['Name'].str.contains('Mega')])


def filter_out_rows_containing(df):
    print(df.loc[~df['Name'].str.contains('Mega')])


def filter_on_rows_containing_regex(df):
    print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)], '\n')
    print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])


def conditional_changes(df):
    df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
    print(df)
    df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = True
    print(df)


def multiple_conditional_changes(df):
    df.loc[df.iloc[:, 4:10].sum(axis=1) > 500, ['Generation', 'Legendary']] = 'TEST VALUE'
    print(df)
    df.loc[df.iloc[:, 4:10].sum(axis=1) > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
    print(df)


def group_by_aggregate_statistics(df):
    # count, mean or sum (does not include empties or NaNs)
    print(df.groupby(['Type 1']).mean(), '\n')
    print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False), '\n')
    df['Count'] = 1
    print(df.groupby(['Type 1', 'Type 2']).count()['Count'])


def read_file_chunks(dta):
    for df in pd.read_csv('csv/pokemon_data.csv', chunksize=5):
        print("CHUNK DF")
        print(df, '\n')
        df['Count'] = 1
        results = df.groupby(['Type 1', 'Type 2']).count()['Count']
        if dta is None:
            dta = results
        else:
            dta = pd.concat([dta, results])
    print(dta.groupby(['Type 1', 'Type 2']).sum())


user_input = None
outputs = ["", "print_head", "read_headers", "read_column", "read_row", "read_specific_location", "read_row_by_row",
           "read_row_by_row_column", "filter_rows_by_column", "describe_structure", "sort_by_column", "sort_by_columns",
           "add_total_column_in_memory", "drop_total_column_from_memory", "add_total_column_iloc", "reorder_columns",
           "save_to_csv", "save_to_csv_excl_row_names", "save_to_excel", "save_to_tsv",
           "filter_rows_multiple_conditions", "filter_rows_multiple_conditions_reset_index",
           "filter_on_rows_containing", "filter_out_rows_containing", "filter_on_rows_containing_regex",
           "conditional_changes", "multiple_conditional_changes", "group_by_aggregate_statistics", "read_file_chunks"]
message = """
Please select an exercise number and output type (i.e 1, 1)
h) Help
Exercises:
1) Dataframe from csv   2) Dataframe from xlsx  3) Dataframe from txt (tab separated values) 
Output types    
1) Print top 3 rows     2) Print Headers        3) Print Column(s)
4) Print Row(s)         5) Print Row n Column n 6) Print Row by Row
7) Print Row by Row with Specified Column       8) Filter Rows by Specified Column Value
9) Describe the Data Frame Structure            10) Sort Values by Specified Column
11) Sort Values by Specified Columns            12) Add Total Column in Memory that Adds up All Others
13) Drop Total Column from Memory and Re-Assign 14) Add Total Column Using iloc to Select and Sum Up
15) Re-Order Columns moving Total Column        16) Save Data Frame to CSV file
17) Save Data Frame to CSV file No Row Names    18) Save Data Frame to XLSX file
19) Save Data Frame to TSV file No Row Names    20) Filter using Multiple Conditions
21) Multi Filter Reset Row Names                22) Filter on Rows Containing a String Value
23) Filter out Rows Containing a String Value   24) Filter on Rows Containing a Regular Expression (import re)
25) Making Column Changes                       26) Making Multiple Column Changes
27) Aggregate & Display Mean by Specific Column 28) Load Data Frame in Chunks *** use 4, 28 ***
> """
while user_input not in ['', 'q']:
    user_input = input(message if user_input is None else "> ")
    do = user_input.replace(" ", "").split(",")
    if user_input in ['', 'q']:
        print("All done, bye ;D")
        continue
    elif user_input == 'h':
        user_input = None
        continue
    elif len(do) < 2:
        print("The entry does not meet the requirement (i.e 1, 2)")
        continue
    elif not do[0].isnumeric() or not do[1].isnumeric():
        print("Please make sure both values are numeric")
        continue
    try:
        obj = [obj for name, obj in inspect.getmembers(sys.modules[__name__])
               if (inspect.isfunction(obj) and
                   name == outputs[int(do[1])] and
                   obj.__module__ == __name__)]
        print(''.join(inspect.getsource(obj[0]).splitlines(True)[1:]))
        if do[1] not in ["13", "15", "16", "17"]:
            df = eval(f"""example{int(do[0])}()""")
        eval(f"{outputs[int(do[1])]}")(df)
    except IndexError as err:
        print(err)
        user_input = None
        continue
