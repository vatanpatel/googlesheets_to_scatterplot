This is a simple function that returns a scatterplot from a google spreadsheet. It takes 5 parameters:

- client_id (str): This is the name of the client_id file that you downloaded from your credential. This will be a json file. Do not include .json in the name.

- spreadsheet_name (str): Write the name of the google spreadsheet you want to create plots from. Make sure the name matches exactly.

- sheet_number (int): This is the sheet number in your spreadsheet on which the table is present)

- xcol (str): The column name of the column you want on the x-axis

- ycol (str): The column name of the column you want on the y-axis
