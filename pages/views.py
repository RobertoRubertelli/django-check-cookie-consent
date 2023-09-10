from django.shortcuts import render ,redirect 

## I neeed a function to read the policy html
def ReadPolicy(request):
    context = {}
    return render(request,'cookie_consent/privacypolicy.html',context)

## I want to check if the visitor accepted the cookies.
## In template the signin is calling this function.
## I start with try , I'm want to manage the error in except.
## In except the visitor cannot go ahead in log in.
## request.COOKIES["displayCookieConsent"] it is in the cookie header dictionary.
## When the visitor accept the cookie, the cookie value get an 'y'.
## if the cookie it is not present, still en error.
## The visitor didn't accept the cookie.
def CheckConsentForLogin(request):

    try:
        mycookie = request.COOKIES["displayCookieConsent"]
        if mycookie == 'y':
            return redirect('account_login')
    except:
        mymsg = "Please Accept Cookies consent before ask for the login, Click Confirm Your Consent in the top nav bar, in the Home Page"
        context= {'mymsg':mymsg}
    return render(request,'home.html',context)


## I want to check if the visitor accepted the cookies.
## In template the sign up is calling this function.
## I start with try , I'm want to manage the error in except.
## In except the visitor cannot go ahead in sign up.
## request.COOKIES["displayCookieConsent"] it is in the cookie header dictionary.
## When the visitor accept the cookie, the cookie value get an 'y'.
## if the cookie it is not present, still en error.
## The visitor didn't accept the cookie.
def CheckConsentForSignUp(request):
    try:
        mycookie = request.COOKIES["displayCookieConsent"]
        if mycookie == 'y':
            return redirect('account_login')
    except:
        mymsg = "Please Accept Cookies consent before ask for the Sign Up, Click Confirm Your Consent in the top nav bar, in the Home Page"
        context= {'mymsg':mymsg}
    return render(request,'home.html',context)


def Home(request):

    context= {}
    
    return render(request,'home.html',context)


