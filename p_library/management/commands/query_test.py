from django.core.management.base import BaseCommand
from p_library.models import Book, Author
from collections import Counter

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

book_price = 0
sum_price = 0
book_count = Counter()

books = Book.objects.all()
author_en = Author.objects.exclude(country='RU')
pushkin = Author.objects.get(full_name='Пушкин Александр Сергеевич')
adams = Author.objects.get(full_name='Douglas Adams')
books_en = Book.objects.filter(author__in=author_en)
books_pushkin = Book.objects.filter(author=pushkin)
books_adams = Book.objects.filter(author=adams)

for book in books:
    if book.price > book_price:
        book_price = book.price
print('\nСамая дорогая книга: ', book_price, '\n')

for book in books:
    if book.price < book_price:
        book_price = book.price
        cnt = book.copy_count

print('Экземпляров самой дешевой книги: ', cnt, '\n')

for book in books:
    book_count[book.author.full_name] += 1
for aut, cnt in book_count.items():
    print('\t', aut, '| произведений: ', cnt)

for book in books:
    if book_count[book.author.full_name] > 1:
        sum_price += book.price * book.copy_count
print('\nСтоимость всех книг плодовитых авторов: ', sum_price, '\n')
sum_price = 0

for book in books_en:
    sum_price += book.price * book.copy_count
print('Стоимость всех книг иностранных авторов: ', sum_price, '\n')
sum_price = 0

for book in books_pushkin:
    sum_price += book.price * book.copy_count
print('Стоимость всех книг Пушкина: ', sum_price, '\n')
sum_price = 0

for book in books_adams:
    sum_price += book.price
print('Стоимость книг автора Douglas Adams: ', sum_price)

# pushkin_book = pushkin.books.all()
# for book in pushkin_book:
#     print(book.title)