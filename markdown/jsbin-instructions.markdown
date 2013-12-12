SWE 430 jsbin Instructions
========================================================================


Instructions
------------

The jsbin.com website allows one to write JavaScript using a simple web-based editor and console.  As you write your code, the code is saved to the jsbin.com server.  The web page checks for changes in the code several times a second and updates the server if any changes were made to the code.

I have created an alternative environment using jsbin for each of the 2 examples and 3 assignments.  The four links to the environments are provided below.  You may use any of these in place of the .zip file environments to work through the examples and assignments.

To use any of the below environments, just click on the appropriate link.  For instance, if you want to work on Assignment 1 using the jsbin environment, click on the Assignment 1 link.  Because the 4 pages are protected, if you attempt to change any of them by editing the JavaScript, jsbin will start a new project and assign it a new identifier in the URL.  For example, if you go to
[http://jsbin.com/swe430_assignment1/latest/edit](http://jsbin.com/swe430_assignment1/latest/edit?javascript,live)
and start typing, the URL will change to include the new ID that jsbin assigns to your new project.  If jsbin assigns "abcdef" to the new project, then the URL will become: 
`http://jsbin.com/swe430_assignment1/1/edit#/abcdef/1/edit`.
The string "abcdef" is your new identifier.  Do not loose this!
When you are finished the assignment, you will send me this identifier so I can grade your work.
Once you receive your new identifier for your project, you can use it directly to go to your project.  Going to http://jsbin.com/abcdef/lastest/edit will always bring you to the latest revision of your work.

You receive one identifier per project.  So if you use the jsbin environments to work the assignments, you will send me three identifiers:  one for Assignment 1, one for Assignment 2, and one for Assignment 3.

The jsbin page only provides a single JavaScript panel.  So using jsbin is like having only a single file available.  Therefore, put both your test code and your production code in the single JavaScript panel.  For Example 1 and Assignment 1, all the test code will already be present and you will only need to add the production code to the single JavaScript panel.  For Example 2 and Assignments 2 and 3, you will write both the test code and production code in the single JavaScript panel.


Lock Revisions Often
--------------------

The jsbin website works with the idea of revisions.  Each revision of your work is numbered.  It starts at 1 and increments each time you make a revision.  You can lock a revision by clicking "Share" in the toolbar and selecting "Lock revision".  You may also simply press `<control> + s` to lock revisions.

Although jsbin automatically saves the changes you make to the current revision of your work, you should still **lock revisions often**.  Since all your work is being shuttled across the internet to the jsbin server, like all web-based technologies, it is only as reliable as the network.  By locking revisions often, you create checkpoints that you can restore in case of failure.


jsbin.com Environment Links
---------------------------

Examples

- [Example 1](http://jsbin.com/swe430_example1/latest/edit?javascript,live)
- [Example 2](http://jsbin.com/swe430_example2/latest/edit?javascript,live)


Assignments

- [Assignment 1](http://jsbin.com/swe430_assignment1/latest/edit?javascript,live)
- [Assignment 2](http://jsbin.com/swe430_assignment2/latest/edit?javascript,live)
- [Assignment 3](http://jsbin.com/swe430_assignment2/latest/edit?javascript,live)


Tips for Using jsbin.com
------------------------

If you experience performance issues while using jsbin, you can uncheck the "Auto-run JS" check box which will disable auto running your code.  When you want to run the tests, just click the "Run with JS" button.

Pressing `<control> + <Enter>` reruns all the code.
Pressing `<control> + s` locks the current revision.

To avoid confusion, Make sure only the Javascript and Output panels are selected.  You don't need to modify the HTML or CSS panels, so they can remain hidden.  Additionally, you can use the Console panel for debugging.  Any `console.log()` function calls will print their arguments to the console.  So `console.log("hello");` will print `hello` to the console.  You can also type JavaScript code directly into the console for interactive debugging.  


Help
----

The top right corner, in the toolbar, there is a "Help" button.  It provides the keyboard shortcuts, an explanation on how jsbin URLs work and links to video tutorials.  If you run into any problems or have additional questions, please don't hesitate to ask me for help!
