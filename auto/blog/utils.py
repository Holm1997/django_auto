from .models import *

menu = [{'title': 'Главная', 'url_name': 'main'},
        {'title': 'Добавить автомобиль', 'url_name': 'addcar'},        
        {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        brands = Brand.objects.all()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        
        context['brands'] = brands
        if 'brands_selected' not in context:
            context['brands_selected'] = 0
        return context