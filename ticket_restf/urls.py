from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.home , name='home'),
    path('logout/', views.logout_user , name='logout_user'),
    path('api/all_tickets/' , views.getData),
    path('api/receive_ticket/' , views.postData),
    path('tickets/<int:ticket_id>/download/', views.download_file, name='download_file'),
    path('tickets/<int:ticket_id>/delete/', views.delete_ticket , name = 'delete_ticket')
]
