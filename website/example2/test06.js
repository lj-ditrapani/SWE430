/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Example 2 Test Code
 * Test the roman module
 */

/*global test,equal,roman*/
(function() {
    'use strict';


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
            ['X', 10],
            ['L', 50],
            ['C', 100],
            ['D', 500],
            ['M', 1000]
        ];
        runTests(tests);
    });


}());
