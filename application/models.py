from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

class CustomUser(AbstractUser):# jo User table me phle fields thi uske sath ab ye new fields jo di hai add ho jaengi
    phone = models.CharField(max_length=12) # or iske liye hme setting.py me jakr USER_ATH ko override kra hai
    profile = models.ImageField(upload_to="static/")#AUTH_USER_MODEL = 'application.CustomUser' # app ka nam . class ka nam
    user_types = (
        ("student","student"),
        ("professor","professor"),
        ("director","director"),
    )
    user_type = models.CharField(max_length=15,choices=user_types,default = "student")



    