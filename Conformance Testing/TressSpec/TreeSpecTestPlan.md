

##  ❗️ ❗️ The following test plan can be considered as a test suit, which needs to be executed for each supporting fragment: ❗️ ❗

 - [ ] Geo-based fragment 
 - [ ] Substring fragment 
 - [ ] Time-based fragment
 - [ ] Pagination fragment
 
## 🌈 LDES Server Test Plan
#### Test case 1 : 
#####  1.	Launch LDES Server with Single Fragment,  `tree:path` configured. Verify the following points:
a.	[1.2.1](./TreeSpecConformancePoints.md#121-when-the-current-page-is-a-treenode-there-must-be-a-property-linking-the-current-page-url-to-the-uri-of-the-treecollection) 
b.	[1.3.1](./TreeSpecConformancePoints.md#131-a-treerelation-must-have-one-treenode-object-of-the-type-treenode)
c.	[1.3.2](./TreeSpecConformancePoints.md#132-the-result-of-the-evaluation-of-the-treepath-is-the-value-that-must-be-compared-to-the-treevalue)
d.	[1.3.4](./TreeSpecConformancePoints.md#134-when-the-only-type-given-for-a-certain-relation-is-treerelation-then-the-client-must-dereference-all-of-the-nodes)
e.	[1.3.5](./TreeSpecConformancePoints.md#135-the-strings-must-then-be-compared-according-to-case-sensitive-unicode-ordering)
f.	[1.3.6](./TreeSpecConformancePoints.md#136-when-using-treegeospatiallycontainsrelation-the-treepath-must-refer-to-a-literal-containing-a-wkt-string-such-as-geosparqlaswkt)
g.	[2.3.3](./TreeSpecConformancePoints.md#233-every-treerelation-should-have-a-treepath-indicating-the-path-from-the-member-to-the-object-on-which-the-treerelation-applies)

#### Test case 2 : 
##### 2.	Launch LDES Server with Single Fragment,  `tree:path` configured. Using relations such as `tree:LessThanRelation` or `tree:GreaterThanRelation`. The `tree:path`'s value set to `xsd:date` to Verify the following points:
a.	[2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)

####  Test case 3 : 
##### 3.	Launch LDES Server with Single Fragment, `tree:path` configured. Using relations such as `tree:LessThanRelation` or `tree:GreaterThanRelation`. The tree:path’s value is set to `xsd:dateTime` to Verify the following points:
a.	[2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)

####  Test case 4 : 
##### 4.	Launch LDES Server with Single Fragment, tree:path configured. Using relations such as `tree:LessThanRelation` or `tree:GreaterThanRelation`. The tree:path’s value is set to `xsd:dateTimeStamp` to Verify the following points:
a.	[2.3.5](./TreeSpecConformancePoints.md#235-when-using-relations-such-as-treelessthanrelation-or-treegreaterthanrelation-the-time-literals-need-to-be-compared-according-to-these-3-possible-data-types-xsddate-xsddatetime-or-xsddatetimestamp)

####  Test case 5:
##### 5.	Launch LDES Server with Single fragment configuration, with NO `tree:path` defined for the fragment. Some properties' `rdfs:range` is incompatible to be compared. Verify following points:
a.	[1.3.3](./TreeSpecConformancePoints.md#133-when-no-treepath-is-defined-the-treevalue-must-be-compared-to-all-members-triples-that-can-be-compared-to-the-treevalue-as-defined-by-the-type-of-the-relation-or-when-no-members-or-collection-are-defined-on-every-triple-in-the-page-when-due-to-rdfsrange-incompatibility-the-object-can%20not-be-compared-the-object-will-not-be-considered-for-comparison)
####  Test case 6: 
#####  6.	Launch LDES Server with Single Fragment configuration, with `tree:path` configured. `SHACL` shape is properly configured (Not a Blank Node). Verify the following points:
a.	[2.2.1](./TreeSpecConformancePoints.md#231-the-treerelations-treevalue-should-be-set)
####  Test case 7:
#####  7.	Launch LDES Server with Single Fragment configuration, with `tree:path` configured. SHACL shape is configured with a blank node. Verify the following points:
a.	[2.2.2](./TreeSpecConformancePoints.md#222-note-the-shape-can-be-a-blank-node-or-a-named-node-on-which-you-should-follow-your-nose-when-it-is-defined-at-a-different-http-url)
####  Test case 8:
#### 8.	Launch LDES Server with Single Fragment configuration, with `tree:path` configured. `tree:value` is accompanied by a data type. Verify the following points:
a.	[2.3.2](./TreeSpecConformancePoints.md#232-the-object-of-treevalue-should-be-accompanied-by-a-data-type-when-it-is-a-literal-value)
#### Test case 9:
#### 9.	Launch LDES Server with Single Fragment configuration, with `tree:path` configured. `tree:value` is Not accompanied by a data type. Verify the following points:
a.	[2.3.2](./TreeSpecConformancePoints.md#232-the-object-of-treevalue-should-be-accompanied-by-a-data-type-when-it-is-a-literal-value)
#### Test case 10:
#### 11.	Launch LDES Server with multi-`tree:view` configured. Verify the following points:
a.	[3.2.2](./TreeSpecConformancePoints.md#322-multiple-treeview-links-may-be-provided)

#### Test case 11:

#### 11.	Launch LDES Server with Single Fragment configuration, with `tree:path` configured. `ShEx` shape is properly configured (Not a Blank Node). Verify the following points:
a.	[3.2.3](./TreeSpecConformancePoints.md#323-note-for-compatibility-with-the-solid-specifications-a-shex-shape-may-also-be-given-see-the-chapter-on-compatibility-bellow)

#### Test case 12:
#### 12.	Launch LDES Server with Single Fragment configuration, with `tree:path` configured. The `Tree:Node` has more than ONE `tree:relation` property. Verify the following points:
a.	[3.3.1](./TreeSpecConformancePoints.md#331-a-treenode-element-may-have-one-or-more-treerelation-properties)

#### Test case 13:
#### 13.	Launch LDES Server with Single Fragment configuration, with `tree:path` configured. The `tree:remaining` Items is set in the ingesting stream or on the LDES server. Verify the following points:
a.	[3.3.4](./TreeSpecConformancePoints.md#334-every-treerelation-may-provide-a-treeremainingitems)

#### Test case 14:
#### 14.	Launch LDES Server with Single Fragment configuration, with `tree:path` configured. The `tree:import` is contained in the LDES stream which is ingested to the LDES Server. Verify the following points:
a.	[3.3.5](./TreeSpecConformancePoints.md#335-a-client-may-use-treeremainingitems-to-estimate-the-completeness-of-the-downloaded-elements-to-the-end-user)

#### Test case 15:
#### 15.	Launch LDES Server with Single Fragment configuration, with No `tree:member` configured. Verify the following points:
a.	[3.3.7](./TreeSpecConformancePoints.md#337-when-there-are-no-treemembers-andor-no-treecollection-defined-then-the-treepath-refers-to-a-pattern-that-can-start-from-every-triple-in-the-page)

## 🌈 LDES Client Test Plan (#TODO)
