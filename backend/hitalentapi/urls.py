from django.urls import path, include


urlpatterns = [
    # Вынужден роутить таким образом, т.к. в ТЗ префикса для API нет.
    path('', include('api.urls', 'api'))
]
