from django.contrib import admin
from django.urls import path
from agenda_App import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.agenda, name='agenda'),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login, name='submit'),
    path('logout/', views.logout_user, name='logout'),
    path('agenda/evento/', views.evento, name='evento'),
    path('agenda/evento/submit', views.submit_evento, name='evento'),
    path('agenda/evento/delete/<id_evento>/', views.delete_evento, name='delete_evento'),
]
