from django.db import models


# Create your models here.

# creating model for advertisement
class ads:
    id: int  # Primary ID for db
    name: str  # Advertisement/ Classified Name
    desc: str  # Ad Desc
    img: str  # Image of Ad
class contact(models.Model):
    phone: models.BigIntegerField(max_length=10)
    name: models.CharField(max_length=50)
    email: models.EmailField(max_length=100)
    message: models.TextField()
