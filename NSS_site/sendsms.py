import requests

url = "https://www.fast2sms.com/dev/bulk"
def send_sms(to_number,msg_body):
    try:
        payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers={}".format(msg_body,to_number)
        headers = {
        'authorization': "thzXerS7DkWlYc6UHdRvVKNoq4fGPT8Q30Fb1EA9yLjxMpmsCJ7F8OXlGWZL5vsegzR1BaIuirnmMfHy",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        if response.ok==True:
            return 1
        else:
            return 0
    except:
        return 0
