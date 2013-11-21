SWE 430 Lesson 1:  Tools and Standards
========================================================================

This lesson discusses general construction tools and coding standards.


Constructions Tools
-------------------

The most obvious and necessary tool in software development is the actual programming language(s) used to implement the software.  Unless writing the software in native machine language, the source code will need to be 
<a href="http://en.wikipedia.org/wiki/Assembly_language">assembled</a>, 
<a href="http://en.wikipedia.org/wiki/Compiler">compiled</a> or 
<a href="http://en.wikipedia.org/wiki/Interpreter_(computing)">interpreted</a>.  In the case of our examples and exercises, the CoffeeScript is first compiled into JavaScript (by the coffee-script.js JavaScript library) which is then interpreted by the web browser's JavaScript interpreter.

There are many languages to chose from.  Wikipedia lists hundreds of languages on its <a href="http://en.wikipedia.org/wiki/Timeline_of_programming_languages">Timeline of programming languages</a> page.

<a href="http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html">Tiobe</a> provides a programming language popularity index that may be helpful in choosing a programming language for a project.
<a href="http://hammerprinciple.com/therighttool">Hammerprinciple.com</a> attempts to create a community-driven set of strengths on weaknesses for popular languages based on survey responses.

Lutz Prechelt, in his paper, <a href="http://wwwipd.ira.uka.de/~prechelt/Biblio/jccpprtTR.pdf">An Empirical Comparison of C, C++, Java, Perl, Python, Rexx, and Tcl</a>, showed how scripting languages typically produce shorter programs when compared to non-scripting languages and often affected the choices in data structures (the programs written in scripting languages were more apt to use dictionaries.)  He states: "_We see that non-scripts are typically two to three times as long as scripts. Even the longest scripts are shorter than the average non-script._" However, it is important to keep in mind the choice of actual developers is much more important than the choice of language, as the author's research shows "_Differences between programmers outweigh differences between languages_".

Another important tool that is relevant to virtually all software projects is the development environment.  Development environments may be more text-centric or more graphical.  For example, popular text-centric development tools include text editors, such as Vim or Emacs, along with a set of command line tools.  On the other hand, many popular integrated development environments (IDE) make use of a graphical user interface (GUI).

The book [97TEPSK] is a collection of short essays by several professional developers over various topics.  Here are some of the authors' opinions on using command-line tools and IDEs.

- <a href="http://programmer.97things.oreilly.com/wiki/index.php/Know_How_to_Use_Command-line_Tools">Know How to Use Command-line Tools</a>, page 86.
- <a href="http://programmer.97things.oreilly.com/wiki/index.php/Know_Your_IDE">Know Your IDE</a>, page 90
- <a href="http://programmer.97things.oreilly.com/wiki/index.php/The_Unix_Tools_Are_Your_Friends">The Unix Tools Are Your Friends</a>, page 176

There are many other software development tools.  Some are generally useful, such as unit testing frameworks (discussed in [Lesson 3](lesson3.html)), and others that are only applicable in specific domains.  We will not attempt to discuss them all in detail here.


Coding Standards
----------------

The ultimate purpose of coding standards is to produce readability and maintainability in the code base through smartly chosen and consistently applied rules.  The intent behind using coding standards is that all developers on a team can easily read each other's code and that future developers that will have to someday maintain the code also be able to easily read the code.

The most prominent component of many coding standards are the naming conventions.  The naming conventions can apply to variables, functions, classes, and any other constructs used in the language.  Coding standards can also address the structure and layout of the code.  For instance, it may define indentation for the body of conditional structures (if statements, while loops, for loops, etc).  This often involves the use of whitespace to create visually structured code.

A bad example of the use (or abuse) of white space is the <a href="http://en.wikipedia.org/wiki/IOCCC">IOCCC</a>.  Other areas coding standards may address include parameter list naming/ordering, and length limits.  Length limits can apply to the maximum number of characters per line, the maximum number of lines in a function, and the maximum number of lines or methods per class.

Python PEP 7, <a href="http://www.python.org/dev/peps/pep-0007/">Style Guide for C Code</a> and PEP 8, <a href="http://www.python.org/dev/peps/pep-0008/">Style Guide for Python Code</a> give concrete examples of coding standards used in practice.  While these coding standards focus more on style, <a href="http://www.misra-c.com/Activities/MISRAC/tabid/160/Default.aspx">MISRA</a> provides C coding standards that focus on software safety.  MISRA C has gained widespread acceptance in the automotive and aerospace industries.

There are a couple of entries in [97TEPSK] that deal with coding standards:

- <a href="http://programmer.97things.oreilly.com/wiki/index.php/Automate_Your_Coding_Standard">Automate Your Coding Standard</a>, page 8
- <a href="http://programmer.97things.oreilly.com/wiki/index.php/Code_Layout_Matters">Code Layout Matters</a>, page 26


Conclusion
----------

This lesson focused on software tools and coding standards.  The next lesson, [Lesson 2](lesson2.html), deals with refactoring.

<dl>
<dt>97TEPSK</dt>
<dd>
Henney, Kevlin.  <em>97 Things Every Programmer Should Know</em>, 2010
</dd>
</dl>
