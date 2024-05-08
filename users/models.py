from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='users/', blank=True)
    
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        verbose_name_plural = 'Users'
        verbose_name = 'User'



class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'
