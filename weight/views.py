from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
import plotly.express as px
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
            mass.user = request.user  
            mass.save()
            return redirect('plan')  
    else:
        form = UserProfileForm()
    return render(request, "mass_input.html", {'form': form})

@user_passes_test(check_user_not_authenticated, login_url='/login', redirect_field_name=None)
def mass_graph(request):
    user = request.user
    data = Mass.objects.filter(user=user).order_by('date_created')

    # Extracting data for the graph
    dates = [entry.date_created for entry in data]
    weights = [entry.weight for entry in data]

    # Creating the Plotly graph
    weight_chart = px.line(x=dates, y=weights, labels={'x': 'Date', 'y': 'Weight (kg)'}, title='Weight Over Time', template='plotly_dark')

    weight_chart_html = weight_chart.to_html(full_html=False)
    
    return render(request, 'mass_graph.html', {'weight_chart': weight_chart_html})