from django.http import HttpResponse, FileResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect


from django.contrib.sessions.backends.cache import SessionStore
from django.contrib.auth.decorators import login_required
from . import auth
from .decorators import user_is_auth

from . import forms,models, process
from .models import OnboardingWizard, ContactInformation
import json, datetime

from .services import cwprojects, cwsettings, cwcompany, cwopportunities, cwfinance, cwtickets
import requests, os
from requests_toolbelt.multipart.encoder import MultipartEncoder


@user_is_auth
def index(request):

    indexData = {}
    companyId = request.session['contactData']['company']['id']

    conditions = "?conditions=recordType!='ProjectTicket'%20AND%20closedFlag=0" #%20or%20status/name=''"
    waitCondition = "?conditions=recordType!='ProjectTicket'%20AND%20closedFlag=0%20AND%20status/name='Waiting Customer'"
    waitTickets = cwtickets.getTickets(companyId, waitCondition)
    waitCount = len(waitTickets)

    indexData['WaitTicketCount'] = waitCount

    tickets = cwtickets.getTickets(companyId, conditions)
    ticketCount = len(tickets)
    indexData['OpenTicketCount'] = ticketCount


    opData = cwopportunities.opportunities
    openOps = opData.getOpenOps(companyId)
    test = len(openOps)

    indexData['OpenOpCount'] = test


    sendData = {'indexData': indexData, 'userData': request.session['contactData']}

    return render(request,'data/index.html', context=sendData)

@user_is_auth
def client_view(request):

    return render(request, 'pages/client_view.html', context=None)


@user_is_auth
def download(request, file_id):

    downloadUrl = cwsettings.CW_BASE_URL + "system/documents/" + str(file_id) + "/download"
    r = requests.get(url=downloadUrl, headers=cwsettings.HEADER_AUTH, stream=True)

    response = FileResponse(r.raw)
    response['Content-Type'] = r.headers['Content-Type']
    response['Content-Disposition'] = r.headers['Content-Disposition']
    response['Content-Length'] = r.headers['Content-Length']

    return response





def login(request):
    if 'userLogged' in request.session:
        if request.session['userLogged'] == True:
            return redirect('index')

        pass

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        #print(form)
        if form.is_valid():
                checkAuth = auth.auth(username=form.cleaned_data['emailAddress'], password=form.cleaned_data['password'])
                if checkAuth['success'] is 'false' or checkAuth['success'] is False:
                    print('Failed Login')
                    data = "The username/password did match in our system."
                    return render(request, 'pages/login.html', context={'failed':data})
                elif checkAuth['success'] is True:
                    print('Login Succeeded')
                    request.session['userPermissions'] = auth.get_perm(user_id=str(checkAuth['contactId']))
                    request.session['contactid'] = checkAuth['contactId']
                    request.session['userLogged'] = checkAuth['success']
                    request.session['sessionStart'] = datetime.datetime.now().__str__()
                    contactData = auth.getContactData(checkAuth['contactId'])
                    request.session['contactData'] = contactData
                    return redirect('index')

        print("failed")
        return render(request, 'pages/login.html', context={'one': 'one'})
    else:
        data = { 'projData': 'data' }

        return render(request, 'pages/login.html', context=data)





@user_is_auth
def logout(request):

    try:
        del request.session['userLogged']
        del request.session['contactid']
        del request.session['sessionStart']
        del request.session['contactData']
        request.session.flush()

    except KeyError:
        pass
    data = {'one':'one'}
    return render(request, 'pages/login.html', context=data)


