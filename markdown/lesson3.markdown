SWE 430 Lesson 3:  Refactoring
========================================================================

In this lesson we will lay the conceptual foundations of refactoring which we will later apply in Example 2 and Exercise 2.

What is Refactoring
-------------------

In [FOWL99], Martin Fowler defines refactoring as:

"_Refactoring is the process of changing a software system in such a way that it does not alter the external behavior of the code yet improves its internal structure. It is a disciplined way to clean up code that minimizes the chances of introducing bugs. In essence when you refactor you are improving the design of the code after it has been written._"

Wikipedia sites the advantages of refactoring as "_improved code readability and reduced complexity to improve the maintainability of the source code, as well as a more expressive internal architecture or object model to improve extensibility._" [WIKIRE]

Joshua Kerievsky, in [KERI04], notes
"_By continuously improving the design of code, we make it easier and easier to work with. This is in sharp contrast to what typically happens: little refactoring and a great deal of attention paid to expediently adding new features. If you get into the hygienic habit of refactoring continuously, you'll find that it is easier to extend and maintain code._"


Refactoring Tips
----------------

The following are the tips found in the first four chapters of [FOWL99].  The book gives a more complete treatment of refactoring.  The first chapter provides a step-by-step example that you may use to augment Example 2.  The full book is available on Safari Online.

<h3>Chapter 1: Refactoring, a First Example</h3>


<p class="quote">
<span class="page">
Page 7:
</span>
When you find you have to add a feature to a program, and the program's code is not structured in a convenient way to add the feature, first refactor the program to make it easy to add the feature, then add the feature.
</p>

<p class="quote">
<span class="page">
Page 8:
</span>
Before you start refactoring, check that you have a solid suite of tests. These tests must be self-checking.
</p>

<p class="quote">
<span class="page">
Page 13:
</span>
Refactoring changes the programs in small steps. If you make a mistake, it is easy to find the bug.
</p>

<p class="quote">
<span class="page">
Page 15:
</span>
Any fool can write code that a computer can understand. Good programmers write code that humans can understand.
</p>

<h3>Chapter 2: Principles in Refactoring</h3>

<p class="quote">
<span class="page">
Page 53:
</span>
Refactoring (noun): a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behavior.
</p>

<p class="quote">
<span class="page">
Page 54:
</span>
Refactor (verb): to restructure software by applying a series of refactorings without changing its observable behavior.
</p>

<p class="quote">
<span class="page">
Page 58:
</span>
Three strikes and you refactor.
</p>

The above tip is in the context of code duplication.  If you see the same code duplicated three (or more) times, you should refactor it.

<div class="quote">
<p class="inner">
<span class="page">
Page 60:
</span>
Why refactor?
</p>

<ul>
    <li>
Programs that are hard to read are hard to modify.
    </li>
    <li>
Programs that have duplicated logic are hard to modify.
    </li>
    <li>
Programs that require additional behavior that requires you to change running code are hard to modify.
    </li>
    <li>
Programs with complex conditional logic are hard to modify.
    </li>
</ul>
</div>

<p class="quote">
<span class="page">
Page 65:
</span>
Don't publish interfaces prematurely. Modify your code ownership policies to smooth refactoring.
</p>

<h3>Chapter 3: Bad Smells in Code</h3>

<div class="quote">
<p class="inner">
<span class="page">
Page 75:
</span>
Top 4 Bad Smells in Code:
</p>
<ul>
    <li>
Duplicated Code
    </li>
    <li>
Long Method
    </li>
    <li>
Large Class
    </li>
    <li>
Long Parameter List
    </li>
</ul>
</div>

<p class="quote">
<span class="page">
Page 88:
</span>
When you feel the need to write a comment, first try to refactor the code so that any comment becomes superfluous.
</p>

<h3>Chapter 4: Building Tests</h3>

<p class="quote">
<span class="page">
Page 90:
</span>
Make sure all tests are fully automatic and that they check their own results.
</p>

<p class="quote">
<span class="page">
Page 90:
</span>
A suite of tests is a powerful bug detector that decapitates the time it takes to find bugs.
</p>

<p class="quote">
<span class="page">
Page 94:
</span>
Run your tests frequently. Localize tests whenever you compile---every test at least every day.
</p>

<p class="quote">
<span class="page">
Page 97:
</span>
When you get a bug report, start by writing a unit test that exposes the bug.
</p>

<p class="quote">
<span class="page">
Page 98:
</span>
It is better to write and run incomplete tests than not to run complete tests.
</p>

<p class="quote">
<span class="page">
Page 99:
</span>
Think of the boundary conditions under which things might go wrong and concentrate your tests there.
</p>

<p class="quote">
<span class="page">
Page 100:
</span>
Don't forget to test that exceptions are raised when things are expected to go wrong.
</p>

<p class="quote">
<span class="page">
Page 101:
</span>
Don't let the fear that testing can't catch all bugs stop you from writing the tests that will catch most bugs.
</p>


Conclusion
----------

This lesson briefly discussed refactoring.  You are ready to work through Example 2.  As you work through the example, keep the above tips in mind.  You will see them in action.  After you have worked through Example 2, You will receive an opportunity to apply these concepts yourself in Exercise 2.

<dl>

<dt>FOWL99</dt>
<dd>
Fowler, Martin.  <em>Refactoring Improving the Design of Existing Code</em>, 1999
</dd>

<dt>KERI04</dt>
<dd>
Kerievsky, Joshua. <em>Refactoring to Patterns</em>, 2004
</dd>

<dt>WIKIRE</dt>
<dd>
Wikipedia.  <em>Code Refactoring</em>, http://en.wikipedia.org/wiki/Refactoring [online; accessed 08-April-2013]
</dd>

</dl>
