from django.urls import path
from .import views
from django.urls import path, re_path
from django.views.generic import TemplateView
# from .views import ViewsToBeImported


app_name = "bola"

urlpatterns = [
    path('',views.home,name='home'),
    path('properties/',views.properties,name='properties'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('blog/<int:pk>/', views.detail_page,name='detail-page'),
    path('blogpost/',views.blogpost,name='blogpost'),
    path('page404/',views.page404,name='page404')
    

]

