  
  
## ❗️ ❗️ The following test plan can be considered as a test suit, which needs to be executed for each supporting fragment: ❗️ ❗  
  
 - [ ] Geo-based fragment   
 - [ ] Substring fragment   
 - [ ] Time-based fragment  
 - [ ] Pagination fragment  
  
## ❗️ ❗️ ***To meet the conformance standard*** ❗️ ❗  
- The under-testing component is possible to be configured to performance the test case.  
- The test output meets the expectation of the test case.  
   
## 🌈 LDES Server Test Plan  
#### Test case 1:   
##### 1.  Launch LDES Server with Single Fragment,  `tree:path` configured. Verify the following points:  
a. [1.2.1](./TreeSpecConformancePoints.md#121-when-the-current-page-is-a-treenode-there-must-be-a-property-linking-the-current-page-url-to-the-uri-of-the-treecollection)   
b. [1.3.1](./TreeSpecConformancePoints.md#131-a-treerelation-must-have-one-treenode-object-of-the-type-treenode)  
c. [1.3.2](./TreeSpecConformancePoints.md#132-the-result-of-the-evaluation-of-the-treepath-is-the-value-that-must-be-compared-to-the-treevalue)  
d. [1.3.4](./TreeSpecConformancePoints.md#134-when-the-only-type-given-for-a-certain-relation-is-treerelation-then-the-client-must-dereference-all-of-the-nodes)  
e. [1.3.5](./TreeSpecConformancePoints.md#135-the-strings-must-then-be-compared-according-to-case-sensitive-unicode-ordering)  
f. [1.3.6](./TreeSpecConformancePoints.md#136-when-using-treegeospatiallycontainsrelation-the-treepath-must-refer-to-a-literal-containing-a-wkt-string-such-as-geosparqlaswkt)  
g. [2.3.3](./TreeSpecConformancePoints.md#233-every-treerelation-should-have-a-treepath-indicating-the-path-from-the-member-to-the-object-on-which-the-treerelation-applies)  
  
#### Test case 2:   
##### 2.   Launch LDES Server with Single Fragment. The `tree:path`'s value set to `xsd:date` to Verify the following points:  
a. [2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)  
  
#### Test case 3:   
##### 3.   Launch LDES Server with Single Fragment. The tree:path’s value is set to `xsd:dateTime` to Verify the following points:  
a. [2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)  
  
#### Test case 4:   
##### 4.   Launch LDES Server with Single Fragment, tree:path configured.  The tree:path’s value is set to `xsd:dateTimeStamp` to Verify the following points:  
a. [2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)  
  
#### Test case 5:  
##### 5.   Launch LDES Server with Single fragment configuration, with NO `tree:path` defined for the fragment. Some properties' `rdfs:range` is incompatible to be compared. Verify following points:  
a. [1.3.3](./TreeSpecConformancePoints.md#133-when-no-treepath-is-defined-the-treevalue-must-be-compared-to-all-members-triples-that-can-be-compared-to-the-treevalue-as-defined-by-the-type-of-the-relation-or-when-no-members-or-collection-are-defined-on-every-triple-in-the-page-when-due-to-rdfsrange-incompatibility-the-object-can%20not-be-compared-the-object-will-not-be-considered-for-comparison)  
#### Test case 6:   
##### 6.  Launch LDES Server with Single Fragment configuration, with `tree:path` configured. `SHACL` shape is properly configured (Not a Blank Node). Verify the following points:  
a. [2.2.1](./TreeSpecConformancePoints.md#231-the-treerelations-treevalue-should-be-set)  
#### Test case 7:  
##### 7.  Launch LDES Server with Single Fragment configuration, with `tree:path` configured. SHACL shape is configured with a blank node. Verify the following points:  
a. [2.2.2](./TreeSpecConformancePoints.md#222-note-the-shape-can-be-a-blank-node-or-a-named-node-on-which-you-should-follow-your-nose-when-it-is-defined-at-a-different-http-url)  
#### Test case 8:  
##### 8.    Launch LDES Server with Single Fragment configuration, with `tree:path` configured. `tree:value` is accompanied by a data type. Verify the following points:  
a. [2.3.2](./TreeSpecConformancePoints.md#232-the-object-of-treevalue-should-be-accompanied-by-a-data-type-when-it-is-a-literal-value)  
#### Test case 9:  
##### 9.    Launch LDES Server with Single Fragment configuration, with `tree:path` configured. `tree:value` is Not accompanied by a data type. Verify the following points:  
a. [2.3.2](./TreeSpecConformancePoints.md#232-the-object-of-treevalue-should-be-accompanied-by-a-data-type-when-it-is-a-literal-value)  
#### Test case 10:  
##### 10.   Launch LDES Server with multi-`tree:view` configured. Verify the following points:  
a. [3.2.2](./TreeSpecConformancePoints.md#322-multiple-treeview-links-may-be-provided)  
  
#### Test case 11:  
  
##### 11.   Launch LDES Server with Single Fragment configuration, with `tree:path` configured. `ShEx` shape is properly configured (Not a Blank Node). Verify the following points:  
a. [3.2.3](./TreeSpecConformancePoints.md#323-note-for-compatibility-with-the-solid-specifications-a-shex-shape-may-also-be-given-see-the-chapter-on-compatibility-bellow)  
  
#### Test case 12:  
##### 12.   Launch LDES Server with Single Fragment configuration, with `tree:path` configured. The `Tree:Node` has more than ONE `tree:relation` property. Verify the following points:  
a. [3.3.1](./TreeSpecConformancePoints.md#331-a-treenode-element-may-have-one-or-more-treerelation-properties)  
  
#### Test case 13:  
##### 13.   Launch LDES Server with Single Fragment configuration, with `tree:path` configured. The `tree:remaining` Items is set in the ingesting stream or on the LDES server. Verify the following points:  
a. [3.3.4](./TreeSpecConformancePoints.md#334-every-treerelation-may-provide-a-treeremainingitems)  
  
#### Test case 14:  
##### 14.   Launch LDES Server with Single Fragment configuration, with `tree:path` configured. The `tree:import` is contained in the LDES stream which is ingested to the LDES Server. Verify the following points:  
a. [3.3.5](./TreeSpecConformancePoints.md#335-a-client-may-use-treeremainingitems-to-estimate-the-completeness-of-the-downloaded-elements-to-the-end-user)  
  
#### Test case 15:  
##### 15.   Launch LDES Server with Single Fragment configuration, with No `tree:member` configured. Verify the following points:  
a. [3.3.7](./TreeSpecConformancePoints.md#337-when-there-are-no-treemembers-andor-no-treecollection-defined-then-the-treepath-refers-to-a-pattern-that-can-start-from-every-triple-in-the-page)  
  
## 🌈 LDES Client Test Plan (#TODO)  
#### Test case 1:   
##### 2.   Launch LDES Client with the configuration to the link of a `tree:view`, the LDES collection is with `tree:path` configured. `tree:value` is accompanied by a data type.   To Verify the following points:  
a. [1.2.2](./TreeSpecConformancePoints.md#122-every-entity-linked-from-treeview-must-be-an-entry-point-to-retrieve-all-members-of-the-collection)  
b. [2.3.2](./TreeSpecConformancePoints.md#232-the-object-of-treevalue-should-be-accompanied-by-a-data-type-when-it-is-a-literal-value)  

#### Test case 2:   
##### 2.   Launch LDES Client with the configuration to the link of a `tree:view`,  the LDES collection has `tree:viewDescription` configured. To Verify the following points:  
a. [1.2.3](./TreeSpecConformancePoints.md#123-a-tree-client-must-traverse-all-relations-from-the-treenodes-linked-to-this-particular-collection-a-client-must-thus-check-for-viewdescriptions-on-both-the-current-node-without-the-treeviewdescription-qualification-as-on-the-current-node-with-the-treeviewdescription-link)  
  
#### Test case 3:   
##### 3.    Launch LDES Client with the configuration to the link of LDES Stream,  the LDES collection has `tree:viewDescription` configured, also several view. To Verify the following points:   
a. [2.2.3](./TreeSpecConformancePoints.md#223-a-client-picks-the-right-view-that-is-use-case-specific-and-can-be-prioritized-by-studying-the-treeviewdescriptions-properties-to-fetch-all-members-one-can-be-chosen-at-random-if-no-specific-treeviewdescription-is-given)  

#### Test case 4:    
##### 4.     Launch LDES Client with the configuration to the link of a `tree:view`,   the LDES collection is with `tree:path` configured. `tree:value` is NOT accompanied by a data type. Verify the following points:    
a. [2.3.2](./TreeSpecConformancePoints.md#232-the-object-of-treevalue-should-be-accompanied-by-a-data-type-when-it-is-a-literal-value)

#### Test case 5:   
##### 5.   Launch LDES Client with the configuration to the link of a `tree:view`, stop and restart the client. The client should not go to visit the page already been visited. This test is to verify the persistency of the LDES server.  The testing point is: 
a. [2.3.4](./TreeSpecConformancePoints.md#234-when-traversing-a-client-should-keep-a-list-of-already-visited-pages-as-despite-this-being-the-tree-spec-circular-references-and-back-links-are-not-explicitly-prohibited)  

#### Test case 6:     
##### 2.     Launch LDES Client with the configuration to the link of a `tree:view`,   the LDES collection is with`tree:path` configured. Using relations such as `tree:LessThanRelation` or `tree:GreaterThanRelation`. The `tree:path`'s value set to `xsd:date` to Verify the following points:    
a. [2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)    
    
#### Test case 7: 
##### 3.   Launch LDES Client with the configuration to the link of a `tree:view`,   the LDES collection is with`tree:path` configured. Using relations such as `tree:LessThanRelation` or `tree:GreaterThanRelation`. The `tree:path`’s value is set to `xsd:dateTime` to Verify the following points:    
a. [2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)    
    
#### Test case 8: 
##### 4.   Launch LDES Client with the configuration to the link of a `tree:view`,   the LDES collection is with`tree:path` configured. Using relations such as `tree:LessThanRelation` or `tree:GreaterThanRelation`.  The `tree:path`’s value is set to `xsd:dateTimeStamp` to Verify the following points:    
a. [2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)