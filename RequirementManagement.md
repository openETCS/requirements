This file is a proposal for the Requirement Management process. This has to be approved or completed by
the QA team.

The process may seems a little bit complex but it allows a unique referencing of requirements (which is necessary
for traceability).

The requirements are prefixed by “R-zz-x-y”, and are written in a roman typeface, where “R”
stands for “Requirement”, “zz” identifies the source document,“x” is the version number and“y”
is the identifier of the requirement. All the text written in italics is not a requirement: it may be a
note, an open issue, an explanation of the requirements, or an example.

When a document is currently under revision/writing process, the requirements are numbered using 
automatic counters and the version number is "X". When a version have to be released, a version 
number is chosen, and the requirement number is hardcoded in the document. This allows to have a unique identifier
for each requirement in the project.

In order for this process to be easy to apply, we use a combination of LaTeX macros and a helper script.

For the "in progress" document, we use macros 
\req{This is a requirement}
\subreq{This is a subrequirement}
\subsubreq{This is a subsubrequirement}

This appears in the pdf as 
R-docname-X-1 This is a requirement.
R-docname-X-1.1 This is a subrequirement}
R-docname-X-1.1.1 This is a subsubrequirement

Before issuing the document (for example for version 3), we run the script v_req.py 3 mydoc.tex mydoc-3.tex
This automatically transforms the document into :
\reqfixed{3}{1}This is a requirement}
\subreqfixed{3}{1}{1}{This is a subrequirement}
\subreqfixed{3}{1}{1}{1}{This is a subsubrequirement}

This appears in the pdf as 
R-docname-3-1 This is a requirement.
R-docname-3-1.1 This is a subrequirement}
R-docname-3-1.1.1 This is a subsubrequirement

Now if it is necessary to add or to modify a requirement, we use the \req{} macro that generate a new number without
collision.
