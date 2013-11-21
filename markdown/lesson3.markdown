SWE 430 Lesson 3:  TDD and Unit Testing
========================================================================

In this lesson we will lay conceptual foundations regarding test-driven development (TDD) and unit testing which we will later apply in the examples and assignments.


Unit Testing
-------------------------

Unit testing is the lowest level of testing and it occurs during the construction phase.  Unit testing is intended to show that each unit has been built correctly (verification).  It tests the actual software construction.  As with all levels of testing, unit testing cannot prove the absence of faults.  It can only prove the absence or presence of faults for the specific test cases in the test suite.  For any non-trivial program, it is generally not feasible to test all possible test cases.  However, it is generally possible to test a set of test cases that exercise all statements in the program.  Also, a set of test cases can be selected that test for high-risk faults (mistakes that occur often and/or faults that have disastrous effects; selected according to the risk-management process).  By carefully selecting test cases that completely exercise the code (verification), and cover high-risk faults, unit testing can be used as a tool to help deliver high-quality software.

Unit testing is the foundation of software testing.  Without reliable unit tests, integration and system testing become extremely difficult.  A software unit is "the smallest software component that can be compiled and executed" as defined by [JORG08].  The definition on Wikipedia.org explains it as the "smallest testable part of an application".  Unit testing is generally performed by the developer who wrote the code-they are the only ones familiar enough with its detailed functioning to be effective at testing it.

Unit testing should be automated.  Automation will allow the tests to be run more often leading to a higher-quality software system.

Test-driven Development
-------------------------

A well-established best practice is to take a test-driven development (TDD) approach which includes using an automated unit testing framework such as an xUnit framework [BECK02] or a Behavior-driven Development (BDD, a more qualified form of TDD [WIKBDD]) framework.

Test-driven development (TDD) is a cyclical development process that combines testing, construction, and design into short steps. The program is written in small units. For each unit, the programmer first writes the unit test, then writes the code to pass the unit test. Each unit is written and fully tested before moving on to the next unit. It often drives a bottom-up approach to development. The boon is more errors are detected earlier than when using an antiquated water-fall-like method.  To be effective, TDD cycles should be relatively short in duration.  An individual TDD cycle should take seconds to minutes.

Figure 1 shows how a TDD cycles fit into the larger picture of testing cycles.  The figure gives the approximate duration for each cycle.

<div class="break"></div>
<div class="image">
<h4> Figure 1:  Cycles of Testing </h4>
<img src="images/cycles.png" alt="Cycles of Testing" />
</div>

A Single Cycle in the TDD Process

- Write a test
- Run all tests to ensure the new test fails
- Write just the code to pass the test
- Run all the tests to ensure the new test passes
- Refactor production code to eliminate any duplication introduced by the new code and improve the structure of the code
- Run all the tests
- Refactor test code to eliminate any duplication introduced by the new test
- Run all the tests

Note that steps 2, 4, 6, and 8 provide immediate feed-back (none of these steps should take more than a second to run).  Steps 1, 5 and 7 are design activities.  In step 1, writing a test, the developer designs the low-level interface to the unit of code.  In step 5, the developer restructures existing production code to eliminate duplication.  Likewise in step 7---but for the test code.  Only step 3 adds new functionality to the system.  So every bit of functionality added is surrounded by robust design and feedback activities allowing the developer to spot errors early and keep the code base in a coherent structure.  Without TDD, construction activities cause the design of the code to decay over time with each addition of functionality.  With TDD, the design in the code base actually improves with each addition of functionality thanks to the refactoring and test-centric development.  Writing tests first forces the developer to write "testable code" and testable code is implicitly easier to maintain than "non-testable" code.


Benefits of TDD and Automated Unit Testing
------------------------------------------


Best practices have now adopted the position that writing test cases before writing the code is a better approach to construction. There are many reasons for this:

Benefits of Test-driven Development (TDD) with an automated testing framework:


- The unit tests partition units of code. Failing tests point directly to the guilty unit.  The smaller the units, the finer the granularity of the fault isolation.
- Creating a test first directs the developer to design each unit to an interface (the test defines the interface to the unit.) 
- TDD also has several (subjective) psychological impacts: 
    - It gives the programmer a steady sense of progress as each unit is completed.
    - It makes the code construction process more manageable by breaking it down into bite-sized pieces (the units).
    - Seeing all the test cases pass during regression testing gives the programmer confidence in the code base. 
- Developers detect errors earlier in the development process instead of waiting for a "testing" phase to find the same errors as in the waterfall method.  Earlier detection means less rework, therefore less cost to fix.
- Writing the tests first does not increase coding time.  The same time would be spent writing the tests during the "testing" phase of a waterfall method; only the developers loose the early detection of faults, increasing the cost of fixing the faults. 
- Obviously, running the tests can expose construction errors.  However, the process of writing test cases often exposes requirements and design errors as well.
- Because the tests are automated, they are run frequently at no cost overhead to the project.  If they were run manually, then they would not be run nearly as frequently, and be expensive to run in terms of manpower.
- Progress and results can be reported to the stakeholders earlier. 
- Many projects have failed because management did not plan for testing.  With TDD, planning for unit tests is no longer an issue since they are accomplished with each unit of code written.  In TDD, developers proactively write tests instead of reacting to "finished" production code with testing.
- The unit tests developed can be used in automated regression testing.



Risk in TDD and Unit Testing
----------------------------

It is important to understand the risks in TDD and unit testing so they can be proactively managed and mitigated.

<h3>Test Suite Execution Time</h3>

The longer the test suite takes to run, the less often the test suite will be run.  Below, in the section on "<em>Scaling Unit Test Suites in Large Projects</em>," we give strategies for dealing with slow running test suites.

<h3>TDD Cycle Time Length</h3>

The longer the TDD cycles run, the more potential for problems and the bigger the problems can become.  With longer cycles, an error will take longer to fix than if shorter cycles were used.  There are two reasons for this:  1) Because more code has been written, it takes longer to isolate the bug.  2) If changes must be rolled back, there are more changes to roll back--therefore, more lost time.  One hour cycle means one hour lost in the worst case.  One minute cycle means one minute lost in the worst case.  A cycle that produces 100 lines of code means there will be 100 lines of code (plus dependencies) to sift through to find a bug.  A cycle that produces only 5 lines of code only has 5 lines (plus dependencies) to sift through to find a bug.

<h3>Writing Too Many Tests</h3>

Given infinite time, you can never have too many tests.  But since all projects have a schedule, time is finite.  Managers and developers must use wisdom to select the minimum number of test cases that 1) exercise all of the statements/expressions of the production code, 2) cover all of the requirements, and 3) test for high-risk faults.

<h3>Maintaining Test Code</h3>

Test code must be maintained to the same quality standards as the production code.  If the test code degrades, it will become difficult to add new tests to the test suite.  If so, developers will avoid creating new tests, and the value of the test suite will plummet as new production code is added without adequate test code.  This is why steps 7 and 8 in the TDD cycle are so important.  They direct the developer to refactor the test code when necessary.  Performing these steps will ensure the test code retains its value and remains manageable for the developers.


Scaling Unit Test Suites in Large Projects
------------------------------------------

The entire test suite must run quickly.  If the entire test suite cannot execute in under a second, its value is diminished.  If the developer has to "waste" time waiting for tests to complete, the developer will be less likely to run the test suite.

TDD generally scales well in large projects, but if a test suite is running too slowly, here are some steps to take.

<h3>Step 1:  Replace Slow Dependencies with Mock Objects</h3>

Identify the slow running tests that are taking up the majority of the test suite's execution time.  The cause of the long execution time of the guilty tests is often its dependencies.  

Examples of dependencies that cause slow running tests:

- Database:  A test that starts a database, sets up initial tables and creates a database connection. 
- Sockets:  A test that requires communicating with a remote server.
- Disk Access:  A test that reads on writes to a file on disk multiple times.

These dependencies can be easily substituted with special stubs called "mock" objects. A mock object has an identical interface to the real object it replaces.  For example, to replace a dependency on a file object that has read and write methods, one might use a mock object that also has read and write methods, but is backed by a string buffer, so reads and writes to the file only access main memory instead of the disk.  The unit under test must be properly parameterized so that the correct dependency can be injected at run time---the mock object during testing, and the actual object during integration testing, system testing and in production use.

<h3>Step 2:  Divide-up Test Suite</h3> 

If the first step is not enough to reduce the execution time of the test suite, it may be necessary to divide the test suite into multiple, smaller test suites.  This only occurs when the system is exceptionally large.  When deciding how to partition the software units, attempt to group interdependent units together.  Some dependencies will still exist between groups of software units.  If a unit depends on units outside its own test suite, those dependencies must be stubbed-out.  This will allow each test suite to be run safely in isolation from the other test suites.

If a second sounds too short to run an entire test suite, don't worry.  If the developers take care to mock out database connections, network connections, files, and the like, you can easily run several thousand tests in one second, even on budget hardware.


Dealing with Legacy Systems
---------------------------

When maintaining a legacy system, automated unit tests may not be available.  In this situation, as maintenance is performed on the software, unit tests should be created, using a TDD approach, for the portion of the system under maintenance.  Once a portion of the code is covered by unit tests, it becomes easier to refactor as the unit tests will detect if the covered code breaks.  As time progresses, more and more of the system will be covered by the unit tests; thus making it easier and easier to maintain.  Figure 2 depicts how, over the long term, a legacy system might progress from having no unit tests to being completely covered by unit tests.  Shaded regions represent portions of code covered by unit test.  Initially, the system has no unit tests and its design--the structure of the system--is not very clear.  As time goes on, more of the system is covered and more of the system can be refactored into a better design.

<div class="image">
<h4> Figure 2:  Progression of a Legacy System </h4>
<img class="legacy"
     src="images/legacy.png"
     alt="Progression of a legacy system" />
</div>

When a bug is reported for the system, before attempting to correct the bug, a unit test should be created that catches the bug, so that if future work on the system reintroduces the bug, the test suite will catch it immediately instead of allowing the bug to be released into the field undetected once again. 

The first maintenance sessions on a legacy system with no unit tests will go slowly at first as time is taken away from maintenance to add new unit tests.  However, over time, the maintenance time will shorten and eventually be much shorter than what it would have been without the unit tests.  Although adding unit tests to a legacy system may seem like a slow and difficult process, over time it will pay great dividends.


Software Security and Information Assurance
-------------------------------------------

The first line of defense in software security and information assurance is producing high quality code.  In other words, produce clean code: readable, maintainable, code that does what it is supposed to and nothing else.  Following the above guidance of using TDD with automated unit testing will go a long way to help produce quality code.

However, this alone is not enough to ensure the security and availability of our software systems.  In addition, abuse cases must be considered.  The development team must think how an attacker might attempt to misuse the system.  From those abuse cases, developers write malicious test cases that exercise how an attacker would use the system in an attempt to compromise it, steal information, damage it, or otherwise harm national security.  

Unit tests should also be developed from the mindset of an attacker.  Managers and developers should always be cognizant of security risks as unit tests are written, ensuring that unit tests cover common security holes such as the sanitization of inputs, to include, but not limited to: user inputs, network I/O, database transactions, and sensor inputs.  A risk-based approach should be taken when developing security-focused unit tests.  Common vulnerabilities and high-threat vulnerabilities should be addressed first. Software security must start at the lowest levels of testing.  One cannot wait until the end of the development process to "bolt" security on.


Testing a GUI
--------------------

Although graphical user interfaces (GUI) may be more difficult to test than business logic, many tools exists to help automate GUI testing.  Furthermore, good design practices in separating and decoupling user interface code from the rest of the application will help tremendously in GUI testing.


Testing Tests
--------------------

Usually test code is very simple.  It flows from setting up pre-conditions, to executing the relevant unit, to assertion of post-conditions, to any cleanup code if necessary. This is often straight-line code with no branching.  However, if any test code becomes complex, including branching or calculations of its own, then it should be tested as well.  It is necessary to test our tests.  This happens implicitly during TDD.  Step 2 of the TDD cycle requires all tests to be run to ensure the new test fails.  However, when the test is more complex than just straight-line code, it may be necessary to write additional test cases that explicitly verify the complex test.


Conclusion
--------------------

This lesson covered TDD and unit testing.  In it, we introduced the concepts, discussed the benefits, and explored the risks of TDD and unit testing.  We also considered strategies to deal with large systems and legacy systems.  Finally we addressed software security, GUI testing, and testing tests as it applies to TDD and unit testing.  Following the above guidance will increase the quality of your code and help keep your project be on time and under budget.  You are now ready to answer the discussion board questions on Blackboard and then move on to [Tutorial 1:  JavaScript Tutorial](javascript-tutorial.html).


References
--------------------

<dl>

<dt>BECK02</dt>
<dd>
Beck, Kent.  <em>Test-Driven Development By Example</em>, 2002
</dd>

<dt>FOWL99</dt>
<dd>
Fowler, Martin.  <em>Refactoring Improving the Design of Existing Code</em>, 1999
</dd>

<dt>HUNT00</dt>
<dd>
Hunt, Andrew and Thomas, Dave.  <em>The Pragmatic Programmer</em>, 2000
</dd>

<dt>JORG08</dt>
<dd>
Jorgensen, Paul C. <em>Software Testing A Craftsman's Approach</em>, 3rd Edition, 2008
</dd>

<dt>MCCO04</dt>
<dd>
McConnell, Steve.  <em>Code Complete</em>, 2nd Edition, 2004
</dd>

<dt>WIKBDD</dt>
<dd>
Wikipedia.  <em>Behavior-driven development</em>,
<a href="http://en.wikipedia.org/wiki/Behavior_driven_development">
http://en.wikipedia.org/wiki/Behavior_driven_development</a>
[online; accessed 22-March-2013]
</dd>

</dl>
