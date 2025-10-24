
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),              # ✅ Root URL - homepage
    path('home/', views.home),         # Optional - if you want /home/ too
    path('tablet/', views.tablet),
    path('capsule/', views.capsule),
    path('pfs/', views.pfs),
    path('syrup/', views.syrup),
]


