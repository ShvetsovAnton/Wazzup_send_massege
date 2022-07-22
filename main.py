import requests
import time
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


def seng_message(token, chanel_id, phone_number, timer, message):
    url = "https://api.wazzup24.com/v3/message"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {"channelId": chanel_id,
              "chatId": f"{phone_number}",
              "chatType": "whatsapp",
              "text": message}
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    time.sleep(timer)


def main():
    chanel_id = input("Введи id канала Wuzzup\n")
    token = input("Введи токен\n")
    timer = int(input("Введи время для задержки в секундах\n"))
    message = input("Введи сообщение для отпарвки\n")
    phone_numbers = read_from_google_sheet()
    for phone_number in phone_numbers:
        print(f"Сообщение отправлено на {phone_number}")
        try:
            seng_message(token, chanel_id, phone_number, timer, message)
        except requests.exceptions.HTTPError:
            print("Неудалось отправить сообщение")


if __name__ == '__main__':
    main()
