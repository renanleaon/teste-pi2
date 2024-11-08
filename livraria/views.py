from django.shortcuts import render
from livraria.models import Book, Genre

def index(request):
    books = Book.objects.all()
    genre = Genre.objects.all()  # Pegando todos os gêneros
    return render(request, 'livraria/index.html', {'cards': books, 'genres': genre})


def categoria(request):
    return render(request, 'livraria/categoria.html')

def carrinho(request):
    return render(request, 'livraria/carrinho.html')

def contato(request):
    return render(request, 'livraria/contato.html')

def login(request):
    return render(request, 'livraria/login.html')



def busca(request):
    books = Book.objects.all()  # Corrigido para chamar o método all()

    if 'q' in request.GET:  # O nome do campo de busca é 'q'
        nome_a_buscar = request.GET['q']
        if nome_a_buscar:
            books = books.filter(title__icontains=nome_a_buscar)  # Filtrando pelo título dos livros

    return render(request, 'livraria/busca.html', {'cards': books})



