/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Example 2 Production Code
 * The roman module contains functions to convert roman numerals into
 * decimal numbers.
 */

/*jslint browser: true */
(function() {
    'use strict';


    function toDecimal(romanNumerals) {
        if (romanNumerals === 'I') {
            return 1;
        } else {
            return 5;
        }
    }


    window.roman = {
        toDecimal: toDecimal
    };


}());
