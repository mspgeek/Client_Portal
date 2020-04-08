"""ict URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url, static
from django.contrib import admin
from django.contrib.auth import views as auth
from django.views import generic
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path

from . import views, errors, views_ticketing,views_project

app_name = "ict"
urlpatterns = [

    #Defaults
    path('', views.index, name='index'),
    path('client_view', views.client_view, name='client_view'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('403/', errors.permission_denied_view),
    path('404/', errors.error404),
    path('admin/', admin.site.urls),
    path('download/<int:file_id>', views.download, name='download'),


    #Projects
    path('project/list', views_project.project_list, name='project_list'),
    path('p/detail/', views_project.project_detail, name='project_detail'),
    path('project/<int:project_id>', views_project.project, name='project'),
    path('project/upload/<int:project_id>', views_project.project_upload, name='project_upload'),
    path('list/', views_project.project_list, name='project_list'),
    path('wizard/<int:id>', views_project.onboarding, name='onboarding'),
    path('wizard/', views_project.onboarding, name='onboarding'),
    path('onboarding/list', views_project.onboarding_list, name='onboarding_list'),


    #projectTemp
    path('projecttemp/<int:project_id>', views_project.projecttemp, name='projecttemp'),
    path('onboard/list', views_project.onboarding_temp, name='onboarding_temp'),

    #Ticketing
    path('ticketing',views_ticketing.tickets, name="tickets"),
    path('ticketing/<int:ticketid>', views_ticketing.viewticket, name="viewticket"),
    path('ticketing/new', views_ticketing.newticket, name="newticket"),
    path('ticketing/new/<int:type>', views_ticketing.newtickettype, name="newtickettype"),
    path('ticketing/createticket', views_ticketing.createTicket, name="createTicket"),
    path('ticketing/updateticket/<int:ticketid>', views_ticketing.updateTicket, name='updateTicket'),
]

handler403 = errors.permission_denied_view
handler404 = errors.error404

@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):

    def test_handler_renders_template_response(self):
        e403 = self.client.get('/403/')
        e404 = self.client.get('/404/')
        # Make assertions on the response here. For example:
        self.assertContains(e403, 'Error handler content', status_code=403)
        self.assertContains(e404, 'Error handler content', status_code=404)