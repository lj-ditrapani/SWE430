SWE 430 zip Instructions
========================================================================


The Local zip File Environment
------------------------------

The local zip environment is simply a zip file containing 6 files:  an html page, two javascript files, a CSS files, and two JavaScript files.

Contents of environment .zip file:

<dl>
    <dt>HTML file</dt>
    <dd>
    This page will display the results of all the unit tests you write in the JavaScript test file (test.js).  Refreshing the page will re-run all the tests (including any new tests you have added since the last run.)  You do not need to modify this file.  Simply open it in your web browser.
    </dd>
    <dt>qunit.js</dt>
    <dd>
    This file contains the xUnit unit testing framework we use in all our examples and assignments.  This is the program that actually runs all the unit tests and writes the results to the HTML page. You never need to touch this file.
    </dd>
    <dt>qunit.css</dt>
    <dd>
    This file contains the styling for the unit testing framework.  You never need to touch this file.
    </dd>
    <dt>JavaScript production code file (code.js)</dt>
    <dd>
    Write all the production code for the example or assignment you are working on in this file.
    </dd>
    <dt>JavaScript test code file (test.js)</dt>
    <dd>
    Write all the test code for the example or assignment you are working on in this file.
    </dd>
</dl>

You'll find the environment zip file under the "Lessons" or "Assignments" section.  E.g. if you want to work through Example 1, select the link for "Example 1 Environment" under "Lessons" which links to a file named "example1.zip".  When you are ready to do Assignment 1, select the link for "Assignment 1 Environment" under "Assignments" which links to a file named "assignment1.zip".

Steps to use the environment:

1. Right click the environment and select "Save target as...".
2. Save the zip file on your computer.
3. Unzip the .zip file into a folder.
4. Open the folder with the contents of the unzipped zip file.
5. Locate the HTML (.html) file and open it in your web browser.
6. Open the test code and production code JavaScript files (they end in .js) in a text editor or IDE.  Write your test code in the test file and your production code in the production file.


Text Editors
------------

If you are not sure what a <a href="http://en.wikipedia.org/wiki/Text_editor">text editor</a> is, it is simply a program to create and modify plain <a href="http://en.wikipedia.org/wiki/ASCII">ASCII</a> text files.  You will need one to edit your .js files.  On Windows, Notepad and Wordpad can be used as text editors and are pre-installed with the operating system.  If you use Wordpad, make sure you save as plain text (.txt) document and not .rtf or some other format.  If you can, I recommend using a text editor designed for writing code, like Notepad++ or jEdit, instead of Notepad or Wordpad.  On Mac OS X, TextEdit is pre-installed.  On Unix systems, vi or vim is usually installed by default with emacs available from the package manager along with a plethora of other text editors.


Printing and Debugging
----------------------

While working with the environment, you will likely benefit from a console and a debugger.  In Internet Explorer 9 and later, they can be accessed by pressing F12, which opens up the Developer Tools.  Selecting the console tab in the new window allows you too see any error messages as well as use the console.log() function to print messages to the console for debugging purposes.  You may also interactively type JavaScript into the console to see it executed immediately.
Firefox has a powerful extension called firebug with similar features.
If you are using an old version of Internet Explorer, you can use qUnit as a makeshift console by making a dummy test with an ok() assertion.  You can pass a label as the second argument to the ok() function.  Whatever you pass will be printed alongside the result of the ok() assertion as long as you convert it to a string first (call the .toString() method on the object). 


Saving and Short-cut Keys
-------------------------

As you work through the examples and assignments, be sure to periodically save your file.  Most GUI-based text editors have the save function mapped to the Control-S (press the Control key and the 'S' key at the same time) keyboard shortcut.  Since you will be running your unit tests often (at least once a minute) you can re-run the tests by pressing the Control-R keyboard shortcut when the web browser is in focus.  To quickly switch between your text editor and web browser, the Alt-Tab key combination can be used.  This way you can make changes to your JavaScript files in you text editor, hit Control-S to save, Alt-Tab to switch to the browser, and Control-R to rerun all the tests; all without lifting your fingers of off the keyboard.  This will save you time in the long run.
