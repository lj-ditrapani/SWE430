/** Author:  Lyall Jonathan Di Trapani =================================
 * Example 1 Test Code
 **/

/*global test,equal,stringStat*/
(function() {
    'use strict';

    test('Count upper-case characters', function() {
        var i, pair, tests = [
            ['abcDEFgHI', 5],
            ['ABcDe', 3],
            ['abcD', 1],
            ['abcde', 0]
        ];
        for (i = 0; i < tests.length; i += 1) {
            pair = tests[i];
            equal(stringStat.countUpperCaseLetters(pair[0]), pair[1]);
        }
        
    });

    test('Count control characters', function() {
        var i, pair, tests = [
            ['abc\u0003\u007F\u0000de', 3],
            ['\u0000\u0010abc', 2],
            ['abc\u001F', 1],
            ['abcde', 0]
        ];
        for (i = 0; i < tests.length; i += 1) {
            pair = tests[i];
            equal(stringStat.countControlCharacters(pair[0]), pair[1]);
        }
    });

}());
