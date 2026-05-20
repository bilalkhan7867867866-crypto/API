from django.db import models
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.IntegerField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name