from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Admin'
admin.site.site_title = 'Admin Portol'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demoapp.urls'))
]
