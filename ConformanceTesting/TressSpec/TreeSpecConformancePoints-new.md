
# Conformance Testing framework   
*Conformance test points for an LDES Server implementation regarding the [Tree Spec](https://treecg.github.io/specification/).*
  
The Testing framework follows:  
 - 🟥 Must   
> When the MUST-test fails, the server is considered non-conformant. The conformance score will be zero.  
 - 🟨 Should  
> When the SHOULD test fails, the tested LDES server can still conform to the recommendation. However, the conformance score will be impacted and the maintainer of the LDES server needs to consider alignment. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.  
 - 🟦 Optional  
> A failing MAY-test does conformance but will result in a lower conformance score. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.  
  
# [The Tree Specification](https://treecg.github.io/specification/#introduction)  
## [1 Collections](https://treecg.github.io/specification/#introduction)  
## [2 Core Concept](https://treecg.github.io/specification/#core-concepts)  
## [2.1 Selecting a view from multiple views](https://treecg.github.io/specification/#multiple-collections)  
  
#### 1 *🟥 Must - A node from which all members of a collection can be discovered, can be found through a triple stating ex:C1 tree:view ex:N1 with ex:C1 being a tree:Collection and ex:N1 being a tree:Node.*  
- [ ] Check that the LDES Collection can be fully replicated by following the `tree:view` Node.  
  
#### 2 *🟦 Optional - Three properties MAY thus be used:*  
1.  `ex:C1 tree:view <> .` May be used  _only_  in the case when the entire  `tree:Collection`  can be found starting from the current node.        
2.  `ex:C1 void:subset <> .` When the node is not a node from which all members can be found, but still a subset of the collection can be found.          
3.  `<> dcterms:isPartOf ex:C1 .` The reverse property of 2.
> #NON-TESTABLE no clue on how to specify to use  `void:subset`  and `dcterms:isPartOf` at the ingest side.  
  
#### 3 *🟥 Must - When the current page is a tree:Node, there MUST be a property linking the current page URL to the URI of the tree:Collection.*  
- [ ]  Check that after processing by the LDES Server, each `tree:Node` has a link between current page to `tree:Collection`  
  
#### 4 *🟨 Should - Therefore a data publisher SHOULD annotate a `tree:Collection ` instance with a SHACL shape. The `tree:shape` points to a SHACL description of the shape (sh:NodeShape).*  
- [ ] Check that when the LDES collection is annotated with a SHACL shape, all members of the collection are validated against the SHACL shape  
  
#### 5 *🟨 Should - Note: the shape can be a blank node, or a named node on which you should follow your nose when it is defined at a different HTTP URL.*  
- [ ] Check when LDES stream is set with a blank node or named node and the shape can be resolved, all members conform to the shape  
  
#### 6 *🟦 Optional - 3.2.3 Note: For compatibility with the Solid specifications, a ShEx shape may also be given (see the chapter on compatibility bellow).*  
- [ ] Check that when an LDES collection is annotated with a  `ShEx shape `, the LDES server works as expected  
  
#### 7 *🟥 Must - Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.*  
- [ ] Check the integrity of the retrieved dataset. Amount of Entity Input = Output.  
  
#### 8 *🟦 Optional - Multiple tree:view links MAY be provided*  
- [ ] Check that LDES Server supports multiple view links per collection  
  
#### 9 *🟥 Must - A TREE client MUST traverse all relations from the tree:Nodes linked to this particular collection. A client MUST thus check for ViewDescriptions on both the current node without the tree:viewDescription qualification, as on the current node with the tree:viewDescription link.*  
 - [ ] Check that regardless of the starting point (a node in the middle or the root node), it should be possible to retrieve/discover all members of the dataset including the collection definition and the view description (by following the relations).  
  
#### 10 *🟨 Should - 2.2.3 A client picks the right view that is use-case specific and can be prioritized by studying the tree:ViewDescription’s properties. To fetch all members, one can be chosen at random if no specific tree:ViewDescription is given.*  
> #NOTE: Client conformance is not part of the scope.  
  
## [3 Relations](https://treecg.github.io/specification/#relations)  
## [3.1 Traversing relations](https://treecg.github.io/specification/#traversing)  
#### 11 *🟦 Optional - A tree:Node element MAY have one or more tree:relation properties.*  
- [ ] Check that if LDES Server supports multiple relations (e.g., by using geospatial or substring fragmentation).  
#### 12 *🟦 Optional - A relation is an entity of the type tree:Relation, and MAY have a more specific type.*  
> #NOTE: NON-TESTABLE  
#### 13 *🟥 Must - A tree:Relation MUST have one tree:node object of the type tree:Node.*  
- [ ] Check that every `tree:Relation` has one `tree:node` object of type `tree:Node`.  
#### 14 *🟨 Should - The tree:Relation’s tree:value SHOULD be set.*  
- [ ] Check that all `tree:Relation`’s `tree:value` are set.  
#### 15 *🟨 Should - The object of tree:value SHOULD be accompanied by a data type when it is a literal value.*  
- [ ] Check that every `tree:Relation`’s tree:value is accompanied by a data type when it is a literal value.  
#### 16 *🟨 Should - Every tree:Relation SHOULD have a tree:path, indicating the path from the member to the object on which the tree:Relation applies.*  
- [ ] Check that every `tree:Relation` has a tree:path property set  
#### 17 *🟦 Optional - All possible combinations of e.g., `shacl:alternativePath`, `shacl:inversePath` or `shacl:inLanguage` in the SHACL spec can be used.*  
- [ ] Check that LDES Server supports `SHACL` property paths in `tree:Relations`.  
#### 18 *🟦 Optional - Every tree:Relation MAY provide a tree:remainingItems. A client MAY use tree:remainingItems to estimate the completeness of the downloaded elements to the end-user.*  
> #NOTE: Client conformance is not part of the scope.  
#### 19 *🟨 Should - When traversing, a client SHOULD keep a list of already visited pages, as despite this being the TREE spec, circular references and back-links are not explicitly prohibited*  
> #NOTE: Client conformance is not part of the scope.  
#### 20 *🟦 Optional - A tree:import MAY be defined in the tree:Relation instance.*  
> #NOTE: NON-TESTABLE no clue on how to specify imports at the ingest side.  
## [3.2  Fallbacks](https://treecg.github.io/specification/#fallbacks)  
#### 21  *🟦 Optional - When there are no `tree:member`s and/or no `tree:Collection` defined, then the `tree:path` refers to a pattern that can start from every triple in the page.*  
> #NOTE: NON-TESTABLE. Not in the scope of LDES Server. A tree:Collection is the prerequisties of an LDES Server.  
#### 22  *🟥 Must - The result of the evaluation of the tree:path, is the value that MUST be compared to the tree:value.*  
- [ ] Check if the evaluation based on the tree:path is as expected.  
#### 23  *🟥 Must  - When no tree:path is defined, the tree:value MUST be compared to all members’ triples that can be compared to the tree:value as defined by the type of the relation (or when no members or collection are defined, on every triple in the page). When due to rdfs:range incompatibility, the object cannot be compared, the object will not be considered for comparison.*  
- [ ] Check that when no `tree:path` is defined, all member triple objects on the page containing the relationship that can be compared to the specified tree:value satisfy the relationship. Objects that cannot be compared to the relationship value are not considered for comparison.  
- [ ] Check that when no `tree:path` is defined and no member or collection is specified all triple objects on the page containing the relationship that can be compared to the specified `tree:value` satisfy the relationship. Objects that cannot be compared to the relationship value are not considered for comparison.  
> #Question: Is it possible ingest only `tree:value` not `tree:path` ?
#### 24 *🟦 Optional - A `tree:path` MAY refer to an implicit property*  
- [ ] Check that LDES Server supports `tree:path` refers to an implicit property.  

## [3.3  Specific relations](https://treecg.github.io/specification/#relationsubclasses)  
#### 25 *🟥 Must - When the only type given for a certain Relation is tree:Relation, then the client must dereference all the nodes.*  
> #NOTE: Client conformance is not part of the scope.  
### [3.3.1  Comparing strings](https://treecg.github.io/specification/#relationsubclasses)  
#### 26  *🟥 Must - The strings MUST then be compared according to case-sensitive unicode ordering.*  
- [ ] Verify that string-based fragmentation use case-sensitive unicode ordering.  
- [ ] Verify that when no language is set in the `tree:path`, strings of all languages are used for comparison.  

#### 27 *🟦 Optional - When a `tree:path` is defined, mind that you also may have to check the language of the element using the property `shacl:inLanguage` More languages MAY be set. When no language is set, all strings are compared.*  
- [ ] Verify that LDES server supports `shacl:inLanguage`.  
> #Question: What does that imply? If you have a language that you only fragment for that language?  
### [3.3.2  Comparing geospatial features](https://treecg.github.io/specification/#geospatial)  
#### 28 *🟥 Must - When using tree:GeospatiallyContainsRelation, the tree:path MUST refer to a literal containing a WKT string, such as geosparql:asWKT.*  
- [ ] Verify that when using tree:GeospatiallyContainsRelation, the tree:path refers to a literal containing a WKT string, such as geosparql:asWKT.  
### [3.3.3  Comparing time literals](https://treecg.github.io/specification/#time)  
#### 29 *🟥 Must - When using relations such as tree:LessThanRelation or tree:GreaterThanRelation, the time literals need to be compared according to these 3 possible data types: xsd:date, xsd:dateTime or xsd:dateTimeStamp.*  
- [ ] Verify that the LDES Server supports time fragmentation with evaluation on following data types:  
   - [ ] xsd:date  
   - [ ] xsd:dateTime  
   - [ ] xsd:dateTimeStamp.  
## [4 Searching through the collection](https://treecg.github.io/specification/#searching)  
## [5 Imports](https://treecg.github.io/specification/#imports)  
#### 30 *🟥 Must - When defined as part of the `tree:Relation`, one MUST fetch the import when the relation needs to be correctly evaluated (e.g., the resulting page contains elements without materialized WKT strings, which however can be fetched from the import).*  
> #NOTE: NON-TESTABLE no clue on how to specify imports at the ingest side.  
#### 31 *🟨 Should - `tree:importStream` can also be defined for providing a pub-sub interface for subscribing to real-time updates. The object SHOULD be a [[websockets]](https://treecg.github.io/specification/#biblio-websockets) or Server-Sent Events ([[eventsource]](https://treecg.github.io/specification/#biblio-eventsource)).*  
> #NOTE: NON-TESTABLE no clue on how to specify `tree:importStream` at the ingest side.  
#### 32 *🟦 Optional - instead of tree:import, one can also use tree:conditionalImport which links to an object of the type tree:ConditionalImport with these properties:  
> #NOTE: NON-TESTABLE no clue on how to specify `tree:conditionalImport` at the ingest side.  
#### 33 *🟥 Must - No hypermedia controls in the body MUST be interpreted in the imported resource and the object must be fully contained within that information resource.*  
> #NOTE: NON-TESTABLE.  
#### 34 *🟦 Optional - On the resources to import, Memento [[RFC7089]](https://treecg.github.io/specification/#biblio-rfc7089) controls MAY be provided for historic versions.*  
> #NOTE: NON-TESTABLE.  
  
## [5.1 Compatibility](https://treecg.github.io/specification/#compatibility)  
### [5.1.1 DCAT](https://treecg.github.io/specification/#dcat)
#### 35 *🟨 Should - [VOCAB-DCAT-2](https://treecg.github.io/specification/#biblio-vocab-dcat-2) is the standard for Open Data Portals by W3C. In order to find TREE compliant datasets in data portals, there SHOULD be a `dcat:accessURL` from the `dcat:Distribution` to the entrypoint where the `tree:Collection`s are described. Furthermore, there SHOULD be a `dct:conformsTo` this URI: `https://w3id.org/tree`.*  
 - [ ] Verify that the LDES server root lists all `tree:Collections` and `tree:Views` and that the corresponding view descriptions include a `dct:conformsTo` property with the value https://w3id.org/tree  
### [5.1.3 Activity Streams 2.0](https://treecg.github.io/specification/#activitystreams)  
#### 36 *🟨 Should - Therefore, when using AS (Activity Streams 2.0) collections, a client implementation should gather the members from the `tree:Node` or `as:CollectionPage` instead.*  
> #NOTE: Client conformance is not part of the scope.  
### [5.1.5 Shape trees](https://treecg.github.io/specification/#shapetrees)  
#### 37 *🟦 Optional - 3.5.2 A client MAY infer a tree:shape of the collection through the st:validatedBy property of the Shapes Tree.*  
> #NOTE: Client conformance is not part of the scope.