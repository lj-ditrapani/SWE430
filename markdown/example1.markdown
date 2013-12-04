SWE 430 Example 1 --- Running Tests
========================================================================

Create a stringStat module with string inspection functions.

- [Example 1 zip Environment](example1.zip)
- [Example 1 jsbin Environment][jsbin example 1]

[jsbin example 1]: http://jsbin.com/swe430_example1/latest/edit?javascript,live



Initial Boilerplate
-------------------

First, we write the boilerplate code for the code.js file.

    (function() {
        'use strict';


    }());

All four tests fail with the same error: `'stringStat' is undefined`.
So we will follow the advice of the test failure messages and create a stringStat object.

    (function() {
        'use strict';


        var stringStat = {};


        window.stringStat = stringStat;


    }());

Now all four tests fail with the message that the function under test is missing.  Let's start with the first one:  "`Object doesn't support property or method 'countUpperCaseLetters'`".

[code01.js](example1/code01.js)



Count Upper-case Characters
---------------------------

We will start by creating an empty function with the appropriate name attached to the stringStat object.

    var stringStat = {};


    stringStat.countUpperCaseLetters = function() {
    };


    window.stringStat = stringStat;

Now the "Count upper-case characters" test assertions each fail with an `undefined` result.  Let's fill in the function to take in a string parameter and count the number of upper-case letters found in the string.  The function should initialize a count variable to 0, loop through each character in the string and add one to the count if the character is an upper-case letter.  Looking at the table on the
[ASCII](http://en.wikipedia.org/wiki/ASCII)
Wikipedia page, we can see that upper-case characters have code values between 64 and 90 inclusive, so these will be the values we will use to compare the character code value against.

    stringStat.countUpperCaseLetters = function(string) {
        var i, code, count = 0;
        for (i = 0; i < string.length; i += 1) {
            code = string.charCodeAt(i);
            if (code >= 65 && code <= 90) {
                count += 1;
            }
        }
        return count;
    };

In order to find the value of a character, we sue the `charCodeAt` method of the String class.  It returns the numerical value of the character at the given position of the string object.

Run the tests again.  Now the first test passes.

[code02.js](example1/code02.js)



Count Lower-case Characters
---------------------------

The next failing test is fails with "`Object doesn't support property or method 'countLowerCaseLetters'`" because the `countLowerCaseLetters` function doesn't exist yet.  Let's declare the `countUpperCaseLetters` function now.

    stringStat.countLowerCaseLetters = function() {
    };

The assertions for the "Count lower-case characters" test now all fail with a result of `undefined`.  Now we can implement the body of the `countLowerCaseLetters` function.  First, we add the string parameter to the function.  The body of the function should be very similar to the `countUpperCaseLetters` function.  So let's copy the code we wrote for `countUpperCaseLetters` and modify it to make it count lower-case letters instead.

    stringStat.countLowerCaseLetters = function(string) {
        var i, code, count = 0;
        for (i = 0; i < string.length; i += 1) {
            code = string.charCodeAt(i);
            if (code >= 97 && code <= 122) {
                count += 1;
            }
        }
        return count;
    };

All we had to do to make the code work is is change the two numbers in the `if` statement.  According to the 
[ASCII](http://en.wikipedia.org/wiki/ASCII)
table, lower-case characters have code values between 97 and 122 inclusive.  So we just change the 65 to 97 and the 90 to 122 and we are done.

Run the tests again.  Now the first and second tests pass.

[code03.js](example1/code03.js)



Refactor Code
-------------

Before we move on to the next test, we should refactor our code.  You probably know that copying and pasting code is generally a sign of poor design.  The code for our `countLowerCaseLetters` and `countUpperCaseLetters` functions are nearly identical.  We should factor-out the duplicate code into a common helper function both functions can share.

As you have seen, the only difference between the two functions is the criteria used to determine if the current character is one we want to count or not.  So let's call our helper function `countCharacters`.  It will take two parameters, a string and a predicate function.

The predicate function takes a character code value as input and returns a boolean (true or false) value as output.  A return value of true indicates the character should be counted and a return value of false indicates the character should not be counted.


    function countCharacters(string, predicate) {
        var i, count = 0;
        for (i = 0; i < string.length; i += 1) {
            if (predicate(string.charCodeAt(i))) {
                count += 1;
            }
        }
        return count;
    }

Run the tests.  The first two tests still pass, so we don't have any major syntax errors.  Now we rewrite the `countUpperCaseLetters` function to make use of the new `countCharacters` helper function.

    stringStat.countUpperCaseLetters = function(string) {
        function predicate(code) {
            return code >= 65 && code <= 90;
        }
        return countCharacters(string, predicate);
    };

The new `countUpperCaseLetters` function simply defines an appropriate predicate function and then calls the `countCharacters` function passing the string and predicate function as parameters.

Run the tests.  The first two tests still pass.  So we haven't broken anything during the refactoring.  No we can refactor the second function using the same process.

    stringStat.countLowerCaseLetters = function(string) {
        function predicate(code) {
            return code >= 97 && code <= 122;
        }
        return countCharacters(string, predicate);
    };

Run the tests one more time.  The first two tests still pass.  We have successfully refactored our code; we eliminated duplication, while preserving behavior.

[code04.js](example1/code04.js)



Count Control Characters
------------------------



Count Non-ASCII Characters
--------------------------


