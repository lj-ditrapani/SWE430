SWE 430 Example 1 --- Running Tests
========================================================================

Before we jump into full-blown TDD, we will start by working through an
example and an assignment where all the tests are already written.
This will introduce you to running tests iteratively and writing code
incrementally while running your test suite between each increment of
code.

In this example, we will create a `stringInfo` module with the following
four string inspection functions.

<table>
<tr>
<th>Function Name</th><th>Input</th><th>Output</th>
</tr>
<tr>
<td>countUpperCaseLetters</td>
<td>String</td>
<td>Number of ASCII upper-case characters.</td>
</tr>
<tr>
<td>countLowerCaseLetters</td>
<td>String</td>
<td>Number of ASCII lower-case characters.</td>
</tr>
<tr>
<td>countControlCharacters</td>
<td>String</td>
<td>Number of ASCII control characters in the input string.</td>
</tr>
<tr>
<td>countNonASCIICharacters</td>
<td>String</td>
<td>Number of non-ASCII characters in the input string.</td>
</tr>
</table>

See the Wikipedia [ASCII page][ASCII] For information on the ASCII
encoding.

At the end of each section, a link to the current state of the `code.js`
file, which incorporates all of the work accomplished in the example
up to that point, is provided for you to check your work against so you
can follow along with confidence.

- [Example 1 zip Environment](example1.zip)
- [Example 1 jsbin Environment][jsbin example 1]

For a refresher on using the above environments, see the 
[Environment Instructions](instructions.html).

[jsbin example 1]: http://jsbin.com/swe430_example1/latest/edit?javascript,live
[ASCII]: http://en.wikipedia.org/wiki/ASCII



Create the `stringInfo` Module
------------------------------

First, we write the boilerplate code for the code.js file.
We will place all our code inside of an anonymous function so all our
code is encapsulated and hidden.
Any local variables we define with the `var` keyword and
any functions we define with the `function` keyword
will only be visible within the anonymous function.
This way, we do not pollute the global namespace.
To accomplish this, we simply define an anonymous function and
immediately execute it with the trailing `()`.

    (function() {
        'use strict';


    }());

Now, run the tests.  All four tests fail with the same error:
`'stringInfo' is undefined`.
So we will follow the advice of the test failure messages and create a
`stringInfo` object.  The `stringInfo` object will serve as the module
namespace.

    (function() {
        'use strict';


        var stringInfo = {};


        window.stringInfo = stringInfo;


    }());

We attach the `stringInfo` object to the global `window` object so that
it is visible and accessible outside of our anonymous function.

Run the tests again.
Now all four tests fail with the message that the function under test is
missing.
Let's start with the first one:
"`Object doesn't support property or method 'countUpperCaseLetters'`".

[code01.js](example1/code01.js)



Count Upper-case Characters
---------------------------

The error message is telling us we need to create a property named
'countUpperCaseLetters'.
We will start by creating an empty function with the appropriate name,
`countUpperCaseLetters`, attached to the `stringInfo` object.

    var stringInfo = {};


    stringInfo.countUpperCaseLetters = function() {
    };


    window.stringInfo = stringInfo;

With this change in place, the `stringInfo` object has a
`countUpperCaseLetters()` function defined,
but it doesn't do anything yet.
Let's run the tests again.
Now the "Count upper-case characters" test assertions
each fail with an `undefined` result.
Let's fill in the function to take in a string parameter and count the
number of upper-case letters found in the string.
The function should initialize a count variable to 0,
loop through each character in the string
and add one to the count if the character is an upper-case letter.
Looking at the table on the
[ASCII][]
Wikipedia page, we can see that upper-case characters have code values
between 64 and 90 inclusive, so these will be the values we will use to
compare the character code value against.

    stringInfo.countUpperCaseLetters = function(string) {
        var i, code, count = 0;
        for (i = 0; i < string.length; i += 1) {
            code = string.charCodeAt(i);
            if (code >= 65 && code <= 90) {
                count += 1;
            }
        }
        return count;
    };

In order to find the value of a character,
we use the `charCodeAt()` method of the String class.
It returns the numerical value of the character at the given position
of the string object.

Run the tests again.  Now the first test passes.
We do not have any duplicate code, and have nothing to refactor yet,
so we can skip the refactoring step.

[code02.js](example1/code02.js)



Count Lower-case Characters
---------------------------

The next failing test has an error message of
"`Object doesn't support property or method 'countLowerCaseLetters'`"
because the `countLowerCaseLetters()` function doesn't exist yet.
Let's declare the `countLowerCaseLetters()` function now.

    stringInfo.countLowerCaseLetters = function() {
    };

Run the tests again.
The assertions for the "Count lower-case characters" test all fail
with a result of `undefined`.
Let's implement the body of the `countLowerCaseLetters()` function.
First, we add the string parameter to the function.
The body of the function should be very similar to the
`countUpperCaseLetters()` function.
So let's copy the code we wrote for `countUpperCaseLetters()` and modify
it to make it count lower-case letters instead.

    stringInfo.countLowerCaseLetters = function(string) {
        var i, code, count = 0;
        for (i = 0; i < string.length; i += 1) {
            code = string.charCodeAt(i);
            if (code >= 97 && code <= 122) {
                count += 1;
            }
        }
        return count;
    };

All we had to do to make the code work is is change the two numbers
inside the `if` statement.
According to the [ASCII][] table, lower-case characters have code values
between 97 and 122 inclusive.
So we just change the 65 to 97 and the 90 to 122 and we are done.

Run the tests again.  Now the first and second tests pass.

[code03.js](example1/code03.js)



Refactor Code
-------------

Before we move on to the next test, we should refactor our code.
You probably know that copying and pasting code is generally a sign of
poor design.
The code for our `countLowerCaseLetters()` and `countUpperCaseLetters()`
functions are nearly identical.
We should factor-out the duplicate code into a common helper function
both functions can share.

As you have seen, the only difference between the two functions is the
criteria used to determine if the current character is one we want to
count or not.
So let's name our helper function `countCharacters()`.
It will take two parameters, a string and a predicate function.

The predicate function takes a character code value as input and returns
a boolean (`true` or `false`) value as output.
A return value of `true` indicates the character should be counted and a
return value of `false` indicates the character should not be counted.
Here is the code for the `countCharacters()` function.


    function countCharacters(string, predicate) {
        var i, count = 0;
        for (i = 0; i < string.length; i += 1) {
            if (predicate(string.charCodeAt(i))) {
                count += 1;
            }
        }
        return count;
    }

Run the tests.  The first two tests still pass, so we don't have any
major syntax errors.
Now we rewrite the `countUpperCaseLetters()` function to make use of the
new `countCharacters()` helper function.

    stringInfo.countUpperCaseLetters = function(string) {
        function predicate(code) {
            return code >= 65 && code <= 90;
        }
        return countCharacters(string, predicate);
    };

The new `countUpperCaseLetters()` function simply defines an appropriate
predicate function and then calls the `countCharacters()` function
passing the string and predicate function as parameters.

Run the tests.  The first two tests still pass.
So we haven't broken anything during the refactoring.
No we can refactor the second function using the same process.

    stringInfo.countLowerCaseLetters = function(string) {
        function predicate(code) {
            return code >= 97 && code <= 122;
        }
        return countCharacters(string, predicate);
    };

Run the tests one more time.  The first two tests still pass.
We have successfully refactored our code;
we eliminated duplication, while preserving behavior.

[code04.js](example1/code04.js)



Count Control Characters
------------------------

Now that we have refactored the code, we can move on to the 3rd test,
"Count control characters".
Looking again at the [ASCII][] tables, we see that the ASCII control
characters are found in the first 32 ASCII characters
(code values 0 through 31 inclusive) and the last ASCII character
(code value 127). 

We can leverage the `countCharacters()` helper function we produced from
the previous refactoring to help us write the `countControlCharacters()`
function.

    stringInfo.countControlCharacters = function(string) {
        function predicate(code) {
            return code <= 31 || code === 127;
        }
        return countCharacters(string, predicate);
    };

Instead of using the "and" boolean operator (`&&`) in the predicate,
we instead use the "or" boolean operator (`||`).

Run the tests.  We now see the first three tests passing.

There is no need to refactor, so we move on.

[code05.js](example1/code05.js)



Count Non-ASCII Characters
--------------------------

We only have one failing test left to deal with---the
"Count Non-ASCII characters" test.
Any character with a code value above 127 is not an ASCII character.
We can write the code for the `countNonASCIICharacters()` function in
the same manner we wrote the code for the other three functions.

    stringInfo.countNonASCIICharacters = function(string) {
        function predicate(code) {
            return code >= 128;
        }
        return countCharacters(string, predicate);
    };

Run the tests.  Now all tests pass.

There is no need to refactor, so we have completed the example.

[final code.js](example1/code.js)

You have completed Example 1 and are now ready to take on
[Assignment 1](assignment1.html).
