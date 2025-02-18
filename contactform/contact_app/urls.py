from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.contact,name='contact'),
    path('login/',views.loginpage,name='login'),
    path('list/',views.list_contact,name='list'),
    path('view/<int:id>/',views.views_page,name='view')
]
