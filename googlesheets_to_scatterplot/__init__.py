# First we need to import all the required libraries

import matplotlib.pyplot as plt
import seaborn as sns
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# We set the style of our plots. I like whitegrid.
sns.set_style('whitegrid')

# We define our function with 4 parameters:
# 1. spreadsheet_name (str, required): Write the name of the google spreadsheet you want to create plots from. Make sure the name matches exactly.
# 2. xcol (str, required): The column name of the column you want on the x-axis.
# 3. ycol (str, required): The column name of the column you want on the y-axis.
# 4. sheet_number (int, default = 1): This is the sheet number in your spreadsheet on which the table is present).

def plot(spreadsheet_name, xcol, ycol, sheet_number = 1):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']                 # We define the scope
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)                              # We add credentials to the account
    client = gspread.authorize(creds)                                                                          # We authorize the clientsheet
    sheet = client.open('{}'.format(spreadsheet_name))                                                         # We get the instance of the Spreadsheet
    sheet_number = sheet_number - 1                                                                            # Indexing in python starts from 0. So we subtract 1 from the sheet number provided, if any
    sheet_instance = sheet.get_worksheet(sheet_number)                                                         # We get the required sheet number of the Spreadsheet
    records_data = sheet_instance.get_all_records()                                                            # We get all the records of the data
    data = pd.DataFrame.from_dict(records_data)                                                                # We convert the json to dataframe
    sns.scatterplot(data[xcol], data[ycol])                                                                    # We create the scatterplot using the xcol and ycol provided
    plt.title('{} - {} Scatterplot'.format(xcol, ycol))                                                        # We set the title
    return plt.show()                                                                                          # We return the plot