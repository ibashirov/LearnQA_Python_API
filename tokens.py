import requests
import time

response_status = "Job is NOT ready"
response_result = "Job is ready"
response_error = "No job linked to this token"
wrong_token = "abc123"

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

resp_token = response.json()['token']
resp_time = response.json()['seconds']

print(response.text)

response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={
    'token': 'resp_token'})
print(response_with_token.text)

time.sleep(resp_time)

data = {
    'token': resp_token
}

response2 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
    params=data
)
if response2.json()['status'] == response_status:
    print(f"PASSED! Server answer when job is not ready: {response2.json()['status']}")
else:
    print(f"FAILED! Wrong server answer when job is not ready: {response2.json()['status']}")
print(f"Response text: {response2.text}")

print(" ")
time.sleep(resp_time)
response3 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
    params=data
)

if response3.json()['status'] == response_result:
    print(f"PASSED! Correct server answer when job is ready: {response3.json()['status']}. Job time: {resp_time}")
else:
    print(f"FAILED! Wrong server answer: {response3.json()['status']}. Job time: {resp_time}")
print(f"Response text: {response3.text}")

print(" ")

response4 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
    params={'token': wrong_token}
)

if response4.json()['error'] == response_error:
    print(f"PASSED! Correct server answer: {response4.json()['error']}")

else:
    print(f"FAILED! Wrong server answer: {response4.json()['error']}")
    print(f"Response text: {response4.text}")