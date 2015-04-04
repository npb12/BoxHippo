from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  companyName = models.CharField(max_length = 144, blank=True, null=True, verbose_name = "Company Name")
  website = models.URLField(verbose_name = "Website", blank=True, null=True)
  facebook = models.URLField(verbose_name = "Facebook Page", blank=True, null=True)
  email = models.EmailField(verbose_name = "Email", blank=False)
  hideEmail = models.BooleanField(default=True, verbose_name="Hide Email?")
  maxListings = models.IntegerField(default=0, verbose_name = "Maximum Listings")

  def __unicode__(self):
    return self.user.username

  class Meta:
    ordering = ['companyName']


class ProfileForm(ModelForm):
  class Meta:
    model = UserProfile
    exclude = ('user','maxListings')

  def __init__(self, *args, **kwargs):
    self.request = kwargs.pop('request', None)
    super(ProfileForm, self).__init__(*args, **kwargs)


class UserEditForm(ModelForm):
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name',)

  def __init__(self, *args, **kwargs):
    self.request = kwargs.pop('request', None)
    super(UserEditForm, self).__init__(*args, **kwargs)


# Create your models here.
