---
layout: single
classes: wide
title: "Brandeis ACS Wrapper (v1)"
---
* Submitter: [keighrim](https://github.com/keighrim)
* Submission Time: 2023-06-06T00:30:33+00:00
* Prebuilt Container Image: [ghcr.io/clamsproject/app-brandeis-acs-wrapper:v1](https://github.com/clamsproject/app-brandeis-acs-wrapper/pkgs/container/app-brandeis-acs-wrapper/v1)


### Brandeis ACS Wrapper (v1) [metadata.json](metadata.json)
###### Brandeis Acoustic Classification & Segmentation (ACS) is a audio segmentation tool developed at Brandeis Lab for Linguistics and Computation. The original software can be found at https://github.com/brandeis-llc/acoustic-classification-segmentation .

* App ID: [http://apps.clams.ai/brandeis-acs-wrapper/v1](http://apps.clams.ai/brandeis-acs-wrapper/v1)
* App License: Apache2.0
* Source Repository: [https://github.com/clamsproject/app-brandeis-acs-wrapper](https://github.com/clamsproject/app-brandeis-acs-wrapper) ([source tree of the submitted version](https://github.com/clamsproject/app-brandeis-acs-wrapper/tree/v1))
* Analyzer Version: 1.11
* Analyzer License: Apache2.0


#### Inputs
* [http://mmif.clams.ai/vocabulary/AudioDocument/v1](http://mmif.clams.ai/vocabulary/AudioDocument/v1) (required)
###### ANY


#### Configurable Parameters
###### Multivalued parameters can have two or more values.

##### N/A


#### Outputs
###### Note that not all output annotations are always generated.
* [http://mmif.clams.ai/vocabulary/TimeFrame/v1](http://mmif.clams.ai/vocabulary/TimeFrame/v1) 
###### timeunit=milliseconds
