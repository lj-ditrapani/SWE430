/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Assignment 1
 * basicMath library
 */


/*global test,equal,stringStat*/
(function() {
    'use strict';


    test('Add', function() {
        equal(basicMath.add(0, 0), 0)
        equal(basicMath.add(5, 2), 7)
        equal(basicMath.add(-12, 10), -2)
    });


    test('Subtract', function() {
        equal(basicMath.subtract(0, 0), 0)
        equal(basicMath.subtract(3, 7), -4)
        equal(basicMath.subtract(-12, -15), 3)
    });


}());
