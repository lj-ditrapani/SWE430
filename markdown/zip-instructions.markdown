SWE 430 zip Instructions
========================================================================


The Local zip File Environment
------------------------------

The local zip environment is simply a zip file containing 5 files:  an html page, a CSS files, and three JavaScript files.

Contents of environment .zip file:

<dl>
    <dt>HTML file</dt>
    <dd>
    This page will display the results of all the unit tests written in the JavaScript test file (test.js).  Refreshing the page will re-run all the tests (including any new tests you have added since the last run.)  You do not need to modify this file.  Simply open it in your web browser.
    </dd>
    <dt>qunit.js</dt>
    <dd>
    This file contains the xUnit unit testing framework we use in all our examples and assignments.  This is the program that actually runs all the unit tests defined in test.js and writes the results to the HTML page. You never need to touch this file.
    </dd>
    <dt>qunit.css</dt>
    <dd>
    This file contains the styling for the unit testing framework.  You never need to touch this file.
    </dd>
    <dt>code.js</dt>
    <dd>
    This file contains the JavaScript production code.  Write all the production code for the example or assignment you are working on in this file.
    </dd>
    <dt>test.js</dt>
    <dd>
    This file contains all the JavaScript test code.  For Example 1 and Assignment 1, this file will already contain all the necessary test code.  For Example 2 and Assignments 2 and 3, this file will be blank and you will write all the test code for the example or assignment you are working on in this file.
    </dd>
</dl>

You'll find the environment zip file hyper-linked in the example or assignment HTML page you are working on.  E.g. if you want to work through Example 1, go to the 
[SWE 430 Index Page](index.html), click on [Example 1](example1.html), and then select the link for the "Example 1 zip Environment" in the introduction, which links to a file named "example1.zip".  When you are ready to do Assignment 1, go to the [Assignment 1](assignment1.html) page and select the link for "Assignment 1 zip Environment" which links to a file named "assignment1.zip".

Steps to use the environment:

1. **Right**-click the environment link and select "Save target as...".
   (Do not left-click, or the zip file will not be saved.)
2. Save the zip file on your computer.
3. Unzip the .zip file into a folder.
4. Open the folder with the contents of the unzipped zip file.
5. Locate the HTML (.html) file and open it in your web browser.
6. Open the test code (test.js) and production code (code.js) JavaScript
   files in a text editor or IDE.  Write your test code in the test file
   and your production code in the production file.  Note:  In Example 1
   and Assignment 1, you will not write any test code, only production
   code, because the test code is already complete.
7. If you receive a "permission denied" error from the qUnit output,
   make sure the exercise.html file is "Unblocked".  To do this,
   right-click on the exercise.html file, select properties, and at the
   bottom of the pop-up box, press the "Unblock" button.



Text Editors
------------

If you are not sure what a
[text editor](http://en.wikipedia.org/wiki/Text_editor)
is, it is simply a program to create and modify plain
[ASCII](http://en.wikipedia.org/wiki/ASCII)
text files.  You will need one to edit your .js files.  On Windows, Notepad and Wordpad can be used as text editors and are pre-installed with the operating system.  If you use Wordpad, make sure you save as plain text (.txt) document and not .rtf or some other format.  If you can, I recommend using a text editor designed for writing code, like Notepad++ or jEdit, instead of Notepad or Wordpad.  On Mac OS X, TextEdit is pre-installed.  On Unix systems, vi or vim is usually installed by default with emacs available from the package manager along with a plethora of other text editors.


Printing and Debugging
----------------------

While working with the environment, you will likely benefit from a console and a debugger.  In Internet Explorer 8 and later, they can be accessed by pressing F12, which opens up the Developer Tools.  Selecting the console tab in the new window allows you too see any error messages as well as use the `console.log()` function to print messages to the console for debugging purposes.  For example, entering `console.log("hello");` will print `hello` to the console.  You may also interactively type JavaScript into the console to see it executed immediately.
The 
[Firefox](https://developer.mozilla.org/en-US/docs/Tools) and
[Chrome](https://developers.google.com/chrome-developer-tools/)
web browsers both come with consoles and debuggers built-in.  Firefox also has an "add-on" (extension) called
[firebug](https://getfirebug.com/) with similar features.
Finally, if you are stuck using an old version of Internet Explorer (pre 8.0), you can use qUnit as a makeshift console by creating a dummy test with an ok() assertion.  You can pass a label as the second argument to the ok() function.  Whatever you pass will be printed alongside the result of the ok() assertion as long as you convert it to a string first (call the .toString() method on the object).  For example:

    test('Dummy', function() {
        ok(true, "hello");
    });

The above will display `hello` as the label of the assertion under the 'Dummy' test in the html output.


Saving and Short-cut Keys
-------------------------

As you work through the examples and assignments, be sure to periodically save your file.  Most GUI-based text editors have the save function mapped to the Control-S (press the Control key and the 'S' key at the same time) keyboard shortcut.  Since you will be running your unit tests often (about once a minute) you can re-run the tests by pressing the Control-R keyboard shortcut when the web browser is in focus.  To quickly switch between your text editor and web browser, the Alt-Tab key combination can be used.  This way you can make changes to your JavaScript files in you text editor, hit Control-S to save, Alt-Tab to switch to the browser, and Control-R to rerun all the tests; all without lifting your fingers of off the keyboard.  This will save you time in the long run.
