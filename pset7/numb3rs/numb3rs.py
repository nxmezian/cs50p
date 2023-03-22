#takes an IP address and evaluates if it is usable
import re

def main():
    ip = input("IPv4 Address: ")
    validate(ip)
    print(validate(ip))


def validate(ip):
    ip_hashes = []

    ip_hashes = re.split(r"\.", ip)

    try:
        for i in ip_hashes:
            if int(i) >255 or int(i)<0:
                return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
