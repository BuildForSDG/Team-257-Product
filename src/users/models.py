from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Hospital(models.Model):
    hospitalName = models.CharField(max_length=200)
    hospitalType = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.hospitalName}({self.hospitalType})"


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



