import requests
# 1. http-запрос без параметра method
response = requests.get(" https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
print(response.status_code)

# 2.Делает http-запрос HEAD
response=requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
print(response.status_code)

# 3. Делает запрос с правильным значением method
response=requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",params={"method":"GET"})
print(response.text)
print(response.status_code)
response=requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",data={"method":"POST"})
print(response.text)
print(response.status_code)
response=requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type",data={"method":"PUT"})
print(response.text)
print(response.status_code)
response=requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type",data={"method":"DELETE"})
print(response.text)
print(response.status_code)

# 4. Все возможные сочетания с помощью циклов
request_types = ["GET", "POST", "PUT", "DELETE"]
methods = ["GET", "POST", "PUT", "DELETE"]
cnt=0
for i in range(len(request_types)):
    for j in range(len(methods)):
        payload = {"method": methods[j]}
        cnt +=1
        if request_types[i] == "GET":
            response = requests.request(request_types[i], "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                        params=payload)
        else:
            response = requests.request(request_types[i], "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                        data=payload)
        print(f"Пара {[i]} {request_types[i]} + {[j]} {methods[j]}")
        print(response.text)
print(f"Всего возможных комбинаций: {cnt}")

