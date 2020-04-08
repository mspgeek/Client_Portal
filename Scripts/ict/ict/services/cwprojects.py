import requests, time, json
from . import cwsettings

class projects:


    def __int__(self):

        return

    def findProject(search=None):

        if search == None:
            return "Missing Search Parameters"

        ##Search based on Name:

        ##Search based on ID:

        return

    def getProjectDocuments(id=None):

        if id is None:
            return "MISSING ID"

        docsUrl = cwsettings.CW_BASE_URL + "system/documents?recordType=Project&recordId="+str(id)+"&pageSize=1000"

        r = requests.get(url=docsUrl, headers=cwsettings.HEADER_AUTH)
        docs = r.json()

        return docs

    def downloadFile(id=None,title=None):

        if id is None:
            return "ERROR"

        downloadUrl = cwsettings.CW_BASE_URL +"system/documents/"+str(id)+"/download"
        r = requests.get(url=downloadUrl, headers=cwsettings.HEADER_AUTH)
        #return open(title, 'wb').write(r.content)
        return r.content()

    def getTeamMembers(id=None):

        if id is None:
            return "ERROR"

        teamUrl = cwsettings.CW_PROJECTS + "/" + str(id) + "/teamMembers?orderBy=projectRole/identifier"
        r = requests.get(url=teamUrl, headers=cwsettings.HEADER_AUTH)
        team = r.json()

        return team

    def uploadFile(id, file, data2):

        fileUrl = cwsettings.CW_BASE_URL + "/system/documents"
        print("DEBUG DATA ---- URL:"+fileUrl+" --- Header:"+str(cwsettings.UPLOAD_AUTH))
        print(file)
        r = requests.post(url=fileUrl, data=data2, files=file, headers=cwsettings.UPLOAD_AUTH)

        print(r.content)
        print(r.status_code)


        return


    def getProject(id=None):

        if id == None:
            return "ERROR Missing ID:"

        projectUrl = cwsettings.CW_PROJECTS + "/"+str(id)
        r = requests.get(url=projectUrl, headers=cwsettings.HEADER_AUTH)
        project = r.json()
        return project



    def updateProject(id=None, data=None):

        return

    def closeProject(id=None):

        return

    def listProjects(type=None):

        if type == None:
            projectUrl = cwsettings.CW_PROJECTS +"?conditions=status/id!=2%20AND%20status/id!=18"
            r = requests.get(url=projectUrl, headers=cwsettings.HEADER_AUTH)
            projects = r.json()

            return projects
        elif type == 'all':

            return

    def listProjectstemp(type=None):

        if type == None:
            projectUrl = cwsettings.CW_PROJECTS +"?conditions=status/id!=2%20AND%20status/id!=18%20AND%20name%20CONTAINS%20'onboarding'"
            r = requests.get(url=projectUrl, headers=cwsettings.HEADER_AUTH)
            projects = r.json()

            return projects
        elif type == 'all':

            return