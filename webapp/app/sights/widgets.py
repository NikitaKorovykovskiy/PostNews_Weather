from proj.settings import API_KEY
from django import forms


class MapWidget(forms.Widget):
    """
    Виджет карты для моделей Примечательных мест в админ-панели
    """

    media = forms.Media(
        js=(
            f"https://api-maps.yandex.ru/2.1/?apikey={API_KEY}&lang=ru-RU",
            "js/map.js",
        )
    )
    template_name = "map_field.html"

    def __init__(self, attrs=None):
        super().__init__(attrs=attrs)


print(API_KEY)
