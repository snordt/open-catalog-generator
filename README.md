open-catalog-generator
======================

Code and templates required to build the DARPA open catalog.

basic structure
=========================

- The Open Catalog website is generated by Python scripts which draw information from JSON files.

- The Python scripts that generate the site are located under the scripts folder, the most important being **generate_html.py**.

- All of the information about the projects are from JSON files that are located in the **darpa\_open\_catalog** folder (which is a separate repository on Github).

- There are three main types of JSON files, **pubs**, **program**, and **software**. The basic naming structure is to have the name of the DARPA Program such as XDATA and then a dash followed by one of the three keywords mentioned above. An example of this is **XDATA-software.json**.

- **pubs** JSON files contain information about the references (APA/MLA/etc) program teams have used for their projects.

- **software** JSON files contain information about any software that has been developed in the program/that will be listed in the catalog.

- **program** JSON files contain information about the DARPA Program itself.

- There are two special JSON files, **active\_content.json** and **active\_content\_deployed.json**. Both files list all the active programs inside of the open catalog, but the difference, is that the deployed file only lists programs that will appear on the DARPA website. Basically, the **active\_content\_deployed.json** file is a subset of the **active\_content**.json file.

open catalog updates
=========================

- New and updated data is typically sent and entered in by the performers, although it must be checked to ensure that it follows a proper format.

- Data is sent in many forms such as Excel Spreadsheets, word documents, and JSON files that don’t follow the catalog’s schemas. Performer data must be transformed to fit the schemas used by the three different types of JSON files.

- There are scripts located in the **transforms** folder to help transform the data into a properly formatted JSON file, the most important is **transform\_into\_JSON.py**. There is a readme inside of the folder that includes instructions for use.

- There are scripts located in the **scripts** folder and **test** folder that can help test/check the data. For instance, there is a script called **test_urls.py** inside the **test** folder which checks if the URLs included in the JSON files work.

makefile/build process
=========================

- The catalog uses a **Makefile** to easily run scripts and build the website. Most important functions of the open catalog generator can be called with a single make command.

- Running the command “**Make datainit**” will bring a current version of all open catalog JSON files into the directory, this command must be used to ensure that all information is current.

- Running the command “**Make**” will generate a version of the website which includes normal hyperlinks and all active content.

- Running the command “**Make deploy**” will generate a version of the website that will be deployed on DARPA’s website.

add_json_fields.py
=========================
Prerequesites - Cygwin installation includes the following packages: json, re, sys, time, os, shutil, pprint, collections. If these packages are not installed, install them through Cygwin setup executable.
Steps for adding json fields to a specific file type:

1. Open the json file for the program that needs to be added or modified. Add a blank("") entry to the program json for both the "Display Software Columns" and "Display Pubs Columns" fields. See the following example:

    "Display Software Columns":[
        "Team",
        "Project",
		"",
        "Category",
        "Code",
        "Description",
        "License"
    ],
    "Display Pubs Columns":[
        "Team",
        "Title",
		"",
        "Link"
    ],

2. From the scripts directory, open the add_json_fields.py script in an editor. 

3. There are three parameters that need to be passed into the make script:
  3a. file_types: This parameter should contain only the type(s) of files that you wish to add fields to. Valid values are "office", "program", "software" and "pubs"
  3b. new_fields: This parameter is a key-value pair object that takes the field name as the key and the field value as the value. There is no limit to the number of key-value pairs that can be added.
  3c. insert_after: The added field(s) will be placed after the given field name. The given field name can also be left empty "", which by default appends the added fields to the end of the json object 
  
4. The Makefile contains an executable definition that can be used to quickly run this script. Using the CYGWIN command line, run the following command with NO SPACES between commas:

	make addfields FILE_TYPES="file_type1" NEW_FIELDS="field1:value1,field2:value2" INSERT_AFTER="field_name"
	e.g. make addfields FILE_TYPES="pubs,software" NEW_FIELDS="Test 1:pass,Test 2:fail,Test Options:[pass,fail]" INSERT_AFTER="Program Teams"

5. Verify that the fields were added correctly and to the appropriate files by reviewing the new files in the "darpa_open_catalog/new_json" directory. If the files are correct, move them to the "darpa_open_catalog" directory and done! Now there are new json files for the next build!

6. Be sure to delete the "new_json" directory from the "darpa_open_catalog" directory so that it is not mistakenly committed to the project repository. 

Note: The json files that are reproduced are based on the active_content.json file. Be sure to add all of the json files that are to be reproduced to the active_content.json file before running the addjsonfields script.


convert_non_ascii_chars.py
=========================
Prerequesites - Cygwin installation includes the following packages: json, re, sys, unicodedata, binascii, chardet. If these packages are not installed, install them through Cygwin setup executable.
Steps for converting/removing non-ascii characters from json files:

1. In the "darpa_open_catalog" directory, record the name of the file(s) that include non-ascii characters in order to use them as parameters in the script. 
 
2. The Makefile contains an executable definition that can be used to quickly run this script after modifying the variable. Using the CYGWIN command line, run the following command with NO SPACES between the filenames:
   
   make fileascii FILES="filename1,filename2,filename3"
   e.g. make fileascii FILES="CRASH-program.json,CRASH-pubs.json"

3. Verify that the non-ascii characters were replaced/removed by opening the new files in the "darpa_open_catalog/new_json" directory. If the files are correct, move them to the "darpa_open_catalog" directory and done! Now there are new json files for the next build!

4. Be sure to delete the "new_json" directory from the "darpa_open_catalog" directory so that it is not mistakenly committed to the project repository. 

Note: In some cases, a non-ascii character may not be mapped to an ascii character, therefore causing the character to be replaced with another non-ascii character or removed completely. If the character needs an ascii equivalent, an exception will need to be added to the "hex2ascii" method in the script to identify an ascii character to replace the character.

  def hex2ascii(hex):
    uni_num = int(hex,16)
    #print "uni_num: %s \r" % uni_num 
    if uni_num > 127:
      if uni_num == 8243:
        char_out = '"'
		.
		.
		.
		
		
Adding tabs to the program page
================================
All json files named below are contained in the open-catalog-generator/darpa_open_catalog/ directory.
All py files named below are contained in the open-catalog-generator/scripts/ directory.
for example purposes, lets name the new tab "Examples"

1. Create a json file in the "darpa_open_catalog" directory for every program page that will be displaying the new tab. 

		`* XDATA-examples.json would be created for the XDATA program, MADCAT-examples.json for the MADCAT program...`
 
2. Update the active_content.json and active_content_deployed.json to include the new examples.json file for each program.

		```javascript	
		{
				"DARPA Office": "I2O",
				"Program Name": "XDATA",
				"Program File": "XDATA-program.json",
				"Pubs File": "XDATA-pubs.json",
				"Software File": "XDATA-software.json",
				"Data File": "XDATA-data.json",
				**"Examples File": "XDATA-examples.json", **
				"Banner":"UPDATED"
		}
		```

3. Add the new tab schema to file 00-schema-examples.json. The schema represents the json objects field names and values.

		```javascript
		{
			"Type":"Examples",
			"Schema":[
				{
					...
				}
			]
		}
		```
		
4. Now that we know the column names from the Examples tab schema, we can choose which columns to display in the tab. 
   Update the display fields in the program schema of file 00-schema-examples.json(line ~25). 
   
		```javascript
		"Display Examples Columns":[
			   ...
		  ],
		```
		
5. Open generate_html.py. You will need to make several modifications to this file.

	a. At the beginning of the program for loop (line ~79), a new column array will need to be declared.
	
			``` examples_columns = [] ```
	   
	b. A description will need to be added for the new tab. You will find the tab descriptions listed in the first else statement(line ~120)
	
			```python
			if program['Examples File'] and not program['Examples File'].isspace():	  
				program_page += "<ul><li>The Examples Table...</li></ul>"
			```  
			
	c. Define the column array for the new tab at the end of the first else statement(line ~147)	   
	
			``` examples_columns = program_details['Display Examples Columns'] ```

	d. Create html for the Examples tab of each program that has an examples.json file(line ~170). Always increment the previous tab id by 1 to get the new tab id.
	
			```python
			if program['Examples File'] != "":
				 program_page += "<li><a href='#tabs3'>Examples</a></li>"
				 search_tab += "<div id='exSearch'><div id='exTable'><h2>Examples</h2></div></div>"
			```	
			
	e. Create html for the content that will be on the Examples tab page similar to the Software, Pubs, and Data html(line ~188).
	
			```python
				if program['Examples File'] != "":
					program_page += "<div id='examples'><div id='tabs3'>"
					program_page += "<input class='search' placeholder='Search' id='search3'/>"
					program_page += "<button class='clear_button' id='clear3'>Clear</button>"
					try:
					  examples = json.load(open(data_dir + program['Examples File']))
					except Exception, e:
					  print "\nFAILED! JSON error in file %s" % program['Examples File']
					  print " Details: %s" % str(e)
					  sys.exit(1)
					program_page += doc.examples_table_header(examples_columns)
					for example in examples:
					  for column in examples_columns:
						...
						...
						...
					program_page += doc.table_footer()
					program_page += "</div></div>"
			```	
			
6. Open darpa_open_catalog.py. You will need to make several modifications to this file.

	a. Create a table header method for the Examples tab page(line ~116).
	
			```python
			def examples_table_header(columns):
				  header = "<table id='examples' class='tablesorter'>\n <thead>\n <tr>"
				  for column in columns:
					header += "<th>%s</th>" % column
				  header += "</tr>\n </thead>\n <tbody  class='list'>"
				  return header
			```
					  
	b. Two lists need to be declared in order to perform the tab search and the all(all-tab) search (line ~179).
	
			```javascript var swList = ssftList = pubList = spubList ... = exList = srchexList; ``` 			

	c. Define table sort by columns (line ~194)
	
			```javascript
			$('#examples').tablesorter({
				sortList: [[0,0],[1,0]]
			});
			```	
			
	d. Configure the Examples table search within the tabs for-loop (line ~252)
	
			```javascript
			if(tabName == "examples"){
				var tabTable = $('#tabs3 table'); //table within this tab
				var tabHeaders = getTableHeaders(tabTable);

				var ex_options = {
				  valueNames: tabHeaders
				};

				exList = new List(tabName, ex_options);

				$("#clear3").click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					exList.search();
				});

			}
			```
				
	e. Configure the Examples table for Search tab (line ~306)
	
			```javascript
			else if (table_clone[k].id == "examples"){
					$("#exSearch #exTable").append(table_clone[k]);
					$("#exSearch #exTable").hide();
					srchexList = new List("exSearch", search_options);
				}
			```	
			
	f. Activate clear button on the Search tab for the Examples table 
	
			```javascript
			$("#clear300").click(function() {
				var currId = this.id.match(/\d+/g);
				$("#search" + currId[0]).val("");
				//...
				if (srchexList != "")
					srchexList.search();
				//...
				$("#exSearch #exTable").hide();
			});
			```
			
	g. Create an Examples search function for searching content in the Examples table (line ~410)
	
			```javascript
			function exSearch(link){
				var search_text = "";
				if(link.hash)
					search_text = link.hash.replace("#", "");
				else
					search_text = link;
					
				$('#tabs').tabs({active: 3}); //examples tab
				var search_box = $("#search3");
				search_box.val(search_text);
				
				//...
			}
			```

	h. Activate tabs in the tabs table function (line ~214). It's important to represent the tab in each section of the if-else statement within this function. 
	
			```javaascript
			//...
			else if (param_tab == "tabs3")
				$("#tabs").tabs({active: 3});  //examples tab
			//...
			else if (param_tab == "tabs3")
					exSearch(param_term);
			//...	
			```
			
	i. Search value and set table for Examples on the all search tab (line ~471)
	
			```javascript
			//...			
			if(sdtList != ""){
				var value = this_search.value;
				sdtList.search(value);

				if ($("#dataSearch #dataTable tbody").children().length != 0)
					$("#dataSearch #dataTable").show();
				else
					$("#dataSearch #dataTable").hide();
			}
			//...
			else{
			//...
					$("#dataSearch #dataTable").hide();
			}
			```
   