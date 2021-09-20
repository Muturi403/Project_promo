from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from cloudinary.models import CloudinaryField

class Projects(models.Model):
  title = models.CharField(max_length=200)
  # image = models.ImageField(upload_to='project/', null=True, blank=True)
  image = CloudinaryField('project/', null=True, blank=True)
  projectowner = models.ForeignKey(User, on_delete=models.CASCADE)
  description = HTMLField(null=True, blank=True)
  livelink = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.title

  def save_project(self):
    self.save()

  @classmethod
  def delete_project(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def update_description(cls, id, description):
    cls.objects.filter(id=id).update(description=description)
  
  @classmethod
  def user_projects(cls, username):
    projects = cls.objects.filter(projectowner__username=username)
    return projects

  @classmethod
  def all_projects(cls):
    allprojects = cls.objects.all()
    return allprojects

  @classmethod
  def searchProjects(cls, searchterm):
    searchresults = cls.objects.filter(Q(title__icontains=searchterm) | Q(description__icontains=searchterm) | Q(projectowner__username__icontains=searchterm))
    return searchresults

  class Meta:
    ordering = ['-id']
