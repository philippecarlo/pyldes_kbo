# Questions
##### Should client also be part of the conformace testing? => Nope, the assumption is LDES Server interacts with a well functioned LDES Client
#### A TREE client MUST traverse all relations from the tree:Nodes linked to this particular collection. A client MUST thus check for ViewDescriptions on both the current node without the tree:viewDescription qualification, as on the current node with the tree:viewDescription link
#### A tree:Node can also be double typed as the tree:ViewDescription. A client must thus check for ViewDescriptions on both the current node without the tree:viewDescription qualification, as on the current node with the tree:viewDescription link.
#### When a `tree:path` is defined, mind that you also may have to check the language of the element using the property `shacl:inLanguage` More languages MAY be set. When no language is set, all strings are compared.*
> What does that imply? If you have a langauge that you only fragment for that langauge??