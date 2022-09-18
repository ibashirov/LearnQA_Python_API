import requests
response=requests.get("https://playground.learnqa.ru/api/long_redirect",allow_redirects=True)
print(response.history)
first_response=response.history[0]
second_response=response.history[1]

print(first_response.url)
print(first_response.status_code)

print(second_response.url)
print(second_response.status_code)

