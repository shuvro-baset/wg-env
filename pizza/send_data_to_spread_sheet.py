from datetime import date

import gspread
from oauth2client.service_account import ServiceAccountCredentials


# =================== send data to spreadsheet start ==================
def send_to_spreadsheet(order_data):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
             'https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('order_data_list.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("order_data_list").sheet1
    try:
        row = [order_data['user_personal_data'], order_data['food_data'], order_data['total_food_price'],
               order_data['service_charge'], order_data['delivery_fee'], order_data['tax_fee'],
               order_data['total_payable'], ]
        index = 2
        sheet.insert_row(row, index)
    except Exception as e:
        print(e)
    return True
    # =================== send data to spreadsheet end ==================
