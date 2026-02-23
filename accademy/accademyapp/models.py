from django.db import models
from django.core.validators import RegexValidator


phone_validator = RegexValidator(r'^\d{10}$', "Enter valid 10 digit number")


class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in months")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mob_no = models.CharField(max_length=10, validators=[phone_validator], unique=True)
    address = models.CharField(max_length=100)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return self.name
