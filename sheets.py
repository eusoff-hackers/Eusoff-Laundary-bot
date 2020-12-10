import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('G_gred.json', scope)
client = gspread.authorize(creds)


def findAvilbility():
    
    # Open the google sheet
    sheet = client.open("WachingMachineData").sheet1

    Acol = sheet.col_values(3)  # A block
    Bcol = sheet.col_values(3)  # B block
    Ccol = sheet.col_values(3)  # C block
    Dcol = sheet.col_values(3)  # D block
    Ecol = sheet.col_values(3)  # E block

    print(Acol)

    return [Acol,Bcol,Ccol,Dcol,Ecol]

