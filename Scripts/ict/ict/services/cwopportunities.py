import requests, json, time
from . import cwsettings



class opportunities:


    default = 1


    ##DEFINE GETS

    def getOp(id):

        if id is '':

            return "ERROR MISSING ID"

    def getOpenOps(companyId):

        Url = cwsettings.CW_OPPORTUNITY + "?conditions=closedDate=null"

        r = requests.get(url=Url, headers=cwsettings.HEADER_AUTH)
        ops = r.json()

        return ops


    def findOp(searchText='', clientid='',):

        return

    def getOpProducts(opid):

        return

    def getOpActivities(opid):

        return


    ##DEFINE UPDATES

    def updateOp(opid):

        return

    def updateOpProducts(opid):

        return

    ##DEFINE CREATES

    def createOp():

        return

    ##DEFINE DELETES




    #########
    ##This is the view builder.  We build out the data going into the views all the legwork ect.
    ########

    def buildIndex():

        return