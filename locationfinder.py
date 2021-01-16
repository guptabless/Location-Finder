import json
from urllib.request import urlopen
import argparse
import sys
import bcolors

def banner():
    print("""

            ██╗░░░░░░█████╗░░█████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗░░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
            ██║░░░░░██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║░░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
            ██║░░░░░██║░░██║██║░░╚═╝███████║░░░██║░░░██║██║░░██║██╔██╗██║█████╗█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
            ██║░░░░░██║░░██║██║░░██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║╚════╝██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
            ███████╗╚█████╔╝╚█████╔╝██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║░░░░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
            ╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝                                                                                                                             
                                                                                                                Code By: NG
              """  )
if len(sys.argv) > 1:
        banner()
        if ((sys.argv[1] != 'a')|(sys.argv[1] != 'i')):
            try:
                input_api = sys.argv[2]
                input_ip = sys.argv[4]
                parser = argparse.ArgumentParser()
                parser.add_argument("-a", required=True)
                parser.add_argument("-i", required=True)
                print(bcolors.BITALIC + "Testing for location")
                try:
                    input_url = 'https://geolocation-db.com/json/'
                    input_full_url = input_url + input_api + '/' + input_ip
                    print('Full ',input_full_url)
                    f = urlopen(input_full_url)
                    d = json.load(f)
                    print(d)
                    print(bcolors.BOLD + "Country Code:  ",d['country_code'])
                    print(bcolors.BOLD + "Country Name:  " +d['country_name'])
                    print(bcolors.BOLD + "City:  " + d['city'])
                    print(bcolors.BOLD + "Postal Code:  " + d['postal'])
                    print(bcolors.BOLD + "State Name:  " + d['state'])
                    print(bcolors.BOLD + "Latitude Code:  " + str(d['latitude']))
                    print(bcolors.BOLD + "Longitude Code:  " + str(d['longitude']))
                    print(bcolors.BOLD + "IP address:  " + d['IPv4'])
                except:
                    print(bcolors.ERRMSG + 'Location not possible')
            except:
              print(bcolors.OKMSG + 'Please enter python locationfinder -a < Valid api key > ')

elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: locationfinder.py [-h] -a API' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-a API,   --api API' '\n' '-l location    What location you want to search')
elif (sys.argv[1] != '-a')| (sys.argv[1] != '-i'):
    print(bcolors.OKMSG + 'Please enter -a < Valid Api key > -i <valid ip address>')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from (-a,-i) or -h, with a mentioned domain')

