from django.urls import path
from .views import register,login,logout,centers,book

urlpatterns = [

    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('centers/', centers, name='centers'),
    path('book/',book,name='book')

]