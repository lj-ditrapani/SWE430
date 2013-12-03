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


Finish Individual Roman Numerals test
-------------------------------------
