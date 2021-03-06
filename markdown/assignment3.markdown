SWE 430 Assignment 3 --- Password Checker
=====================================

Assignment Instructions
---------------------

Use test-driven development (TDD) along with qUnit, the xUnit testing framework, to implement the password checker code module (defined below) for a DoD information system.  Ensure you write a unit test before writing the code to pass the unit test.

The TDD cycle:

- Write a test
- Run all your tests, ensuring the new test fails
- Write the production code to pass the test
- Run all your tests, ensuring the new test passes
- Refactor your production code if necessary
- Run all your tests
- Refactor your test code if necessary
- Run all your tests
- Repeat

Submission Instructions

- zip Environment users:  Turn in both the source code (code.js) and the
  unit tests (test.js) in the blackboard Assignment 3 Submission.
- jsbin Environment users:  Submit the URL of your jsbin project in the
  blackboard Assignment 3 Submission.

If you have any questions, run into problems, or need clarification, please let me know.  Your production code will be evaluated by running it against a set of reference test cases (written according to the specification).  Your unit test cases will be evaluated by using them to test a faulty implementation.

Password Checker Specification
------------------------------

The check function in the password module determines if a proposed
password is valid or not.
Function signature:  `String X Array of Strings => boolean X String`

- Inputs: a proposed password (String) and an array of 0 to 6 previous
  passwords (Array of Strings).
- Output: A 2 element array containing a boolean and a String.  The
  boolean is true if the proposed password is valid, false otherwise.
  When the boolean is false, the String provides the reason the
  password is invalid.  When the boolean is true, the second value is
  the empty string: `""`.

Precondition:  All previous passwords are assumed to be valid (you don't have to test that the previous passwords are valid, only test the proposed password.)  Here is an example of using the password.check function:

    var proposed_password, previous_passwords, pair, result, reason;
    proposed_password = 'P@55W*rd';
    previous_passwords = ['aaAA11!!', 'bbBB22@@'];
    pair = password.check(proposed_password, previous_passwords);
    result = pair[0];       // true or false boolean value
    reason = pair[1];       // String value

Because `proposed_password` is a valid password, the result variable would evaluate to true and the reason would be `""`; the empty string.


    var proposed_password, previous_passwords, pair, result, reason;
    proposed_password = 'aaaaaaaaaaaaaaaBB22##';
    previous_passwords = ['aaAA11!!', 'bbBB22@@'];
    pair = password.check(proposed_password, previous_passwords);
    result = pair[0];       // true or false boolean value
    reason = pair[1];       // String value

In this case, the result variable would evaluate to false and the reason would be `"too long"`.  Even though the password fails 2 rules, `"too long"` and `"4+ char substring"`, only the reason for the first failure (according to the order listed below) is reported.

The only global variable your code should export is an object (which will serve as a module) named `password` which contains a function named `check()`.  This is accomplished in the same way we exported the `stringInfo` object, which contained 4 functions, in Example 1.


    // code.js

    var password = {};          // Create password module

    // Create check function and attach it to password module
    password.check = function(proposed_password, previous_passwords) {
        // body of function goes here
        // ...
    };

    window.password = password; // Export password module

In order to be declared "valid," all accepted passwords must adhere to the following criteria (the reason string returned for failing the associated rule is in green and parentheses):

1. A password must be at least 8 (**too short**) and no more than 20 characters long (**too long**).
2. A password is comprised of only [ASCII](http://en.wikipedia.org/wiki/ASCII) printable characters.  No whitespcae---tabs, space, etc., control characters, or unicode is allowed (**not printable ASCII**).
3. Each password must contain:
    - 2 or more upper-case letters (**upper-case**)
    - 2 or more lower-case letters (**lower-case**)
    - 2 or more digit characters (0-9) (**digit**)
    - 2 or more non-alphanumeric characters (**non-alphanumeric**)
4. A password cannot be similar to any of the user's previous six passwords.
      "Similar to" is defined as having any of the following:
    - 6 or more of the same characters anywhere in the two passwords (**6+ same chars**)
        - Example: aaaaaaAA11!! and aaOO22@@aaa are not similar
        - Example: aaaaaaAA11!! and _aaa_OO22@@_aaa_ are similar
        - Example: _aoAO12_!! and _oa_@_O1A_@_2_ are similar
    - 4 or more of the same characters in the same relative position 
        from the start of the password 
        (**4+ chars in same position**)
        - Example: aAaA!1!1 and oAoA@1@2 are not similar
        - Example: a_A_a_A_!_1_!_1_ and o_A_o_A_@_1_@_1_ are similar
    - Any identical 4-character substring 
        (**4+ char substring**)
        - Example: aaAA11!! and AA12oo@@ are not similar
        - Example: aa_AA11_!! and _AA11_oo@@ are similar

The appropriate "reason string" for each rule is shown in parentheses and in green.  The check() function only returns one reason for a password failure.  If a password fails multiple rules, only the reason for the first rule failed, according to the order listed above, is returned by the function.  Be sure to use the exact reason strings listed above---they are case sensitive.

Because this module deals with password strings, string methods will be particularly useful in completing the assignment.  Take a moment to review the "Strings" section of the [JavaScript Tutorial](javascript-tutorial.html).  Pay special attention to the "Useful String Methods" table.
Also review the "Arrays" section.  Array indexing will be useful in dealing with the set of 6 previous passwords.

When writing certain tests for this assignment, you may want to express an arbitrary Unicode character within a string.  In order to express any Unicode character, the format is as follows `'\uDDDD'` where DDDD is the four hexadecimal digits that represent the desired character.  For example, `'\u2660'` represents a spade.

Therefore, the line of code:

    var s = 'My favorite suit is \u2660';

Will cause variable `s` to point to the string 'My favorite suit is &#9824;'.

Some ASCII control characters can be expressed directly using an escape sequence.  For example, the line feed character (the tenth character, or 0x0A in hexadecimal) can be expressed within a string a `'\n'`.  However, this character can also be expressed using the Unicode notation as `'\u000A'`.  So the Unicode notation allows you to express all Unicode characters, including ASCII control characters.

Assignment 3 Environments (use one or the other):

- [Assignment 3 zip Environment](assignment3.zip)
- [Assignment 3 jsbin Environment][jsbin]

[Instructions](instructions.html)
for the environments are available.

[jsbin]: http://jsbin.com/swe430_assignment3/latest/edit?javascript,live
