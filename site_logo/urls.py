from django.urls import path
from .import views
urlpatterns = [
   # path('home/',views.index6,name='home'),
    path('login/',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('viewall/',views.viewall,name='viewall'),
    path('updatereg/</str:pk>/',views.updatereg,name='updatereg'),
]

