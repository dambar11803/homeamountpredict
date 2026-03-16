from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

SEX_CHOICES=[("Male", "Male"),
             ("Female", "Female")]

MARITAL_STATUS= [("Married","Married"),
                 ("Unmarried", "Unmarried")]

LOAN_TENURE = [(10, 10),
               (15, 15)]

class ClientDetails(models.Model):
    name = models.CharField(max_length=100, default='Ram Rai')
    sex=models.CharField(max_length=8, choices=SEX_CHOICES, default="Male")
    marital= models.CharField(max_length=20, choices=MARITAL_STATUS, default= "Married")
    age = models.PositiveIntegerField(default= 18, validators=[MinValueValidator(18), MaxValueValidator(69)])
    salary= models.FloatField(blank=True, default=5000)
    family_income= models.FloatField(blank=True, default= 0.0)
    home_value = models.FloatField(blank= True, default=571429, validators=[MinValueValidator(571429), MaxValueValidator(14500000)])
    tenure= models.PositiveIntegerField(choices=LOAN_TENURE, default= 15)
    interest= models.FloatField(default = 9.41)
    
    
  
    
    


