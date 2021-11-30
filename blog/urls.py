from django.urls import path
from .views import BlogProfileView

app_name="blog"

urlpatterns = [
    path('', BlogProfileView.as_view(), name="blog"),
    

]