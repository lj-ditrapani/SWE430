SWE 430 Tutorial 2:  qUnit Tutorial
========================================================================

You can interact with the code from the following qUnit tutorial at jsbin.com:

- [jsbin qUnit Tutorial](http://jsbin.com/swe430_qunit_tutorial/latest/edit?javascript,live)


[qUnit](http://qunitjs.com) is the Javascript unit testing framework we use in all the examples and assignments.  It exports several functions used for testing.  Make sure you understand the functions below.  The qUnit documentation is available on their
[website](http://api.qunitjs.com)
for more detailed information.  We will only make use of the functions below, so don't worry about trying to learn the entire API (which is quite small).

Here is an example of each function and a link to the qUnit documentation for more details:

test

The 'test' function is the core of the qUnit framework.  Each test function defines a new test case.  The test function takes another, user-define callback function as a parameter.  The callback function contains the actual test code to be run.  When you call the 'test' function, you are telling qUnit to add the callback function to the test suite.
[test documentation](http://api.qunitjs.com/test/)

    // test() has 2 parameters, a string title and a function
    test('test title', func)    
                                
    // Define a function to test
    function func() {
        equal(1 + 1, 2);
    }

    // Add 'func' to the test suite
    test('Test 1 + 1 = 2', func) 

    // This is identical to the above.  The function is 
    // anonymous; it is defined in-line without a name
    test('Test 1 + 1 = 2', function() {
        equal(1 + 1, 2);
    });
                                

from now on, we will anonymous functions in our tests because it 
is easier and less cluttered

ok

'ok' is the first of four 'assert' functions we use (ok, equal, deepEqual, and throws are all assert functions).  'Assert' functions are what we use to assert post-conditions on our tests.  'ok' is the simplest of the assert functions.  It merely checks that the value passed in is true.  If not, it automatically fails.
[ok documentation](http://api.qunitjs.com/ok/)

    # If any assertion fails, the entire test fails
    test 'x is true', ->
        x = true
        ok x                    # Passes, because x is true
        y = false
        ok y                    # Fails because y is false

The above test fails because the second assertion failed.

equal

'equal' is another assert function.  It takes two arguments and checks that they are equal.
[equal documentation](http://api.qunitjs.com/equal/)

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
[deepEqual documentation](http://api.qunitjs.com/deepEqual/)

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
[throws documentation](http://api.qunitjs.com/throws/)

    test "Divide by zero", ->
        # x is undefined
        throws x                # Trying to evaluate x raises an error

This test passes because an error was thrown as expected.

module

Tests can be organized into modules.
[module documentation](http://api.qunitjs.com/module/)

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
[setup example in module documentation](http://api.qunitjs.com/module/)

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
