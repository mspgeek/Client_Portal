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
def project_detail(request):

    return render(request, 'data/project_detail.html', context=None)

@user_is_auth
def project_list(request):

    projects = cwprojects.projects
    projectList = projects.listProjects()
    print(projectList)
    project = { 'projData': projectList }

    return render(request, 'data/project_list.html', context=project)

@user_is_auth
@require_POST
def file_upload(request):

    if request.POST:
        fileData = request.POST
        file = requests.FILES
        recordType = request['']
        return


@require_POST
def project_upload(request):
    ## if this is a POST request we need to process the form data
    if request.method == 'POST':
        ## create a form instance and populate it with the data from the request:
        form = forms.ProjectDetailForms(request.POST)
        ## check if its valid data
        if form.is_valid():
            ## process the data in form.cleaned_data as required
            #....send to cw



            ## redirect to the new HTML
            return
    ## if its a get or we are here in error:
    else:

        HttpResponseRedirect('p/list')


@user_is_auth
def onboarding(request, id=None, clientid=None):

    ##client_name = request.session['companyname']
    client_name = 'ThirstyDesign, L.L.C.'
    clientid=1

    ##check to see if they have an open onboarding, even if we didn't get here properly.

    checkFor = OnboardingWizard.objects.filter(f1_client_name=client_name, complete=False)
    checkFor = getattr(checkFor[0], 'id')
    if int(checkFor) > 0:

        print('Onboarding Check ' + str(checkFor))

        id = checkFor
    else:
        pass

    if request.is_ajax():


        print('inside ajax call')
        try:
            updateData = False
            if id is not None:
                ##This is json data, ALL of the form data submitted.  What we don't want to do is process everything, lets process only the tab that was sent.
                updateData = True
            data = request.POST
            print(data)
            test = {'data':data['name'], 'type':data['type']}
            print('checkProcess')
            checkProcess = process.savePage(data['type'],data,'',id)
            print('exitProcess')

            if checkProcess is True:
                return HttpResponse(content=checkProcess)
            else:
                return HttpResponse(content=test)


        except Exception as e:

                data = {'error':'Unable to process data, error'}
                print('An Exception Occurred: '+e )
                return HttpResponse(content=data)


    if request.method == 'POST':
        ## we are saving additional data



        return
    elif id is not None:
        ## Reopen one
        print("Working in ID: " + str(id))
        ###TempVars to show stuff
        fwBrandTemp = [{'id': '1', 'name':'Cisco'},{'id':'2','name':'Fortinet'},{'id':'3','name':'Netgear'}]
        fwModelTemp = [{'id': '1', 'name':'5506 B'}]
        fwReplace = [{'id':'1','name':'Yes'},{'id':'2','name':'No'}]
        ##WE ARE HERE FOR THE FIRSt TIME

        ##Attempt to get the data we have stored.
        onboardingCheck = OnboardingWizard.objects.get(id=id).to_dict()
        print(onboardingCheck)
        if onboardingCheck['saved_stage'] >= 1:
            getContacts = ContactInformation.objects.filter(onboarding_id_id=id).values()
            getCompanyData = OnboardingWizard.objects.filter(id=id).values()
            print(getContacts)
        else:
            getContacts = ''
            getCompanyData = ''

        company = cwcompany.companies
        request.session['clientid'] = 20096
        companyData = company.getCompany(id=20096)##id=request.session['clientid'])
        contacts = company.getContacts(id=20096)##id=request.session['clientid'])
        #project = cwprojects.projects
        ##created the class
        ##CreateNew
        #createProject = project.createNew(clientid)


        data = {'OnboardingID':id,'Company':companyData[0],'setCompany':getCompanyData,'SetContact':getContacts, 'Contacts':contacts, 'FWBrand':fwBrandTemp, 'FWModel':fwModelTemp, 'FWReplace':fwReplace}

        return render(request, 'data/onboarding_wizard.html', context=data)
    else:
        ##Check if the ID is set.
        ##NEED TO CHECK CLIENTID CUZ WE NEED TO ADD IT IN IF ITS MISSING FOR REASONS

        ##We are not set, create new onboarding
        newOnboard = OnboardingWizard()
        newOnboard.date_start = '2018-09-12'
        newOnboard.saved_stage = 0
        newOnboard.complete = False
        newOnboard.f1_client_id = request.session['clientid']
        newOnboard.f1_client_name = request.session['companyname']
        newOnboard.save()

        onboardingId = newOnboard.pk




        ###TempVars to show stuff
        fwBrandTemp = [{'id': '1', 'name':'Cisco'},{'id':'2','name':'Fortinet'},{'id':'3','name':'Netgear'}]
        fwModelTemp = [{'id': '1', 'name':'5506 B'}]
        fwReplace = [{'id':'1','name':'Yes'},{'id':'2','name':'No'}]
        ##WE ARE HERE FOR THE FIRSt TIME


        company = cwcompany.companies
        companyData = company.getCompany(id=request.session['clientid'])
        contacts = company.getContacts(id=request.session['clientid'])
        #project = cwprojects.projects
        ##created the class
        ##CreateNew
        #createProject = project.createNew(clientid)
        print('notset,stuff')

        data = {'OnboardingID':onboardingId,'Company':companyData[0], 'Contacts':contacts, 'FWBrand':fwBrandTemp, 'FWModel':fwModelTemp, 'FWReplace':fwReplace}

        return render(request, 'data/onboarding_wizard.html', context=data)


    return




@user_is_auth
def onboarding_list(request):

    onboardings = OnboardingWizard.objects.all()

    projects = cwprojects.projects
    projectList = projects.listProjects()

    data = { 'projData': onboardings }

    return render(request, 'data/onboarding_list.html', context=data)


@user_is_auth
def onboarding_temp(request):



    projects = cwprojects.projects
    projectList = projects.listProjectstemp()

    data = { 'projData': projectList, 'userData': request.session['contactData'], 'permissions': request.session['userPermissions']}

    return render(request, 'data/onboarding_temp.html', context=data)



@user_is_auth
def projecttemp(request, project_id):
    print("Working on Project:"+ str(project_id))

    if request.method == 'POST':
        print('METHOD POST')
        ## create a form instance and populate it with the data from the request:
        form = forms.ProjectDetailForms(request.POST, request.FILES, error_class=forms.DivErrorList)
        ## check if its valid data
        if form.is_valid():
            ## process the data in form.cleaned_data as required
            # ....send to cw
            project = cwprojects.projects

            file = form.cleaned_data['fileAdd']
            print(file)

            ## build out api stuff for CW
            files = {'file': (file, file.file, 'application/octet-stream')}
            params = {'recordId': project_id, 'recordType': 'Project','permissions': request.session['userPermissions']}

            success = "<span class='alert alert-success'><i class='icon icon-check2 icon-2x'></i> File Uploaded Successfully</span>"

            doUpload = project.uploadFile(project_id, files, params)

            ## re-render the page, hopefully with the new cw data

            getProject = project.getProject(project_id)

            getDocs = project.getProjectDocuments(project_id)
            fileUpload = forms.ProjectDetailForms(error_class=forms.DivErrorList)
            getTeam = project.getTeamMembers(project_id)
            sendProject = {'Project': getProject, 'Documents': getDocs, 'Team': getTeam, 'Form': form, 'Success': success, 'userData': request.session['contactData'] ,'permissions': request.session['userPermissions']}
            ## redirect to the new HTML
            return render(request, 'data/project_detailtemp.html', context=sendProject)
        else:
            print(form.errors)
            print('FAILED DATACHECK')
            project = cwprojects.projects
            getProject = project.getProject(project_id)

            ##SessionOut the ClientID


            getDocs = project.getProjectDocuments(project_id)
            getTeam = project.getTeamMembers(project_id)
            sendProject = {'Project': getProject, 'Documents': getDocs, 'Team': getTeam, 'Form': form, 'userData': request.session['contactData'],'permissions': request.session['userPermissions']}
            ## redirect to the new HTML
            return render(request, 'data/project_detailtemp.html', context=sendProject)
    ## if its a get or we are here in error:
    else:

        project = cwprojects.projects
        getProject = project.getProject(project_id)

        getDocs = project.getProjectDocuments(project_id)
        fileUpload = forms.ProjectDetailForms
        getTeam = project.getTeamMembers(project_id)

        if request.session.get('clientid', False):

            print('CLIENT SET - RESETTING')
            request.session['clientid'] = getProject['company']['id']
            request.session['companyname'] = getProject['company']['name']

            print('ClientId:' + str(request.session['clientid']) + " ---- ClientName: "+str(request.session['companyname']))

        else:
            print('CLIENT NOT SET, SETTING')
            request.session['clientid'] = getProject['company']['id']
            request.session['companyname'] = getProject['company']['name']



        sendProject = {'Project': getProject, 'Documents': getDocs, 'Team': getTeam, 'Form': fileUpload, 'userData': request.session['contactData'],'permissions': request.session['userPermissions']}
        return render(request, 'data/project_detailtemp.html', context=sendProject)



def project(request, project_id):
    print("Working on Project:"+ str(project_id))

    if request.method == 'POST':
        print('METHOD POST')
        ## create a form instance and populate it with the data from the request:
        form = forms.ProjectDetailForms(request.POST, request.FILES, error_class=forms.DivErrorList)
        ## check if its valid data
        if form.is_valid():
            ## process the data in form.cleaned_data as required
            # ....send to cw
            project = cwprojects.projects

            file = form.cleaned_data['fileAdd']
            print(file)

            ## build out api stuff for CW
            files = {'file': (file, file.file, 'application/octet-stream')}
            params = {'recordId': project_id, 'recordType': 'Project'}

            success = "<span class='alert alert-success'><i class='icon icon-check2 icon-2x'></i> File Uploaded Successfully</span>"

            doUpload = project.uploadFile(project_id, files, params)

            ## re-render the page, hopefully with the new cw data

            getProject = project.getProject(project_id)

            getDocs = project.getProjectDocuments(project_id)
            fileUpload = forms.ProjectDetailForms(error_class=forms.DivErrorList)
            getTeam = project.getTeamMembers(project_id)
            sendProject = {'Project': getProject, 'Documents': getDocs, 'Team': getTeam, 'Form': form, 'Success': success}
            ## redirect to the new HTML
            return render(request, 'data/project_detail.html', context=sendProject)
        else:
            print(form.errors)
            print('FAILED DATACHECK')
            project = cwprojects.projects
            getProject = project.getProject(project_id)

            ##SessionOut the ClientID


            getDocs = project.getProjectDocuments(project_id)
            getTeam = project.getTeamMembers(project_id)
            sendProject = {'Project': getProject, 'Documents': getDocs, 'Team': getTeam, 'Form': form}
            ## redirect to the new HTML
            return render(request, 'data/project_detail.html', context=sendProject)
    ## if its a get or we are here in error:
    else:

        project = cwprojects.projects
        getProject = project.getProject(project_id)

        getDocs = project.getProjectDocuments(project_id)
        fileUpload = forms.ProjectDetailForms
        getTeam = project.getTeamMembers(project_id)

        if request.session.get('clientid', False):

            print('CLIENT SET - RESETTING')
            request.session['clientid'] = getProject['company']['id']
            request.session['companyname'] = getProject['company']['name']

            print('ClientId:' + str(request.session['clientid']) + " ---- ClientName: "+str(request.session['companyname']))

        else:
            print('CLIENT NOT SET, SETTING')
            request.session['clientid'] = getProject['company']['id']
            request.session['companyname'] = getProject['company']['name']



        sendProject = {'Project': getProject, 'Documents': getDocs, 'Team': getTeam, 'Form': fileUpload}
        return render(request, 'data/project_detail.html', context=sendProject)
