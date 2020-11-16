from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#on_delete tells django what todo if prof is deleted. 
    #CASCADE will delete it if user idis deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #prints pratik profile


    def save(self):#making this to add more functionality
    	super().save() # super runs the method of parent class. 
       #here save of parent class

    	img = Image.open(self.image.path)

    	if img.height >300 or img.width >300:
    		output_size = (300,300)
    		img.thumbnail(output_size)
    		img.save(self.image.path)
    		