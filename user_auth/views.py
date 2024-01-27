from django.shortcuts import render

# Create your views here.
def user_auth_view(request):
    return render(request, 'user_auth/user_auth.html')
