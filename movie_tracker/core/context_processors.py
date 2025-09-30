from .models import Profile

def user_profile(request):
    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
        return {"navbar_profile": profile}
    return {}