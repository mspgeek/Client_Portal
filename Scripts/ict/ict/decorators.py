from django.core.exceptions import PermissionDenied
import datetime, time

def user_is_auth(function):
    def wrap(request, *args, **kwargs):
        #if request.session['contactid'] > 0 and request.session['userLogged'] == True:
        if 'contactid' in request.session and 'userLogged' in request.session:
            curTime = time.gmtime()
            sessionTime = request.session['sessionStart']
           # time1 = datetime.datetime.strptime(request.session['sessionStart'], "%Y %m %d %H:%M:%S")
            #time2 = datetime.datetime.now()
            #time3 = (time1-time2).minutes
            #print('Time1' + time1)
            ##print('Time2 '+time2)
            #print('Time3 '+time3)
            #timeDelta =  datetime.datetime.now() - request.session['sessionStart']
            #timeDelta = datetime.timedelta(min=timeDelta)
            timeDelta = 29
            if timeDelta > 30:
                raise PermissionDenied
            else:
                return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap