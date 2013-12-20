SWE 430:  Example 2
========================================================================

For Example 2, we will use the Test-driven Development (TDD) process to
iteratively develop a function that can translate roman numerals into
decimal values.  We will write both the test code and the production
code step-by-step.

The TDD cycle:

- Write a test
- Run all your tests, ensuring the new test fails
- Write the code to pass the test
- Run all your tests, ensuring the new test passes
- Refactor your production code if necessary
- Run all your tests
- Refactor your test code if necessary
- Run all your tests
- Repeat

We will create a module named `roman` which has a function `toDecimal()`
that converts roman numerals to decimal values.

If you are not familiar with roman numerals, take a look at the
[Wikipedia page](http://en.wikipedia.org/wiki/Roman_numerals).

The `toDecimal()` function must be able to handle roman numerals with
values from 1 to 3999.  In roman numerals, this means
`I` to `MMMCMXCIX`.
The roman numerals are assumed to be valid numbers;
therefore the `toDecimal()` function is not responsible for performing
any validation.

At the end of each section, a link to the current state of the `code.js`
and `test.js` files, which incorporates all of the work accomplished in
the example up to that point, is provided for you to check your work
against so you can follow along with confidence.

Example 2 Environments (use one or the other):

- [Example 2 zip Environment](example2.zip)
- [Example 2 jsbin Environment][jsbin]

For a refresher on using the above environments, see the 
[Environment Instructions](instructions.html).

[jsbin]: http://jsbin.com/swe430_example2/latest/edit?javascript,live


Initial Code
------------

Both the code.js and test.js files are empty.  If we try running the tests, we see this response from qUnit.

    Tests completed in 18 milliseconds.
    0 assertions of 0 passed, 0 failed.

Since there are no tests to run, there is nothing to report.

As we did in Example 1, we start by writing the boilerplate code for the
`test.js` file.
We will place all our test code inside of an anonymous function so all
our code is encapsulated and hidden.
Any local variables we define with the `var` keyword and
any functions we define with the `function` keyword
will only be visible within the anonymous function.
This way, we do not pollute the global namespace.
To accomplish this, we simply define an anonymous function and
immediately execute it with the trailing `()`.

    // test.js
    (function() {
        'use strict';


    }());

We do the same thing with the `code.js` file.

    // code.js
    (function() {
        'use strict';


    }());

Run the tests again.  Since we haven't defined anything yet other than
the enclosing anonymous functions, we get the same result as before.

[test01.js](example2/test01.js)
[code01.js](example2/code01.js)


`I -> 1` Test
-------------

Let's write our first test.  We will start with the most basic test:
convert `I` to 1.  To write a test, we invoke the qUnit `test` function.
The `test()` function takes a function object as it's second argument.
The `test()` function is how we tell qUnit to add the function object to
the test suite.  The test should assert that the return value of the
`toDecimal()` function, when given an argument of `'I'`, is 1.
We use the qUnit `equal()` function to make this assertion.

    // test.js
    test('I -> 1', function() {
        equal(roman.toDecimal('I'), 1);
    });

Run the tests.  The test fails with a result of:
"`'roman' is undefined`".  This makes sense, because we have not defined
the variable `roman` yet.
Let's do that now, as the test results suggest.

The `roman` variable should reference an object that we will use as our
module namespace.

    // code.js
    window.roman = {};

Let's run our tests again.  Now the test fails with a different message:
"`Object doesn't support property or method 'toDecimal'`".  This is a
logical response as we have not defined a `toDecimal` property on the
`roman` object yet.
Therefor, we create an empty `toDecimal()` function and
attach it as a property of the `roman` object.

    // code.js
    function toDecimal() {
    }


    window.roman = {
        toDecimal: toDecimal
    };

Run the tests.  The test fails again.  This time the message is:

- expected: 1
- result: undefined

What is the simplest solution to make this test pass?
It is to modify the `toDecimal()` function to return 1.  Let's do that.

    // code.js
    function toDecimal() {
        return 1;
    }


    window.roman = {
        toDecimal: toDecimal
    };

Run the tests.  The test now passes.  There is no need to refactor,
so we will move on to the next test.

[test02.js](example2/test02.js)
[code02.js](example2/code02.js)


V -> 5 Test
-----------

    // test.js
    test('V -> 5', function() {
        equal(roman.toDecimal('V'), 5);
    });

Failed

- expected: 5
- result: 1

Use if-else

    // code.js
    function toDecimal(romanNumerals) {
        if (romanNumerals === 'I') {
            return 1;
        } else {
            return 5;
        }
    }

pass

[test03.js](example2/test03.js)
[code03.js](example2/code03.js)


X -> 10 Test
------------

    // test.js
    test('X -> 10', function() {
        equal(roman.toDecimal('X'), 10);
    });

Failed
- expected: 10
- result: 5

Use if-else

    // code.js
    function toDecimal(romanNumerals) {
        if (romanNumerals === 'I') {
            return 1;
        } else if (romanNumerals === 'V') {
            return 5;
        } else {
            return 10;
        }
    }

pass

[test04.js](example2/test04.js)
[code04.js](example2/code04.js)


Refactor to use dictionary
--------------------------

    // code.js
    var DICTIONARY = {
        I: 1,
        V: 5,
        X: 10
    };


    function toDecimal(romanNumerals) {
        return DICTIONARY[romanNumerals];
    }

[code05.js](example2/code05.js)


Refactor test code
------------------

    // test.js
    function runTests(tests) {
        var i, pair, label;
        for (i = 0; i < tests.length; i += 1) {
            pair = tests[i];
            label = pair[0] + ' -> ' + pair[1];
            equal(roman.toDecimal(pair[0]), pair[1], label);
        }
    }


    test('Individual Roman Numerals', function() {
        var tests = [
            ['I', 1],
            ['V', 5],
            ['X', 10]
        ];
        runTests(tests);
    });

[test05.js](example2/test05.js)


Finish Individual Roman Numerals test
-------------------------------------

    // test.js
    test('Individual Roman Numerals', function() {
        var tests = [
            ['I', 1],
            ['V', 5],
            ['X', 10],
            ['L', 50],
            ['C', 100],
            ['D', 500],
            ['M', 1000]
        ];
        runTests(tests);
    });

Failed
Result is undefined for L, C, D, and M

Add L, C, D, M entries by copying the X entry.

    // code.js
    var DICTIONARY = {
        I: 1,
        V: 5,
        X: 10,
        L: 10,
        C: 10,
        D: 10,
        M: 10
    };

Failed
Result is 10 for L, C, D, and M

Fix dictionary values

    // code.js
    var DICTIONARY = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };

Pass

[test06.js](example2/test06.js)
[code06.js](example2/code06.js)


Roman Numeral String Test
-------------------------------------

    // test.js
    test('Roman Numeral Stings', function() {
        var tests = [
            ['II', 2],
            ['III', 3],
            ['VI', 6],
            ['VIII', 8],
            ['XII', 12],
            ['XVII', 17],
            ['CLXVI', 166],
            ['MMDCCCLXXXVIII', 2888],
            ['MMMDCCLXXVII', 3777]
        ];
        runTests(tests);
    });

All assertions fail with undefined.  Expected single letter numbers.  We must rewrite the code to handle strings of multiple roman numerals.

Rewrite code to loop through characters and sum values.

    // code.js
    function toDecimal(romanNumerals) {
        var i, number = 0;
        for (i = 0; i < romanNumerals.length; i += 1) {
            number += DICTIONARY[romanNumerals[i]];
        }
        return number;
    }

Pass

[test07.js](example2/test07.js)
[code07.js](example2/code07.js)


Subtractive Rules Test
----------------------

Add a test to ensure subtractive rules are being applied.

    // test.js
    test('Subtractive Rules', function() {
        var tests = [
            ['IV', 4],
            ['IX', 9],
            ['XL', 40],
            ['XC', 90],
            ['CD', 400],
            ['CM', 900],
            ['CDLIX', 459],
            ['MCMXIX', 1919],
            ['MCMXX', 1920],
            ['MCMXXI', 1921],
            ['MMMCDXLIV', 3444],
            ['MMMCDXCIV', 3494],
            ['MMMDCCCXCVII', 3897],
            ['MMMCMXLIX', 3949],
            ['MMMCMXCIX', 3999]
        ];
        runTests(tests);
    });

Fails because we have not implemented subtractive rules yet.

[test08.js](example2/test08.js)


Rewrite function
----------------

Our code works fine if we allow numerals to be repeated 4 times and ignore the Subtractive rules.  Instead of changing our code, let's create a rewrite function that rewrites normal roman numerals by removing subtractive pairs and replacing them by the 4 symbol equivalent.

We start by writing the test.

    // test.js
    test('Rewrite function', function() {
        equal(roman.rewrite('IV'), 'IIII');
        equal(roman.rewrite('IX'), 'VIIII');
        equal(roman.rewrite('XL'), 'XXXX');
        equal(roman.rewrite('XC'), 'LXXXX');
        equal(roman.rewrite('CD'), 'CCCC');
        equal(roman.rewrite('CM'), 'DCCCC');
        equal(roman.rewrite('CDLIX'), 'CCCCLVIIII');
        equal(roman.rewrite('MCMXIX'), 'MDCCCCXVIIII');
        equal(roman.rewrite('MCMXX'), 'MDCCCCXX');
        equal(roman.rewrite('MCMXXI'), 'MDCCCCXXI');
        equal(roman.rewrite('MMMCDXLIV'), 'MMMCCCCXXXXIIII');
        equal(roman.rewrite('MMMCDXCIV'), 'MMMCCCCLXXXXIIII');
        equal(roman.rewrite('MMMDCCCXCVII'), 'MMMDCCCLXXXXVII');
        equal(roman.rewrite('MMMCMXLIX'), 'MMMDCCCCXXXXVIIII');
        equal(roman.rewrite('MMMCMXCIX'), 'MMMDCCCCLXXXXVIIII');
    });

The new test fails because `roman.rewrite` is undefined:
Object doesn't support property or method 'rewrite'

Now we write the production code.

Add rewrite function to roman module

    // code.js
    function rewrite(romanNumerals) {
    }


    window.roman = {
        rewrite: rewrite,
        toDecimal: toDecimal
    };

The rewrite test now runs, but all assertions fail with `result is undefined`.

Create helper function `replaceTwoCharacters`


Replace Two Characters function
-------------------------------

Write test for `replaceTwoCharacters`

    // test.js
    test('Replace Two Characters', function() {
        var f = roman.replaceTwoCharacters;
        equal(f('a', 'fg', 'WX'), 'a');
        equal(f('abcde', 'fg', 'WX'), 'abcde');
        equal(f('abcde', 'ab', 'WX'), 'WXcde');
        equal(f('abcde', 'cd', 'WXY'), 'abWXYe');
        equal(f('abcde', 'de', 'WXYZ'), 'abcWXYZ');
    });

fail
Object expected

Create empty `replaceTwoCharacters` function

    // code.js
    function replaceTwoCharacters(string, twoCharacters, replacement) {
    }


    window.roman = {
        replaceTwoCharacters: replaceTwoCharacters,
        rewrite: rewrite,
        toDecimal: toDecimal
    };


fail
result undefined

Define body of replace two characters function `replaceTwoCharacters`
If `twoCharacters` is found in string, replace it with `replacement`.

    // code.js
    function replaceTwoCharacters(string, twoCharacters, replacement) {
        var index = string.indexOf(twoCharacters);
        if (index === -1) {
            return string;
        }
        return string.slice(0, index) + replacement +
               string.slice(index + 2, string.length);
    }

Run the tests.  The 'Replace Two Characters' test now passes.

[test09.js](example2/test09.js)
[code09.js](example2/code09.js)


Back to the Rewrite Function
----------------------------

Now we write the code for the `rewrite` function using the `replaceTwoCharacters` helper function.

Call `replaceTwoCharacters` six times in rewrite function

    // code.js
    function rewrite(romanNumerals) {
        romanNumerals = replaceTwoCharacters(romanNumerals,
                                             'IV', 'IIII');
        romanNumerals = replaceTwoCharacters(romanNumerals,
                                             'IX', 'VIIII');
        romanNumerals = replaceTwoCharacters(romanNumerals,
                                             'XL', 'XXXX');
        romanNumerals = replaceTwoCharacters(romanNumerals,
                                             'XC', 'LXXXX');
        romanNumerals = replaceTwoCharacters(romanNumerals,
                                             'CD', 'CCCC');
        romanNumerals = replaceTwoCharacters(romanNumerals,
                                             'CM', 'DCCCC');
        return romanNumerals;
    }

pass

Refactor into loop

    // code.js
    function rewrite(romanNumerals) {
        var i, subtractivePairs, replacements;
        subtractivePairs = [
            'IV', 'IX', 'XL', 'XC', 'CD', 'CM'
        ];
        replacements = [
            'IIII', 'VIIII', 'XXXX', 'LXXXX', 'CCCC', 'DCCCC'
        ];
        for (i = 0; i < subtractivePairs.length; i += 1) {
            romanNumerals = replaceTwoCharacters(romanNumerals,
                                                 subtractivePairs[i],
                                                 replacements[i]);
        }
        return romanNumerals;
    }

pass

Refactor the test.  Use existing runTest with second `runRewriteTest` boolean parameter.

    // test.js
    function runTests(tests, runRewriteTest) {
        var i, pair, label, functionName = 'toDecimal';
        if (runRewriteTest) {
            functionName = 'rewrite';
        }
        for (i = 0; i < tests.length; i += 1) {
            pair = tests[i];
            label = pair[0] + ' -> ' + pair[1];
            equal(roman[functionName](pair[0]), pair[1], label);
        }
    }

    test('Rewrite function', function() {
        var tests = [
            ['IV', 'IIII'],
            ['IX', 'VIIII'],
            ['XL', 'XXXX'],
            ['XC', 'LXXXX'],
            ['CD', 'CCCC'],
            ['CM', 'DCCCC'],
            ['CDLIX', 'CCCCLVIIII'],
            ['MCMXIX', 'MDCCCCXVIIII'],
            ['MCMXX', 'MDCCCCXX'],
            ['MCMXXI', 'MDCCCCXXI'],
            ['MMMCDXLIV', 'MMMCCCCXXXXIIII'],
            ['MMMCDXCIV', 'MMMCCCCLXXXXIIII'],
            ['MMMDCCCXCVII', 'MMMDCCCLXXXXVII'],
            ['MMMCMXLIX', 'MMMDCCCCXXXXVIIII'],
            ['MMMCMXCIX', 'MMMDCCCCLXXXXVIIII']
        ];
        runTests(tests, true);
    });

pass

[final test.js](example2/test.js)
[code10.js](example2/code10.js)


Integrate the Rewrite function into the toDecimal function
----------------------------------------------------------

Integrate the `rewrite` function into the `toDecimal` function to pass the "Subtractive Rules" test.

    // code.js
    function toDecimal(romanNumerals) {
        var i, number = 0;
        romanNumerals = rewrite(romanNumerals);
        for (i = 0; i < romanNumerals.length; i += 1) {
            number += DICTIONARY[romanNumerals[i]];
        }
        return number;
    }

Pass

[final code.js](example2/code.js)
