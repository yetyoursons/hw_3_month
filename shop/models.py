from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=150)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.text
