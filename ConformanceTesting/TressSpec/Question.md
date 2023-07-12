# Questions
##### *1 Should LDES Server support all fragments (Geo,Stringbased,timebased,paginating)? Must, Sould, or Optional*?
##### *2 Should Client also be part of the conformance testing*? 
>Nope, the assumption is LDES Server interacts with a well functioned LDES Client
##### *3 Should LDES Sever validate ingesting member before accepting it, or it is the job for Client to prune out the `Not valid` members*? 
##### *4 Note: A tree:Node linked through tree:view can thus be used to _view_ all members of the collection, hence the name (this is similar in the Hydra specification).*
> Which name?
##### *5 When a `tree:path` is defined, mind that you also may have to check the language of the element using the property `shacl:inLanguage` More languages MAY be set. When no language is set, all strings are compared.*
> What does that imply? If you have a langauge that you only fragment for that langauge?
##### *6 Is it possible ingest only `tree:value` not `tree:path` when configuring LDES Server?