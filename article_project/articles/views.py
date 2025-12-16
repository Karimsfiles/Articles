from django.shortcuts import render

# Create your views here.



def bz(request):
    return render(request, 'base.html')


def artcl(request):
    return render(request, 'articles.html')


def cr(request):
    return render(request, 'create.html')


def ed(request):
    return render(request, 'edit.html')
