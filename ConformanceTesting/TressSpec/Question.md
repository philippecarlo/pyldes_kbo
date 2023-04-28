# Questions
##### *Should LDES Server support all fragments (Geo,Stringbased,timebased,paginating)? Must, Sould, or Optional*?
##### *Should Client also be part of the conformance testing*? 
>Nope, the assumption is LDES Server interacts with a well functioned LDES Client
##### *Should LDES Sever validate ingesting member before accepting it, or it is the job for Client to prune out the `Not valid` members*? 
#####  *Note: A tree:Node linked through tree:view can thus be used to _view_ all members of the collection, hence the name (this is similar in the Hydra specification).*
> Which name?
##### *A tree:Node can also be double typed as the tree:ViewDescription. A client must thus check for ViewDescriptions on both the current node without the tree:viewDescription qualification, as on the current node with the tree:viewDescription link.*
##### *When a `tree:path` is defined, mind that you also may have to check the language of the element using the property `shacl:inLanguage` More languages MAY be set. When no language is set, all strings are compared.*
> What does that imply? If you have a langauge that you only fragment for that langauge?