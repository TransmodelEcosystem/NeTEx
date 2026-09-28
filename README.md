# NeTEx (Network Timetable EXchange) XML schema
**(C) 2009-2026 NeTEx, CEN, Crown Copyright**


## Overview 🔍

NeTEx is CEN Technical Specification (CEN/TS); it is published as a series referenced as CEN/TS 16614. It is dedicated to the exchange of scheduled data (network, timetable and fare information). It is based on Transmodel V6.2 (EN 12896 series) and SIRI (CEN/TS 15531-4/-5 and EN 15531-1/-2/-3) and supports the exchange of information of relevance for passenger information about public transport services and also for running Automated Vehicle Monitoring Systems (AVMS).

Although the data exchanges targeted by NeTEx are predominantly oriented towards provisioning passenger information systems and AVMS with data from public transport scheduling systems, it is not restricted to this purpose. NeTEx can also provide an effective solution to many other use cases for transport data exchange.

_Note : Many NeTEx concepts are taken directly from Transmodel. The definitions and explanation of these concepts are extracted directly from the respective standard and reused in NeTEx, sometimes with adaptions in order to fit the NeTEx context._

### Repository content 📚

This repository contains the XML Schemas (XSD) for:
- The core part of NeTEx
- NeTEx Part 1 (Network topology)
- NeTEx Part 2 (Scheduled Timetables)
- NeTEx Part 3 (Fare information)
- NeTEx Part 5 (Alternative modes )

### Respository structure 📁

In each branch, we have:
- The folder `xsd` in which all the XML schemas can be found,
- The folder `examples` in which all examples can be found,
- At the root folder, `NeTEx.spp` which is the project for XMLSpy and `NeTEx.xpr` for Oxygen.

The `xsd` folder is sub-divided as follow:
-  `gml` for all geometry-related elements,
- `netex_framework` for all shared components and frames,
- one sub-folder per NeTEx Part (from 1 to 5),
- other complementary sub-folders.
At the root of the `xsd` folder, the file `NeTEx_publication.xsd` should be used as the main one for production and validation purposes. It includes references to all the other XSD.

### Branches 🌿

| Branch Name | Description                                             | Maintenance status                                    | Link                                            |
| ----------- | ------------------------------------------------------- | ----------------------------------------------- |----------------------------------------------- 
| v2.0        | The last stable branch of the XML Schema, result of the NeTEx revision made during 2022-2026 | Bug fixes only | [Direct link](https://github.com/TransmodelEcosystem/NeTEx)    |
| v1.3        | The previous branch of the XML Schema that was published prior to the 2026 revision of NeTEx, it matches the state of the XSD at the date of the publication of Part 6 (CEN/TS 16614-6:2024) with the correction of bugs and typos -- **Important note**: this branch is not longer maintained | Not maintained | [Direct link](https://github.com/TransmodelEcosystem/NeTEx/tree/v1.3) |
| v2.1-wip    | All the upcoming work to improve v2.0     | In development   | [GitHub](https://github.com/TransmodelEcosystem/NeTEx/tree/v2.1-wip) |
| v3.0-wip    | All the upcoming work preparing the migration from CEN/TS to CEN/EN for the entire NeTEx series        | In development | [GitHub](https://github.com/TransmodelEcosystem/NeTEx/tree/v3.0-wip) |

All other branches are considered as feature branches, meaning that they are used for development only and are to be deleted once a Pull Request is merged. See below for more details on contributions.

**Important notes:** 
- Any branch marked `wip` is a non-stable branch.
- For a specific XML Schema matching a published CEN document, use `releases`.

----

## Getting started 🛠️

### Main root schemas 

1. **netex_publication.xsd**
   - Embeds NeTEx XML model elements in a bulk output file format for use in asynchronous publication.
   - The intended content scope can be indicated by a filter object.
   - It should be used as the main XSD for production and validation purposes.

Note: `netex_publication_noConstraint.xsd` is the same as `netex_publication.xsd` but without all the XSD constraints (e.g., unicity of attributes). It is convenient to speed up the work in development phases, but at the price of a much weaker validation.

2. **netex_siri.xsd**
   - Embeds NeTEx XML model elements in the SIRI protocol for dynamic exchange of elements between servers.
   - Supports both request/response and publish/subscribe.

3. **nx.xsd**
   - Embeds NeTeX XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx.
   - The NX schema is not intended for actual use.

### How to navigate the schemas

The schema is systematically divided into small modular files. Generally, for each functional package in the design model there are two XML schema files:

- **netex_xxxx_version.xsd**: Contains the definitions of each element or group,
- **netex_xxxx_suppport.xsd**: Contains the data type, reference structures and values for enumerations.

### XML examples

1. **Functions**

The folder contains snippets of XML files focused on a specific function or element of Public transport services (e.g., timetable, stop places, fares, etc.). They are meant to illustrate how to use NeTEx to model part of the public transport service.

2. **Standards**

The folder contains more comprehensive NeTEx files that aim to represent either an entire dataset as commonly found in other specifications, domains or Member States. They are meant to illustrate several parts of one public transport service. They should be used as an ensemble rather than single files.

----

## How to contribute 🖊️

### Starting a discussion 💬

Either for a modelling question or a request for change, please start a discussion using the [GitHub issues](https://github.com/TransmodelEcosystem/NeTEx/issues). 
In your issue, make sure that:
- The title is a clear summary of your question / requst for change,
- The content sufficiently details:
   - The context,
   - The elements / features you want to discuss,
- If relevant, include extracts of your NeTEx file.

### Making a change 🚀

1. Identify which branch you need to target:
   - v2.1-wip for all changes that will apply to NeTEx v2.0 (e.g., bug fixes, typos, improvement of certain features without breaking changes, etc.)
   - v3.0-wip for all changes that will apply when NeTEx migrates to EN (e.g., deprecation of features, refactor of certain elements, breaking changes including new features, etc.)
2. Create a feature branch with a clear name (e.g., bugfix_vehicletype)
3. Work on the changes and do the Pull Request

For new features, the decision between targetting v2.1-wip or v3.0-wip will be made by the group.

_Upcoming: templates for Pull Request_

### The use of AI in this repo 🤖

In this repository, the use of AI should follow these guidelines. The guiding principle is that any contributor is ultimately reponsible for their work on NeTEx and they should be the last reviewer of any AI-guided work before submitting it for peer-review; in other words, only contributors can be authors or co-authors of any change made to NeTEx.

AI **can** be used for:
- Generation of code for contributors to work on the XSD by themselves,
- Analysis of any change proposed to the XSD before it is edited / commented / approved,
- Improvements to the general language in the documentation (i.e, anything in `<xsd:annotation>` and `<xsd:documentation>`) or to check for typos in any work.

AI **cannot** be used for:
- Committing a change in a Pull Request, i.e. the AI agent cannot be an author or co-author of any commit,
- Authoring a change, i.e. the AI agent cannot be an author or co-author of any Pull Request,
- Automated code review as a stand alone action, i.e. the result of a review must be proof-read by a contributor,
- Produce documentation from scratch (i.e, anything in `<xsd:annotation>` and `<xsd:documentation>` should be proof-read by a contributor if it was suggested by AI).

In case you have a GitHub Pro account, please disable the feature `Automated Copilot code review` before contributing here.

----

## Changelog 📰

### Releases
| Release Number | Release Date  | Description                                    | Link          |
| -------------- | ------------- | ---------------------------------------------- | ------------- |
| v1.2            | March 2022    | Before the extension to alternative modes of operation | [Code](https://github.com/TransmodelEcosystem/NeTEx/releases/tag/v1.2)    |
| v1.2.2          | August 2023   | With the inclusion of NeTEx Part 5 (Alternative modes) | [Code](https://github.com/TransmodelEcosystem/NeTEx/releases/tag/v1.2.2)  |
| v1.2.3          | May 2024      | Improvement on the v1.2.2 before the release of NeTEx Part 6 (EPIAP) | [Code](https://github.com/TransmodelEcosystem/NeTEx/releases/tag/v1.2.3)  |
| v1.3.1          | May 2024      | Release of NeTex Part 6, the European Passenger Information Accessibility Profile (EPIAP) | [Code](https://github.com/TransmodelEcosystem/NeTEx/releases/tag/v1.3.1) |
| v2.0.0          | February 2026 | Matches the CEN documentation published in February 2026 for NeTEx Parts 1, 2, 3 and 5. Considered as the latest version of NeTEx to be used for production. | [Code](https://github.com/TransmodelEcosystem/NeTEx/releases/tag/v2.0.0) |

**Important notes:** 
- Releases (and their tags) are a snapshot of the corresponding working branch in time.
- For any official reference to a NeTEx version, it is recommended to point to a 2-digit version (e.g., v1.3, v2.0).
- For any development work, it is recommended to use the latest 3-digit version of NeTEx XML Schema.

### Comprehensive version history
The comprehensive versions history is available in [CHANGELOG.md](https://github.com/TransmodelEcosystem/NeTEx/blob/v2.0/CHANGELOG.md)
