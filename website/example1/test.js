/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Example 1 Test Code
 */

/*global test,equal,stringStat*/
(function() {
    'use strict';


    function runTests(functionName, tests) {
        var i, pair;
        for (i = 0; i < tests.length; i += 1) {
            pair = tests[i];
            equal(stringStat[functionName](pair[0]), pair[1]);
        }
    }


    test('Count upper-case characters', function() {
        var tests = [
            ['abcDEFgHI', 5],
            ['ABcDe\u0003\u2660\u0100', 3],
            ['abcZ', 1],
            ['abcde', 0],
            ['@[\u0003\u2660\u0100', 0]
        ];
        runTests('countUpperCaseLetters', tests);
    });


    test('Count lower-case characters', function() {
        var tests = [
            ['ABCdefGhi', 5],
            ['abCdE\u0003\u2660\u0100', 3],
            ['ABCz', 1],
            ['ABCDE', 0],
            ['`{\u0003\u2660\u0100', 0]
        ];
        runTests('countLowerCaseLetters', tests);
    });


    test('Count control characters', function() {
        var tests = [
            ['abc\u0003\u007F\u0000de', 3],
            ['\u0000\u0010abc', 2],
            ['abc\u001F', 1],
            ['abcde\u0100\u2660', 0]
        ];
        runTests('countControlCharacters', tests);
    });


    test('Count Non-ASCII characters', function() {
        var tests = [
            ['abc\u00FF\u2660\u0000\uFFFFde', 3],
            ['\u00FF\u007F\u0080abc', 2],
            ['abc\u0080', 1],
            ['abcde', 0],
            ['\u0000abcde\u007F\u0000', 0]
        ];
        runTests('countNonASCIICharacters', tests);
    });


}());
