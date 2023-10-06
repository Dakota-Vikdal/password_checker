import requests

url = 'https://api.pwnedpasswords.com/range/' + 'C8AFC'
res = requests.get(url)

print(res)
print(url)