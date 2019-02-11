from django.contrib import admin
from django.urls import path
import posts.views
import sitepages.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cv/', posts.views.cv, name="cv"),
    path('', posts.views.home, name="home"),
    path('about/', sitepages.views.about, name="about"),
    path('download/', posts.views.download, name="download"),
    path('contact/', sitepages.views.contact, name="contact"),
    path('posts/<int:post_id>/', posts.views.post_details, name="post_detail"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
