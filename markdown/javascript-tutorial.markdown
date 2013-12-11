SWE 430 Tutorial 1:  JavaScript Tutorial
========================================================================

This tutorial gives a short introduction of the JavaScript basics you will need to understand to complete the course.  The estimated time to complete this tutorial is 1 hours.

All our examples and assignments are in JavaScript.  Make sure you understand the topics listed below.  If the overview is not enough, complete books are also available: 

If you have any questions or run into any problems, please don't hesitate to ask me for help!

You can interact with the code from this JavaScript tutorial at jsbin.com:

- [jsbin JavaScript Tutorial](http://jsbin.com/swe430_javascript_tutorial/latest/edit?javascript,console,live)


Note:  **Everything you need to run JavaScript and qUnit is contained within the environment for each example and assignment.  You do not need to install anything.**



Math Operators
--------------

    x + 7;                  // Adds 7 to the value of x
    3 * y;                  // Multiply 3 by y
    x - 7;                  // Subtracts 7 from the value of x
    3 / y;                  // Divide 3 by y


var declarations
----------------

To declare a new variable, precede it with the var keyword.  This ensures that it is only defined in the local scope and not globally.  Because  JavaScript is dynamically typed, you do not specify the type of the variable as you would in statically type languages like Java, C#, and C++.

    var x, y, z;
    x = 5;
    y = 'hello';
    z = [true, false];
    var x;                  // Ok, x defined locally
    y = 5;                  // Bad; missing var; y defined globally
    var a, b, c;            // Multiple variables separated by commas 
                            // can be declared on the same line


Arrays
------
    
    var list;
    // Create a list with []
    list = [];
    // You can specify initial values for a list
    list = ['a', 'b', 'c'];
    // Use [] to return the value of the list at the given index
    list[0];                    // Returns 'a'
    list[1];                    // Returns 'b'
    list[2];                    // Returns 'c'
    list.length;                // Returns 3


Control flow
------------

    if good
        do_a()
    else
        do_b()


functions
---------

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


Namespaces
----------

JavaScript doesn't directly support namespaces (also called modules.)  However, objects can be used to simulate a namespace.  Below we simulate a module by creating an object and naming it mod.  We then define a property 'x' on the mod object.  The variable x is thus 'hidden' in the mod namespace.

    window.mod = {};        // Create an empty object literal and attach 
                            // it to the global window object
    mod.x = 7;              // The variable x is not visible globally but 
                            // only accessible from the mod object.
    x                       // Error, x is undefined!
    mod.x + 10;             // OK, accessing x from the mod object.


Assignment
---------------------

As with many programming languages, = is used for assigning a value to a variable.

    var x = 5;              // Declare x and assign 5 to it
    x = 3;                  // Reassign x to have the value 3
    x = x + 5;              // Make x 5 + the current value of x
                            // x now has the value of 8
    x += 5;                 // Shorthand for the previous line 
                            // x now has the value of 13


Arrays
------

Arrays can be created with the [] notation.  Elements can be appended to the array with the push() method.  Using [] on an existing array allows you to index into the array.  Array indexing is 0 based.

    var a = [];             // New empty array
    a.push(5);              // Append the element 5 to the end of the array
                            // now the array is [5]
    a.push(3);              // now the array is [5, 3]
    a = [5, 3];             // Create another array with the same elements
    a[0];                   // Index into the array; returns 5
    a[1];                   // Index into the array; returns 3


Iteration
---------

Iteration can be accomplished using 'for' loops.  The for loop has three parts:  initialization, condition, and step operation.

for loop

    // Displays the elements of the array one at a time
    var i, a;                   // Declare variables
    a = [1, 2, 3];              // Array with 3 elements
    // i iterates from 0 to 2; providing the indexes of the array
    for (i = 0; i &lt; array.length; i += 1) {
        alert(a[i]);            // Each element is displayed
    }


Functional Constructs
---------------------

Functions are defined using the "function" keyword.  JavaScript supports both named and anonymous functions (lambdas in other languages such as scheme, Haskell, ruby and python.)


function
--------

    function square(x) {        // Define a function named square
        return x * x;
    }

    // Invoke/call the square function with different inputs
    square(2);                  // Returns 4
    square(4);                  // Returns 16

    function(x) {               // Defines the same function, 
        return x * x;           // but does not name it
    };

Anonymous functions can be used to create a private namespace to prevent temporary variables from polluting the global namespace or colliding with global variable names.


Anonymous function to hid temporary variables
---------------------------------------------

    x = 5;                      // Global variable

    (function() {
        var x = 7;              // Separate, locally scoped variable x
        var temp = x + 9;       // temp is only defined locally
        window.mod.y = temp * 3;
    }());                       // Notice the function is immediately 
                                // called
                                // x is still 5
                                // temp is undefined


Conclusion
----------

If you would like more details on any of the above topics, you can
browse 
[Eloquent JavaScript](http://eloquentjavascript.net/contents.html)
a free online interactive book on JavaScript.
The relevant chapters of the book are listed below.

- [Basics](http://eloquentjavascript.net/chapter2.html)
- [Functions](http://eloquentjavascript.net/chapter3.html)
- [Objects and Arrays](http://eloquentjavascript.net/chapter4.html)

The Mozilla Developer Network also provides a nice introduction in their [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)

Now that you have an understanding of the JavaScript basics, you are ready for the [qUnit Tutorial](qunit-tutorial.html).

