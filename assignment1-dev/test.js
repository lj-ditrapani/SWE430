/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Assignment 1
 * Test the basicMath library
 */


/*global test,equal,ok,basicMath*/
(function() {
    'use strict';


    function runTests(function_name, tests) {
        var i, triple, result;
        for (i = 0; i < tests.length; i += 1) {
            triple = tests[i];
            result = basicMath[function_name](triple[0], triple[1]);
            equal(result, triple[2]);
        }
    }


    test('Add', function() {
        var tests = [
            [0, 0, 0],
            [5, 2, 7],
            [-12, 10, -2]
        ];
        runTests('add', tests);
    });


    test('Subtract', function() {
        var tests = [
            [0, 0, 0],
            [3, 7, -4],
            [-12, -15, 3]
        ];
        runTests('subtract', tests);
    });


    test('Multiply', function() {
        var tests = [
            [0, 0, 0],
            [3, 7, 21],
            [9, -4, -36],
            [-2, -5, 10],
            [-6, 1, -6]
        ];
        runTests('multiply', tests);
    });


    test('Divide', function() {
        var tests = [
            [0, 100, 0],
            [7, 1, 7],
            [1, 8, 0.125],
            [16, 5, 3.2],
            [7, -2, -3.5],
            [-9, -3, 3],
            [-6, 12, -0.5]
        ];
        ok(isNaN(basicMath.divide(0, 0)));
        runTests('divide', tests);
    });


}());
