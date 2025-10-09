from django import template
from django.templatetags.static import static
from ..models import Profile

register = template.Library()

@register.simple_tag
def avatar_url_for(user):
    """Return the avatar URL for a user, or the static placeholder if none."""
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return static('placeholder_avatar.png')

    # CloudinaryField may provide a url attribute or be empty
    avatar = getattr(profile, 'avatar', None)
    if not avatar:
        return static('placeholder_avatar.png')
    # avatar may be a string URL or an object with url attribute
    url = getattr(avatar, 'url', None) or avatar
    if not url:
        return static('placeholder_avatar.png')
    return url
