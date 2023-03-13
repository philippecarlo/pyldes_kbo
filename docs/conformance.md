

# Conformance Testing framework 
*The current framework is make for conforming the test points regarding the[Tree Spec](https://treecg.github.io/specification/)*

Which contains: 

 - [🟥 Must](#must-categor) 
 - [🟩 Optional](#optional-category)

## 🟥 Must Category

### **1. [Core Concepts](https://treecg.github.io/specification/#core-concepts)**

 ***1.1. When the current page is a `tree:Node`, there MUST be a property linking the current page URL to the URI of the `tree:Collection`.*** 
  
  ➔ 
 - [ ] for all the page with `tree:Node` tag, there is a property
       linking to the URI of the `tree:Collection`
  
[1.2. Every entity linked from `tree:view` MUST be an entry point to retrieve **all** members of the collection. Multiple `tree:view` links MAY be provided, and a TREE client MUST traverse all relations from the `tree:Node`s linked to this particular collection. ](https://treecg.github.io/specification/#multiple-views)
 
 ➔ A LDES Collection Must be able to be replicated from LDES Server by the root link (identified by 
 `tree: view`). Also its integrity needs to be persisted. The test needs to be run on all the following fragments.   

 - [ ] Time-based fragment view 
 - [ ] Geo-based fragment view 	
 - [ ] Pagination fragment view
 - [ ] Substring fragment view

## 🟩 Optional Category

### **1. [Core Concepts](https://treecg.github.io/specification/#core-concepts)**

[***1.1. When multiple collections are found by a client, it can choose to prune the collections based on the `tree:shape` property. Therefore a data publisher SHOULD annotate a `tree:Collection` instance with a SHACL shape. The `tree:shape` points to a SHACL description of the shape (`sh:NodeShape`).***](https://treecg.github.io/specification/#multiple-collections) 
  
  ➔ 
 - [ ] The  `tree:Collection`  has a SHACL shape linked with
 - [ ] The SHACL shape could be used for pruning the multiple collections retrieved by a client
