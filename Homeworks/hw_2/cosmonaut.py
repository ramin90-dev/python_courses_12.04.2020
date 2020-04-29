import requests

def numberaustro():
    # получение информации по сервису
    res = requests.get('http://api.open-notify.org/astros.json')
    # возврат ответа
    return res.json()["number"]
    #альтернативный вариант
    #a = res.json()
    #return a["number"]


