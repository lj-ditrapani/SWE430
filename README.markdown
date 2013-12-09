4 parts to project
========================================================================

- Git project: on github and SWE430-source.zip from github on L drive
  All source files (except FOUO stuff, 3rd party stuff, and media)
    - **Needed for dev**

- Release: website dir
    - `zip_website.py` to create release SWE430.zip
    - put SWE430.zip on ditrapani.info/resources & L drive
    - This .zip file is loaded right on blackboard
    - .zip file contains everything but the FOUO stuff
    - **Needed for teaching**

- Exam and Assignment Answers, separate git project
  (goes on L drive, FOUO stuff, ONLY answers)
    - assignment1/test.js sourced from website/assignment1
    - exam-and-assignment-answers dir
    - `zip_exam_and_assignment_answers.py`
    - exam-and-assignment-answers.zip
    - `create_dev_environments.py`  copy dependencies of
      assignment answers (exercis-tests.html, qunit.js, qunit.css)
      answers into assignment answer folders
    - **Needed for teaching**
    - **Needed for dev**

- Support:  SWE430-support.zip `zip_support.py`
  (SWE430-support.zip goes on L drive, script on github)
  `zip_support.py`
    - support files added to .gitignore 
    - zip files into SWE430-support.zip and put on shared L drive and 
      served from ditrapani.info
    - for 3rd party libraries, .pdf, .png files
    - media files (images, books, videos)
    - binary art sources (dia, gimp)
    - immutable libraries (qunit.js qunit.css)
    - **Needed for dev**


Flow
=====

- Get and unzip `SWE430-support.zip`
- Get and unzip `SWE430-exam-and-assignment-answers.zip`
- `generatetesthtml.py`
- Copy files to locations with `create_dev_environments.py`
- # do work (modify markdown files, code examples, assignments) ...
- # Ready to teach class
- `create_zip_env.py` to zip up example and assignment environments
- `convertmarkdown.py` to generate html files
- # Deploy
- `zip_website.py` -> SWE430.zip
- # Put SWE430.zip on blackboard
- # save FOUO stuff for future
- `zip_exam_and_assignment_answers.py`


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
- qunit tutorial:  do we need throws or module stuff?
- Update qunit jsbin to JavaScript
- Change CoffeeScript jsbin to JavaScript

Instructions

- Grab instructions from 499 course and update 430 instructions

Examples

- Give checkpoints in the examples (complete code so far) so students
  know where they are.
  Provide links to e.g. code01.js code02.js code03.js ...
- New examples (1 and 2)
- ex 1 is write code against finished tests
- ex 2 is full-blow TDD
- Make video screen cast for Example 1
- Make video screen cast for Assignment 1
- Make video screen cast for Example 2?
- Grab ideas from example 1.1, 1.2 and 2 from 430 13B

Assignments

- Explain type signatures?

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

- Combine `generatetesthtml` and `create_dev_environments` into init
- Combine into deploy:
    - `create_zip_env.py`
    - `convertmarkdown.py`
    - `zip_website.py`
    - `zip_exam_and_assignment_answers.py`
- Delete ljd-utils.js???
- Could write `check_html.js`
    - `check_html.bat` calls `check_html.js` which checks all html files
- convert jshint, jslint to py/batch
- Create ui.py to 1) init env and 2) deploy 3) lint check
- clean git ls-files
- Update jsbins

General TO DO

- Check SWE 430 13A offering discussion board and announcement, for
  info to include (questions, problems, ..)
- Ensure all files are set ff=dos
- Remove references to refactoring example and exercise
- Delete or integrate extra files being ignored
    - Lib/check-html.sh
    - `possible_roman_decimal.js`
    - website/old-example1

Low-priority

- Load code.js and test.js increments on the page 
    - When convertmarkdown.py runs, transform special div tags into
      container with code, prettyprint, make invisible, and provide
      "show code" button.
- Provide "run tests" button for each "show code" button to run the
  actual tests
- jsfiddle.net codepen.io ???
- use HAML, SASS, and/or LESS?  Other templating?
- make a survey for 330/430 asking how many hours for each
    - learn javascript/qunit
    - lesson
    - example
    - assignment
    - exam



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
