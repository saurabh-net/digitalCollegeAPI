from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json,httplib,urllib
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django import forms
from django.template import RequestContext
import django_excel as excel
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import pyexcel
import urllib
from attendance.models import ListOfClasses
from datetime import datetime
from mywrapper.models import *
from mywrapper.serializers import *
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.test import APIRequestFactory
from mywrapper.views import *
from django.contrib.auth.models import User

# Create your views here.
factory = APIRequestFactory()

def getStudentList(classSection,restKey,appKey):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	params = urllib.urlencode({"where":json.dumps({
		   "Class_Name": '%s' % classSection
		 })})
	connection.connect()
	connection.request('GET', '/1/classes/Class?%s' % params, '', {
		   # "X-Parse-Application-Id": "Sqj2XR5GDdMcXuMsffDQ9yEdzhYJqBZYvDSMLqFC",
		   # "X-Parse-REST-API-Key": "Ox5FKRyiEM33GzS7Ka6oTJCXRIjiPghotbD9dWPx",
		   "X-Parse-Application-Id": appKey,
		   "X-Parse-REST-API-Key": restKey
		 })
	result = json.loads(connection.getresponse().read())
	# print result
	return result['results'][0]['Student_Name']

def getUsernames(classSection,restKey,appKey):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	params = urllib.urlencode({"where":json.dumps({"Class_Name": classSection,}),"limit":999})
	connection.connect()
	connection.request('GET', '/1/classes/_User?%s' % params, '', {
			# "X-Parse-Application-Id": "Sqj2XR5GDdMcXuMsffDQ9yEdzhYJqBZYvDSMLqFC",
		    #   "X-Parse-REST-API-Key": "Ox5FKRyiEM33GzS7Ka6oTJCXRIjiPghotbD9dWPx"
		    "X-Parse-Application-Id": appKey,
		    "X-Parse-REST-API-Key": restKey
			})
	userNames = json.loads(connection.getresponse().read())
	return userNames['results']

def postAttendanceData(classSection,json_data,restKey,appKey):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/' + classSection , json_data, {
		   # "X-Parse-Application-Id": "Sqj2XR5GDdMcXuMsffDQ9yEdzhYJqBZYvDSMLqFC",
		   # "X-Parse-REST-API-Key": "Ox5FKRyiEM33GzS7Ka6oTJCXRIjiPghotbD9dWPx",
		   "X-Parse-Application-Id": appKey,
		   "X-Parse-REST-API-Key": restKey,
		   "Content-Type": "application/json"
		 })
	results = json.loads(connection.getresponse().read())
	#print results


@login_required
def index(request):
	# latest_class_list = ListOfClasses.objects.filter(schoolUser=request.user)	
	requestInternal = factory.get('/myapi/getallsubjects/',format='json')
	requestInternal.user = request.user	
	response = getallsubjects(requestInternal)
	print response.data
	print '**********************************'
	for i in range(len(response.data)):
		print response.data[i]['id']

	latest_class_list = Subject.objects.all()
	classLinks = [p.id for p in latest_class_list]
	classNames = [p.subjectName for p in latest_class_list]
	zipped_data = zip(classLinks, classNames)
	context = {'item1':"My first string",'classLinks':classLinks,'classNames':classNames,'zipped_data':zipped_data}
	return render(request,'attendance/listSubject.html',context)	

@login_required
def indexComponent(request,pk):
	# latest_class_list = ListOfClasses.objects.filter(schoolUser=request.user)	
	subject = Subject.objects.get(id=pk)
	latest_class_list = SubjectComponents.objects.filter(subject=subject)
	classLinks = [p.id for p in latest_class_list]
	classNames = [p.componentID + ' ' + p.sectionID for p in latest_class_list]
	zipped_data = zip(classLinks, classNames)
	context = {'item1':"My first string",'classLinks':classLinks,'classNames':classNames,'zipped_data':zipped_data}
	return render(request,'attendance/listComponent.html',context)

@login_required
def viewAttendance(request,classSection):
	firstInstance = ListOfClasses.objects.filter(schoolUser=request.user).first()
	restKey = firstInstance.restKey
	javaKey = firstInstance.javaKey
	appKey 	= firstInstance.appKey
	neatSection = classSection[1:-1] + " " + classSection[-1]
	strippedSection = classSection[1:]	
	context = {'classSection':classSection,'neatSection':neatSection,'strippedSection':strippedSection,'appKey':appKey,'javaKey':javaKey}
	return render(request,'attendance/viewAttendance.html',context)

@login_required
def enterAttendance(request,pk):
	# latest_class_list = ListOfClasses.objects.filter(schoolUser=request.user)	
	# classLinks = [p.someClass for p in latest_class_list]
	# classNames = [p[1:-1] + " " + p[-1] for p in classLinks]
	# zipped_data = zip(classLinks, classNames)
	# firstInstance = ListOfClasses.objects.filter(schoolUser=request.user).first()
	subjectComponents = SubjectComponents.objects.get(id=pk)
	students = SubjectsPerStudent.objects.filter(subjectComponents=subjectComponents)
	ids = []
	for student in students:
		ids.append(student.student.id)
	studentsList = Student.objects.filter(id__in=ids)
	studentName = [p.studentFullName for p in studentsList]
	studentID = [p.studentID for p in studentsList]
	databaseID = [p.id for p in studentsList]
	zipped_data = zip(studentName, studentID,databaseID)
	# serializer = ReadStudentSerializer(students2,many="True")
	# print serializer
	# studentList = getStudentList(classSection,restKey,appKey)
	if request.method == 'POST':
		absentStudents = request.POST
		print absentStudents
		# subjectComponents = SubjectComponents.objects.get(id=pk) 
		dateOfAttendance = request.POST['date']
		# myDateObject = datetime.strptime(dateOfAttendance,'%d/%m/%Y').strftime('%Y-%m-%d')
		# # date = datetime.strptime(request.POST['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
		# daysAttendanceWasTaken = DaysAttendanceWasTaken(subjectComponents=subjectComponents, dateOfAttendance=myDateObject,owner=request.user)
		# try:	
		# 	daysAttendanceWasTaken.save()
		# except IntegrityError: 
		# 	return Response({'id':-2, 'status': 'Attendance already exists for this date. Do you want to overwrite it?'},status=status.HTTP_400_BAD_REQUEST)
		# requestInternal = factory.post('/myapi/postabsentstudents/',{'students': [1,2],'teacher':1,'subjectcomponent': 2, "date": "03/04/2016" },format='json')
		# requestInternal.user = request.user	
		# response = postabsentstudents(requestInternal)
		# print response.data
		# data = {}
		# data['cDate'] = request.POST['date']
		# dateOfAttendance = data['cDate']
		# myDateObject = datetime.strptime(dateOfAttendance,'%d/%m/%Y')
		# myDateObject = myDateObject.strftime("%d %B %Y")
		# # For loop to iterate over list of students and assign 'A' or 'P'.
		# # Also sends emails to absent students' parents
		# for student in studentList:
		# 	studentMod = student.replace (" ", "_")
		# 	studentMod = "R" + studentMod
		# 	if(student in absentStudents):
		# 		data[studentMod] = "A"
		# 		userdata = (user for user in userNames if user["username"] == classSection+student).next()
		# 		# if 'email' in userdata:
		# 		# 	print 'email the person!'
		# 		# 	email = EmailMessage('Hello there', 'well well, your son was absent today', to=[userdata['email']])
		# 		# 	print userdata['email']
		# 		# 	email.send()
		# 		# else:
		# 		# 	print 'ask them to enter their e-mail!'
		# 		if 'phoneNumber' in userdata:
		# 			# print 'Starting now'
		# 			try:
		# 				childName = userdata["username"].split()
		# 				childName = childName[1:]
		# 				childName = " ".join(childName)
		# 			except:
		# 				childName = "Your child"
		# 			myMessage =  childName + ' was absent on ' + myDateObject + '\r\n - Kerala Public School'
		# 			myNumber = userdata['phoneNumber']
		# 			print childName
		# 			# print 'Is this where I go wrong?'
		# 			params = urllib.urlencode({'user': 'Saurabh', 'password': '123@123', 'mobiles': myNumber, 'sms':myMessage,'senderid':'PTMNOW','version':3})
		# 			# print 'Or here?'
		# 			f = urllib.urlopen("http://trans.profuseservices.com/sendsms.jsp?%s" % params)
		# 			print f.read()
		# 	else:
		# 		data[studentMod] = "P"
		# start = dateOfAttendance.find('/')
		# end = dateOfAttendance.rfind('/')
		# data['mdate'] = int(dateOfAttendance[start+1:end])
		# json_data = json.dumps(data)
		# postAttendanceData(classSection,json_data,restKey,appKey)					
		# # return HttpResponseRedirect(reverse('attendance:index'))
		# #return redirect(reverse('attendance:index'), {'alert':'alert'})
		# return render(request,'attendance/listSubject.html',{'alert':'alert',"classSection":classSection,'classLinks':classLinks,'classNames':classNames,'zipped_data':zipped_data})
		context = {'studentList':zipped_data,'classSection':pk}
		return render(request,'attendance/enterAttendance.html',context)
	else:	
		context = {'studentList':zipped_data,'classSection':pk}
		# return redirect(reverse('attendance:index'), {"alert":"alert"})
		return render(request,'attendance/enterAttendance.html',context)

class UploadFileForm(forms.Form):
	file = forms.FileField()

@login_required
def uploadAttendance(request,classSection):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			filehandle = request.FILES['file']
			attendanceExcel = request.FILES['file'].get_array()
			for i in range(1,len(attendanceExcel)):
				print attendanceExcel[i]
	else:
		form = UploadFileForm()
	return render_to_response(
		'attendance/uploadAttendance.html',
		{
			'form': form,
			'title': 'Excel file upload and download example',
			'header': 'Please choose any excel file from your cloned repository:'
		},
		context_instance=RequestContext(request))
