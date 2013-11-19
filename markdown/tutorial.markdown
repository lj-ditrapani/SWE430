SWE 430 Tutorial
========================================================================


You can interact with the code from the following CoffeeScript and qUnit tutorials at jsbin.com:

- [jsbin CoffeeScript Tutorial](http://jsbin.com/swe430_tutorial/latest/edit?javascript,console,live)
- [jsbin qUnit Tutorial](http://jsbin.com/swe430_qunit_tutorial/latest/edit?javascript,live)


CoffeeScript
------------

All our examples and exercises are in CoffeScript.  A quick overview of CoffeScript is available at <a href="http://coffeescript.org">coffeescript.org</a>.  The overview provides several code snippets.  You can test a code snippet by clicking the 'load' button and then run it using the 'run' button.  You can also modify any snippet you load.  Make sure you understand the topics listed below.  If the overview is not enough, complete books are also available: 
<a href="http://autotelicum.github.com/Smooth-CoffeeScript/">Smooth CoffeeScript</a>
(if link is blocked, here's the pdf of  
<a href="SmoothCoffeeScript.pdf">Smooth CoffeeScript</a>) and
<a href="http://arcturo.github.io/library/coffeescript/02_syntax.html">The Little Book on CoffeeScript</a> (if link is blocked, you can also read it on Safari Online.)  If you have any questions or run into any problems, please don't hesitate to ask me for help!

Note:  **Everything you need to run CoffeeScript and qUnit is contained within the environment for each example and exercise.  You do not need to install anything.**

whitespace

Most programmers use whitespace to give a visual layout to their code.  In CoffeeScript, this idea is taken a step further.  Whitespace is used to define both the visual layout and the syntax of the program.  It makes the code more readable by enforcing consistent layout while eliminating needless syntax tokens  (semicolons, braces, parentheses) already expressed by the layout.

From coffeescript.org:

"First, the basics: CoffeeScript uses significant whitespace to delimit blocks of code."

    f = (x) -> x * x            # Function defined in-line, compiles ok

    f = (x) ->                  # Function defined with body as sub-block
        x = 2                   # Proper indentation
        x + 5                   # Every statement in body lines up

    f = (x) ->                  # Improper indentation
        x = 2                   # Statements in body must line up
          x + 5                 # Should be 2 spaces &lt;-

    if good                     # Proper indentation of blocks
        do_a()                  # if and else line up
    else
        do_b()

    if bad
        do_a()
        else                    # Improper indentation, will not compile
        do_b()

From wikipedia:
"Coffeescript is very sensitive to whitespace, counting a tab as a single space."

When writing CoffeeScript, it's best not to use tabs and instead just stick with spaces.  Most text editors and IDEs have a setting to change tabs to spaces.  For example, when I type Tab, my editor inserts 4 spaces instead.

functions

    square = (x) -> x * x       # -> defines a function
    square 3                    # Returns 9

    alias = square              # Both square and alias refer to the 
                                # same function
    alias 3                     # Also returns 9

    call_with_3 = (f) -> f 3    # A function that takes a function as a
                                # parameter and calls it
    call_with_3 square          # Also return 9

Functions are defined with `->`.  Functions are first-class objects, can create closures, be assigned to variables, passed into functions as parameters and returned from functions as a return value.

String interpolation

    obj = {x: 7}                # An object with x = 7
    "3 + 4 = #{obj.x}"          # content inside #{} is executed
                                # returns "3 + 4 = 7"

The @ symbol

    @x                          # means this.x (replace @ with this.)
                                # 'this' is dynamically scoped

Classes and Constructors

    class A                 
        constructor: (@x) ->    # Class A has a property named x

        f: -> @x                # The method f() returns the value of x

Inheritance and polymorphism with the "extends" and "super" keywords

    class B extends A           # Inherits from class A
        constructor: ->
            super 5             # Call's class A constructor

        f: -> super()           # Call's class A's f() method

Accessing an object's property using a string

    b = new B                   # the x property is set to x
    b["x"]                      # returns 5

Regular Expressions

    re = /\d\d/                 # matches 2 digits


qUnit
-----

<a href="http://qunitjs.com">qUnit</a> is the Javascript unit testing framework we use in all the examples and exercises.  It exports several functions used for testing.  Make sure you understand the functions below.  The qUnit documentation is available on their <a href="http://api.qunitjs.com">website</a> for more detailed information.  We will only make use of the functions below, so don't worry about trying to learn the entire API (which is quite small).

The qUnit documentation is written for Javascript, not CoffeeScript, so the syntax is different, but the semantics are the same regardless of the language.

Here is an example of each function in CoffeeScript and a link to the qUnit documentation for more details:

test

The 'test' function is the core of the qUnit framework.  Each test function defines a new test case.  The test function takes another, user-define callback function as a parameter.  The callback function contains the actual test code to be run.  When you call the 'test' function, you are telling qUnit to add the callback function to the test suite.
<a href="http://api.qunitjs.com/test/">test documentation</a>

    test 'test title', func     # test has 2 parameters, a string title
                                # and a function

    func = -> equal 1 + 1, 2    # Define a function to test

    test 'Test 1 + 1 = 2', func # Add 'func' to the test suite

    test 'Test 1 + 1 = 2', ->   # This is identical to the above.
        equal 1 + 1, 2          # The function is anonymous; it is
                                # defined in-line without a name

from now on, we will anonymous functions in our tests because it 
is easier and less cluttered

ok

'ok' is the first of four 'assert' functions we use (ok, equal, deepEqual, and throws are all assert functions).  'Assert' functions are what we use to assert post-conditions on our tests.  'ok' is the simplest of the assert functions.  It merely checks that the value passed in is true.  If not, it automatically fails.
<a href="http://api.qunitjs.com/ok/">ok documentation</a>

    # If any assertion fails, the entire test fails
    test 'x is true', ->
        x = true
        ok x                    # Passes, because x is true
        y = false
        ok y                    # Fails because y is false

The above test fails because the second assertion failed.

equal

'equal' is another assert function.  It takes two arguments and checks that they are equal.
<a href="http://api.qunitjs.com/equal/">equal documentation</a>

    test 'x equals y', ->       # fails
        x = 5
        y = 7
        equal x, y

    test 'x equals z', ->       # passes
        x = 5
        z = 5
        equal x, z, 'x = z'

deepEqual

'deepEqual' is like equal except it recursively checks the values inside of lists and objects.
<a href="http://api.qunitjs.com/deepEqual/">deepEqual documentation</a>

    test 'two arrays with equal', ->
        a = [1, 2]
        b = [1, 2]
        equal a, b              # fails, two distinct array objects

    test 'two arrays with deepEqual', ->
        a = [1, 2]
        b = [1, 2]
        deepEqual a, b          # passes, same values within arrays

throws

'throws' is used to assert a callback throws an exception.  This allows us to test the behavior of our code when things go amiss.
<a href="http://api.qunitjs.com/throws/">throws documentation</a>

    test "Divide by zero", ->
        # x is undefined
        throws x                # Trying to evaluate x raises an error

This test passes because an error was thrown as expected.

module

Tests can be organized into modules.
<a href="http://api.qunitjs.com/module/">module documentation</a>

    module 'Module A'           # Until we define another module
                                # all new tests will belong to A

    test 'test 1.1', ->         # Belongs to module A
        ok true

    test 'test 1.2', ->         # Belongs to module A
        ok true

    module 'Module B'           # All new test will belong to B

    test 'test 2.1', ->         # Belongs to module B
        ok true

    test 'test 2.2', ->         # Belongs to module B
        ok true

setup

When using modules, you can factor your common setup code into the module's setup method.
<a href="http://api.qunitjs.com/module/">setup example in module documentation</a>

    module 'Module A', {
        setup: ->               # Common setup code
            @x = 5              # @ refers to the module
            @y = 7              
            @z = 5
    }

    test 'x = y', ->            # tests are run inside of Module A
        equal @x, @y            # so x and y are available via @

    test 'x = z', ->            # @ means this. and this refers to
        equal @x, @z            # Module A
