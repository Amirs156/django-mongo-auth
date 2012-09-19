from django import template

register = template.Library()

@register.inclusion_tag('user/user_image.html', takes_context=True)
def user_image(context, user=None):
    if user is None:
        user = context['user']

    return {
        'user_image_url': user.get_image_url(),
    }

@register.filter()
def is_active(current_path, url_path):
    return  current_path.startswith(url_path)
