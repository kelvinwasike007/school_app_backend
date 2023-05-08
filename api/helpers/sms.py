import requests
def signup_msg(phone, domain, account):
    server = "https://api.africastalking.com/version1/messaging"
    payload = {
        'username':'schoolplatform',
        'to':f"{phone}",
        'message': f"""\
            Thank you for choosing School-Platform By WesEmpire\
            Your School Domain is {domain} \
            The Adminstrator Account Credentials are: \
            USERNAME:{account["username"]} \
            PASSWORD: {account["password"]} \

            PLEASE CHANGE THIS PASSWORD AFTER YOU HAVE LOGGED IN
            """,
    }
    heads={
        'apiKey': '7c857b85054b7cbb6235099c6108f6472ec7617617903126ca375e37ad4ce1e9',
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    req = requests.post(server, data=payload, headers=heads, timeout=1)
    return req.text

def bulk(phones, message):
    server = "https://api.africastalking.com/version1/messaging"
    payload = {
        'username':'schoolplatform',
        'to': ",".join(phones),
        'message': message,
    }
    heads={
        'apiKey': '7c857b85054b7cbb6235099c6108f6472ec7617617903126ca375e37ad4ce1e9',
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    req =  requests.post(server, data=payload, headers=heads, timeout=1)
    return req.text