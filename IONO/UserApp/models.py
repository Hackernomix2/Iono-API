from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, null=True)
    gender = models.CharField(max_length=10, null=True)
    # id (AutoField): 
    # password (CharField): Stores the hashed password.
    # username (CharField): The username field used for authentication.
    # first_name (CharField): The user's first name.
    # last_name (CharField): The user's last name.
    # email (EmailField): The user's email address.
    
    #are all present in the abstractuser class and more 



    
    