from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', signin, name="signin"),
    path('signup/', signup, name="signup"),
    path('logout/', signout, name="signout"),
    path('profile/', profile, name="profile"),
    path('contact_us/', contact, name="contact"),
    path('post/<str:title>/', post_view, name="post_view"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
