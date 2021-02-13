from django.views.decorators import csrf
from NSS_site.forms import LoginForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DonationRequest
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
    return render(request, 'form.html')

# Handle ajax request
@csrf_exempt
def submitData(request):
    if request.method == 'POST':
        print("Ajax request recieved")
        formData = json.loads(request.POST['formData'])
        print(formData)
        try:
            firstName = formData['firstName']
            lastName = formData['lastName']
            address = formData['address']
            contact = formData['contact']
            items = formData['items']
        except:
            print("Invalid Data Received")

        req = DonationRequest(first_name = firstName, last_name = lastName, address = address, phone_number = contact, items = items)
        req.save()
        print("Request saved")
        
        response = JsonResponse({
            'formData': formData,
            'message': "Form submitted successfully",
            'redirect': '/success/'
        })
        return response
    # return redirect('/success/')

def success(request):
    return render(request, 'success.html')

def list(request):
    donation_request_list = DonationRequest.objects.order_by('-time_of_request')
    context = {'donation_request_list': donation_request_list }
    return render(request, 'list.html', context)

def details(request, request_id_no):
    req = get_object_or_404(DonationRequest, id_no=request_id_no)
    return render(request, 'details.html', {'donation_request':req})