from requests import get

myip = get('https://api.ipify.org').text
# print('{}'.format(myip))