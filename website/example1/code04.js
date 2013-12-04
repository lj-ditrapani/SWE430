/**
 * Author:  Lyall Jonathan Di Trapani ==================================
 * Example 1 Production Code
 * The stringInfo module contains functions for counting the number of
 * a specified type of character present in a string.
 */

/*jslint browser: true */
(function() {
    'use strict';


    var stringInfo = {};


    function countCharacters(string, predicate) {
        var i, count = 0;
        for (i = 0; i < string.length; i += 1) {
            if (predicate(string.charCodeAt(i))) {
                count += 1;
            }
        }
        return count;
    }


    stringInfo.countUpperCaseLetters = function(string) {
        function predicate(code) {
            return code >= 65 && code <= 90;
        }
        return countCharacters(string, predicate);
    };


    stringInfo.countLowerCaseLetters = function(string) {
        function predicate(code) {
            return code >= 97 && code <= 122;
        }
        return countCharacters(string, predicate);
    };


    window.stringInfo = stringInfo;


}());
