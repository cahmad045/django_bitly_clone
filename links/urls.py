from django.urls import path
from .views import index, link_redirect, create_link
urlpatterns = [
    path('', index, name='home'),
    path('<str:root_link>', link_redirect, name='root_link'),
    path('link/create', create_link, name='create_link')


]