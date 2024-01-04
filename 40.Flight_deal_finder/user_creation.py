import requests

SHEETY_API_ENDPOINT = "https://api.sheety.co/646d03120bcc87b2b47ad6e35990337c/flightDeals/users"


print("Welcome to Madhu's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email: ")
retype_email = input("Re-enter your email: ")
if email == retype_email:
    print("You're in the club!")
    data = {
        "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        }
    }
    response = requests.post(url=SHEETY_API_ENDPOINT, json=data)
    print(response.text)
else:
    print("Sorry! Email doesn't matches.")