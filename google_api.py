import httplib2
from oauth2client.service_account import ServiceAccountCredentials
import apiclient


def read_from_google_sheet():
    CREDENTIALS_FILE = 'creds.json'
    spreadsheet_id = input("Введи id таблицы\n")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    phone_numbers = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:A1000',
        majorDimension='ROWS'
    ).execute()
    print(phone_numbers["values"])
    return phone_numbers["values"]

