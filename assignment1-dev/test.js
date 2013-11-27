/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Assignment 1
 * Test the basicMath library
 */


/*global test,equal,ok,basicMath*/
(function() {
    'use strict';


    test('Add', function() {
        equal(basicMath.add(0, 0), 0);
        equal(basicMath.add(5, 2), 7);
        equal(basicMath.add(-12, 10), -2);
    });


    test('Subtract', function() {
        equal(basicMath.subtract(0, 0), 0);
        equal(basicMath.subtract(3, 7), -4);
        equal(basicMath.subtract(-12, -15), 3);
    });


    test('Multiply', function() {
        equal(basicMath.multiply(0, 0), 0);
        equal(basicMath.multiply(3, 7), 21);
        equal(basicMath.multiply(9, -4), -36);
        equal(basicMath.multiply(-2, -5), 10);
        equal(basicMath.multiply(-6, 1), -6);
    });


    test('Divide', function() {
        ok(isNaN(basicMath.divide(0, 0)));
        equal(basicMath.divide(16, 5), 3.2);
        equal(basicMath.divide(-9, -3), 3);
    });


}());
