import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder


run = True
while run:
    number = input("\n\nEnter the 10 digit number: \n\n")
    if len(number) != 10:
        print("Enter 10 digit number only".center(50, "-"), "\n")
        continue

    ch_number = phonenumbers.parse("+91" + number, "CH")
    region = geocoder.description_for_number(ch_number, "de")
    ro_number = phonenumbers.parse("+91" + number, "RO")
    service_provider = carrier.name_for_number(ro_number, "en")

    if not (region or service_provider):
        print("Enter the correct number".center(50, "-"), "\n")
        continue
    print(
        f"\nThe Number is {region} and the Service provider is {service_provider}")

    run = True if input("\nContinue? (Y/N)").lower() == "y" else False
