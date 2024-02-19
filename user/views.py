from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode,  urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from .utils import token_generator
from .forms import RegistrationForm, LoginForm, PasswordChangeForm, ShippingAddressForm
from .models import ShippingAddress, CustomUser


# Create your views here.
def user_auth_view(request):
    reg_form = RegistrationForm
    login_form = LoginForm

    context = {
        "reg_form": reg_form,
        "login_form": login_form
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
                    "noreply@essence.com",
                    [user.email],
                    headers={"Message-ID": "@essence-hotdesk"},
                )
                # send email
                email.send(fail_silently=False)
                
                messages.success(request, "Your Registration is Successful, check your mailbox to activate your account before login")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
                print(f"Error sending email: {e}")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    form = LoginForm(request.POST)
    reg_form = RegistrationForm(request.POST)
    context = {
        "reg_form": reg_form,
        "login_form": form
    }



    return render(request, 'user_auth/user_auth.html', context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        remember_me = request.POST.get('remember_me')
        if user is not None:
            login(request, user)

            if not remember_me:
                # Set session to expire when the browser is closed
                request.session.set_expiry(0)
            greetings = "You're Welcome!"
            messages.success(request, greetings)
            # redirect to home
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    form = LoginForm(request.POST)
    reg_form = RegistrationForm(request.POST)
    context = {
        "reg_form": reg_form,
        "login_form": form
    }

    return render(request, 'user_auth/user_auth.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, "You've been logged out successfully")
    # Redirect to login
    return redirect('user_auth')


def user_profile(request):
    change_password_form = PasswordChangeForm(request.POST)
    user_shipping_address = None
    
    if request.user.is_authenticated:
        user_shipping_address, created = ShippingAddress.objects.get_or_create(user=request.user )
    
    context = {
        "user_shipping_address": user_shipping_address,
        "change_password_form": change_password_form,
    }
    
    return render(request, 'user_profile/user_profile.html', context)

def update_user_info(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user  = get_object_or_404(CustomUser, pk = request.user.id)
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            
            user.email= email
            user.first_name=first_name
            user.last_name=last_name
            
            user.save()
            messages.success(request, "Updated successfully!")
        else:
            # Unauthenticated user
            messages.warning(request, 'Only Authenticated User is Allowed')
            raise PermissionDenied
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_shipping_info(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_shipping_address  = get_object_or_404(ShippingAddress, user=request.user )
            
            email = request.POST['email']
            phone = request.POST['phone']
            street_address = request.POST['street_address']
            post_code = request.POST['post_code']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']
            
            if user_shipping_address:
                user_shipping_address.email = email
                user_shipping_address.phone = phone
                user_shipping_address.street_address = street_address
                user_shipping_address.post_code = post_code
                user_shipping_address.city = city
                user_shipping_address.state = state
                user_shipping_address.country = country
                
                user_shipping_address.save()
                messages.success(request, "Updated Successfully!")
                
        else:
            # Unauthenticated user
            messages.warning(request, 'Only Authenticated User is Allowed')
            raise PermissionDenied
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def change_password(request):
    if request.method == 'POST':
        change_password_form = PasswordChangeForm(user=request.user, data=request.POST)

        if change_password_form.is_valid():
            change_password_form.save()
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        change_password_form = PasswordChangeForm(user=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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