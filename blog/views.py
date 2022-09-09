from multiprocessing import context
from django.shortcuts import render,HttpResponse



def blogPost(request):
    return render(request,'blog/blogpost.html')
    
