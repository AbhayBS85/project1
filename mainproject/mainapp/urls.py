from django.urls import path
from. import views
urlpatterns=[
    path('sec',views.first),
    path('login/newregister',views.second),
    path('reg',views.adarsh,name='reg'),
    path('profile',views.fourth,name='profile'),
    path('apbooking',views.fifth,name='apbooking')
]