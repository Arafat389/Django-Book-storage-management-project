from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages
from .import models
from . import forms
# Create your views here.
def homepage(request):
    # 1. fetch all data of book form database
    # 2. send all fetched data to a template
    books = Book.objects.all()
    
    return render(request,'book_list.html',{'books':books})


def add_book(request):
    if request.method == 'POST':
        # 1. get the all data from frontend
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    else:
        print("get the form")
        form = BookForm()
        return render(request,'add_book.html',{'form':form})
    
def update_book(request, book_id):
    books = models.Book.objects.get(id=book_id)
    form = forms.BookForm(instance=books) 
    
    if request.method == 'POST': 
        form = forms.BookForm(request.POST,request.FILES, instance=books) 
        if form.is_valid(): 
            form.save() # 
            messages.add_message(request,messages.SUCCESS,"Student Updated Successfully.")
            return redirect('homepage')

    return render(request,'add_book.html',{'form':form})


def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    if book:
        book.delete()

    return redirect('homepage')