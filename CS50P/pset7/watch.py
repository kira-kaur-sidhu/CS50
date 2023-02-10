# Watch on Youtube - implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"<iframe.*src=\"(https?://(?:www\.)?youtube.com/embed/[a-zA-Z0-9]+)\".*></iframe>$",s,):
        url = matches.group(1)
        return url.replace("ube.com/embed", "u.be").replace("www.","").replace("http:","https:")
    else:
        return None

if __name__ == "__main__":
    main()
