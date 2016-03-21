from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
	subjectID = models.CharField(max_length=50,unique=True)
	subjectName = models.CharField(max_length=100,default=None, blank=True)
	def __str__(self):
		return '%s' % (self.subjectID)


class SubjectComponents(models.Model):
	subject = models.ForeignKey(Subject)
	sectionID = models.CharField(max_length=50)
	componentID = models.CharField(max_length=50) #Make choices?
	def __str__(self):
		return '%s %s %s' % (self.subject,self.sectionID,self.componentID)
	class Meta:
		unique_together = ('subject', 'sectionID','componentID')

class Student(models.Model):
	studentID = models.CharField(unique=True,max_length=50)
	studentFullName = models.CharField(max_length=100)
	phoneNumber = models.CharField(max_length=20,default=None, blank=True)
	emailID = models.CharField(max_length=100,default=None, blank=True)
	def __str__(self):
		return '%s' % (self.studentID)

class Teacher(models.Model):
		teacherID = models.CharField(unique=True,max_length=50)
		teacherFullName = models.CharField(max_length=100)
		phoneNumber = models.CharField(max_length=20,default=None, blank=True)
		emailID = models.CharField(max_length=100,default=None, blank=True)
		def __str__(self):
			return '%s' % (self.teacherID)

class SubjectsPerTeacher(models.Model):
	teacher = models.ForeignKey(Teacher)
	subjectComponents = models.ForeignKey(SubjectComponents)
	def __str__(self):
		return '%s %s' % (self.teacher, self.subjectComponents) # Might need to change
	class Meta:
		unique_together = ('teacher', 'subjectComponents')

class SubjectsPerStudent(models.Model):
	student = models.ForeignKey(Student)
	subjectComponents = models.ForeignKey(SubjectComponents)
	def __str__(self):
		return '%s %s' % (self.student, self.subjectComponents) # Might need to change
	class Meta:
		unique_together = ('subjectComponents', 'student')

class DaysAttendanceWasTaken(models.Model):
	subjectComponents = models.ForeignKey(SubjectComponents)
	dateOfAttendance = models.DateField()
	timeAttendanceWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)
	class Meta:
		unique_together = ('subjectComponents', 'dateOfAttendance')

class Attendance(models.Model):
	student = models.ForeignKey(Student)
	dayAttendanceWasTaken = models.ForeignKey(DaysAttendanceWasTaken)
	class Meta:
		unique_together = ('student', 'dayAttendanceWasTaken')

class Test(models.Model):
	subjectComponents  = models.ForeignKey(SubjectComponents)
	totalMarks = models.CharField(max_length=50)
	testType   = models.CharField(max_length=100)
	dateOfTest = models.DateField()
	timeTestWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)
	def __str__(self):
		return '%s %s %s' % (self.subjectComponents, self.testType,self.dateOfTest)
	class Meta:
		unique_together = ('subjectComponents', 'totalMarks','testType','dateOfTest')

class Marks(models.Model):
	student      = models.ForeignKey(Student)
	test         = models.ForeignKey(Test)
	studentMarks = models.CharField(max_length=50) # support for both grade and marks type. Not it is not an integer
	class Meta:
		unique_together = ('student', 'test','studentMarks') # is this neccessary?

class Profile(models.Model):
    user = models.OneToOneField(User)
    # department = models.CharField(max_length=200, default='Computer Science')
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_administrator = models.BooleanField(default=False)
    student_teacher_id = models.CharField(unique=True,max_length=50)
