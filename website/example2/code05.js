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
        X: 10
    };


    function toDecimal(romanNumerals) {
        return DICTIONARY[romanNumerals];
    }


    window.roman = {
        toDecimal: toDecimal
    };


}());
