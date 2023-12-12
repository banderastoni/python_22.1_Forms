from django.urls import path

from catalog.views import example, home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('example/', example)
]
