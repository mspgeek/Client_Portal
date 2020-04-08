from django.http import HttpResponse, FileResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import loader, RequestContext
from django.views.decorators.http import require_POST
from django.conf import settings

from django.contrib.sessions.backends.cache import SessionStore
from django.contrib.auth.decorators import login_required
from . import auth
from .decorators import user_is_auth

import json, datetime

from .services import cwprojects, cwsettings, cwcompany, cwopportunities, cwfinance
import requests, os



def permission_denied_view(request, exception=None):

    ##ERROR 403 PERMISSION DENIED
    sendData = {}
    return render(request, 'error/403.html', context=sendData)


def error404(request, exception=None):

    ##ERROR 404 PERMISSION DENIED
    sendData = {}
    return render(request, 'error/404.html', context=sendData)
