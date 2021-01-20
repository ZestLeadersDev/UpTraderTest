from django import template
from ..models import Menu, MenuItem


register = template.Library()


@register.inclusion_tag('templatetags/draw_menu.html')
def draw_menu(menu_label):
    menu_items = []
    menu_sub_items = []
    menu_items_list = MenuItem.objects.filter(menu__label__exact=menu_label).order_by('order')

    for item in menu_items_list:
        if not item.parent_item:
            menu_items.append(item)
        else:
            menu_sub_items.append(item)

    return {
        'menu_label': str(menu_label),
        'menu_items': menu_items,
        'menu_sub_items': menu_sub_items,
    }

