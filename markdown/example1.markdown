SWE 430 Example 1 --- Running Tests
========================================================================

String inspection functions

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


Count Upper-case Characters
---------------------------


Count Lower-case Characters
---------------------------


Count Control Characters
------------------------


Count Non-ASCII Characters
--------------------------


Refactor Code
-------------
