from django.shortcuts import render
from Jobs.models import *

# Create your views here.


def detail_view(request, pk):
    job = Job.objects.get(id=pk)
    print(job.title)
    context = {'job':job}
    template_name = 'afripal/job_detail.html'
    return render (request, template_name, context)




def mark(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        job = Job.objects.get(id=job_id)
        if job.state == 'pending':
            job.state = 'completed'
            job.save()
        else:
            pass
    template_name = 'afripal/success.html'
    return render (request, template_name)
