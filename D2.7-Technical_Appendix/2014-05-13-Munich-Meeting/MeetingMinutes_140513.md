Status: Draft  
Location DB-Netz, Völckerstrasse 5  
Date: 13.05.2014, 09:00 - 16:00  
Called By: Baseliyos Jacob, DB
Notes taken by: Bernd Hekele

* Participants 
 - Nicolas Boverie, Alstom
 - Frederique Vallee, All4Tec
 - Klaus-Ruediger Hase, DB
 - Baseliyos Jacob, DB
 - Bernd Hekele, DB
 - Peter Mahlmann, DB
 - Francisco Lozano, GE
 - Pierre-Yves Le Morvan, GE
 - Jan Welvaarts, LLRE
 - Marc Behrens, DLR
 - Uwe Eckelmann-Wendt, Siemens
 - Uwe Steinke, Siemens
 
You can find the slides used in the meeting in this location:
https://github.com/openETCS/requirements/tree/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting  

## Agenda:
 * 09:00 - 09:15 Welcome
 * 09:15 - 09:30 Meeting Minutes last meeting (10.4.14) and action items (Baseliyos)
 * 09:30 - 10:00 Status of API Requirements document (Baseliyos)
 * 10:00 - 10:30 Proposal for openETCS Abstraction Layer (Bernd/Uwe)
 * 10:30 - 10:45 Coffee Break
 * 10:45 - 12:15 Review comments sructured by owner od document (Nicolas)
 * 12:15 - 15:30 Technical Discussion of issues on Requirements Github
 * 15:30 - 16:00 Summary on Key decision / Action Items
 
## Minutes
### Welcome (KRH)
Start now to get a better structure, completion in context of next project  
Goals: Conclusion on the User Requirements (End-User = Organisation who operates the ETCS)  


### Meeting Minutes last Meeting
Action Items:  
You find the updated action items in the following location [Action Items](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/20140513_mom_2ndAPI_strategy%26review_Workshop.pdf).

The weekly follow-up meeting (Friday session) had to be cancelled (we need the slot for preparing the ITEA review). Instead we are now covering the API issues in the 10:45 - 11:00 slot (part of WP3).  

### API Requirement Document
Form not sufficient. E.g., requirements need to be identifiable. Document shall be continued on Github in Repository Requirements. The current version is to be sent out to revision.

### Application Layer Proposal
* Presentation [Bernd](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/openETCS-GenericAPI.pdf)
* Presentation [Uwe Steinke]()

The proposal has been discussed. The proposed structure (adaptation layer between a vender specific API and the Genric API of openETCS has been supported by most partners. The statement from Alstom is open (management level needed). 

WP3-leader will be contacted to be asked to  the issue on the agenda of the WP3 meeting.

The understanding of "generic" is not unique. Proposals like having a real generic and data-driven" have been discussed. Example ASN.1 or xml could be used define the data-model.  
Currently, Unisig does not deliver such descriptive files. openETCS could support them with this approach.
API could be abstract regarding the functions they are interfacing to.  
It is recommended to use the expertise from ERSA for the concept.  
Another point of discussion: How can we get a future proof implementation?
The poposal to support some sort of Stream of structures - not stream of bits in the interface has been supported.  
For the abstraction layer no standard will be provided but an example implementation  (either with ERSA as vendor or with Alstom as a vendor), Both functions are required in openETCS.

Principles of openETCS API form shall be agreed on in the project in a technical meeting.

Conclusion on API Layer after presentation.
 - Abstraction Layer  page 6
 - openETCS API comes out of the modelling work, support from suppliers needed
 - ERSA should be involved to generate the openETCS API
 - GE - Alstom API alone cannot be the basis. GE supports common API approach.
 - Question: confirmation for the proposal given?
 - GE: Yes, red-line. Support depends on availability of resources
 - Alstom: Important is the definition of the structures. No statement on Behalf of Alstom. 
 - WP3 workshop: put it on the agenda.
 - Siemens: agrees to the target to define the API.

### Walk thru review comments

More relaxed view because of generic API to be taken as working base. This API document is to be seen as a paper for the Alstom specific solution - only a guidance in openETCS. 

Proposal in Discussion - use a parameter to exchange the cycle-time via the init interface to make the application aware of the average range of cycle-time (latency).

Agreed proceeding: biliteral offline + escalation + Github schliessen wo klar.

WP4 presentation on Verification of the common API.

Issue: who will be responsible to provide the API. Alstom to answer.

All4Tec proposal for model-based testing.

 * tool is not open source
 * 

Proposal on Safety Architect.

 * tool is planned to be open source
 

