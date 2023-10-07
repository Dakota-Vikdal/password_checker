import requests
import hashlib

# request the status code of a hashed password.
def request_api_data(hash_char):
    url = 'https://api.pwnedpasswords.com/range/' + hash_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}, try again bucko!')
    return res


# Generate a SHA-1 hash from the provided password for security checks.   
def pwned_api_check(password):
    print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())


print(request_api_data('C8AFC'))
pwned_api_check('123')