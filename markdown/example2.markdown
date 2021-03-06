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

Both the code.js and test.js files are empty.
If we try running the tests, we see this response from qUnit.

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

- Expected: 1
- Result: undefined

What is the simplest solution to make this test pass?
It is to modify the `toDecimal()` function to return 1.  Let's do that.

    // code.js
    function toDecimal() {
        return 1;
    }


    window.roman = {
        toDecimal: toDecimal
    };

Run the tests.  The test now passes.
There is no need to refactor, so we will move on to the next test.

[test02.js](example2/test02.js)
[code02.js](example2/code02.js)


`V -> 5` Test
-------------

What is the next most basic test we could write?
Let's create a test for when the input is `"V"`.
This should produce an output of 5.
We can copy the previous test for `I -> 1`
and replace `I` with `V` and 1 with 5.

    // test.js
    test('V -> 5', function() {
        equal(roman.toDecimal('V'), 5);
    });

Run the tests.  Th second test fails with the following message:

- Expected: 5
- Result: 1

We previously hard-coded the `toDecimal()` function to always return 1
regardless of the input parameter.
We want the return value to be determined by the input parameter.
First, we must define an actual input parameter---we
will call it `romanNumerals`.
Then we will use an if-else statement to return either 1 or 5 based on
the value of the input parameter `romanNumerals`.

    // code.js
    function toDecimal(romanNumerals) {
        if (romanNumerals === 'I') {
            return 1;
        } else {
            return 5;
        }
    }

Run the tests again.  Now they both pass.
There is no need to refactor, so we will move on to the next test.

[test03.js](example2/test03.js)
[code03.js](example2/code03.js)


`X -> 10` Test
--------------

Now we write a test to handle `"X"` in the same manner we have don for
`"I"` and `"V"`.

    // test.js
    test('X -> 10', function() {
        equal(roman.toDecimal('X'), 10);
    });

Run the tests.  The third test fails with the following message:

- Expected: 10
- Result: 5

Our `toDecimal()` function returns 5 for any input other than `"I"`.
Let's add another else clause to our code.
We want the second clause to capture the case when the input is `"V"`
and as a result, return 5.
The third and final else clause should return 10.

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

Run the tests.  All tests pass.  However, there is a disturbing pattern
in our production code that requires some refactoring.

[test04.js](example2/test04.js)
[code04.js](example2/code04.js)


Refactor Production Code
------------------------

Looking ahead, we know we will want our code to work for `L`, `C`, `D`,
and `M` as well as `I`, `V`, and `X`.
We already see a pattern emerging in the `toDecimal()` function from the
if-else statement.
It checks the value of the `romanNumerals` input parameter against the
possible roman numerals and returns the corresponding decimal value.
Each additional roman numeral will require duplicating another else
clause to perform the same actions on different values.
The code is acting like a mapping from roman numerals to decimal values.
We should use a datastructure to express this mapping implicitly
instead of using redundant if-else clauses.
It turns out, JavaScript objects are already key-value mappings.
So let's rewrite the code to use a JavaScript object so that the
`toDecimal()` function only needs to look up the correct decimal value
by accessing the correct property.
We'll call the JavaScript object `DICTIONARY` to indicate its true
purpose and write it in upper-case to indicate it is immutable (the
value of `DICTIONARY` does not change during execution of the program).

    // code.js
    var DICTIONARY = {
        I: 1,
        V: 5,
        X: 10
    };


    function toDecimal(romanNumerals) {
        return DICTIONARY[romanNumerals];
    }

The `romanNumerals` input parameter is actually the look-up key of the
`DICTIONARY` object.  Notice how simple our `toDecimal()` function has
become.  It is only a single line with no need for control-flow logic.

Run the tests.  They all pass.  This means our production code
refactoring has been successful because we improved the _structure_ of
our code without changing the _behavior_ of our code.

[code05.js](example2/code05.js)


Refactor Test Code
------------------

We have removed duplication from the production code via refactoring,
but we still have duplication in our test code to deal with.
Our three tests are nearly identical.  They differ only in the input
roman numeral and expected output decimal value.
Instead of writing a new test for each roman numeral, it would be nice
to have a single test with a list of test cases that executes the code
for each test case automatically.
Testing an additional roman numeral would only require adding a test
case input/output pair to the list of test cases instead of copying an
entire test and changing the values.

Let's start by creating a generic `runTests()` function that takes an
array of test cases an input.  Each test case should be a sub-array that
consists of two values, the input roman numeral and the expected output
decimal value.  The `runTests()` function should pass the input to the
`toDecimal()` function and compare the actual result with the expected
result.

    // test.js
    function runTests(tests) {
        var i, pair, label;
        for (i = 0; i < tests.length; i += 1) {
            pair = tests[i];
            label = pair[0] + ' -> ' + pair[1];
            equal(roman.toDecimal(pair[0]), pair[1], label);
        }
    }

The `runTests()` function iterates over the test cases in the `tests`
input parameter.  In each iteration, the current test case is assigned
to the `pair` variable.  The first item in `pair` is the roman numeral
and the second item in `pair` is the expected output.

Line 6 provides a label for each assertion explaining the purpose of
the test case.

Run the tests.  All tests still pass, so we don't have any syntax
problems with our new code.

Now let's rewrite our three original tests into a single test that
makes use of the new `runTests()` function.  The new test should define
a array of test cases named `tests` and then invoke the `runTests`
function passing the `tests` variable as the input.


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

The `tests` array contains three test cases that represent the three
original tests we had before the refactoring.  So this single test does
all the work accomplished by the original three tests, but without the
duplication in test code.  In addition, our `runTests()` helper function
will come in handy when writing future tests.

Run the tests.  All tests still pass.
This means our test code refactoring has been successful because we
improved the _structure_ of our code without changing the _behavior_ of
our code.

[code05.js](example2/code05.js)
[test05.js](example2/test05.js)


Finish "Individual Roman Numerals" test
---------------------------------------

It's time to complete our "Individual Roman Numerals" test.
It is missing test cases for `"L"`, `"C"`, `"D"`, and `"M"`.
Now that our test code is nicely refactored, we can easily add the
required test cases.  All we have to do is insert 4 items into the
`tests` array.

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

Run the tests.  The test now fails.  Of the seven assertions,
the assertions for
`L`, `C`, `D`, and `M`
fail with
"`Result: undefined`".
The failure is due to not having
`L`, `C`, `D`, or `M`
properties defined in the `DICTIONARY` object of the production code.

Therefore, we should add `L`, `C`, `D`, and `M` properties to the
`DICTIONARY` object.  We will do so by copying the `X` property four
times and changing the property name each time.

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

Let's run the tests again.  This time the test fails because the result
for
`L`, `C`, `D`, and `M`
is 10 instead of the expected value.
Let's change the values of the properties to the correct numbers.

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

Run the tests again.  This time the test passes.
There is no need to refactor, so we will move on to the next test.

[test06.js](example2/test06.js)
[code06.js](example2/code06.js)


Roman Numeral String Test
-------------------------

Up to this point, our tests have only considered single-character
roman numerals.  It is time to create a test that deals with
multi-character roman numeral strings.

We create a new test, "Roman Numeral String".  It is very similar to
the "Individual Roman Numerals" test.  It has an array of test cases
named `tests` and calls the `runTests()` function passing `tests` as the
input parameter.  However, it differs in that the input value for each
test case is a string of roman numerals instead of a single-character.

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

Run the tests.  All assertions in the new test fail with
"`Result: undefined`".
The production code was written to expected a single letter roman
numeral.  We must rewrite the code to handle strings of multiple roman
numerals.

The easiest way I see to fix this is to create a loop that iterates
over each character and sums the decimal values of each character.
To accomplish this, we need a `number` local variable that keeps track
of the running sum.  The `number` variable must be initialized to 0.
We can use the `DICTIONARY` to lookup the value of each character as we
did previously.

    // code.js
    function toDecimal(romanNumerals) {
        var i, number = 0;
        for (i = 0; i < romanNumerals.length; i += 1) {
            number += DICTIONARY[romanNumerals.charAt(i)];
        }
        return number;
    }

Run the tests.  Both tests now pass.
Notice that our production code now works for both single-character
and multi-character roman numeral strings.
There is no need to refactor, so we will move on to the next test.

[test07.js](example2/test07.js)
[code07.js](example2/code07.js)


Subtractive Rules Test
----------------------

Roman numerals use subtractive rules to avoid repeating the same numeral
more than 3 times.  For example 4 is not `IIII`, but `IV` and 9 is not
`VIIII`, but `IX`.

According to
[Wikipedia](http://en.wikipedia.org/wiki/Roman_numerals):

> Symbols are placed from left to right in order of value, starting with
> the largest. However, in a few specific cases, to avoid four
> characters being repeated in succession (such as `IIII` or `XXXX`)
> these can be reduced using subtractive notation as follows:
> 
> - the numeral `I` can be placed before `V` and `X` to make 4 units
>   (`IV`) and 9 units (`IX`) respectively
> - `X` can be placed before `L` and `C` to make 40 (`XL`) and 90 (`XC`)
>   respectively
> - `C` can be placed before D and M to make 400 (`CD`) and 900 (`CM`)
>   according to the same pattern


We should add a test to ensure the subtractive rules are being applied
correctly.  The test is very similar to the previous 2 tests.
It defines an array of test cases and then invokes the `runTests()`
function passing the `tests` array as the input argument.

We define test cases that cover the 6 possible subtractive rules in
various combinations throughout the range of allowed values (1 to 3999).

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

Run the tests.  The new fails.  Every assertion in the test has a
result value that is greater than the expected value.
This is because we have not yet implemented the subtractive rules.
Let's work on implementing the subtractive rules in our production code
in order to pass this new test.

[test08.js](example2/test08.js)


"Rewrite" Function
------------------

Our code works fine if we allow numerals to be repeated 4 times and
ignore the Subtractive rules.  Instead of changing our existing code,
let's create a `rewrite()` function that rewrites normal roman
numerals by removing subtractive pairs and replacing them by the 4
symbol equivalent.

For example, `rewrite('IV')` will return `IIII` and
`rewrite('IX')` will return `VIIII`.

We start by writing the test for the `rewrite()` function.
We define several test-cases inside the test.  Each test case
corresponds to a test-case from the "Subtractive Rules" test.
For each test-case, we assert that the result of calling the `rewrite()`
function on the input is equal to the expected output.

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

We cannot leverage our `runTests()` helper function for this test
because the `runTests()` helper function calls the `roman.toDecimal()`
function and not the `roman.rewrite()` function.

The new test fails because `roman.rewrite()` is undefined.  The failure
message is:
"`Object doesn't support property or method 'rewrite'`"
So we have 2 failing tests, the "Subtractive Rules" test and the
"Rewrite function" test.

Now let's turn to the production code.  We will start by declaring the
`rewrite()` function.  We will give it an empty function body for now.
Line 7 attaches the `rewrite()` function to the `roman` module so it
will be accessible for testing outside the `code.js` file.

    // code.js
    function rewrite(romanNumerals) {
    }


    window.roman = {
        rewrite: rewrite,
        toDecimal: toDecimal
    };

The rewrite test now runs and executes all assertions,
but each assertions fail with `Result: undefined`.

Before we dive into filling-in the body of the `rewrite()` function with
code, it would be nice to break down this problem into smaller pieces.
Let's isolate a portion of the rewrite function into a smaller,
helper function.


"Replace Two Characters" Function
---------------------------------

In light of what the `rewrite()` function is required to do,
it would be nice to have a helper function that,
given a string, a two character string, and a replacement substring,
would return a string with the first occurrence of the two character
string replaced with the replacement substring.
Let's create a helper function named `replaceTwoCharacters()`
that does exactly that.

Before we write the production code for `replaceTwoCharacters()`, we
write a test for it.

    // test.js
    test('Replace Two Characters', function() {
        var f = roman.replaceTwoCharacters;
        equal(f('a', 'fg', 'WX'), 'a');
        equal(f('abcde', 'fg', 'WX'), 'abcde');
        equal(f('abcde', 'ab', 'WX'), 'WXcde');
        equal(f('abcde', 'cd', 'WXY'), 'abWXYe');
        equal(f('abcde', 'de', 'WXYZ'), 'abcWXYZ');
    });

Run the tests.  The new test fails with a message of:
`undefined: Object expected`.  This is expected since we haven't even
declared the `replaceTwoCharacters()` function in the production code
yet.

Let's create an empty `replaceTwoCharacters()` function in the production code now.  The function should have 3 parameters:

- `string`:  the input string
- `twoCharacters`:  the two characters that should be removed from the
  input string.
- `replacement`:  the replacement substring that should be added to the
  string at the position of the `twoCharacters`.

Line 7 attaches the `replaceTwoCharacters()` function to the `roman`
module so it is accessible for testing outside of the `code.js` file.


    // code.js
    function replaceTwoCharacters(string, twoCharacters, replacement) {
    }


    window.roman = {
        replaceTwoCharacters: replaceTwoCharacters,
        rewrite: rewrite,
        toDecimal: toDecimal
    };

Run the tests.  Now the test executes all the assertions, but each assertions fails because the result is `undefined`.

Now we can define the body of `replaceTwoCharacters()` function.
The function should check if `twoCharacters` is found in `string`.
If `twoCharacters` is found in string, it should replace it with
`replacement`.

    // code.js
    function replaceTwoCharacters(string, twoCharacters, replacement) {
        var index = string.indexOf(twoCharacters);
        if (index === -1) {
            return string;
        }
        return string.slice(0, index) + replacement +
               string.slice(index + 2, string.length);
    }

- Line 3 tries to find the index of the first occurrence of `twoCharacters` in `string`. 
- Lines 4 and 5: If `index` is -1, it means `twoCharacters` was not found in `string` and therefore `string` should be returned as-is with no changes.
- Lines 7 and 8 insert the `replacement` substring where `twoCharacters` used to be.  The first `slice()` returns the portion of `string` before `twoCharacters` and the second `slice()` returns the portion of `string` after `twoCharacters`.

Run the tests.  The "Replace Two Characters" test now passes.
However, we still have 2 failing tests.
Let's try to get the "Rewrite function" test to pass.

[test09.js](example2/test09.js)
[code09.js](example2/code09.js)


Back to the "Rewrite" Function
------------------------------

Now we write the code for the `rewrite()` function using the
`replaceTwoCharacters()` helper function.
Since we have already solved the problem of replacing two characters
with a substring by writing the `replaceTwoCharacters()` helper
function, the implementation of the `rewrite()` function is very simple
and straight forward.

Recall, there are six subtractive rules to apply.  All we need to do now
to implement the `rewrite()` function is call the
`replaceTwoCharacters()` function six times;
once for each subtractive rule.
Each time, we update the value of romanNumerals to the value returned
by `replaceTwoCharacters()`.

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

Run the tests.  The "Rewrite function" test now passes.  However, there
is a lot of duplication in the code we just wrote.  Now that we know it
works properly because of the passing test, let's refactor it to remove
the redundant code.

We rewrite the function to use a "`for`" loop that iterates over the
`subtractivePairs` and `replacements`.  At each iteration, the function
calls `replaceTwoCharacters()`, and replaces the value of
`romanNumerals` with the result.

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

- Lines 4-6 define the pairs of roman numerals that make use of the
  subtractive rules.
- Lines 7-9 define the roman numerals that should be used to replace the
  subtractive pairs.
- Lines 11-13 invoke the `replaceTwoCharacters()` function for the
  current iteration, updating the value of `romanNumerals` to the result
  of the function call.

Run the tests.  The "Rewrite function" still passes.  This means the
refactoring has been successful because we improved the _structure_ of
our code without changing the _behavior_ of our code.

We have refactored the production code, but what about the test code?
There is a lot of duplication in the "Rewrite function" test.  It would
be nice if we could leverage the `runTests()` function to run the test
as we have done in the other test functions.
This would allow us to remove
the duplication in the "Rewrite function" test.  Let's refactor the
`runTests()` function so it works for both `roman.rewrite()` and
`roman.toDecimal()`.  To do this, we add a second parameter to the
`runTests()` function named `runRewriteTest` with a boolean type.
Remember, booleans can only have a value of `true` or `false`.
If the input parameter `runRewriteTest` is `false`, `undefined`, or
missing, the `toDecimal()` function is executed.  If the
`runRewriteTest` input parameter is `true`, the `rewrite()` function is
executed.

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

Run the tests.  All tests (except the "Subtractive Rules" test) still
pass.  This means the `runTests()` function still works correctly for
all the previous tests.  Now we can modify the "Rewrite function" test
to make use of the `runTests()` helper function.  We write the
"Rewrite function" test in the same way we have written the other tests
that make use of the `runTests()` function.  We define an array of
test-cases named `tests` and pass them as input to the `runTests()`
function.  The only wrinkle is, this time, `runTests()` takes a second
input argument, a literal `true` to indicate the `runTests()` function
should call the `roman.rewrite()` function instead of the
`roman.toDecimal()` function.

    // test.js
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

Run the tests.  All tests (except the "Subtractive Rules" test) still pass.  Our refactoring was successful.  We can now move on to the final step in making our production code pass the "Subtractive Rules" test.

[final test.js](example2/test.js)
[code10.js](example2/code10.js)


Integrate the "rewrite" and "toDecimal" Functions
-------------------------------------------------

Now that we have a working `rewrite()` function, we simply need to
modify the `toDecimal()` function to make use of it and pass the
"Subtractive Rules" test.

The modification is simple.  We add a single line of code that calls
the `rewrite()` function and updates the value of `romanNumerals` with
the result.

    // code.js
    function toDecimal(romanNumerals) {
        var i, number = 0;
        romanNumerals = rewrite(romanNumerals);
        for (i = 0; i < romanNumerals.length; i += 1) {
            number += DICTIONARY[romanNumerals.charAt(i)];
        }
        return number;
    }

Run the tests.  Now all tests pass and we have completed the project.
Well done!

[final code.js](example2/code.js)


You are now ready to proceed to [Assignment 2](assignment2.html).
