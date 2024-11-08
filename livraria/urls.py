from django.urls import path
from livraria.views import index, busca, categoria, carrinho, contato, login

urlpatterns = [
    path('', index, name='index'),
    path('busca/', busca, name='busca'),
    path('categoria/', categoria, name='categoria'),
    path('carrinho/', carrinho, name='carrinho'),
    path('contato/', contato, name='contato'),
    path('login/', login, name='login'),
    
]