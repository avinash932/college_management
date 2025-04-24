from django.db import models

# Create your models here.
class students_records(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    course = models.CharField(max_length=10, blank=True)
    branch = models.CharField(max_length=20, blank=True)  # Add this
    year = models.IntegerField(default=1)                 # Add this
    address = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    fee_status = models.CharField(max_length=10, default='Paid')  # Paid / Pending / Overdue


    def __str__(self):
        return self.name