import requests
import hashlib
import sys


def request_api_data(query_char):
    """
    Fetches matching Hash (first 5 chars) from the pwnedpasswords website.
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the url and try again!")
    return res

def get_password_leaks(response_hashes, tail):
    """
    Parses the response and returns the count
    """
    hashes = (line.split(':') for line in response_hashes.text.splitlines())
    for hash, count in hashes:
        # print(hash, count)
        if hash == tail:
            return count
    return 0

def pwned_api_check(password):
    """
    Checks if the password was ever hacked and returns the number of times it was
    """
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(sha1password)
    return get_password_leaks(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"'{password}' was hacked {count} times. You should choose a different password")
        else:
            print(f"'{password}' was NEVER hacked. You can use this password")
    return 'Done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))