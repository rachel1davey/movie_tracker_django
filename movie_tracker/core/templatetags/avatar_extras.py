from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def avatar_url_for(user):
    """Return the avatar URL for a user, or the static placeholder if none.

    Import Profile lazily to avoid import-time app registry issues.
    """
    try:
        # import here to avoid potential import-time side effects
        from movie_tracker.core.models import Profile
    except Exception:
        # If the model cannot be imported for any reason, fall back to static
        return static('placeholder_avatar.png')

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return static('placeholder_avatar.png')

    avatar = getattr(profile, 'avatar', None)
    if not avatar:
        return static('placeholder_avatar.png')

    url = getattr(avatar, 'url', None) or avatar
    if not url:
        return static('placeholder_avatar.png')
    return url
