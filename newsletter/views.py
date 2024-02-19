from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

from .models import NewsletterSubscribers
from user.models import CustomUser
# Create your views here.
def subscribe_newsletter(request):
    try:
        
        if request.user.is_authenticated:
            user = get_object_or_404(CustomUser, pk= request.user.id)
            newsletter, created = NewsletterSubscribers.objects.get_or_create(user=user, email=user.email)
            user.is_subscribed_newsletter = True
            user.save()
            
            # set up email notification to user
            email_subject = '@essence-newsletter'
            email_msg =  "Thank you for for subscribing to our newsletter, We'll keep you posted on our product and trends."      
            email_body = f"Hi {newsletter.email}, {email_msg}"
            
            email = EmailMessage(
                email_subject,
                email_body,
                "noreply@essence.com",
                [newsletter.email],
                headers={"Message-ID": "@essence-hotdesk"},
            )
            # send email
            email.send(fail_silently=False)
            messages.success(request, "Successfully Subscribed to Newsletter!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    
    except Exception as e:
        messages.error(request, f'Internal Server Error {e}')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    return render(request, 'user_profile/user_profile.html')

def unsubscribe_newsletter(request):
    try:
        
        if request.user.is_authenticated:
            user = get_object_or_404(CustomUser, pk= request.user.id)
            newsletter = get_object_or_404(NewsletterSubscribers, user=user, email=user.email)
            user.is_subscribed_newsletter = False
            user.save()
            
            newsletter.delete()
            
            # set up email notification to user
            email_subject = '@essence-newsletter'
            email_msg =  "You have successfully unsubscribed from our newsletter, Hope to get in touch with you again."      
            email_body = f"Hi {newsletter.email}, {email_msg}"
            
            email = EmailMessage(
                email_subject,
                email_body,
                "noreply@essence.com",
                [newsletter.email],
                headers={"Message-ID": "@essence-hotdesk"},
            )
            # send email
            email.send(fail_silently=False)
            messages.success(request, "Successfully Unsubscribed from Newsletter!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    
    except Exception as e:
        messages.error(request, f'Internal Server Error {e}')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    return render(request, 'user_profile/user_profile.html')