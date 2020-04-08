from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile, UploadedFile
from django.forms.utils import ErrorList
from . import models

class ProjectUpload(forms.Form):
    uploadModel = models.ProjectDocumentUpload
    fields = ('uploaded_by','upload_date','description','associate_id','record_type','document')


class DivErrorList(ErrorList):
     def __str__(self):
         return self.as_divs()
     def as_divs(self):
         if not self: return ''
         return '<div class="col-md-12" style="padding-bottom: 15px;"><span class="alert alert-danger"><i class="icon icon-warning"></i>  %s</span><br></div><br>' % ''.join(['<span>%s</span>' % e for e in self])

class DocumentForm(forms.ModelForm):
    class Meta:

        fields = ('description', 'document', )

        docfile = forms.FileField(
            label='Select a file',
            help_text='max. 42 megabytes'
        )

class ProjectDetailForms(forms.Form):


    fileAdd = forms.FileField(label='Add additional files...', help_text="<small class='display-block'>File Limits</small>", required=True, widget=forms.FileInput(attrs={'class': "custom-file-input"}))
    projectType = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput(), empty_value='')

class BasicTicketForms(forms.Form):

    ##Basic

    contact = forms.CharField(label="Ticket Contact", required=True)
    email = forms.EmailField(label="Contact Email", required=True)
    company = forms.CharField(label="Company Name", required=True)
    companyid = forms.CharField(required=False)
    contactid = forms.CharField(required=False)
    phone = forms.CharField(label="Contact Phone", required=True)
    companyphone = forms.CharField(label="Company Phone", required=True)
    title = forms.CharField(label="Ticket Title", required=True)
    details = forms.Textarea()
    computers = forms.Select()
    fileAdd = forms.FileField(label='Add additional files...', help_text="<small class='display-block'>File Limits</small>", required=False, widget=forms.FileInput(attrs={'class': "form-control m-input"}))

class UpdateTicket(forms.Form):


    text = forms.Textarea()
    id = forms.CharField()
    ticketid = forms.CharField()

class LoginForm(forms.Form):

    emailAddress= forms.EmailField(label="Username")
    password = forms.CharField(label="Password")

class OnboardingWizardForm(forms.ModelForm):

    ##CLIENT SPECIFIC
    clientName = forms.CharField(label='Company Name:', help_text="The current company name.")
    clientAddress = forms.CharField(label='Company Address:', help_text="Main company address.")
    clientPhone = forms.CharField(label='Phone Number:', help_text="Main company phone number.")
    clientContact = forms.CharField(label='Primary Contact:')
    ##CLIENT CONTACTS
    clientITSupport = forms.CharField(label='IT Support Contact')
    clientITPlanProj = forms.CharField(label='IT Planning and Project Contact')
    clientAccountPay = forms.CharField(label='Accounts Payable')
    clientEmergBuild = forms.CharField(label='Emergency Building Access Contact')
    clientCompliance = forms.CharField(label='Compliance Officer')
    clientVendorMgmt = forms.CharField(label='Vendor Management Contact')


    ##NETWORKING RELATED
    netIPScheme = forms.CharField(label='Local IP Scheme')
    netExtIP = forms.GenericIPAddressField(label='External IP')
    netISP = forms.ChoiceField(label='Internet Service Provider')
    netSpeed = forms.ChoiceField(label='Estimated Speed in Mbps')







    ##THINGS
    def __init__(self, *args, **kwargs):
        super().__init__(*args,*kwargs)
        #netFWBrand = models.NetworkInformation.objects.filter(
         #   fwbrand = self.instance
        #)
        #for i in range(len(netFWBrand)+1):
         #   field_brand = 'netFirewall_Brand_%s' % (i,)
          #  self.fields[field_brand] = forms.Select(label='Firewall Brand')
           # try:
            #    self.initial[field_brand] = netFWBrand[i].fwbrand
            #except:
             #   self.initial[field_brand] = ""
        #field_brand = 'netFirewall_Brand_%s' % (i+1,)
        #self.fields[field_brand] = forms.CharField(required=False)
        #self.fields[field_brand] = ""

