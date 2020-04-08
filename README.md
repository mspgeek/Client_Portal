# Client_Portal
Python Client Portal for ConnectWise Manage



## How to get this to work...maybe

The only important  folder should be the  "ict" folder inside  /Scripts/

You need Python installed and pip installed (can be installed from the python.org installer)

important commands (CMD as Administrator)

pip install django

pip install requests

pip install requests_toolbelt

pip install django-phone-filter

thats SHOULD be it, but if the  commands below error out ping me with the message so I can  see if its something missing

Navigate to your ict folder, then run  python manage.py runserver  This should begin a server on localhost:8000 .  Once that is done and running you can edit the  CWSETTINGS file with  your APIKEY (already encoded) and you clientid  (obtainable from the developer.connectwise.com website)

Once you've added those, you can rerun  the server and then test login.


#HOWTOAPIKEY
Create the api key inside of manage, and the proper method of encoding is companyid+pubkey:privkey  Once you have that fully correct then you can go to base64encode.com  to encode it should spit something out like Gjh32048ghqw3gJHQ3g9h354yg==

Edit the CW_API_KEY to "Basic (apikeyhere)" and then add the clientID from the dev portal and it should function.  
