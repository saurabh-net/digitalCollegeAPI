import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwib3JpZ19pYXQiOjE0NTg0OTAyOTEsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDkwMDI2MjkxfQ.MJvjtnUnBOWbAJMl4N-Wc48TXPbxqJ5le-LNv528Cmk'

url = 'http://127.0.0.1:8000/myapi/student/'
headers = {'Authorization': 'JWT '+token}
listOfStudents = ['Vedant_Dual', 'Braj_Mech', 'Pinto_ENI']
for student in listOfStudents:
	r = requests.post(url,headers=headers, data={'studentID':student})
	print r.text
	