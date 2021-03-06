SWE 330/430 Lesson 2:  Refactoring
========================================================================

In this lesson we will lay the conceptual foundations of refactoring.


What is Refactoring
-------------------

In \[[FOWL99][]\], Martin Fowler defines refactoring as:

"_Refactoring is the process of changing a software system in such a way that it does not alter the external behavior of the code yet **improves its internal structure**. It is a disciplined way to clean up code that minimizes the chances of introducing bugs. In essence when you refactor you are **improving the design of the code** after it has been written._"

Wikipedia sites the advantages of refactoring as "_improved code **readability** and **reduced complexity** to improve the **maintainability** of the source code, as well as a more expressive internal architecture or object model to improve **extensibility**._"
\[[WIKIRE](http://en.wikipedia.org/wiki/Refactoring)\]

Joshua Kerievsky, in
\[[KERI04](http://techbus.safaribooksonline.com/0321213351)\], notes
"_By continuously improving the design of code, we make it easier and easier to work with. This is in sharp contrast to what typically happens: little refactoring and a great deal of attention paid to expediently adding new features. If you get into the hygienic habit of refactoring continuously, you'll find that it is easier to **extend** and **maintain** code._"


Refactoring Tips
----------------

The following are the tips found in the first four chapters of
\[[FOWL99][]\].  The book gives a more complete treatment of refactoring, to include a step-by-step example provided in the first chapter.  The full book is available on Safari Online.

### Chapter 1: Refactoring, a First Example ###

Page 7:

> When you find you have to add a feature to a program, and the program's code is not structured in a convenient way to add the feature, first refactor the program to make it easy to add the feature, then add the feature.

Page 8:

> Before you start refactoring, check that you have a solid suite of tests. These tests must be self-checking.

Page 13:

> Refactoring changes the programs in small steps. If you make a mistake, it is easy to find the bug.

Page 15:

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand.

### Chapter 2: Principles in Refactoring ###

Page 53:

> Refactoring (noun): a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behavior.

Page 54:

> Refactor (verb): to restructure software by applying a series of refactorings without changing its observable behavior.

Page 58:

> Three strikes and you refactor.

The above tip is in the context of code duplication.  If you see the same code duplicated three (or more) times, you should refactor it.

Page 60:

> Why refactor?
> 
> - Programs that are hard to read are hard to modify.
> - Programs that have duplicated logic are hard to modify.
> - Programs that require additional behavior that requires you to change running code are hard to modify.
> - Programs with complex conditional logic are hard to modify.

Page 65:

> Don't publish interfaces prematurely. Modify your code ownership policies to smooth refactoring.

### Chapter 3: Bad Smells in Code ###

Page 75:

> Top 4 Bad Smells in Code:
>
> - Duplicated Code
> - Long Method
> - Large Class
> - Long Parameter List

Page 88:

> When you feel the need to write a comment, first try to refactor the code so that any comment becomes superfluous.

### Chapter 4: Building Tests ###

Page 90:

> Make sure all tests are fully automatic and that they check their own results.

Page 90:

> A suite of tests is a powerful bug detector that decapitates the time it takes to find bugs.

Page 94:

> Run your tests frequently. Localize tests whenever you compile---every test at least every day.

Page 97:

> When you get a bug report, start by writing a unit test that exposes the bug.

Page 98:

> It is better to write and run incomplete tests than not to run complete tests.

Page 99:

> Think of the boundary conditions under which things might go wrong and concentrate your tests there.

Page 100:

> Don't forget to test that exceptions are raised when things are expected to go wrong.

Page 101:

> Don't let the fear that testing can't catch all bugs stop you from writing the tests that will catch most bugs.


Conclusion
----------

This lesson discussed refactoring.  You are ready for
[Lesson 3: Test-driven Development](lesson3.html).

**For 430 students**: later in the course,
as you work through the examples,
keep the above tips in mind.  You will see them in action.
Also, you will receive opportunities to apply these concepts yourself
in Assignments 1, 2, and 3.


<dl>

<dt>FOWL99</dt>
<dd>
Fowler, Martin.
<em>Refactoring:  Improving the Design of Existing Code</em>, 1999
</dd>

<dt>KERI04</dt>
<dd>
Kerievsky, Joshua.
<em>Refactoring to Patterns</em>, 2004
</dd>

<dt>WIKIRE</dt>
<dd>
Wikipedia.
<em>Code Refactoring</em>,
<a href="http://en.wikipedia.org/wiki/Refactoring">
http://en.wikipedia.org/wiki/Refactoring</a>
[online; accessed 08-April-2013]
</dd>

</dl>


[FOWL99]: http://techbus.safaribooksonline.com/0201485672
