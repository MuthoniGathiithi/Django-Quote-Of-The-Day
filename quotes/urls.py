from django.contrib import admin
from django.urls import path, include
from quotes.views import random_quote  # import your quote view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('quotes/', include('quotes.urls')),
    path('', random_quote, name='random_quote'),  # 👈 this serves the root URL
]
