## Start LDES server and mongo db

Please run ```docker compose up``` under the directory: ```pyldes_kbo/Cegeka -KBO-Pagination```

Two docker containers should start at this moment: Ldes server and mongo DB

## Post KBO data to the Ldes server

Please run 

```for f in ../sample/bel20/*; do curl -i -X POST "http://localhost:8080/kbo" -H "Content-Type: application/turtle" -d "@$f";done```

Also modify the directory accordingly based on your setup.\

The current test is only for pagination of the [LDES server](https://github.com/Informatievlaanderen/VSDS-LDESServer4J)
