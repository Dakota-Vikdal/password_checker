import requests
import hashlib
import sys

# Request the status code of a hashed password.
def request_api_data(hash_char):
    url = 'https://api.pwnedpasswords.com/range/' + hash_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code}, try again bucko!')
    return res

# Check to see how many times a password has been leaked.
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

# Generate a SHA-1 hash from the provided password for security checks.   
def pwned_api_check(password):
    hashed_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = hashed_pass[:5], hashed_pass[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

# Print how many times a password has been leaked, if any.
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. You should consider changing your password.')
        else:
            print('Your password is really great! It wasn\'t found a single time. Nice choice!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))