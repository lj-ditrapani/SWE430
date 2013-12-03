Example 2
========================================================================

- [Example 2 zip Environment](example2.zip)
- [Example 2 jsbin Environment][jsbin example 2]

[jsbin example 2]: http://jsbin.com/swe430_example2/latest/edit?javascript,live


Initial
-------

Initial skeleton, module function wrapper

[test01.js](example2/test01.js)
[code01.js](example2/code01.js)


I -> 1 Test
-----------

'roman' is undefined

export roman name-space

Object doesn't support property or method 'toDecimal'

create empty toDecimal method

Failed
- expected: 1
- result: undefined

Return 1

Passes

[test02.js](example2/test02.js)
[code02.js](example2/code02.js)


V -> 5 Test
-----------

Failed
- expected: 5
- result: 1

Use if-else

pass

[test03.js](example2/test03.js)
[code03.js](example2/code03.js)


X -> 10 Test
------------

Failed
- expected: 10
- result: 5

Use if-else

pass

[test04.js](example2/test04.js)
[code04.js](example2/code04.js)


Refactor to use dictionary
--------------------------


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


[test05.js](example2/test05.js)


Finish Individual Roman Numerals test
-------------------------------------

Failed
Result is undefined for L, C, D, and M

Add L, C, D, M entries by copying the X entry.

Failed
Result is 10 for L, C, D, and M

Fix dictionary values

Pass

[test06.js](example2/test06.js)
[code06.js](example2/code06.js)


Roman Numeral String Test
-------------------------------------

All assertions fail with undefined.  Expected single letter numbers.  We must rewrite the code to handle strings of multiple roman numerals.

Rewrite code to loop through characters and sum values.

Pass

[test07.js](example2/test07.js)
[code07.js](example2/code07.js)


Subtractive Rules Test
----------------------

Add a test to ensure subtractive rules are being applied.

Fails because we have not implemented subtractive rules yet.

[test08.js](example2/test08.js)


Rewrite function
----------------

Our code works fine if we allow numerals to be repeated 4 times and ignore the Subtractive rules.  Instead of changing our code, let's create a rewrite function that rewrites normal roman numerals by removing subtractive pairs and replacing them by the 4 symbol equivalent.

We start by writing the test.

fail

Now we write the code.

Object doesn't support property or method 'rewrite'

Add rewrite function to roman module

All assertions fail; result is undefined

Create helper function `replaceTwoCharacters`


Replace Two Characters function
-------------------------------

Write test for `replaceTwoCharacters`

fail
Object expected

Create empty `replaceTwoCharacters` function

fail
result undefined

Define body of replace two characters function `replaceTwoCharacters`
If `twoCharacters` is found in string, replace it with `replacement`.

pass

[test09.js](example2/test09.js)
[code09.js](example2/code09.js)


Back to the Rewrite Function
----------------------------

Now we write the code for the `rewrite` function using the `replaceTwoCharacters` helper function.

Call `replaceTwoCharacters` six times in rewrite function

pass

Refactor into loop

pass

Refactor the test.  Use existing runTest with second `runRewriteTest` boolean parameter.

pass

[test10.js](example2/test10.js)
[code10.js](example2/code10.js)


Integrate the Rewrite function into the toDecimal function
----------------------------------------------------------

Integrate the `rewrite` function into the `toDecimal` function to pass the "Subtractive Rules" test.

Pass

[code11.js](example2/code11.js)
