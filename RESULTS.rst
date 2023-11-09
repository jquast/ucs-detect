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

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Tabby appears to be 
is 12.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26        100
5.2.0              79        269         70.632
6.0.0               0         13        100
9.0.0               0       1000        100
10.0.0              0        735        100
11.0.0              0         62        100
12.0.0              0         62        100
12.1.0              0          1        100
13.0.0            100        100          0
14.0.0             41         41          0
15.0.0             15         15          0
15.1.0              5          5          0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 13.0.0, python string 
``'\\u31bb'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x37\x35\x33\x33\x33\x31\x36\x32\x36\x32|\\n12|
    ㆻ|
    12|

wcwidth measures width 2,
while Tabby measures width 1

.. _cool-retro-term:

cool-retro-term
---------------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for cool-retro-term appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0              19         26       26.9231
5.2.0             100        109        8.25688
6.0.0               2         13       84.6154
9.0.0              27       1000       97.3
10.0.0            100        100        0
11.0.0             62         62        0
12.0.0             62         62        0
12.1.0              1          1        0
13.0.0            100        100        0
14.0.0             41         41        0
15.0.0             15         15        0
15.1.0              5          5        0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 9.0.0, python string 
``'\\u231a'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x37\x35\x33\x32\x33\x33\x33\x31\x36\x31|\\n12|
    ⌚|
    12|

wcwidth measures width 2,
while cool-retro-term measures width 1

.. _VSCode_Terminal:

VSCode Terminal
---------------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for VSCode Terminal appears to be 
is 12.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26        100
5.2.0              79        269         70.632
6.0.0               0         13        100
9.0.0               0       1000        100
10.0.0              0        735        100
11.0.0              0         62        100
12.0.0              0         62        100
12.1.0              0          1        100
13.0.0            100        100          0
14.0.0             41         41          0
15.0.0             15         15          0
15.1.0              5          5          0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 13.0.0, python string 
``'\\u31bb'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x37\x35\x33\x33\x33\x31\x36\x32\x36\x32|\\n12|
    ㆻ|
    12|

wcwidth measures width 2,
while VSCode Terminal measures width 1

.. _Terminal:

Terminal
--------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Terminal appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              79        269        70.632
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             54        541        90.0185
14.0.0              4         41        90.2439
15.0.0             15         15         0
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 10.0.0, python string 
``'\\U0001b00b'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x30\x33\x30\x36\x32|\\n12|
    𛀋|
    12|

wcwidth measures width 2,
while Terminal measures width 1

.. _XTerm:

XTerm
-----

Wide character support
++++++++++++++++++++++

The best wide unicode table version for XTerm appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0             100        210        52.381
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             54        541        90.0185
14.0.0              4         41        90.2439
15.0.0             15         15         0
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 10.0.0, python string 
``'\\U0001b00b'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x30\x33\x30\x36\x32|\\n12|
    𛀋|
    12|

wcwidth measures width 2,
while XTerm measures width 1

.. _Konsole:

Konsole
-------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Konsole appears to be 
is 15.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              79        269        70.632
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             22        735        97.0068
11.0.0              1         62        98.3871
12.0.0              1         62        98.3871
12.1.0              0          1       100
13.0.0             16        541        97.0425
14.0.0              1         41        97.561
15.0.0              0         15       100
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 15.1.0, python string 
``'\\u2ffc'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x37\x35\x33\x32\x36\x36\x36\x36\x36\x33|\\n12|
    ⿼|
    12|

wcwidth measures width 2,
while Konsole measures width 1

.. _GNOME_Terminal:

GNOME Terminal
--------------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for GNOME Terminal appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              79        269        70.632
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             54        541        90.0185
14.0.0              4         41        90.2439
15.0.0              1         15        93.3333
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 10.0.0, python string 
``'\\U0001b00b'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x30\x33\x30\x36\x32|\\n12|
    𛀋|
    12|

wcwidth measures width 2,
while GNOME Terminal measures width 1

.. _xfce4-terminal:

xfce4-terminal
--------------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for xfce4-terminal appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              79        269        70.632
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             54        541        90.0185
14.0.0              4         41        90.2439
15.0.0              1         15        93.3333
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 10.0.0, python string 
``'\\U0001b00b'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x30\x33\x30\x36\x32|\\n12|
    𛀋|
    12|

wcwidth measures width 2,
while xfce4-terminal measures width 1

.. _st:

st
--

Wide character support
++++++++++++++++++++++

The best wide unicode table version for st appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0             100        210        52.381
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             54        541        90.0185
14.0.0              4         41        90.2439
15.0.0             15         15         0
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 10.0.0, python string 
``'\\U0001b00b'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x30\x33\x30\x36\x32|\\n12|
    𛀋|
    12|

wcwidth measures width 2,
while st measures width 0

.. _Hyper:

Hyper
-----

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Hyper appears to be 
is 12.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26        100
5.2.0              79        269         70.632
6.0.0               0         13        100
9.0.0               0       1000        100
10.0.0              0        735        100
11.0.0              0         62        100
12.0.0              0         62        100
12.1.0              0          1        100
13.0.0            100        100          0
14.0.0             41         41          0
15.0.0             15         15          0
15.1.0              5          5          0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 13.0.0, python string 
``'\\u31bb'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x37\x35\x33\x33\x33\x31\x36\x32\x36\x32|\\n12|
    ㆻ|
    12|

wcwidth measures width 2,
while Hyper measures width 1

.. _Alacritty:

Alacritty
---------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Alacritty appears to be 
is 15.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26        100
5.2.0              79        269         70.632
6.0.0               0         13        100
9.0.0               0       1000        100
10.0.0              0        735        100
11.0.0              0         62        100
12.0.0              0         62        100
12.1.0              0          1        100
13.0.0              0        541        100
14.0.0              0         41        100
15.0.0              0         15        100
15.1.0              5          5          0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 15.1.0, python string 
``'\\u2ffc'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x37\x35\x33\x32\x36\x36\x36\x36\x36\x33|\\n12|
    ⿼|
    12|

wcwidth measures width 2,
while Alacritty measures width 1

.. _iTerm2:

iTerm2
------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for iTerm2 appears to be 
is 12.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              79        269        70.632
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             54        541        90.0185
14.0.0              4         41        90.2439
15.0.0              1         15        93.3333
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 12.0.0, python string 
``'\\U0001b165'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x31\x33\x36\x33\x35|\\n12|
    𛅥|
    12|

wcwidth measures width 2,
while iTerm2 measures width 1

.. _QTerminal:

QTerminal
---------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for QTerminal appears to be 
is 15.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26        100
5.2.0             100        210         52.381
6.0.0               0         13        100
9.0.0               0       1000        100
10.0.0              0        735        100
11.0.0              0         62        100
12.0.0              0         62        100
12.1.0              0          1        100
13.0.0              0        541        100
14.0.0              0         41        100
15.0.0              0         15        100
15.1.0              5          5          0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 15.1.0, python string 
``'\\u2ffc'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x37\x35\x33\x32\x36\x36\x36\x36\x36\x33|\\n12|
    ⿼|
    12|

wcwidth measures width 2,
while QTerminal measures width 1

.. _LXTerminal:

LXTerminal
----------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for LXTerminal appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              79        269        70.632
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             54        541        90.0185
14.0.0              4         41        90.2439
15.0.0              1         15        93.3333
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 10.0.0, python string 
``'\\U0001b00b'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x30\x33\x30\x36\x32|\\n12|
    𛀋|
    12|

wcwidth measures width 2,
while LXTerminal measures width 1

.. _zoc:

zoc
---

Wide character support
++++++++++++++++++++++

The best wide unicode table version for zoc appears to be 
is 14.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              55        269        79.5539
6.0.0              10         13        23.0769
9.0.0              27       1000        97.3
10.0.0              6        735        99.1837
11.0.0              0         62       100
12.0.0             12         62        80.6452
12.1.0              0          1       100
13.0.0              2        541        99.6303
14.0.0              2         41        95.122
15.0.0              1         15        93.3333
15.1.0              4          5        20
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 14.0.0, python string 
``'\\U0001f6dd'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x36\x33\x36\x36\x34\x36\x34|\\n12|
    🛝|
    12|

wcwidth measures width 2,
while zoc measures width 1

.. _kitty:

kitty
-----

Wide character support
++++++++++++++++++++++

The best wide unicode table version for kitty appears to be 
is 15.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              79        269        70.632
6.0.0               1         13        92.3077
9.0.0               0       1000       100
10.0.0             20        735        97.2789
11.0.0              1         62        98.3871
12.0.0              1         62        98.3871
12.1.0              0          1       100
13.0.0             16        541        97.0425
14.0.0              1         41        97.561
15.0.0              0         15       100
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 15.1.0, python string 
``'\\u2ffc'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x37\x35\x33\x32\x36\x36\x36\x36\x36\x33|\\n12|
    ⿼|
    12|

wcwidth measures width 2,
while kitty measures width 1

.. _WezTerm:

WezTerm
-------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for WezTerm appears to be 
is 15.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              79        269        70.632
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             55        541        89.8336
14.0.0              4         41        90.2439
15.0.0              1         15        93.3333
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 15.0.0, python string 
``'\\U0001fabc'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x36\x36\x31\x36\x32\x36\x33|\\n12|
    🪼|
    12|

wcwidth measures width 2,
while WezTerm measures width 0

.. _zutty:

zutty
-----

Wide character support
++++++++++++++++++++++

The best wide unicode table version for zutty appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0             100        210        52.381
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0             54        541        90.0185
14.0.0              4         41        90.2439
15.0.0             15         15         0
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 10.0.0, python string 
``'\\U0001b00b'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x30\x33\x30\x36\x32|\\n12|
    𛀋|
    12|

wcwidth measures width 2,
while zutty measures width 1

.. _ExtratermQt:

ExtratermQt
-----------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for ExtratermQt appears to be 
is 14.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26        100
5.2.0              79        269         70.632
6.0.0               0         13        100
9.0.0               0       1000        100
10.0.0              0        735        100
11.0.0              0         62        100
12.0.0              0         62        100
12.1.0              0          1        100
13.0.0              0        541        100
14.0.0              0         41        100
15.0.0             15         15          0
15.1.0              5          5          0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 15.0.0, python string 
``'\\U0001f6dc'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x36\x33\x36\x36\x34\x36\x33|\\n12|
    🛜|
    12|

wcwidth measures width 2,
while ExtratermQt measures width 1

.. _mlterm:

mlterm
------

Wide character support
++++++++++++++++++++++

The best wide unicode table version for mlterm appears to be 
is 9.0.0, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total    pct_success
=========  ==========  =========  =============
5.1.0               0         26       100
5.2.0              78        269        71.0037
6.0.0               0         13       100
9.0.0               0       1000       100
10.0.0             73        735        90.068
11.0.0              6         62        90.3226
12.0.0              6         62        90.3226
12.1.0              0          1       100
13.0.0            100        100         0
14.0.0             41         41         0
15.0.0             15         15         0
15.1.0              5          5         0
=========  ==========  =========  =============

Example shell test using printf(1) of a WIDE character 
from Unicode Version 10.0.0, python string 
``'\\U0001b00b'`` as a utf-8 bytestring, 
``|`` should align in output::

    $ printf "\x35\x63\x35\x35\x33\x30\x33\x30\x33\x30\x33\x31\x36\x32\x33\x30\x33\x30\x36\x32|\\n12|
    𛀋|
    12|

wcwidth measures width 2,
while mlterm measures width 0

