
  
    
        
##  *Test Suits for LDES Server to conformance the [LDES SPEC](https://semiceu.github.io/LinkedDataEventStreams/#biblio-rfc2119) and [TREE SPEC](https://treecg.github.io/specification/)*  
> #Notice me: For the review, please start from the question page.

### Current test suits follow the scoring system as follows.      
 - 🟥 Must   (Pass - Score no change / Fail - Final score: 0)      
> When the MUST-test fails, the server is considered non-conformant. The conformance score will be zero.        
 - 🟨 Should (Pass - Score + 10/ Fail - (Score - 10) / System Crash - Final score: 0)      
> When the SHOULD tests fail, the tested LDES server can still conform to the recommendation. However, the conformance score will be impacted and the maintainer of the LDES server needs to consider alignment. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.        
 - 🟦 Optional (Pass - Score + 5 / Fail - (Score - 5) / System Crash - Final score: 0)      
> A failing MAY-test does conformance but will result in a lower conformance score. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.      
      
## Test Suits against [Conformance Points](./TreeSpecConformancePoints.md)
  
### 🟥 Must - Test case 1  
    
***Scenario** : 
 - *Launch the LDES Server with `tree:view` configured.*

***Expected result**: 

 - *LDES Server does the fragment and provides a `tree:view` in the output LDES collection.*

>Fulfil the Conformance Point: 1.  
    
### 🟥 Must - Test case 2  
  ***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured.*   
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

  
  ***Expected result**:  

 - *Each `tree:Node` in the LDES Collection has a link between current page to `tree:Collection`.*
>Fulfil the Conformance Point: 3.

    
    
### 🟨 Should - Test case 3  
  
***Scenario** :    

 - *1. Launch the LDES Server.* 
 - *2. Traverse all the linked `LDES members` in the output collection.*

 ***Expected result**:

 - *There is a tree:shape annotation in the whole graph*
>Fulfil the Conformance Point: 4.

   
### 🟨 Should - Test case 4  
  
***Scenario** :    
 - *1. Launch the LDES Server with `Blank Node` configured to the SHACL shape.*

 ***Expected result**: 
- LDES Server works correctly.* 
> Fulfil the Conformance Point: 5.
> The shape can be a blank node, or a named node on which you should follow your nose when it is defined at a different HTTP URL.
  
### 🟦 Optional - Test case 5  
  
***Scenario** :    

 - *1. Launch the LDES Server with `SHEx shape` configured.* 
 - *2. Traverse all the linked `LDES members` in the output collection.*

 ***Expected result**: 

 - *All members of the collection are conform to the `ShEx Shape` shape.*

 >Fulfil the Conformance Point: 6.  
   
### 🟥 Must - Test case 6  
  ***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured.*
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

  ***Expected result**:  

 - *The amount of the LDES members = The Input LDES members (20, in the context of BEL20, KBO data).*

>Fulfil the Conformance Point: 7.  
  
  
### 🟦 Optional - Test case 7  
  
***Scenario** :    

 - *1. Launch the LDES Server with several `tree:view` configured.*

 ***Expected result**:  

 - *LDES Server fragments the input stream to the defined multi-views.*

 > Fulfil the Conformance Point: 8.  
  
### 🟥 Must - Test case 8  
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured.* 
 - *2. Traverse the full fragmented LDES Collection, by following a random `url` of the `treeNode` pointed by `tree:node`.*

  ***Expected result**:  

 - *The full collection can be replicated/traversed . The amount of the LDES members = The Input LDES members (20, in the context of BEL20, KBO data)*

> Fulfil the Conformance Point: 9.  
  
### 🟦 Optional - Test case 9  
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured to make `geospatial fragment`.*
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by treeView`.*

  ***Expected result**:  

 - *Some `tree:Relation` has more than one `tree:relation`.*

 >Fulfil the Conformance Point: 11.   
  
### 🟥 Must - Test case 10  
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured.*
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

  ***Expected result**:  
 -  *Each `tree:Relation` has one `tree:node` object of the type `tree:Node`.*

 >Fulfil the Conformance Point: 13.  
  
### 🟨 Should - Test case 11  
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured.*
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

  ***Expected result**:  
 - *Each `tree:Relation` has one `tree:value` set.*
 >Fulfil the Conformance Point: 14.  
  
  
### 🟨 Should - Test case 12  (DUPLICATED with TEST CASE 11)
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured.*
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

  ***Expected result**:  

 - *Each `tree:Relation` has one `tree:value` set.*

 >Fulfil the Conformance Point: 14.  
  
### 🟨 Should - Test case 13  
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured.* 
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

  ***Expected result**:  

 - *Each `tree:Relation`'s `tree:value` is accompanied by a data type when it is a literal value.*

 >Fulfil the Conformance Point: 15.  
  
### 🟨 Should - Test case 14  
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured.* 
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

  
***Expected result**:  

 - *Each `tree:Relation` has one `tree:path` set.*

 >Fulfil the Conformance Point: 16.  
  
### 🟦 Optional - Test case   15  
> #TODO  
  
***Scenario** :    

 - *1. Launch the LDES Server with `SHACL shape` configured,  `SHACL shape` contains `shacl:alternativePath`.*
 -   *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

  ***Expected result**:  
 *All members of the collection conform to the `SHACL` shape*  
 >Fulfil the Conformance Point: 17 - All possible combinations of e.g., `shacl:alternativePath`, `shacl:inversePath` or `shacl:inLanguage` in the SHACL spec can be used.*   
  
### 🟥 Must - Test case 16  
  
***Scenario** :    
- *1. Launch the LDES Server with `tree:view` configured.* 
- *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*  

***Expected result**:  
 - The evaluation based on the `tree:value` of the `tree:path` is correct.*   
 >Fulfil the Conformance Point: 22.  
  
### 🟥 Must - Test case 17  
> #Question: Is it possible ingest only `tree:value` not `tree:path` ?  
  
***Scenario** :    
- *1. Launch the LDES Server with `tree:view` configured, and no `tree:path` is defined.* 
- *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*  

***Expected result**:  
 - *All member triple objects on the page containing the relationship that can be compared to the specified `tree:value` satisfy the relationship. Objects that cannot be compared to the relationship value are not considered for comparison.*   
 >Fulfil the Conformance Point: 23.  
  
  
### 🟦 Optional - Test case 18  

***Scenario** :    
- *1. Launch the LDES Server with `tree:view` configured, and `tree:path` refers to an implicit property.*   
- *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*  

***Expected result**:  
 - *The evaluation based on the `tree:value` of the `tree:path` is correct.*   
 >Fulfil the Conformance Point: 24.  
  
### 🟦 Optional - Test case 19  (DUPLICATED with TEST CASE 18)
***Scenario** :    

 -  *1. Launch the LDES Server with `tree:view` configured, and `tree:path` refers to an implicit property.*  
 -  *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

 ***Expected result**:  
- *The evaluation based on the `tree:value` of the `tree:path` is correct.*   
 >Fulfil the Conformance Point: 24.  
  
  
### 🟥 Must - Test case 20  [ONLY FOR Comparing strings fragment]  
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured to do `string-based fragmentation`, Language is set in the `tree:path`.*
 - *2. Traverse the full fragmented LDES Collection, by following `url` of the `treeNode` pointed by `treeView`.*

***Expected result**:  

 - *The evaluation based on the `tree:value` of the `tree:path` is complaint to case-sensitive unicode ordering*

 >Fulfil the Conformance Point: 26.     


###  🟦 Optional - Test case 21
>#Todo: Space hold for 27
>#Question: What does that imply? If you have a language that you only fragment for that language?
  
***Scenario** :    
***Expected result**:  
   
 >Fulfil the Conformance Point: 27.

### 🟥 Must - Test case 22 [ONLY FOR geospatial fragmentation]  
  
***Scenario** :    

 - *1. Launch the LDES Server with `tree:view` configured to do `geospatial fragmentation`.*
 - *2. Traverse the full fragmented LDES  Collection, by following the `url` of the `treeNode` pointed by`treeView`.*

  ***Expected result**:  
 - *The tree:path of each `tree:Relation` refers to a literal containing a WKT string, such as geosparql:asWKT.*   
 >Fulfil the Conformance Point: 28.

### 🟥 Must - Test case 23 [ONLY FOR time fragmentation]  
  
***Scenario** :    
 - *1. Launch the LDES Server with `tree:view` configured to do `time fragmentation` , `tree:value` is set with `xsd:date` datatype.*
 - *2. Traverse the full fragmented LDES  Collection, by following the `url` of the `treeNode` pointed by`treeView`.*

  ***Expected result**:  
 *The evaluation based on the `tree:value` is correct.*   
 >Fulfil the Conformance Point: 29.

 
### 🟥 Must - Test case 24 [ONLY FOR time fragmentation]  
  
***Scenario** :    
 -  *1. Launch the LDES Server with `tree:view` configured to do `time fragmentation` , `tree:value` is set with `xsd:dateTime` datatype.*
 -  *2. Traverse the full fragmented LDES  Collection, by following the `url` of the `treeNode` pointed by`treeView`.*

  ***Expected result**:  
 *The evaluation based on the `tree:value` is correct.*   
 >Fulfil the Conformance Point: 29.

 
### 🟥 Must - Test case 25 [ONLY FOR time fragmentation]  
  
***Scenario** :    
 -  *1. Launch the LDES Server with `tree:view` configured to do `time fragmentation` , `tree:value` is set with ` xsd:dateTimeStamp` datatype.*
 -  *2. Traverse the full fragmented LDES  Collection, by following the `url` of the `treeNode` pointed by`treeView`.*

  ***Expected result**:-
  - *The evaluation based on the `tree:value` is correct.*   
 >Fulfil the Conformance Point: 29.

###  🟨 Should - Test case 26
  
***Scenario** :    
 -  *1. Launch the LDES Server with `tree:view` configured to do `time fragmentation` , `tree:value` is set with ` xsd:dateTimeStamp` datatype.*
 -  *2. ping the root `tree:Node` of the LDES collection.*

  ***Expected result**:  
-  *the LDES server root lists all `tree:Collections` and `tree:Views` and that the corresponding view descriptions include a `dct:conformsTo` property with the value https://w3id.org/tree.*
 >Fulfil the Conformance Point: 35.
