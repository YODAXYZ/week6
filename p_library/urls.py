from django.conf.urls.static import static
from django.urls import path
from .views import AuthorEdit, AuthorList, author_create_many, friend_with_book
from django.conf import settings

app_name = 'p_library'
urlpatterns = [
    path('author/create/', AuthorEdit.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('friend/', friend_with_book, name='friend_with_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)