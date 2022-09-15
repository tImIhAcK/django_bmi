from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class BMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.username