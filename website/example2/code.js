/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Example 2 Production Code
 * The roman module contains functions to convert roman numerals into
 * decimal numbers.
 */

/*jslint browser: true */
(function() {
    'use strict';


    var DICTIONARY = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };


    function toDecimal(romanNumerals) {
        var i, number = 0;
        for (i = 0; i < romanNumerals.length; i += 1) {
            number += DICTIONARY[romanNumerals[i]];
        }
        return number;
    }


    window.roman = {
        toDecimal: toDecimal
    };


}());
