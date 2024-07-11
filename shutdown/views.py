from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
import os

@login_required
@user_passes_test(lambda u: u.is_superuser)
def shutdown(request):
    if request.method == 'POST':
        os.system('sudo shutdown -h now')
        return HttpResponse('Shutting down...')
    return HttpResponse('Invalid request method.')