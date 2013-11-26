/** Author:  Lyall Jonathan Di Trapani =================================
 * Example 1 Production Code
 **/

/*jslint browser: true */
(function() {
    'use strict';

    var stringStat = {};

    stringStat.countUpperCaseLetters = function(string) {
        var i, code, count = 0;
        for (i = 0; i < string.length; i += 1) {
            code = string.charCodeAt(i);
            if (code >= 65 && code <= 90) {
                count += 1;
            }
        }
        return count;
    };

    

    stringStat.countControlCharacters = function(string) {
        var i, code, count = 0;
        for (i = 0; i < string.length; i += 1) {
            code = string.charCodeAt(i);
            if (code <= 0x1F || code === 0x7F) {
                count += 1;
            }
        }
        return count;
    };

    window.stringStat = stringStat;

}());
