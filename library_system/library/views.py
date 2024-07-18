from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Author, Book, BorrowRecord
from .forms import AuthorForm, BookForm, BorrowRecordForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import HttpResponse
import csv

class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'
    paginate_by = 10

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    paginate_by = 10

class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'library/borrowrecord_list.html'
    paginate_by = 10

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('author_list')

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book_list')

class BorrowRecordCreateView(CreateView):
    model = BorrowRecord
    form_class = BorrowRecordForm
    template_name = 'library/borrowrecord_form.html'
    success_url = reverse_lazy('borrowrecord_list')

def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="library_data.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Author Name', 'Email', 'Bio'])
    authors = Author.objects.all()
    for author in authors:
        writer.writerow([author.name, author.email, author.bio])
    
    writer.writerow([''])
    writer.writerow(['Book Title', 'Genre', 'Published Date', 'Author'])
    books = Book.objects.all()
    for book in books:
        writer.writerow([book.title, book.genre, book.published_date, book.author.name])
    
    writer.writerow([''])
    writer.writerow(['User Name', 'Book', 'Borrow Date', 'Return Date'])
    borrow_records = BorrowRecord.objects.all()
    for record in borrow_records:
        writer.writerow([record.user_name, record.book.title, record.borrow_date, record.return_date])
    
    return response
