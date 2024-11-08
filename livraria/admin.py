from django.contrib import admin
from .models import Author, Publisher, Book, Genre, BookGenre, Customer, Order, OrderItem, Supplier, SupplierBook

# Personalização do modelo Author no admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    search_fields = ('first_name', 'last_name')
    list_filter = ('date_of_birth',)

# Personalização do modelo Publisher no admin
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'website')
    search_fields = ('name',)

# Personalização do modelo Book no admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'price', 'publication_date', 'publisher')
    search_fields = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date')

# Personalização do modelo Genre no admin
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Personalização do modelo BookGenre no admin
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ('book', 'genre')
    search_fields = ('book__title', 'genre__name')
    list_filter = ('genre',)

# Personalização do modelo Customer no admin
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)

# Personalização do modelo Order no admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('customer__first_name', 'customer__last_name')

# Personalização do modelo OrderItem no admin
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'price')
    list_filter = ('order', 'book')
    search_fields = ('book__title',)

# Personalização do modelo Supplier no admin
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'email', 'phone')
    search_fields = ('name', 'contact_name')
    list_filter = ('name',)

# Personalização do modelo SupplierBook no admin
class SupplierBookAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'book', 'supply_price', 'supply_date')
    list_filter = ('supplier', 'supply_date', 'book')
    search_fields = ('book__title', 'supplier__name')

# Registrando os modelos no admin com as personalizações
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookGenre, BookGenreAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierBook, SupplierBookAdmin)
