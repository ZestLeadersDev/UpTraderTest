from django.db import models


class Menu(models.Model):
    """ Основное меню """
    label = models.CharField('Название', null=False, unique=True, max_length=200)

    def __str__(self):
        return self.label


class MenuItem(models.Model):
    """ Пункт меню """
    menu = models.ForeignKey(Menu, verbose_name="Меню", on_delete=models.CASCADE, null=False, default=None)
    parent_item = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField('Название пункта', null=False, max_length=100)
    url = models.CharField('Ссылка', null=False, max_length=300)
    is_named_url = models.BooleanField('Named url?', default=False)
    order = models.PositiveSmallIntegerField('Порядок', default=0)

    def __str__(self):
        return self.menu.label + ' / ' + self.label

