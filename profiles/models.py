from curses.ascii import US
from django.db import models
from accounts.models import User

class PatientProfile(models.Model):

    BLOOD_GROUPS = [
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, 
        primary_key=True, limit_choices_to={'user_type': 'P'}, 
        related_name='patprofile', #* related_name is used to give alternate name to the reverse relationship
        )
    profile_pic = models.ImageField(upload_to='images/profiles/patients', null=True, blank=True)
    dob = models.DateField(blank=True, null=True) #TODO -remove blank=True, null=True
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    allergies = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"