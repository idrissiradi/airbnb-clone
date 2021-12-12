from django import template

from lists import models as list_model

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):
    user = context.request.user
    the_list = list_model.List.objects.get_or_none(
        user=user, name="My Favorites Houses"
    )
    return the_list.rooms.contains(room)
