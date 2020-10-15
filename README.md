googlesheets_to_scatterplot is a Python library for creating plots directly from spreadsheet.

The project was started in 2020 by Vatan Patel as a pre-process task for Greendeck.

#
### Dependencies:

- pandas
- matplotlib
- seaborn
- gspread
- oauth2client

#
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
 #
 ### Installation:
 
 If you already have a working installation of numpy, pandas, matplotlib, seaborn, oauth2client and gspread the easiest way to install googlesheets_to_scatterplot is using pip:
   
```bash
    $ pip install googlesheets-to-scatterplot==0.0.8
```

#
### Function to plot:

googlesheets_to_scatterplot.plot(spreadsheet_name, xcol, ycol, sheet_number)

#
### Parameters for googlesheets_to_scatterplot.plot():

- spreadsheet_name (str, required): Write the name of the google spreadsheet you want to create plots from. Make sure the name matches exactly.

- xcol (str, required): The column name of the column you want on the x-axis.

- ycol (str, required): The column name of the column you want on the y-axis.

- sheet_number (int, default = 1): This is the sheet number in your spreadsheet on which the table is present.

#
### Imortant Links:
URL: https://pypi.org/project/googlesheets-to-scatterplot/0.0.12/

# 
### Changelog:

- 0.0.4 (08/10/2020)
    - First Release

- 0.0.7 (09/10/2020)
    - Second Release
       - We remove the need for providing the client name
       - Default sheet number is takes as 1
       - We updated the README file.
       - We add proper comments to our library for people to refer later
       - Made changes to the title
       - We removed changelog from long_description
       
- 0.0.12 (09/10/2020)
    - Third release
        - We added changelog and other descriptions to README

#