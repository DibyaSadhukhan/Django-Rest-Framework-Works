from django.db import models

class User_Details(models.Model):
    gender_choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    Email=models.EmailField(max_length=50,primary_key=True)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    DOB=models.DateField()
    Gender=models.CharField(max_length=1,choices=gender_choices)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name

class Answer(models.Model):
    Option_choices=(
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    )
    question_id=models.CharField(max_length=50)
    user_id=models.CharField(max_length=50)
    submission_id=models.CharField(max_length=50,primary_key=True)
    option_choice= models.CharField(max_length=1,choices=Option_choices)
    Attempt_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_id + 'Attempt for ' + self.question_id