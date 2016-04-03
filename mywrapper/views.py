from django.shortcuts import render
import datetime
from django.utils import timezone
from django.core.mail import send_mail
 # Create your views here.
# from mywrapper.models import Subject, SubjectComponents,Student,Teacher, SubjectsPerStudent,SubjectsPerTeacher, Attendance,DaysAttendanceWasTaken,Test,Marks
from mywrapper.serializers import *
from calendar import timegm

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.db import IntegrityError
from rest_framework import permissions
from mywrapper.models import Profile
import sendgrid
from .authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated

sg = sendgrid.SendGridClient('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')


class IsTeacher(permissions.BasePermission):
	"""
	Global permission check for whether the user is a teacher
	"""

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		try:
			user = request.user
			profile = Profile.objects.get(user=user)
		except: 
			return False    
		if profile.is_teacher == True or profile.is_administrator == True:
			return True
		return False

class IsAdministrator(permissions.BasePermission):
	"""
	Global permission check for whether the user is a teacher
	"""

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		try:
			user = request.user
			profile = Profile.objects.get(user=user)
		except: 
			return False    
		if profile.is_administrator == True:
			return True
		return False

class SubjectList(generics.ListCreateAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class SubjectComponentsList(generics.ListCreateAPIView):
	queryset = SubjectComponents.objects.all()
	serializer_class = SubjectComponentsSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class SubjectComponentsDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = SubjectComponents.objects.all()
	serializer_class = SubjectComponentsSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class SubjectsPerStudentList(generics.ListCreateAPIView):
	queryset = SubjectsPerStudent.objects.all()
	serializer_class = SubjectsPerStudentSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class SubjectsPerStudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = SubjectsPerStudent.objects.all()
	serializer_class = SubjectsPerStudentSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class SubjectsPerTeacherList(generics.ListCreateAPIView):
	queryset = SubjectsPerTeacher.objects.all()
	serializer_class = SubjectsPerTeacherSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class SubjectsPerTeacherDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = SubjectsPerTeacher.objects.all()
	serializer_class = SubjectsPerTeacherSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class StudentList(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class TeacherList(generics.ListCreateAPIView):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class AttendanceList(generics.ListCreateAPIView):
	queryset = Attendance.objects.all()
	serializer_class = AttendanceSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Attendance.objects.all()
	serializer_class = AttendanceSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class TestList(generics.ListCreateAPIView):
	queryset = Test.objects.all()
	serializer_class = TestSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Test.objects.all()
	serializer_class = TestSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class MarksList(generics.ListCreateAPIView):
	queryset = Marks.objects.all()
	serializer_class = MarksSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class MarksDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Marks.objects.all()
	serializer_class = MarksSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class DaysAttendanceWasTakenList(generics.ListCreateAPIView):
	queryset = DaysAttendanceWasTaken.objects.all()
	serializer_class = DaysAttendanceWasTakenSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class DaysAttendanceWasTakenDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = DaysAttendanceWasTaken.objects.all()
	serializer_class = DaysAttendanceWasTakenSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class ProfileList(generics.ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]
	def perform_create(self, serializer):
		serializer.save(accept_tokens_after=datetime.datetime.now())

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]


@api_view(['GET','POST','PUT'])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,IsTeacher])
# @permission_classes((IsTeacher, ))
def postnotice(request):
	"""
	[{
		"category": "General",
		"message" : "Classes will be suspended on the 18th of April, 2016",
		"subjectComponents": [1,2,3],
		"is_sms": 1,
		"is_email": 1,
		"is_push": 0
	}]
	"""
	if request.method == 'POST':
		# request.data['message'] = "Hell"
		try:
			profile = Profile.objects.get(user=request.user)
		except:
			return Response({'id':-2 ,'status': 'No profile for current user'},status=status.HTTP_400_BAD_REQUEST)	
		name = '[empty]'
		try:
			if profile.is_teacher == True or profile.is_administrator == True:
				teacher = Teacher.objects.get(teacherID = profile.student_teacher_id)
				name = teacher.teacherFullName
			else:
				student = Student.objects.get(studentID = profile.student_teacher_id)
				name = student.studentFullName
		except:
			return Response({'id':-3 ,'status': 'No teacher/student for profile ID'},status=status.HTTP_400_BAD_REQUEST)	

		signature = ' -- Message sent by ' + name
		request.data['message'] = request.data['message'] + signature
		studentsToPing = []
		for subjectComponent in request.data['subjectComponents']:
			dataToSave = {}
			dataToSave['category'] = request.data['category']
			dataToSave['message'] = request.data['message']
			if request.data['is_sms'] == 1:
				dataToSave['is_sms'] = True
			else:
				dataToSave['is_sms'] = False

			if request.data['is_email'] == 1:
				dataToSave['is_email'] = True
			else:
				dataToSave['is_email'] = False

			if request.data['is_push'] == 1:
				dataToSave['is_push'] = True
			else:
				dataToSave['is_push'] = False

			# dataToSave['owner'] = request.user
			try:
				print int(subjectComponent)
				sc = SubjectComponents.objects.get(id=int(subjectComponent))
				print 'One'
			except:
				return Response({'id':-4 ,'status': 'No such subject component', 'value':subjectComponent},status=status.HTTP_400_BAD_REQUEST)
			print 'Two'
			# dataToSave['classToSendNotice'] = sc
			dataToSave['classToSendNotice'] = int(subjectComponent)
			print 'Three'
			serializer = NoticeSerializer(data=dataToSave)
			if serializer.is_valid():
				serializer.save(owner=request.user)
				# return Response(serializer.data, status=status.HTTP_201_CREATED)
			# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response({'id':1 ,'status': 'success'},serializer.data, status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'Only POST request supported'},status=status.HTTP_400_BAD_REQUEST)

	# def perform_create(self, serializer):
	# 	serializer.save(owner=self.request.user)

class NoticeList(generics.ListCreateAPIView):
	queryset = Notice.objects.all()
	serializer_class = NoticeSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

class NoticeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Notice.objects.all()
	serializer_class = NoticeSerializer
	permission_classes = [IsAuthenticated,IsTeacher]
	authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication,]

@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication,])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,])
def getteachersubjects(request,pk):
	"""
	[
		{
			"id": 1,
			"teacher": 1,
			"subjectComponents": 1
		},
		{
			"id": 2,
			"teacher": 1,
			"subjectComponents": 2
		}
	]

	"""
	if request.method == 'GET':
		try:
			teacher = Teacher.objects.get(id=pk)
		except:
			return Response({'id':-2, 'status': 'No such teacher'},status=status.HTTP_400_BAD_REQUEST)
		subjects = SubjectsPerTeacher.objects.filter(teacher=teacher)
		serializer = ReadSubjectsPerTeacherSerializer(subjects,many="True")
		return Response(serializer.data)
	return Response({'id':-1 ,'status': 'Only GET requests are supported'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,])
def getstudentlistforcomponent(request,pk):
	if request.method == 'GET':
		try:
			subjectComponents = SubjectComponents.objects.get(id=pk)
		except:
			return Response({'id':-2 ,'status': 'No such subject component'},status=status.HTTP_400_BAD_REQUEST)	 
		students = SubjectsPerStudent.objects.filter(subjectComponents=subjectComponents)
		ids = []
		for student in students:
			ids.append(student.student.id)
		students2 = Student.objects.filter(id__in=ids)
		serializer = ReadStudentSerializer(students2,many="True") # Can use a cleaner serializer
		return Response(serializer.data)
	return Response({'id':-1 ,'status': 'Only GET requests are supported'},status=status.HTTP_400_BAD_REQUEST)	 

@api_view(['GET','POST','PUT'])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,IsTeacher])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
# @permission_classes((IsTeacher, ))
def postabsentstudents(request):
	"""
	JSON Example
	{
	  "students": [1,2,3],
	  "teacher": 1,
	  "subjectcomponent": 2,
	  "date": "04/02/2016"
	}
	"""
	if request.method == 'POST':
		try:
			subjectComponents = SubjectComponents(pk=request.data['subjectcomponent'])
			date = datetime.datetime.strptime(request.data['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
			daysAttendanceWasTaken = DaysAttendanceWasTaken(subjectComponents=subjectComponents, dateOfAttendance=date,owner=request.user)
		except:
			return Response({'id':-1, 'status': 'inaccurate input parameters'},status=status.HTTP_400_BAD_REQUEST)
		try:	
			daysAttendanceWasTaken.save()
		except IntegrityError: 
			return Response({'id':-2, 'status': 'Attendance already exists for this date. Do you want to overwrite it?'},status=status.HTTP_400_BAD_REQUEST)

		for studentid in request.data['students']:
			student = Student.objects.get(id=studentid)
			# student = Student(pk=studentid)

			attendance = Attendance(student=student,dayAttendanceWasTaken=daysAttendanceWasTaken)
			try:
				attendance.save()
			except IntegrityError: 
				return Response({'id':-2, 'status': 'Attendance already exists for this date. Do you want to overwrite it?'},status=status.HTTP_400_BAD_REQUEST)
		return Response({'id': 1 ,'status': 'success'},status=status.HTTP_201_CREATED)
	# return Response(status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'PUT':
		try:
			subjectComponents = SubjectComponents(pk=request.data['subjectcomponent'])
			date = datetime.datetime.strptime(request.data['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
		except:
			return Response({'id':-1, 'status': 'inaccurate input parameters'},status=status.HTTP_400_BAD_REQUEST)
		try:
			daysAttendanceWasTaken = DaysAttendanceWasTaken.objects.get(subjectComponents=subjectComponents, dateOfAttendance=date)
		except:
			return Response({'id':-2, 'status': 'Attendance does not already exist for this date. Add fresh attendance?'},status=status.HTTP_400_BAD_REQUEST)
		currentTime = timezone.now()
		elapsedTime =  currentTime - daysAttendanceWasTaken.timeAttendanceWasMarked
		if ((elapsedTime.total_seconds()/60) > 20000 ):
			return Response({'id':-3 ,'status': 'Too much time has changed since this data was entered'},status=status.HTTP_400_BAD_REQUEST)

		Attendance.objects.filter(dayAttendanceWasTaken=daysAttendanceWasTaken).delete()
		for studentid in request.data['students']:
			student = Student(pk=studentid)
			attendance = Attendance(student=student,dayAttendanceWasTaken=daysAttendanceWasTaken)
			attendance.save()
		return Response({'id': 1 ,'status': 'success'},status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'GET request not supported'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,IsTeacher])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
# @permission_classes((IsAdministrator, ))
def addstudentaccount(request):
	# send_mail('Is this mail being sent?', 'Hello, all the way from ', 'saurabhmaurya06@gmail.com', ['f2012055@pilani.bits-pilani.ac.in','vedantmishra1243@gmail.com'], fail_silently=False)
	if request.method == 'POST':
		try:
			studentID = request.data['studentID']
			studentName = request.data['studentFullName']
			studentPhoneNumber = request.data.get('studentPhoneNumber')
			studentEmailID = request.data.get('studentEmailID')
			# studentPhoneNumber = ''
			# studentEmailID = ''
		except:
			return Response({'id':-1, 'status': 'inaccurate input parameters'},status=status.HTTP_400_BAD_REQUEST)
		try:
			if User.objects.filter(username=studentID).exists():
				return Response({'id':-1, 'status': 'A student with this ID exists'},status=status.HTTP_400_BAD_REQUEST)
			user = User.objects.create_user(studentID, studentEmailID, 'temp123')
		except e :
			return Response({'id':-1, 'status': repre(e)},status=status.HTTP_400_BAD_REQUEST)
		profile = Profile(user=user,is_teacher=False,is_administrator=False,is_student=True, student_teacher_id = studentID,phoneNumber=studentPhoneNumber,emailID=studentEmailID,accept_tokens_after=datetime.datetime.now())
		profile.save()
		return Response({'id':1, 'status': 'success'},status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'GET request not supported'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,IsTeacher])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
# @permission_classes((IsAdministrator, ))
def addteacheraccount(request):
	# send_mail('Is this mail being sent?', 'Hello, all the way from ', 'saurabhmaurya06@gmail.com', ['f2012055@pilani.bits-pilani.ac.in','vedantmishra1243@gmail.com'], fail_silently=False)
	if request.method == 'POST':
		try:
			teacherID = request.data['teacherID']
			teacherName = request.data['teacherFullName']
			teacherPhoneNumber = request.data.get('teacherPhoneNumber')
			teacherEmailID = request.data.get('teacherEmailID')
		except:
			return Response({'id':-1, 'status': 'inaccurate input parameters'},status=status.HTTP_400_BAD_REQUEST)
		try:
			if User.objects.filter(username=teacherID).exists():
				return Response({'id':-1, 'status': 'A teacher with this ID exists'},status=status.HTTP_400_BAD_REQUEST)
			user = User.objects.create_user(teacherID, teacherEmailID, 'temp789')
		except e :
			return Response({'id':-1, 'status': repre(e)},status=status.HTTP_400_BAD_REQUEST)
		profile = Profile(user=user,is_teacher=True,is_administrator=False,is_student=False, student_teacher_id = teacherID,phoneNumber=teacherPhoneNumber,emailID=teacherEmailID,accept_tokens_after=datetime.datetime.now())
		profile.save()
		return Response({'id':1, 'status': 'success'},status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'GET request not supported'},status=status.HTTP_400_BAD_REQUEST)



class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

@api_view(['GET'])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
def getallsubjects(request):
	"""

	"""
	if request.method == 'GET':
		subjects = Subject.objects.all()
		serializer = DetailedSubjectSerializer(subjects, many=True)
		return Response(serializer.data)
	return Response({'id':-1 ,'status': 'Only GET request is supported'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
def changepassword(request):
	"""

	"""
	if request.method == 'POST':
		password = request.data['password']
		confirm_password = request.data['confirm_password']
		if password == confirm_password:
			user = request.user
			user.set_password(confirm_password)
			user.save()
		else:
			return Response({'id':-1 ,'status': 'Passwords did not match.'},status=status.HTTP_400_BAD_REQUEST)
		return Response({'id': 1 ,'status': 'success'},status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'Only POST request is supported'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
def getattendanceforsubjectcomponent(request,pk):
	"""

	"""
	if request.method == 'GET':
		daysAttendanceWasTaken = DaysAttendanceWasTaken.objects.filter(subjectComponents=pk)
		# print daysAttendanceWasTaken
		ids = []
		for item in daysAttendanceWasTaken:
			ids.append(item.id)
		absentStudents = Attendance.objects.filter(dayAttendanceWasTaken__in=ids)
		students = SubjectsPerStudent.objects.filter(subjectComponents=pk)
		dictionaryOfAllStudentAbsentDates = {}
		listOfDaysAttendanceWasTaken = []
		for day in daysAttendanceWasTaken:
			date = day.dateOfAttendance
			date = datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%d/%m/%Y')
			listOfDaysAttendanceWasTaken.append(date)
		dictionaryOfAllStudentAbsentDates['allDaysAttendanceWasTaken'] = listOfDaysAttendanceWasTaken
		tempDict = {}
		for student in students:
			ListOfStudentAbsentDates = []
			for temp in absentStudents:
				if temp.student ==  student.student:
					date =  DaysAttendanceWasTaken.objects.get(id=temp.dayAttendanceWasTaken.id)
					date = date.dateOfAttendance
					date = datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%d/%m/%Y')
					ListOfStudentAbsentDates.append(date)
			tempDict[ str(student.student) ] = ListOfStudentAbsentDates
			# dictionaryOfAllStudentAbsentDates[ str(student.student) ] = ListOfStudentAbsentDates
		dictionaryOfAllStudentAbsentDates['students'] = tempDict
		print dictionaryOfAllStudentAbsentDates
		return Response(dictionaryOfAllStudentAbsentDates,status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'Only GET request is supported'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,])
# @authentication_classes([SessionAuthentication,BasicAuthentication,JSONWebTokenAuthentication,])
def getattendanceforstudent(request,pk):
	"""
	pk refers to the id of the student	
	"""
	if request.method == 'GET':
		try:
			student = Student.objects.get(id=pk)
			subjectComponentsOfStudent = SubjectsPerStudent.objects.filter(student=student)
		except:
			return Response({'id':-2, 'status': 'inaccurate input parameters'},status=status.HTTP_400_BAD_REQUEST)
		# dictOfAllSubjectAttendance = {}
		listOfAllSubjectAttendance = []
		for item in subjectComponentsOfStudent:
			dictOfSingleSubject = {}
			daysAttendanceWasTaken = DaysAttendanceWasTaken.objects.filter(subjectComponents=item.subjectComponents)
			ids = []
			for day in daysAttendanceWasTaken:
				ids.append(day.id)
			absentStudents = Attendance.objects.filter(dayAttendanceWasTaken__in=ids)
			onlyThisStudent = absentStudents.filter(student=student)
			listOfDaysAttendanceWasTaken = []
			for day in daysAttendanceWasTaken:
				date = day.dateOfAttendance
				date = datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%d/%m/%Y')
				listOfDaysAttendanceWasTaken.append(date)
			dictOfSingleSubject['allDaysAttendanceWasTaken'] = listOfDaysAttendanceWasTaken
			ListOfStudentAbsentDates = []
			for day in onlyThisStudent:
				date =  DaysAttendanceWasTaken.objects.get(id=day.dayAttendanceWasTaken.id)
				date = date.dateOfAttendance
				date = datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%d/%m/%Y')
				ListOfStudentAbsentDates.append(date)
			humanReadableInfo = {}
			humanReadableInfo['subjectName'] = item.subjectComponents.subject.subjectName
			humanReadableInfo['subjectID'] = item.subjectComponents.subject.subjectID
			humanReadableInfo['componentID'] = item.subjectComponents.componentID
			humanReadableInfo['sectionID'] = item.subjectComponents.sectionID

			dictOfSingleSubject['student'] = ListOfStudentAbsentDates
			dictOfSingleSubject['info'] = humanReadableInfo
			# dictOfAllSubjectAttendance[item.subjectComponents.id] = dictOfSingleSubject
			listOfAllSubjectAttendance.append(dictOfSingleSubject)
		return Response(listOfAllSubjectAttendance,status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'Only GET request is supported'},status=status.HTTP_400_BAD_REQUEST)


def my_decode_handler(token):
	options = {
		'verify_exp': api_settings.JWT_VERIFY_EXPIRATION,
	}
	print 'I am being used!'
	payload = jwt.decode(
		token,
		api_settings.JWT_SECRET_KEY,
		api_settings.JWT_VERIFY,
		options=options,
		leeway=api_settings.JWT_LEEWAY,
		audience=api_settings.JWT_AUDIENCE,
		issuer=api_settings.JWT_ISSUER,
		algorithms=[api_settings.JWT_ALGORITHM]
	)
	now = timegm(datetime.utcnow().utctimetuple())
	# if int(payload['iat']) < now:
	msg = _('Signature has expired.')
	raise serializers.ValidationError(msg)
	return None
	return payload


@api_view(['GET'])
@authentication_classes([JWTAuthentication,SessionAuthentication,BasicAuthentication,])
@permission_classes([IsAuthenticated,])
def getteacherdetails(request):
	if request.method == 'GET':
		try:
			profile = Profile.objects.get(user=request.user)
			teacher = Teacher.objects.get(teacherID=profile.student_teacher_id)
		except:
			return Response({'id':-2, 'status': 'User has no profile or Teacher does not exist'},status=status.HTTP_400_BAD_REQUEST)
		teacherDetails = {}
		teacherDetails['name'] = teacher.teacherFullName
		teacherDetails['teacherID'] = teacher.teacherID 
		return Response(teacherDetails,status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'Only GET request is supported'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def resetpassword(request):
	"""
	{
		"emailID" :"saurabhmaurya06@gmail.com"
	}
	"""
	if request.method == 'POST':
		try:
			emailID = request.data['emailID']
		except:
			return Response({'id':-1, 'status': 'inaccurate input parameters'},status=status.HTTP_400_BAD_REQUEST)
		print reset_password(emailID,'webmaster@ptmnow.com',request=request)
		return Response({'id':1, 'status': 'success'},status=status.HTTP_201_CREATED)
	return Response({'id':-1 ,'status': 'GET request not supported'},status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.forms import PasswordResetForm

def reset_password(email, from_email,request):
	"""
	Reset the password for all (active) users with given E-Mail adress
	"""
	form = PasswordResetForm({'email': email})
	print 'hello 1'
	if form.is_valid():
		print 'hello 2'
		return form.save(from_email=from_email,request=request,email_template_name='registration/password_reset_email.html')
		print 'hello 3'
	print 'hello 4'