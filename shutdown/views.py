from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
import subprocess
import os

@login_required
@user_passes_test(lambda u: u.is_superuser)
def shutdown(request):
    if request.method == 'POST':
        try:
            os.system("sudo shutdown -h now")
            return HttpResponse(f'Shutdown command issued.')
        except:
            return HttpResponse(f'Failed to issue shutdown command', status=500)
    return HttpResponse('Invalid request method.', status=405)