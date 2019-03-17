from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from posts import views


urlpatterns = [
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
