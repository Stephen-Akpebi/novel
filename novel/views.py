from django.shortcuts import render
from django.views import generic
from telnetlib import GA
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views import generic
from .models import Gallery, Teachers, Bod, Instructor
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

class Home(generic.ListView):
    queryset = Teachers.objects.all()
    template_name = 'novel/index.html'


class Facility(generic.TemplateView):
    template_name = 'novel/courses.html'


class Preschool(generic.TemplateView):
    template_name = 'novel/preschool.html'

class Middle(generic.TemplateView):
    template_name = 'novel/middle.html'

class Secondary(generic.TemplateView):
    template_name = 'novel/secondary.html'


class Boarding(generic.TemplateView):
    template_name = 'novel/boarding.html'


class Admission(generic.TemplateView):
    template_name = 'novel/admission.html'


class Contact(generic.TemplateView):
    template_name = 'novel/contact.html'



class Gallery(generic.ListView):
    queryset = Gallery.objects.all()
    template_name = 'novel/gallery.html'


class Teachers(generic.ListView):
    queryset = Teachers.objects.all()
    template_name = 'novel/teacher.html'


class Instructor(generic.ListView):
    queryset = Instructor.objects.all()
    template_name = 'novel/teacher.html'


class Bod(generic.ListView):
    queryset = Bod.objects.all()
    template_name = 'novel/bod.html'

class Blog(generic.TemplateView):
    template_name = 'novel/blog.html'


class BlogDetail(generic.TemplateView):
    template_name  = 'novel/blog-single.html'


#class Blog(DetailView):
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    #def get_queryset(self):
        #return super().get_queryset()
    
    #template_name = 'blog.html'


#class BlogDetail(DetailView):
    #template_name = 'blog-details.html'


class About(generic.TemplateView):
    template_name = 'novel/about.html'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            return render(request, 'novel/contact.html', {'form': ContactForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    form = ContactForm()
    context = {'form': form}
    return render(request, 'novel/contact.html', context)






