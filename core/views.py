from django.shortcuts import render
from .models import About, Blog, Contact, Gallery, Hero, Skill, Year
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