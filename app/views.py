from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


job_title=[
    'first job',
    'second job'
]
job_description=[
    'frist job description',
    'second job description'
]
# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def job_detail(request,id):
    if id==0:
        return redirect('/')
    return_html=f"<h1>{job_title[id]}</h1><br><br><h3>{job_description[id]}</h3>"
    return HttpResponse(return_html)