from django.urls import path
from .views import signupview, loginview, listview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('list/', listview, name='list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)