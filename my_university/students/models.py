from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    name = models.CharField(max_length=2000, null=True, blank=True)
    surname = models.CharField(max_length=2000, null=True, blank=True)
    patronymic = models.CharField(max_length=2000, null=True, blank=True)
    email = models.EmailField(max_length=2000, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gpa = models.FloatField(null=True, blank=True)
    course = models.IntegerField(null=True, blank=True)
    faculty = models.CharField(max_length=512, null=True, blank=True)
    education_form = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    @property
    def course_str(self):
        return {
            "1": "First",
            "2": "Second",
            "3": "Third",
            "4": "Fourth",
            "5": "Fifth",
            "6": "Sixth",
        }.get(str(self.course), "First")

    @property
    def full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["surname"]
