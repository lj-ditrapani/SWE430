SWE 430 Tutorial 1:  JavaScript Tutorial
========================================================================

This tutorial gives a short introduction of the JavaScript basics you
will need to understand to complete the course.
The estimated time to complete this tutorial is 1 hour.

All the examples and assignments of this course are in JavaScript,
so it is important you understand the topics listed below.
If the overview is not enough,a book with addition information
is available at the end of the tutorial.
If you have any questions or run into any problems,
please don't hesitate to ask me for help!

You can interact with the code from this JavaScript tutorial
at jsbin.com:

- [jsbin JavaScript Tutorial](http://jsbin.com/swe430_javascript_tutorial/latest/edit?javascript,console)

[Instructions](jsbin-instructions.html) for using jsbin are available.


Note:  **Everything you need to run JavaScript and qUnit is contained
within the environment for each example and assignment.
You do not need to install anything.**


Comments
--------

Comments begin with `//` and continue until the end of the line.
They are ignored by the JavaScript interpreter.
Multi-line (or block) comments start with `/*` and end with a `*/`.
Comments provide a means to communicate information that may not be
immediately evident in the code itself.
Comments are often used to document code.
They are also used to provide explanations in tutorials.

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

A Boolean type can have one of two values, `true` or `false`.

The Number type represents numbers and can have values such as
0, 5, 0.01, -500.76, -1, etc.

The String type represents a sequence of characters.
String is defined by surrounding a sequence of characters with
single quotes (`'` `'`) or double quotes (`"` `"`).

    '';                         // An empty string
    'I am a string';
    "I am also a string";
    // A double quoted string can contain single quotes
    "I'm a string";
    // A single quoted string can contain double quotes
    'I am a "string"';

Arrays represent sequences of arbitrary values.
They are defined using brackets (`[` `]`).

    // An empty array
    [];
    // An array containing numbers
    [1, 2, 3];
    // An array of numbers and string
    ['one', 2, 'three'];
    // Arrays can be nested,
    // this array contains 2 other arrays
    ['mixed array', [1, 2, 3], ['one', 'two']];

Like Arrays, Objects are also a composite data type.
However, instead of being a sequence of values,
an object is a collection of named properties (also called attributes).
Objects are defined using the curly braces (`{` `}`).
A property is associated with a value using the colon (`:`).
Property-value pairs are separated by a comma (`,`).
    
    // An empty object
    {};
    // An object with 2 properties, 'a' and 'b'.
    // The string 'a' is associated with the value 1
    // The string 'b' is associated with the value 2
    {a: 1, b: 2};
    // Properties can refer to any type as their value
    {
        key1: false,            // Boolean
        key2: 'a string',       // String
        key3:  -42.7,           // Number
        key4: [1, 2, 3, 4],     // Array
        key5: {a: 1, b: 2}      // Object
    };

Functions are also a type in JavaScript.
We will discuss them later on in the tutorial.


Var Declarations and Assignment
-------------------------------

To declare a new variable, precede it with the var keyword.  This ensures that it is only defined in the local scope and not globally.  Because  JavaScript is dynamically typed, you do not specify the type of the variable as you would in statically type languages like Java, C#, and C++.

    var x;                  // OK, x defined locally
    y = 5;                  // Bad; missing var; y defined globally

Multiple variables can be declared in the same `var` statement.  It is best practice to declare all the local variables of a function at the beginning of the function.  The `=` operator is the assignment operator.  It assigns the value on the right-hand-side to the variable on the left-hand-side so that the variable refers the value.

    // Declare 5 variables in one var statement
    var myBool, myNumber, myString, myArray, myObject;
    // Assign values to all 5 variables
    myBool = true;          // Assign true to myBool
    myNumber = 5;           // Assign 5 to myNumber
    myString = 'hello';
    myArray = [true, false];
    myObject = {a: 1, b: myArray}
    // myObject.b refers to the array [true, false]


Variables can be reassigned to different values over time.

    var x = 5;              // Declare x and assign 5 to it
    x = 3;                  // Reassign x to have the value 3
    x = x + 5;              // Make x 5 + the current value of x
                            // x now has the value of 8
    x += 5;                 // Shorthand for the previous line 
                            // x now has the value of 13


Math Operators
--------------

    x + 7;                  // Adds 7 to the value of x
    3 * y;                  // Multiply 3 by y
    x - 7;                  // Subtracts 7 from the value of x
    3 / y;                  // Divide 3 by y


Boolean Comparison Operators
----------------------------

JavaScript has boolean operators that allow comparisons between two
values.
The operators return `true` if the comparison is true and
`false` otherwise.

<table>

<tr>
<th>Symbol</th>
<th>Name</th>
</tr>

<tr>
<td>===</td>
<td>Exactly equal to</td>
</tr>

<tr>
<td>!==</td>
<td>Not exactly equal to</td>
</tr>

<tr>
<td>&lt;</td>
<td>Less than</td>
</tr>

<tr>
<td>&gt;</td>
<td>Greater than</td>
</tr>

<tr>
<td>&lt;=</td>
<td>Less than or equal to</td>
</tr>

<tr>
<td>&gt;=</td>
<td>Greater than or equal to</td>
</tr>

<tr>
<td>&amp;&amp;</td>
<td>Logical AND</td>
</tr>

<tr>
<td>||</td>
<td>Logical OR</td>
</tr>

</table>

Examples:

    5 === 5;                    // true
    5 !== 5;                    // false
    2 === 3;                    // false
    2 !== 3;                    // true
    2 < 3;                      // true
    5 < 3;                      // false
    5 > 3;                      // true
    2 > 3;                      // false
    2 <= 2;                     // true
    2 <= 3;                     // true
    5 <= 3;                     // false
    3 >= 3;                     // true
    5 >= 3;                     // true
    2 >= 3;                     // false
    true && false;              // false
    false && true;              // false
    true && true;               // true
    true || false;              // true
    false || true;              // true
    false || false;             // false

The `!` operator is a unary operator (it only take one argument as opposed to two arguments).  It negates the boolean value of its argument.

    !true;                      // false
    !false;                     // true


Strings
-------

A string is a sequence a characters.
You can index into a string using the string's `charAt()` method.
String indexing is 0-based.
The first character is at index 0,
the second at index 1, and so on.
The string's `charCodeAt()`
method returns the ASCII/UTF-8 numerical value of the character
at the given index.

    var s = 'hello';
    s.indexOf('he');            // Returns 0
    s.indexOf('o');             // Returns 4
    s.indexOf('llo');           // Returns 2
    s.charAt(0);                // Returns 'h'
    s.charAt(1);                // Returns 'e'
    s.length;                   // Returns 5
    s.charAt(s.length - 1);     // Returns 'o'
    s.charCodeAt(1);            // Returns 101

The plus (`+`) operator can be used to concatenate strings together.
    
    var s, w;
    w = 'world';
    // The + concatenates (joins) strings together
    s = 'hello' + ' ' + w;
    // s now refers to the string 'hello world'

The `String.slice()` method returns a substring of the string.

    var s = 'hello world';
    s.slice(6);                 // Returns 'world'
    s.slice(0, 5);              // Returns 'hello'
    s.slice(5, 6);              // Returns ' ' (a space)

The String methods `toUpperCase()` and `toLowerCase()` return a string
with all upper-case or all lower-case letters respectively.

    var s1, s2;
    s1 = 'hello';
    s2 = s1.toUpperCase();      // s2 now refers to 'HELLO'
    s2.toLowerCase();           // Returns 'hello'

The String method `split()` can be used to break a string into an array
of its substrings.

    var s;
    s = '192.168.0.100';
    s.split('.');               // Returns ['192', '168', '0', '100']
    s = 'hello world';
    s.split(' ');               // Returns ['hello', 'world']

Useful String Methods:
<table>

<tr>
<th>Method</th>
<th>Use</th>
</tr>

<tr>
<td>indexOf()</td>
<td>Return the index of the substring in the string or -1 if the substring in not found in the string.</td>
</tr>

<tr>
<td>charAt()</td>
<td>Return the character found at the given index.</td>
</tr>

<tr>
<td>charCodeAt()</td>
<td>Return the numerical value of the character found at the given index.</td>
</tr>

<tr>
<td>slice()</td>
<td>Return a substring defined by the given index(es).</td>
</tr>

<tr>
<td>toUpperCase()</td>
<td>Return the string with all letters in upper-case.</td>
</tr>

<tr>
<td>toLowerCase()</td>
<td>Return the string with all letters in lower-case.</td>
</tr>

<tr>
<td>split()</td>
<td>Split the original string and return an array of substrings</td>
</tr>

</table>


Arrays
------

Arrays can be created with the [] notation.
Using [] on an existing array allows you to index into the array.
Array indexing is 0-based;
the first element is a index 0, the second at index 1, and so forth.
    
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

Elements can be appended to the array with the push() method.

    // New empty array
    var a = [];
    // Append the element 5 to the end of the array
    a.push(5);
    // now the array is [5]
    a.push(3);              
    // now the array is [5, 3]
    // Create another array with the same elements
    a = [5, 3];             
    a[0];                   // Index into the array; returns 5
    a[1];                   // Index into the array; returns 3


Accessing an object's properties
--------------------------------

    b = {};                 // Create an empty objet
    b.x = 5;                // Add a property x with value 5
    // A property can be accessed using the '.' notation
    b.x;                    // Returns 5
    // or by using the string '[]' notation
    b['x'];                 // Also returns 5


Namespaces
----------

JavaScript doesn't directly support namespaces (also called modules.)  However, objects can be used to simulate a namespace.  Below we simulate a module by creating an object and naming it mod.  We then define a property 'x' on the mod object.  The variable x is thus 'hidden' in the mod namespace.

    window.mod = {};        // Create an empty object literal and attach 
                            // it to the global window object
    mod.x = 7;              // The variable x is not visible globally but 
                            // only accessible from the mod object.
    x                       // Error, x is undefined!
    mod.x + 10;             // OK, accessing x from the mod object.



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


If Statement
------------

The `if` statement can be used to invoke conditional execution.

In the example below,
the function `do_a()` is only executed if the variable `good` is set to `true`.  Regardless of whether `do_a()` is executed or not, the function `always_do_c()` will be executed.

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


Conclusion
----------

If you would like more details on any of the above topics, you can
browse 
[Eloquent JavaScript](http://eloquentjavascript.net/contents.html),
a free online interactive book on JavaScript.
The relevant chapters of the book are listed below.

- [Basics](http://eloquentjavascript.net/chapter2.html)
- [Functions](http://eloquentjavascript.net/chapter3.html)
- [Objects and Arrays](http://eloquentjavascript.net/chapter4.html)

The Mozilla Developer Network also provides a nice introduction with their [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide).

Now that you have an understanding of the JavaScript basics, you are ready for the [qUnit Tutorial](qunit-tutorial.html).

