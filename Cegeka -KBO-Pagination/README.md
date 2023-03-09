

#Start LDES server and mongo db

Please run docker compose up 

#Post KBO data to the Ldes server

for f in ../pyldes_kbo/sample/bel20/*; do curl -i -X POST "http://localhost:8080/kbo" -H "Content-Type: application/turtle" -d "@$f";done

Modify accordingly based your setup.

Current the test is only for pagination of the lDES server