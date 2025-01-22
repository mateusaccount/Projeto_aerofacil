from django.urls import path
from . import views

urlpatterns = [
    # Login e Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Cadastro
    path('signup/', views.signup, name='signup'),

    # CRUD das Viagens
    path('', views.login_view, name='login'),
    path('viagem/<int:viagem_id>/', views.viagem_detail, name='viagem_detail'),
    path('viagem/criar/', views.viagem_create, name='viagem_create'),
    path('viagem/<int:viagem_id>/editar/', views.viagem_update, name='viagem_update'),
    path('viagem/<int:viagem_id>/deletar/', views.viagem_delete, name='viagem_delete'),
]