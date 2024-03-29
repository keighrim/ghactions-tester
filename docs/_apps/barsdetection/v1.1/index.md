---
layout: single
classes: wide
title: "Bars Detection (v1.1)"
---
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-07-31T23:31:12+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-barsdetection:v1.1](https://github.com/clamsproject/app-barsdetection/pkgs/container/app-barsdetection/v1.1)


### Bars Detection (v1.1) [metadata.json](metadata.json)
###### This tool detects SMPTE color bars.

* App ID: [http://apps.clams.ai/barsdetection/v1.1](http://apps.clams.ai/barsdetection/v1.1)
* App License: MIT
* Source Repository: [https://github.com/clamsproject/app-barsdetection](https://github.com/clamsproject/app-barsdetection) ([source tree of the submitted version](https://github.com/clamsproject/app-barsdetection/tree/v1.1))


#### Inputs
* [http://mmif.clams.ai/vocabulary/VideoDocument/v1](http://mmif.clams.ai/vocabulary/VideoDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

|Name|Description|Type|Multivalued|Default|Choices|
|----|-----------|----|-----------|-------|-------|
|timeUnit|Unit for output typeframe.|string|N|frames|**_`frames`_**, `seconds`, `milliseconds`|
|sampleRatio|Frequency to sample frames.|integer|N|30||
|stopAt|Frame number to stop processing.|integer|N|9000||
|stopAfterOne|When True, processing stops after first timeframe is found.|boolean|N|true|`false`, **_`true`_**|
|minFrameCount|minimum number of frames required for a timeframe to be included in the output.|integer|N|10||
|threshold|Threshold from 0-1, lower accepts more potential slates.|number|N|0.7||
|pretty|The JSON body of the HTTP response will be re-formatted with 2-space indentation|boolean|N|false|**_`false`_**, `true`|


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### typeSpecificProperty={'frameType': 'bars'}
