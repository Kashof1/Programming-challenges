from calendar import month
from concurrent.futures import process
import csv
from pathlib import Path
from matplotlib import test
csv_path = Path('AAPL.csv')

def check_file_exists(path):
    return path.is_file()

def read_csv(csv_path):
    csv_array = []
    if check_file_exists(csv_path):
        with open (csv_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                csv_array.append(row)
    
    return csv_array

def data_splitter(csv_array):
    processed_month_list = []
    monthly_dictionary = {}
    for currentrow in csv_array:
        current_date_value = currentrow[0].split('-')
        current_year_month = current_date_value[0] + '-' + current_date_value[1]
        if current_year_month not in processed_month_list:
            monthly_dictionary[current_year_month] = [[],[],[]] #adj_close, volume, total_sale
            processed_month_list.append(current_year_month)
        if current_year_month == ((currentrow[0])[:-3]): #(currentrow[0])[:-3] returns the year and month of the current row, and strips off the day at the end
            adj_close = float(currentrow[5]) #test float and multiplying
            print (adj_close)
            volume = float(currentrow[6])
            print (volume)
            total_sale = adj_close * volume
            (monthly_dictionary[current_year_month][0]).append(adj_close)
            (monthly_dictionary[current_year_month][1]).append(volume)
            (monthly_dictionary[current_year_month][2]).append(total_sale)

#need to write code to calcualte the average for each month and somehow store it (probably best to store it as an integer with the month key in the dictionary, inside the list for each key)

    print (processed_month_list)
    return monthly_dictionary



if __name__ == '__main__':
    csv_array = read_csv(csv_path)
    testdictionary = data_splitter(csv_array)
    print (testdictionary)