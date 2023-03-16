
# Conformance Testing framework 
*The current framework is made for conforming the test points regarding the [Tree Spec](https://treecg.github.io/specification/)*

Which contains:
 - [🟥 Must](#the-tree-specification-must-) 
 - [🟨 Should](#the-tree-specification-should-)
 - [🟩 Optional](#the-tree-specification-optional-)

The conformance test needs to be executed on the all supporting fragment method:

 - [ ] Geo-based fragment 
 - [ ] Substring fragment 
 - [ ] Time-based fragment
 - [ ] Pagination fragment
 

# [The Tree Specification](https://treecg.github.io/specification/#introduction) [Must🟥]

> When the MUST situation applied, the system MUST follow the recommendations. Otherwise, the system fails the SPEC.
> 
## [Collections](https://treecg.github.io/specification/#introduction)
## [Core Concept](https://treecg.github.io/specification/#core-concepts)
#### *When the current page is a tree:Node, there MUST be a property linking the current page URL to the URI of the tree:Collection.*		    

 - [ ] Check after the processing by LDES Server, each tree:Node has a link between current page to tree:Collection

####  *Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.*	

 - [ ] Verify LDES Client retrieves the full collection from the link of  tree:view
 - [ ] Check the integrity of the retrieved dataset

####	*A TREE client MUST traverse all relations from the tree:Nodes linked to this particular collection. A client MUST thus check for ViewDescriptions on both the current node without the tree:viewDescription qualification, as on the current node with the tree:viewDescription link.*

 - [ ] Check the reaction of the LDES Client when the relation is more than one. [LDES Client Must Not crash]	
 - [ ] Verify LDES client retrieves all dataset if there is tree:viewDescription
 - [ ] Verify client retrieves all dataset if there is NO tree:viewDescription

## [Relations](https://treecg.github.io/specification/#relations)
####	*A tree:Relation MUST have one tree:node object of the type tree:Node.*
- [ ] Check if all tree:Relation  has one tree:node 
####	*The result of the evaluation of the tree:path, is the value that MUST be compared to the tree:value.*
- [ ] Check if the evaluation based on the tree:path is as expected.
####	*When no tree:path is defined, the tree:value MUST be compared to all members’ triples that can be compared to the tree:value as defined by the type of the relation (or when no members or collection are defined, on every triple in the page). When due to rdfs:range incompatibility, the object cannot be compared, the object will not be considered for comparison.*
- [ ] Check if the tree:path is not defined, the LDES Server could fragment the collection in an expected way.
- [ ] Check if the tree:path is not defined, the LDES Client could retrieve the collection in an expected way.

####	*When the only type given for a certain Relation is tree:Relation, then the client must dereference all of the nodes.*
####	*The strings MUST then be compared according to case sensitive unicode ordering.*
####	*When using tree:GeospatiallyContainsRelation, the tree:path MUST refer to a literal containing a WKT string, such as geosparql:asWKT.*

## [Searching through the collection](https://treecg.github.io/specification/#searching)
## [Imports](https://treecg.github.io/specification/#imports)

####    *When defined as part of the `tree:Relation`, one MUST fetch the import when the relation needs to be correctly evaluated (e.g., the resulting page contains elements without materialized WKT strings, which however can be fetched from the import).*

####     *No hypermedia controls in the body MUST be interpreted in the imported resource and the object must be fully contained within that information resource.*

❓ https://treecg.github.io/specification/#ldp

# [The Tree Specification](https://treecg.github.io/specification/#introduction) [Should 🟨]

> When the SHOULD situation applied, the system follow the recommendation. Otherwise, the choice needs to be re-evaluated.

##	[Collections](https://treecg.github.io/specification/#introduction)
##	[Core Concept](https://treecg.github.io/specification/#core-concepts)
#### *Therefore a data publisher SHOULD annotate a tree:Collection instance with a SHACL shape. The tree:shape points to a SHACL description of the shape (sh:NodeShape).*
#### *Note: the shape can be a blank node, or a named node on which you should follow your nose when it is defined at a different HTTP URL.*
#### *A client picks the right view that is use-case specific and can be prioritized by studying the tree:ViewDescription’s properties. To fetch all members, one can be chosen at random if no specific tree:ViewDescription is given.*
##	[Relations](https://treecg.github.io/specification/#relations)
#### *The tree:Relation’s tree:value SHOULD be set.*
#### *The object of tree:value SHOULD be accompanied by a data type when it is a literal value.*
#### *Every tree:Relation SHOULD have a tree:path, indicating the path from the member to the object on which the tree:Relation applies.*
#### *When traversing, a client SHOULD keep a list of already visited pages, as despite this being the TREE spec, circular references and back-links are not explicitly prohibited*
#### *When using relations such as tree:LessThanRelation or tree:GreaterThanRelation, the time literals need to be compared according to these 3 possible data types: xsd:date, xsd:dateTime or xsd:dateTimeStamp.*

 - [ ] LDES Client persistency
## [Searching through the collection](https://treecg.github.io/specification/#searching)
## [Imports](https://treecg.github.io/specification/#imports)
#### *A `tree:importStream` can also be defined for providing a pubsub interface for subscribing to real-time updates. The object SHOULD be a [[websockets]](https://treecg.github.io/specification/#biblio-websockets) or Server-Sent Events ([[eventsource]](https://treecg.github.io/specification/#biblio-eventsource)).*

## [Imports](https://treecg.github.io/specification/#imports)
####	*[[VOCAB-DCAT-2]](https://treecg.github.io/specification/#biblio-vocab-dcat-2) is the standard for Open Data Portals by W3C. In order to find TREE compliant datasets in data portals, there SHOULD be a `dcat:accessURL` from the `dcat:Distribution` to the entrypoint where the `tree:Collection`s are described. Furthermore, there SHOULD be a `dct:conformsTo` this URI: `https://w3id.org/tree`.*

####	*Therefore, when using AS (Activity Streams 2.0) collections, a client implementation should gather the members from the `tree:Node` or `as:CollectionPage` instead.*

# [The Tree Specification](https://treecg.github.io/specification/#introduction) [Optional 🟩]


> When the MAY situation applied, the system MUST NOT crash!
##	[Collections](https://treecg.github.io/specification/#introduction)
##	[Core Concept](https://treecg.github.io/specification/#core-concepts)
#### *Three properties may thus be used:*
	1.  `ex:C1 tree:view <> .`  
	    May be used  _only_  in the case when the entire  `tree:Collection`  can be found starting from the current node.	    
	2.  `ex:C1 void:subset <> .`  
	    When the node is not a node from which all members can be found, but still a subset of the collection can be found.	    
	3.  `<> dcterms:isPartOf ex:C1 .`  
####	*Multiple tree:view links MAY be provided*
####	*Note: the shape can be a blank node, or a named node on which you should follow your nose when it is defined at a different HTTP URL.*
####	*Note: For compatibility with the Solid specifications, a ShEx shape may also be given (see the chapter on compatibility bellow).*
####	*The class `tree:ViewDescription` indicates a specific TREE structure on a `tree:Collection`.*

##	[Relations](https://treecg.github.io/specification/#relations)

####  *A tree:Node element MAY have one or more tree:relation properties.*
####	*A relation is an entity of the type tree:Relation, and MAY have a more specific type.*
####	*All possible combinations of e.g., `shacl:alternativePath`, `shacl:inversePath` or `shacl:inLanguage` in the SHACL spec can be used.*
####	*Every tree:Relation MAY provide a tree:remainingItems.*
####	*A client MAY use tree:remainingItems to estimate the completeness of the downloaded elements to the end-user.*
####	*A tree:import MAY be defined in the tree:Relation instance.*
####	*When there are no `tree:member`s and/or no `tree:Collection` defined, then the `tree:path` refers to a pattern that can start from every triple in the page.*
####	*When a `tree:path` is defined, mind that you also may have to check the language of the element using the property `shacl:inLanguage` More languages MAY be set. When no language is set, all strings are compared.*
####	*A `tree:path` MAY refer to an implicit property*
####	*When a `tree:path` is defined, mind that you also may have to check the language of the element using the property `shacl:inLanguage` More languages MAY be set. When no language is set, all strings are compared.*


## [Searching through the collection](https://treecg.github.io/specification/#searching)
## [Imports](https://treecg.github.io/specification/#imports)
####	*On the resources to import, Memento [[RFC7089]](https://treecg.github.io/specification/#biblio-rfc7089) controls MAY be provided for historic versions.*

 ####	*A client MAY infer a tree:shape of the collection through the st:validatedBy property of the Shapes Tree.*
