/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Example 1 Production Code
 * The stringStat module contains functions for counting the number of
 * a specified type of character present in a string.
 */

/*jslint browser: true */
(function() {
    'use strict';


    var stringStat = {};


    function countCharacters(string, predicate) {
        var i, count = 0;
        for (i = 0; i < string.length; i += 1) {
            if (predicate(string.charCodeAt(i))) {
                count += 1;
            }
        }
        return count;
    }


    stringStat.countUpperCaseLetters = function(string) {
        function predicate(code) {
            return code >= 65 && code <= 90;
        }
        return countCharacters(string, predicate);
    };


    stringStat.countLowerCaseLetters = function(string) {
        function predicate(code) {
            return code >= 97 && code <= 122;
        }
        return countCharacters(string, predicate);
    };


    stringStat.countControlCharacters = function(string) {
        function predicate(code) {
            return code <= 31 || code === 127;
        }
        return countCharacters(string, predicate);
    };


    window.stringStat = stringStat;


}());
