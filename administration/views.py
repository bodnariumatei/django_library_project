from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from administration.forms import BookForm
from library.models import BorrowRecord, Book
from django.db.models import Q
from datetime import datetime as dt

# Create your views here.

@login_required
@user_passes_test(lambda u: u.is_staff)  # only staff can access
def admin_reports(request):
    if request.method == "POST" and request.POST.get("return"):
        br_id = request.POST.get("return")
        br = get_object_or_404(BorrowRecord, id=br_id)
        if not br.returned:
            br.returned = True
            br.date_of_return = dt.now()
            br.book.no_available += 1
            br.book.save()
            br.save()

    borrow_records = BorrowRecord.objects.filter(returned=False)
    books = Book.objects.filter(no_available__gt=0)
    return render(request, "administration/reports.html", {"brs":borrow_records, "books":books})

@login_required
@user_passes_test(lambda u: u.is_staff)  # only staff can access
def admin_users(request):
    if request.method == "POST":
        u_id = request.POST.get("approve")
        user = CustomUser.objects.get(id=u_id)
        user.is_approved = True
        user.save()
    admins = CustomUser.objects.filter(is_staff=True)
    p_users = CustomUser.objects.filter(is_approved=False, is_staff=False)
    a_users = CustomUser.objects.filter(is_approved=True, is_staff=False)
    return render(request, "administration/users.html", {"pending_users": p_users, "approved_users": a_users, "admins":admins})

@login_required
@user_passes_test(lambda u: u.is_staff)  # only staff can access
def admin_user(request, u_id):
    if request.method == "POST":
        # print(request.POST)
        user = CustomUser.objects.get(id=u_id)
        if request.POST.get("approve"):
            user.is_approved = True
            user.save()
        elif request.POST.get("disapprove"):
            user.is_approved = False
            user.save()
        elif request.POST.get("makeadmin"):
            user.is_staff = True
            user.save()
        elif request.POST.get("noadmin"):
            user.is_staff = False
            user.save()
        elif request.POST.get("remove"):
            user.delete()
        else:
            print("Invalid input!")
    user = CustomUser.objects.get(id=u_id)
    return render(request, "administration/user.html", {"user":user})

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_books(request):
    if request.GET.get("q"):
        query = request.GET.get("q")
        if query != "":
            books = Book.objects.filter( Q(title__icontains=query) | Q(author__icontains=query) )
    else:
        books = Book.objects.all()
    #print(books)
    return render(request, "administration/books.html", {"books":books})

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_update_book(request, b_id):
    book = Book.objects.get(id=b_id)
    if request.method == "POST":
        # print(request.POST)
        if request.POST.get("update"):
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
            return redirect("/admin/books")
        elif request.POST.get("remove"):
            book.delete()
            return redirect("/admin/books")
        else:
            print("Invalid form command")

    form = BookForm(instance=book)
    #print(books)
    return render(request, "administration/update_book.html", {"book":book, "form":form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_create_book(request):
    if request.method == "POST":
        # print(request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/admin/books")
    form = BookForm()
    return render(request, "administration/create_book.html", {"form":form})