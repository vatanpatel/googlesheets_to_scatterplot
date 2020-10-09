googlesheets_to_scatterplot is a Python module for creating plots directly from spreadsheet.

The project was started in 2020 by Vatan Patel as a pre-process task for Greendeck.

### Function to plot:
googlesheets_to_scatterplot.plot(spreadsheet_name, xcol, ycol, sheet_number)

### Dependencies:

- pandas
- matplotlib
- seaborn
- gspread
- oauth2client

### Setup:

 - Now you need to set up your sharing options. You will need to generate Signed Credentials, something that sounds more difficult than it is. Navigate to the Google Developers Console and create a new project (or use an existing one).

 - Give your project a suitable name and then click create.
 
 - Enable Drive API and Sheets API from Google Apps APIs.
 
 - Now select Credentials on the left menu. Click the little arrow on the Create credentials button and select 'Help me choose' and select following options:
    - Which API are you using: Google drive API
    - Where will you be calling the API from: Other non-UI
    - What data will you be accessing: Application data
    - Are you planning to use this API with App Engine or Compute Engine: No, I'm not using them
    - Download the JSON file which contains your client id
    - Move the json into your current directory and rename it creds.json. 
    - Finally, open the file and look for client_email. This should be the name of your project at appspot.gserviceaccount.com. Share your Google Sheet with this email address (Top Right > Share > Enter Email).
    
 Now we are good to go. You can now use the module.

### Parameters:

- spreadsheet_name (str, required): Write the name of the google spreadsheet you want to create plots from. Make sure the name matches exactly.

- xcol (str, required): The column name of the column you want on the x-axis.

- ycol (str, required): The column name of the column you want on the y-axis.

- sheet_number (int, default = 1): This is the sheet number in your spreadsheet on which the table is present).

