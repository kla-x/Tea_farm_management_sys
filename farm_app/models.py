from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    # phone = models.CharField(max_length=20, null=False, blank=False, verbose_name="Phone Number", help_text="Enter the farmer's phone number")


    def __str__(self):
        return self.name

class TeaPlot(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    area = models.DecimalField(max_digits=8, decimal_places=2)
    soil_type = models.CharField(max_length=100)
    number_of_plants = models.PositiveIntegerField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='tea_plots')

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title