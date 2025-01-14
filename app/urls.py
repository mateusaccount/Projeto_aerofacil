from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ViagemListView, ViagemCreateView, ViagemUpdateView, ViagemDeleteView, signup  # Adiciona a view de registro

urlpatterns = [
    # Login e Logout
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Cadastro
    path('signup/', signup, name='signup'),  # Adiciona a URL para o registro

    # CRUD das Viagens
    path('', ViagemListView.as_view(), name='viagem_list'),
    path('nova/', ViagemCreateView.as_view(), name='viagem_create'),
    path('editar/<int:pk>/', ViagemUpdateView.as_view(), name='viagem_update'),
    path('deletar/<int:pk>/', ViagemDeleteView.as_view(), name='viagem_delete'),
]