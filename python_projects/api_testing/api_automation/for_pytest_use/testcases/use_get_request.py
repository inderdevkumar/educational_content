import requests

url= "https://reqres.in/api/users?page=2"

response= requests.get(url)
# TO print response
print(response)

# To display content/body of resposne

response_content= response.content
print(response_content)

# Display only header of the respinse
print(response.headers)

print(response.headers.get("Date"))

print(response.headers.get("Server"))

# Fetch cookies
print(response.cookies)

# Fetch encoding

print(response.encoding)

print(response.elapsed)

