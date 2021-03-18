import requests


server = "http://127.0.0.1:5000"
r = requests.get(server+"/")
print(r.status_code)
print(r.text)

blood_data = {"HDL": 60}
r = requests.post(server+"/HDL", json=blood_data)
print(r.status_code)
print(r.text)
answer = r.json()
print(answer)
print(type(answer))
