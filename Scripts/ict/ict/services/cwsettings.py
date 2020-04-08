import requests, json



###
# File : cwsettings
##
# Desc : This holds the settings to interact with ConnectWise and other Defaults
###
# Date : 7/30/18
###


##REST API
CW_API_KEY = ""
CW_CLIENTID = ""
HEADER_AUTH = {"Authorization":CW_API_KEY, "Content-type":"application/json", "clientId":CW_CLIENTID}
UPLOAD_AUTH = {"Authorization":CW_API_KEY, "clientId": CW_CLIENTID}

##URLS
##CW_BASE_URL = "https://manage.intellicomp.net/v4_6_release/apis/3.0/"
CW_BASE_URL = "https://staging.connectwisedev.com/v2020_2/apis/3.0/"

##Service/Tickets
CW_TICKETS = CW_BASE_URL + "service/tickets/"
CW_SURVEY = CW_BASE_URL + "service/survey/"
CW_BOARDS = CW_BASE_URL + "service/boards/"


##PROJECT
CW_PROJECTS = CW_BASE_URL + "project/projects"
CW_PROJECT_STATUS = CW_BASE_URL + "project/statuses"


##COMPANIES
CW_COMPANY = CW_BASE_URL + "company/companies"
CW_CONFIGURATION = CW_BASE_URL + "company/configurations"
CW_CONTACTS = CW_BASE_URL + "company/contacts"
CW_CONTACTS_AUTH = CW_BASE_URL + "company/contacts/validatePortalCredentials"


##OPPORTUNITIES/SALES
CW_OPPORTUNITY = CW_BASE_URL + "sales/opportunities"
CW_ACTIVITIY = CW_BASE_URL + "sales/activities"


