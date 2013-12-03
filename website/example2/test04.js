/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Example 2 Test Code
 * Test the roman module
 */

/*global test,equal,roman*/
(function() {
    'use strict';


    test('I -> 1', function() {
        equal(roman.toDecimal('I'), 1);
    });


    test('V -> 5', function() {
        equal(roman.toDecimal('V'), 5);
    });


    test('X -> 10', function() {
        equal(roman.toDecimal('X'), 10);
    });


}());
