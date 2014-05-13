Status: Draft for review  
Location DB-Netz, Völckerstrasse 5  
Date: 13.05.2014, 09:00 - 16:00  
Called By: Baseliyos Jacob, DB
Notes taken by: Bernd Hekele

* Participants 
 - Klaus-Ruediger Hase, DB
 - Baseliyos Jacob, DB
 - Bernd Hekele, DB
 - Peter Mahlmann, DB
 - Nicolas Boverie, Alstom
 - Uwe Steinke, Siemens
 - Vincent Hache, GE
 - Jan Welvaarts LLRE
 - Marc Behrens, DLR
 
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
1. Document delivered.
2.  
3. 
4. 
5. 

No comment


### API Requirement Document
Form not sufficient. E.g., requirements need to be identifiable. Document shall be continued on Github in Repository Requirements. Prposal: Update the document D2.5 section 7. 

### Application Layer Proposal
* Presentation Bernd
* Presentation Uwe Steinke

What means Platform Independend?
Can we have an abstract and language independent implementation of the API? Example ASN.1 or xml?
Currently, Unisig does not deliver such descriptive files. But might do in future.
API could be abstract regarding the functions they are interfacing to.
<> Get expertise from ERSA for the concept <>

How can we get a future proof implementation?
Generic can mean data driven interfaces. 

Stream of structures - not stream of bits.

Also abstraction layer needs to be standardized. Platform independent part is something like providing Interface definitions. Responsibility lies with the vendor for the complete layer. platfrom indepenent and dependent blocks to be merged.

Principles of openETCS API form shall be agreed on in the project.

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

