from django.urls import path 
from . import views
urlpatterns=[
    path('',views.Index,name='index'),
    path('About',views.About,name='about'),
    path('Careers',views.Careers,name='careers'),
    path('News',views.News,name='news'),
    path('Contact',views.Contact,name='contact'),
    path('Account',views.Login,name='login'),
    path('Register',views.Register,name='register'),
    path('Logout',views.Logout,name='logout'),
    path('LKDJHJFSDKJKSFJKS/JKJKSDJHJSD',views.Admin,name='admin'),
    path('Sliders',views.Sliders,name='Sliders')
]