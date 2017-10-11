from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('account.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^cadastro/', include('cadastro.urls')),
    url(r'social-auth/', include('social_django.urls', namespace='social'))
]
