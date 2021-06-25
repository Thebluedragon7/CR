import requests


def get_chest():
    chestURL = 'https://api.clashroyale.com/v1/players/%23'+playerID+'/upcomingchests'
    upComing_Chests = requests.get(chestURL, headers = {"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjMzZDQ2OGQxLWM5ZTAtNDI3Ni1iZTQ2LTkxYzAzNTJiZjZkNyIsImlhdCI6MTYyNDYyMzk3Nywic3ViIjoiZGV2ZWxvcGVyLzc4NzdkN2YzLTlhNGYtYjBmMi04Y2UwLWJkNWQzOTcwM2U4YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyNy4zNC4xMDguOTkiXSwidHlwZSI6ImNsaWVudCJ9XX0.mHBR5ijRoDwHT4NPzMEegjwY8g-Q1s2zzbiqcTyNS_B6n-eyUAJm8cNiEWr75TJpffZiLwyEX6O2Tu4CPV4mmg"})
    chests = upComing_Chests.json()

    for i in range(len(chests['items'])):
        if i == 0:
            print(f"The next chest is {chests['items'][0]['name']}")
        elif i == 1:
            print(f"The {chests['items'][i]['index']}nd chest is {chests['items'][1]['name']}")
        elif i == 2:
            print(f"The {chests['items'][i]['index']}rd chest is {chests['items'][2]['name']}")
        else:
            print(f"The {chests['items'][i]['index']}th chest is {chests['items'][i]['name']}")
            
            

p_ID = input(str("Enter your player ID without '#' :"))
playerID = p_ID.upper()
get_chest()