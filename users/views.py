from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from users.models import UserEditForm, ProfileForm, UserProfile
from listings.models import Listing


def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      profile = UserProfile(user = new_user)
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
  c = {
    'user': request.user,
    'listings': listings,
  }
  return render(request, "pages/users/dashboard.html", c)
