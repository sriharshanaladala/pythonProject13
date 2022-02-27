from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Allcourses
from django.template import loader
# Create your views here.


def courses(request):
    ac= Allcourses.objects.all()
    template=loader.get_template('Technicalcourses/courses.html')
    context=\
    {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))


def detail(request, course_id):
    try:
        course=Allcourses.objects.get(pk = course_id)
    except Allcourses.DoesNotExist:
        raise Http404("course does not available")
    return render(request, 'Technicalcourses/detail.html',{'course': course})

