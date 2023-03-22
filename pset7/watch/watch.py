#takes a youtube link and returns shortened link

import re

#input html link
def main():
    s = (input("HTML: "))
    parse(s)

#looks for embedded link and creates new, short link
def parse(s):
    try:
        if matches := re.search(r'(?:src="http).+\/embed\/([a-z_A-Z_0-9]+)"', s):
            link = (f"https://youtu.be/" + matches.group(1))
            return link
    except TypeError:
        print("Invalid link")


if __name__ == "__main__":
    main()