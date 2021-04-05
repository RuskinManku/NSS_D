from django.views.decorators import csrf
from NSS_site.forms import LoginForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from .models import DonationRequest, Volunteer
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

@csrf_exempt
def volunteerSubmitData(request):
    if request.method == 'POST':
        print("Ajax request recieved (volunteer)")
        formData = json.loads(request.POST['formData'])
        print(formData)
        try:
            firstName = formData['firstName']
            lastName = formData['lastName']
            idno = formData['idno']
            contact = formData['contact']
            date = formData['date']
            startTime = formData['starttime']
            endTime = formData['endtime']
            print(startTime, endTime)
            # calendly_link = formData['calendly_link']
        except:
            print("Invalid Data Received")

        req = Volunteer(first_name = firstName, last_name = lastName, idno = idno, phone_number = contact, date=date, start_time=startTime, end_time=endTime)
        req.save()
        print("Request saved")
        
        response = JsonResponse({
            'formData': formData,
            'message': "Form submitted successfully",
            'redirect': '/volunteer_signup_success/'
        })
        return response
    # return redirect('/success/')

def success(request):
    return render(request, 'success.html')

def volunteerSuccess(request):
    return render(request, 'volunteer_signup_success.html')

@staff_member_required
def list(request):
    donation_request_list = DonationRequest.objects.order_by('-time_of_request')
    context = {'donation_request_list': donation_request_list }
    return render(request, 'list.html', context)

@staff_member_required
def details(request, id_no):
    req = get_object_or_404(DonationRequest, id_no=id_no)
    return render(request, 'details.html', {'donation_request':req})

def index(request):
    return render(request, 'index.html')

def volunteerSignup(request):
    return render(request, 'volunteer_signup.html')