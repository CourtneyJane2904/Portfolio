#!/usr/bin/python3

from sys import argv
import requests
import json
import urllib

red = '\033[91m'
reset = '\033[0m'

class OAuth():
    def __init__(self, url):
        self.url = url
        self.parsed_url = self.parse_url(url)
        # used in check_redirect_url- false if an accepted method
        self.frags = False

    def parse_url(self, url):
        oauth_dict = {}
        oauth_params = url.split('?')[-1].split('&')

        for oauth_param in oauth_params:
            o_split = oauth_param.split('=')
            oauth_dict[o_split[0]] = o_split[1]
        return oauth_dict

    def create_url(self,**kwargs):
        """
        Updates GET parameter values of URL, useful for testing for open redirect. Use: create_url(state="newvalue")
        """
        for p in kwargs.keys(): self.parsed_url[p] = kwargs[p]

        # grab URL before query string and use urllib to neatly convert dictionary back to GET parameter string. 
        url = f"{self.url.split('?')[0]}?{urllib.parse.urlencode(self.parsed_url)}"         
        self.url = url
        return url

    def check_csrf(self):
        """
        Checks if state parameter is present: a lack of indicates CSRF.
        """
        print(self.url)
        return True if 'state' in self.parsed_url.keys() else False

    def check_redirect_uri(self):
        """
        Used to see if open redirect is possible. Based on the status code of the request. Repeats checks twice if fragment is accepted to request mode as the use of this request mode can effect how this is handled.
        """

        redir_uri = urllib.parse.unquote(self.parsed_url['redirect_uri'])
        # if the redirect uri has a query string, the base of the url is before that point. Otherwise the whole url is before the last '/'
        endp = redir_uri.split("?") if redir_uri.find("?") else redir_uri.rsplit("/") 
        # use full_url if you want all directories in the redirect_uri, otherwise use bare_uri (will return just the domain)
        full_url = endp[0] ; bare_url = redir_uri.split("/") ; bare_url = f"https://{bare_url[2]}"
        print(bare_url)

        # place payloads here
        open_redirect_payloads = [
          f"{full_url}/directory",
          f"{full_url}/../directory",
          f"{full_url}@https://www.google.com",
          f"https://www.google.com#{full_url}",
          f"{full_url}#@https://www.google.com",
          f"{full_url}&@https://www.google.com#@https://www.google.com",
          f"{bare_url}.www.google.com",
          f"https://localhost/"
        ]

        # execute code block twice if frag is true (able to be used,) otherwise it will just repeat once
        cycle = 1 if self.frags else 2

        for c in range(0,cycle):
            for p in open_redirect_payloads:
                if c == 0 and cycle == 2:   self.create_url(redirect_uri = p, request_mode = "fragment")       
                else:   self.create_url(redirect_uri = p)

                redir = requests.get(self.url) 

                if redir:   print (f"redirect_uri {p}:  {red}{redir.status_code}{reset}") 
                else:   print (f"redirect_uri {p}:  {redir.status_code}")


    def check_request_method(self):
        """
        Check what request_modes (etc) are accepted
        """
        #Here need to check for optional method = fragment
        #return true if request_mode=fragment results in error 403
        openid_config = requests.get(f"{self.url.split('?')[0]}/.well-known/openid-configuration")
        config_dict = json.loads(openid_config.text)
        resp_modes = config_dict["response_modes_supported"]
        
        if "fragment" in resp_modes:    self.create_url(response_mode="fragment") 
        else: self.frags = True ; return self.frags
        # send request
        frag_req = requests.get(self.url)
        self.frags = False if frag_req else True
        return self.frags
        

def scan(url):
    """
    Returns information about oauth configuration at provided URL
    """
    oauth = OAuth(url)
    #Here need to create the scan suite
    print(f"CSRF (true = not present): {oauth.check_csrf()}")
    print(f"is fragment usable in request_mode (true = no): {oauth.check_request_method()}")
    oauth.check_redirect_uri()
   #  oauth.create_url(state="ssee") ; print (oauth.url)
    



if __name__ == "__main__":
    scan(argv[1])
