# with open("tinder_api/utils/token.txt", "r") as f:
#     tinder_token = f.read()

tinder_token = '742afe94-b0b0-4d56-89fe-c45ea1bf9137'
# it is best for you to write in the token to save yourself the file I/O
# especially if you have python byte code off
#tinder_token = ""

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    'content-type': 'application/json',
    'User-agent': 'Tinder/7.5.3 (iPohone; iOS 10.3.2; Scale/2.00)',
    'X-Auth-Token': tinder_token,
}

host = 'https://api.gotinder.com'

if __name__ == '__main__':
    pass
