import argparse
import json

from src.core import BlackBird
from src.scheme import Site
from src.service import Webserver

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Um programa de exemplo.')
    parser.add_argument('--proxy', help='Proxy to send requests through. E.g: --proxy http://127.0.0.1:8080 ')
    parser.add_argument('--data', default='data.json', help='Location of data.json')
    parser.add_argument('-p', '--port', type=int, default=9797, help='Port for webserver')
    parser.add_argument('-o', '--output', default='results', help='Save location for user.json')
    arguments = parser.parse_args()

    # Parsing data.json to list of sites
    with open(arguments.data, 'r') as streamer:
        sites = [
            Site.parse_obj(s)
            for s in json.load(streamer)['sites']
        ]

    # Loading useragent.txt
    with open('useragents.txt', 'r') as streamer:
        agents = streamer.read().splitlines()

    blackbird = BlackBird(sites, agents, arguments.proxy, arguments.output)
    webserver = Webserver(blackbird)
    webserver.run(port=arguments.port)
