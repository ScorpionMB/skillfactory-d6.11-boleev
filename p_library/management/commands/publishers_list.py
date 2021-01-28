from django.core.management.base import BaseCommand
from p_library.models import Book, Author, Publisher
from collections import Counter
from django.db.models import Count

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

publishers = Publisher.objects.all()
books = Book.objects.all()
authors = Author.objects.all()


# for pub in publishers:
#     print(pub.title)
#     for book in books:
#         if book.publisher.title == pub.title:
#             print(f'\t{book.title}')

for pub in publishers:
    print(pub.title)
    for book in pub.books.all():
        print(f'\t{book.title}')