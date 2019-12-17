from django.shortcuts import render

def template_three_simple(request):
    view = "template_three"
    return render(request, 'myview.html', {'name': view}) # view и контекст