from django.db import models
from django.db.models.fields.related import ManyToManyField


app_label = "ict"

class PrintModel(models.Model):
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if self.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(self).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(self)
        return data

    class Meta:
        abstract = True

class ProjectDocumentUpload(models.Model):

    title = models.CharField(max_length=500, null=True)
    uploaded_by = models.ForeignKey('Users', related_name='uploaded_documents', on_delete=models.SET('0'))
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    associate_id = models.IntegerField()
    record_type = models.IntegerField()
    id = models.AutoField(primary_key=True)



class Users(models.Model):

    username = models.TextField()
    userid = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    password = models.TextField()

class Clients(models.Model):

    name = models.TextField()
    id = models.IntegerField(primary_key=True)
    external_id = models.IntegerField(unique=True)
    external_name = models.TextField(null=True)


class Firewall_Brand(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.TextField()


class Firewall_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    brandid = models.ForeignKey(to=Firewall_Brand, on_delete=models.SET('0'))


class Switch_Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()


class Switch_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()


class OnboardingWizard(PrintModel):

    id = models.AutoField(primary_key=True)
    date_start = models.DateField()
    saved_stage = models.IntegerField()
    complete = models.BooleanField()
    f1_client_id = models.IntegerField()
    f1_client_name = models.TextField()
    client_address = models.TextField(default='MISSING ADDR')
    client_phone = models.TextField(default='MISSING PHONE')

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data

class ContactInformation(PrintModel):

    id = models.AutoField(primary_key=True)
    contact_id = models.IntegerField()
    contact_firstname = models.TextField()
    contact_lastname = models.TextField()
    contact_type = models.IntegerField() ## 1 = PC, 2 = ITSupport, 3 = applications, 4 = vendors, 5 = accounts payable, 6 = emergency access, 7 = compliance
    onboarding_id = models.ForeignKey(OnboardingWizard, on_delete=models.SET('0'))

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data



class NetworkInformation(PrintModel):

    id = models.IntegerField(primary_key=True)
    onboarding_id = models.ForeignKey(OnboardingWizard, on_delete=models.SET('0'))
    type = models.TextField() ## 1 - Switch, 2 - WAP,3 - FW,4 - Other
    brand = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    replace = models.CharField(max_length=500)

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data

class ServerInformation(PrintModel):

    id = models.IntegerField(primary_key=True)
    onboarding_id = models.ForeignKey(OnboardingWizard, on_delete=models.SET('0'))
    type = models.CharField(max_length=500) ## Physical, Virtual
    brand = models.CharField(blank=True,max_length=500)
    model = models.CharField(blank=True,max_length=500)
    os = models.CharField(max_length=500) ## Windows 2XXX, Linux, Mac OS, Other
    is_vhost = models.BooleanField()
    vhost_os = models.CharField(blank=True,max_length=500)

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data

class WorkstationInformation(PrintModel):

    id = models.IntegerField(primary_key=True)
    onboarding_id = models.ForeignKey(OnboardingWizard, on_delete=models.SET('0'))
    type = models.CharField(max_length=500) ## Desktop / Laptop / Other
    brand = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    os = models.CharField(max_length=500) ## Windows / Linux /  Mac / Android / iOS
    count = models.IntegerField()
    replace = models.TextField(max_length=500)

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data


class PrinterInformation(PrintModel):

    id = models.IntegerField(primary_key=True)
    onboarding_id = models.ForeignKey(OnboardingWizard, on_delete=models.SET('0'))
    brand = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    shared = models.BooleanField()

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data

class ApplicationInformation(PrintModel):

    id = models.IntegerField(primary_key=True)
    onboarding_id = models.ForeignKey(OnboardingWizard, on_delete=models.SET('0'))
    name = models.CharField(max_length=500)
    version = models.CharField(blank=True,max_length=500)
    license = models.CharField(blank=True,max_length=500)
    location = models.CharField(blank=True,max_length=500)
    criticality = models.CharField(max_length=500)

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if instance.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data










