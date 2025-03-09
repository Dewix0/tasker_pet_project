from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta


class Task(models.Model):
    STATUS_CHOICES = [
        ("NS", "Not started"),
        ("ACT", "Active"),
        ("DN", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]

    def default_deadline():
        return date.today() + timedelta(days=7)

    Task_ID = models.AutoField(primary_key=True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="NS")
    Description = models.TextField()
    Priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="H")
    Deadline = models.DateField(default=default_deadline)

    def __str__(self):
        return f"Task {self.Task_ID} - {self.Status}"
