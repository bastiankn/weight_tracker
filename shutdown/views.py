from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
import subprocess

@login_required
@user_passes_test(lambda u: u.is_superuser)
def shutdown(request):
    if request.method == 'POST':
        try:
            result = subprocess.run(
                ["sudo", "/sbin/shutdown", "-h", "now"],
                capture_output=True,
                text=True,
                check=True
            )
            return HttpResponse(f'Shutdown command issued. Output: {result.stdout}')
        except subprocess.CalledProcessError as e:
            return HttpResponse(f'Failed to issue shutdown command: {e}', status=500)
    return HttpResponse('Invalid request method.', status=405)