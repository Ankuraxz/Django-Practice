from django.db import models


# Create your models here.

# creating model for advertisement
class ads:
    id: int  # Primary ID for db
    name: str  # Advertisement/ Classified Name
    desc: str  # Ad Desc
    img: str  # Image of Ad
class contact(models.Model):
    id: int
    phone: int
    name: str
    email: str
    message: str
