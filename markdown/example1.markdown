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

Now all four tests fail with the message that the function under test is missing.  Let's start with the first one:  `Object doesn't support property or method 'countUpperCaseLetters'`.

[code01.js](example1/code01.js)


Count Upper-case Characters
---------------------------

We will start by creating an empty function with the appropriate name attached to the stringStat object.

    var stringStat = {};


    stringStat.countUpperCaseLetters = function() {
    };


    window.stringStat = stringStat;

Now the "Count upper-case characters" test assertions each fail with an `undefined` result.  Let's fill in the function to take in a string parameter and count the number of upper-case letters found in the string.

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

Run the tests again.  Now the first test passes.

[code02.js](example1/code02.js)


Count Lower-case Characters
---------------------------


Count Control Characters
------------------------


Count Non-ASCII Characters
--------------------------


Refactor Code
-------------
