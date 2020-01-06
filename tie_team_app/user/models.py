from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

objects = models.Manager()

#Create a Basemodel 
class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_time']
    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        raise NotImplementedError

#Create Member stats link back to each individual User
class stats(BaseModel):
    #stats is map to the User's table id column. 
    user = models.ForeignKey(to=User,to_field='id',on_delete=models.CASCADE)
    mesh_ip = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    mesh = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    gas = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    water = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    DA = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    PLX = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    database = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    class Meta:
        verbose_name_plural = 'User Stats'
    def __str__(self):
        #not sure why this 'username' is mark as incorrect but it is behaving just fine. So ignore it 
        return self.user.username

class ImgInfo(BaseModel):
        user = models.ForeignKey(to=User,to_field='id',on_delete=models.CASCADE)
        position_icon_addr = models.CharField(max_length=200)
        profile_pic_addr = models.CharField(max_length=200)
        stat_graph_addr = models.CharField(max_length=200)
        def __str__(self):
            return "img addr info"




      

    


