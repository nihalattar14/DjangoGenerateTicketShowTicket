from django.shortcuts import render, redirect
from django.utils import log

from .models import User1
import mysql.connector
from operator import itemgetter
from django.contrib import messages
import traceback
import requests
import json



# Create your views here.

def welcome(req):
    return render(req,'welcome.html')

def login(req):
    try:
        con = mysql.connector.connect(host='127.0.0.1', user='admin', passwd='admin4321', database='login')
        cursor = con.cursor(buffered=True)
        sqlcommand = "select email from login_user1"
        cursor.execute(sqlcommand)
        con1 = mysql.connector.connect(host='127.0.0.1', user='admin', passwd='admin4321', database='login')
        cursor1 = con1.cursor()
        sqlcommand2 = "select password from login_user1"
        cursor1.execute(sqlcommand2)

        e = []
        p = []

        for i in cursor:
            e.append(i)

        for j in cursor1:
            p.append(j)

        print("e>>>", e)
        print("p>>>", p)

        res = list(map(itemgetter(0), e))
        print("res>>>", res)
        res1 = list(map(itemgetter(0), p))
        print("res1>>>", res1)

        warning_message = "Check Username and Password"

        if req.method == "POST":
            print("Enter into req.method == ")
            email = req.POST['email']
            password = req.POST['password']
            k = len(res)
            print("k>>>>>>>>>>>>>", k)
            i = 0

            while i < k:
                print("Enter into req.method == While>>>>>>>>>> ")
                if res[i] == email and res1[i] == password:
                    print("i>>>>>>>>", i)
                    print("Enter into req.method == While -> if >>>>>>>>> ")
                    return render(req, 'support.html', {'email': email})
                    break
                i += 1

            else:
                print("Enter into req.method == While -> else >>>>>>>>> ")
                messages.info(req, warning_message)
                return render(req, 'login.html', {'warning_message': warning_message})

        # else:
        #     print("Enter into req.method == else >>>>>>>>> ")
        #     messages.info(req, warning_message)
        #     return render(req, 'login.html')
        # return redirect('support')
        # else:
        #     print("Enter into req.method else >>>>>>>>> ")
        #     messages.info(req,"Check Username and Password")
        #     return redirect('support')+
        print("End Function")
        return render(req, 'login.html')
    except Exception as e:
        print('Exception>>>>>>>>>>>>',e, str(traceback.format_exc()))


def register(req):
    # print("enter in register")

    try:
        if req.method == "POST":
            # print("enter in if req.method == ")
            user = User1()
            user.first_name = req.POST['first_name']
            user.last_name = req.POST['last_name']
            user.email = req.POST['email']
            user.password = req.POST['password']

            if user.email == "" or user.password == "":
                # print("enter in if")
                messages.info(req, "All fields are required")
                # return redirect('register/')
            else:
                # print("enter in else")
                user.save()
                messages.info(req, "Successfully registerd")
        else:

            print("enter in else req.method == ")
        return render(req, 'register.html')
    except Exception as e:
        print('Exception>>>>>>>>>>>>',e, str(traceback.format_exc()))

def support(req):
    return render(req,'support.html')


def addticket(req):
    print("enter in  addticket ")
    try:
        headers = {"orgId": "60001280952",
                   "Authorization": "9446933330c7f886fbdf16782906a9e0",
                   'content-type': 'application/json',
                   'Accept-Charset': 'UTF-8'
                   }
        url = "https://desk.zoho.in/api/v1/tickets"
        if req.method == "POST":
            print("enter in if addticket req.method == ")
            departmentId = req.POST['department']
            category = req.POST['category']
            subject = req.POST['subject']
            description = req.POST['description']
            contact_name = req.POST['contact_name']
            email = req.POST['email']
            phone = req.POST['phone']
            priority = req.POST['priority']
            attach = req.POST['attach']

            id_split = departmentId.split("-")
            id_split = id_split[1]

            data = {
                "subject": subject,
                "departmentId": id_split,
                "contact": {
                    "firstName": contact_name,
                    "email": email,
                    "phone": phone
                }
            }

            request = requests.post(url=url, json=data, headers=headers)
            print("request>>>>", request)
            print("request.status_code>>>>>>>>", request.status_code)

            a = request.json()
            print("a>>>>>>>>>>>", a)
            # ticketdetails = {
            #     'ticket_id': a['ticketNumber'],
            #     'subject': a['subject'],
            #     'status': a['status'],
            #     'description': a['description']
            # }
            #
            # showtickets(req, ticketdetails)
            # success_message = "Ticket Added Successfully "
            return render(req, 'showtickets.html')
        else:
            print("enter in else addticket req.method == ")
        return render(req, 'addticket.html')
    except Exception as e:
        print('Exception>>>>>>>>>>>>', e, str(traceback.format_exc()))

def showtickets(req):
    return render(req, 'showtickets.html')
    # print("ticketdetails>>>>>>>>>",ticketdetails)

    # try:
    #     subject = ticketdetails['subject']
    #     description = ticketdetails['description'],
    #     ticket_ID = ticketdetails['ticket_id'],
    #     status = ticketdetails['status']
    #
    #     headers = {"orgId": "60001280952",
    #                "Authorization": "9446933330c7f886fbdf16782906a9e0",
    #                'content-type': 'application/json',
    #                'Accept-Charset': 'UTF-8'
    #                }
    #
    #     ticket_ID = ticketdetails['ticket_id']
    #     url = "https://desk.zoho.in/api/v1/tickets/" + ticket_ID + "?"
    #     request = requests.get(url=url, headers=headers)
    #     print("request>>>>", request)
    #     print("request.status_code>>>>>>>>", request.status_code)
    #
    #     return render(req, 'showtickets.html')
    # except Exception as e:
    #     print('Exception>>>>>>>>>>>>', e, str(traceback.format_exc()))




