from django.db import models
# from model_utils.managers import PassThroughManager
# Create your models here.
# This is without generalizing the sections! 
# Do a model with them generalized as well

class Subject(models.Model):
	subjectID = models.CharField(max_length=50)
	sectionID = models.CharField(max_length=20)
	class Meta:
		unique_together = ('subjectID', 'sectionID')

class Student(models.Model):
	studentID = models.CharField(unique=True,max_length=50)

class SubjectsPerStudent(models.Model):
	studentID = models.ForeignKey(Student)
	subjectID = models.ForeignKey(Subject)

class Attendance(models.Model):
	studentID = models.ForeignKey(Student)
	subjectID = models.ForeignKey(Subject)
	dateOfAttendance = models.DateField()
	timeAttendanceWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)

class DaysAttendaceWasTaken(models.Model):
	subjectID = models.ForeignKey(Subject)
	dateOfAttendance = models.DateField()
	timeAttendanceWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)

class Test(models.Model):
	subjectID  = models.ForeignKey(Subject)
	totalMarks = models.CharField(max_length=10)
	testType   = models.CharField(max_length=50)
	dateOfTest = models.DateField()
	timeTestWasMarked = models.DateTimeField(auto_now=False, auto_now_add=True)

class Marks(models.Model):
	studentID    = models.ForeignKey(Student)
	miscDetails  = models.ForeignKey(Test)
	studentMarks = models.CharField(max_length=10) # support for both grade and marks type. Not it is not an integer


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