from django.db import models

# Create your models here.
from django.urls import reverse


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Автор"  # name in admin panel
        verbose_name_plural = "Aвторы"

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.full_name} \n'


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

    def __str__(self):
        return f'{self.name} \n'


class Friend(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друзья"

    def __str__(self):
        return f'{self.name} \n'


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=19, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # models.CASCADE say that if Author was delete all
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    friend = models.ForeignKey(Friend, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    img = models.ImageField(upload_to='img/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name = "Книга"  # name in admin panel
        verbose_name_plural = "Книги"

    def __str__(self):
        return f'{self.title} \n'
