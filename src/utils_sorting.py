import numpy as np
import pandas as pd

from data.data_pairing_list import data as DATA_PAIRING_LIST
from data.data_pairing_list import TEAMS as TEAMS

from data.data_pairing_list2 import data as DATA_PAIRING_LIST2
from data.data_pairing_list2 import TEAMS as TEAMS2

from config import *


def create_pairing_list(event):
    '''
    Temporary function to create (hard-coded) pairing list
    :return: Pairing list as a pandas DataFrame
    '''
    data = DATA_PAIRING_LIST

    # Parse the data
    lines = data[event].strip().split('\n')
    parsed_data = []

    for line in lines[1:]:
        split_line = line.split()
        race = split_line[0].strip()
        boats = split_line[1:]
        temp_list = [int(race)]
        for boat_number, team in enumerate(boats, start=1):
            temp_list.append(team)
        parsed_data.append(temp_list)

    columns = ['Race']
    columns.extend(['Boat{}'.format(i) for i in range(1, 7)])
    df = pd.DataFrame(parsed_data, columns=columns)
    df['flight'] = [number for number in range(1, 17) for _ in range(3)]

    results_dict = {'Teams': TEAMS, 'SCP': [0] * len(TEAMS)}
    for flight in range(1, FLIGHTS + 1):
        results_dict[f'Flight {flight}'] = [np.nan] * len(TEAMS)
    results_dict['Total'] = [0] * len(TEAMS)
    results = pd.DataFrame(results_dict)

    return df, results


def count_values(row):
    # You can adjust this list based on the values you're interested in
    values_of_interest = [i for i in range(1, 6 + 2)]
    # TODO look only in Race{}.format() columns
    counts = {value: (row == value).sum() for value in values_of_interest}
    return pd.Series(counts)


def replace_rdg(result_df, value="RDG", mode="all"):
    rows, cols = (result_df == value).to_numpy().nonzero()

    for row, col in zip(rows, cols):
        result_df_copy = result_df.copy()
        result_df_copy["SCP"] = np.nan
        result_df_copy["_id"] = np.nan
        result_df_copy["Total"] = np.nan
        row_values = result_df_copy.iloc[row, :].apply(pd.to_numeric, errors='coerce')
        mean_value = row_values[row_values.notna()].mean()
        result_df.iloc[row, col] = round(mean_value, 1)

    return result_df


def sort_results(result_df, prints=False):
    result_df_copy = result_df.copy()

    result_df_copy.replace(BUCHSTABEN, inplace=True)
    result_df_copy.replace('-', np.nan, inplace=True)
    result_df_copy = replace_rdg(result_df_copy)

    columns_to_sum = ['SCP']
    columns_to_sum.extend([f'Flight {i}' for i in range(1, FLIGHTS + 1)])

    result_df_copy[columns_to_sum] = result_df_copy[columns_to_sum].astype('float64')

    result_df_copy['Total'] = result_df_copy[columns_to_sum].sum(axis=1)
    counts_df = result_df_copy.apply(count_values, axis=1)
    result_df_copy = pd.concat([result_df_copy, counts_df], axis=1, )

    sort_column_list = ['Total']
    sort_column_list.extend([i for i in range(1, BOATS + 2)])
    sort_column_list.extend(['Flight {}'.format(i) for i in range(FLIGHTS, 1, -1)])

    sort_column_order_list = [True]
    sort_column_order_list.extend([False for i in range(1, BOATS + 2)])
    sort_column_order_list.extend([True for i in range(FLIGHTS, 1, -1)])

    result_df_copy.sort_values(by=sort_column_list, ascending=sort_column_order_list, inplace=True)

    index = result_df_copy.index
    result_df = result_df.reindex(index)
    result_df['Total'] = result_df_copy['Total']
    
    if prints:
        print("[INFO] Results computed.")
        
    return result_df


def get_flight(race):
    return int(np.ceil(race / (len(TEAMS) / BOATS)))


def add_results(result_df):
    return result_df
