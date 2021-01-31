from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from p_library.models import Book, Author, Publisher, Friend
from django.template import loader
from p_library.forms import AuthorForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'


def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {"title": "мою библиотеку",
                   "books_count": books_count,
                   "books": books}
    return HttpResponse(template.render(biblio_data, request))


def friend_with_book(request):
    template = loader.get_template('friend_book.html')
    books_with_friend = Book.objects.exclude(friend=None)
    friends = Friend.objects.all()
    biblio_data = {'books_with_friend': books_with_friend, 'friends': friends}
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
            return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def index_publisher(request):
    template = loader.get_template('index_publisher.html')
    publisers = Publisher.objects.all()
    biblio_data = {"pubs": publisers}
    return HttpResponse(template.render(biblio_data, request))


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    # На странице с несколькими формами изначально будет появляться 2 формы создания авторов.

    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        # Здесь мы заполняем формы формсета теми данными, которые пришли в запросе.
        # Обратите внимание на параметр `prefix`.
        # Мы можем иметь на странице не только несколько форм,
        # но и разных формсетов, этот параметр позволяет их отличать в запросе.

        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(
                reverse_lazy('p_library:author_list'))
    else:  # Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(prefix='authors')
        # Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


