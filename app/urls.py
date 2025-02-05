from django.urls import path
from .views import (
    login_view, logout_view, signup,
    viagem_list, viagem_create, viagem_detail, viagem_update, viagem_delete, base
)

urlpatterns = [
    path('', base, name='base'), 
    # Login e Logout
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Cadastro de usuários
    path('signup/', signup, name='signup'),

    # CRUD das Viagens
    path('viagem/', viagem_list, name='viagem_list'),
    path('viagem/nova/', viagem_create, name='viagem_create'),
    path('viagem/<int:pk>/', viagem_detail, name='viagem_detail'),
    path('viagem/<int:pk>/editar/', viagem_update, name='viagem_update'),
    path('viagem/<int:pk>/deletar/', viagem_delete, name='viagem_delete'),
]
