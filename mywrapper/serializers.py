from rest_framework import serializers
from django.contrib.auth.models import User
from mywrapper.models import Subject, Student, SubjectsPerStudent, Attendance,DaysAttendanceWasTaken,Test,Marks

class SubjectSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Subject
		fields = ('id','subjectID', 'sectionID')

class StudentSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Student
		fields = ('id','studentID')

class AttendanceSerializer(serializers.ModelSerializer):
	dateOfAttendance = serializers.DateField(input_formats = ('%d/%m/%Y',))
	class Meta:
		model = Attendance
		fields = ('studentID', 'subjectID', 'dateOfAttendance')

class DaysAttendanceWasTakenSerializer(serializers.ModelSerializer):
	dateOfAttendance = serializers.DateField(input_formats = ('%d/%m/%Y',))
	class Meta:
		model = DaysAttendanceWasTaken
		fields = ('subjectID', 'dateOfAttendance')

class TestSerializer(serializers.ModelSerializer):
	dateOfTest = serializers.DateField(input_formats = ('%d/%m/%Y',))
	class Meta:
		model = Test
		fields = ('subjectID','totalMarks','testType','dateOfTest')

class MarksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Marks
		fields = ('studentID','studentMarks','miscDetails')

class SubjectsPerStudentSerializer(serializers.ModelSerializer):
	studentID = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
	subjectID = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
	class Meta:
		model = SubjectsPerStudent
		fields = ('studentID','subjectID')

class UserSerializer(serializers.ModelSerializer):
	# notice = serializers.PrimaryKeyRelatedField(many=True, queryset=Notice.objects.all())
	class Meta:
		model = User
		fields = ('id', 'username')