#!/usr/bin/python
import subprocess
from subprocess import CompletedProcess
import glob
import requests
from rdflib import Graph, Literal, URIRef
import rdflib
url = "http://localhost:8080/kbo"

payload = {}
files = {}
headers_post = {
    'Content-Type': 'application/turtle'
}


headers_get_json = {
  'accept': 'application/ld+json'
}

class Support():
    def start_service(self) -> CompletedProcess:
        with open("server.log", "a") as output:
            return subprocess.run("docker compose --env-file user.env up -d", shell=True, stdout=output, stderr=output)

    def server_ready(self)-> CompletedProcess:
        return requests.request("GET", url, headers={}, data=payload, files=files)

    def post_data(self,location= "../sample/bel20/*") -> None:
        print("I am here")
        for file in glob.glob(location):
            #reparse turtle file to make sure jena doesn't crash with dot.
            with open(file, 'r') as f:
                data = f.read()
                g = rdflib.Graph()
                g.parse(data=data, format='turtle')
            print(requests.request("POST", url, headers=headers_post, data=g.serialize(format='turtle')).status_code)
    def stop_server(self) -> None:
        with open("server.log", "a") as output:
            subprocess.run("docker compose down", shell=True, stdout=output, stderr=output)

    def retrieve_specific_page(self, url_view) -> CompletedProcess:
        return requests.request("GET", url_view, headers=headers_get_json)

if __name__ == '__main__':
         Support().post_data()