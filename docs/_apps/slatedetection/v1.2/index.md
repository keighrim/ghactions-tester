---
layout: single
classes: wide
title: "Slate Detection (v1.2)"
---
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-17T11:25:34+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-slatedetection:v1.2](https://github.com/clamsproject/app-slatedetection/pkgs/container/app-slatedetection/v1.2)


### Slate Detection (v1.2) [metadata.json](metadata.json)
###### This tool detects slates.

* App ID: [http://apps.clams.ai/slatedetection/v1.2](http://apps.clams.ai/slatedetection/v1.2)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-slatedetection](https://github.com/clamsproject/app-slatedetection) ([source tree of the submitted version](https://github.com/clamsproject/app-slatedetection/tree/v1.2))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|timeUnit|Unit for output typeframe|string|N|frames|**_`frames`_**, `milliseconds`|
|sampleRatio|Frequency to sample frames.|integer|N|30||
|stopAt|Frame number to stop processing|integer|N|540000||
|stopAfterOne|When True, processing stops after first timeframe is found|boolean|N|1|`false`, `true`|
|minFrameCount|Minimum number of frames required for a timeframe to be included in the output|integer|N|10||
|threshold|Threshold from 0-1, lower accepts more potential slates.|number|N|0||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### properties={'frameType': 'string'}
