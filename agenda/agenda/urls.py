
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [

    path('', RedirectView.as_view(url='/agenda/')),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('lista/', views.listar_eventos),
    path('lista/atualizar/<int:id_evento>', views.atualizar_evento),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
     path('lista/atualizar/<int:id_evento>/', views.atualizar_evento)
   

]

