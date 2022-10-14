from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    template_name = 'novel/index.html'

class Courses(generic.TemplateView):
    template_name = 'novel/courses.html'


class Contact(generic.TemplateView):
    template_name = 'novel/contact.html'



class Gallery(generic.TemplateView):
    template_name = 'novel/gallery.html'




class Teachers(generic.TemplateView):
    template_name = 'novel/teacher.html'

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





