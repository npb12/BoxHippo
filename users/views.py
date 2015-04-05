from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from users.models import UserEditForm, ProfileForm, UserProfile
from listings.models import Listing
import string
import random, ast

import subprocess
from subprocess import Popen, PIPE

base_url = "http://.boxhippo.com/whmcs/includes/api.php"

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      profile = UserProfile(user = new_user)
      profile.email = new_user.username
      profile.save()
      if len(request.POST['password1']) > 5:  
        new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        login(request, new_user)
        return HttpResponseRedirect("/listings/")
  else:
    form = UserCreationForm()
  return render(request, "registration/register.html", { 'form': form, })

@login_required
def profile(request):
  p = User.objects.get(username = request.user.username)

  if request.method == 'POST':
    form = UserEditForm(request.POST, instance=request.user)
    profile = ProfileForm(request.POST, instance=p.userprofile)
    if form.is_valid() and profile.is_valid():
      form.save()
      profile.save()
      return HttpResponseRedirect("/user/dashboard/")
  else:
    form = UserEditForm(instance=request.user)
    profile = ProfileForm(instance=p.userprofile)

  return render(request, "pages/users/profile.html", { 'form': form, 'profile':profile,})


@login_required
def dashboard(request):
  listings = Listing.objects.filter(owner = request.user)

  email = request.user.userprofile.email

  cmd = "/var/www/boxhippo/static/scripts/get_max_listings.php"

  #p = subprocess.Popen(['php', cmd, email], shell=False)
  #results = p.communicate()
  p = subprocess.Popen(['php', cmd, email], shell=False, stdout=subprocess.PIPE)
  # out should be the max number of listings the user has purchased
  out, err = p.communicate()

  usr = UserProfile.objects.get(user = request.user)
  usr.maxListings = int(out)
  usr.save()

  c = {
    'user': request.user,
    'listings': listings,
    'listings_count': listings.count(),
    'maxListings': int(out),
  }
  return render(request, "pages/users/dashboard.html", c)



@login_required
def start_listing(request):
  pw = ''.join(random.SystemRandom().choice(string.uppercase + string.digits) for _ in xrange(10))
  cmd = "php /var/www/boxhippo/static/scripts/register_user.php " + request.user.userprofile.email + " " + pw
  cmd2 = "/var/www/boxhippo/static/scripts/register_user.php"
  email = request.user.userprofile.email
  # subprocess.call(cmd, shell=True)

  #p = subprocess.check_output(['php', cmd2, email, pw], shell=False, stderr=subprocess.STDOUT)
  #p = subprocess.Popen(['php', cmd2, email, pw], shell=False, stderr=subprocess.STDOUT)
  #p = subprocess.Popen(['php', cmd2, email, pw], shell=False)
  subprocess.call(['php', cmd2, email, pw], shell=False)
  #val = p.communicate()

  c = {
    'email': request.user.userprofile.email,
  }
  return render(request, "basics/start_listing.html", c)
