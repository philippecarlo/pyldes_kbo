


# Conformance Testing framework 
*The current framework is made for conforming the test points regarding the [Tree Spec](https://treecg.github.io/specification/)*
Which contains:
 - [🟥 Must](#the-tree-specification-must-) 
 - [🟨 Should](#the-tree-specification-should-)
 - [🟦 Optional](#the-tree-specification-optional-)

# [1. The Tree Specification](https://treecg.github.io/specification/#introduction) [Must🟥]

> When the MUST situation is applied, the system MUST follow the recommendations. Otherwise, the system fails the SPEC.
> 
## [1.1 Collections](https://treecg.github.io/specification/#introduction)
## [1.2 Core Concept](https://treecg.github.io/specification/#core-concepts)
#### *1.2.1 When the current page is a tree:Node, there MUST be a property linking the current page URL to the URI of the tree:Collection.*		    

 - [ ] Check after the processing by LDES Server, each tree:Node has a link between current page to tree:Collection

####  *1.2.2 Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.*	

 - [ ] Verify LDES Client retrieves the full collection from the link of  tree:view
 - [ ] Check the integrity of the retrieved dataset

####	*1.2.3 A TREE client MUST traverse all relations from the tree:Nodes linked to this particular collection. A client MUST thus check for ViewDescriptions on both the current node without the tree:viewDescription qualification, as on the current node with the tree:viewDescription link.*

 - [ ] Check the reaction of the LDES Client when the relation is more than one. [LDES Client Must Not crash]	
 - [ ] Verify LDES client retrieves all datasets if there is tree:viewDescription
 - [ ] Verify client retrieves all datasets if there is NO tree:viewDescription

## [1.3 Relations](https://treecg.github.io/specification/#relations)
####	*1.3.1 A tree:Relation MUST have one tree:node object of the type tree:Node.*
- [ ] Check if all tree:Relation  has one tree:node 
####	*1.3.2 The result of the evaluation of the tree:path, is the value that MUST be compared to the tree:value.*
- [ ] Check if the evaluation based on the tree:path is as expected.
####	*1.3.3 When no tree:path is defined, the tree:value MUST be compared to all members’ triples that can be compared to the tree:value as defined by the type of the relation (or when no members or collection are defined, on every triple in the page). When due to rdfs:range incompatibility, the object cannot be compared, the object will not be considered for comparison.*
- [ ] Check if the tree:path is not defined, the LDES Server could fragment the collection in an expected way.
- [ ] Check if the tree:path is not defined, and also some rdfs:range incompatibility, the LDES Server could fragment the collection in an expected way.

####	*1.3.4 When the only type given for a certain Relation is tree:Relation, then the client must dereference all of the nodes.*
####	*1.3.5 The strings MUST then be compared according to case sensitive unicode ordering.*
- [ ] Check when the fragment is set for a substring, LDES server fragment the collection is according to the case sensitive unicode ordering.
####	*1.3.6 When using tree:GeospatiallyContainsRelation, the tree:path MUST refer to a literal containing a WKT string, such as geosparql:asWKT.*

## [1.4 Searching through the collection](https://treecg.github.io/specification/#searching)
## [1.5 Imports](https://treecg.github.io/specification/#imports)

####    *1.5.1 When defined as part of the `tree:Relation`, one MUST fetch the import when the relation needs to be correctly evaluated (e.g., the resulting page contains elements without materialized WKT strings, which however can be fetched from the import).*
####    *1.5.2 No hypermedia controls in the body MUST be interpreted in the imported resource and the object must be fully contained within that information resource.*
####    *1.5.3 LDP Containers: If this container is paged by the [[!ldp-paging]] (chapter 7) spec, then this MUST be ignored.*
####    *1.5.4 LDP Containers: If there is an ordering, this MUST be ignored by TREE clients (the relations contain all necessary information for pruning).*

# [2 The Tree Specification](https://treecg.github.io/specification/#introduction) [Should 🟨]

> When the SHOULD situation is applied, the system follows the recommendation. Otherwise, the choice needs to be re-evaluated.

##	[2.1 Collections](https://treecg.github.io/specification/#introduction)
##	[2.2 Core Concept](https://treecg.github.io/specification/#core-concepts)
#### *2.2.1 Therefore a data publisher SHOULD annotate a tree:Collection instance with a SHACL shape. The tree:shape points to a SHACL description of the shape (sh:NodeShape).*
- [ ] Check when LDES stream is set with a SHACL shape, LDES server fragment works as expected
#### *2.2.2 Note: the shape can be a blank node, or a named node on which you should follow your nose when it is defined at a different HTTP URL.*
- [ ] Check when LDES stream is set with a blank node, LDES server fragment works as expected
#### *2.2.3 A client picks the right view that is use-case specific and can be prioritized by studying the tree:ViewDescription’s properties. To fetch all members, one can be chosen at random if no specific tree:ViewDescription is given.*
- [ ] Check when there are several views and no tree:ViewDescription, LDES client works as expected
- [ ] Check when there are several views and tree:ViewDescription, LDES client works as expected

##	[2.3 Relations](https://treecg.github.io/specification/#relations)
#### *2.3.1 The tree:Relation’s tree:value SHOULD be set.*
#### *2.3.2 The object of tree:value SHOULD be accompanied by a data type when it is a literal value.*
- [ ] Check when tree:value is accompanied by a data type , LDES client and LDES Server works as expected
- [ ] Check when tree:value is Not accompanied by a data type , LDES client and LDES Server works as expected
#### *2.3.3 Every tree:Relation SHOULD have a tree:path, indicating the path from the member to the object on which the tree:Relation applies.*
#### *2.3.4 When traversing, a client SHOULD keep a list of already visited pages, as despite this being the TREE spec, circular references and back-links are not explicitly prohibited*
- [ ] Check the data persistency of the LDES Client.
#### *2.3.5 When using relations such as tree:LessThanRelation or tree:GreaterThanRelation, the time literals need to be compared according to these 3 possible data types: xsd:date, xsd:dateTime or xsd:dateTimeStamp.*
- [ ] Check LDES Server time fragment should work with the ontology with following data types:
	- [ ] xsd:date
	- [ ] xsd:dateTime
	- [ ] xsd:dateTimeStamp.
- - [ ] Check LDES Client could replicate the LDES collection which is with the 'tree:path' is set, and the 'tree:path' is following data types:
	- [ ] xsd:date
	- [ ] xsd:dateTime
	- [ ] xsd:dateTimeStamp.

## [2.4 Searching through the collection](https://treecg.github.io/specification/#searching)
## [2.5 Imports](https://treecg.github.io/specification/#imports)
#### *2.5.1 A `tree:importStream` can also be defined for providing a pub-sub interface for subscribing to real-time updates. The object SHOULD be a [[websockets]](https://treecg.github.io/specification/#biblio-websockets) or Server-Sent Events ([[eventsource]](https://treecg.github.io/specification/#biblio-eventsource)).*

####	*2.5.2 [[VOCAB-DCAT-2]](https://treecg.github.io/specification/#biblio-vocab-dcat-2) is the standard for Open Data Portals by W3C. In order to find TREE compliant datasets in data portals, there SHOULD be a `dcat:accessURL` from the `dcat:Distribution` to the entrypoint where the `tree:Collection`s are described. Furthermore, there SHOULD be a `dct:conformsTo` this URI: `https://w3id.org/tree`.*

####	*2.5.3 Therefore, when using AS (Activity Streams 2.0) collections, a client implementation should gather the members from the `tree:Node` or `as:CollectionPage` instead.*

# [3 The Tree Specification](https://treecg.github.io/specification/#introduction) [Optional 🟦]


> When the MAY situation applied, the system MUST NOT crash!
##	[3.1 Collections](https://treecg.github.io/specification/#introduction)
##	[3.2 Core Concept](https://treecg.github.io/specification/#core-concepts)
#### *3.2.1 Three properties MAY thus be used:*
	1.  `ex:C1 tree:view <> .`  
	    May be used  _only_  in the case when the entire  `tree:Collection`  can be found starting from the current node.	    
	2.  `ex:C1 void:subset <> .`  
	    When the node is not a node from which all members can be found, but still a subset of the collection can be found.	    
	3.  `<> dcterms:isPartOf ex:C1 .`  

 - [ ]  Check when any mentioned properties are used, LDES Server doesn't crash for ingesting stream.
 - [ ]  Check when any mentioned properties are used, LDES Client doesn't crash for subscribed stream.

####	*3.2.2 Multiple tree:view links MAY be provided*
- [ ] Check LDES Server and LDES Client doesn't crash with multiple tree:view links

####	*3.2.3 Note: For compatibility with the Solid specifications, a ShEx shape may also be given (see the chapter on compatibility bellow).*
- [ ] Check when LDES stream is set with a  `ShEx shape `, LDES server fragment works as expected
- [ ] Check when LDES stream is set with a  `ShEx shape `, LDES server doesn't crash

##	[3.3 Relations](https://treecg.github.io/specification/#relations)

####  *3.3.1 A tree:Node element MAY have one or more tree:relation properties.*
- [ ] Check when tree:Node element has one or more tree:relation properties, LDES Server doesn't crash for ingesting stream.
- [ ] Check when tree:Node element has one or more tree:relation properties, LDES Client doesn't crash for subscribed stream.
####	*3.3.2 A relation is an entity of the type tree:Relation, and MAY have a more specific type.*
####	*3.3.3 All possible combinations of e.g., `shacl:alternativePath`, `shacl:inversePath` or `shacl:inLanguage` in the SHACL spec can be used.*
- [ ] Check when All possible combinations of e.g., `shacl:alternativePath`, `shacl:inversePath` or `shacl:inLanguage` in the SHACL spec being used., LDES Client doesn't crash.
- [ ] Check when All possible combinations of e.g., `shacl:alternativePath`, `shacl:inversePath` or `shacl:inLanguage` in the SHACL spec being used., LDES Server doesn't crash.
####	*3.3.4 Every tree:Relation MAY provide a tree:remainingItems.*
- [ ] Check when   `tree:remainingItems ` is set. LDES Server doesn't crash for ingesting stream.
- [ ] Check when   `tree:remainingItems ` is set. LDES Client doesn't crash for subscribed stream.
####	*3.3.5 A client MAY use tree:remainingItems to estimate the completeness of the downloaded elements to the end-user.*
- [ ] Same as previous one
####	*3.3.6 A tree:import MAY be defined in the tree:Relation instance.*
- [ ] Check when  `tree:import `  is set. LDES Server doesn't crash for ingesting stream.
- [ ] Check when  `tree:import  ` is set. LDES Client doesn't crash for subscribed stream
####	*3.3.7 When there are no `tree:member`s and/or no `tree:Collection` defined, then the `tree:path` refers to a pattern that can start from every triple in the page.*
- [ ] Check when  no `tree:member`s and/or no `tree:Collection` defined is set. LDES Server doesn't crash for ingesting stream.
- [ ] Check when no `tree:member`s and/or no `tree:Collection` defined is set. LDES Client doesn't crash for subscribed stream
####	*3.3.8 When a `tree:path` is defined, mind that you also may have to check the language of the element using the property `shacl:inLanguage` More languages MAY be set. When no language is set, all strings are compared.*

- [ ] Check when  `tree:path` and  `shacl:inLanguage` is set. LDES Server doesn't crash for ingesting stream.
- [ ] Check when  `tree:path` and  `shacl:inLanguage` is set. LDES Client doesn't crash for subscribed stream
- [ ] Check when  `tree:path` is set and  `shacl:inLanguage` is not set. LDES Server doesn't crash for ingesting stream. Fragment works as expected.
- [ ] Check when  `tree:path` is set and  `shacl:inLanguage` is not set. LDES Client doesn't crash for ingesting stream.

####	*3.3.8 A `tree:path` MAY refer to an implicit property*
- [ ] Check when  `tree:path` refers to an implicit property. LDES Server doesn't crash for ingesting stream.
- [ ] Check when  `tree:path` refers to an implicit property. LDES Client doesn't crash for subscribed stream

## [3.4 Searching through the collection](https://treecg.github.io/specification/#searching)
## [3.5 Imports](https://treecg.github.io/specification/#imports)
####	*3.5.1 On the resources to import, Memento [[RFC7089]](https://treecg.github.io/specification/#biblio-rfc7089) controls MAY be provided for historic versions.*

####	*3.5.2 A client MAY infer a tree:shape of the collection through the st:validatedBy property of the Shapes Tree.*
