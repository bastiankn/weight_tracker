from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from .forms import UserProfileForm

# User Authenticated
def check_user_not_authenticated(user):
    return user.is_authenticated

@user_passes_test(check_user_not_authenticated, login_url='/login', redirect_field_name=None)
def mass_input(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('plan') 
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "mass_input.html", {'form': form})