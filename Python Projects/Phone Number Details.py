import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter Phone Number with Country Code : ")
print("done number")
phone = phonenumbers.parse(number)
print("done parsing")
time = timezone.time_zone_for_number(phone)
print("done timezone")
registration = geocoder.description_for_number(phone, "en")
print("done registration")
carr = carrier.name_of_number(phone, "en")
print("done carrier")

print(phone)
print(time)
print(registration)
print(carr)