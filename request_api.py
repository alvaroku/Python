import requests 

URL = 'http://localhost/apis/usuario/get.php?idUs=1'

data = requests.get(URL) 

data = data.json()

print(data)