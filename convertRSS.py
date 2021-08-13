import requests
import os, sys
import argparse

# the main get content codes
def get_url(url):
    # some server requests need headers, otherwise return empty
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }
    page = requests.get(url, headers = headers).content
    # convert to str within utf-8 encoding
    page = page.decode('utf-8')
    return page

# the main convert codes
def convert_content(content):
    content = content.replace("ZNing源创库","张宁网·源创库")
    return content

if __name__ == '__main__':
    # need system args input
    arg_prsr = argparse.ArgumentParser()
    arg_prsr.add_argument('--url', required=True, type=str, default="", help = 'Required. Which one RSS Xml do you want to convert.')
    args = arg_prsr.parse_args(sys.argv[1:])
    url = args.url

    # place a flag to judge should write file to disk or not
    flag = False

    url_content = convert_content(get_url(url))
    url_list = url.split("/")

    if os.path.exists(url_list[-1]):
        with open(url_list[-1], 'r', encoding='utf-8') as file:
            if(file.read()!=url_content):
                flag = True
    else:
        # if the file dose not exist, the flag should placed True to convert first time
        flag = True

    if flag:
        # writing to disk codes
        with open(url_list[-1], 'w', encoding='utf-8') as file:
            file.write(url_content)
        print("The RSS Xml had update, convert done.")
        sys.exit(0)
    else:
        print("The RSS Xml have no change, convert abort.")
        sys.exit(1)
