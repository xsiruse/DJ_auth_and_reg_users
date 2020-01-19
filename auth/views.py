from django.shortcuts import render


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    # request.user.
    return render(
        request,
        'registration/signup.html'
    )
