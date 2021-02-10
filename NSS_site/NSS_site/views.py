from NSS_site.forms import LoginForm
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def form(request):
    formData = {}
    if request.method == 'POST':
        print("Ajax request recieved")
        formData = json.loads(request.POST['formData'])
        firstName = formData['firstName']
        lastName = formData['lastName']
        return JsonResponse({
            'out_string': 'out_string_test',
            'formData': formData,
        })
    else:
        return render(request, 'form.html')