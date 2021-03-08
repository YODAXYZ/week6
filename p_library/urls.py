from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy, include
from .views import AuthorEdit, AuthorList, author_create_many, friend_with_book, RegisterView, my_blog
from django.conf import settings

app_name = 'p_library'
urlpatterns = [
    path('author/create/', AuthorEdit.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('friend/', friend_with_book, name='friend_with_book'),
    path('register/', RegisterView.as_view(
            template_name='register.html',
            success_url=reverse_lazy('common:profile-create')
        ), name='register'),
    path('my_blog/',my_blog, name='my_blog'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)