SWE 430 Lesson 1:  Tools and Standards
========================================================================

This lesson discusses general implementation tools and coding standards.


Implementation Tools
-------------------

The most obvious and necessary tool in software development is the actual programming language(s) used to implement the software.  Unless writing the software in native machine language, the source code will need to be 
[assembled](http://en.wikipedia.org/wiki/Assembly_language), 
[compiled](http://en.wikipedia.org/wiki/Compiler), or 
[interpreted](http://en.wikipedia.org/wiki/Interpreter_%28computing%29).
The examples and exercises you will work with in this course make use of the JavaScript programming language.  JavaScript is an interpreted language.  Your web browser contains a JavaScript interpreter, which parses and interprets any linked or embedded JavaScript in the current web page.  

Although we will only be dealing with JavaScript, there are many languages to chose from.  Wikipedia lists a few hundred languages on its
[Timeline of Programming Languages][timeline]
page.

[Tiobe](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html)
provides a programming language popularity index that may be helpful in selecting appropriate programming language(s) for a given project.
[Hammerprinciple.com](http://hammerprinciple.com/therighttool)
attempts to create a community-driven set of strengths on weaknesses for popular languages based on survey responses.

Lutz Prechelt, in his paper,
[An Empirical Comparison of C, C++, Java, Perl, Python, Rexx, and Tcl](http://wwwipd.ira.uka.de/~prechelt/Biblio/jccpprtTR.pdf),
showed how scripting languages typically produce shorter programs when compared to non-scripting languages and often affected the choices in data structures (the programs written in scripting languages were more apt to use dictionaries.)  He states: "_We see that non-scripts are typically two to three times as long as scripts. Even the longest scripts are shorter than the average non-script._" However, it is important to keep in mind the choice of actual developers is much more important than the choice of language, as the author's research shows "_Differences between programmers outweigh differences between languages_".

Another important tool that is relevant to virtually all software projects is the development environment.  Development environments may be more text-centric or more graphical.  For example, popular text-centric development tools include text editors, such as Vim or Emacs, along with a set of command line tools.  On the other hand, many popular integrated development environments (IDE), like Eclipse, NetBeans, and Visual Studio make use of a graphical user interface (GUI).

The book \[[97TEPSK][]\] is a collection of short essays by several professional developers over various topics.  Here are some of the authors' opinions on using command-line tools and IDEs.

- [Know How to Use Command-line Tools][command-line], page 86.
- [Know Your IDE][IDE], page 90
- [The Unix Tools Are Your Friends][Unix], page 176

There are many other software development tools.  Some are generally useful, such as unit testing frameworks (discussed in [Lesson 3](lesson3.html)), and others that are only applicable in specific domains.  We will not attempt to discuss them all in detail here.


Coding Standards
----------------

The ultimate purpose of coding standards is to produce readability and maintainability in the code-base, and prevent common programming errors, through smartly chosen and consistently applied rules.
In order to create cost-effective software, all developers on a team must be able to easily read and understand each other's code.  This includes future developers, who may not be on the team yet, but will have to, someday, maintain the code.
Coding standards can help us achieve this.

The most prominent component of many coding standards are the naming conventions.  The naming conventions can apply to variables, functions, classes, and any other constructs used in the language.  Coding standards can also address the structure and layout of the code.  For instance, it may define indentation for the body of conditional structures (if statements, while loops, for loops, etc).  This often involves the use of whitespace to create visually structured code.
A bad example of the use (or abuse) of white space is the
[IOCCC](http://en.wikipedia.org/wiki/IOCCC).

Other areas coding standards may address include parameter list naming/ordering, and length limits.  Length limits can apply to the maximum number of characters per line, the maximum number of lines in a function, and the maximum number of lines or methods per class.

Python PEP 7,
[Style Guide for C Code](http://legacy.python.org/dev/peps/pep-0007/),
and PEP 8,
[Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/),
give concrete examples of coding standards used in practice.

While the aforementioned coding standards focus more on style, other coding standards focus on preventing common programming errors.
[MISRA](http://www.misra-c.com/Activities/MISRAC/tabid/160/Default.aspx)
provides C coding standards that focus on software safety.  MISRA C has gained widespread acceptance in the automotive and aerospace industries.

Since we will be using JavaScript in our examples and exercises, here are some well-known JavaScript coding standards:

- [Douglas Crockford's JavaScript Conventions][Crokford]
- [Mozilla Coding Style][Mozilla]
- [Google JavaScript Style Guide][Google]
- [Node.js Style Guide][Node]

The following entries in \[[97TEPSK][]\] discuss coding standards in more detail:

- [Code Layout Matters][codeLayout], page 26
- [Automate Your Coding Standard][codingStandard], page 8


Conclusion
----------

This lesson focused on software tools and coding standards.  The next lesson, [Lesson 2](lesson2.html), deals with refactoring.

<dl>
<dt>97TEPSK</dt>
<dd>
Henney, Kevlin.  <em>97 Things Every Programmer Should Know</em>, 2010
</dd>
</dl>



[timeline]: http://en.wikipedia.org/wiki/Timeline_of_programming_languages
[97TEPSK]: http://programmer.97things.oreilly.com/
[command-line]: http://programmer.97things.oreilly.com/wiki/index.php/Know_How_to_Use_Command-line_Tools
[IDE]: http://programmer.97things.oreilly.com/wiki/index.php/Know_Your_IDE
[Unix]: http://programmer.97things.oreilly.com/wiki/index.php/The_Unix_Tools_Are_Your_Friends
[codingStandard]: http://programmer.97things.oreilly.com/wiki/index.php/Automate_Your_Coding_Standard
[codeLayout]: http://programmer.97things.oreilly.com/wiki/index.php/Code_Layout_Matters
[Crokford]: http://javascript.crockford.com/code.html
[Mozilla]: https://developer.mozilla.org/en-US/docs/Developer_Guide/Coding_Style
[Google]: https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml
[Node]: https://github.com/felixge/node-style-guide

