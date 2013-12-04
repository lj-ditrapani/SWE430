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


    stringInfo.countUpperCaseLetters = function(string) {
        var i, code, count = 0;
        for (i = 0; i < string.length; i += 1) {
            code = string.charCodeAt(i);
            if (code >= 65 && code <= 90) {
                count += 1;
            }
        }
        return count;
    };


    window.stringInfo = stringInfo;


}());
