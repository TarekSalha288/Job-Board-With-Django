from . models import Job
from . serializer import JobSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
@api_view(['GET'])
def jobs(request):
    list=Job.objects.all()
    data=JobSerializer(list,many=True).data
    return Response({'data':data})
@api_view(['GET'])
def job(request,id):
    job=Job.objects.get(id=id)
    data=JobSerializer(job).data
    return Response({'data':data})