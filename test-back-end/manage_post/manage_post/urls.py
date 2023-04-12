from django.contrib import admin
from django.urls import path
from account.views import AccountViews
from category.views import CategoryViews
from post.views import PostViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', AccountViews.as_view(), name='account-url'),
    path('category/', CategoryViews.as_view(), name='category-url'),
    path('post/', PostViews.as_view(), name='post-url'),
]
