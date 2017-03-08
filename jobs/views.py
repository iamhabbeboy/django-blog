from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from jobs.models import Employment, Member

# Create your views here.

def index(request):
    #template = loader.get_template("home.html")
    #return HttpResponse(template.render(request))
    member_data = Member.objects.all()
    context = {
       'member_data': member_data
    }
    return render(request, "home.html", context)

def create(request):
    return render( request, "create.html")

def data(request, blog_id):
    #return HttpResponse("My value is " + str(blog_id) )
    table = Member(username="abiodun", password="solomon")
    table.save()
    return HttpResponse("Data Saved Successfully !")
