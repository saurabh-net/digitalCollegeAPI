import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwib3JpZ19pYXQiOjE0NTg0OTAyOTEsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDkwMDI2MjkxfQ.MJvjtnUnBOWbAJMl4N-Wc48TXPbxqJ5le-LNv528Cmk'

url = 'http://127.0.0.1:8000/myapi/student/'
url2 = 'http://127.0.0.1:8000/myapi/addstudentaccount/'
headers = {'Authorization': 'JWT '+token}
listOfStudents = ['Vedant_Dual', 'Braj_Mech', 'Pinto_ENI','Saurabh_CS']
listOfNames = ['Vedant Mishra', 'Braj Kishore', 'Dev Pinto','Saurabh Maurya']
listOfEmails = ['vedant@gmail.com','braj@gmail.com','','saurabhmaurya06@gmail.com']
listOfPhoneNumbers = ['8504005493','9031702359','','9945149074']


for i in range(4):
	r = requests.post(url2,headers=headers, data={'studentID':listOfStudents[i],'studentFullName':listOfNames[i],'studentPhoneNumber':listOfPhoneNumbers[i],'studentEmailID':listOfEmails[i]})
	print r.text
	r = requests.post(url,headers=headers, data={'studentID':listOfStudents[i],'studentFullName':listOfNames[i]})
	print r.text

# url = 'http://127.0.0.1:8000/myapi/teacher/'	
# listOfTeacherIDs = ['Ricky_Schlum','Karwa_EY']
# listOfTeacherNames = ['Ricky Lakhar', 'Chaitanya Karwa']
# for i in range(2):
# 	r = requests.post(url,headers=headers, data={'teacherID':listOfTeacherIDs[i],'teacherFullName':listOfTeacherNames[i]})
# 	print r.text

# url = 'http://127.0.0.1:8000/myapi/subject/'	
# url2 = 'http://127.0.0.1:8000/myapi/subjectcomponents/'
# listOfSubjectIDs = ['HUM_F105','HUM_F106','Math_F103','BIO_F104']
# listOfSubjectNames = ['Creative Art', 'Contempory Philosophy','Introduction to Proofs','Epigenetics']
# for i in range(4):
# 	r = requests.post(url,headers=headers, data={'subjectID':listOfSubjectIDs[i],'subjectName':listOfSubjectNames[i]})
# 	print r.text
# 	result = r.json()
# 	while (True):
# 		componentID = raw_input(" Please enter componentID for " + listOfSubjectNames[i] + " or 'n' to move on to next subject")
# 		if componentID == 'n':
# 			break
# 		sectionID = raw_input("Please enter sectionID for "+ componentID + " or 'n' to move on to next subject")
# 		if sectionID == 'n':
# 			break
# 		r = requests.post(url2,headers=headers, data={'subject':result['id'],'componentID':componentID,'sectionID':sectionID})
# 		print r.text
# 	