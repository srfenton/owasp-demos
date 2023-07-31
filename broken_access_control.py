import requests

url = 'http://localhost:3000/api/products/9'
put = requests.put(url, json = {
    "description": "O-Saft is an easy to use tool to show information about SSL certificate and tests the SSL connection according given list of ciphers and various SSL configurations. <a href=\"https://www.owasp.slack.com\" target=\"_blank\">More...</a>"
    })
print(str(put.status_code))