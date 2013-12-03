/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Example 2 Test Code
 * Test the roman module
 */

/*global test,equal,roman*/
(function() {
    'use strict';


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


    test('Replace Two Characters', function() {
        var f = roman.replaceTwoCharacters;
        equal(f('a', 'fg', 'WX'), 'a');
        equal(f('abcde', 'fg', 'WX'), 'abcde');
        equal(f('abcde', 'ab', 'WX'), 'WXcde');
        equal(f('abcde', 'cd', 'WXY'), 'abWXYe');
        equal(f('abcde', 'de', 'WXYZ'), 'abcWXYZ');
    });


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


}());
