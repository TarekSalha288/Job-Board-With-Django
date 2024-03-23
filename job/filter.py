import django_filters
from . models import Job
class JobFilter(django_filters.FilterSet):
    descreption = django_filters.CharFilter(lookup_expr='icontains')
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['salary', 'job_type','experience','category','descreption','title']