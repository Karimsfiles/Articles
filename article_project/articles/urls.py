from django.urls import path
from .views import artcl, cr, ed

app_name = 'articles'

urlpatterns = [
    path('', artcl),
    path('create/', cr),
    path('<int:id>/edit/', ed),
]