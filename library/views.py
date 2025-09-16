from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from library.models import Book, BorrowRecord
from datetime import datetime as dt, timedelta


# Create your views here.

def landing(request):
    return render(request, "library/landing.html", {})

@login_required
def home(request):
    if request.user.is_approved:
        if request.method == "POST":
            #print(request.POST)
            if request.POST.get("borrow"):
                book_id = request.POST.get("borrow")
                b_book = Book.objects.get(id=book_id)
                if b_book.no_available > 0:
                    user = request.user
                    b_book.no_available = b_book.no_available - 1
                    b_book.save()
                    borrow_book(user, b_book)
                else:
                    print("No more books available")
                    #messages.info(request, message="We're sorry, there are no more copies of this book available.")
            else:
                print("Invalid input!")

        books = Book.objects.all()
        return render(request, "library/home.html", {"books":books})
    else:
        #messages.warning(request, "Your account is awaiting admin approval.")
        return redirect("pending")


def book(request, id):
    if request.user.is_approved:
        if request.method == "POST":
            #print(request.POST)
            if request.POST.get("borrow"):
                book_id = request.POST.get("borrow")
                b_book = Book.objects.get(id=book_id)
                if b_book.no_available > 0:
                    user = request.user
                    b_book.no_available = b_book.no_available - 1
                    b_book.save()
                    borrow_book(user, b_book)
                else:
                    print("No more book available")
                    #messages.info(request, message="We're sorry, there are no more copies of this book available.")
            else:
                print("Invalid input!")
        book = Book.objects.get(id=id)
        return render(request, "library/book.html", {"book":book})
    else:
        #messages.warning(request, "Your account is awaiting admin approval.")
        return redirect("pending")

def borrowed(request):
    if request.user.is_approved:
        if request.POST.get("return"):
            br_id = request.POST.get("return")
            br = BorrowRecord.objects.get(id = br_id)
            br.returned = True
            br.date_of_return = dt.now()
            b_book = br.book
            b_book.no_available += 1
            b_book.save()
            br.save()
        else:
            print("Invalid input!")

        brs = request.user.borrowrecord_set.all()
        return render(request, "library/borrowed.html", {"brs":brs})
    else:
        #messages.warning(request, "Your account is awaiting admin approval.")
        return redirect("pending")

def history(request):
    if request.user.is_approved:
        brs = request.user.borrowrecord_set.all()
        return render(request, "library/history.html", {"brs":brs})
    else:
        #messages.warning(request, "Your account is awaiting admin approval.")
        return redirect("pending")

def borrow_book(user, b_book):
    br = BorrowRecord(user=user,
                      book = b_book,
                      due_date = dt.now() + timedelta(days=14))
    br.save()