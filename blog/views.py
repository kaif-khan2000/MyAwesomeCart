from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from math import ceil

blogs = Blog.objects.all()

def index(request):
    params = {
        'blogs':blogs,
    }
    return render(request,'blog/index.html',params)

def blogpost(request,id):
    blog = Blog.objects.filter(post_id=id)
    prevBlog = Blog.objects.filter(post_id=id-1)
    nextBlog = Blog.objects.filter(post_id=id+1)
    params = {
        'blog':blog[0],
        'prevEx':False,
        'nextEx':False,
    }
    if len(prevBlog):
        params["prev"] = prevBlog[0]
        params['prevEx'] = True
    if len(nextBlog):
        params["next"] = nextBlog[0]
        params['nextEx'] = True
    return render(request,'blog/blogpost.html',params)
def search(request):
    query = request.GET.get('search')
    query = query.lower()
    searchResult = []
    for blog in blogs:
        if queryMatch(query,blog):
            searchResult.append(blog)
    print(searchResult)
    return render(request,'blog/search.html',{'result':searchResult})

def queryMatch(query,blog):
    matches = [
        blog.title.lower(),
        blog.head0.lower(),
        blog.chead0.lower(),
        blog.head1.lower(),
        blog.chead1.lower(),
        blog.head2.lower(),
        blog.chead2.lower(),
    ]
    for match in matches:
        if query in match:
            return True
    return False 