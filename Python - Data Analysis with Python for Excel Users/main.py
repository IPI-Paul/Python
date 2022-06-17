# Tutorial: https://m.youtube.com/watch?v=WcDaZ67TVRo
# Although tutorial uses Jupyter Notebook, I used PyCharm IDE which is now my preferred IDE on my Linux Distro
# Altered to present in an interactive environment, which also increased learning
import pandas as pd
import numpy as np
import sys
import inspect
import re
import matplotlib.pyplot as plt
pd.options.display.width = 0


# 0 creating an array
def numpy_array():
    data = np.array([[1, 4], [2, 5], [3, 6]])
    return data


# 1 creating a dataframe
def dataframe_from_array(data):
    df = pd.DataFrame(data=data, index=['row1', 'row2', 'row3'], columns=['col1', 'col2'])
    return df


# 2 creating an array with list shape
def array_list_shape():
    data = [[11, 4], [2, 5], [3, 6]]
    return data


# 3 lists used for the example
def us_states_and_populations():
    states = ['California', 'Texas', 'Florida', 'New York']
    population = [39613493, 29730311, 21944577, 19299981]
    return states, population


# 4 Storing lists within a dictionary
def states_and_population_dictionary():
    states, population = us_states_and_populations()
    dict_states = {'States': states, 'Population': population}
    return dict_states


# 5 Creating the dataframe
def population_dataframe(dict_states):
    df_population = pd.DataFrame(dict_states)
    return df_population


# 6 reading from a csv file
def import_csv():
    df_exams = pd.read_csv('csv/StudentsPerformance.csv')
    return df_exams


# 7 display only the first 5 rows
def first_5_rows(df_exams):
    df_head = df_exams.head()
    return df_head


# 8 display the last 5 rows
def last_5_rows(df_exams):
    df_tail = df_exams.tail()
    return df_tail


# 9 show first n rows in dataframe
def show_first_n_rows(df_exams, n):
    df_head = df_exams.head(n)
    return df_head


# 10 show last n rows in dataframe
def show_last_n_rows(df_exams, n):
    df_tail = df_exams.tail(n)
    return df_tail


# 11 getting access to the shape attribute
def access_shape_attribute(df_exams):
    df_shape = df_exams.shape
    return df_shape


# 12 display n rows using shape attribute
def n_rows_shape_attribute(df_exams, n):
    pd.set_option('display.max_rows', n)
    df = df_exams
    return df


# 13 getting access to the index attribute
def access_index_attribute(df_exams):
    df_index = df_exams.index
    return df_index


# 14 getting access to the columns attribute
def access_columns_attribute(df_exams):
    df_columns = df_exams.columns
    return df_columns


# 15 get the data types of each column
def get_column_data_types(df_exams):
    df_data_types = df_exams.dtypes
    return df_data_types


# 16 using the info method of dataframe
def use_info_method(df_exams):
    df_info = df_exams.info()
    return df_info


# 17 using the describe method of dataframe
def use_describe_method(df_exams):
    df_described = df_exams.describe()
    return df_described


# 18 obtaining the length of the dataframe (number of columns and rows)
def number_of_columns(df_exams):
    columns = len(df_exams.columns)
    rows = len(df_exams)
    return f"Columns: {columns}\tRows: {rows}"


# 19 obtaining the maximum value of the dataframe
def max_value(df_exams):
    min_dataframe = max(df_exams)
    max_index = max(df_exams.index)
    return f"Maximum of Data Frame: {min_dataframe}\tMaximum of Index Column: {max_index}"


# 20 obtaining the minimum value of the dataframe
def min_value(df_exams):
    min_dataframe = min(df_exams)
    min_index = min(df_exams.index)
    return f"Minimum of Data Frame: {min_dataframe}\tMinimum of Index Column: {min_index}"


# 21 obtaining the object type of the dataframe
def dataframe_type(df_exams):
    df_type = type(df_exams)
    return f"{df_type}"


# 22 rounding the values of the dataset
def round_values(df_exams):
    df_rounded = round(df_exams, 2)
    return df_rounded


# 23 select a column with [] (preferred way to select a column)
def select_column_preferred(df_exams):
    df_column = df_exams['gender']
    return df_column


# 24 check out the datatype of a column
def get_column_datatype(df_exams):
    df_type = type(df_exams['gender'])
    return f"{df_type}"


# 25 series: attributes and methods
def get_series_index_attribute(df_exams):
    df_index = df_exams['gender'].index
    return df_index


# 26 series: attributes and methods
def get_series_head_attribute(df_exams):
    df_head = df_exams['gender'].head()
    return df_head


# 27 select a column with . notation
def get_column_dot_notated(df_exams):
    df_column = df_exams.gender
    return df_column


# 28 select a spaced column name
def get_spaced_column_name(df_exams):
    # neither df_exams.math score nor df_exams.math_score will not work for column math score
    df_column = df_exams['math score']
    return df_column


# 29 select 2 columns using [[]]
def select_2_or_more_columns(df_exams):
    df_columns = df_exams[['gender', 'math score']]
    return df_columns


# 30 display datatype of result when 2 or more columns are selected
# [] 1 pair of brackets returns a series, and [[]] returns a dataframe
def multi_column_datatype(df_exams):
    df_type = type(df_exams[['gender', 'math score']])
    return f"{df_type}"


# 31 select 2 columns using [[]] and order columns
def select_2_or_more_columns_in_order(df_exams):
    df_columns = df_exams[['gender', 'writing score', 'math score', 'reading score']]
    return df_columns


# 32 Add new column to dataframe with scalar value
def add_column_with_scalar_value(df_exams):
    df_exams['language score'] = 70
    return df_exams


# 33 create an array of 1000 elements
def create_array_of_1000():
    language_score = np.arange(0, 1000)
    return language_score


# 34 length of the array
def length_of_array(language_score):
    array_length = len(language_score)
    return array_length


# 35 adding a new column to dataframe with an array
def new_column_from_array(language_score, df_exams=import_csv()):
    df_exams['language score'] = language_score
    df_new = df_exams
    return df_new


# 36 create random integer numbers between 1 and 100
def random_integers_1_100():
    int_language_score = np.random.randint(1, 100, size=1000)
    return int_language_score


# 37 min value inclusive and high value exclusive
def inclusive_exclusive_values(int_language_score):
    min_value = min(int_language_score)
    max_value = max(int_language_score)
    return f"Minimum Value: {min_value}\tMaximum Value: {max_value}"


# 38 adding a new column to dataframe with an array
def new_column_from_array_random(int_language_score, df_exams=import_csv()):
    df_exams['language score'] = int_language_score
    df_new = df_exams
    return df_new


# 39 create random float numbers between 1 and 100
def create_random_float_1_100():
    array_random_float = np.random.uniform(1, 100, 1000)
    return array_random_float


# 40 select a column and calculate total sum
def sum_up_column(df_exams):
    df_total = df_exams['math score'].sum()
    return df_total


# 41 count, mean, std, max and min
def dataframe_math_operations(df_exams):
    df_count = df_exams['math score'].count()
    df_mean = df_exams['math score'].mean()
    df_std = df_exams['math score'].std()
    df_min = df_exams['math score'].min()
    df_max = df_exams['math score'].max()
    return f"Count: {df_count}\tMean: {df_mean}\tStd: {df_std}\tMin: {df_min}\tMax: {df_max}"


# 42 use the describe method on current dataframe
def pass1():
    pass


# 43 calculating the sum in a row without iloc
def sum_of_row(df_exams):
    df_scores = df_exams['math score'] + df_exams['reading score'] + df_exams['writing score']
    return df_scores


# 44 calculating the average score and assigning the result to a new column
def column_from_average_of_columns(df_exams):
    df_exams['average'] = (df_exams['math score'] + df_exams['reading score'] + df_exams['writing score']) / 3
    return df_exams


# 45 rounding numeric columns to 2 decimal places
def round_to_2(df_exams):
    df_rounded = round(df_exams, 2)
    return df_rounded


# 46 counting gender elements by category
def count_column_by_category(df_exams, column_name):
    gender_count_by_category = df_exams[column_name].value_counts()
    return gender_count_by_category


# 47 return the relative frequency (divide all values by the sum of values)
def relative_frequency(df_exams, column_name):
    gender_relative_frequency = df_exams[column_name].value_counts(normalize=True).round(2)
    return gender_relative_frequency


# 48 sort by one or more columns (multiple columns in list form)
def sort_by_column(df_exams, column_name):
    df_sorted = df_exams.sort_values(by=column_name)
    return df_sorted


# 49 sort descending by one or more columns (multiple columns in list form)
def sort_by_column_descending(df_exams, column_name):
    df_sorted = df_exams.sort_values(by=column_name, ascending=False)
    return df_sorted


# 50 sort descending by multiple columns and update dataframe
def sort_update_column_descending(df_exams, column_name):
    df_exams.sort_values(by=column_name, ascending=False, inplace=True)
    return df_exams


# 51 sort descending with a key function (is case-insensitive)
def sort_key_descending(df_exams, column_name):
    df_sorted = df_exams.sort_values(column_name, ascending=True, key=lambda col: col.str.lower())
    return df_sorted


# 52 read and show gdp.csv dataset
def read_gdp_csv():
    df_gdp = pd.read_csv('csv/gdp.csv')
    return df_gdp


# 53 reshape gdp dataframe with .pivot()
def reshape_gdp_pivot(df_gdp):
    df_pivot = df_gdp.pivot(index="year", columns="country", values="gdppc")
    return df_pivot


# 54 read and show supermarket_sales.xlsx dataset
def read_supermarket_sales_xlsx():
    df_sales = pd.read_excel("xlsx/supermarket_sales.xlsx")
    return df_sales


# 55 make a pivot table and add an aggregate function
def pivot_sales_aggregated(df_sales, row_columns, func):
    df_pivot = df_sales.pivot_table(index=row_columns, aggfunc=func).round(2)
    return df_pivot


# 56 make a pivot table, add an aggregate function and select some columns
def pivot_sales_aggregated_columns(df_sales, row_columns, func, value_columns):
    df_pivot = df_sales.pivot_table(index=row_columns, values=value_columns, aggfunc=func).round(2)
    return df_pivot


# 57 make a pivot table that says how much specified column spends in each specification
def pivot_sales_columns_aggregated_by(df_sales, row_columns, func, value_columns, by_columns):
    df_pivot = df_sales.pivot_table(index=row_columns, columns=by_columns, values=value_columns, aggfunc=func).round(2)
    return df_pivot


# 58 read population_total.csv file
def read_population_total_csv():
    df_population_raw = pd.read_csv("csv/population_total.csv")
    return df_population_raw


# 59 dropping null values
def drop_null_values(df_population_raw):
    df_population_raw.dropna(inplace=True)
    return df_population_raw


# 60 make a pivot table from population dataset
def pivot_population_total(df_population_raw, row_columns, by_columns, value_columns):
    df_pivot = df_population_raw.pivot(index=row_columns, columns=by_columns, values=value_columns)
    return df_pivot


# 61 selecting countries from population pivot
def select_population_pivot_countries(df_population_raw, row_columns, by_columns, value_columns, col_num, by_values):
    df_pivot = df_population_raw.pivot(index=row_columns, columns=by_columns, values=value_columns)
    df_pivot = df_pivot[value_columns[int(col_num[0])]][by_values]
    return df_pivot


# 62 line plot
def line_plot_population_filter(df_population_raw, row_columns, by_columns, value_columns, col_num, by_values,
                                file_path=[]):
    df_pivot = select_population_pivot_countries(df_population_raw, row_columns, by_columns, value_columns, col_num,
                                                 by_values)
    df_pivot.plot(kind='line', xlabel='Year', ylabel='Population', title='Population (1955-2020)', figsize=(8, 4))
    if len(file_path) > 0:
        if file_path[0] == "png":
            plt.savefig(file_path[1])
        else:
            df_pivot.to_excel(file_path[1])
    return "Show Plot"


# 63 bar plot (selecting only one year 2020)
def bar_plot_population_filter(df_population_raw, row_columns, by_index, by_columns, value_columns, col_num, by_values,
                                file_path=[]):
    df_pivot = select_population_pivot_countries(df_population_raw, row_columns, by_columns, value_columns, col_num,
                                                 by_values)
    df_pivot = df_pivot[df_pivot.index.isin([int(x) for x in by_index])]
    if len(by_index) == 1:
        df_pivot = df_pivot.T
        x_label = "Country"
    else:
        x_label = "Year"
    df_pivot.plot(kind='bar', xlabel=x_label, ylabel='Population', title=f'Population {min(by_index)} to '
                                                                         f'{max(by_index)}')
    if len(by_index) == 1:
        plt.subplots_adjust(bottom=0.25, right=0.75)
    else:
        plt.subplots_adjust(bottom=0.175, right=0.75)
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.4, 0.6))
    if len(file_path) > 0:
        if file_path[0] == "png":
            plt.savefig(file_path[1])
        else:
            df_pivot.to_excel(file_path[1])
    return "Show Plot"


# 64 pie chart (like bar plot)
def pie_chart_population_filter(df_population_raw, row_columns, by_index, by_columns, value_columns, col_num, by_values,
                                file_path=[]):
    df_pivot = select_population_pivot_countries(df_population_raw, row_columns, by_columns, value_columns, col_num,
                                                 by_values)
    df_pivot = df_pivot[df_pivot.index.isin([int(x) for x in by_index])]
    if len(by_index) == 1:
        df_pivot = df_pivot.T
    df_pivot = df_pivot.rename(columns={int(by_index[0]): by_index[0]})
    df_pivot.plot(kind='pie', y=by_index[0], title=f'Population {min(by_index)}')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.175)
    plt.legend(bbox_to_anchor=(.95, 0.125))
    if len(file_path) > 0:
        if file_path[0] == "png":
            plt.savefig(file_path[1])
        else:
            df_pivot.to_excel(file_path[1])
    return "Show Plot"


# 65 save current plot
def save_plot(df_population_raw, row_columns, by_index, by_columns, value_columns, col_num, by_values, plot_type,
              file_name):
    file_path = ["png", f"png/{file_name[0]}.png"]
    if plot_type[0] == 'line':
        line_plot_population_filter(df_population_raw, row_columns, by_columns, value_columns, col_num, by_values,
                                    file_path)
    elif plot_type[0] == 'bar':
        bar_plot_population_filter(df_population_raw, row_columns, by_index, by_columns, value_columns, col_num,
                                   by_values, file_path)
    else:
        pie_chart_population_filter(df_population_raw, row_columns, by_index, by_columns, value_columns, col_num,
                                    by_values, file_path)
    return "Show Plot"


# 66 export pivot table and chart to excel
def export_table_chart_to_excel(df_population_raw, row_columns, by_index, by_columns, value_columns, col_num, by_values,
                                plot_type, file_name):
    file_path = ["xlsx", f"xlsx/{file_name[0]}.xlsx"]
    if plot_type[0] == 'line':
        line_plot_population_filter(df_population_raw, row_columns, by_columns, value_columns, col_num, by_values,
                                    file_path)
    elif plot_type[0] == 'bar':
        bar_plot_population_filter(df_population_raw, row_columns, by_index, by_columns, value_columns, col_num,
                                   by_values, file_path)
    else:
        pie_chart_population_filter(df_population_raw, row_columns, by_index, by_columns, value_columns, col_num,
                                    by_values, file_path)
    return "Show Plot"


# showing the dataframe
def show(*args):
    lines = []
    rem = [i for i, _ in enumerate(args) if _.__contains__(',')]
    rem = rem[-1] - len(args) if len(rem) > 0 else None
    for idx, _ in sorted(enumerate(args if len(args) < 2 else args[:rem]), reverse=True):
        obj = [obj for name, obj in inspect.getmembers(sys.modules[__name__])
               if (inspect.isfunction(obj) and
                   name == args[idx] and
                   obj.__module__ == __name__)]
        lines.append(''.join(inspect.getsource(obj[0]).splitlines(True)[1:-1]))
    print(''.join(lines))
    try:
        result = \
            eval(f"{args[0]}({args[1]}({args[2] + '()' if len(args) > 2 and not args[2].__contains__(',') else ''}) \
        {args[rem] if not rem is None else ''})" if len(args) > 1 else f"{args[0]}()")
        if re.compile("<class '(.*)'>").match(f"{type(result)}").groups()[0] == 'str' and result == "Show Plot":
            return plt.show()
        print(re.compile("<class '(.*)'>").match(result).groups()[0] if f"{result}".__contains__("<class") else result,
              "\n")
    except Exception as err:
        print(f"{err.args[0]} was not a recognised parameter!")


user_input = None
examples = [[1, 0], [1, 2], [5, 4], [6], [7, 6], [8, 6], [9, 6], [10, 6], [11, 6], [12, 6], [13, 6], [14, 6], [15, 6],
            [16, 6], [17, 6], [18, 6], [19, 6], [20, 6], [21, 6], [22, 6], [23, 6], [24, 6], [25, 6], [26, 6], [27, 6],
            [28, 6], [29, 6], [30, 6], [31, 6], [32, 6], [33], [34, 33], [35, 33], [36], [37, 36], [38, 36], [39],
            [40, 6], [41, 6], [17, 38, 36], [43, 38, 36], [44, 38, 36], [45, 44, 6], [46, 6], [47, 6], [48, 6], [49, 6],
            [50, 6], [51, 6], [52], [53, 52], [54], [55, 54], [56, 54], [57, 54], [58], [59, 58], [60, 59, 58],
            [61, 59, 58], [62, 59, 58], [63, 59, 58], [64, 59, 58], [65, 59, 58], [66, 59, 58]]
message = """
1) Create Data Frame from a Numpy Array             2) Create Data Frame from a List Shape Array
3) Create Data Frame from Dictionary                4) Import a CSV file and display all rows
5) Import a CSV file and display 1st 5 rows         6) Import a CSV file and display last 5 rows
7) Display the first n rows (enter 7, n where n is the number of rows you want displayed)
8) Display the last n rows (enter 8, n where n is the number of rows you want displayed)
9) Display shape attribute of dataframe
10) Set number of rows to display and show (enter 10, n where n is the number of rows you want displayed)
11) Display index attribute of dataframe            12) Display columns attribute of dataframe
13) Display the Data Types of each column           14) Use the info method of dataframe
15) Use the describe method of dataframe            16) Display the length of columns and rows in dataframe
17) Display the max values of dataframe             18) Display the min values of dataframe
19) Display the object type of dataframe            20) Display rounded values of dataframe
21) Select a column using [] notation (1D Array)    22) Display the data type of column selected using []
23) Display a series result's index attribute       24) Display a series result's head attribute
25) Select a column using . notation                26) Select a spaced column name
27) Select 2 or more columns                        28) Display datatype of result when 2 or more columns selected
29) Select 2 or more columns and re-order columns   30) Add a column with a scalar value
31) Create an array of 1000 elements                32) Display the length of new array
33) Add column using array values                   34) Create an array of 1000 random numbers between 1 and 100
35) Show the Min and Max values                     36) Add column using array of random values 
37) Create an array of 1000 random float numbers    38) Calculate the total of a column
37) Create an array of 1000 random float numbers    38) Calculate the total of a column
39) Perform math operations on a column             40) Use dataframe describe method to view current state
41) Calculate the sum of specified columns          42) Create column from average of specified columns
43) Round dataframe numeric values to 2 decimals    44) Get average count by gender category (enter 44, Column Name(s))
45) Get relative frequency by category of (enter 45, Column Name(s))
46) Sort by column(s) (enter 46, Column Name(s))    47) Sort descending by column(s) (enter 47, Column Name(s))
48) Sort descending by column(s) (enter 48, Column Name(s)) and update dataframe
49) Sort by string column (enter 49, Column Name(s)) 50) Import and Display gdp.csv
51) Pivot gdp.csv by Year, Country and gdppc        52) Import and display supermarket_sales.xlsx
53) Pivot Sales and aggregate by (enter 53, Column Name(s): Function)  
54) Pivot Sales and aggregate by (enter 54, Column Name(s): Function: Value Column Name(s))  
55) Pivot Sales and aggregate by (enter 55, Column Name(s): Function: Value Column Name(s): By Column Name(s))
56) Import Population Total csv file                57) Drop null values from dataframe
58) Pivot Population Total by (enter 58, Column Name(s): By Column Name(s): Value Column Name(s))
59) Pivot Population Total by (enter 59, Column Name(s): By Column Name(s): Value Column Name(s): Filter on Column 
Number of Value Column(s): Country(ies))            
60) Line Plot from population filter (i.e. 60, year: country: population: 0: United States, India, China, Indonesia, 
Brazil)
61) Bar Plot from population filter (i.e. 61, year: 2020: country: population: 0: United States, India, China, 
Indonesia, Brazil)
62) Pie Chart from population filter (i.e. 62, year: 2020: country: population: 0: United States, India, China, 
Indonesia, Brazil)                                  
63) Save current plot to (i.e 63, year: 2020: country: population: 0: United States, India, China, Indonesia, Brazil: 
bar: bar_test)                                
64) Save current plot to Excel using(i.e 64, year: 2020: country: population: 0: United States, India, China, Indonesia, 
Brazil: bar: bar_pivot_table)
> """
methods = {}
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isfunction(obj):
        _, start_line = inspect.getsourcelines(obj)
        methods[start_line] = name
methods = [methods[key] for key in sorted(list(methods.keys()))][:-1]
while user_input not in ['', 'q']:
    user_input = input(message if user_input in [None, 'h'] else "> ")
    if user_input in ['', 'q']:
        print("All done, bye ;D")
        continue
    elif user_input == 'h':
        continue
    try:
        input_number = int(user_input if len(user_input.replace(" ", "").split(",")) == 1 else
                           user_input.replace(" ", "").split(",")[0]) - 1
    except Exception as err:
        print(err.args[0])
        continue
    if (user_input.__contains__(",") and (
            not user_input.replace(" ", "").split(",")[0].isnumeric() or
            not user_input.replace(" ", "").split(",")[1].isnumeric()) and not
            all(item in eval(f"{methods[examples[input_number][1]]}("
                             f"{methods[examples[input_number][2]] + '()' if len(examples[input_number]) > 2 else ''}"
                             f").columns") for item in
                [str(x).strip() for x in user_input.split(",", 1)[1].split(":")[0].strip().split(",")])) or \
            (not user_input.__contains__(",") and not user_input.isnumeric()):
        print("Please make sure the value is numeric, or if entering column names that all exist in dataframe!")
        continue
    try:
        if len(examples[input_number]) > 1 and not user_input.__contains__(","):
            try:
                show(*[methods[x] for x in examples[input_number]])
            except TypeError as err:
                print(err)
                continue
        elif len(examples[input_number]) > 2 and user_input.__contains__(",") and not \
                user_input.split(",")[1].split(":")[0].strip() in eval(f"{methods[examples[input_number][1]]}("
                             f"{methods[examples[input_number][2]] + '()' if len(examples[input_number]) > 2 else ''}"
                             f").columns"):
            show(*[methods[x] for x in examples[input_number]],
                 ', ' + user_input.replace(" ", "").split(",")[1])
        elif len(examples[input_number]) > 1 and user_input.__contains__(",") and not \
                user_input.split(",")[1].split(":")[0].strip() in eval(f"{methods[examples[input_number][1]]}("
                             f"{methods[examples[input_number][2]] + '()' if len(examples[input_number]) > 2 else ''}"
                             f").columns"):
            show(*[methods[x] for x in examples[input_number]],
                 ', ' + user_input.replace(" ", "").split(",")[1])
        elif len(examples[input_number]) > 1 and user_input.__contains__(","):
            show(*[methods[x] for x in examples[input_number]],
                 ", ['" +
                 "','".join(str(x).strip() for x in user_input.split(",", 1)[1].split(":")[0].strip().split(","))
                 + "']" +
                 (", ['" +
                 "','".join(str(x).strip() for x in user_input.split(",", 1)[1].split(":")[1].strip().split(","))
                 + "']" if user_input.__contains__(":") else "") +
                 (", ['" +
                 "','".join(str(x).strip() for x in user_input.split(",", 1)[1].split(":")[2].strip().split(","))
                 + "']" if len(user_input.split(",", 1)[1].split(":")) > 2 else "") +
                 (", ['" +
                 "','".join(str(x).strip() for x in user_input.split(",", 1)[1].split(":")[3].strip().split(","))
                 + "']" if len(user_input.split(",", 1)[1].split(":")) > 3 else "") +
                 (", ['" +
                 "','".join(str(x).strip() for x in user_input.split(",", 1)[1].split(":")[4].strip().split(","))
                 + "']" if len(user_input.split(",", 1)[1].split(":")) > 4 else "") +
                 (", ['" +
                 "','".join(str(x).strip() for x in user_input.split(",", 1)[1].split(":")[5].strip().split(","))
                 + "']" if len(user_input.split(",", 1)[1].split(":")) > 5 else "") +
                 (", ['" +
                 "','".join(str(x).strip() for x in user_input.split(",", 1)[1].split(":")[6].strip().split(","))
                 + "']" if len(user_input.split(",", 1)[1].split(":")) > 6 else "") +
                 (", ['" +
                 "','".join(str(x).strip() for x in user_input.split(",", 1)[1].split(":")[7].strip().split(","))
                 + "']" if len(user_input.split(",", 1)[1].split(":")) > 7 else ""))
        else:
            show(methods[examples[input_number][0]])
    except IndexError as err:
        print(err)
