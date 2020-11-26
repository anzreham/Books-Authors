from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __repr__(self):
    #     return f"<title: Name = {self.title}> , id: {self.id}"
    @property
    def getauthor(self):
        return self.publishers.all()
#  firstname lastname notes books 

class Authors (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def getbook(self):
        return self.books.all()

    # def __repr__(setitlelf):
    #     return f"<firstname: Name = {self.firstname}> , id: {self.id}" 


