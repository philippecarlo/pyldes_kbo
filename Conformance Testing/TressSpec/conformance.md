


# Conformance Testing framework 
*The current framework is make for conforming the test points regarding the[Tree Spec](https://treecg.github.io/specification/)*

Which contains: 

 - [🟥 Must](#must-category) 
 - [🟨 Should](#)
 - [🟩 Optional](#optional-category)



# The Tree Specification [Must] 🟥

## Collections
## Core Concept
#### *When the current page is a tree:Node, there MUST be a property linking the current page URL to the URI of the tree:Collection.*
		    

 - [ ] LDES Server, a tree:Node has a link between current page to tree:Collection
	 - [ ]  Geo-based fragment 
	 - [ ]  Substring fragment
	 - [ ]  Time-based fragment
	 - [ ]  pagination fragment 

####  *Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.*	

 - [ ] LDES client retrieves the full collection from the link of  tree:view
 - [ ] Check the integrity of the retrieved dataset
 - [ ] All supporting fragments
	 - [ ]  Geo-based fragment 
	 - [ ]  Substring fragment
	 - [ ]  Time-based fragment
	 - [ ]  pagination fragment 

####	*A TREE client MUST traverse all relations from the tree:Nodes linked to this particular collection.*

 - [ ] Same as previous points
 - [ ] Check the reaction of the LDES Client when the relation is more than one. [LDES Client Must Not crash]
 
####	*A client MUST thus check for ViewDescriptions on both the current node without the tree:viewDescription qualification, as on the current node with the tree:viewDescription link.*
	
 - [ ] LDES client retrives all dataset if there is tree:viewDescription
 - [ ] LDES client retrives all dataset if there NO tree:viewDescription

## Relations
####	*A tree:Relation MUST have one tree:node object of the type tree:Node.*

####	*When no tree:path is defined, the tree:value MUST be compared to all members’ triples that can be compared to the tree:value as defined by the type of the relation (or when no members or collection are defined, on every triple in the page).* 


# The Tree Specification [Should] 🟨
##	Collections
##	Core Concept
#### *Therefore a data publisher SHOULD annotate a tree:Collection instance with a SHACL shape. The tree:shape points to a SHACL description of the shape (sh:NodeShape).*
#### *A client picks the right view is use-case specific, and can be prioritized by studying the tree:ViewDescription’s properties. In order to fetch all members, one can be chosen at random if no specific tree:ViewDescription is given.*
##	Relations
#### *The tree:Relation’s tree:value SHOULD be set.*
#### *The object of tree:value SHOULD be accompanied by a data type when it is a literal value.*
#### *Every tree:Relation SHOULD have a tree:path, indicating the path from the member to the object on which the tree:Relation applies.*
####	*A client SHOULD keep a list of already visited pages*

 - [ ] LDES Client persistency

# The Tree Specification [Optional] 🟩
##	Collections
##	Core Concept
####	Multiple tree:view links MAY be provided
##	Relations

####  *A tree:Node element MAY have one or more tree:relation properties.*
####	*A relation is an entity of the type tree:Relation, and MAY have a more specific type.*
####	*Every tree:Relation MAY provide a tree:remainingItems.*
####	*A client MAY use tree:remainingItems to estimate the completeness of the downloaded elements to the end-user.*
####	*A tree:import MAY be defined in the tree:Relation instance.*


