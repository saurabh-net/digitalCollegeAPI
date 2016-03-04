from django.db import models
# from model_utils.managers import PassThroughManager
# Create your models here.
# This is without generalizing the sections! 
# Do a model with them generalized as well

class Subject(models.Model):
	subjectID = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.subjectID)

class SubjectComponents(models.Model):
	subject = models.ForeignKey(Subject)
	sectionID = models.CharField(max_length=50)
	componentID = models.CharField(max_length=50) #Make choices?
	def __str__(self):
		return '%s %s %s' % (self.subject,self.sectionID,self.componentID)

class Student(models.Model):
	studentID = models.CharField(unique=True,max_length=50)
	def __str__(self):
		return '%s' % (self.studentID)

class Teacher(models.Model):
		teacherID = models.CharField(unique=True,max_length=50)
		def __str__(self):
			return '%s' % (self.teacherID)

class SubjectsPerTeacher(models.Model):
	teacher = models.ForeignKey(Teacher)
	subjectComponents = models.ForeignKey(SubjectComponents)
	def __str__(self):
		return '%s %s' % (self.teacher, self.subjectComponents) # Might need to change

class SubjectsPerStudent(models.Model):
	student = models.ForeignKey(Student)
	subjectComponents = models.ForeignKey(SubjectComponents)
	def __str__(self):
		return '%s %s' % (self.student, self.subjectComponents) # Might need to change

class Attendance(models.Model):
	student = models.ForeignKey(Student)
	subjectComponents = models.ForeignKey(SubjectComponents)
	dateOfAttendance = models.DateField()
	timeAttendanceWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)

class DaysAttendanceWasTaken(models.Model):
	subjectComponents = models.ForeignKey(SubjectComponents)
	dateOfAttendance = models.DateField()
	timeAttendanceWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)

class Test(models.Model):
	subjectComponents  = models.ForeignKey(SubjectComponents)
	totalMarks = models.CharField(max_length=50)
	testType   = models.CharField(max_length=50)
	dateOfTest = models.DateField()
	timeTestWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)
	def __str__(self):
		return '%s %s %s' % (self.subjectComponents, self.testType,self.dateOfTest)

class Marks(models.Model):
	student      = models.ForeignKey(Student)
	test         = models.ForeignKey(Test)
	studentMarks = models.CharField(max_length=10) # support for both grade and marks type. Not it is not an integer
	# class Meta:
	# 	unique_together = ('studentID', 'miscDetails','studentMarks') # is this neccessary?



# Integrity Check at application level that the student is actually enrolled in that class    	

# class Notice(models.Model):
# 	category = models.CharField(max_length=50)
# 	message = models.CharField(max_length=800)
# 	timeNoticeWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)
# 	classToSendNotice = models.ForeignKey(Grade) # It is the fully qualified class, e.g. 5A
# 	owner = models.ForeignKey('auth.User')

# TO DO: Marks | Service Layer





# class TodoQuerySet(models.query.QuerySet):
#     def incomplete(self):
#         return self.filter(is_done=False)

#     def high_priority(self):
#         return self.filter(priority=1)

# class Todo(models.Model):
#     content = models.CharField(max_length=100)
#     # other fields go here..

#     objects = PassThroughManager.for_queryset_class(TodoQuerySet)()