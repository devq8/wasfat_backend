from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete= models.CASCADE,
        primary_key=True,
    )
    image = models.ImageField(upload_to='images/profile', blank=True,)

    def __str__(self) :
        return self.user.get_username()
    
# class UserFollowing(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='following',
#     )
#     following_user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='followers',
#     )
