from django.views.decorators import csrf
from NSS_site.forms import LoginForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from .models import DonationRequest, VolunteerSlot
from sendsms import send_sms

from datetime import datetime, tzinfo
import json
import pytz


def bad_request(message):
    response = HttpResponse(json.dumps({'message': message}), 
        content_type='application/json')
    response.status_code = 400
    return response

def getDateTimeFromString(dateStr, timeStr):
    datetimeString = dateStr + ' ' + timeStr
    print(f'datetimeString : {datetimeString}')
    timezone = pytz.timezone("Asia/Kolkata")
    out = datetime.strptime(datetimeString, "%b %d, %Y %I:%M %p")
    # out = timezone.localize(out)
    print(f'Strifed : {out}')
    return out

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
    slots = VolunteerSlot.objects.filter(start_time__gte=datetime.now())
    
    for slot in slots:
        print('\n\n')
        print(slot.first_name + ' ' + slot.last_name)
        print(slot.start_time.date)
        print(slot.start_time)
        print(slot.start_time.time)
        print('\n---------------------------------')

    return render(request, 'form.html', {'slots':slots})

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
            slot_id = int(formData['slot_id'])
        except Exception as e:
            print(e)
            print("Invalid Data Received")

        # print('Slot_id : ', slot_id)

        slot = VolunteerSlot.objects.get(slot_id=slot_id)
        req = DonationRequest(slot=slot, first_name = firstName, last_name = lastName, address = address, phone_number = contact, items = items)
        
        
        print(f"Sending SMS to {slot.phone_number}")
        slot_phonenumber=slot.phone_number
        slot_message=f"{firstName} {lastName} registered for slot on {slot.start_time}. Pickup adress: {address}, Donor Phone number: {contact}"
        if send_sms(slot_phonenumber,slot_message):
            print("SMS sent successfully")
            req.save()
            print("Request saved")
            
        else:
            print("SMS sending unsucessful")
            return bad_request('Request unsucessful, Please Try Again')
            
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
            startTime = getDateTimeFromString(date, formData['starttime'])
            endTime = getDateTimeFromString(date, formData['endtime'])
            # calendly_link = formData['calendly_link']
        except:
            print("Invalid Data Received")

        req = VolunteerSlot(first_name = firstName, last_name = lastName, idno = idno, phone_number = contact, start_time=startTime, end_time=endTime)
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
def volunteerPage(request):
    return render(request, 'volunteer_page.html')

@staff_member_required
def details(request, id_no):
    req = get_object_or_404(DonationRequest, id_no=id_no)
    return render(request, 'details.html', {'donation_request':req})

def index(request):
    return render(request, 'index.html')

def volunteerSignup(request):
    return render(request, 'volunteer_signup.html')


def listVolunteerSlots(request):
    print('sadkjh a : ')
    slots = VolunteerSlot.objects.filter(start_time__gte=datetime.now())

    return render(request, 'slot_table.html', {'slots':slots})


def listRequests(request):
    # print('sadkjh a : ')
    requests = DonationRequest.objects.filter(slot__start_time__gte=datetime.now())

    return render(request, 'requests_table.html', {'requests':requests})
