# LDES validation client
This simple LDES client allows validating server implementations with a SHACL file.
As an LDES stream consists of multiple pages linked to each other, SHACL validation of individual pages is insufficient to guarantee consistency.

The client follows all tree:relations from the starting url, and adds all fragments/tree:nodes to one big graph.
It does so by applying object embedding:
All triples contained in a certain graph (page) are anonymised and nested inside a page object.

## Object embedding
The object embedding algorithm assumes that the graph operated on is an [object graph](https://github.com/sandervd/ldes-transactional/blob/main/object-graph-shacl.ttl), and can be represented as a tree: only named object occur at the 'root', and blank nodes can only occur once in the object position.

Given a graph containing the following triples:
```
food:stew a schema:Recipe ;
	rdfs:label "Stoofvlees"
	schema:step [
		schema:position "1" ;
		schema:text "Vlees aanbakken" .
	] ;
	schema:step [
		schema:position "2" ;
		schema:text "Pan deglaceren met St. Bernardus 12" .
	] .
food:maccheese a schema:Recipe ;
	rdfs:label "Mac and Cheese" .
```

After object embedding this becomes:
```
[] a oe:RDFDocument;
	oe:hasObject [
		rdf:subject food:stew ;
		a schema:Recipe ;
		rdfs:label "Stoofvlees"
		schema:step [
			schema:position "1" ;
			schema:text "Vlees aanbakken" .
		] ;
		schema:step [
			schema:position "2" ;
			schema:text "Pan deglaceren met St. Bernardus 12" .
		] .
	] .
	oe:hasObject [
		rdf:subject food:maccheese ;
		a schema:Recipe ;
		rdfs:label "Mac and Cheese" .
	] .
```

# Install
- checkout repository
- cd to folder
- python3 -m venv env
- . ./env/bin/activate
- pip install pipreqs
- pip install -r requirements.txt


## Freeze dependencies
- pipreqs

# How to run  
- Set following required parameters in the `class TreeSpider` of [tree.py](./crawldf/spiders/tree.py). Please refer to the example [gipod.py](./crawldf/spiders/gipod.py).
  - name  
    - e.g. name = "gipod"  
  - allowed_domains  
    - e.g. allowed_domains = ["private-api.gipod.beta-vlaanderen.be"]  
  - start_urls  
    - e.g. start_urls = ["https://private-api.gipod.beta-vlaanderen.be/api/v1/ldes/mobility-hindrances"]  
- Under the directory `./crawldf/`, run `scrapy crawl [name]`, e.g.`scrapy crawl gipod`.  
or create a [run.py](crawldf/run.py) under the directory `./crawldf/` with follow content, please modify accordingly:

```
    from scrapy.cmdline import execute  
    execute(["scrapy","crawl","gipod"])
```
  
# Output  
- `items.rdf` file is generated under the directory `./crawldf/`
  
