from django.shortcuts import render

from .models import Job

def home(Request):

	jobs = Job.objects
	return render(Request, 'jobs/home.html', {"jobs":jobs})