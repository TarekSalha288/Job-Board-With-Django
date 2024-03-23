from django.urls import path
from . import views
from . import api
app_name="jobs"
urlpatterns = [
    path('',views.job_list,name='list'),
    path('add',views.add_Job,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_detail'),
     path('jobs/list',api.jobs,name='jobs'),
      path('jobs/<int:id>',api.job,name='job')

] 