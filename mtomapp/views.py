from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from .models import Authors
def index(request):
    return render(request,'index.html')

def addbook(request):
    # print("add book")
    context = {}
    context["objs"]= Book.objects.all()
    return render(request, "addbook.html", context )

def viewbook(request, id):
    # print("add book")
    context = {}
    context["objs"]= Book.objects.get(id = int(id))
    context["objs2"]= Authors.objects.all()
    print(context["objs2"])
    return render(request, "viewbook.html", context )

def addAuthortobook(request, bid, aid):
    this_Author = Authors.objects.get(id = aid)
    this_book = Book.objects.get(id=bid)
    
    this_book.publishers.add(this_Author) 
    return redirect( '/viewbook/'+bid)

def addauthor(request):
    # print("add book")
    context = {}
    context["objs"]= Authors.objects.all()
    return render(request, "addauthor.html", context )
    
def viewauthor(request, id):
    # print("add book")
    context = {}
    context["objs"]= Authors.objects.get(id = int(id))
    context["objs2"]= Book.objects.all()
    print(context["objs2"])
    return render(request, "viewauthor.html", context )

def additem(request, which_form):
    print("add item here")
    if which_form == "book":
        this_book= Book.objects.create(title =request.POST['title'], desc = request.POST['description']) 
        for bk in Book.objects.all():
             print(bk.title)
        return redirect('/addbook')
    
        
    if which_form == "author":
        this_author= Authors.objects.create(firstname =request.POST['firstname'],
         lastname = request.POST['lastname'], notes= request.POST['notes'] ) 
        for au in Authors.objects.all():
         print(au.firstname)
        print("add author")
        return redirect('/addauthor')

def addBooktoAuthor(request, bid, aid):
    this_Author = Authors.objects.get(id = aid)
    this_book = Book.objects.get(id=bid)
    
    this_Author.books.add(this_book) 
    return redirect( '/viewauthor/'+aid)



