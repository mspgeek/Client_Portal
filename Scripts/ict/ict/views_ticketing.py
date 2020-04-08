from django.http import HttpResponse, FileResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from operator import itemgetter

from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import loader, RequestContext
from django.views.decorators.http import require_POST
from django.conf import settings

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
def doThing(dict, merge):

    for index, item in enumerate(merge):
        merge[index]['dateEntered'] = merge[index]['dateCreated']
    dict2 = dict + merge
    dict3 = sorted(dict2, key=itemgetter('dateEntered'), reverse=True)

    return dict3


@user_is_auth
def viewticket(request, ticketid):


    companyId = request.session['contactData']['company']['id']
    company = cwcompany.companies
    companyData = company.getCompany(id=companyId)

    ticket = cwtickets.getTicketData(ticketid)
    ticketNotes = cwtickets.getTicketNotes(ticket['_info']['notes_href'])
    ticketTime = cwtickets.getTicketTimeEntries(ticket['_info']['timeentries_href'])
    ticketResources = cwtickets.getTicketResources(ticket['_info']['scheduleentries_href'])

    test = doThing(ticketTime, ticketNotes)



    sendData = {'userData': request.session['contactData'], 'ticketData': ticket, 'ticketDetails':test, 'resources':ticketResources }
    return render(request, 'ticketing/viewticket.html', context=sendData)


@user_is_auth
def tickets(request):

    companyId = request.session['contactData']['company']['id']
    conditions = "?conditions=recordType!='ProjectTicket'" #%20or%20status/name=''"
    tickets = cwtickets.getTickets(companyId, conditions)

    company = cwcompany.companies
    companyData = company.getCompany(id=companyId)

    sendData = {'userData': request.session['contactData'], 'companyData':companyData, 'ticketData': tickets}

    return render(request, 'ticketing/tickets.html', context=sendData)


@user_is_auth
def newticket(request):

    sendData = {'userData': request.session['contactData']}

    return render(request, 'ticketing/new.html', context=sendData)




@user_is_auth
def newtickettype(request, type=1):

    #getClientData
    companyId = request.session['contactData']['company']['id']
    company =  cwcompany.companies
    companyData = company.getCompany(id=companyId)
    #print(companyData)
    computerData = company.getConfigs(companyid=companyId)

    if type is 1:

        form = forms.BasicTicketForms(request.POST, request.FILES, error_class=forms.DivErrorList)

        sendData = {'userData': request.session['contactData'], 'companyData':companyData, 'Form':form, 'computerData':computerData}

        return render(request, 'ticketing/type/basic.html', context=sendData)

    if type is 2:

        sendData = {'userData': request.session['contactData'], 'companyData':companyData}

        return render(request, 'ticketing/type/user.html', context=sendData)

    if type is 3:

        sendData = {'userData': request.session['contactData'],'companyData':companyData}

        return render(request, 'ticketing/type/sales.html', context=sendData)

    if type is 4:

        sendData = {'userData': request.session['contactData'], 'companyData':companyData}

        return render(request, 'ticketing/type/crit.html', context=sendData)

@require_POST
def updateTicket(request, ticketid=0):
    print('Updating Ticket')
    if request.method == 'POST':
        print(request.POST)
        form = forms.UpdateTicket(request.POST, error_class=forms.DivErrorList)
        print(request.POST)
        if True:

            text = request.POST['text']
            cid = request.POST['id']
            ticketid = request.POST['ticketid']

            data = {"text":text,"customerUpdatedFlag":"true","detailDescriptionFlag": "true", "contact":{"id":cid}, "member":{"id":"0"}}

            data = json.dumps(data)
            print(data)

            url = cwsettings.CW_TICKETS+"/"+ticketid+"/notes"
            r = requests.post(url=url, data=data, headers=cwsettings.HEADER_AUTH)
            returnData = r.json()
            print(returnData)

            if r.status_code == 200 and returnData['id']:
                success = "<span class='alert alert-success'><i class='icon icon-check2 icon-2x'></i> Ticket Updated Successfully</span>"
            else:
                error = "error"
            ticket = returnData
            test = []
            return redirect('viewticket', ticketid=ticketid)
        else:
            print('Form Not Valid')
            return redirect('viewticket', ticketid=ticketid)
    print('Not Posted')
    return


@require_POST
@user_is_auth
def createTicket(request):

    ## if this is a POST request we need to process the form data
    if request.method == 'POST':
        print('METHOD POST')
        ## create a form instance and populate it with the data from the request:
        form = forms.BasicTicketForms(request.POST, error_class=forms.DivErrorList)
        ## check if its valid data
        if form.is_valid():
            ## process the data in form.cleaned_data as required
            # ....send to cw
            companyId = request.session['contactData']['company']['id']
            company = cwcompany.companies
            companyData = company.getCompany(id=companyId)
            # print(companyData)
            computerData = company.getConfigs(companyid=companyId)
            print(request.POST)
            print(form.cleaned_data)

            ## build out api stuff for CW
            #files = {'file': (file, file.file, 'application/octet-stream')}
            ###
            ##BOARD ID's 1-helpdesk, 21-clientaccess, 24-Proactive, 28-Sales,29 -KSDS, 30-Artscroll, 32-Gigabit, 33 -DChem, 35-Strategic
            ###
            company = form.cleaned_data['company']
            if 'Artscroll' in company:
                boardId='30'
            elif 'Strategic' in company:
                boardId='35'
            elif 'Gigabit' in company or 'Star' in company:
                boardId = '32'
            else:
                boardId='38'
            ##Set data into JSON Like Code (python array)
            data = {'summary':str(form.cleaned_data['title']), 'company':{'id':str(form.cleaned_data['companyid'])},'contact':{'id':str(form.cleaned_data['contactid'])}, 'initialDescription':str(request.POST.get('details')), 'board':{'id':boardId}}
            print("DATA : ")
            ##Change Array into JSON
            data = json.dumps(data)
            ##Echo so I can see it
            print(data)

            url = cwsettings.CW_TICKETS ##CW_TICKETS = CW_BASE_URL + "fqdn.com/v4_6_release/apis/3.0/service/tickets/"
            ##SEND DATA
            r = requests.post(url=url, data=data, headers=cwsettings.HEADER_AUTH)
            returnData = r.json()
            print(returnData)

            if r.status_code == 200 and returnData['id']:
                success = "<span class='alert alert-success'><i class='icon icon-check2 icon-2x'></i> File Uploaded Successfully</span>"
            else:
                error = "error"
            ticket = returnData
            test = []

            ## re-render the page, hopefully with the new cw data
            sendData = {'userData': request.session['contactData'], 'companyData': companyData, 'Form': form,
                            'computerData': computerData}

            ## redirect to the new HTML
            sendData = {'userData': request.session['contactData'], 'ticketData': ticket, 'ticketDetails': test}
            return render(request, 'ticketing/viewticket.html', context=sendData)

        else:
            print(form.errors)
            print('FAILED DATACHECK')
            # getClientData
            companyId = request.session['contactData']['company']['id']
            company = cwcompany.companies
            companyData = company.getCompany(id=companyId)
            # print(companyData)
            computerData = company.getConfigs(companyid=companyId)


            form = forms.BasicTicketForms(request.POST, request.FILES, error_class=forms.DivErrorList)

            sendData = {'userData': request.session['contactData'], 'companyData': companyData, 'Form': form,
                            'computerData': computerData}

            return render(request, 'ticketing/type/basic.html', context=sendData)
    ## if its a get or we are here in error:
    else:

        HttpResponseRedirect('p/list')

