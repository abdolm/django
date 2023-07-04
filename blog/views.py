from django.http import HttpResponse
from django.shortcuts import render

data = {
    'posts': [
        {
            'id':5,
            'title':'post 1',
            'year': 2016
        },
        {
            'id':7,
            'title':'post 2',
            'year': 2016
        },
        {
            'id':4,
            'title':'post 3',
            'year': 2016
        }
    ]
}
def blog(request):
    return render(request, 'blog/blog.html', data)

def home(request):
    return HttpResponse("Home page")