from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dayoff(models.Model):
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    reason = models.CharField(max_length=255)
    
    TYPES = (
        ('01', 'ลากิจ'),
        ('02', 'ลาป่วย'),
    )
    type = models.CharField(max_length=2, choices=TYPES, default='01')

    date_start = models.DateField()
    date_end = models.DateField()

    A_STATUS = (
        ('w8', 'รอการอนุมัติ'),
        ('no', 'ไม่อนุมัติ'),
        ('ok', 'อนุมัติ'),
    )
    approve_status = models.CharField(max_length=2, choices=A_STATUS, default='w8')

    def status_text(self):
        for s in self.A_STATUS:
            if self.approve_status == s[0]:
                return s[1]