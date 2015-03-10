from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime


class Listing(models.Model):
  owner = models.ForeignKey(User, verbose_name="Listing Owner")
  title = models.CharField(max_length = 144, default = "Product Title")
  webpage = models.URLField(verbose_name="Listing Webpage", blank=True, null=True)
  description = models.TextField(verbose_name="Listing Description", blank=True, null=True)
  price = models.DecimalField(max_digits=9, decimal_places=2 , verbose_name="Price", blank=True, null=True)
  rating = models.DecimalField(max_digits=4, decimal_places=2 , verbose_name="Rating", default=0)

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ['title']


class ListingForm(ModelForm):
  class Meta:
    model=Listing
    exclude=('rating', 'owner',)

  def __init__(self, *args, **kwargs):
    self.request = kwargs.pop('request', None)
    super(ListingForm, self).__init__(*args, **kwargs)
