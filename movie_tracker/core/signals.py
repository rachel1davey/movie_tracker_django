from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages

# allauth signal for signup
try:
    from allauth.account.signals import user_signed_up
except Exception:
    user_signed_up = None

@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    messages.success(request, "Signed in successfully.")

@receiver(user_logged_out)
def on_logout(sender, user, request, **kwargs):
    messages.info(request, "Signed out.")


if user_signed_up:
    @receiver(user_signed_up)
    def on_signup(sender, request, user, **kwargs):
        messages.success(request, "Welcome! Your account has been created.")
