TO DO
=====
- use new ljd-utils.js
- Fix all html to be HTML 5
- Mark of the web?
- Exercise instructions
- Exercise answer CoffeeScript -> JavaScript
- What about:  keep refactoring lesson only
  (help meet objectives? and test is still good)
- Create package-support.sh
    - for 3rd party libraries, .pdf, .png files
    - .gitignore support files
    - zip files into SWE430-support.zip and put on shared L drive and 
      served from ditrapani.info
    - media files (images, books, videos)
    - binary art sources (dia, gimp)
    - immutable libraries (qunit.js qunit.css)
- Create unpack-support.sh script to unzip support and place files in 
  correct directory
- Create `exam-and-exercise-answers` directory.  Contains exam 
  questions .txt with answers.  Also contains exercise answers.
  Put under git
- Shorten example (old example 1, now just example, because only 1)
- Remove Refactoring content (move to SWE 450)
- make a survey for 330/430 asking how many hours for each
    - learn javascript/qunit
    - lesson
    - example
    - exercise
    - exam
- jsfiddle.net codepen.io ???

3 parts to project
-------------------

Production: website dir (goes on github)
    - zip-website.sh to create release SWE430-website.zip
    - put SWE430-website.zip on ditrapani.info/resources & L drive
    - This .zip file is loaded right on blackboard
    - .zip file contains everything but the FOUO stuff

Exams/Answers, separte git project (goes on L drive, FOUO stuff)
exam-and-exercise-answers, zip-exam-and-exercise-answers.sh

support.zip package-support.sh unpack-support.sh
(support.zip goes on L drive, scripts on github)


old notes
==========

Provide a web-based IDE to eliminate the use of notepad
Use smaller language (subset of coffeescript, scheme)



BLACKBOARD
============

content collection -> class name
upload package -> website.zip (overwrite)
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
