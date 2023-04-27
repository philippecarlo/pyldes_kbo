  
##  *Test Suits for LDES Server to conformance the [LDES SPEC](https://semiceu.github.io/LinkedDataEventStreams/#biblio-rfc2119) and [TREE SPEC](https://treecg.github.io/specification/)* 

### Current test suits follows the scoring system as follows.
 - 🟥 Must   (0/No change)
> When the MUST-test fails, the server is considered non-conformant. The conformance score will be zero.  
 - 🟨 Should (+10/-10/0)
> When the SHOULD tests fails, the tested LDES server can still conform to the recommendation. However, the conformance score will be impacted and the maintainer of the LDES server needs to consider alignment. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.  
 - 🟦 Optional (+5/-5/0)
> A failing MAY-test does conformance but will result in a lower conformance score. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.

### Test Suits:
####  🟥 Must   (0/No change) - Test case 1  : Launch LDES Server with `tree:view`. Verify that LDES Server does the fragment and provides a `tree:view`.
####  🟥 Must   (0/No change) - Test case 2 : Launch LDES Server with `tree:view`, after processing by the LDES Server, each `tree:Node` has a link between current page to `tree:Collection`.
####  #TODO 🟦 Optional (+5/-5/0) - Test case 3 : Launch LDES Server with `tree:view`, after processing by the LDES Server, each `tree:Node` has a link between current page to `tree:Collection`.
####  🟨 Should (+10/-10/0) - Test case 1  : Launch LDES Server with `SHACL shape`, verify that all members of the collection are validated against the `SHACL shape`.
