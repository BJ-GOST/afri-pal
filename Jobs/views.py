from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.



@api_view(['GET'])
def api_overview(request):
    api_urls= {
        'jobs' : 'Jobs/job-list/',
    
    }
    return Response(api_urls, safe=False)
    
   
   
   
@api_view(['GET'])
def job_list(request):
    jobs= Job.objects.filter(state='pending')
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def previous_jobs(request):
    jobs = Job.objects.filter(state='completed')
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def pending_job_list(request):
    jobs= Job.objects.filter(state='pending')
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def my_jobs(request):
    user = request.user
    jobs = Job.objects.filter(customer=user)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def job_detail(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)
    
    

@api_view(['POST'])
def create_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print('not valid')
    return Response(serializer.data)
    
  
  
@api_view(['POST'])
def job_update(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(request.data, instance=job)
    if serializer.is_valid(): 
        serializer.save()
    return Response(serializer.data)




@api_view(['DELETE'])
def job_delete(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return Response('Job successfully deleted')