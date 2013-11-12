TO DO
=====
- use new ljd-utils.js
- Fix all html to be HTML 5
- Mark of the web?
- Exercise instructions
- Exercise answer CoffeeScript -> JavaScript
- Create `exam-and-exercise-answers` directory.  Contains exam 
  questions .txt with answers.  Also contains exercise answers.
  Put under git
- Shorten example (old example 1, now just example, because only 1)
- Remove Refactoring content (move to SWE 450)
- What about:  keep refactoring lesson only
  (help meet objectives? and test is still good)
- make a survey for 330/430 asking how many hours for each
    - learn javascript/qunit
    - lesson
    - example
    - exercise
    - exam
- jsfiddle.net codepen.io ???
- use HAML, SASS, and/or LESS?  Other templating?

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
  exam-and-exercise-answers dir, exam-and-exercises.zip
    - **Needed for teaching**

- Support:  SWE430-support.zip package-support.sh
(SWE430-support.zip goes on L drive, scripts on github)
package-support.sh
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
