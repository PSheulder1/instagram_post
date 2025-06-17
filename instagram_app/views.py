from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login as auth_login, logout

from .models import Post
# Create your views here.


def home(request):
    posts  = Post.objects.all().order_by('-id')

    return render(request, 'index.html', {'posts':posts})



def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):

    if request.method=="POST":
        full_name=request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username, email=email).exists():
            return render(request, 'signup.html', {'error': 'user already exists'})
        
        user = User.objects.create_user(first_name=full_name,
                                         username=username,
                                           email=email,
                                           password=password
                                        )
        user.save()
        return redirect('login')

    return render(request, 'signup.html')




def post(request):
    if request.method=="POST":
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        user = request.user

        data = Post(author=user, content=content, image=image)
        data.save()

        return redirect('home')



    return render(request, 'post.html')



def  update_post(request, post_id):
    updated_post = get_object_or_404(Post, id=post_id)

    if request.method=="POST":
        content = request.POST.get('content')
        image = request.FILES.get('image')

        user = request.user

        updated_post.content = content
        if image:
            updated_post.image = image
        updated_post.save()
        return redirect('home')
    return render(request, 'update.html',{'updated_post':updated_post} )



def delete_post(request, post_id):
    delete_post = get_object_or_404(Post, id=post_id)
    if request.method=="POST":
        delete_post.delete()
        return redirect('home')
    return render(request, 'delete.html')
