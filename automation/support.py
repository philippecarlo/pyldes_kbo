#!/usr/bin/python
import subprocess
import requests
import unittest
from rdflib import Graph
import glob,os
payload = {}
files = {}
headersPost = {
  'Content-Type': 'application/turtle'
}
url = "http://localhost:8080/kbo"

class Support():
    def startService(self):
        with open("server.log", "a") as output:
            return subprocess.run("docker compose up -d", shell=True, stdout=output, stderr=output)
    def serverReady(self):
         return requests.request("GET", url, headers={}, data=payload, files=files).status_code

    def postData(self):
        for file in glob.glob("../sample/bel20/*"):
            requests.request("POST", url, headers=headersPost, data=file)
    def stopServer(self):
        with open("server.log", "a") as output:
            subprocess.run("docker compose down", shell=True, stdout=output, stderr=output)