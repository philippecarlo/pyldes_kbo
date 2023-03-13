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
