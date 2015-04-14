from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime
import os.path

class Category(models.Model):
  title = models.CharField(max_length = 50, verbose_name = "Main Category")

  def __unicode__(self):
   return self.title

class SubCategory(models.Model):
  title = models.CharField(max_length = 50, verbose_name = "Sub Category")

  def __unicode__(self):
    return self.title

class ProductPicture(models.Model):
  docfile = models.FileField(upload_to = "products", verbose_name = "Product Picture")
  def filename(self):
    return os.path.basename(self.docfile.name)

class Listing(models.Model):
  FREQ_CHOICES = (
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly'),
    ('Q', 'Quarterly'),
    ('S', 'Semi-Annually'),
    ('A', 'Annually'),
  )

  owner = models.ForeignKey(User, verbose_name="Listing Owner")
  title = models.CharField(max_length = 144, default = "Product Title")
  webpage = models.URLField(verbose_name="Listing Webpage", blank=True, null=True)
  category = models.ForeignKey(Category, verbose_name="Category", blank=True, null=True)
  subCategory = models.ForeignKey(SubCategory, verbose_name="Sub Category", blank=True, null=True)
  webpage = models.URLField(verbose_name="Listing Webpage", blank=True, null=True)
  description = models.TextField(verbose_name="Listing Description", blank=True, null=True)
  price = models.DecimalField(max_digits=9, decimal_places=2 , verbose_name="Price", blank=True, null=True)
  rating = models.DecimalField(max_digits=4, decimal_places=2 , verbose_name="Rating", default=0)
  freqType = models.CharField(max_length = 2, verbose_name = "Frequency Type", choices = FREQ_CHOICES, default = "M")
  pic = models.ForeignKey(ProductPicture, verbose_name = "Product Picture", blank = True, null = True)

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ['title']


class ListingForm(ModelForm):
  class Meta:
    model=Listing
    exclude=('rating', 'owner', 'subCategory', 'pic')

  def __init__(self, *args, **kwargs):
    self.request = kwargs.pop('request', None)
    super(ListingForm, self).__init__(*args, **kwargs)


class PictureForm(ModelForm):
  class Meta:
    model = ProductPicture
    fields = ('docfile',)
