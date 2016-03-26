from rest_framework import serializers
from django.contrib.auth.models import User
from mywrapper.models import Subject, SubjectComponents,Student,Teacher, SubjectsPerStudent,SubjectsPerTeacher, Attendance,DaysAttendanceWasTaken,Test,Marks, Profile, Notice

class SubjectSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Subject
		fields = ('id','subjectID','subjectName')

class SubjectComponentsSerializer(serializers.ModelSerializer):
	subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
	id = serializers.ReadOnlyField()
	class Meta:
		model = SubjectComponents
		fields = ('id','subject','sectionID','componentID')


class ReadSubjectComponentsSerializer(serializers.ModelSerializer):
	subject = SubjectSerializer(read_only=True)
	id = serializers.ReadOnlyField()
	class Meta:
		model = SubjectComponents
		fields = ('id','subject','sectionID','componentID')

class DetailedSubjectComponentsSerializer(serializers.ModelSerializer):
	# subject = SubjectSerializer(read_only=True)
	id = serializers.ReadOnlyField()
	class Meta:
		model = SubjectComponents
		fields = ('id','sectionID','componentID')

class DetailedSubjectSerializer(serializers.ModelSerializer):
	subjectcomponents_set = DetailedSubjectComponentsSerializer(read_only=True,many=True)
	id = serializers.ReadOnlyField()
	class Meta:
		model = Subject
		fields = ('id','subjectID','subjectName', 'subjectcomponents_set')

class StudentSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Student
		fields = ('id','studentID','studentFullName','phoneNumber','emailID')

class ReadStudentSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Student
		fields = ('id','studentID','studentFullName','phoneNumber','emailID')

class TeacherSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Teacher
		fields = ('id','teacherID','teacherFullName','phoneNumber','emailID')

class SubjectsPerTeacherSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	class Meta:
		model = SubjectsPerTeacher
		fields = ('id','teacher','subjectComponents')

class ReadSubjectsPerTeacherSerializer(serializers.ModelSerializer):
	# id = serializers.ReadOnlyField()
	# teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
	# subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	subjectComponents = ReadSubjectComponentsSerializer(read_only=True)
	class Meta:
		model = SubjectsPerTeacher
		fields = ('subjectComponents',)

class SubjectsPerStudentSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	class Meta:
		model = SubjectsPerStudent
		fields = ('id','student','subjectComponents')

class ReadSubjectsPerStudentSerializer(serializers.ModelSerializer):
	student = ReadStudentSerializer(read_only=True)
	class Meta:
		model = SubjectsPerStudent
		fields = ('student',)

# class AttendanceSerializer(serializers.ModelSerializer):
# 	id = serializers.ReadOnlyField()
# 	student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
# 	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
# 	dateOfAttendance = serializers.DateField(input_formats = ('%d/%m/%Y',))
# 	class Meta:
# 		model = Attendance
# 		fields = ('id','student', 'subjectComponents', 'dateOfAttendance')

class DaysAttendanceWasTakenSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	dateOfAttendance = serializers.DateField(input_formats = ('%d/%m/%Y',))
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	class Meta:
		model = DaysAttendanceWasTaken
		fields = ('id','subjectComponents', 'dateOfAttendance')

class AttendanceSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
	dayAttendanceWasTaken = serializers.PrimaryKeyRelatedField(queryset=DaysAttendanceWasTaken.objects.all())
	class Meta:
		model = Attendance
		fields = ('id','student', 'dayAttendanceWasTaken')

class TestSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	dateOfTest = serializers.DateField(input_formats = ('%d/%m/%Y',))
	class Meta:
		model = Test
		fields = ('id','subjectComponents','totalMarks','testType','dateOfTest')

class MarksSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	test = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all())
	student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
	class Meta:
		model = Marks
		fields = ('id','student','test','studentMarks')

class ProfileSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Profile
		fields = ('id','user','is_teacher','is_student','is_administrator','student_teacher_id')

class UserSerializer(serializers.ModelSerializer):
	# notice = serializers.PrimaryKeyRelatedField(many=True, queryset=Notice.objects.all())
	profile = ProfileSerializer(read_only=True)
	class Meta:
		model = User
		fields = ('id', 'username','profile')

class NoticeSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	timeNoticeWasMarked = serializers.ReadOnlyField()
	classToSendNotice = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Notice
		fields = ('id','message','classToSendNotice','owner','timeNoticeWasMarked','is_sms','is_push','is_email')


