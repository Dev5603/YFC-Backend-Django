from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
    
    def __str__(self) -> str:
        return self.name

class Offer(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.CharField(max_length=500)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image
        }

    def __str__(self) -> str:
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    description = models.TextField()

    point1 = models.CharField(max_length=500)
    point2 = models.CharField(max_length=500)
    point3 = models.CharField(max_length=500)

    amount = models.CharField(max_length=50)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'description': self.description,
            'point1': self.point1,
            'point2': self.point2,
            'point3': self.point3,
            'amount': self.amount
        }
    
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self) -> str:
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'description': self.description,
            'category': self.category.name,
            'date': self.date.isoformat(),
            'comments': [comment.serialize() for comment in self.comments.all()]
        }

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date.isoformat(),
            'blog': self.blog.title,
            'comment': self.comment
        }

    def __str__(self) -> str:
        return f'{self.name} on {self.date.day}, {self.date.month}'