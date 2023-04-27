
    
##  *Test Suits for LDES Server to conformance the [LDES SPEC](https://semiceu.github.io/LinkedDataEventStreams/#biblio-rfc2119) and [TREE SPEC](https://treecg.github.io/specification/)*   
### Current test suits follows the scoring system as follows.  
 - 🟥 Must   (Pass - Score no change / Fail - Final score:0)  
> When the MUST-test fails, the server is considered non-conformant. The conformance score will be zero.    
 - 🟨 Should (Pass - Score + 10/ Fail - (Score - 10) / System Crash - Final score:0)  
> When the SHOULD tests fails, the tested LDES server can still conform to the recommendation. However, the conformance score will be impacted and the maintainer of the LDES server needs to consider alignment. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.    
 - 🟦 Optional (Pass - Score + 5 / Fail - (Score - 10) / System Crash - Final score:0)  
> A failing MAY-test does conformance but will result in a lower conformance score. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.  
  
### Test Suits:s
#### 🟥 Must - Test case  - Conformance point 1  

**Scenario**  : *Launch the LDES Server with `tree:view` configured*  
**Expected result**: *LDES Server does the fragment and provides a `tree:view` in the output LDES collection*

#### 🟥 Must - Test case: Launch LDES Server with `tree:view`, after processing by the LDES Server, each `tree:Node` has a link between current page to `tree:Collection`.  
> #Conformance point 3  
#### 🟨 Should - Test case: Launch LDES Server with  `SHACL shape` configured, all members of the collection are validated against the `SHACL` shape  
> #Conformance point 4  
#### 🟨 Should - Test case: Launch LDES Server with `Blank Node - Shacl Shape` configured, all members of the collection are validated against the SHACL shape  
> #Conformance point 5  
#### 🟦 Optional - Test case: Launch LDES Server with  `SHEx shape` configured, all members of the collection are validated against the ShEx shape  
> #Conformance point 6  
#### 🟥 Must - Test case: Launch LDES Server, verify that following the `treeNode` linked by `tree:view`, full LDES collection can be replicated. Amount of ingested entities = Ouput  
> #Conformance point 7  
#### 🟦 Optional - Test case: Launch LDES Server with several views ingested.  
> #Conformance point 8  
#### 🟥 Must - Test case: Following any `tree:Node` inside an LDES Server processed LDES Collection, the full collection can be replicated.  
> #Conformance point 9  
#### 🟥 Must - Test case: Launch LDES Server. Verify that in the LDES Server processed LDES collection, each `tree:Relation` has one `tree:node` object of the type `tree:Node`.  
> > #Conformance point 13