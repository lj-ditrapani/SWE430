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
- `generate_test_html.py`
- Copy files to locations with `create_dev_environments.py`
- # do work (modify markdown files, code examples, assignments) ...
- # Ready to teach class
- `create_zip_env.py` to zip up example and assignment environments
- `convert_markdown.py` to generate html files
- # Deploy
- `zip_website.py` -> SWE430.zip
- # Put SWE430.zip on blackboard
- # save FOUO stuff for future
- `zip_exam_and_assignment_answers.py`


WIP
====


TO DO
========================================================================

- Revise lessons (3)
    - Clarify references to examples/assignments (not exercises)
      as 430 only (because these will be shared with 330 students)
    - what about links:  could be confusing for 330 students
      either:
        - remove links
        - or create sepreate 330/430 versions (seperate links & titles).
- Discussion board questions
- Progress Check: review, include study guide (check 430 13A)?
- Choose content to cut-out of 330 and replace with new lessons (3)
- Video screen casts
- screen shots for environment tutorial
- Update 330 with better content?
- 330 DoDI 5000.02 curriculum update
- learning objective matrix update (objective 3)
- CUI prep (430 documentation on sharepoint)
- Missing jsbin for tutorials (remove or create one)

Tutorials

- Make javascript tutorial
- Update qunit jsbin to JavaScript
- Change CoffeeScript jsbin to JavaScript, update

Tutorial 2:  qUnit Tutorial

- qunit tutorial:  do we need throws or module stuff?

Tutorial 3:  Environment Instructions

- Add screenshots (console, debugger, jsbin)

Examples

- Work through both examples, step by step.  Fill-in prose.
- Work through both examples, step by step.  Time it.
- Make video screen cast for Example 1
- Make video screen cast for Example 2?
- Grab ideas from example 1.1, 1.2 and 2 from 430 13B

Assignments

- Work through all 3 assignments and time each.
- Make video screen cast for Assignment 1
- Explain type signatures?
- Put list of useful functions in each assignment instruction

Assignment 3

- Explain unicode \u2660 \n
- 335 LOC: 183 code, 152 test

- string manipulation functions; provide tutorial
- String.length, replace, slice() to get substring, indexOf to find
  substring
- slice() and indexOf() for "has 4 char substring" '4+ char substring'
- charCodeAt

Tools and scripts

- Combine `generate_test_html` and `create_dev_environments` into init
- Combine into deploy:
    - `convert_markdown.py`
    - `create_zip_env.py`
    - `zip_website.py`
    - `zip_exam_and_assignment_answers.py`
- Could write `check_html.js`
    - `check_html.bat` calls `check_html.js` which checks all html files
- convert jshint, jslint to py/batch
- Create ui.py to 1) init env and 2) deploy 3) lint check
- clean git ls-files

General TO DO

- Check SWE 430 13A offering discussion board and announcement, for
  info to include (questions, problems, ..)
- Delete or integrate extra files being ignored
    - Lib/check-html.sh
    - Lib/lint-ex1.sh
    - Lib/lint-ex2.sh

Low-priority

- Load code.js and test.js increments on the page 
    - When `convert_markdown.py` runs, transform special div tags into
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


BLACKBOARD
============

- content collection -> class name
- upload package -> SWE430.zip (overwrite)
- ensure folders have public read permission set
  or just link to a top level file?
- content collection -> class name -> click on permissions column for
  pertinent file
- Permit Anyone -> read only -> submit
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

- Build content -> File -> single link item (html, zip)
- Build content -> Item -> multi-link item + title [+ description]
        - very similar to new page...
- Assessment -> Test:  build an exam; can upload questions in one shot
using excel tab delimited ASCII text format

Assessment -> do unlimited attempts

- to grade -> grade center -> view grade details
- (top right 'v' in assignment box) clear attempt or ignore attempt



Objectives
==========

430
---
- Actively participates in online course activities.
* Assess the impact of decisions made in selecting construction tools
  and processes.
- Assess various sources for obtaining software artifacts.
* Detail software artifacts produced during and in support of
  construction.
* Analyze software construction artifacts for standards compliance and
  errors.
* Evaluate the conversion of low-level design artifacts into a software
  solution.
* Trace elements of a software solution to the design.
* Assess the effectiveness of unit and interface test cases.
* Analyze methods of improving software assurance.
* Identify steps involved in construction and debugging processes

330
---
- Actively participates in online course activities.
- Assess the impact of decisions made in selecting construction tools
  and processes.
- Evaluate various sources for obtaining software artifacts.
- Describe software artifacts produced during and in support of
  construction.
- Trace elements of constructed software to requirements.
- Define characteristics of a productive development environment.
- Assess software assurance characteristics of artifacts developed in
  software construction.
- Assess options to mitigate risks associated with transitioning beyond
  the construction phase
 

