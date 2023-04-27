

### The current folder contains two parts of the conformance testing.

 - [Conformance Testing framework](./TreeSpecConformancePoints.md)
   contains all testing points for an implementation of LDES Server to conform to the [Tree
   Specification](https://treecg.github.io/specification/) 
   The test points are categorized to:
	 - [🟥 Must](./TreeSpecConformancePoints.md#the-tree-specification-must-) 
		 - When the MUST-test fails, the server is considered non-conformant. The conformance score will be zero.
	 - [🟨 Should](./TreeSpecConformancePoints.md#the-tree-specification-should-)
		 - When the SHOULD tests fails, the tested LDES server can still conform to the recommendation. However, the conformance score will be impacted and the maintainer of the LDES server needs to consider alignment. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.
	 - [🟦 Optional](./TreeSpecConformancePoints.md#the-tree-specification-optional-)
		 - A failing MAY-test does conformance but will result in a lower conformance score. The only strict requirement is that the server handles the test gracefully. Failure to do so will result in non-conformance.
 - [Tree Specification Test Plan](./TreeSpecTestPlan.md) specifies down to the implementation and configurations, which contains the test cases for
	 - [LDES Server](./TreeSpecTestPlan.md#ldes-server-test-plan)
    The test cases cover the test points documented in [Conformance Testing framework](./TreeSpecConformancePoints.md)


#### Potential reference:

[Linked Data Platform 1.0 Test Cases](https://dvcs.w3.org/hg/ldpwg/raw-file/tip/tests/ldp-testsuite.html#test-case-description)
