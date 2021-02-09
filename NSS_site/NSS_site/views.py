from NSS_site.forms import LoginForm
from django.shortcuts import render


def login(request):
    username = "not logged in"
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            # print("######IS VALID")
            username = MyLoginForm.cleaned_data['username']
    else:
        # print("######EMPTY FORM")
        MyLoginForm = Loginform()
		
    return render(request, 'loggedin.html', {"username" : username})