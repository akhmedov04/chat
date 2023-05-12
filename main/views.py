from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    return render(request, 'home.html')

def main(request):
    if request.user.is_authenticated:
        data = {
            "user": request.user
        }
        return render(request, 'main.html', data)
    return redirect('/')