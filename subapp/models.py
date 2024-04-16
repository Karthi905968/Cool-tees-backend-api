from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class PostModel(models.Model):
    class Meta:
        db_table='post'
    
    name = models.CharField(
        'Name',max_length=100,blank=False,default='Anonymous',null=True,db_index=True
    )

    body= models.TextField(
        'Body',blank=True,null=False,db_index=True
    )

    image = CloudinaryField(
        'Image',blank=True,null=True
    )

    count = models.PositiveIntegerField(
        'Count' , default=0 ,blank=False 
    )

    created_at = models.DateTimeField(
       'Created DateTime' , auto_now_add=True , blank=True
    )

    updated_at = models.DateTimeField(
       'Updated DateTime' , auto_now=True , blank=True
    )

    


