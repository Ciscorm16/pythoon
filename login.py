import requests
import json
import csv

correo=""
contrasena=""
url="http://127.0.0.1:3333/api/v1/usuarios/login"
print("Correo")
correo = input()
print("contraseña")
contrasena = input()

if __name__=='__main__':
    payload ={"email": correo, "password":contrasena}
    headers={'Accept':'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json['token']
        token = access_token
        with open('token.json', 'w') as file:
            json.dump("Bearer "+token, file, indent=4)
        with open('token.json') as file:
            data = json.load(file)
            print(data)
        #print(token)
    else:
        print("Error de datos")