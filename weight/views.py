from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Mass
from .forms import UserProfileForm

# User Authenticated
def check_user_not_authenticated(user):
    return user.is_authenticated

@user_passes_test(check_user_not_authenticated, login_url='/login', redirect_field_name=None)
def mass_input(request):
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            mass = form.save(commit=False)
            mass.user = request.user  # Set the user to the currently logged-in user
            mass.save()
            return redirect('plan')  # Redirect to a 'plan' page after saving
    else:
        form = UserProfileForm()


    return render(request, "mass_input.html", {'form': form})