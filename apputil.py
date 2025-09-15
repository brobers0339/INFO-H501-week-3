import seaborn as sns
import pandas as pd
import numpy as np


"""
Write a recursive function to compute the nth Fibonacci number (sum of previous two numbers within the series starting with 0 and 1).
The fib function is defined as follows:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2) for n > 1
The function should raise a ValueError if the input is not a non-negative integer, which will account for any invalid inputs.
"""

def fibonacci(n):
    if type(n) is int and n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    else:
        raise ValueError("Input must be a non-negative integer")
    
"""
Write a function to convert a non-negative integer to its binary representation as a string.
If the number is 0, the function will automatically return 0.
While the current number is greater than 0, add the remainer of the number when divided by 2 to the binary string and find the new number (which is the current number divided by 2 using the floor division operator (aka the divided number down)).
Once the number is 0, return the found converted binary string.
The function should raise a ValueError if the input is not a non-negative integer, which will account for any invalid inputs.
"""
def to_binary(num):
    binary_string = ""
    if type(num) is int and num >= 0:
        if num == 0:
            return "0"
        while num > 0:
            binary_string = str(num % 2) + binary_string
            num = num // 2
        return binary_string
    else:
        raise ValueError("Input must be a non-negative integer")
    

#Here we import the bellevue csv file using the following url.
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

"""
Our first task is to return a list of all column names sorted by least to greatest amount of missing values.
First, we need to remedy the gender column since we have values other than M (male), F (female), and NaN (missing).
Then, we can create a list of the column names by using the built-in tolist() function.
Finally, we return the list sorted (automatically ascending) by the sum of all missing values.
We use the index and tolist() functions since the return statement would intially return a series, including both the column name and
 number of missing values while we only need the column name (the index of the series). 
"""
def task_1():
    print(df_bellevue['gender'].unique())
    df_bellevue['gender'] = df_bellevue['gender'] \
                                .replace(['h', 'g', '?'], np.nan)
    col_list = df_bellevue.columns.tolist()
    return df_bellevue[col_list].isna().sum().sort_values().index.tolist()

    
"""
Our second task is to create a data frame with 2 columns that store each year within the 
 bellevue data frame and the number of admissions for each of those years.
First, we create an empty pandas data frame with the columns, year and total_admissions.
Next, we use the date_in column from the bellevue data frame to find the year, which is
 also the first 4 characters of date_in string and set that to the year column in the new data frame.
Then, we use the groupby function to find the total number of admissions under each year in the
 data frame, transforming the type to a size to add to the total_admissions column in the new data frame.
Finally, we drop all duplicate values in the year column so we only have one instance of each year before
 returning the final data frame including each year and their corresponding admission sums.
"""
def task_2():
    df = pd.DataFrame(columns=['year', 'total_admissions'])
    df['year'] = df_bellevue['date_in'].str[:4]
    df['total_admissions'] = df.groupby('year')['year'].transform('size')
    df = df.drop_duplicates(subset = 'year')
    return df

#return a series with index: gender (for each gender) and values: avg age of indexed gender
#continuing to use altered gender column from above
def task_3():
    df_bellevue['gender'] = df_bellevue['gender'] \
                                .replace(['h', 'g', '?'], np.nan)
    avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean()
    return pd.Series(avg_age_by_gender, 
                        index = df_bellevue['gender'].unique().astype(str))

#return a list of the top 5 professions in order of prevalence (most common first)
def task_4():
    return df_bellevue['profession'].value_counts()[:5].index.tolist()
