Status: Draft for review  
Location DB-Netz, Völckerstrasse 5
Date: 10.04.2014, 09:00 - 16:00  
Notes taken by: Bernd Hekele

* Participants 
 - Klaus-Ruediger Hase, DB
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
 
You can find the slides used in the meeting in this location:
https://github.com/openETCS/requirements/tree/master/D2.7-Technical_Appendix/2014-04-12-Munich-Meeting  

1. Introduction (Baseliyos)  
Please, refer to the [slides](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-04-12-Munich-Meeting/20140410_API_Strategy%26Review_Workshop_3.pdf)  
Alstom openETCS API is starting point for openETCS Developement.
The API has to be designed in a way that it is generic to work with other Hardware. 
The API has to be future-proof.
The openETCS API proposal is actually in use in Alstom's Baseline 3 developement of ETCS. It is stable. It is under evolution since about 10 years. There are no major technical issues known with the chosen API solution. However, the design is close to the architecture chosen by Alstom.  
GE started a SysML model on the API as a part of WP5 activities. Exchange of the information will be organised in a meeting (Bernd to organise)  
WP3 started to provide a service view of the API in SysML (bottom-up). This work will be continued and extended with the analysis of the top-down approach.  
Conditions: to be discussed with new WP3 lead
WP3 will model the API in SysML (accepted under condition of confirmation by the WP3-leader to come)  
Commercial Requirements: openETCS API is planned to be used in future tenders in the railway sector.
Discussion on "Stability of the interfaces".
Target: the API  has to upward compatible and future-proof for at least 10 years to come.  
Example: odometry information is part of the Balise interface in the current implementation. The example shows dependency on the chosen solution.  
Additional Requirements: the openETCS API has to be open for other products, e.g., National Legecy systems.  
Hardware and Communication Channels slide:  
Alstom has reasons to have both types of interfaces (telegrams with e.g., JRU and DMI, Variables in Odometry).  
Performance Requirements  
To be clarified: Commitment of the partners to contribute to API-standardization work (GE, ERSA, Siemens) to be confirmed within 2 weeks (AI 4)  
API-Requirements (Performance + Commercial + ...) to be designed in a new document, Action will be driven by Baseliyos.
Deadline: 1 month. Part of WP2. (AI 2).   
2. Report on Document by partners.  
Alstom: had a look at comments on Github. Outstanding statements on technical issues will be delivered by April 18th. Github is to be used for documentation.  
ERSA: Findings are on Github  
GE: on Github. In addition split between Application SW and Basic SW  is to be defined more precisely. 
Siemens: on Github + [Slides](https://github.com/openETCS/requirements/tree/master/D2.7-Technical_Appendix/2014-04-12-Munich-Meeting) (e.g., Order of messages according to time, open)  
Software technology - more general ways requested. Should be less concrete and more general. Details then are for implementation level. Option: use a buffer concept or dynamic I/O system.  
Proposal for continuation (Siemens): Define System Archtiecture and Provide more generic API definition interface for interface.  
Decision not possible immediatly because of commitment of resources are not available (see AI 4).
Plan: wait until resource commitment is available. Answer by organisations expected by April 18th.  
Even after the work on the API redefinition is completed it can take some time until an updated version of the API is available.  
WP3 will continue with modelling. In addition, the basis for the architecture in SysML will be put more focus on.
A later decision on differences in the API have to be later considered in the modelling work.
We agreed on a follow-up meeting at about Mai 14th. The meeting will be aligned with a WP3 kick-off meeting for the new WP3 lead.  
The Summary of the findings can be found in this action [list](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-04-12-Munich-Meeting/20140410_mom_API_strategy%26review_Workshop.pdf) 
