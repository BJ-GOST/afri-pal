from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


# Create your models here.
STATES= (
('pending', 'pending'),
('completed', 'completed')
)


class Job(models.Model):
    customer =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author', null=True)
    name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    #timestamp= models.DateTimeField(auto_now_add=True, null=True)
    day = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    state = models.CharField(max_length=255, default='pending', choices=STATES)
    payment = models.CharField(max_length=255, default='pending', choices=STATES)
    budget = models.IntegerField(null=True)
    due_date = models.DateTimeField(null=True)
    job_file = CloudinaryField("Image", resource_type="auto", null=True, blank=True)

    def __str__(self):
        return str(self.title)
    