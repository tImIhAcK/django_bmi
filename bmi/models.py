from django.db import models
from django.contrib.auth.models import User

class BMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    weight = models.FloatField(verbose_name='weight')
    height = models.FloatField(verbose_name='height')
    bmi = models.FloatField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ('user',)
        