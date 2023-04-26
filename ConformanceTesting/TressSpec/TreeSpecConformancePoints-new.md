# Conformance Testing framework 
*The current framework is made for conforming the test points regarding the [Tree Spec](https://treecg.github.io/specification/), under the circumstances of implementing an LDES Server.*

Which contains:
 - [🟥 Must](#the-tree-specification-must-) 
> When the MUST-test fails, the server is considered non-conformant. The conformance score will be zero.
 - [🟨 Should ](#the-tree-specification-should-)
> When the SHOULD tests fails, the tested LDES server can still conform to the recommendation. However, the conformance score will be impacted and the maintainer of the LDES server needs to consider alignment. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.
 - [🟦 Optional](#the-tree-specification-optional-)
> A failing MAY-test does conformance but will result in a lower conformance score. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.

# [The Tree Specification](https://treecg.github.io/specification/#introduction)
## [1 Collections](https://treecg.github.io/specification/#introduction)
## [2 Core Concept](https://treecg.github.io/specification/#core-concepts)
## [2.1 Selecting a view from multiple views](https://treecg.github.io/specification/#multiple-collections)

#### *🟦 Optional - Three properties MAY thus be used:*
	1.  `ex:C1 tree:view <> .`  
	    May be used  _only_  in the case when the entire  `tree:Collection`  can be found starting from the current node.	    
	2.  `ex:C1 void:subset <> .`  
	    When the node is not a node from which all members can be found, but still a subset of the collection can be found.	    
	3.  `<> dcterms:isPartOf ex:C1 .`  

- [ ] Check that LDES Server support ontologies 'tree:view', 'void:subset', 'dcterms:isPartOf'

#### *🟥 Must - When the current page is a tree:Node, there MUST be a property linking the current page URL to the URI of the tree:Collection.*
- [ ]  Check that after processing by the LDES Server, each tree:Node has a link between current page to tree:Collection

#### *🟨 Should - Therefore a data publisher SHOULD annotate a tree:Collection instance with a SHACL shape. The tree:shape points to a SHACL description of the shape (sh:NodeShape).*
- [ ] Check that when the LDES collection is annotated with a SHACL shape, all members of the collection are validated against the SHACL shape

#### *🟨 Should - Note: the shape can be a blank node, or a named node on which you should follow your nose when it is defined at a different HTTP URL.*
- [ ] Check when LDES stream is set with a blank node or named node and the shape can be resolved, all members conform to the shape

#### *🟦 Optional - 3.2.3 Note: For compatibility with the Solid specifications, a ShEx shape may also be given (see the chapter on compatibility bellow).*
- [ ] Check that when an LDES collection is annotated with a  `ShEx shape `, the LDES server works as expected

#### *🟥 Must - Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.*
- [ ] Check the integrity of the retrieved dataset. Amount of Entity Input = Output.

#### *🟦 Optional - Multiple tree:view links MAY be provided*
- [ ] Check that LDES Server supports multiple view links per collection

#### *🟥 Must - A TREE client MUST traverse all relations from the tree:Nodes linked to this particular collection. A client MUST thus check for ViewDescriptions on both the current node without the tree:viewDescription qualification, as on the current node with the tree:viewDescription link.*
 - [ ] Check that regardless of the startting point (a node in the middle or the root node), it should be possible to retrieve/discover all members of the dataset including the collection definition and the view description (by following the relations).

#### *🟨 Should - 2.2.3 A client picks the right view that is use-case specific and can be prioritized by studying the tree:ViewDescription’s properties. To fetch all members, one can be chosen at random if no specific tree:ViewDescription is given.*
> #NOTE: Client conformance is not part of the scope.

## [3 Relations](https://treecg.github.io/specification/#relations)
## [3.1 Traversing relations](https://treecg.github.io/specification/#traversing)
####  *🟦 Optional - A tree:Node element MAY have one or more tree:relation properties.*
- [ ] Check that if LDES Server supports multiple relations (e.g., by using geospacial or substring fragmentation).
####  *🟦 Optional - A relation is an entity of the type tree:Relation, and MAY have a more specific type.*
> #NOTE: NON-TESTABLE
#### *🟥 Must - A tree:Relation MUST have one tree:node object of the type tree:Node.*
- [ ] Check that every `tree:Relation` has one tree:node object of type tree:Node.
#### *🟨 Should - The tree:Relation’s tree:value SHOULD be set.*
- [ ] Check that all `tree:Relation`’s tree:value are set.
#### *🟨 Should - The object of tree:value SHOULD be accompanied by a data type when it is a literal value.*
- [ ] Check that every `tree:Relation`’s tree:value is accompanied by a data type when it is a literal value.
#### *🟨 Should - Every tree:Relation SHOULD have a tree:path, indicating the path from the member to the object on which the tree:Relation applies.*
- [ ] Check that every `tree:Relation` has a tree:path property set
#### *🟦 Optional - All possible combinations of e.g., `shacl:alternativePath`, `shacl:inversePath` or `shacl:inLanguage` in the SHACL spec can be used.*
- [ ] Check that LDES Server supports `SHACL` property paths in `tree:Relations`.
#### *🟦 Optional - Every tree:Relation MAY provide a tree:remainingItems. A client MAY use tree:remainingItems to estimate the completeness of the downloaded elements to the end-user.*
- [ ] Check that LDES Server supports `tree:remainingItems`.
> #NOTE: Client conformance is not part of the scope.
#### *🟨 Should - When traversing, a client SHOULD keep a list of already visited pages, as despite this being the TREE spec, circular references and back-links are not explicitly prohibited*
> #NOTE: Client conformance is not part of the scope.
####	*🟦 Optional - A tree:import MAY be defined in the tree:Relation instance.*
> #NOTE: NON-TESTABLE no clue on how to specify imports at the ingest side.
## [3.2  Fallbacks](https://treecg.github.io/specification/#fallbacks)
####	*🟦 Optional - When there are no `tree:member`s and/or no `tree:Collection` defined, then the `tree:path` refers to a pattern that can start from every triple in the page.*
> #NOTE: NON-TESTABLE. Not in the schop of LDES Server. A tree:Collection is the prerequisties of an LDES Server.
####	*🟥 Must - The result of the evaluation of the tree:path, is the value that MUST be compared to the tree:value.*
- [ ] Check if the evaluation based on the tree:path is as expected.
####	*(🟥 Must ) - When no tree:path is defined, the tree:value MUST be compared to all members’ triples that can be compared to the tree:value as defined by the type of the relation (or when no members or collection are defined, on every triple in the page). When due to rdfs:range incompatibility, the object cannot be compared, the object will not be considered for comparison.*
- [ ] Check that when no tree:path is defined, all member triple objects on the page containing the relationship that can be compared to the specified tree:value satisfy the relationship. Objects that cannot be compared to the relationship value are not considered for comparison.
- [ ] Check that when no tree:path is defined and no member or collection is specified all triple objects on the page containing the relationship that can be compared to the specified tree:value satisfy the relationship. Objects that cannot be compared to the relationship value are not considered for comparison.
#### *🟦 Optional - A `tree:path` MAY refer to an implicit property*
- [ ] Check that LDES Server supports `tree:path` refers to an implicit property.
## [3.3  Specific relations](https://treecg.github.io/specification/#relationsubclasses)
####	*🟥 Must - When the only type given for a certain Relation is tree:Relation, then the client must dereference all of the nodes.*
> #NOTE: Client conformance is not part of the scope.
### [3.3.1  Comparing strings](https://treecg.github.io/specification/#relationsubclasses)
####	*🟥 Must - The strings MUST then be compared according to case-sensitive unicode ordering.*
- [ ] Verify that string-based fragmentation use case-sensitive unicode ordering.
- [ ] Verify that when no langauge is set in the tree:path, strings of all languages are used for comparison.
#### *🟦 Optional - When a `tree:path` is defined, mind that you also may have to check the language of the element using the property `shacl:inLanguage` More languages MAY be set. When no language is set, all strings are compared.*
- [ ] Verify that LDES server supports `shacl:inLanguage`.
> #Question: What does that imply? If you have a langauge that you only fragment for that langauge?
### [3.3.2  Comparing geospatial features](https://treecg.github.io/specification/#geospatial)
#### *🟥 Must - When using tree:GeospatiallyContainsRelation, the tree:path MUST refer to a literal containing a WKT string, such as geosparql:asWKT.*
- [ ] Verify that when using tree:GeospatiallyContainsRelation, the tree:path refers to a literal containing a WKT string, such as geosparql:asWKT.
### [3.3.3  Comparing time literals](https://treecg.github.io/specification/#time)
#### *🟥 Must - When using relations such as tree:LessThanRelation or tree:GreaterThanRelation, the time literals need to be compared according to these 3 possible data types: xsd:date, xsd:dateTime or xsd:dateTimeStamp.*
- [ ] Verify that the LDES Server supports time fragmentation with evaluation on following data types:
	- [ ] xsd:date
	- [ ] xsd:dateTime
	- [ ] xsd:dateTimeStamp.
> #Question: Should or Must?
## [4 Searching through the collection](https://treecg.github.io/specification/#searching)
## [5 Imports](https://treecg.github.io/specification/#imports)
####  *🟥 Must - When defined as part of the `tree:Relation`, one MUST fetch the import when the relation needs to be correctly evaluated (e.g., the resulting page contains elements without materialized WKT strings, which however can be fetched from the import).*
- [ ] Verify that the LDES Server supports imports configuration.
- [ ] Verify that the LDES Server supports evaluation on import resource.
#### *🟨 Should - `tree:importStream` can also be defined for providing a pub-sub interface for subscribing to real-time updates. The object SHOULD be a [[websockets]](https://treecg.github.io/specification/#biblio-websockets) or Server-Sent Events ([[eventsource]](https://treecg.github.io/specification/#biblio-eventsource)).*
- [ ] Verify that the LDES Server supports `tree:importStream`.
#### *🟦 Optional - instead of tree:import, one can also use tree:conditionalImport which links to an object of the type tree:ConditionalImport with these properties:
- [ ] Verify that the LDES Server supports `tree:conditionalImport`.
- [ ] Verify that the LDES Server supports `tree:ConditionalImport`.
####    *🟥 Must - No hypermedia controls in the body MUST be interpreted in the imported resource and the object must be fully contained within that information resource.*
> #NOTE: NON-TESTABLE.
####	*🟦 Optional - On the resources to import, Memento [[RFC7089]](https://treecg.github.io/specification/#biblio-rfc7089) controls MAY be provided for historic versions.*
> #NOTE: NON-TESTABLE.

## [5.1 Compatibility](https://treecg.github.io/specification/#compatibility)
### [5.1.1 DCAT] (https://treecg.github.io/specification/#dcat
####	🟨 Should - [[VOCAB-DCAT-2]](https://treecg.github.io/specification/#biblio-vocab-dcat-2) is the standard for Open Data Portals by W3C. In order to find TREE compliant datasets in data portals, there SHOULD be a `dcat:accessURL` from the `dcat:Distribution` to the entrypoint where the `tree:Collection`s are described. Furthermore, there SHOULD be a `dct:conformsTo` this URI: `https://w3id.org/tree`.*
 - [ ] Verify that the LDES server root lists all tree:Collections and tree:Views and that the corresponding view descriptions include a dct:conformsTo property with the value https://w3id.org/tree
### [5.1.3 Activity Streams 2.0] (https://treecg.github.io/specification/#activitystreams)
####	*🟨 Should - Therefore, when using AS (Activity Streams 2.0) collections, a client implementation should gather the members from the `tree:Node` or `as:CollectionPage` instead.*
> #NOTE: Client conformance is not part of the scope.
### [5.1.5 Shape trees] (https://treecg.github.io/specification/#shapetrees)
####	*🟦 Optional - 3.5.2 A client MAY infer a tree:shape of the collection through the st:validatedBy property of the Shapes Tree.*
> #NOTE: Client conformance is not part of the scope.