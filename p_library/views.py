from django.shortcuts import redirect, render
from .models import Author, Book, Publisher, Friend
from .forms import AuthorForm, BookForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.http.response import HttpResponseRedirect

# Create your views here.
def lib(request):
    context = {}
    return render(request, 'p_library/lib.html', context)

def test(request):
    books = Book.objects.all()
    context = {'books': books, "title": "мою библиотеку",}
    return render(request, 'p_library/test.html', context)

def index(request):
    context = {}
    return render(request, 'p_library/index.html', context)

def publisher(request):
    publishers = Publisher.objects.all()
    context = {'publishers': publishers}
    return render(request, 'p_library/publishers.html', context)

def friends(request):
    friends = Friend.objects.all()
    context = {'friends': friends}
    return render(request, 'p_library/friends_book.html', context)

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/lib/test/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/lib/test/')
            book.copy_count += 1
            book.save()
        return redirect('/lib/test/')
    else:
        return redirect('/lib/test/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/lib/test/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/lib/test/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/lib/test/')
    else:
        return redirect('/lib/test/')

class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p_library:author_list')  
    template_name = 'p_library/author_edit.html'  
  
  
class AuthorList(ListView):  
    model = Author  
    template_name = 'p_library/authors_list.html'

class BookList(ListView):  
    model = Book  
    template_name = 'p_library/book_list.html'

def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:  
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'p_library/manage_authors.html', {'author_formset': author_formset})

def books_authors_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  
    BookFormSet = formset_factory(BookForm, extra=2)  
    if request.method == 'POST':  
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')  
        if author_formset.is_valid() and book_formset.is_valid():  
            for author_form in author_formset:  
                author_form.save()  
            for book_form in book_formset:  
                book_form.save()  
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  
    else:  
        author_formset = AuthorFormSet(prefix='authors')  
        book_formset = BookFormSet(prefix='books')  
    return render(
	    request,  
		'p_library/manage_books_authors.html',  
		{  
	        'author_formset': author_formset,  
			'book_formset': book_formset,  
		}  
	)