import re



ip_hashes = []

ip = input()

ip_hashes = re.split(r"\.", ip)


for i in ip_hashes:
    if int(i) >255:
        print("error")
    else:
        continue
