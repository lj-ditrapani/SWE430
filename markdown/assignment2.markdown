Assignment 2
========================================================================

In this assignment, you will apply what you learned in Example 2.
Use the Test-driven Development (TDD) process to iteratively develop the module definde below.  You will write both the test code and the production code on your own.

The TDD cycle:

- Write a test
- Run all your tests, ensuring the new test fails
- Write the code to pass the test
- Run all your tests, ensuring the new test passes
- Refactor your production code if necessary
- Run all your tests
- Refactor your test code if necessary
- Run all your tests
- Repeat


For Assignment 2, you will create a module named `wordModule`
with the following 4 functions:

<table>
<tr>
    <th>Function</th>
    <th>Parameters</th>
    <th>Description</th>
</tr>
<tr>
    <td><code>toWords</code></td>
    <td><code>string</code></td>
    <td>Convert the string of words into an Array of
    <strong>lower-case</strong> words.
    If the string is empty (<code>''</code>),
    then return the empty array (<code>[]</code>).</td>
</tr>
<tr>
    <td><code>inList</code></td>
    <td><code>word, list</code></td>
    <td>If word is found in list, return true.
    Otherwise, return false.</td>
</tr>
<tr>
    <td><code>capitalize</code></td>
    <td><code>word</code></td>
    <td>Return the word with the first letter capitalize.
    If the first letter is not a letter of the alphabet (a-z),
    then return it as-is.</td>
</tr>
<tr>
    <td><code>titleize</code></td>
    <td><code>string</code></td>
    <td>Return string in title form
    (see <em>Rules for titles</em>).</td>
</tr>
</table>

Example usage:

    var words, result, word, title;

    words = wordModule.toWords('UPPER CASE and lower case');
    // words is ['UPPER', 'CASE', 'and', 'lower', 'case']

    result = wordModule.inList('pear', ['apple', 'pear', 'banana']);
    // result is true

    word = wordModule.capitalize('pear');
    // word is 'Pear'

    title = wordModule.titleize('a title for a book');
    // title is 'A Title for a Book'

Rules for titles:

- The first letter of the first and last words are always capitalized.
- The first letter of each word is capitalized with the following
  exception.
- The following words are not capitalized,
  unless they appear as the first or last words:
  `a an and at but by for in nor of on or so the to up yet`.
- Digits, symbols, and punctuation are left as-is.

Useful JavaScript [String methods][string]:
`split()` `toLowerCase()` `toUpperCase()` `slice()`

Useful JavaScript [Array methods][array]:
`push()`

**Note**:  The `toWords()`, `inList()`, and `capitalize()` functions can
(and should) be used to construct the `titleize()` function.

Environments:

- zip Environment users:  Turn in both the source code (code.js) and the
  unit tests (test.js) in the blackboard Assignment 2 Submission.
- jsbin Environment users:  Submit the URL of your jsbin project in the
  blackboard Assignment 2 Submission.

Assignment 2 Environments (use one or the other):

- [Assignment 2 zip Environment](assignment2.zip)
- [Assignment 2 jsbin Environment][jsbin]

[Instructions](instructions.html)
for the environments are available.

[string]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/prototype#Methods
[array]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/prototype#Methods
[jsbin]: http://jsbin.com/swe430_assignment2/latest/edit?javascript,live
