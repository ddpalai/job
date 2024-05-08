from django.shortcuts import render
from testapp.models import HydJob, BngJob, PunJob
# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')
def hydjobs_view(request):
    job_list = HydJob.objects.all()
    my_dict = {'job_list':job_list}
    return render(request,'testapp/hyd.html',my_dict)
def bngjob_view(request):
    job_list = BngJob.objects.all()
    my_dict = {'job_list':job_list}
    return render(request,'testapp/bng.html',my_dict)
def punjob_view(request):
    job_list = PunJob.objects.all()
    my_dict = {'job_list':job_list}
    return render(request,'testapp/pun.html',my_dict)