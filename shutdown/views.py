from django.http import HttpResponse
import os

def shutdown(request):
    if request.method == 'POST':
        os.system('sudo shutdown now')
        return HttpResponse('Shutting down...')
    return HttpResponse('Invalid request method.')