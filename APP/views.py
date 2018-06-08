
from django.shortcuts import render,redirect,HttpResponse

from APP.models import Post
# Create your views here.
def create(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        post=Post.objects.create(title=title,content=content)
        # return render(request,'create.html',{'data':data})

        return redirect('app/read/?post_id={}'.format(post.id))
    else:
        return render(request,'create.html')
        # return HttpResponse(123123)


def read(request):
    post_id=request.GET.get("post_id")
    post = Post.objects.get(id=post_id)
    # return render(request,'read.html',{"post":post})
    return HttpResponse(123123)
