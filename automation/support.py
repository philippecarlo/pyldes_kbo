#!/usr/bin/python
import glob
import subprocess

import rdflib
import requests

url = "http://localhost:8080/kbo"
# docker_compose_file = "../cegekaKBO/cegeka_kbo_pagination/docker-compose.yml"

payload = {}
files = {}
headers_post = {
    'Content-Type': 'application/turtle'
}

headers_get_json = {
    'accept': 'application/ld+json'
}


class Support:
    def start_service(self, path_docker):
        with open("server.log", "a") as output:
            return subprocess.run(f"docker compose --env-file user.env  -f {path_docker} up -d", shell=True,
                                  stdout=output, stderr=output)

    def server_ready(self):
        return requests.request("GET", url, headers={}, data=payload, files=files)

    def post_data(self, location) -> None:
        for file in glob.glob(location):
            # reparse turtle file to make sure jena doesn't crash with dot.
            with open(file, 'r') as f:
                data = f.read()
                g = rdflib.Graph()
                g.parse(data=data, format='turtle')
            print(file)
            print(requests.request("POST", url, headers=headers_post, data=g.serialize(format='turtle')).status_code)

    def stop_server(self, path_docker) -> None:
        with open("server.log", "a") as output:
            subprocess.run(f"docker compose -f {path_docker} down", shell=True, stdout=output, stderr=output)

    def retrieve_specific_page(self, url_view):
        return requests.request("GET", url_view, headers=headers_get_json)

# if __name__ == '__main__':
#          Support().start_service()
