from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode,  urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.contrib.auth import login, logout
from django.views.generic.base import View

from .utils import token_generator
from .forms import RegistrationForm, LoginForm
from .models import ShippingAddress, CustomUser

# Create your views here.
def user_auth_view(request):
    reg_form = RegistrationForm
    login_form = LoginForm

    context = {
        "reg_form": reg_form
    }

    return render(request, 'user_auth/user_auth.html', context)

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Form data is valid; create a new user,
            user = form.save()
            # create user
            # e user profile
            new_shipping_address = ShippingAddress.objects.create(user=user, id_user=user.id)
            new_shipping_address.save()
            

            user.is_active = False
            user.save()
            # email subject here
            email_subject = 'Activate Your Account'
            # email body
           
            token = token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            link = reverse('activate', kwargs={
                'uidb64': uidb64, 'token': token
            })
            
            domain = get_current_site(request).domain
            activate_url = 'http://'+domain+link
            email_body = f"Dear {user.email},  Please use this link to veify your account\n {activate_url}"
            try:
                # setup email
                email = EmailMessage(
                    email_subject,
                    email_body,
                    "noreply@abzrecipe.com",
                    [user.email],
                    headers={"Message-ID": "@essence-hotdesk"},
                )
                # send email
                email.send(fail_silently=False)
                
                messages.success(request, "Your Registration is Successful, check your mailbox to activate your account before login")
                return redirect('user_auth')
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
                print(f"Error sending email: {e}")
                return redirect('user_auth')
    form = RegistrationForm(request.POST)
    context ={
        'reg_form': form
    }


    return render(request, 'user_auth/user_auth.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            greetings = "You're Welcome "+user.username
            messages.success(request, greetings)
            # redirect to home
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
    
    form = LoginForm(request.POST)
    context ={
        'login_form': form
    }

    return render(request, 'user_auth/user_auth.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, "You've been logged out successfully")
    # Redirect to login
    return redirect('user_auth')


def user_profile(request):
    return render(request, 'user_profile/user_profile.html')



class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=id)
            greetings = f"You're Welcome {user.email}, Account activated successfully."
            if user.is_active:
                messages.info(request, "user account is already activated.")
                login(request,user)
                # Redirect to a success page, e.g., user's profile page
                return redirect("home")
            user.is_active = True
            user.save()
            login(request,user)
            messages.success(request, greetings)
            return redirect("home")
            
        except Exception as ex:
            messages.error(request, "Error Activating Your Account.")
            print(f"Error Activating Your Account: {ex}")
        return redirect("user_auth")