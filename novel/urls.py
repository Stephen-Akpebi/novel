from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
from novel import views

app_name = 'novel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home'),
    path('about/',views.About.as_view(),name='about'),
    path('gallery/',views.Gallery.as_view(),name='gallery'),
    path('blog/',views.Blog.as_view(),name='blog'),
    path('blogdetail/',views.BlogDetail.as_view(),name='blogdetail'),
    path('teacher/',views.Teachers.as_view(),name='teacher'),
    path('courses/',views.Courses.as_view(),name='courses'),
    path('contact/',views.Contact.as_view(),name='contact'),
]
