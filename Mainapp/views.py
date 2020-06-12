from django.shortcuts import render
from  rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
import random
import datetime
from .serializers import *
# Create your views here.

#Check is User Email Id Exsist
def is_user_email_exist(email):
    check=Users.objects.filter(Users_Email=email).count()
    if check==0:
        return True
    else:
        return False




#Register User
@api_view(["PUT"])
def Register(request):
    apiresponse= {}
    #Getting The Comming Request
    data = JSONParser().parse(request)
    if ("Users_Email" in data and data['Users_Email'] != "" and "Users_Password" in data and data['Users_Password'] != ""):
        email=data['Users_Email']
        password=data['Users_Password']
        if is_user_email_exist(email):
            serializer = Userserilazers(data=data)
            if serializer.is_valid():
                serializer.save()
                apiresponse['status'] = 102
                apiresponse['Details'] = "Registration Complete"
            else:
                apiresponse['status'] = 103
                apiresponse['Details'] = serializer.errors
        else:
            apiresponse['status'] = 101
            apiresponse['Details'] = "Email Id Already Exist"
    else:
        apiresponse['status'] = 104
        apiresponse['Details'] = "Need To Pass User Name And Password"

    return Response(apiresponse)


@api_view(["POST"])
def Login(request):
    apiresponse= {}
    # Getting The Comming Request
    data = JSONParser().parse(request)
    if ("Users_Email" in data and data['Users_Email'] != "" and "Users_Password" in data and data[
        'Users_Password'] != ""):
        email = data['Users_Email']
        password = data['Users_Password']
        if is_user_email_exist(email)==False:

            check_valid_user=Users.objects.filter(Users_Email=email,Users_Password=password).count()
            if check_valid_user==1:
                apiresponse['status'] = 106
                apiresponse['Details'] = "Login Success"
            else:
                apiresponse['status'] = 107
                apiresponse['Details'] = "Invalid Password"
        else:
            apiresponse['status'] = 105
            apiresponse['Details'] = "This User Email Not Exist"
    else:
        apiresponse['status'] = 104
        apiresponse['Details'] = "Need To Pass User Name And Password"
    return Response(apiresponse)

@api_view(["POST"])
def Forgotpassword(request):
    apiresponse= {}
    # Getting The Comming Request
    data = JSONParser().parse(request)
    if ("Users_Email" in data and data['Users_Email'] != "" ):
        email = data['Users_Email']

        if is_user_email_exist(email)==False:
            check_valid_user=Users.objects.get(Users_Email=email)
            apiresponse['status'] = 108
            apiresponse['Password'] = check_valid_user.Users_Password
        else:
            apiresponse['status'] = 105
            apiresponse['Details'] = "This User Email Not Exist"
    else:
        apiresponse['status'] = 104
        apiresponse['Details'] = "Need To Pass User Name And Password"
    return Response(apiresponse)


@api_view(["GET"])
def Allplans(request):
    queryset = Plans.objects.all()
    serializer = Planserilazers(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def All_Intrest_Category(request):
    queryset = Intrest_Category.objects.all()
    serializer = Intrest_Categoryserilazers(queryset, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def All_Intrest_Sub_Category(request):
    apiresponse = {}
    # Getting The Comming Request
    data = JSONParser().parse(request)
    if ("Cat_id" in data and data['Cat_id'] != ""):
        cat=int(data['Cat_id'])
        maincat=Intrest_Category.objects.get(id=cat)
        queryset = Intrest_Sub_Category.objects.filter(Category=maincat)
        serializer = Intrest_Sub_Categoryserilazers(queryset, many=True)
        return Response(serializer.data)
    else:
        apiresponse['status'] = 109
        apiresponse['Password'] = "Pass Catgory ID"
        return Response(apiresponse)

@api_view(["POST"])
def Setuserplan(request):
    apiresponse= {}
    # Getting The Comming Request
    data = JSONParser().parse(request)
    if ("Users_Email" in data and data['Users_Email'] != "" and "plan_id" in data and data['plan_id'] != "" ):
        email = data['Users_Email']
        planid = data['plan_id']

        if is_user_email_exist(email)==False:
            planid = int(data['planid'])
            plan = Plans.objects.get(id=planid)
            user = Users.objects.get(Users_Email=email)
            user.Users_Current_Plan=plan
            user.save()
            apiresponse['status'] = 110
            apiresponse['Password'] = "Plan Updated"
        else:
            apiresponse['status'] = 105
            apiresponse['Details'] = "This User Email Not Exist"
    else:
        apiresponse['status'] = 104
        apiresponse['Details'] = "Need To Pass User Name And Password"
    return Response(apiresponse)


@api_view(["POST"])
def Videos_for_specific_Category(request):
    apiresponse = {}
    # Getting The Comming Request
    data = JSONParser().parse(request)
    if ("Cat_id" in data and data['Cat_id'] != ""):
        cat=int(data['Cat_id'])
        maincat=Intrest_Category.objects.get(id=cat)
        queryset = Intrest_Sub_Category.objects.filter(Category=maincat)
        serializer = Intrest_Sub_Categoryserilazers(queryset, many=True)
        return Response(serializer.data)
    else:
        apiresponse['status'] = 109
        apiresponse['Password'] = "Pass Catgory ID"
        return Response(apiresponse)

