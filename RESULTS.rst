Tabulated Summary
=================
=====================================  ==================  ===========  =============  ============  ======================  ============  ===========  =====================  ============
Terminal Software                      Software Version    OS System    FINAL score    WIDE score    Wide Unicode version    LANG score    ZWJ score    ZWJ Unicode version    VS16 score
=====================================  ==================  ===========  =============  ============  ======================  ============  ===========  =====================  ============
`iTerm2`_                              3.5.0               Darwin       A+             C-            12.0.0                  C+            A+           15.1                   A-
`kitty`_                               0.30.1              Darwin       A-             A+            15.0.0                  A+            F            na                     A+
`Konsole`_                             22.12.3             Linux        B              A+            15.0.0                  C             A            15.1                   F
`WezTerm`_                             20230712            Darwin       B              A-            15.0.0                  C-            A+           15.1                   F
`ExtratermQt`_                         0.73.0              Darwin       B-             A-            14.0.0                  F             F            na                     A+
`cool-retro-term`_                     1.2.0               Darwin       C              F             9.0.0                   F             C-           11.0                   A-
`QTerminal`_                           1.2.0               Linux        C              A+            15.0.0                  A+            F            2.0                    F
`zoc`_                                 8.07.0              Darwin       C+             B+            14.0.0                  F             F            na                     A+
`Alacritty`_                           0.12.3_1            Darwin       D+             A+            15.0.0                  C             F            2.0                    F
`Tabby`_                               1.0.201             Darwin       D-             C             12.0.0                  C             F            2.0                    F
`VSCode Terminal <VSCode_Terminal_>`_  1.84.0              Darwin       D-             C             12.0.0                  C             F            2.0                    F
`Hyper`_                               4.0.0 canary5       Darwin       D-             C             12.0.0                  C             F            2.0                    F
`mlterm`_                              3.9.0               Linux        D-             F             9.0.0                   B+            F            na                     F
`Terminal`_                            2.12.7              Darwin       F              F             9.0.0                   C             F            na                     F
`XTerm`_                               379                 Linux        F              F             9.0.0                   C             F            2.0                    F
`GNOME Terminal <GNOME_Terminal_>`_    3.46.8              Linux        F              F             9.0.0                   C             F            2.0                    F
`xfce4-terminal`_                      1.0.4               Linux        F              F             9.0.0                   C             F            2.0                    F
`st`_                                  0.9                 Linux        F              F             9.0.0                   C             F            2.0                    F
`LXTerminal`_                          0.4.0               Linux        F              F             9.0.0                   C             F            2.0                    F
`zutty`_                               0.14                Linux        F              F             9.0.0                   C             F            2.0                    F
=====================================  ==================  ===========  =============  ============  ======================  ============  ===========  =====================  ============

Definitions:

- *WIDE score*: Determined by version release level of wide character
  support, multiplied by the pct of wide codepoints supported at that
  version, scaled.
- *Wide Unicode version*: The Unicode version specification most
  closely matching in compatibility with this emulator, scaled.
- *LANG score*: The percentage of international languages tested
  as having support, scaled.
- *ZWJ score*: Determined by version release level of emoji sequences
  with Zero-Width Joiner support, multiplied by the pct of emoji
  sequences supported at that version, scaled.
- *VS16 score*: Determined by the number of Emoji using Variation
  Selector-16 supported as wide characters, scaled.

Software details
================

.. _Tabby:

Tabby
-----

Tested Software version 1.0.201 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Tabby appears to be 
**12.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26        100
'5.2.0'            79        269         70.632
'6.0.0'             0         13        100
'9.0.0'             0       1000        100
'10.0.0'            0        735        100
'11.0.0'            0         62        100
'12.0.0'            0         62        100
'12.1.0'            0          1        100
'13.0.0'          100        100          0
'14.0.0'           41         41          0
'15.0.0'           15         15          0
'15.1.0'            5          5          0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 13.0.0, of python string 
``\u31bb`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe3\x86\xbb|\\n12|\\n"
    ㆻ|
    12|

python `wcwidth`_ measures width 2,
while *Tabby* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Tabby* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *Tabby* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Tabby* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *Tabby* measures width 1

.. _cool-retro-term:

cool-retro-term
---------------

Tested Software version 1.2.0 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for cool-retro-term appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'            19         26       26.9231
'5.2.0'           100        109        8.25688
'6.0.0'             2         13       84.6154
'9.0.0'            27       1000       97.3
'10.0.0'          100        100        0
'11.0.0'           62         62        0
'12.0.0'           62         62        0
'12.1.0'            1          1        0
'13.0.0'          100        100        0
'14.0.0'           41         41        0
'15.0.0'           15         15        0
'15.1.0'            5          5        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 9.0.0, of python string 
``\u231a`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe2\x8c\x9a|\\n12|\\n"
    ⌚|
    12|

python `wcwidth`_ measures width 2,
while *cool-retro-term* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *cool-retro-term* appears to be 
**11.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              22         22         0
'4.0'             100        100         0
'5.0'               0        100       100
'11.0'              1         73        98.6301
'12.0'             24        112        78.5714
'12.1'             72        165        56.3636
'13.0'             38         51        25.4902
'13.1'             70         83        15.6627
'14.0'             20         20         0
'15.0'              0          1       100
'15.1'             87        109        20.1835
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 11.0, of python string 
``\U0001f3f4\u200d\u2620\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x8f\xb4\xe2\x80\x8d\xe2\x98\xa0\xef\xb8\x8f|\\n12|\\n"
    🏴‍☠️|
    12|

python `wcwidth`_ measures width 2,
while *cool-retro-term* measures width 4

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *cool-retro-term* is 12 errors out of 100 total codepoints tested, 88.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``\u2694\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe2\x9a\x94\xef\xb8\x8f|\\n12|\\n"
    ⚔️|
    12|

python `wcwidth`_ measures width 2,
while *cool-retro-term* measures width 1

.. _VSCode_Terminal:

VSCode Terminal
---------------

Tested Software version 1.84.0 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for VSCode Terminal appears to be 
**12.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26        100
'5.2.0'            79        269         70.632
'6.0.0'             0         13        100
'9.0.0'             0       1000        100
'10.0.0'            0        735        100
'11.0.0'            0         62        100
'12.0.0'            0         62        100
'12.1.0'            0          1        100
'13.0.0'          100        100          0
'14.0.0'           41         41          0
'15.0.0'           15         15          0
'15.1.0'            5          5          0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 13.0.0, of python string 
``\u31bb`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe3\x86\xbb|\\n12|\\n"
    ㆻ|
    12|

python `wcwidth`_ measures width 2,
while *VSCode Terminal* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *VSCode Terminal* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *VSCode Terminal* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *VSCode Terminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *VSCode Terminal* measures width 1

.. _Terminal:

Terminal
--------

Tested Software version 2.12.7 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Terminal appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            79        269        70.632
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'           15         15         0
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 10.0.0, of python string 
``\U0001b00b`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2,
while *Terminal* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Terminal* appears to be 
**None**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              22         22              0
'4.0'             100        100              0
'5.0'             100        100              0
'11.0'             73         73              0
'12.0'            100        100              0
'12.1'            100        100              0
'13.0'             51         51              0
'13.1'             83         83              0
'14.0'             20         20              0
'15.0'              1          1              0
'15.1'            100        100              0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *Terminal* measures width 7

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Terminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *Terminal* measures width 1

.. _XTerm:

XTerm
-----

Tested Software version 379 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for XTerm appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'           100        210        52.381
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'           15         15         0
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 10.0.0, of python string 
``\U0001b00b`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2,
while *XTerm* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *XTerm* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *XTerm* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *XTerm* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *XTerm* measures width 1

.. _Konsole:

Konsole
-------

Tested Software version 22.12.3 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Konsole appears to be 
**15.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            79        269        70.632
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           22        735        97.0068
'11.0.0'            1         62        98.3871
'12.0.0'            1         62        98.3871
'12.1.0'            0          1       100
'13.0.0'           16        541        97.0425
'14.0.0'            1         41        97.561
'15.0.0'            0         15       100
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 15.1.0, of python string 
``\u2ffc`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe2\xbf\xbc|\\n12|\\n"
    ⿼|
    12|

python `wcwidth`_ measures width 2,
while *Konsole* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Konsole* appears to be 
**15.1**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'               1         22        95.4545
'4.0'              49        579        91.5371
'5.0'               0        100       100
'11.0'              0         73       100
'12.0'              0        112       100
'12.1'              0        165       100
'13.0'              1         51        98.0392
'13.1'              2         83        97.5904
'14.0'              0         20       100
'15.0'              0          1       100
'15.1'              1        109        99.0826
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 15.1, of python string 
``\u26d3\ufe0f\u200d\U0001f4a5`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe2\x9b\x93\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x92\xa5|\\n12|\\n"
    ⛓️‍💥|
    12|

python `wcwidth`_ measures width 2,
while *Konsole* measures width 1

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Konsole* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *Konsole* measures width 1

.. _GNOME_Terminal:

GNOME Terminal
--------------

Tested Software version 3.46.8 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for GNOME Terminal appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            79        269        70.632
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'            1         15        93.3333
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 10.0.0, of python string 
``\U0001b00b`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2,
while *GNOME Terminal* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *GNOME Terminal* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *GNOME Terminal* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *GNOME Terminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *GNOME Terminal* measures width 1

.. _xfce4-terminal:

xfce4-terminal
--------------

Tested Software version 1.0.4 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for xfce4-terminal appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            79        269        70.632
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'            1         15        93.3333
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 10.0.0, of python string 
``\U0001b00b`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2,
while *xfce4-terminal* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *xfce4-terminal* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *xfce4-terminal* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *xfce4-terminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *xfce4-terminal* measures width 1

.. _st:

st
--

Tested Software version 0.9 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for st appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'           100        210        52.381
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'           15         15         0
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 10.0.0, of python string 
``\U0001b00b`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2,
while *st* measures width 0

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *st* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *st* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *st* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *st* measures width 1

.. _Hyper:

Hyper
-----

Tested Software version 4.0.0 canary5 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Hyper appears to be 
**12.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26        100
'5.2.0'            79        269         70.632
'6.0.0'             0         13        100
'9.0.0'             0       1000        100
'10.0.0'            0        735        100
'11.0.0'            0         62        100
'12.0.0'            0         62        100
'12.1.0'            0          1        100
'13.0.0'          100        100          0
'14.0.0'           41         41          0
'15.0.0'           15         15          0
'15.1.0'            5          5          0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 13.0.0, of python string 
``\u31bb`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe3\x86\xbb|\\n12|\\n"
    ㆻ|
    12|

python `wcwidth`_ measures width 2,
while *Hyper* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Hyper* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *Hyper* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Hyper* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *Hyper* measures width 1

.. _Alacritty:

Alacritty
---------

Tested Software version 0.12.3_1 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Alacritty appears to be 
**15.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26        100
'5.2.0'            79        269         70.632
'6.0.0'             0         13        100
'9.0.0'             0       1000        100
'10.0.0'            0        735        100
'11.0.0'            0         62        100
'12.0.0'            0         62        100
'12.1.0'            0          1        100
'13.0.0'            0        541        100
'14.0.0'            0         41        100
'15.0.0'            0         15        100
'15.1.0'            5          5          0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 15.1.0, of python string 
``\u2ffc`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe2\xbf\xbc|\\n12|\\n"
    ⿼|
    12|

python `wcwidth`_ measures width 2,
while *Alacritty* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Alacritty* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *Alacritty* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Alacritty* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *Alacritty* measures width 1

.. _iTerm2:

iTerm2
------

Tested Software version 3.5.0 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for iTerm2 appears to be 
**12.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            79        269        70.632
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'            1         15        93.3333
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 12.0.0, of python string 
``\U0001b165`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x85\xa5|\\n12|\\n"
    𛅥|
    12|

python `wcwidth`_ measures width 2,
while *iTerm2* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *iTerm2* appears to be 
**15.1**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'               0         22       100
'4.0'              40        579        93.0915
'5.0'               0        100       100
'11.0'              0         73       100
'12.0'              0        112       100
'12.1'              0        165       100
'13.0'              0         51       100
'13.1'              0         83       100
'14.0'              0         20       100
'15.0'              0          1       100
'15.1'              0        109       100
=========  ==========  =========  =============

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *iTerm2* is 9 errors out of 100 total codepoints tested, 91.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *iTerm2* measures width 1

.. _QTerminal:

QTerminal
---------

Tested Software version 1.2.0 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for QTerminal appears to be 
**15.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26        100
'5.2.0'           100        210         52.381
'6.0.0'             0         13        100
'9.0.0'             0       1000        100
'10.0.0'            0        735        100
'11.0.0'            0         62        100
'12.0.0'            0         62        100
'12.1.0'            0          1        100
'13.0.0'            0        541        100
'14.0.0'            0         41        100
'15.0.0'            0         15        100
'15.1.0'            5          5          0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 15.1.0, of python string 
``\u2ffc`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe2\xbf\xbc|\\n12|\\n"
    ⿼|
    12|

python `wcwidth`_ measures width 2,
while *QTerminal* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *QTerminal* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *QTerminal* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *QTerminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *QTerminal* measures width 1

.. _LXTerminal:

LXTerminal
----------

Tested Software version 0.4.0 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for LXTerminal appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            79        269        70.632
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'            1         15        93.3333
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 10.0.0, of python string 
``\U0001b00b`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2,
while *LXTerminal* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *LXTerminal* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *LXTerminal* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *LXTerminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *LXTerminal* measures width 1

.. _zoc:

zoc
---

Tested Software version 8.07.0 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for zoc appears to be 
**14.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            55        269        79.5539
'6.0.0'            10         13        23.0769
'9.0.0'            27       1000        97.3
'10.0.0'            6        735        99.1837
'11.0.0'            0         62       100
'12.0.0'           12         62        80.6452
'12.1.0'            0          1       100
'13.0.0'            2        541        99.6303
'14.0.0'            2         41        95.122
'15.0.0'            1         15        93.3333
'15.1.0'            4          5        20
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 14.0.0, of python string 
``\U0001f6dd`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x9b\x9d|\\n12|\\n"
    🛝|
    12|

python `wcwidth`_ measures width 2,
while *zoc* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *zoc* appears to be 
**None**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              22         22              0
'4.0'             100        100              0
'5.0'             100        100              0
'11.0'             73         73              0
'12.0'            100        100              0
'12.1'            100        100              0
'13.0'             51         51              0
'13.1'             83         83              0
'14.0'             20         20              0
'15.0'              1          1              0
'15.1'            100        100              0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *zoc* measures width 6

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *zoc* is 0 errors out of 100 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.
.. _kitty:

kitty
-----

Tested Software version 0.30.1 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for kitty appears to be 
**15.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            79        269        70.632
'6.0.0'             1         13        92.3077
'9.0.0'             0       1000       100
'10.0.0'           20        735        97.2789
'11.0.0'            1         62        98.3871
'12.0.0'            1         62        98.3871
'12.1.0'            0          1       100
'13.0.0'           16        541        97.0425
'14.0.0'            1         41        97.561
'15.0.0'            0         15       100
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 15.1.0, of python string 
``\u2ffc`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xe2\xbf\xbc|\\n12|\\n"
    ⿼|
    12|

python `wcwidth`_ measures width 2,
while *kitty* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *kitty* appears to be 
**None**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              22         22              0
'4.0'             100        100              0
'5.0'             100        100              0
'11.0'             73         73              0
'12.0'            100        100              0
'12.1'            100        100              0
'13.0'             51         51              0
'13.1'             83         83              0
'14.0'             20         20              0
'15.0'              1          1              0
'15.1'            100        100              0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *kitty* measures width 6

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *kitty* is 0 errors out of 100 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.
.. _WezTerm:

WezTerm
-------

Tested Software version 20230712 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for WezTerm appears to be 
**15.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            79        269        70.632
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           55        541        89.8336
'14.0.0'            4         41        90.2439
'15.0.0'            1         15        93.3333
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 15.0.0, of python string 
``\U0001fabc`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\xaa\xbc|\\n12|\\n"
    🪼|
    12|

python `wcwidth`_ measures width 2,
while *WezTerm* measures width 0

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *WezTerm* appears to be 
**15.1**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'               0         22            100
'4.0'               0        579            100
'5.0'               0        100            100
'11.0'              0         73            100
'12.0'              0        112            100
'12.1'              0        165            100
'13.0'              0         51            100
'13.1'              0         83            100
'14.0'              0         20            100
'15.0'              0          1            100
'15.1'              0        109            100
=========  ==========  =========  =============

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *WezTerm* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *WezTerm* measures width 1

.. _zutty:

zutty
-----

Tested Software version 0.14 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for zutty appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'           100        210        52.381
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'           15         15         0
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 10.0.0, of python string 
``\U0001b00b`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2,
while *zutty* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *zutty* appears to be 
**2.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              21         22        4.54545
'4.0'             100        100        0
'5.0'             100        100        0
'11.0'             73         73        0
'12.0'            100        100        0
'12.1'            100        100        0
'13.0'             50         51        1.96078
'13.1'             83         83        0
'14.0'             20         20        0
'15.0'              1          1        0
'15.1'            100        100        0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *zutty* measures width 5

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *zutty* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *zutty* measures width 1

.. _ExtratermQt:

ExtratermQt
-----------

Tested Software version 0.73.0 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for ExtratermQt appears to be 
**14.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26        100
'5.2.0'            79        269         70.632
'6.0.0'             0         13        100
'9.0.0'             0       1000        100
'10.0.0'            0        735        100
'11.0.0'            0         62        100
'12.0.0'            0         62        100
'12.1.0'            0          1        100
'13.0.0'            0        541        100
'14.0.0'            0         41        100
'15.0.0'           15         15          0
'15.1.0'            5          5          0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 15.0.0, of python string 
``\U0001f6dc`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x9b\x9c|\\n12|\\n"
    🛜|
    12|

python `wcwidth`_ measures width 2,
while *ExtratermQt* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *ExtratermQt* appears to be 
**None**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              22         22              0
'4.0'             100        100              0
'5.0'             100        100              0
'11.0'             73         73              0
'12.0'            100        100              0
'12.1'            100        100              0
'13.0'             51         51              0
'13.1'             83         83              0
'14.0'             20         20              0
'15.0'              1          1              0
'15.1'            100        100              0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *ExtratermQt* measures width 8

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *ExtratermQt* is 0 errors out of 100 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.
.. _mlterm:

mlterm
------

Tested Software version 3.9.0 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for mlterm appears to be 
**9.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'5.1.0'             0         26       100
'5.2.0'            78        269        71.0037
'6.0.0'             0         13       100
'9.0.0'             0       1000       100
'10.0.0'           73        735        90.068
'11.0.0'            6         62        90.3226
'12.0.0'            6         62        90.3226
'12.1.0'            0          1       100
'13.0.0'          100        100         0
'14.0.0'           41         41         0
'15.0.0'           15         15         0
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character 
from Unicode Version 10.0.0, of python string 
``\U0001b00b`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2,
while *mlterm* measures width 0

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *mlterm* appears to be 
**None**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
'2.0'              22         22              0
'4.0'             100        100              0
'5.0'             100        100              0
'11.0'             73         73              0
'12.0'            100        100              0
'12.1'            100        100              0
'13.0'             51         51              0
'13.1'             83         83              0
'14.0'             20         20              0
'15.0'              1          1              0
'15.1'            100        100              0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of an Emoji ZWJ sequence 
from Emoji Version 2.0, of python string 
``\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2,
while *mlterm* measures width 7

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *mlterm* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using printf(1) of Emoji sequence containing *Variation Selector-16*
of python string
``0\ufe0f`` as a utf-8 bytestring, 
trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2,
while *mlterm* measures width 1

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth`: https://www.github.com/jquast/wcwidth/
