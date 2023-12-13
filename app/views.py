from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

from app.models import JobPost


def index(request):
    # template=loader.get_template('app/index.html')
    context={"name":"Kamalesh"}
    # return HttpResponse(template.render(context,request))
    return render(request,'app/index.html',context)


job_title=[
    'first job',
    'second job',
    'third job'
]
job_description=[
    'frist job description',
    'second job description',
    'third job description'
]
# Create your views here.
def job_list(request):
    jobs= JobPost.objects.all()
    context={'jobs':jobs}
    return render(request,'app/job_list.html',context)
    # list_of_jobs="<ul>"
    # for i in job_title:
    #     job_id=job_title.index(i)
    #     detail_url=reverse('jobs_detail',args=(job_id,))
    #     list_of_jobs+=f"<li><a href='{detail_url}'>{i}</a></li>"
    # list_of_jobs+="</ul>"
    # return HttpResponse(list_of_jobs)

def job_detail(request,id):
    try:
        print("id",id)
        job= JobPost.objects.filter(id=id)
        print("job",job[0].title)
        context={"job_title":job[0].title,"job_description":job[0].description}
        return render(request,'app/job_detail.html',context)
        
        
    except:
        return HttpResponseNotFound("Not Found")