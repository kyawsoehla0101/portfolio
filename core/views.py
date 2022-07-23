from django.shortcuts import render
from .models import About, Blog, Category, Contact, Gallery, Hero, Skill, Year
from django.db.models import Count
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    about = About.objects.first()
    contact = Contact.objects.first()
    hero = Hero.objects.first()
    skills = Skill.objects.all()
    blogs = Blog.objects.all()[:8]
    gallery = Gallery.objects.all()
    years = Year.objects.all()
    context = {"about":about,'contact':contact,'skills':skills,'hero':hero,'blogs':blogs,'gallery':gallery,'years':years}
    return render(request,'home.html',context)

def detail(request,slug):

    blog = Blog.objects.get(slug=slug)

    context = {'blog':blog}
    return render(request,'layouts/detail.html',context)

def allBlog(request):
    about = About.objects.first()
    contact = Contact.objects.first()
    hero = Hero.objects.first()
    categories = Category.objects.all().annotate(posts_count=Count('blog'))
    blogs = Blog.objects.all()
    gallery = Gallery.objects.all()
    years = Year.objects.all()
    context = {"about":about,'contact':contact,'categories':categories,'hero':hero,'blogs':blogs,'gallery':gallery,'years':years}
    return render(request,'layouts/allblogs.html',context)

def categorypost(request,slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(category=category)
    categories = Category.objects.all().annotate(posts_count=Count('blog'))
    context = {'categories':categories,'blogs':blogs,'slug':slug}
    return render(request,'layouts/categorypost.html',context)