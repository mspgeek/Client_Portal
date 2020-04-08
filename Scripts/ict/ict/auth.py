from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User, AbstractUser
import requests
from .services import cwsettings


def auth(username=None, password=None):
    if username is None or password is None:

        return "ERROR MISSING INFORMATION"

    else:

        url = cwsettings.CW_CONTACTS_AUTH
        data = {'email': username, 'password': password}
        print(url)
        print(cwsettings.HEADER_AUTH)
        print(data)
        r = requests.post(url=url, json=data, headers=cwsettings.HEADER_AUTH)
        data = r.json()
        print(data)
        print(r)
        return data

def getContactData(contactid):

    url = cwsettings.CW_CONTACTS + "/"+str(contactid)
    r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
    data = r.json()

    return data

def get_perm(user_id):

    url = cwsettings.CW_CONTACTS + "/" + str(user_id) +"/portalSecurity"

    r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
    data = r.json()

    return data

def checkSession(session):

    return



class CWAuth:

    def authenticate(self, request, username=None, password=None):

        if username is None or password is None:

            return "ERROR MISSING INFORMATION"

        else:

            url = cwsettings.CW_CONTACTS_AUTH
            data = {"email":username, "password":password}
            r = requests.post(url=url, data=data, headers=cwsettings.HEADER_AUTH)
            data = r.json()
            print(data)
            print(r)
            return data


    def get_perm(self, user_id):

        url = cwsettings.CW_CONTACTS + "/" +user_id+"/portalSecurity"

        r = requests.get(url=url, headers=cwsettings.HEADER_AUTH)
        data = r.json()

        return data

    def get_user(self, user_id):
        return