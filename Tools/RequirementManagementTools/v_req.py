#!/usr/bin/env python

"""
Usage: v_req.py <version> <inputfile.tex> <outputfile.tex>

Description: this script allows to replace all the requirements and subrequirements in the document 
which are numbered automatically into a fixed numbered requirement. 

The script should be run on the file before releasing a version, in order for a requirement to keep 
its number in the subsequent life of the document. When an existing fixed requirement is modified, it 
is mandatory to recreate a new number by using the non fixed requirement macros, until the official 
version release. 

Ex:
	v_req.py 3 proto_req.py	proto_req-3.py
"""

s_req = r'\req{'
s_subreq = r'\subreq{'
s_subsubreq = r'\subsubreq{'

s_rep_req = r'\reqfixed{%02d}{%03d}{'
s_rep_subreq = r'\subreqfixed{%02d}{%03d}{%02d}{'
s_rep_subsubreq = r'\subsubreqfixed{%02d}{%03d}{%02d}{%02d}{'

import sys

def reqnumber(version,infile,outfile):
	req_num = 0
	subreq_num = 0
	subsubreq_num = 0
	
	for line in infile:
		if line.find(s_req) != -1:
			req_num += 1
			subreq_num = 0
			subsubreq_num = 0
			s_replace = s_rep_req % (version,req_num,)
			out_line = line.replace(s_req,s_replace)

		elif line.find(s_subreq) != -1:
			subreq_num += 1
			subsubreq_num = 0
			s_replace = s_rep_subreq % (version,req_num,subreq_num)
			out_line = line.replace(s_subreq,s_replace)

		elif line.find(s_subsubreq) != -1:
			subsubreq_num += 1
			s_replace = s_rep_subsubreq % (version,req_num,subreq_num,subsubreq_num)
			out_line = line.replace(s_subsubreq,s_replace)			
		else:
			out_line = line

		outfile.write(out_line)
			
if __name__ == '__main__':
	version = int(sys.argv[1])
	infile = open(sys.argv[2])
	outfile = open(sys.argv[3],"w")
	reqnumber(version,infile,outfile)
	
	
	
	