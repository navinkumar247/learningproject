from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
User = get_user_model()

class Group(models.Model):
    name = models.CharField(blank=False, max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    description = models.CharField(blank=True, max_length=255)
    member = models.ManyToManyField(User,through='GroupMember')
    # owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups:joingroup',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-created_at']

class GroupMember(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'membership')
    group = models.ForeignKey(Group, related_name = 'user_group',on_delete=models.CASCADE)
    # ownership = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ['user','group']

# class GroupOwner(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'ownership')
#     owner_group = models.ForeignKey(GroupMember,related_name = 'owner_membership',on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.user.username
#
#     class Meta:
#         unique_together = ['user','owner_group']
