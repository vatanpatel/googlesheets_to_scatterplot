import matplotlib.pyplot as plt
import seaborn as sns
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

sns.set_style('whitegrid')

def plot(client_id, spreadsheet_name, sheet_number, xcol, ycol):
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('{}.json'.format(client_id), scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open('{}'.format(spreadsheet_name))

    # get the first sheet of the Spreadsheet
    sheet_number = sheet_number - 1
    sheet_instance = sheet.get_worksheet(sheet_number)

    # get all the records of the data
    records_data = sheet_instance.get_all_records()

    # convert the json to dataframe
    data = pd.DataFrame.from_dict(records_data)
    sns.scatterplot(data[xcol], data[ycol])
    plt.title('Scatterplot')
    return plt.show()