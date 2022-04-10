
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indext,name='index'),
    path('collection/',views.collection,name='collection'),
    path('shoes/',views.shoes,name='shoes'),
    path('contact/',views.contact,name='contact'),
    path('recing/',views.recing,name='recing'),
    path('register/',views.register,name='register'),
]
