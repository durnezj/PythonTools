import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import time

baseUrl = "http://pastebin.com/trends"
index = 1
links = []

def append_to_file(list):
    file = open("data.txt", "a")
    for link in list:
        file.write(str(link) + "\n")


def get_page_pastes(page_url):  # gets urls from links and appends to list
    http = httplib2.Http()
    status, response = http.request(page_url)
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        string = str(link)
        parts = string.split("\"")
        try:
            if not(str(parts[1]) is "/" or\
                   str(parts[1]).startswith("/trends") or\
                   str(parts[1]).startswith("/tools") or\
                   str(parts[1]).startswith("/api") or\
                   str(parts[1]).startswith("/lang") or\
                   str(parts[1]).startswith("/u/") or\
                   str(parts[1]).startswith("/lang") or\
                   str(parts[1]).startswith("/faq") or\
                   str(parts[1]).startswith("/dmca") or\
                   str(parts[1]).startswith("/scraping") or\
                   str(parts[1]).startswith("/pro") or\
                   str(parts[1]).startswith("http") or\
                   str(parts[1]).startswith("/privacy") or\
                   str(parts[1]).startswith("cd") or\
                   str(parts[1]).startswith("/login") or\
                   str(parts[1]).startswith("/messages") or\
                   str(parts[1]).startswith("/alerts") or\
                   str(parts[1]).startswith("/settings") or\
                   str(parts[1]).startswith("/archive") or\
                   str(parts[1]).startswith("mmh") or\
                   str(parts[1]).startswith("button") or\
                   str(parts[1]).startswith("/message") or\
                   str(parts[1]).startswith("/co")):
                links.append(parts[1])
        except:
            pass
            # append_to_file(list)


def scrape_page(paste):
    http = httplib2.Http()
    status, response = http.request("http://pastebin.com/raw" + paste)
    raw_data = BeautifulSoup(response)
    wordlist = ["password", "username", "ssh", "login", "passwd", "pw", "minecraft", "email",""]
    if any(word in str(raw_data) for word in wordlist):
        print("""===================
                    FOUND MATCH
                ====================\n""" + paste)
        print(raw_data)
    else:
        print(str(paste) +" doesnt match any keywords")


def print_list():
    for i in range(links.__len__()):
        print (str(i) + "\t" + links[i])


if __name__ == '__main__':
    get_page_pastes(baseUrl)
    print_list()
    for i in range(links.__len__()):
        get_page_pastes("http://pastebin.com" + str(links[i]))


    for i in range(links.__len__()):
        print("scraping " + str(index))
        index += 1
        scrape_page(links[i])