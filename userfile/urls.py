from django.urls import path,include
from . import views
urlpatterns = [
    
    path('home/',views.home,name='home'),
    path('',views.index,name='index'),
    path('users/',views.UserLoginApiview.as_view(),name='users'),
    path('userscsvadd/',views.UserCsvAddApiview.as_view(),name='userscsvadd'),
    path('csvupload/',views.CSVUploadAPIView.as_view(),name='csvupload'),


]