from django.urls import path,include,re_path
from .import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'movie',views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls))

]