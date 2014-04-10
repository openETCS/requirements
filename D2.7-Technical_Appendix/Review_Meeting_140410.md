* Location DB-Netz, Völckerstrasse 5
* Date: 10.04.2014, 09:00 - 

* Participants 
 - Klaus-Ruediger Hase
 - Baseliyos Jacob, DB
 - Bernd Hekele, DB
 - Peter Mahlmann, DB
 - Nicolas Boverie, Alstom
 - Niklas Schaffrath, Siemens
 - Uwe Steinke, Siemens
 - Vincent Hache, GE
 - Eric Schellenberg, ERSA
 - Didier Weckmann, ERSA
 - Jan Welvaarts LLRE
 - Marc Behrens, DLR
 
1. Introduction (Baseliyos)  
Alstom openETCS API is starting point for openETCS Developement.
The API has to be designed in a way that it is generic to work with other Hardware. 
The API has to be future-proof.
The API is currently used by Baseline 3 Alstom developement of Onboard Platform.
 
GE started a SysML model on the API as a part of WP5 activities. Exchange of the information will be organised in a meeting (Bernd to organise)

Conditions: to be discussed with new WP3 lead ()
 WP3 will model the API in SysML (accepted under condition)

Commercial Requirements: openETCS API is planned to be used in future tenders in the railway sector.
Discussion on "Stability of the interfaces".
Target: it has to upward compatible.
Example: odometry information is part of the Balise interface in the current implementation. The example shows dependency on the chosen solution. 

Additional Requirements: the openETCS API has to be open for other products. (Check wording)

Hardware and Communication Channels slide:
Alstom has reasons to have both types of interfaces (telegrams with e.g., JRU and DMI, Variables in Odometry).
Conclusion: ?

Performance Requirements

To be clarified: Commitment of the partners to contribute to WP3/API-work (GE, ERSA, Siemens) to be confirmed within 2 weeks??

API-Requirements (Performance + Commercial + ...) to be designed in a new document, Action will be driven by Baseliyos.
Deadline: 1 month. Part of WP2. 

2. Report on Document by partners.
Alstom: had a look at comments on Github.
ERSA: on Github
GE: on Github. In addition split between Application SW and Basic SW  is to be defined more precisely. 
WP4: Page 134 - technical question on filter
Siemens: on Github + Slides (e.g., Order of messages according to time, open)
Niklas slides. Software technology - more general ways requested. Should be less concrete and more general. Details then are for implementation level. Option: use a buffer concept or dynamic I/O system.

Proposal for continuation (Siemens): Define System Archtiecture and Provide more generic API definition interface for interface.

Decision not possible because of commitment of resources are not available.
Plan: wait until resource commitment is available.

WP3 will continue with modelling. In addition, the basis for the architecture in SysML will be put more focus on.
A later decision on differences in the API have to be later considered in the modelling work.

