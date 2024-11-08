from django.db import models
from localflavor.br.models import BRCPFField

# Tabela para Autores dos livros
class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nome")
    last_name = models.CharField(max_length=100, verbose_name="Sobrenome")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    date_of_death = models.DateField(null=True, blank=True, verbose_name="Data de Falecimento")
    bio = models.TextField(blank=True, verbose_name="Biografia")

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Tabela para Editoras dos livros
class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Editora")
    address = models.TextField(blank=True, verbose_name="Endereço")
    website = models.URLField(blank=True, verbose_name="Website")

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

    def __str__(self):
        return self.name

# Tabela para Livros
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    publication_date = models.DateField(verbose_name="Data de Publicação")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="Editora")
    authors = models.ManyToManyField(Author, related_name='books', verbose_name="Autores")
    cover_image = models.ImageField(upload_to='fotos/%Y/%m/%d/', null=True, blank=True, verbose_name="Imagem de Capa")


    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.title

# Tabela para Gêneros dos livros
class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Gênero")

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    def __str__(self):
        return self.name

# Tabela intermediária para relacionar Livro e Gênero
class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Livro")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Gênero")

    class Meta:
        unique_together = ('book', 'genre')
        verbose_name = 'Gênero do Livro'
        verbose_name_plural = 'Gêneros dos Livros'

# Tabela para Clientes
class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nome")
    last_name = models.CharField(max_length=100, verbose_name="Sobrenome")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Telefone")
    address = models.TextField(blank=True, verbose_name="Endereço")
    cpf = BRCPFField(unique=True, verbose_name="CPF", null=False, blank=False, default='123.456.789-09')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Tabela para Pedidos dos clientes
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregue')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Cliente")
    order_date = models.DateField(auto_now_add=True, verbose_name="Data do Pedido")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"Pedido {self.id} - {self.customer}"

# Tabela para Itens de cada Pedido
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Pedido")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Livro")
    quantity = models.PositiveIntegerField(verbose_name="Quantidade")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens dos Pedidos'

    def __str__(self):
        return f"{self.quantity} x {self.book.title} - Pedido {self.order.id}"

# Tabela para Fornecedores
class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Fornecedor")
    contact_name = models.CharField(max_length=100, blank=True, verbose_name="Nome do Contato")
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Telefone")
    address = models.TextField(blank=True, verbose_name="Endereço")

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.name

# Tabela intermediária para relacionar Fornecedor e Livro
class SupplierBook(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Fornecedor")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Livro")
    supply_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Fornecimento")
    supply_date = models.DateField(verbose_name="Data de Fornecimento")

    class Meta:
        unique_together = ('supplier','book')
        verbose_name = 'Fornecedor do Livro'
        verbose_name_plural = 'Fornecedores dos Livros'
