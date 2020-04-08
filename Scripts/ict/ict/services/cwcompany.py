import requests, time, json
from . import cwsettings

class companies:


    def __int__(self):

        return


    def getCompany(name=None, id=None):

        if name is None and id is None:

            return "ERROR MISSING INFORMATION"

        else:

            if id is not None:
                url = cwsettings.CW_COMPANY + "?conditions=id="+str(id)
            if name is not None:
                url = cwsettings.CW_COMPANY +"?conditions=name%20LIKE%20'"+ str(name)

            r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
            data = r.json()

            return data


    def getContacts(id=None):

        if id is None:
            return


        url = cwsettings.CW_CONTACTS +"?conditions=company/id=" + str(id)
        r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
        contacts = r.json()

        return contacts

    def getConfigs(companyid=None):

        if companyid is None:
            return

        url = cwsettings.CW_CONFIGURATION + "?conditions=company/id=" +str(companyid)
        r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
        data = r.json()

        return data


