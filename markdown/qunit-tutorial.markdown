SWE 430 Tutorial 2:  qUnit Tutorial
========================================================================

You can interact with the code from the following qUnit tutorial at jsbin.com:

- [jsbin qUnit Tutorial](http://jsbin.com/swe430_qunit_tutorial/latest/edit?javascript,live)

[Instructions](jsbin-instructions.html) for using jsbin are available.

[qUnit](http://qunitjs.com) is the JavaScript unit testing framework we use in all the examples and assignments.  It exports several functions used for testing.  Make sure you understand the functions below.  The qUnit documentation is available on their
[website](http://api.qunitjs.com)
for more detailed information.  We will only make use of the functions below, so don't worry about trying to learn the entire API (which is quite small anyway).

Here is an example of each function and a link to the qUnit documentation for more details:


test
----

The 'test' function is the core of the qUnit framework.  Each test function defines a new test case.  The test function takes another, user-define callback function as a parameter.  The callback function contains the actual test code to be run.  When you call the 'test' function, you are telling qUnit to add the callback function to the test suite.
[test documentation](http://api.qunitjs.com/test/)

    // test() has 2 parameters, a string title and a function
    test('test title', func);
                                
    // Define a function to test
    function func() {
        equal(1 + 1, 2);
    }

    // Add 'func' to the test suite
    test('Test 1 + 1 = 2', func);

    // This is identical to the above.  The function is
    // anonymous; it is defined in-line without a name
    test('Test 1 + 1 = 2', function() {
        equal(1 + 1, 2);
    });

From now on, we will use anonymous functions in our tests because it 
is easier and less cluttered


ok
---

'ok' is the first of four 'assert' functions we use (ok, equal, deepEqual, and throws are all assert functions).  'Assert' functions are what we use to assert post-conditions on our tests.  'ok' is the simplest of the assert functions.  It merely checks that the value passed in is true.  If not, it automatically fails.
[ok documentation](http://api.qunitjs.com/ok/)

    // If any assertion fails, the entire test fails
    test('x is true', function() {
        var x, y;
        x = true;
        // Passes, because x is true
        ok(x);
        y = false;
        // Fails because y is false
        ok(y);
    });

The above test fails because the second assertion failed.


equal
-----

'equal' is another assert function.  It takes two arguments and checks that they are equal.
[equal documentation](http://api.qunitjs.com/equal/)

    // fails
    test('x equals y', function() {
        var x, y;
        x = 5;
        y = 7;
        equal(x, y);
    });


    // passes
    test('x equals z', function() {
        var x, z;
        x = 5;
        z = 5;
        equal(x, z, 'x = z');
    });


deepEqual
---------

'deepEqual' is like equal except it recursively checks the values inside of arrays and objects.
[deepEqual documentation](http://api.qunitjs.com/deepEqual/)

    test('two arrays with equal', function() {
        var a, b;
        a = [1, 2];
        b = [1, 2];
        // fails, two distinct array objects
        equal(a, b);
    });


    test('two arrays with deepEqual', function() {
        var a, b;
        a = [1, 2];
        b = [1, 2];
        // passes, same values within arrays
        deepEqual(a, b);
    });


throws
------

'throws' is used to assert that a callback throws an error or exception.  This allows us to test the behavior of our code when things go amiss.
[throws documentation](http://api.qunitjs.com/throws/)

    test("Divide by zero", function() {
        // x is undefined
        // Trying to evaluate x raises an error
        throws(x);                
    });

This test passes because an error was thrown as expected.


module
------

Tests can be organized into modules.
[module documentation](http://api.qunitjs.com/module/)

    // Until we define another module
    // all new tests will belong to A
    module('Module A');


    // Belongs to module A
    test('test 1.1', function() {
        ok(true);
    });


    // Belongs to module A
    test('test 1.2', function() {
        ok(true);
    });


    // All new test will belong to B
    module('Module B');


    // Belongs to module B
    test('test 2.1', function() {
        ok(true);
    });


    // Belongs to module B
    test('test 2.2', function() {
        ok(true);
    });


setup
-----

When using modules, you can factor your common setup code into the module's setup method.  The setup method is defined inside an object as the value of the `setup` attribute.  The object is passed as the second parameter to the `module` function.
[setup example in module documentation](http://api.qunitjs.com/module/)

    module('Module A', {
        // Common setup code
        setup: function() {
            // 'this' refers to the module
            this.x = 5;
            this.y = 7;
            this.z = 5;
        }
    });


    // tests are run inside of Module A
    test('x = y', function() {
        // so x and y are available via the 'this' keyword
        equal(this.x, this.y);
    });


    // 'this' refers to Module A
    test('x = z', function() {
        equal(this.x, this.z);
    });


Conclusion
----------

You will be using the above functions in the examples and exercises.  With the JavaScript and qUnit tutorials under your belt, you can now move on to the [Environment Instructions](instructions.html).
