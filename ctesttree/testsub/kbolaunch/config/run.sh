#!/bin/sh
#Start docker containers
docker compose up -d
echo "Program launching..."
#Wait the system starts
sleep 30s


container_name="basic_ldes-server"

# Check if the container is running
if docker ps --format "{{.Names}}" | grep -q "$container_name"; then
    echo "Container $container_name is running."
else
    echo "Container $container_name is not running."
    echo "The implementation doesn't support the minimum SPEC, Stopping the program..."
    exit 0
fi

echo "Post kbo stream.."
#Post the stream configuration
curl -X POST 'http://localhost:8080/admin/api/v1/eventstreams' -H 'Content-Type: text/turtle' -d '@./kbo.ttl'
if [ $? != 0 ]
    then exit $?
fi

#Check if endpoints are up
url="http://localhost:8080/kbo"

content=$(curl -sSL "$url")

if [[ -n $content ]]; then
    echo "http://localhost:8080/kbo is reachable"
else
    echo "http://localhost:8080/kbo isn not reachable"
    echo "The implementation doesn't support the minimum SPEC, Stopping the program..."
    exit 0
fi

echo "Post pagination view.."
#Post the page based view configuration
curl -X POST 'http://localhost:8080/admin/api/v1/eventstreams/kbo/views' -H 'Content-Type: text/turtle' -d '@./kbo.by-page.ttl'
if [ $? != 0 ]
    then exit $?
fi

echo "Post time based view.."
#Post the time based view configuration
curl -X POST 'http://localhost:8080/admin/api/v1/eventstreams/kbo/views' -H 'Content-Type: text/turtle' -d '@./kbo.by-time.ttl'
if [ $? != 0 ]
    then exit $?
fi

echo "Post location based view.."
#Post the geo based view configuration
curl -X POST 'http://localhost:8080/admin/api/v1/eventstreams/kbo/views' -H 'Content-Type: text/turtle' -d '@./kbo.by-location.ttl'
if [ $? != 0 ]
    then exit $?
fi

echo "Post name based view.."
#Post the substring view configuration
curl -X POST 'http://localhost:8080/admin/api/v1/eventstreams/kbo/views' -H 'Content-Type: text/turtle' -d '@./kbo.by-name.ttl'
if [ $? != 0 ]
    then exit $?
fi

echo "Post dataset"
#Post dataset
for f in ../../../../sample/bel20/*; do curl -i -X POST "http://localhost:8080/kbo" -H "Content-Type: application/turtle" -d "@$f";done


#Remove previous cached output
cd /mnt/c/VSDS/pyldes_kbo/sdk/ldes-test-client
folder_path=".scrapy"  # Replace with the actual folder path

# Check if the folder exists
if [ -d "$folder_path" ]; then
    # Remove the folder and its contents recursively
    rm -r "$folder_path"
    echo "Folder .scrapy removed successfully."
else
    echo "Folder .scrapy does not exist."
fi

#Remove previous output
file="items.rdf"

if [ -f "$file" ]; then
    rm "$file"
    echo "File $file removed."
else
    echo "File $file does not exist."
fi

# generate the whole graph of the output
cd crawldf
python3 run.py

echo "Creating MUST SPEC report."
# shellcheck disable=SC2103
cd /mnt/c/VSDS/pyldes_kbo/ctesttree/testsuits/must/mustSuites
python3 mustSuits.py

echo "Creating SHOULD SPEC report."
cd /mnt/c/VSDS/pyldes_kbo/ctesttree/testsuits/should/shouldSuites
python3 shouldSuits.py

echo "Creating OPTIONAL report."
cd /mnt/c/VSDS/pyldes_kbo/ctesttree/testsuits/optional/optionalSuites
python3 optionalSuits.py


#stop docker containers
cd  /mnt/c/VSDS/pyldes_kbo/ctesttree/testsub/kbolaunch
docker compose down
echo "Test Finish."