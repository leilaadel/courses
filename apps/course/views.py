from django.shortcuts import render, HttpResponse, redirect
from .models import Course
# Create your views here.
def index(request):
    # print "made it to index"
    # if request.method == "POST":
    print "made it into the if statement"
    context = {
    'course_name': Course.objects.all()

    }
        # print context
        # print course_name
    return render(request, "course/index.html", context)
    return render(request, "course/index.html")

def course(request):
    #using ORM
    print "we are in course"
    Course.objects.create(course_name=request.POST["course_name"], description=request.POST['description'], date_added=NOW())
    return redirect('/')

def destroy(request):
    print "we made it to remove"
    # print course.id

    return render(request, "course/destroy.html")
    # return redirect('/destroy')
# def id(request):
#     #this is for tracking the course we want to remove
