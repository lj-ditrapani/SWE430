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


    function replaceTwoCharacters(string, twoCharacters, replacement) {
        var index = string.indexOf(twoCharacters);
        if (index === -1) {
            return string;
        }
        return string.slice(0, index) + replacement +
               string.slice(index + 2, string.length);
    }


    function rewrite(romanNumerals) {
        var i, subtractivePairs, replacements;
        subtractivePairs = [
            'IV', 'IX', 'XL', 'XC', 'CD', 'CM'
        ];
        replacements = [
            'IIII', 'VIIII', 'XXXX', 'LXXXX', 'CCCC', 'DCCCC'
        ];
        for (i = 0; i < subtractivePairs.length; i += 1) {
            romanNumerals = replaceTwoCharacters(romanNumerals,
                                                 subtractivePairs[i],
                                                 replacements[i]);
        }
        return romanNumerals;
    }


    function toDecimal(romanNumerals) {
        var i, number = 0;
        for (i = 0; i < romanNumerals.length; i += 1) {
            number += DICTIONARY[romanNumerals[i]];
        }
        return number;
    }


    window.roman = {
        replaceTwoCharacters: replaceTwoCharacters,
        rewrite: rewrite,
        toDecimal: toDecimal
    };


}());
