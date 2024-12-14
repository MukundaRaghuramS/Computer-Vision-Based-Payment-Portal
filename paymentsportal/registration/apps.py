from django.apps import AppConfig
# your_app/apps.py
import subprocess

class RegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration'


    def ready(self):
        # Use subprocess to call the eye control script in a separate process
            subprocess.Popen(['python', 'eye_control.py'])
