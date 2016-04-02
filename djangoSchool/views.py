from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,Http404
from django.template.context import RequestContext

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json,httplib,urllib
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from attendance.models import ListOfClasses
from mywrapper.models import *



# Create your views here.

@login_required
def home(request):
	# latest_class_list = ListOfClasses.objects.filter(schoolUser=request.user)	
	latest_class_list = Subject.objects.all()
	classLinks = [p.id for p in latest_class_list]
	classNames = [p.subjectName for p in latest_class_list]
	zipped_data = zip(classLinks, classNames)
	context = {'item1':"My first string",'classLinks':classLinks,'classNames':classNames,'zipped_data':zipped_data}
	return render(request,'attendance/listSubject.html',context)

