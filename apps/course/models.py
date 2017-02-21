from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
