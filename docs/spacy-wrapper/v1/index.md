
### CLAMS wrapper for spaCy NLP (v1)
###### Apply spaCy NLP to all text documents in a MMIF file.

* App ID: http://apps.clams.ai/spacy-wrapper/v1
* App License: Apache 2.0
* Source Repository: https://github.com/clamsproject/app-spacy-nlp
* Prebuilt Container Image: ghcr.io/clamsproject/app-spacy-wrapper:v1
* Analyzer Version: 3.1.2
* Analyzer License: MIT
#### Inputs
##### http://mmif.clams.ai/vocabulary/TextDocument/v1 (required)
###### 
##### http://vocab.lappsgrid.org/Token 
###### 
#### Configurable Parameters
Multivalued parameters can have two or more values.
|Name|Description|Type|Multivalued|Choices|
|----|-----------|----|-----------|-------|
|pretokenized|Boolean parameter to set the app to use existing tokenization, if available, for text documents for NLP processing. Useful to process ASR documents, for example.|boolean|False|**`false`** (*), `true`|
#### Outputs
Note that not all output annotations are always generated.
##### http://vocab.lappsgrid.org/Token 
###### 
##### http://vocab.lappsgrid.org/Token#pos 
###### 
##### http://vocab.lappsgrid.org/Token#lemma 
###### 
##### http://vocab.lappsgrid.org/NounChunk 
###### 
##### http://vocab.lappsgrid.org/Sentence 
###### 
##### http://vocab.lappsgrid.org/NamedEntity 
###### 
