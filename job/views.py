from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.urls import reverse
from . models import Job
from . form import JobApply,AddJob
from . filter import JobFilter
from django.contrib.auth.decorators import login_required
# Create your views here.
def job_list(request):
    jobs=Job.objects.all()
    f=JobFilter(request.GET, queryset=jobs)
    jobs=f.qs
    paginator = Paginator(jobs, 4)  # Show contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj,'f':f}
    return render(request,'job/job_list.html',context)

def job_detail(request,slug):
    job=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=JobApply(request.POST,request.FILES)
        if form.is_valid():
           myform=form.save(commit=False)
           myform.job=job
           myform.save()
           print('after')
    else:
       form =JobApply()
    context={"job":job,'form':form}
    return render(request,'job/job_detail.html',context) 
@login_required
def add_Job(request):
    if request.method=='POST':
       form=AddJob(request.POST,request.FILES) 
       if form.is_valid():
           myform=form.save(commit=False)
           myform.owner=request.user
           myform.save()
           return redirect(reverse('jobs:list'))
    else:
     form=AddJob()
    return render(request,'job/add_job.html',{'form':form})
