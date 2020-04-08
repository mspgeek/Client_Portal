##Here we process all the datas, all of them...

import requests, time, json

from .services import cwopportunities, cwfinance, cwsettings, cwcompany, cwprojects

from .models import OnboardingWizard, Firewall_Brand, Firewall_Model, NetworkInformation, ServerInformation, Clients, ApplicationInformation, PrinterInformation, ContactInformation



def savePage(type,data,updated='',id=''):

    check = False
    print(type)

    saveData = data
    ## 1 = PC, 2 = ITSupport, 3 = applications/planning, 4 = vendors, 5 = accounts payable, 6 = emergency access, 7 = compliance
    ##ClientType
    if data['type'] == '0':
        print('Inside Type 0')
        ##Check to see if we find the onboarding ID already
        onBoardingObj = OnboardingWizard.objects.get(id=id)

        if onBoardingObj.saved_stage >= 1:
            checkSaved = True

        else:
            checkSaved = False


        ##Non-Contact Info:
        phoneNumber = data['phoneNumber']
        address = data['address']

        onBoardingObj.client_phone = data['phoneNumber']
        onBoardingObj.address = data['address']
        onBoardingObj.save()



        ##Specify
        nameList = {'contactid':data['primaryContact'],'name':data['pcName'], 'ctype':1},{'contactid':data['itSupport'],'name':data['itsName'], 'ctype':2}, {'contactid':data['itPlan'], 'name':data['itpName'],'ctype':3},{'contactid':data['accountsPayable'],'name':data['apName'], 'ctype':5},{'contactid':data['buildingAccess'],'name':data['baName'], 'ctype':6}, {'contactid':data['complianceOfficer'],'name':data['coName'],'ctype':7}, {'contactid':data['vendorManagement'],'name':data['vmName'], 'ctype':4}
        #print(nameList)


        for item in nameList: ##FORLOOP, COMBINE
            print(item)

            try:
                name = item['name'].split(' ')
                print(name)
                fname = name[0]
                lname = name[1]

                if checkSaved is True:
                    contact = ContactInformation.objects.get(onboarding_id_id=id, contact_type=item['ctype'])
                    contact.contact_firstname = fname
                    contact.contact_lastname = lname
                    contact.contact_id = str(item['contactid'])
                    contact.contact_type = item['ctype']
                    contact.save()
                    print('Updated Contact')
                else:
                    contact = ContactInformation()
                    contact.contact_firstname = fname
                    contact.contact_lastname = lname
                    contact.contact_id = str(item['name'])
                    contact.contact_type = item['ctype']
                    contact.onboarding_id_id = str(id)

                    print('ID' + str(id) + ' - ContactFNAME: ' + fname + ' - ContactLNAME: ' + lname + ' - contactID: ' + str(item['name']) + '- ITEM TYPE: ' + str(item['ctype']))

                    contact.save()

            except Exception as e:
                print(e)
        if onBoardingObj.saved_stage <= 0:
            onBoardingObj.saved_stage = 1
            onBoardingObj.save()

        check = True


        return check




    elif data['type'] == '1':
        a = 2
        print("Type:" + data['type'])

        #print(data['fwlist'])
        ##Lets try to process the networking data.
        onBoardingObj = OnboardingWizard.objects.get(id=id)
        print(onBoardingObj)
        if onBoardingObj.saved_stage >= 2:
            checkSaved = True
        else:
            checkSaved = False
        stringFw = data['fwList']
        stringSw = data['swList']
        stringAp = data['apList']

        if len(stringFw) > 0:

            splitFw = stringFw.split(';')


            fwlist = []

            for item in splitFw:
                if len(item) == 0:
                   continue
                tempDict = dict(x.split('=') for x in item.split(','))
                fwlist.append(tempDict)



            for fw in fwlist:
                try:
                    network = NetworkInformation()
                    network.onboarding_id = onBoardingObj
                    network.brand = fw['fwbrand']
                    network.model = fw['fwmodel']
                    network.type = "1"
                    network.replace = fw['replace']
                    network.save()
                    print("Network Item:" + fw['fwbrand'] + " Saved.")
                except Exception as e:
                    print(e)

        if len(stringSw) > 0:

            splitSw = stringSw.split(';')


            swlist = []

            for item in splitSw:
                if len(item) == 0:
                   continue
                tempDict = dict(x.split('=') for x in item.split(','))
                swlist.append(tempDict)


            for sw in swlist:
                try:
                    network = NetworkInformation()
                    network.onboarding_id = onBoardingObj
                    network.brand = sw['swbrand']
                    network.model = sw['swmodel']
                    network.type = "2"
                    network.replace = sw['replace']
                    network.save()
                    print("Network Item:" + sw['swbrand'] + " Saved.")
                except Exception as e:
                    print(e)

        if len(stringAp) > 0:

            splitAp = stringAp.split(';')


            aplist = []

            for item in splitAp:
                if len(item) == 0:
                   continue
                tempDict = dict(x.split('=') for x in item.split(','))
                aplist.append(tempDict)


            for ap in aplist:
                try:
                    network = NetworkInformation()
                    network.onboarding_id = onBoardingObj
                    network.brand = ap['apbrand']
                    network.model = ap['apmodel']
                    network.type = "3"
                    network.replace = ap['replace']
                    network.save()
                    print("Network Item:" + ap['swbrand'] + " Saved.")
                except Exception as e:
                    print(e)





        ##process data
    elif data['type'] == '2':
        a = 3
        ##process data
    elif data['type'] == '3':
        a = 4
        ##process data
    elif data['type'] == '4':
        a = 5
        ##process data
    elif data['type'] == '5':
        a = 6
        ##process data
    else:
        ##GETDATA cuz thats all thats left
        a = 7

    return check