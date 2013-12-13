SWE 430 Tutorial 1:  JavaScript Tutorial
========================================================================

This tutorial gives a short introduction of the JavaScript basics you will need to understand to complete the course.  The estimated time to complete this tutorial is 1 hour.

All the examples and assignments of this course are in JavaScript, so it is important you understand the topics listed below.  If the overview is not enough, a book with addition information is available at the end of the tutorial.  If you have any questions or run into any problems, please don't hesitate to ask me for help!

You can interact with the code from this JavaScript tutorial at jsbin.com:

- [jsbin JavaScript Tutorial](http://jsbin.com/swe430_javascript_tutorial/latest/edit?javascript,console)


Note:  **Everything you need to run JavaScript and qUnit is contained within the environment for each example and assignment.  You do not need to install anything.**


Comments
--------

Comments begin with `//` and continue until the end of the line.  They are ignored by the JavaScript interpreter.  Multi-line (or block) comments start with `/*` and end with a `*/`.  Comments provide a means to communicate information that may not be immediately evident in the code itself.  Comments are often used to document code.  They are also used to provide explanations in tutorials.

    // This is a single line comment

    // Comments are not code, 
    // they are ignored by the JavaScript interpreter

    /* 
       This is a multi-line comment,
       it started with /*
       It can contain anything {[()]}
       end comment
    */


Basic Types
-----------

JavaScript has 5 basic types that we will use in this course:
Boolean, Number, String, Array, and Object.
Boolean, Number and String are primitive types
while Array and Object are composite types.

A Boolean type can have one of two values, `True` or `False`.

The Number type represents numbers and can have values such as
0, 5, 0.01, -500.76, -1, etc.

The String type represents a sequence of characters.
String is defined by surrounding a sequence of characters with
single quotes (`'` `'`) or double quotes (`"` `"`).

    ''                          // An empty string
    'I am a string'
    "I am also a string"
    // A double quoted string can contain single quotes
    "I'm a string"
    // A single quoted string can contain double quotes
    'I am a "string"'

Arrays represent sequences of arbitrary values.  They are defined using brackets (`[` `]`).

    // An empty array
    []
    // An array containing numbers
    [1, 2, 3]
    // An array of numbers and string
    ['one', 2, 'three']
    // Arrays can be nested,
    // this array contains 2 other arrays
    ['mixed array', [1, 2, 3], ['one', 'two']]

Like Arrays, Objects are also a composite data type.  However, instead of being a sequence of values, an object is a collection of named attributes.  Objects are defined using the curly braces (`{` `}`).
    
    // An empty object
    {}
    // An object with 2 attributes, 'a' and 'b'.
    // The string 'a' is associated with the value 1
    // The string 'b' is associated with the value 2
    { a: 1, b: 2}
    // Attributes can refer to any type as their value
    {
        key1: False,            // Boolean
        key2: 'a string',       // String
        key3:  -42.7,           // Number
        key4: [1, 2, 3, 4],     // Array
        key5: {a: 1, b: 2}      // Object
    }

Functions are also a type in JavaScript.
We will discuss them later on in the tutorial.


Var Declarations and Assignment
-------------------------------

To declare a new variable, precede it with the var keyword.  This ensures that it is only defined in the local scope and not globally.  Because  JavaScript is dynamically typed, you do not specify the type of the variable as you would in statically type languages like Java, C#, and C++.

    var x, y, z;
    x = 5;
    y = 'hello';
    z = [true, false];
    var x;                  // Ok, x defined locally
    y = 5;                  // Bad; missing var; y defined globally
    var a, b, c;            // Multiple variables separated by commas 


Assignment
----------

As with many programming languages, = is used for assigning a value to a variable.

    var x = 5;              // Declare x and assign 5 to it
    x = 3;                  // Reassign x to have the value 3
    x = x + 5;              // Make x 5 + the current value of x
                            // x now has the value of 8
    x += 5;                 // Shorthand for the previous line 
                            // x now has the value of 13
                            // can be declared on the same line

Math Operators
--------------

    x + 7;                  // Adds 7 to the value of x
    3 * y;                  // Multiply 3 by y
    x - 7;                  // Subtracts 7 from the value of x
    3 / y;                  // Divide 3 by y



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


Accessing an object's property using a string
---------------------------------------------

    b = new B                   # the x property is set to x
    b["x"]                      # returns 5


Namespaces
----------

JavaScript doesn't directly support namespaces (also called modules.)  However, objects can be used to simulate a namespace.  Below we simulate a module by creating an object and naming it mod.  We then define a property 'x' on the mod object.  The variable x is thus 'hidden' in the mod namespace.

    window.mod = {};        // Create an empty object literal and attach 
                            // it to the global window object
    mod.x = 7;              // The variable x is not visible globally but 
                            // only accessible from the mod object.
    x                       // Error, x is undefined!
    mod.x + 10;             // OK, accessing x from the mod object.


if Statement
------------

The function `do_a()` is only executed if the variable `good` is set to `true`.  Regardless of whether `do_a()` is executed or not, the function `always_do_c()` will be executed.

    if (good) {
        do_a();
    }
    always_do_c();

By including an `else` clause with the `if` statement, if the variable `good` is true, `do_a()` is executed, otherwise, `do_b()` is executed.  Either one or the other is executed, but not both.  Finally, `always_do_c()` executed regardless of the value of `good`.

    if (good) {
        do_a();
    } else {
        do_b();
    }
    always_do_c();


For loop
--------

Iteration can be accomplished using 'for' loops.  The for loop has three parts:  initialization, condition, and step operation.

    // Displays the elements of the array one at a time
    var i, a;                   // Declare variables
    a = [1, 2, 3];              // Array with 3 elements
    // i iterates from 0 to 2; providing the indexes of the array
    for (i = 0; i < array.length; i += 1) {
        alert(a[i]);            // Each element is displayed
    }


Functions
---------

Functions are defined using the `function` keyword.
JavaScript supports both named and anonymous functions
(also called lambdas in many other languages such as scheme, Haskell,
ruby and python.)
Functions are first-class objects, can be assigned to variables,
can be passed into functions as parameters,
and can be returned from functions as a return value.


    function square(x) {        // Define a function named square
        return x * x;
    }

    // Invoke/call the square function with different inputs
    square(2);                  // Returns 4
    square(4);                  // Returns 16

    function(x) {               // Defines the same function, 
        return x * x;           // but does not name it
    };

    // Both square and alias refer to the same function
    alias = square;
    alias(2);                   // Also returns 4

    // A function that takes a function as a parameter and calls it
    call_with_2 = function(f) {
        f(2);
    };

    // Also return 4
    call_with_2(square);



Anonymous function to hide temporary variables
---------------------------------------------

Anonymous functions can be used to create a private namespace to prevent temporary variables from polluting the global namespace or colliding with global variable names.

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

The Mozilla Developer Network also provides a nice introduction with their [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide).

Now that you have an understanding of the JavaScript basics, you are ready for the [qUnit Tutorial](qunit-tutorial.html).

