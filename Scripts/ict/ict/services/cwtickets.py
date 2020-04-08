import requests, time, json
from . import cwsettings


def getTickets(companyid, conditions=''):

    if companyid is None:
        return "Error"


    url = cwsettings.CW_TICKETS + str(conditions)
    print(url)
    r = requests.get(url, headers=cwsettings.HEADER_AUTH)
    ticketData = r.json()


    return ticketData


def getTicketData(ticketid, conditions=''):


    url = cwsettings.CW_TICKETS + str(ticketid) +""+ str(conditions)
    r = requests.get(url, headers=cwsettings.HEADER_AUTH)
    ticketData= r.json()
    
    return ticketData

def getTicketNotes(url):


    r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
    noteData = r.json()


    return noteData


def getTicketTimeEntries(url):

    r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
    timeData = r.json()

    return timeData

def createTicket(postData):



    return


def getTicketResources(url):

    r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
    data = r.json()

    return data

class ServiceTicketData:


    def indexTicketData(companyid, conditions=''):

        if companyid is None:
            return "Error"


        url = cwsettings.CW_TICKETS + str(conditions)
        print(url)
        r = requests.get(url, headers=cwsettings.HEADER_AUTH)
        ticketData = r.json()


        return ticketData















