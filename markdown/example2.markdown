Example 2
========================================================================

- [Example 2 zip Environment](example2.zip)
- [Example 2 jsbin Environment][jsbin example 2]

[jsbin example 2]: http://jsbin.com/swe430_example2/latest/edit?javascript,live


Initial
-------

Initial skeleton, module function wrapper

[code01.js](example2/code01.js)
[test01.js](example2/test01.js)


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

[code02.js](example2/code02.js)
[test02.js](example2/test02.js)


V -> 5 Test
-----------

Failed
- expected: 5
- result: 1

Use if-else

pass

[code03.js](example2/code03.js)
[test03.js](example2/test03.js)


X -> 10 Test
------------

Failed
- expected: 10
- result: 5

Use if-else

pass

[code04.js](example2/code04.js)
[test04.js](example2/test04.js)


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
[test05.js](example2/test05.js)
