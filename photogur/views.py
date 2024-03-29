from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from photogur.models import Picture, Comment

# def root_path(request):
#     return HttpResponseRedirect('')

def pictures(request):
    pictures = Picture.objects.all() 
    context = {'pictures': pictures}
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture} 
    response = render(request, 'picture.html', context)
    return HttpResponse(response)
    



