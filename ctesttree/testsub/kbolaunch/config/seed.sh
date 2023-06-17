#!/bin/sh
#Start docker containers
docker compose up -d

#Wwait the system starts
sleep 2m

#Post the stream/view configuration
curl -X PUT 'http://localhost:8080/admin/api/v1/eventstreams' -H 'Content-Type: text/turtle' -d '@./kbo.ttl'
if [ $? != 0 ] 
    then exit $? 
fi

#Post dataset
for f in ../../../../sample/bel20/*; do curl -i -X POST "http://localhost:8080/kbo" -H "Content-Type: application/turtle" -d "@$f";done