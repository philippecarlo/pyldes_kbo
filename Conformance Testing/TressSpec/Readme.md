

### The current folder contains two parts of the conformance testing.

 - [Conformance Testing framework](./TreeSpecConformancePoints.md)
   contains all testing points to conform to the [Tree
   Specification](https://treecg.github.io/specification/) 
   The test points are categorized to:
	 - [🟥 Must](./TreeSpecConformancePoints.md#the-tree-specification-must-) 
		 - When the MUST situation is applied, the system MUST follow the recommendations. Otherwise, the system fails the SPEC.
	 - [🟨 Should](./TreeSpecConformancePoints.md#the-tree-specification-should-)
		 - When the SHOULD situation is applied, the system follows the recommendation. Otherwise, the choice needs to be re-evaluated.
	 - [🟦 Optional](./TreeSpecConformancePoints.md#the-tree-specification-optional-)
		 - When the MAY situation is applied, the system MUST NOT crash!
Three different levels.

 - [Tree Specification Test Plan](./TreeSpecTestPlan.md) specifies down to the implementation and configurations, which contains the test cases for
	 - [LDES Server](./TreeSpecTestPlan.md#ldes-server-test-plan)
	 - LDES Client (To Do)

    The test cases cover the test points documented in [Conformance Testing framework](./TreeSpecConformancePoints.md)


#### Potential reference:

[Linked Data Platform 1.0 Test Cases](https://dvcs.w3.org/hg/ldpwg/raw-file/tip/tests/ldp-testsuite.html#test-case-description)
