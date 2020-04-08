from django import template

import phonenumbers


register = template.Library()


@register.filter(name='phonenumber')
def phonenumber(
        value, country='US', format=phonenumbers.PhoneNumberFormat.NATIONAL):
    try:
        parsed = phonenumbers.parse(value, country)
        return phonenumbers.format_number(parsed, format)
    except phonenumbers.NumberParseException as e:
        return value
        

@register.filter(name='phonenumber_intl')
def phonenumber_international(value, country='US'):
    return phonenumber(
        value, country, phonenumbers.PhoneNumberFormat.INTERNATIONAL)


@register.filter(name='phonenumber_e164')
def phonenumber_e164(value, country='US'):
    return phonenumber(
        value, country, phonenumbers.PhoneNumberFormat.E164)
