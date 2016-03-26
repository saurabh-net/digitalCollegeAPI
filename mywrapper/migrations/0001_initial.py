# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='DaysAttendanceWasTaken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateOfAttendance', models.DateField()),
                ('timeAttendanceWasMarked', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentMarks', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('timeNoticeWasMarked', models.DateTimeField(auto_now_add=True)),
                ('is_sms', models.BooleanField(default=False)),
                ('is_email', models.BooleanField(default=False)),
                ('is_push', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=True)),
                ('is_administrator', models.BooleanField(default=False)),
                ('student_teacher_id', models.CharField(unique=True, max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentID', models.CharField(unique=True, max_length=50)),
                ('studentFullName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('emailID', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('gcm_registration_id', models.TextField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subjectID', models.CharField(unique=True, max_length=50)),
                ('subjectName', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectComponents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sectionID', models.CharField(max_length=50)),
                ('componentID', models.CharField(max_length=50)),
                ('subject', models.ForeignKey(to='mywrapper.Subject')),
            ],
            options={
                'ordering': ['componentID', 'sectionID'],
            },
        ),
        migrations.CreateModel(
            name='SubjectsPerStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.ForeignKey(to='mywrapper.Student')),
                ('subjectComponents', models.ForeignKey(to='mywrapper.SubjectComponents')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectsPerTeacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subjectComponents', models.ForeignKey(to='mywrapper.SubjectComponents')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacherID', models.CharField(unique=True, max_length=50)),
                ('teacherFullName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('emailID', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('gcm_registration_id', models.TextField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('totalMarks', models.CharField(max_length=50)),
                ('testType', models.CharField(max_length=100)),
                ('dateOfTest', models.DateField()),
                ('timeTestWasMarked', models.DateTimeField(auto_now_add=True)),
                ('subjectComponents', models.ForeignKey(to='mywrapper.SubjectComponents')),
            ],
        ),
        migrations.AddField(
            model_name='subjectsperteacher',
            name='teacher',
            field=models.ForeignKey(to='mywrapper.Teacher'),
        ),
        migrations.AddField(
            model_name='notice',
            name='classToSendNotice',
            field=models.ForeignKey(to='mywrapper.SubjectComponents'),
        ),
        migrations.AddField(
            model_name='notice',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='marks',
            name='student',
            field=models.ForeignKey(to='mywrapper.Student'),
        ),
        migrations.AddField(
            model_name='marks',
            name='test',
            field=models.ForeignKey(to='mywrapper.Test'),
        ),
        migrations.AddField(
            model_name='daysattendancewastaken',
            name='subjectComponents',
            field=models.ForeignKey(to='mywrapper.SubjectComponents'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='dayAttendanceWasTaken',
            field=models.ForeignKey(to='mywrapper.DaysAttendanceWasTaken'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='mywrapper.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='test',
            unique_together=set([('subjectComponents', 'totalMarks', 'testType', 'dateOfTest')]),
        ),
        migrations.AlterUniqueTogether(
            name='subjectsperteacher',
            unique_together=set([('teacher', 'subjectComponents')]),
        ),
        migrations.AlterUniqueTogether(
            name='subjectsperstudent',
            unique_together=set([('subjectComponents', 'student')]),
        ),
        migrations.AlterUniqueTogether(
            name='subjectcomponents',
            unique_together=set([('subject', 'sectionID', 'componentID')]),
        ),
        migrations.AlterUniqueTogether(
            name='marks',
            unique_together=set([('student', 'test', 'studentMarks')]),
        ),
        migrations.AlterUniqueTogether(
            name='daysattendancewastaken',
            unique_together=set([('subjectComponents', 'dateOfAttendance')]),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('student', 'dayAttendanceWasTaken')]),
        ),
    ]
