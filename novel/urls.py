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
    path('facility/',views.Facility.as_view(),name='facility'),
    path('preschool/',views.Preschool.as_view(),name='preschool'),
    path('primary/',views.Primary.as_view(),name='primary'),
    path('secondary/',views.Secondary.as_view(),name='secondary'),
    path('boarding/',views.Boarding.as_view(),name='boarding'),
    path('admission/',views.Admission.as_view(),name='admission'),
    path('admission/',views.Bod.as_view(),name='admission'),
    #path('contact/',views.Contact.as_view(),name='contact'),
    path('contact/', views.contact_view, name='contact'),
]
