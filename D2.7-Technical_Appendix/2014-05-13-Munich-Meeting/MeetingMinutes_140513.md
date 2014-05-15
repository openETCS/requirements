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
### Welcome (Klaus-Rüdiger)
Message: Start now to get a better structure, completion of the proposal might be in the context of next project.   
Goals: Conclusion on the User Requirements (End-User = Organisation who operates the ETCS)  

### Meeting Minutes last Meeting/Summary of actual Meeting (Baseliyos)
Action Items:  
You find the updated action items in the following location [Action Items](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/20140513_mom_2ndAPI_strategy%26review_Workshop.pdf).

The weekly follow-up meeting (Friday session) had to be cancelled (we need the slot for preparing the ITEA review). Instead we are now covering the API issues in the 10:45 - 11:00 slot (part of WP3).  

There is a need for a follow-up Meeting in roughly 4 weeks. Details to be clarified. A doodle will be sent to clarify the options.

### API Requirement Document (Baseliyos)
Form is not sufficient, e.g., requirements need to be identifiable. The [actual document](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/Bullit%20point%20openETCS%20requirements_20140511.pdf) is available on Github for revision.  
We will make a proposal on how the document will be aligned with the existing requirement documents. 

### Abstraction Layer Proposal
* Presentation [Bernd](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/openETCS-GenericAPI.pdf)
* Presentation [Uwe Steinke](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/WP3_API_AbstractionLayer.pdf)

The proposal has been discussed. The proposed structure (adaptation layer between a vender specific API and the Genric API of openETCS has been supported by most partners. The statement from Alstom is open (management level needed). 

WP3-leader will be contacted to be asked to  the issue on the agenda of the WP3 meeting.

The understanding of "generic" is not unique. Proposals like being real generic and "data-driven" have been discussed. For example, ASN.1 or xml could be used to define the data-model.  
Currently, Unisig does not deliver such descriptive files. openETCS could support them with this approach.
The API could be abstract regarding the functions they are interfacing to. Anyway, we need to get a future proof implementation.  
It is recommended to use the expertise from ERSA for the new concept.  
The poposal to support some sort of Stream of structures - not stream of bits in the interface has been supported.  
For the abstraction layer no standard will be provided but an example implementation  (either with ERSA as vendor or with Alstom as a vendor), both applications are part of the openETCS ITEA project.

Principles of openETCS API form shall be agreed on in the project in a technical meeting.

Conclusion on API Layer after presentation.
 - Basic was the Uwe's slide set, Abstraction Layer, page 6
 - openETCS API comes out of the modelling work, support from suppliers needed
 - ERSA should be involved to generate the openETCS API (AI Bernd)
 - GE - Alstom API alone cannot be the basis. GE supports common API approach.
 - Question: confirmation for the proposal given?
 - GE: Yes, red-line. Support depends on availability of resources
 - Alstom: Important is the definition of the structures. No statement on behalf of Alstom. Confirmation needed by WP3 leader. 
 - WP3 workshop: put it on the agenda.
 - Siemens: agrees to the target to define the API.

### Walk thru review comments (Nicolas)

Nicolas presented the summary of the review comments collected in the [xls-file](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/OETCS_API_review_2014_05_12.xlsx).  
Having had the agreement on the new architecture we now can have a little bit more relaxed view on the review . Design choices can be accepted if they can be reolved with the new architecture with the generic API to be taken as working base. This API document is to be seen as a paper for the Alstom specific solution - only a guidance in openETCS. 

Next steps with the comments are as follows:
The “normal” review process will go on.  
First, the reviewer has to react on the “answered” comments.  
If needed, there will be a discussion between me and each reviewer until we are sure to understand each-other.  
When the analysis is finished,  
- either there is an agreement -> modify or not the document.  
- or there is no agreement: then we bring the point to higher level  of decision.  
For the “Rejected” - “design choice” points :  
The owner (Nicolas) will ask to each reviewer to bring explicit evidences that the Alstom choice is an error and to bring explicit alternative solutions.  
Then we will see if we have to change the status to “accepted” or not.  

But it is true that, at the end of the review process between the auther and the reviewer, the outcome for “Rejected” - “design choice” is likely to be “no action”.

### WP4 presentation on Verification of the common API. (Marc)
Slides to be provided.

Issue: who will be responsible to provide the API. Alstom to answer.

### Tools for Verification (Frederique)

Proposal for [Model-Based Testing](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/A4T_Presentation%20A4Tv2.02-nosound-LD3.ppsx)  

Proposal for [Proposal on Safety Architect](https://github.com/openETCS/requirements/blob/master/D2.7-Technical_Appendix/2014-05-13-Munich-Meeting/Safety_Architect_OpenETCS.PDF)

 * Remarks: tool is planned to be open source
