
from django.contrib import admin
from django.urls import path
from myapplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('inner/', views.inner,name='inner'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('details/',views.detail, name='detail'),
    path('users/', views.user, name='users'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),



]
