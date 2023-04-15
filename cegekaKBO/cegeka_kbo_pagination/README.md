## Start LDES server and mongo db

- Please run ```docker compose up``` under the directory: ```pyldes_kbo/Cegeka-KBO-Pagination```
- Two docker containers should start at this moment: Ldes server and mongo DB

## Post KBO data to the Ldes server

- Please run ```for f in ../sample/bel20/*; do curl -i -X POST "http://localhost:8080/kbo" -H "Content-Type: application/turtle" -d "@$f";done```
Please, also modify the directory accordingly based on your setup.
- Current test is only for Pagination [test case 1](../../Conformance%20Testing/TressSpec/TreeSpecTestPlan.md#test-case-1-) of the [LDES server](https://github.com/Informatievlaanderen/VSDS-LDESServer4J)
- ```http://localhost:8080/kbo``` root of the LDES collection
