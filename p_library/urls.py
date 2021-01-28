from django.urls import path
from .views import AuthorEdit, AuthorList, BookList, author_create_many, books_authors_create_many, book_increment, book_decrement, test, lib
# from django.conf.urls.static import static
# from django.conf import settings

app_name = 'p_library'

urlpatterns = [
    path('', lib),
    path('book_increment/', book_increment),
    path('book_decrement/', book_decrement),
    path('test/', test),
    path('author/create/', AuthorEdit.as_view(), name='author_create'),  
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('books/', BookList.as_view(), name='book_list'),
    path('author/create_many/', author_create_many, name='author_create_many'),
    path('author_book/create_many/', books_authors_create_many, name='author_book_create_many'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)