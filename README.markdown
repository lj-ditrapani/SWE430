WIP
====

example 1

TO DO
========================================================================

Lessons

- Add javascript style standards to lesson 1

DBQ

- Add discussion board questions for interaction with managers

Tutorials

- Make javascript tutorial
- Grab tutorial (and lessons) from 499 course and integrate into
  Lesson 1 and 2
- string manipulation functions; provide tutorial
- function, function parameters & return
- function definition vs function calling
- var declaration
- comparisons `> < >= <= ===`
- not (!) operator
- for loop (i & sequence length)
- array and array indexing, push, .length
- bool, num, string, array, object

Instructions

- Grab instructions from 499 course and update 430 instructions

Examples

- Give checkpoints in the examples (complete code so far) so students
  know where they are
- New examples (1 and 2)
- ex 1 is write code against finished tests
- ex 2 is full-blow TDD
- Make video screen cast for Example 1
- Make video screen cast for Example 2?
- Grab ideas from example 1.1, 1.2 and 2 from 430 13B

Assignments

- fix shell scripts too for exam-and-assignment-answers project to use
  assigment instead of exercise 

Assignment 3

- string manipulation functions; provide tutorial
- consider splitting the project up into 2 segments?
- Fix this sentence for new example code: "This is accomplished in
  the same way we export the target object which contains both the
  Target and the Grid classes in Example 1."
- 335 LOC: 183 code, 152 test

- String.length, replace, slice() to get substring, indexOf to find
  substring
- slice() and indexOf() for "has 4 char substring" '4+ char substring'
- charCodeAt
- regex /[a-z]/ /[^a-z]/

Tools and scripts

- Fix `Lib/zip_website.py` 
  does not generate valid zip file with jython, but ok with cpython
  see `zip_website_error.txt`
- Rewrite .sh scripts into python scripts, put in Lib
  (mostly zip, unzip, cp, and delete files)
    - Test with jython.
- shell scripts to convert to python and put under Lib:
    - load-exercise-answers-dependencies.sh
    - zip-student-evironments.sh
    - zip-support.sh
    - zip-tool.sh
- Update packaging scripts (additional support libs; see .gitignore)
- integrate studend-dev-tools/generate.py into batch file ...
    - generate everytime you do something (part of convertmarkdown.bat?)
    - generate once in a pre-dev set-up script
- use new ljd-utils.js (no need so far...used in old example1.1)
- Could write jshint and jslint launcher in python script?
    - `check_js.bat` calls `check_js.js` which checks all js files
- jsfiddle.net codepen.io ???
- use HAML, SASS, and/or LESS?  Other templating?
- git rm pyunziptest.py once unzipping scripts complete
- convert jshint, jslint to py/batch
- convert-markdown.bat integrate into ui.py?
- clean git ls-files

General TO DO

- Check SWE 430 13A offering discussion board and announcement, for
  info to include (questions, problems, ..)
- Ensure all files are set ff=dos
- Remove references to refactoring example and exercise
- make a survey for 330/430 asking how many hours for each
    - learn javascript/qunit
    - lesson
    - example
    - assignment
    - exam
- Delete or integrate extra files being ignored
    - art
    - coffeescript-windows
    - `possible_roman_decimal.js`
    - website/old-example1


4 parts to project
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

- Exam and Assignment Answers, separate git project
  (goes on L drive, FOUO stuff)
    - exam-and-assignment-answers dir
    - zip-exam-and-assignment-answers.sh
    - exam-and-assignment-answers.zip
    - load-assignment-dependencies.sh  copy dependencies of
      assignment answers (exercis-tests.html, qunit.js, qunit.css)
      answers into assignment answer folders
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
content collection -> class name -> click on permissions column for
pertinent file
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
    - Tool link:  Announcements and Contacts (in type)
    - content area:  everything else (emaxs, lessons, assignments,
      admin info)


Content Area
------------------
Build content -> File -> single link item (html, zip)
Build content -> Item -> multi-link item + title [+ description]
    very similar to new page...
Assessment -> Test:  build an exam; can upload questions in one shot
using excel tab delimited ASCII text format

Assessment -> do unlimited attempts
    to grade -> grade center -> view grade details
    (top right 'v' in assignment box) clear attempt or ignore attempt
