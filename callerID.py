#!/usr/bin/python

# Phone tracker utilizing Google's libphonenumber library
# run pip install phonenumbers to download package
# import phonenumers, geocoder object#
import phonenumbers
from phonenumbers import geocoder, carrier

input_value = str(input("Enter a phone number: "))

# number object containing phone number string / must specify country code
number = phonenumbers.parse(input_value, 'US')
print(number)
print(type(number))

# example using international number
# y = phonenumbers.parse("020 8366 1177", "GB")
# print(y)

# as dialled from GB, not a GB number z = phonenumbers.parse("00 1 650 253 2222", "GB")  
#print(z)

#  check if number is valid ( assigned ) 
valid = phonenumbers.is_valid_number(number)
if valid:
    print("Phone number is valid")
    

# check if number is possible ( ex. has right number of digits )
possible = phonenumbers.is_possible_number(number)
if possible:
    print("Phone number is possible: ")

# formating the number 
# national_format = phonenumbers.format_number(number,phonenumbers.PhoneNumberFormat.NATIONAL)
# print(national_format)

# internat_format = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
#  print(internat_format)

# match valid phone numbers in a string usin PhoneNumberMatcher object
# text = ''
# for match in phonenumbers.PhoneNumberMatcher(text, 'US'):
#print(match)

# format matched numebers
# for match in phonenumbers.PhoneNumberMatcher(text, 'US'):
#    print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
 

# get Carrier data (ex. name of carrier

carrier = carrier.name_for_7number(number, 'en')
print("Service provider: " + carrier)
# Region data
Region = geocoder.description_for_number(number, 'en')
print("Region: " + Region)

