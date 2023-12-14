from django.urls import path
from .views import index, log, data, posts, log

urlpatterns = [
    path('', index, name='home'),
    path('reg', log, name='reg'),
    path('data', data, name='data'),
    path('posts', posts, name='posts'),
    path('log', log, name='log'),
]