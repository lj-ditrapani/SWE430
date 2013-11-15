TO DO
=====
- Ensure all files are set ff=dos
- Get markdown working
    - prettyprint
    - css/js file selection in building head
- Rewrite .sh scripts into python scripts
  (mostly zip, unzip, cp, and delete files)
    - Test with jython.
- Could write jshint and jslint launcher in python script?
    - `check_js.bat` calls `check_js.js` which checks all js files
- Exercise instructions
    - string manipulation functions; provide tutorial
    - consider splitting the project up into 2 segments?
    - Fix this sentence for new example code: "This is accomplished in the same way we export the target object which contains both the Target and the Grid classes in Example 1."
- use new ljd-utils.js
- Fix all html to be HTML 5
- Mark of the web?
- Shorten example (old example 1, now just example, because only 1)
- keep refactoring lesson
  (help meet objectives and test is still good)
- Remove references to refactoring example and exercise
- make a survey for 330/430 asking how many hours for each
    - learn javascript/qunit
    - lesson
    - example
    - exercise
    - exam
- jsfiddle.net codepen.io ???
- use HAML, SASS, and/or LESS?  Other templating?
- powershell has zip.exe and unzip.exe that work just like linux equiv

3 parts to project
-------------------

- Git project: (goes on github and a SWE430-source.zip on L drive)
  All source files (except FOUO stuff, 3rd party stuff, and media)
    - **Needed for dev**

- Release: website dir
    - zip-website.sh to create release SWE430.zip
    - put SWE430.zip on ditrapani.info/resources & L drive
    - This .zip file is loaded right on blackboard
    - .zip file contains everything but the FOUO stuff
    - **Needed for teaching**

- Exam and Exercise Answers, separate git project
  (goes on L drive, FOUO stuff)
    - exam-and-exercise-answers dir
    - zip-exam-and-exercise-answers.sh
    - exam-and-exercise-answers.zip
    - load-exercise-dependencies.sh  copy dependencies of
      exercise answers (exercis-tests.html, qunit.js, qunit.css)
      answers into exercise answer folders
    - **Needed for teaching**

- Support:  SWE430-support.zip zip-support.sh
(SWE430-support.zip goes on L drive, scripts on github)
zip-support.sh
    - for 3rd party libraries, .pdf, .png files
    - .gitignore support files
    - zip files into SWE430-support.zip and put on shared L drive and 
      served from ditrapani.info
    - media files (images, books, videos)
    - binary art sources (dia, gimp)
    - immutable libraries (qunit.js qunit.css)
    - **Needed for dev**


old notes
==========

Provide a web-based IDE to eliminate the use of notepad
Use smaller language (subset of coffeescript, scheme)



BLACKBOARD
============

content collection -> class name
upload package -> SWE430.zip (overwrite)
ensure folders have public read permission set
    or just link to a top level file?
content collection -> class name -> click on permissions column for pertinent file
Permit Anyone -> read only -> submit
    -> adds read permission to public group

Course copy
-----------
Packages and utilities -> course copy


Enroll user
-----------
Users and Group -> Users ->


Navigation menu
-------------
Top left + sign
    -> Tool link:  Announcements and Contacts (in type)
    -> content area:  everything else (emaxs, lessons, exercises, admin info)


Content Area
------------------
Build content -> File -> single link item (html, zip)
Build content -> Item -> multi-link item + title [+ description]
    very similar to new page...
Assessment -> Test:  build an exam; can upload questions in one shot using excel tab delimited ASCII text format

Assessment -> do unlimited attempts
    to grade -> grade center -> view grade details
    (top right 'v' in assignment box) clear attempt or ignore attempt
