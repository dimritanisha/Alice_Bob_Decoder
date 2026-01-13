Add files via upload
In this Assignment Alice wants to send a message to Bob but doesn't want Eve to read it. So decides to encrypt it using a scheme. This scheme follows the following rule:
A = ._
B = _...
C = _._.
D = _..
E = .
F = .._.
G = __.
H = ....
I = ..
J = .___
K = _._
L = ._..
M = __
N = _.
O = ___
P = .__.
Q = __._
R = ._.
S = ...
T = _
U = .._
V = ..._
W = .__
X = _.._
Y = _.__
Z = __..
For example, "__.._...__" is the word "GREAT". Unfortunately, this
sequence also decrypts to 'GAEEAT', 'GAEEEM', 'MEAIW', 'TTELW', 'ZTEUT', etc., along
with many others. To solve this problem, Alice asks you to find a
solution while she works on developing her own language.
Input
The input will be a string of encrypted message.
Output
Print all of the possible decodings, separated by newlines,
in alphabetical order.
Example
STDIN
_.__.

STDOUT:
KN
KTE
NG
NME
NTN
NTTE
TAN
TATE
TEG
TEME
TETN
TETTE
TP
TWE
YE
 first in the program I made a variable called letter_code which means letter to code which is holding the mapping of letter to their corresponding encrypted codes and then reverse the mapping like code_letter  and  removed alll whitespaces and next line character of input by using strip function ,then by creating backtracking function having pos and path as parameters in that function where pos is representing current index of encrypted string and path as the decoded string  , when the end of encrypted string it is added to result list . all possible results  then stored in a list called result. Also ensured that there is no overflowing  then started recursion which helps in moving forward in encrypted string and append the decoded  string to path  and then started decoding from beginning and then sorted the list alphabetically.
