from django.shortcuts import render

def plan(request):
    return render(request, "workoutplan.html")
