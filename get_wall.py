import requests
import conf
import json

def getwall():
    req = requests.get('https://api.vk.com/method/wall.get?owner_id=130314&count=100&access_token=' + conf.TOKEN)
    f = open('polet.txt', 'w', encoding='utf-8')
    f.write(req.text)
    f.close()

def main():
    getwall()

if __name__ == '__main__':
    main()