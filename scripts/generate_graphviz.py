#!/usr/bin/python
import json
import re
import sys
import time
import os
import shutil
import darpa_open_catalog as doc
from pprint import pprint

active_content_file = sys.argv[1]
data_dir = sys.argv[2]
build_dir = sys.argv[3]
darpa_links = sys.argv[4]
date = time.strftime("%Y-%m-%d", time.localtime())

nodes = {}
edges = {}

print """
Active content file: %s
Data directory: %s
Build directory: %s
""" % (active_content_file, data_dir, build_dir)

#print "Attempting to load %s" %  active_content_file
active_content = json.load(open(active_content_file))

for program in active_content:
  software_columns = []
  if program['Program File'] == "":
    print "ERROR: %s has no program details json file." % program_name
    sys.exit(1)
  else:
    #print "Attempting to load %s" %  program['Program File']
    program_details = json.load(open(data_dir + program['Program File']))

  #print " NODE " + program_details['Long Name']
  nodes[str(program_details['Long Name'])] = {'type':"program",'color':'blue','shape':'rect','label':str(program_details['Long Name'])}
  nodes[str(program_details['Program Manager'])] = {'type':"pm",'color':'blue','shape':'rect','label':str(program_details['Program Manager'])}
  edges[str(program_details['Long Name'])] = {str(program_details['Program Manager']):{}}
  

  # program_details['Description']
  # program_details['Program Manager']
  # program_details['Program Manager Email'])
  print "NODES -----------"
  pprint(nodes)
  print "EDGES -----------"
  pprint(edges) 
  print "\nDATA ----------"
  print "nodes:" + str(nodes)
  print "edges:" + str(edges)
  sys.exit(0)  
  ###### SOFTWARE
  if program['Software File'] != "":
    #print "Attempting to load %s" %  program['Software File']
    softwares = json.load(open(data_dir + program['Software File']))   
    for software in softwares:
      for column in software_columns:
          for team in software['Program Teams']:
            if team in pubs_exist:
              team += " <a href='#" + team + "' onclick='pubSearch(this)'>(publications)</a>"
          software['Software']
          elink = software['External Link']
          if re.search('^http',elink) and elink != "":
            if darpa_links == "darpalinks":
              lurl = "http://www.darpa.mil/External_Link.aspx?url=" + elink
            else:
              lurl = elink
          else:
            lurl = "unlinked"
            # unlinked

  ####### Publications
  if program['Pubs File'] != "":
    #print "Attempting to load %s" %  program['Pubs File']
    pubs = json.load(open(data_dir + program['Pubs File']))
    for pub in pubs:
      for team in pub['Program Teams']:
        fake = ''
        #nodes[team] = {'type':"team"}
      link = pub['Link']
      if re.search('^http',link) or re.search('^ftp',link):
        if darpa_links == "darpalinks":
          lurl = "http://www.darpa.mil/External_Link.aspx?url=" + link
        else:
          lurl = link
      else:
        lurl = "unlinked"
        # not a link





























































