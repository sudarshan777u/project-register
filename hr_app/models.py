from django.db import models

# Create your models here.

from datetime import datetime
from django.utils import timezone

class registration(models.Model):
    Name=models.CharField(max_length=100)
    Primary_contact=models.CharField(max_length=13)
    Secondary_contact=models.CharField(max_length=13)
    Location=models.CharField(max_length=1000,default=" ")
    Email_Id=models.EmailField()
    Current_CTC=models.CharField(max_length=50)
    Expected_CTC=models.CharField(max_length=50)
    Notice_Period=models.CharField(max_length=50)
    Current_designation=models.CharField(max_length=100,default=' ')
    Applied_designation=models.CharField(max_length=100,default=' ')
    experience=models.CharField(max_length=100)
    General_Skills=models.TextField()
    Technical_Skills=models.TextField()
    Soft_Skills=models.TextField()
    Job_portal_source=models.CharField(max_length=100)
    Contacted_by=models.CharField(max_length=100)
    current_datetime = timezone.localtime(timezone.now())
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %I:%M')
    
    created_at = models.CharField(max_length=50,default=formatted_datetime[0:17])

    def __str__(self):
        return self.Email_Id
    
    
from django.core.validators import MinValueValidator, MaxValueValidator
class Review(models.Model):
    
    user_name=models.OneToOneField(registration,on_delete=models.CASCADE)
    Moral_character=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Moral Character out of 10")
    punctuality=models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Punctuality out of 10")
    health=models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Health out of 10")
    behaviour=models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Behaviour out of 10",null=True)
    attitude=models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" marks out of 10")
    Career_goals=models.CharField(max_length=100)
    understanding_level=models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Understanding level out of 10")
    possitive_attitude_and_mind=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Possitive attitude and mind out of 10",null=True)
    executive=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Executive out of 10",null=True)
    responsibility=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Responsibility out of 10")
    response_ability=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Response Ability out of 10")
    team_handling=models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Team handling out of 10")
    planing=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Planing out of 10")
    communicate_ability=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Communicate Ability out of 10")
    passion=models.CharField(max_length=100)
    confidence=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Confidence out of 10")
    profissional_background=models.CharField(max_length=100)
    work_experience=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(25)],
                                        help_text=" Work Experience Max 25 Years")
    knowledge_level=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text=" Knowledge Level out of 10")
    english_skils=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        help_text="English Skils out of 10")
    other_languages=models.CharField(max_length=1000,default=' ')
    c=[
        (" "," "),
        ("yes","yes"),
        ("no","no")
       ]
    consider_to_client=models.CharField(max_length=10,default=' ',choices=c)
    
    Internal_hiring=models.CharField(max_length=10,default=' ',choices=c)
    reject=models.CharField(max_length=10,default=' ',choices=c)
    current_datetime = timezone.localtime(timezone.now())
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %I:%M:%S %p')
    created_at = models.CharField(max_length=50,default=formatted_datetime)
    remarks=models.TextField()
    
    class Meta:
        ordering = ['user_name']

    def __str__(self):
        return f"{self.user_name.Name}"
    
