import seaborn as sns
import pandas as pd
import numpy as np


"""
Our goal is to write a recursive function to compute the nth Fibonacci number, 
 (sum of previous two numbers within the series starting with 0 and 1).
Assuming the inputted n number is an integer and greater than or equal to zero,
 we first check if n is equal to 0 or equal to 1. If so, return the respective number back.
Otherwise, our function recursively calls upon itself calculating the sum of the
 previous number (n-1) and number before the previous (n-2) until n is equal to 0 or 1.
Once n reaches 0 or 1, it returns the calculated fibonacci sum.
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
Our goal is to write a function to convert a non-negative integer to its binary representation as a string.
If the number is 0, the function will automatically return 0.
While the current number is greater than 0, add the remainer of the number when divided by 2 to the binary string
 and find the new number (which is the current number divided by 2 using the floor division operator (aka the divided number down)).
Once the number is 0, return the found converted binary string.
The function should raise a ValueError if the input is not a non-negative integer, 
 which will account for any invalid inputs.
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
    return df_bellevue[col_list].isna() \
                                .sum() \
                                .sort_values() \
                                .index.tolist()

    
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
    df['total_admissions'] = df.groupby('year')['year'] \
                                .transform('size')
    df = df.drop_duplicates(subset = 'year')
    return df

"""
Our third task is to return a series with the index containing each gender from the bellevue data frame
 and the values showing the average age for that indexed gender.
First, we must remedy the same issue with the gender column from task one to ensure that
 there is only M (male), F (female), and NaN (missing) values.
Then, we find the average age by using the groupby function (for gender then age) and the 
 mean function to calculate the average age for each gender.
Finally, we return a series that sets the index to a string value of each unique
 gender value and the value at each index to the corresponding calculated average age.
"""
def task_3():
    df_bellevue['gender'] = df_bellevue['gender'] \
                                .replace(['h', 'g', '?'], np.nan)
    avg_age_by_gender = df_bellevue.groupby('gender')['age'] \
                                    .mean()
    return pd.Series(avg_age_by_gender, 
                        index = df_bellevue['gender'].unique().astype(str))

"""
Our fourth (and final) task is to return a list of the top 5 professions in order for most
 to least prevalent.
This function uses the value_counts() function to return the first 5 professions
 sorted by the value_count(which automatically sorts descending by count).
The index and tolist() function are also used since the value_count function returns a series,
 so we find the index (the profession name) and just return a list of those values instead.
"""
def task_4():
    return df_bellevue['profession'].value_counts()[:5].index.tolist()
