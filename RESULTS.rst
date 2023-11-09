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
`zoc`_                                 8.07.0              Darwin       C+             B+            14.0.0                  F             F            na                     A+
`cool retro term <cool_retro_term_>`_  1.2.0               Darwin       C              F             9.0.0                   F             C-           11.0                   A-
`QTerminal`_                           1.2.0               Linux        C              A+            15.0.0                  A+            F            2.0                    F
`Alacritty`_                           0.12.3_1            Darwin       D+             A+            15.0.0                  C             F            2.0                    F
`GNOME Terminal <GNOME_Terminal_>`_    3.46.8              Linux        D+             A-            15.0.0                  C             F            2.0                    F
`Tabby`_                               1.0.201             Darwin       D-             C             12.0.0                  C             F            2.0                    F
`VSCode Terminal <VSCode_Terminal_>`_  1.84.0              Darwin       D-             C             12.0.0                  C             F            2.0                    F
`Hyper`_                               4.0.0 canary5       Darwin       D-             C             12.0.0                  C             F            2.0                    F
`mlterm`_                              3.9.0               Linux        D-             F             9.0.0                   B+            F            na                     F
`xfce4-terminal`_                      1.0.4               Linux        F              F             9.0.0                   C             F            2.0                    F
`st`_                                  0.9                 Linux        F              F             9.0.0                   C             F            2.0                    F
`LXTerminal`_                          0.4.0               Linux        F              F             9.0.0                   C             F            2.0                    F
`zutty`_                               0.14                Linux        F              F             9.0.0                   C             F            2.0                    F
`XTerm`_                               379                 Linux        F              F             9.0.0                   C             F            2.0                    F
`Terminal`_                            2.12.7              Darwin       F              F             9.0.0                   C             F            na                     F
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

Common Language support
=======================
All of the following languages were successfull with all terminals emulators tested,
and will be not be reported:

- Armenian
- Chinese, Mandarin (Simplified)
- Chinese, Mandarin (Traditional)
- Cree, Swampy
- English
- Georgian
- Greek (polytonic)
- Hebrew
- Japanese
- Korean

.. _iTerm2:

iTerm2
======

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 12.0.0 of python string ``"\U0001b165"`` (Katakana Letter Small We)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x85\xa5|\\n12|\\n"
    𛅥|
    12|

python `wcwidth`_ measures width 2, while *iTerm2* measures width 1

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
-----------------------------

Emoji VS-16 results for *iTerm2* is 9 errors out of 100 total codepoints tested, 91.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *iTerm2* measures width 1

Language Support
----------------

The following 17 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Chakma                            1000
Vai                               1000
Lao                                472
Sanskrit (Grantha)                1000
Maldivian                         1000
Pular (Adlam)                     1000
Cherokee (cased)                  1000
Russian                           1000
Nuosu                              261
Arabic, Standard                  1000
Tigrigna                          1000
Thai                               370
Mongolian, Halh (Mongolian)         33
Tagalog (Tagalog)                   31
Tamazight, Standard Morocan       1000
Tai Dam                           1000
Assyrian Neo-Aramaic              1000
===========================  =========

The following 14 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Javanese (Javanese)        101
Tamil                      105
Kannada                    109
Khmer, Central             114
Burmese                    115
Malayalam                  115
Bengali                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    182
Tibetan, Central           292
===================  =========

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *iTerm2* measures width 73

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *iTerm2* measures width 4

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *iTerm2* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *iTerm2* measures width 25

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *iTerm2* measures width 11

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *iTerm2* measures width 21

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *iTerm2* measures width 12

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *iTerm2* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *iTerm2* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *iTerm2* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *iTerm2* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *iTerm2* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *iTerm2* measures width 4

Tibetan, Central
----------------

Example shell test using `printf(1)`_ of language, Tibetan, Central of python string ``"\u0f7c\u0f66\u0f0b\u0f54\u0f60\u0f72\u0f0b\u0f50\u0f7c\u0f56\u0f0b\u0f51\u0f56\u0f44\u0f0b\u0f61\u0f7c\u0f51\u0f0d"`` (Tibetan Vowel Sign O, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Pa, Tibetan Letter -A, Tibetan Vowel Sign I, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Vowel Sign O, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Da, Tibetan Letter Ba, Tibetan Letter Nga, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ya, Tibetan Vowel Sign O, Tibetan Letter Da, Tibetan Mark Shad)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xbd\xbc\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x96\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x91\xe0\xbc\x8d|\\n123456789012345|\\n"
    ོས་པའི་ཐོབ་དབང་ཡོད།|
    123456789012345|

python `wcwidth`_ measures width 15, while *iTerm2* measures width 16

.. _kitty:

kitty
=====

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 15.1.0 of python string ``"\u2ffc"`` (na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\xbf\xbc|\\n12|\\n"
    ⿼|
    12|

python `wcwidth`_ measures width 2, while *kitty* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *kitty* measures width 6

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *kitty* is 0 errors out of 100 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.
Language Support
----------------

The following 28 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Tamazight, Standard Morocan       1000
Tai Dam                           1000
Pular (Adlam)                     1000
Tamil                             1000
Arabic, Standard                  1000
Lao                                487
Telugu                            1000
Cherokee (cased)                  1000
Burmese                           1000
Vai                               1000
Khmer, Central                     560
Gujarati                          1000
Javanese (Javanese)                288
Sanskrit (Grantha)                1000
Tigrigna                          1000
Khün                               474
Kannada                           1000
Hindi                             1000
Maldivian                         1000
Chakma                            1000
Tagalog (Tagalog)                   31
Panjabi, Eastern                  1000
Thai                               373
Assyrian Neo-Aramaic              1000
Russian                           1000
Tibetan, Central                   312
Nuosu                              262
Mongolian, Halh (Mongolian)         33
===========================  =========

The following 3 languages are not supported or only partially supported:

=========  =========
lang         n_total
=========  =========
Malayalam        792
Sinhala         1057
Bengali         1002
=========  =========

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d38\u0d30\u0d4d\u200d\u0d35\u0d4d\u0d35\u0d24\u0d4b\u0d28\u0d4d\u0d2e\u0d41\u0d16\u0d2e\u0d3e\u0d2f"`` (Malayalam Letter Sa, Malayalam Letter Ra, Malayalam Sign Virama, Zero Width Joiner, Malayalam Letter Va, Malayalam Sign Virama, Malayalam Letter Va, Malayalam Letter Ta, Malayalam Vowel Sign Oo, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Ma, Malayalam Vowel Sign U, Malayalam Letter Kha, Malayalam Letter Ma, Malayalam Vowel Sign Aa, Malayalam Letter Ya)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xb8\xe0\xb4\xb0\xe0\xb5\x8d\xe2\x80\x8d\xe0\xb4\xb5\xe0\xb5\x8d\xe0\xb4\xb5\xe0\xb4\xa4\xe0\xb5\x8b\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xae\xe0\xb5\x81\xe0\xb4\x96\xe0\xb4\xae\xe0\xb4\xbe\xe0\xb4\xaf|\\n123456789|\\n"
    സര്‍വ്വതോന്മുഖമായ|
    123456789|

python `wcwidth`_ measures width 9, while *kitty* measures width 10

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db4\u0dca\u200d\u0dbb\u0d9a\u0dcf\u0dc1\u0db1\u0dba"`` (Sinhala Letter Alpapraana Payanna, Sinhala Sign Al-Lakuna, Zero Width Joiner, Sinhala Letter Rayanna, Sinhala Letter Alpapraana Kayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Taaluja Sayanna, Sinhala Letter Dantaja Nayanna, Sinhala Letter Yayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb4\xe0\xb7\x8a\xe2\x80\x8d\xe0\xb6\xbb\xe0\xb6\x9a\xe0\xb7\x8f\xe0\xb7\x81\xe0\xb6\xb1\xe0\xb6\xba|\\n12345|\\n"
    ප්‍රකාශනය|
    12345|

python `wcwidth`_ measures width 5, while *kitty* measures width 6

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u0989\u09a4\u09cd\u200d\u09aa\u09c0\u09a1\u09bc\u09a8\u09c7\u09b0"`` (Bengali Letter U, Bengali Letter Ta, Bengali Sign Virama, Zero Width Joiner, Bengali Letter Pa, Bengali Vowel Sign Ii, Bengali Letter Dda, Bengali Sign Nukta, Bengali Letter Na, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\x89\xe0\xa6\xa4\xe0\xa7\x8d\xe2\x80\x8d\xe0\xa6\xaa\xe0\xa7\x80\xe0\xa6\xa1\xe0\xa6\xbc\xe0\xa6\xa8\xe0\xa7\x87\xe0\xa6\xb0|\\n12345|\\n"
    উত্‍পীড়নের|
    12345|

python `wcwidth`_ measures width 5, while *kitty* measures width 6

.. _Konsole:

Konsole
=======

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 15.1.0 of python string ``"\u2ffc"`` (na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\xbf\xbc|\\n12|\\n"
    ⿼|
    12|

python `wcwidth`_ measures width 2, while *Konsole* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 15.1 of python string ``"\u26d3\ufe0f\u200d\U0001f4a5"`` (Chains, Variation Selector-16, Zero Width Joiner, Collision Symbol)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\x9b\x93\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x92\xa5|\\n12|\\n"
    ⛓️‍💥|
    12|

python `wcwidth`_ measures width 2, while *Konsole* measures width 1

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *Konsole* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *Konsole* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Arabic, Standard                  1000
Thai                               373
Cherokee (cased)                  1000
Tai Dam                           1000
Vai                               1000
Tamazight, Standard Morocan       1000
Assyrian Neo-Aramaic              1000
Pular (Adlam)                     1000
Mongolian, Halh (Mongolian)         33
Lao                                487
Tibetan, Central                   312
Nuosu                              262
Maldivian                         1000
Tigrigna                          1000
Tagalog (Tagalog)                   31
Russian                           1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Javanese (Javanese)        106
Sanskrit (Grantha)         107
Kannada                    110
Khmer, Central             114
Malayalam                  115
Bengali                    116
Khün                       123
Burmese                    133
Telugu                     142
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *Konsole* measures width 4

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *Konsole* measures width 71

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *Konsole* measures width 13

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *Konsole* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *Konsole* measures width 25

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *Konsole* measures width 21

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *Konsole* measures width 12

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *Konsole* measures width 15

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *Konsole* measures width 11

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *Konsole* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *Konsole* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *Konsole* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *Konsole* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *Konsole* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *Konsole* measures width 8

.. _WezTerm:

WezTerm
=======

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 15.0.0 of python string ``"\U0001fabc"`` (Jellyfish)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\xaa\xbc|\\n12|\\n"
    🪼|
    12|

python `wcwidth`_ measures width 2, while *WezTerm* measures width 0

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
-----------------------------

Emoji VS-16 results for *WezTerm* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *WezTerm* measures width 1

Language Support
----------------

The following 12 languages were tested with 100% success:

====================  =========
lang                    n_total
====================  =========
Javanese (Javanese)         284
Lao                         472
Khmer, Central              560
Burmese                    1000
Gujarati                   1000
Assyrian Neo-Aramaic       1000
Khün                        474
Chakma                     1000
Kannada                    1000
Cherokee (cased)           1000
Hindi                      1000
Arabic, Standard           1000
====================  =========

The following 19 languages are not supported or only partially supported:

===========================  =========
lang                           n_total
===========================  =========
Thai                               101
Nuosu                              102
Tibetan, Central                   103
Russian                            103
Telugu                             107
Sanskrit (Grantha)                 108
Tagalog (Tagalog)                   31
Pular (Adlam)                      112
Maldivian                          112
Tamil                              114
Tamazight, Standard Morocan        115
Mongolian, Halh (Mongolian)         33
Panjabi, Eastern                   118
Tigrigna                           120
Sinhala                            121
Vai                                143
Tai Dam                            143
Malayalam                          203
Bengali                           1002
===========================  =========

Thai
----

Example shell test using `printf(1)`_ of language, Thai of python string ``"\u0e1b\u0e0f\u0e34\u0e0d\u0e0d\u0e32\u0e2a\u0e32\u0e01\u0e25\u0e27\u0e48\u0e32\u0e14\u0e49\u0e27\u0e22\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e21\u0e19\u0e38\u0e29\u0e22\u0e0a\u0e19"`` (Thai Character Po Pla, Thai Character To Patak, Thai Character Sara I, Thai Character Yo Ying, Thai Character Yo Ying, Thai Character Sara Aa, Thai Character So Sua, Thai Character Sara Aa, Thai Character Ko Kai, Thai Character Lo Ling, Thai Character Wo Waen, Thai Character Mai Ek, Thai Character Sara Aa, Thai Character Do Dek, Thai Character Mai Tho, Thai Character Wo Waen, Thai Character Yo Yak, Thai Character So Sua, Thai Character Sara I, Thai Character Tho Thahan, Thai Character Tho Thong, Thai Character Sara I, Thai Character Mo Ma, Thai Character No Nu, Thai Character Sara U, Thai Character So Rusi, Thai Character Yo Yak, Thai Character Cho Chang, Thai Character No Nu)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xa5\xe0\xb8\xa7\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\xa1\xe0\xb8\x99\xe0\xb8\xb8\xe0\xb8\xa9\xe0\xb8\xa2\xe0\xb8\x8a\xe0\xb8\x99|\\n12345678901234567890123|\\n"
    ปฏิญญาสากลว่าด้วยสิทธิมนุษยชน|
    12345678901234567890123|

python `wcwidth`_ measures width 23, while *WezTerm* measures width 79

Nuosu
-----

Example shell test using `printf(1)`_ of language, Nuosu of python string ``"\u300a\ua2e7\ua0c5\ua2bd\ua305\ua14d\ua11c\ua2ca\ua12f\ua489\u300b"`` (Left Double Angle Bracket, Yi Syllable Zzyt, Yi Syllable Mu, Yi Syllable Cot, Yi Syllable Nzy, Yi Syllable Ddu, Yi Syllable Ti, Yi Syllable Cyt, Yi Syllable Tep, Yi Syllable Yy, Right Double Angle Bracket)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe3\x80\x8a\xea\x8b\xa7\xea\x83\x85\xea\x8a\xbd\xea\x8c\x85\xea\x85\x8d\xea\x84\x9c\xea\x8b\x8a\xea\x84\xaf\xea\x92\x89\xe3\x80\x8b|\\n1234567890123456789012|\\n"
    《ꋧꃅꊽꌅꅍꄜꋊꄯꒉ》|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *WezTerm* measures width 49

Tibetan, Central
----------------

Example shell test using `printf(1)`_ of language, Tibetan, Central of python string ``"\u0f04\u0f05\u0f0e"`` (Tibetan Mark Initial Yig Mgo Mdun Ma, Tibetan Mark Closing Yig Mgo Sgab Ma, Tibetan Mark Nyis Shad)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xbc\x84\xe0\xbc\x85\xe0\xbc\x8e|\\n123|\\n"
    ༄༅༎|
    123|

python `wcwidth`_ measures width 3, while *WezTerm* measures width 3

Russian
-------

Example shell test using `printf(1)`_ of language, Russian of python string ``"\u0412\u0441\u0435\u043e\u0431\u0449\u0430\u044f"`` (Cyrillic Capital Letter Ve, Cyrillic Small Letter Es, Cyrillic Small Letter Ie, Cyrillic Small Letter O, Cyrillic Small Letter Be, Cyrillic Small Letter Shcha, Cyrillic Small Letter A, Cyrillic Small Letter Ya)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xd0\x92\xd1\x81\xd0\xb5\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb0\xd1\x8f|\\n12345678|\\n"
    Всеобщая|
    12345678|

python `wcwidth`_ measures width 8, while *WezTerm* measures width 66

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *WezTerm* measures width 4

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *WezTerm* measures width 46

Tagalog (Tagalog)
-----------------

Example shell test using `printf(1)`_ of language, Tagalog (Tagalog) of python string ``"\u1700\u1705"`` (Tagalog Letter A, Tagalog Letter Nga)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9c\x80\xe1\x9c\x85|\\n12|\\n"
    ᜀᜅ|
    12|

python `wcwidth`_ measures width 2, while *WezTerm* measures width 69

Pular (Adlam)
-------------

Example shell test using `printf(1)`_ of language, Pular (Adlam) of python string ``"\U0001e907\U0001e900\U0001e910\U0001e918\U0001e90b\U0001e910\U0001e900\U0001e910\U0001e901\U0001e909"`` (Adlam Capital Letter Bhe, Adlam Capital Letter Alif, Adlam Capital Letter Nun, Adlam Capital Letter Ga, Adlam Capital Letter I, Adlam Capital Letter Nun, Adlam Capital Letter Alif, Adlam Capital Letter Nun, Adlam Capital Letter Daali, Adlam Capital Letter E)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9e\xa4\x87\xf0\x9e\xa4\x80\xf0\x9e\xa4\x90\xf0\x9e\xa4\x98\xf0\x9e\xa4\x8b\xf0\x9e\xa4\x90\xf0\x9e\xa4\x80\xf0\x9e\xa4\x90\xf0\x9e\xa4\x81\xf0\x9e\xa4\x89|\\n1234567890|\\n"
    𞤇𞤀𞤐𞤘𞤋𞤐𞤀𞤐𞤁𞤉|
    1234567890|

python `wcwidth`_ measures width 10, while *WezTerm* measures width 2

Maldivian
---------

Example shell test using `printf(1)`_ of language, Maldivian of python string ``"10"`` (Digit One, Digit Zero)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "10|\\n12|\\n"
    10|
    12|

python `wcwidth`_ measures width 2, while *WezTerm* measures width 18

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *WezTerm* measures width 2

Tamazight, Standard Morocan
---------------------------

Example shell test using `printf(1)`_ of language, Tamazight, Standard Morocan of python string ``"\u2d30\u2d4d\u2d56\u2d53"`` (Tifinagh Letter Ya, Tifinagh Letter Yal, Tifinagh Letter Yagh, Tifinagh Letter Yu)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\xb4\xb0\xe2\xb5\x8d\xe2\xb5\x96\xe2\xb5\x93|\\n1234|\\n"
    ⴰⵍⵖⵓ|
    1234|

python `wcwidth`_ measures width 4, while *WezTerm* measures width 6

Mongolian, Halh (Mongolian)
---------------------------

Example shell test using `printf(1)`_ of language, Mongolian, Halh (Mongolian) of python string ``"\u182c\u1826\u182e\u1826\u1828"`` (Mongolian Letter Qa, Mongolian Letter Ue, Mongolian Letter Ma, Mongolian Letter Ue, Mongolian Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa0\xac\xe1\xa0\xa6\xe1\xa0\xae\xe1\xa0\xa6\xe1\xa0\xa8|\\n12345|\\n"
    ᠬᠦᠮᠦᠨ|
    12345|

python `wcwidth`_ measures width 5, while *WezTerm* measures width 8

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *WezTerm* measures width 72

Tigrigna
--------

Example shell test using `printf(1)`_ of language, Tigrigna of python string ``"\u12d3\u1208\u121d\u1208\u12bb\u12ca"`` (Ethiopic Syllable Pharyngeal Aa, Ethiopic Syllable La, Ethiopic Syllable Me, Ethiopic Syllable La, Ethiopic Syllable Kxaa, Ethiopic Syllable Wi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x8b\x93\xe1\x88\x88\xe1\x88\x9d\xe1\x88\x88\xe1\x8a\xbb\xe1\x8b\x8a|\\n123456|\\n"
    ዓለምለኻዊ|
    123456|

python `wcwidth`_ measures width 6, while *WezTerm* measures width 22

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *WezTerm* measures width 15

Vai
---

Example shell test using `printf(1)`_ of language, Vai of python string ``"\ua57a\ua583"`` (Vai Syllable Kpoo, Vai Syllable Loo)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\x95\xba\xea\x96\x83|\\n12|\\n"
    ꕺꖃ|
    12|

python `wcwidth`_ measures width 2, while *WezTerm* measures width 7

Tai Dam
-------

Example shell test using `printf(1)`_ of language, Tai Dam of python string ``"\uaa81\uaaab\uaab1\uaaa3"`` (Tai Viet Letter High Ko, Tai Viet Letter High Vo, Tai Viet Vowel Aa, Tai Viet Letter High Mo)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xaa\x81\xea\xaa\xab\xea\xaa\xb1\xea\xaa\xa3|\\n1234|\\n"
    ꪁꪫꪱꪣ|
    1234|

python `wcwidth`_ measures width 4, while *WezTerm* measures width 32

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d38\u0d30\u0d4d\u200d\u0d35\u0d4d\u0d35\u0d24\u0d4b\u0d28\u0d4d\u0d2e\u0d41\u0d16\u0d2e\u0d3e\u0d2f"`` (Malayalam Letter Sa, Malayalam Letter Ra, Malayalam Sign Virama, Zero Width Joiner, Malayalam Letter Va, Malayalam Sign Virama, Malayalam Letter Va, Malayalam Letter Ta, Malayalam Vowel Sign Oo, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Ma, Malayalam Vowel Sign U, Malayalam Letter Kha, Malayalam Letter Ma, Malayalam Vowel Sign Aa, Malayalam Letter Ya)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xb8\xe0\xb4\xb0\xe0\xb5\x8d\xe2\x80\x8d\xe0\xb4\xb5\xe0\xb5\x8d\xe0\xb4\xb5\xe0\xb4\xa4\xe0\xb5\x8b\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xae\xe0\xb5\x81\xe0\xb4\x96\xe0\xb4\xae\xe0\xb4\xbe\xe0\xb4\xaf|\\n123456789|\\n"
    സര്‍വ്വതോന്മുഖമായ|
    123456789|

python `wcwidth`_ measures width 9, while *WezTerm* measures width 10

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u0989\u09a4\u09cd\u200d\u09aa\u09c0\u09a1\u09bc\u09a8\u09c7\u09b0"`` (Bengali Letter U, Bengali Letter Ta, Bengali Sign Virama, Zero Width Joiner, Bengali Letter Pa, Bengali Vowel Sign Ii, Bengali Letter Dda, Bengali Sign Nukta, Bengali Letter Na, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\x89\xe0\xa6\xa4\xe0\xa7\x8d\xe2\x80\x8d\xe0\xa6\xaa\xe0\xa7\x80\xe0\xa6\xa1\xe0\xa6\xbc\xe0\xa6\xa8\xe0\xa7\x87\xe0\xa6\xb0|\\n12345|\\n"
    উত্‍পীড়নের|
    12345|

python `wcwidth`_ measures width 5, while *WezTerm* measures width 6

.. _ExtratermQt:

ExtratermQt
===========

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 15.0.0 of python string ``"\U0001f6dc"`` (Wireless)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x9b\x9c|\\n12|\\n"
    🛜|
    12|

python `wcwidth`_ measures width 2, while *ExtratermQt* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *ExtratermQt* measures width 8

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *ExtratermQt* is 0 errors out of 100 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.
Language Support
----------------

The following 6 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Tigrigna                          1000
Vai                               1000
Tamazight, Standard Morocan       1000
Cherokee (cased)                  1000
Russian                           1000
Nuosu                              262
===========================  =========

The following 25 languages are not supported or only partially supported:

===========================  =========
lang                           n_total
===========================  =========
Javanese (Javanese)                100
Tamil                              101
Chakma                             102
Kannada                            102
Tibetan, Central                   103
Gujarati                           103
Khün                               104
Malayalam                          105
Burmese                            105
Telugu                             105
Khmer, Central                     107
Sanskrit (Grantha)                 107
Bengali                            108
Maldivian                          113
Sinhala                            116
Hindi                              117
Panjabi, Eastern                   119
Thai                               127
Lao                                145
Tagalog (Tagalog)                   31
Pular (Adlam)                      214
Tai Dam                            247
Mongolian, Halh (Mongolian)         33
Assyrian Neo-Aramaic              1067
Arabic, Standard                  1020
===========================  =========

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *ExtratermQt* measures width 95

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *ExtratermQt* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *ExtratermQt* measures width 13

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *ExtratermQt* measures width 4

Tibetan, Central
----------------

Example shell test using `printf(1)`_ of language, Tibetan, Central of python string ``"\u0f61\u0f7c\u0f44\u0f66\u0f0b\u0f41\u0fb1\u0f56\u0f0b\u0f42\u0f66\u0f63\u0f0b\u0f56\u0f66\u0f92\u0fb2\u0f42\u0f66\u0f0b\u0f60\u0f42\u0fb2\u0f7c\u0f0b\u0f56\u0f0b\u0f58\u0f72\u0f60\u0f72\u0f0b\u0f50\u0f7c\u0f56\u0f0b\u0f50\u0f44\u0f0c\u0f0d"`` (Tibetan Letter Ya, Tibetan Vowel Sign O, Tibetan Letter Nga, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Kha, Tibetan Subjoined Letter Ya, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ga, Tibetan Letter Sa, Tibetan Letter La, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ba, Tibetan Letter Sa, Tibetan Subjoined Letter Ga, Tibetan Subjoined Letter Ra, Tibetan Letter Ga, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter -A, Tibetan Letter Ga, Tibetan Subjoined Letter Ra, Tibetan Vowel Sign O, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ma, Tibetan Vowel Sign I, Tibetan Letter -A, Tibetan Vowel Sign I, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Vowel Sign O, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Letter Nga, Tibetan Mark Delimiter Tsheg Bstar, Tibetan Mark Shad)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x84\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x81\xe0\xbe\xb1\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\xa6\xe0\xbd\xa3\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\xa6\xe0\xbe\x92\xe0\xbe\xb2\xe0\xbd\x82\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x82\xe0\xbe\xb2\xe0\xbd\xbc\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x98\xe0\xbd\xb2\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\x84\xe0\xbc\x8c\xe0\xbc\x8d|\\n1234567890123456789012345678901|\\n"
    ཡོངས་ཁྱབ་གསལ་བསྒྲགས་འགྲོ་བ་མིའི་ཐོབ་ཐང༌།|
    1234567890123456789012345678901|

python `wcwidth`_ measures width 31, while *ExtratermQt* measures width 40

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *ExtratermQt* measures width 4

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *ExtratermQt* measures width 22

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *ExtratermQt* measures width 29

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *ExtratermQt* measures width 16

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *ExtratermQt* measures width 13

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *ExtratermQt* measures width 36

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *ExtratermQt* measures width 14

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *ExtratermQt* measures width 12

Maldivian
---------

Example shell test using `printf(1)`_ of language, Maldivian of python string ``"\u0791\u07a8\u0790\u07ac\u0789\u07b0\u0784\u07a6\u0783"`` (Thaana Letter Daviyani, Thaana Ibifili, Thaana Letter Seenu, Thaana Ebefili, Thaana Letter Meemu, Thaana Sukun, Thaana Letter Baa, Thaana Abafili, Thaana Letter Raa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xde\x91\xde\xa8\xde\x90\xde\xac\xde\x89\xde\xb0\xde\x84\xde\xa6\xde\x83|\\n12345|\\n"
    ޑިސެމްބަރ|
    12345|

python `wcwidth`_ measures width 5, while *ExtratermQt* measures width 9

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *ExtratermQt* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *ExtratermQt* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *ExtratermQt* measures width 6

Thai
----

Example shell test using `printf(1)`_ of language, Thai of python string ``"\u0e1b\u0e0f\u0e34\u0e0d\u0e0d\u0e32\u0e2a\u0e32\u0e01\u0e25\u0e27\u0e48\u0e32\u0e14\u0e49\u0e27\u0e22\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e21\u0e19\u0e38\u0e29\u0e22\u0e0a\u0e19"`` (Thai Character Po Pla, Thai Character To Patak, Thai Character Sara I, Thai Character Yo Ying, Thai Character Yo Ying, Thai Character Sara Aa, Thai Character So Sua, Thai Character Sara Aa, Thai Character Ko Kai, Thai Character Lo Ling, Thai Character Wo Waen, Thai Character Mai Ek, Thai Character Sara Aa, Thai Character Do Dek, Thai Character Mai Tho, Thai Character Wo Waen, Thai Character Yo Yak, Thai Character So Sua, Thai Character Sara I, Thai Character Tho Thahan, Thai Character Tho Thong, Thai Character Sara I, Thai Character Mo Ma, Thai Character No Nu, Thai Character Sara U, Thai Character So Rusi, Thai Character Yo Yak, Thai Character Cho Chang, Thai Character No Nu)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xa5\xe0\xb8\xa7\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\xa1\xe0\xb8\x99\xe0\xb8\xb8\xe0\xb8\xa9\xe0\xb8\xa2\xe0\xb8\x8a\xe0\xb8\x99|\\n12345678901234567890123|\\n"
    ปฏิญญาสากลว่าด้วยสิทธิมนุษยชน|
    12345678901234567890123|

python `wcwidth`_ measures width 23, while *ExtratermQt* measures width 29

Lao
---

Example shell test using `printf(1)`_ of language, Lao of python string ``"\u0e9b\u0eb0\u0e81\u0eb2\u0e94\u0eaa\u0eb2\u0e81\u0ebb\u0e99"`` (Lao Letter Po, Lao Vowel Sign A, Lao Letter Ko, Lao Vowel Sign Aa, Lao Letter Do, Lao Letter So Sung, Lao Vowel Sign Aa, Lao Letter Ko, Lao Vowel Sign Mai Kon, Lao Letter No)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xba\x9b\xe0\xba\xb0\xe0\xba\x81\xe0\xba\xb2\xe0\xba\x94\xe0\xba\xaa\xe0\xba\xb2\xe0\xba\x81\xe0\xba\xbb\xe0\xba\x99|\\n123456789|\\n"
    ປະກາດສາກົນ|
    123456789|

python `wcwidth`_ measures width 9, while *ExtratermQt* measures width 10

Tagalog (Tagalog)
-----------------

Example shell test using `printf(1)`_ of language, Tagalog (Tagalog) of python string ``"\u170e\u1711\u1706\u1714"`` (Tagalog Letter La, Tagalog Letter Ha, Tagalog Letter Ta, Tagalog Sign Virama)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9c\x8e\xe1\x9c\x91\xe1\x9c\x86\xe1\x9c\x94|\\n123|\\n"
    ᜎᜑᜆ᜔|
    123|

python `wcwidth`_ measures width 3, while *ExtratermQt* measures width 4

Pular (Adlam)
-------------

Example shell test using `printf(1)`_ of language, Pular (Adlam) of python string ``"\U0001e916\U0001e90b\U0001e902\U0001e946\U0001e900\U0001e912\U0001e900\U0001e910\U0001e911\U0001e90c\U0001e945\U0001e908\U0001e909"`` (Adlam Capital Letter Ha, Adlam Capital Letter I, Adlam Capital Letter Laam, Adlam Gemination Mark, Adlam Capital Letter Alif, Adlam Capital Letter Ya, Adlam Capital Letter Alif, Adlam Capital Letter Nun, Adlam Capital Letter Kaf, Adlam Capital Letter O, Adlam Vowel Lengthener, Adlam Capital Letter Ra, Adlam Capital Letter E)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9e\xa4\x96\xf0\x9e\xa4\x8b\xf0\x9e\xa4\x82\xf0\x9e\xa5\x86\xf0\x9e\xa4\x80\xf0\x9e\xa4\x92\xf0\x9e\xa4\x80\xf0\x9e\xa4\x90\xf0\x9e\xa4\x91\xf0\x9e\xa4\x8c\xf0\x9e\xa5\x85\xf0\x9e\xa4\x88\xf0\x9e\xa4\x89|\\n12345678901|\\n"
    𞤖𞤋𞤂𞥆𞤀𞤒𞤀𞤐𞤑𞤌𞥅𞤈𞤉|
    12345678901|

python `wcwidth`_ measures width 11, while *ExtratermQt* measures width 13

Tai Dam
-------

Example shell test using `printf(1)`_ of language, Tai Dam of python string ``"\uaab9\uaa95\uaab8\uaa89"`` (Tai Viet Vowel Uea, Tai Viet Letter High To, Tai Viet Vowel Ia, Tai Viet Letter High Ngo)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xaa\xb9\xea\xaa\x95\xea\xaa\xb8\xea\xaa\x89|\\n123|\\n"
    ꪹꪕꪸꪉ|
    123|

python `wcwidth`_ measures width 3, while *ExtratermQt* measures width 4

Mongolian, Halh (Mongolian)
---------------------------

Example shell test using `printf(1)`_ of language, Mongolian, Halh (Mongolian) of python string ``"\u1828\u1821\u1837\u180e\u1821"`` (Mongolian Letter Na, Mongolian Letter E, Mongolian Letter Ra, Mongolian Vowel Separator, Mongolian Letter E)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa0\xa8\xe1\xa0\xa1\xe1\xa0\xb7\xe1\xa0\x8e\xe1\xa0\xa1|\\n1234|\\n"
    ᠨᠡᠷ᠎ᠡ|
    1234|

python `wcwidth`_ measures width 4, while *ExtratermQt* measures width 5

Assyrian Neo-Aramaic
--------------------

Example shell test using `printf(1)`_ of language, Assyrian Neo-Aramaic of python string ``"\u072c\u071d\u0712\u0742\u0720\u071d\u0710"`` (Syriac Letter Taw, Syriac Letter Yudh, Syriac Letter Beth, Syriac Rukkakha, Syriac Letter Lamadh, Syriac Letter Yudh, Syriac Letter Alaph)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xdc\xac\xdc\x9d\xdc\x92\xdd\x82\xdc\xa0\xdc\x9d\xdc\x90|\\n123456|\\n"
    ܬܝܒ݂ܠܝܐ|
    123456|

python `wcwidth`_ measures width 6, while *ExtratermQt* measures width 7

Arabic, Standard
----------------

Example shell test using `printf(1)`_ of language, Arabic, Standard of python string ``"\u0627\u0639\u062a\u064f\u0645\u062f"`` (Arabic Letter Alef, Arabic Letter Ain, Arabic Letter Teh, Arabic Damma, Arabic Letter Meem, Arabic Letter Dal)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xd8\xa7\xd8\xb9\xd8\xaa\xd9\x8f\xd9\x85\xd8\xaf|\\n12345|\\n"
    اعتُمد|
    12345|

python `wcwidth`_ measures width 5, while *ExtratermQt* measures width 6

.. _zoc:

zoc
===

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 14.0.0 of python string ``"\U0001f6dd"`` (Playground Slide)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x9b\x9d|\\n12|\\n"
    🛝|
    12|

python `wcwidth`_ measures width 2, while *zoc* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *zoc* measures width 6

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *zoc* is 0 errors out of 100 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.
Language Support
----------------

The following 4 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Tigrigna                          1000
Tamazight, Standard Morocan       1000
Vai                               1000
Russian                           1000
===========================  =========

The following 27 languages are not supported or only partially supported:

===========================  =========
lang                           n_total
===========================  =========
Cherokee (cased)                   100
Nuosu                              100
Javanese (Javanese)                101
Tamil                              101
Chakma                             102
Kannada                            102
Gujarati                           103
Tibetan, Central                   103
Khün                               104
Malayalam                          105
Telugu                             105
Burmese                            105
Tai Dam                            106
Khmer, Central                     107
Sanskrit (Grantha)                 107
Bengali                            108
Maldivian                          113
Sinhala                            116
Hindi                              117
Panjabi, Eastern                   119
Thai                               127
Lao                                145
Tagalog (Tagalog)                   31
Pular (Adlam)                      214
Mongolian, Halh (Mongolian)         33
Assyrian Neo-Aramaic              1067
Arabic, Standard                  1020
===========================  =========

Cherokee (cased)
----------------

Example shell test using `printf(1)`_ of language, Cherokee (cased) of python string ``"\u13c2\uab7c\uab8e\uabab"`` (Cherokee Letter Ni, Cherokee Small Letter Gv, Cherokee Small Letter Na, Cherokee Small Letter Dv)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x8f\x82\xea\xad\xbc\xea\xae\x8e\xea\xae\xab|\\n1234|\\n"
    Ꮒꭼꮎꮫ|
    1234|

python `wcwidth`_ measures width 4, while *zoc* measures width 7

Nuosu
-----

Example shell test using `printf(1)`_ of language, Nuosu of python string ``"\u300a\ua2e7\ua0c5\ua2bd\ua305\ua14d\ua11c\ua2ca\ua12f\ua489\u300b"`` (Left Double Angle Bracket, Yi Syllable Zzyt, Yi Syllable Mu, Yi Syllable Cot, Yi Syllable Nzy, Yi Syllable Ddu, Yi Syllable Ti, Yi Syllable Cyt, Yi Syllable Tep, Yi Syllable Yy, Right Double Angle Bracket)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe3\x80\x8a\xea\x8b\xa7\xea\x83\x85\xea\x8a\xbd\xea\x8c\x85\xea\x85\x8d\xea\x84\x9c\xea\x8b\x8a\xea\x84\xaf\xea\x92\x89\xe3\x80\x8b|\\n1234567890123456789012|\\n"
    《ꋧꃅꊽꌅꅍꄜꋊꄯꒉ》|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *zoc* measures width 13

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *zoc* measures width 52

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *zoc* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *zoc* measures width 13

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *zoc* measures width 4

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *zoc* measures width 4

Tibetan, Central
----------------

Example shell test using `printf(1)`_ of language, Tibetan, Central of python string ``"\u0f61\u0f7c\u0f44\u0f66\u0f0b\u0f41\u0fb1\u0f56\u0f0b\u0f42\u0f66\u0f63\u0f0b\u0f56\u0f66\u0f92\u0fb2\u0f42\u0f66\u0f0b\u0f60\u0f42\u0fb2\u0f7c\u0f0b\u0f56\u0f0b\u0f58\u0f72\u0f60\u0f72\u0f0b\u0f50\u0f7c\u0f56\u0f0b\u0f50\u0f44\u0f0c\u0f0d"`` (Tibetan Letter Ya, Tibetan Vowel Sign O, Tibetan Letter Nga, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Kha, Tibetan Subjoined Letter Ya, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ga, Tibetan Letter Sa, Tibetan Letter La, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ba, Tibetan Letter Sa, Tibetan Subjoined Letter Ga, Tibetan Subjoined Letter Ra, Tibetan Letter Ga, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter -A, Tibetan Letter Ga, Tibetan Subjoined Letter Ra, Tibetan Vowel Sign O, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ma, Tibetan Vowel Sign I, Tibetan Letter -A, Tibetan Vowel Sign I, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Vowel Sign O, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Letter Nga, Tibetan Mark Delimiter Tsheg Bstar, Tibetan Mark Shad)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x84\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x81\xe0\xbe\xb1\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\xa6\xe0\xbd\xa3\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\xa6\xe0\xbe\x92\xe0\xbe\xb2\xe0\xbd\x82\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x82\xe0\xbe\xb2\xe0\xbd\xbc\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x98\xe0\xbd\xb2\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\x84\xe0\xbc\x8c\xe0\xbc\x8d|\\n1234567890123456789012345678901|\\n"
    ཡོངས་ཁྱབ་གསལ་བསྒྲགས་འགྲོ་བ་མིའི་ཐོབ་ཐང༌།|
    1234567890123456789012345678901|

python `wcwidth`_ measures width 31, while *zoc* measures width 40

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *zoc* measures width 22

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *zoc* measures width 29

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *zoc* measures width 13

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *zoc* measures width 16

Tai Dam
-------

Example shell test using `printf(1)`_ of language, Tai Dam of python string ``"\uaa81\uaaab\uaab1\uaaa3"`` (Tai Viet Letter High Ko, Tai Viet Letter High Vo, Tai Viet Vowel Aa, Tai Viet Letter High Mo)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xaa\x81\xea\xaa\xab\xea\xaa\xb1\xea\xaa\xa3|\\n1234|\\n"
    ꪁꪫꪱꪣ|
    1234|

python `wcwidth`_ measures width 4, while *zoc* measures width 8

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *zoc* measures width 36

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *zoc* measures width 14

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *zoc* measures width 12

Maldivian
---------

Example shell test using `printf(1)`_ of language, Maldivian of python string ``"\u0791\u07a8\u0790\u07ac\u0789\u07b0\u0784\u07a6\u0783"`` (Thaana Letter Daviyani, Thaana Ibifili, Thaana Letter Seenu, Thaana Ebefili, Thaana Letter Meemu, Thaana Sukun, Thaana Letter Baa, Thaana Abafili, Thaana Letter Raa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xde\x91\xde\xa8\xde\x90\xde\xac\xde\x89\xde\xb0\xde\x84\xde\xa6\xde\x83|\\n12345|\\n"
    ޑިސެމްބަރ|
    12345|

python `wcwidth`_ measures width 5, while *zoc* measures width 9

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *zoc* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *zoc* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *zoc* measures width 6

Thai
----

Example shell test using `printf(1)`_ of language, Thai of python string ``"\u0e1b\u0e0f\u0e34\u0e0d\u0e0d\u0e32\u0e2a\u0e32\u0e01\u0e25\u0e27\u0e48\u0e32\u0e14\u0e49\u0e27\u0e22\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e21\u0e19\u0e38\u0e29\u0e22\u0e0a\u0e19"`` (Thai Character Po Pla, Thai Character To Patak, Thai Character Sara I, Thai Character Yo Ying, Thai Character Yo Ying, Thai Character Sara Aa, Thai Character So Sua, Thai Character Sara Aa, Thai Character Ko Kai, Thai Character Lo Ling, Thai Character Wo Waen, Thai Character Mai Ek, Thai Character Sara Aa, Thai Character Do Dek, Thai Character Mai Tho, Thai Character Wo Waen, Thai Character Yo Yak, Thai Character So Sua, Thai Character Sara I, Thai Character Tho Thahan, Thai Character Tho Thong, Thai Character Sara I, Thai Character Mo Ma, Thai Character No Nu, Thai Character Sara U, Thai Character So Rusi, Thai Character Yo Yak, Thai Character Cho Chang, Thai Character No Nu)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xa5\xe0\xb8\xa7\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\xa1\xe0\xb8\x99\xe0\xb8\xb8\xe0\xb8\xa9\xe0\xb8\xa2\xe0\xb8\x8a\xe0\xb8\x99|\\n12345678901234567890123|\\n"
    ปฏิญญาสากลว่าด้วยสิทธิมนุษยชน|
    12345678901234567890123|

python `wcwidth`_ measures width 23, while *zoc* measures width 29

Lao
---

Example shell test using `printf(1)`_ of language, Lao of python string ``"\u0e9b\u0eb0\u0e81\u0eb2\u0e94\u0eaa\u0eb2\u0e81\u0ebb\u0e99"`` (Lao Letter Po, Lao Vowel Sign A, Lao Letter Ko, Lao Vowel Sign Aa, Lao Letter Do, Lao Letter So Sung, Lao Vowel Sign Aa, Lao Letter Ko, Lao Vowel Sign Mai Kon, Lao Letter No)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xba\x9b\xe0\xba\xb0\xe0\xba\x81\xe0\xba\xb2\xe0\xba\x94\xe0\xba\xaa\xe0\xba\xb2\xe0\xba\x81\xe0\xba\xbb\xe0\xba\x99|\\n123456789|\\n"
    ປະກາດສາກົນ|
    123456789|

python `wcwidth`_ measures width 9, while *zoc* measures width 10

Tagalog (Tagalog)
-----------------

Example shell test using `printf(1)`_ of language, Tagalog (Tagalog) of python string ``"\u170e\u1711\u1706\u1714"`` (Tagalog Letter La, Tagalog Letter Ha, Tagalog Letter Ta, Tagalog Sign Virama)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9c\x8e\xe1\x9c\x91\xe1\x9c\x86\xe1\x9c\x94|\\n123|\\n"
    ᜎᜑᜆ᜔|
    123|

python `wcwidth`_ measures width 3, while *zoc* measures width 4

Pular (Adlam)
-------------

Example shell test using `printf(1)`_ of language, Pular (Adlam) of python string ``"\U0001e916\U0001e90b\U0001e902\U0001e946\U0001e900\U0001e912\U0001e900\U0001e910\U0001e911\U0001e90c\U0001e945\U0001e908\U0001e909"`` (Adlam Capital Letter Ha, Adlam Capital Letter I, Adlam Capital Letter Laam, Adlam Gemination Mark, Adlam Capital Letter Alif, Adlam Capital Letter Ya, Adlam Capital Letter Alif, Adlam Capital Letter Nun, Adlam Capital Letter Kaf, Adlam Capital Letter O, Adlam Vowel Lengthener, Adlam Capital Letter Ra, Adlam Capital Letter E)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9e\xa4\x96\xf0\x9e\xa4\x8b\xf0\x9e\xa4\x82\xf0\x9e\xa5\x86\xf0\x9e\xa4\x80\xf0\x9e\xa4\x92\xf0\x9e\xa4\x80\xf0\x9e\xa4\x90\xf0\x9e\xa4\x91\xf0\x9e\xa4\x8c\xf0\x9e\xa5\x85\xf0\x9e\xa4\x88\xf0\x9e\xa4\x89|\\n12345678901|\\n"
    𞤖𞤋𞤂𞥆𞤀𞤒𞤀𞤐𞤑𞤌𞥅𞤈𞤉|
    12345678901|

python `wcwidth`_ measures width 11, while *zoc* measures width 13

Mongolian, Halh (Mongolian)
---------------------------

Example shell test using `printf(1)`_ of language, Mongolian, Halh (Mongolian) of python string ``"\u1828\u1821\u1837\u180e\u1821"`` (Mongolian Letter Na, Mongolian Letter E, Mongolian Letter Ra, Mongolian Vowel Separator, Mongolian Letter E)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa0\xa8\xe1\xa0\xa1\xe1\xa0\xb7\xe1\xa0\x8e\xe1\xa0\xa1|\\n1234|\\n"
    ᠨᠡᠷ᠎ᠡ|
    1234|

python `wcwidth`_ measures width 4, while *zoc* measures width 5

Assyrian Neo-Aramaic
--------------------

Example shell test using `printf(1)`_ of language, Assyrian Neo-Aramaic of python string ``"\u072c\u071d\u0712\u0742\u0720\u071d\u0710"`` (Syriac Letter Taw, Syriac Letter Yudh, Syriac Letter Beth, Syriac Rukkakha, Syriac Letter Lamadh, Syriac Letter Yudh, Syriac Letter Alaph)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xdc\xac\xdc\x9d\xdc\x92\xdd\x82\xdc\xa0\xdc\x9d\xdc\x90|\\n123456|\\n"
    ܬܝܒ݂ܠܝܐ|
    123456|

python `wcwidth`_ measures width 6, while *zoc* measures width 7

Arabic, Standard
----------------

Example shell test using `printf(1)`_ of language, Arabic, Standard of python string ``"\u0627\u0639\u062a\u064f\u0645\u062f"`` (Arabic Letter Alef, Arabic Letter Ain, Arabic Letter Teh, Arabic Damma, Arabic Letter Meem, Arabic Letter Dal)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xd8\xa7\xd8\xb9\xd8\xaa\xd9\x8f\xd9\x85\xd8\xaf|\\n12345|\\n"
    اعتُمد|
    12345|

python `wcwidth`_ measures width 5, while *zoc* measures width 6

.. _cool_retro_term:

cool retro term
===============

Tested Software version 1.2.0 on Darwin

Wide character support
++++++++++++++++++++++

The best wide unicode table version for cool retro term appears to be 
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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 9.0.0 of python string ``"\u231a"`` (Watch)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\x8c\x9a|\\n12|\\n"
    ⌚|
    12|

python `wcwidth`_ measures width 2, while *cool retro term* measures width 1

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *cool retro term* appears to be 
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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 11.0 of python string ``"\U0001f3f4\u200d\u2620\ufe0f"`` (Waving Black Flag, Zero Width Joiner, Skull And Crossbones, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x8f\xb4\xe2\x80\x8d\xe2\x98\xa0\xef\xb8\x8f|\\n12|\\n"
    🏴‍☠️|
    12|

python `wcwidth`_ measures width 2, while *cool retro term* measures width 4

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *cool retro term* is 12 errors out of 100 total codepoints tested, 88.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"\u2694\ufe0f"`` (Crossed Swords, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\x9a\x94\xef\xb8\x8f|\\n12|\\n"
    ⚔️|
    12|

python `wcwidth`_ measures width 2, while *cool retro term* measures width 1

Language Support
----------------

The following 5 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Nuosu                              262
Mongolian, Halh (Mongolian)         33
Tigrigna                          1000
Thai                               372
Russian                           1000
===========================  =========

The following 26 languages are not supported or only partially supported:

===========================  =========
lang                           n_total
===========================  =========
Vai                                100
Javanese (Javanese)                100
Cherokee (cased)                   100
Kannada                            102
Gujarati                           103
Khün                               104
Malayalam                          105
Telugu                             105
Tamil                              105
Tai Dam                            106
Tibetan, Central                   106
Burmese                            106
Khmer, Central                     107
Bengali                            108
Sanskrit (Grantha)                 113
Maldivian                          113
Chakma                             115
Sinhala                            116
Tamazight, Standard Morocan        117
Hindi                              117
Panjabi, Eastern                   119
Tagalog (Tagalog)                   31
Lao                                149
Assyrian Neo-Aramaic              1048
Arabic, Standard                  1020
Pular (Adlam)                     1003
===========================  =========

Vai
---

Example shell test using `printf(1)`_ of language, Vai of python string ``"\ua57a\ua583"`` (Vai Syllable Kpoo, Vai Syllable Loo)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\x95\xba\xea\x96\x83|\\n12|\\n"
    ꕺꖃ|
    12|

python `wcwidth`_ measures width 2, while *cool retro term* measures width 0

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *cool retro term* measures width 0

Cherokee (cased)
----------------

Example shell test using `printf(1)`_ of language, Cherokee (cased) of python string ``"\u13c2\uab7c\uab8e\uabab"`` (Cherokee Letter Ni, Cherokee Small Letter Gv, Cherokee Small Letter Na, Cherokee Small Letter Dv)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x8f\x82\xea\xad\xbc\xea\xae\x8e\xea\xae\xab|\\n1234|\\n"
    Ꮒꭼꮎꮫ|
    1234|

python `wcwidth`_ measures width 4, while *cool retro term* measures width 1

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *cool retro term* measures width 4

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *cool retro term* measures width 4

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *cool retro term* measures width 0

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *cool retro term* measures width 29

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *cool retro term* measures width 13

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *cool retro term* measures width 4

Tai Dam
-------

Example shell test using `printf(1)`_ of language, Tai Dam of python string ``"\uaa81\uaaab\uaab1\uaaa3"`` (Tai Viet Letter High Ko, Tai Viet Letter High Vo, Tai Viet Vowel Aa, Tai Viet Letter High Mo)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xaa\x81\xea\xaa\xab\xea\xaa\xb1\xea\xaa\xa3|\\n1234|\\n"
    ꪁꪫꪱꪣ|
    1234|

python `wcwidth`_ measures width 4, while *cool retro term* measures width 0

Tibetan, Central
----------------

Example shell test using `printf(1)`_ of language, Tibetan, Central of python string ``"\u0f61\u0f7c\u0f44\u0f66\u0f0b\u0f41\u0fb1\u0f56\u0f0b\u0f42\u0f66\u0f63\u0f0b\u0f56\u0f66\u0f92\u0fb2\u0f42\u0f66\u0f0b\u0f60\u0f42\u0fb2\u0f7c\u0f0b\u0f56\u0f0b\u0f58\u0f72\u0f60\u0f72\u0f0b\u0f50\u0f7c\u0f56\u0f0b\u0f50\u0f44\u0f0c\u0f0d"`` (Tibetan Letter Ya, Tibetan Vowel Sign O, Tibetan Letter Nga, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Kha, Tibetan Subjoined Letter Ya, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ga, Tibetan Letter Sa, Tibetan Letter La, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ba, Tibetan Letter Sa, Tibetan Subjoined Letter Ga, Tibetan Subjoined Letter Ra, Tibetan Letter Ga, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter -A, Tibetan Letter Ga, Tibetan Subjoined Letter Ra, Tibetan Vowel Sign O, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ma, Tibetan Vowel Sign I, Tibetan Letter -A, Tibetan Vowel Sign I, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Vowel Sign O, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Letter Nga, Tibetan Mark Delimiter Tsheg Bstar, Tibetan Mark Shad)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x84\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x81\xe0\xbe\xb1\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\xa6\xe0\xbd\xa3\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\xa6\xe0\xbe\x92\xe0\xbe\xb2\xe0\xbd\x82\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x82\xe0\xbe\xb2\xe0\xbd\xbc\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x98\xe0\xbd\xb2\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\x84\xe0\xbc\x8c\xe0\xbc\x8d|\\n1234567890123456789012345678901|\\n"
    ཡོངས་ཁྱབ་གསལ་བསྒྲགས་འགྲོ་བ་མིའི་ཐོབ་ཐང༌།|
    1234567890123456789012345678901|

python `wcwidth`_ measures width 31, while *cool retro term* measures width 40

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *cool retro term* measures width 11

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *cool retro term* measures width 36

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *cool retro term* measures width 12

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *cool retro term* measures width 14

Maldivian
---------

Example shell test using `printf(1)`_ of language, Maldivian of python string ``"\u0791\u07a8\u0790\u07ac\u0789\u07b0\u0784\u07a6\u0783"`` (Thaana Letter Daviyani, Thaana Ibifili, Thaana Letter Seenu, Thaana Ebefili, Thaana Letter Meemu, Thaana Sukun, Thaana Letter Baa, Thaana Abafili, Thaana Letter Raa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xde\x91\xde\xa8\xde\x90\xde\xac\xde\x89\xde\xb0\xde\x84\xde\xa6\xde\x83|\\n12345|\\n"
    ޑިސެމްބަރ|
    12345|

python `wcwidth`_ measures width 5, while *cool retro term* measures width 9

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *cool retro term* measures width 10

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *cool retro term* measures width 4

Tamazight, Standard Morocan
---------------------------

Example shell test using `printf(1)`_ of language, Tamazight, Standard Morocan of python string ``"\u2d30\u2d4d\u2d56\u2d53"`` (Tifinagh Letter Ya, Tifinagh Letter Yal, Tifinagh Letter Yagh, Tifinagh Letter Yu)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\xb4\xb0\xe2\xb5\x8d\xe2\xb5\x96\xe2\xb5\x93|\\n1234|\\n"
    ⴰⵍⵖⵓ|
    1234|

python `wcwidth`_ measures width 4, while *cool retro term* measures width 0

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *cool retro term* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *cool retro term* measures width 6

Tagalog (Tagalog)
-----------------

Example shell test using `printf(1)`_ of language, Tagalog (Tagalog) of python string ``"\u170e\u1711\u1706\u1714"`` (Tagalog Letter La, Tagalog Letter Ha, Tagalog Letter Ta, Tagalog Sign Virama)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9c\x8e\xe1\x9c\x91\xe1\x9c\x86\xe1\x9c\x94|\\n123|\\n"
    ᜎᜑᜆ᜔|
    123|

python `wcwidth`_ measures width 3, while *cool retro term* measures width 4

Lao
---

Example shell test using `printf(1)`_ of language, Lao of python string ``"\u0e9b\u0eb0\u0e81\u0eb2\u0e94\u0eaa\u0eb2\u0e81\u0ebb\u0e99"`` (Lao Letter Po, Lao Vowel Sign A, Lao Letter Ko, Lao Vowel Sign Aa, Lao Letter Do, Lao Letter So Sung, Lao Vowel Sign Aa, Lao Letter Ko, Lao Vowel Sign Mai Kon, Lao Letter No)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xba\x9b\xe0\xba\xb0\xe0\xba\x81\xe0\xba\xb2\xe0\xba\x94\xe0\xba\xaa\xe0\xba\xb2\xe0\xba\x81\xe0\xba\xbb\xe0\xba\x99|\\n123456789|\\n"
    ປະກາດສາກົນ|
    123456789|

python `wcwidth`_ measures width 9, while *cool retro term* measures width 10

Assyrian Neo-Aramaic
--------------------

Example shell test using `printf(1)`_ of language, Assyrian Neo-Aramaic of python string ``"\u072c\u071d\u0712\u0742\u0720\u071d\u0710"`` (Syriac Letter Taw, Syriac Letter Yudh, Syriac Letter Beth, Syriac Rukkakha, Syriac Letter Lamadh, Syriac Letter Yudh, Syriac Letter Alaph)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xdc\xac\xdc\x9d\xdc\x92\xdd\x82\xdc\xa0\xdc\x9d\xdc\x90|\\n123456|\\n"
    ܬܝܒ݂ܠܝܐ|
    123456|

python `wcwidth`_ measures width 6, while *cool retro term* measures width 7

Arabic, Standard
----------------

Example shell test using `printf(1)`_ of language, Arabic, Standard of python string ``"\u0627\u0639\u062a\u064f\u0645\u062f"`` (Arabic Letter Alef, Arabic Letter Ain, Arabic Letter Teh, Arabic Damma, Arabic Letter Meem, Arabic Letter Dal)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xd8\xa7\xd8\xb9\xd8\xaa\xd9\x8f\xd9\x85\xd8\xaf|\\n12345|\\n"
    اعتُمد|
    12345|

python `wcwidth`_ measures width 5, while *cool retro term* measures width 6

Pular (Adlam)
-------------

Example shell test using `printf(1)`_ of language, Pular (Adlam) of python string ``"\U0001e932\u2019\U0001e923\U0001e935\U0001e932\u2e41"`` (Adlam Small Letter Nun, Right Single Quotation Mark, Adlam Small Letter Daali, Adlam Small Letter U, Adlam Small Letter Nun, Reversed Comma)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9e\xa4\xb2\xe2\x80\x99\xf0\x9e\xa4\xa3\xf0\x9e\xa4\xb5\xf0\x9e\xa4\xb2\xe2\xb9\x81|\\n123456|\\n"
    𞤲’𞤣𞤵𞤲⹁|
    123456|

python `wcwidth`_ measures width 6, while *cool retro term* measures width 5

.. _QTerminal:

QTerminal
=========

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 15.1.0 of python string ``"\u2ffc"`` (na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\xbf\xbc|\\n12|\\n"
    ⿼|
    12|

python `wcwidth`_ measures width 2, while *QTerminal* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *QTerminal* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *QTerminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *QTerminal* measures width 1

Language Support
----------------

The following 28 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Telugu                            1000
Russian                           1000
Khmer, Central                     560
Mongolian, Halh (Mongolian)         33
Tigrigna                          1000
Tamil                             1000
Gujarati                          1000
Javanese (Javanese)                287
Nuosu                              262
Panjabi, Eastern                  1000
Tibetan, Central                   307
Tagalog (Tagalog)                   31
Lao                                479
Burmese                           1000
Tai Dam                           1000
Vai                               1000
Assyrian Neo-Aramaic              1000
Cherokee (cased)                  1000
Arabic, Standard                  1000
Hindi                             1000
Tamazight, Standard Morocan       1000
Maldivian                         1000
Pular (Adlam)                     1000
Kannada                           1000
Thai                               372
Chakma                            1000
Sanskrit (Grantha)                1000
Khün                               474
===========================  =========

The following 3 languages are not supported or only partially supported:

=========  =========
lang         n_total
=========  =========
Malayalam        792
Sinhala         1057
Bengali         1002
=========  =========

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d38\u0d30\u0d4d\u200d\u0d35\u0d4d\u0d35\u0d24\u0d4b\u0d28\u0d4d\u0d2e\u0d41\u0d16\u0d2e\u0d3e\u0d2f"`` (Malayalam Letter Sa, Malayalam Letter Ra, Malayalam Sign Virama, Zero Width Joiner, Malayalam Letter Va, Malayalam Sign Virama, Malayalam Letter Va, Malayalam Letter Ta, Malayalam Vowel Sign Oo, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Ma, Malayalam Vowel Sign U, Malayalam Letter Kha, Malayalam Letter Ma, Malayalam Vowel Sign Aa, Malayalam Letter Ya)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xb8\xe0\xb4\xb0\xe0\xb5\x8d\xe2\x80\x8d\xe0\xb4\xb5\xe0\xb5\x8d\xe0\xb4\xb5\xe0\xb4\xa4\xe0\xb5\x8b\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xae\xe0\xb5\x81\xe0\xb4\x96\xe0\xb4\xae\xe0\xb4\xbe\xe0\xb4\xaf|\\n123456789|\\n"
    സര്‍വ്വതോന്മുഖമായ|
    123456789|

python `wcwidth`_ measures width 9, while *QTerminal* measures width 10

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db4\u0dca\u200d\u0dbb\u0d9a\u0dcf\u0dc1\u0db1\u0dba"`` (Sinhala Letter Alpapraana Payanna, Sinhala Sign Al-Lakuna, Zero Width Joiner, Sinhala Letter Rayanna, Sinhala Letter Alpapraana Kayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Taaluja Sayanna, Sinhala Letter Dantaja Nayanna, Sinhala Letter Yayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb4\xe0\xb7\x8a\xe2\x80\x8d\xe0\xb6\xbb\xe0\xb6\x9a\xe0\xb7\x8f\xe0\xb7\x81\xe0\xb6\xb1\xe0\xb6\xba|\\n12345|\\n"
    ප්‍රකාශනය|
    12345|

python `wcwidth`_ measures width 5, while *QTerminal* measures width 6

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u0989\u09a4\u09cd\u200d\u09aa\u09c0\u09a1\u09bc\u09a8\u09c7\u09b0"`` (Bengali Letter U, Bengali Letter Ta, Bengali Sign Virama, Zero Width Joiner, Bengali Letter Pa, Bengali Vowel Sign Ii, Bengali Letter Dda, Bengali Sign Nukta, Bengali Letter Na, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\x89\xe0\xa6\xa4\xe0\xa7\x8d\xe2\x80\x8d\xe0\xa6\xaa\xe0\xa7\x80\xe0\xa6\xa1\xe0\xa6\xbc\xe0\xa6\xa8\xe0\xa7\x87\xe0\xa6\xb0|\\n12345|\\n"
    উত্‍পীড়নের|
    12345|

python `wcwidth`_ measures width 5, while *QTerminal* measures width 6

.. _Alacritty:

Alacritty
=========

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 15.1.0 of python string ``"\u2ffc"`` (na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe2\xbf\xbc|\\n12|\\n"
    ⿼|
    12|

python `wcwidth`_ measures width 2, while *Alacritty* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *Alacritty* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *Alacritty* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *Alacritty* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Tibetan, Central                   311
Nuosu                              262
Assyrian Neo-Aramaic              1000
Tigrigna                          1000
Cherokee (cased)                  1000
Vai                               1000
Tamazight, Standard Morocan       1000
Mongolian, Halh (Mongolian)         33
Tai Dam                           1000
Lao                                486
Thai                               373
Pular (Adlam)                     1000
Arabic, Standard                  1000
Russian                           1000
Tagalog (Tagalog)                   31
Maldivian                         1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Javanese (Javanese)        106
Sanskrit (Grantha)         107
Kannada                    109
Khmer, Central             114
Malayalam                  114
Bengali                    115
Burmese                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *Alacritty* measures width 4

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *Alacritty* measures width 73

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *Alacritty* measures width 14

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *Alacritty* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *Alacritty* measures width 25

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *Alacritty* measures width 21

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *Alacritty* measures width 12

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *Alacritty* measures width 11

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *Alacritty* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *Alacritty* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *Alacritty* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *Alacritty* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *Alacritty* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *Alacritty* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *Alacritty* measures width 8

.. _GNOME_Terminal:

GNOME Terminal
==============

Tested Software version 3.46.8 on Linux

Wide character support
++++++++++++++++++++++

The best wide unicode table version for GNOME Terminal appears to be 
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
'13.0.0'           54        541        90.0185
'14.0.0'            4         41        90.2439
'15.0.0'            1         15        93.3333
'15.1.0'            5          5         0
=========  ==========  =========  =============

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 15.0.0 of python string ``"\U0001fabc"`` (Jellyfish)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\xaa\xbc|\\n12|\\n"
    🪼|
    12|

python `wcwidth`_ measures width 2, while *GNOME Terminal* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *GNOME Terminal* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *GNOME Terminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *GNOME Terminal* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Lao                                472
Pular (Adlam)                     1000
Nuosu                              261
Tamazight, Standard Morocan       1000
Tigrigna                          1000
Tibetan, Central                   292
Arabic, Standard                  1000
Maldivian                         1000
Cherokee (cased)                  1000
Vai                               1000
Tai Dam                           1000
Tagalog (Tagalog)                   31
Russian                           1000
Mongolian, Halh (Mongolian)         33
Thai                               370
Assyrian Neo-Aramaic              1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Javanese (Javanese)        107
Sanskrit (Grantha)         107
Kannada                    109
Khmer, Central             114
Malayalam                  114
Burmese                    115
Bengali                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *GNOME Terminal* measures width 4

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *GNOME Terminal* measures width 73

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *GNOME Terminal* measures width 14

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *GNOME Terminal* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *GNOME Terminal* measures width 25

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *GNOME Terminal* measures width 21

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *GNOME Terminal* measures width 11

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *GNOME Terminal* measures width 12

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *GNOME Terminal* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *GNOME Terminal* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *GNOME Terminal* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *GNOME Terminal* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *GNOME Terminal* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *GNOME Terminal* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *GNOME Terminal* measures width 8

.. _Tabby:

Tabby
=====

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 13.0.0 of python string ``"\u31bb"`` (Bopomofo Final Letter G)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe3\x86\xbb|\\n12|\\n"
    ㆻ|
    12|

python `wcwidth`_ measures width 2, while *Tabby* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *Tabby* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *Tabby* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *Tabby* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Thai                               373
Arabic, Standard                  1000
Mongolian, Halh (Mongolian)         33
Tagalog (Tagalog)                   31
Tibetan, Central                   311
Tai Dam                           1000
Pular (Adlam)                     1000
Tigrigna                          1000
Lao                                486
Cherokee (cased)                  1000
Nuosu                              262
Assyrian Neo-Aramaic              1000
Vai                               1000
Russian                           1000
Tamazight, Standard Morocan       1000
Maldivian                         1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Javanese (Javanese)        105
Tamil                      105
Sanskrit (Grantha)         107
Kannada                    109
Malayalam                  114
Khmer, Central             114
Bengali                    115
Burmese                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *Tabby* measures width 73

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *Tabby* measures width 4

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *Tabby* measures width 14

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *Tabby* measures width 4

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *Tabby* measures width 21

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *Tabby* measures width 25

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *Tabby* measures width 12

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *Tabby* measures width 11

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *Tabby* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *Tabby* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *Tabby* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *Tabby* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *Tabby* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *Tabby* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *Tabby* measures width 8

.. _VSCode_Terminal:

VSCode Terminal
===============

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 13.0.0 of python string ``"\u31bb"`` (Bopomofo Final Letter G)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe3\x86\xbb|\\n12|\\n"
    ㆻ|
    12|

python `wcwidth`_ measures width 2, while *VSCode Terminal* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *VSCode Terminal* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *VSCode Terminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *VSCode Terminal* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Nuosu                              262
Pular (Adlam)                     1000
Cherokee (cased)                  1000
Mongolian, Halh (Mongolian)         33
Tai Dam                           1000
Tagalog (Tagalog)                   31
Assyrian Neo-Aramaic              1000
Thai                               373
Tigrigna                          1000
Lao                                487
Arabic, Standard                  1000
Russian                           1000
Tamazight, Standard Morocan       1000
Tibetan, Central                   312
Vai                               1000
Maldivian                         1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Javanese (Javanese)        100
Tamil                      105
Sanskrit (Grantha)         107
Kannada                    109
Khmer, Central             114
Malayalam                  114
Burmese                    115
Bengali                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *VSCode Terminal* measures width 73

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *VSCode Terminal* measures width 4

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *VSCode Terminal* measures width 14

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *VSCode Terminal* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *VSCode Terminal* measures width 25

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *VSCode Terminal* measures width 21

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *VSCode Terminal* measures width 11

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *VSCode Terminal* measures width 12

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *VSCode Terminal* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *VSCode Terminal* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *VSCode Terminal* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *VSCode Terminal* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *VSCode Terminal* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *VSCode Terminal* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *VSCode Terminal* measures width 8

.. _Hyper:

Hyper
=====

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 13.0.0 of python string ``"\u31bb"`` (Bopomofo Final Letter G)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe3\x86\xbb|\\n12|\\n"
    ㆻ|
    12|

python `wcwidth`_ measures width 2, while *Hyper* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *Hyper* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *Hyper* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *Hyper* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Thai                               373
Tigrigna                          1000
Tibetan, Central                   312
Tagalog (Tagalog)                   31
Tai Dam                           1000
Lao                                487
Pular (Adlam)                     1000
Mongolian, Halh (Mongolian)         33
Arabic, Standard                  1000
Tamazight, Standard Morocan       1000
Russian                           1000
Cherokee (cased)                  1000
Assyrian Neo-Aramaic              1000
Maldivian                         1000
Nuosu                              262
Vai                               1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Javanese (Javanese)        106
Sanskrit (Grantha)         107
Kannada                    109
Khmer, Central             114
Malayalam                  114
Burmese                    115
Bengali                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *Hyper* measures width 4

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *Hyper* measures width 73

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *Hyper* measures width 14

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *Hyper* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *Hyper* measures width 25

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *Hyper* measures width 21

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *Hyper* measures width 11

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *Hyper* measures width 12

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *Hyper* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *Hyper* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *Hyper* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *Hyper* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *Hyper* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *Hyper* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *Hyper* measures width 8

.. _mlterm:

mlterm
======

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 10.0.0 of python string ``"\U0001b00b"`` (Hentaigana Letter U-2)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2, while *mlterm* measures width 0

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *mlterm* measures width 7

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *mlterm* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *mlterm* measures width 1

Language Support
----------------

The following 23 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Lao                                472
Vai                               1000
Cherokee (cased)                  1000
Khün                               474
Khmer, Central                     560
Panjabi, Eastern                  1000
Gujarati                          1000
Russian                           1000
Assyrian Neo-Aramaic              1000
Tamazight, Standard Morocan       1000
Tamil                             1000
Maldivian                         1000
Burmese                           1000
Sanskrit (Grantha)                1000
Nuosu                              261
Chakma                            1000
Tagalog (Tagalog)                   31
Thai                               370
Hindi                             1000
Tigrigna                          1000
Telugu                            1000
Tai Dam                           1000
Pular (Adlam)                     1000
===========================  =========

The following 8 languages are not supported or only partially supported:

===========================  =========
lang                           n_total
===========================  =========
Javanese (Javanese)                178
Malayalam                          375
Mongolian, Halh (Mongolian)         33
Arabic, Standard                  1099
Bengali                           1061
Sinhala                           1057
Tibetan, Central                   292
Kannada                           1001
===========================  =========

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua994\ua9c0\ua992\ua9bf\ua9bc\ua981\ua9b1\ua9bc\ua981\ua994\ua98f\ua9ba\ua9ad\ua9a4\ua9c0\ua994\ua9aa\ua9ba\ua9b4\ua9a9\ua9c0\ua9a9\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua9b2\ua9b1\ua9b1\ua9c0\ua9b1\ua9b6\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9a9\ua9ab\ua981\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9a5\ua9bf\ua9b6\ua9a7\ua9a2\ua9b6\ua9c9"`` (Javanese Letter Nga, Javanese Pangkon, Javanese Letter Ga, Javanese Consonant Sign Cakra, Javanese Vowel Sign Pepet, Javanese Sign Cecak, Javanese Letter Sa, Javanese Vowel Sign Pepet, Javanese Sign Cecak, Javanese Letter Nga, Javanese Letter Ka, Javanese Vowel Sign Taling, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Nga, Javanese Letter Ya, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Ma, Javanese Pangkon, Javanese Letter Ma, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Sa, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter Ma, Javanese Letter Ra, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Consonant Sign Cakra, Javanese Vowel Sign Wulu, Javanese Letter Ba, Javanese Letter Da, Javanese Vowel Sign Wulu, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa6\x94\xea\xa7\x80\xea\xa6\x92\xea\xa6\xbf\xea\xa6\xbc\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xbc\xea\xa6\x81\xea\xa6\x94\xea\xa6\x8f\xea\xa6\xba\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x94\xea\xa6\xaa\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xa9\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb1\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xa9\xea\xa6\xab\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xbf\xea\xa6\xb6\xea\xa6\xa7\xea\xa6\xa2\xea\xa6\xb6\xea\xa7\x89|\\n1234567890123456789012345678901234|\\n"
    ꦔ꧀ꦒꦿꦼꦁꦱꦼꦁꦔꦏꦺꦭꦤ꧀ꦔꦪꦺꦴꦩ꧀ꦩꦶꦲꦏ꧀ꦲꦏ꧀ꦲꦱꦱ꧀ꦱꦶꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦩꦫꦁꦱꦧꦼꦤ꧀ꦥꦿꦶꦧꦢꦶ꧉|
    1234567890123456789012345678901234|

python `wcwidth`_ measures width 34, while *mlterm* measures width 35

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d32\u0d4b\u0d15\u0d24\u0d4d\u0d24\u0d3f\u0d32\u0d4d\u200d"`` (Malayalam Letter La, Malayalam Vowel Sign Oo, Malayalam Letter Ka, Malayalam Letter Ta, Malayalam Sign Virama, Malayalam Letter Ta, Malayalam Vowel Sign I, Malayalam Letter La, Malayalam Sign Virama, Zero Width Joiner)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xb2\xe0\xb5\x8b\xe0\xb4\x95\xe0\xb4\xa4\xe0\xb5\x8d\xe0\xb4\xa4\xe0\xb4\xbf\xe0\xb4\xb2\xe0\xb5\x8d\xe2\x80\x8d|\\n12345|\\n"
    ലോകത്തില്‍|
    12345|

python `wcwidth`_ measures width 5, while *mlterm* measures width 6

Mongolian, Halh (Mongolian)
---------------------------

Example shell test using `printf(1)`_ of language, Mongolian, Halh (Mongolian) of python string ``"\u1828\u1821\u1837\u180e\u1821"`` (Mongolian Letter Na, Mongolian Letter E, Mongolian Letter Ra, Mongolian Vowel Separator, Mongolian Letter E)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa0\xa8\xe1\xa0\xa1\xe1\xa0\xb7\xe1\xa0\x8e\xe1\xa0\xa1|\\n1234|\\n"
    ᠨᠡᠷ᠎ᠡ|
    1234|

python `wcwidth`_ measures width 4, while *mlterm* measures width 5

Arabic, Standard
----------------

Example shell test using `printf(1)`_ of language, Arabic, Standard of python string ``"\u0627\u0644\u0623\u0648\u0644"`` (Arabic Letter Alef, Arabic Letter Lam, Arabic Letter Alef With Hamza Above, Arabic Letter Waw, Arabic Letter Lam)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xd8\xa7\xd9\x84\xd8\xa3\xd9\x88\xd9\x84|\\n12345|\\n"
    الأول|
    12345|

python `wcwidth`_ measures width 5, while *mlterm* measures width 4

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09b8\u09cd\u09ac\u09c0\u0995\u09c3\u09a4\u09bf\u200c\u0987"`` (Bengali Letter Sa, Bengali Sign Virama, Bengali Letter Ba, Bengali Vowel Sign Ii, Bengali Letter Ka, Bengali Vowel Sign Vocalic R, Bengali Letter Ta, Bengali Vowel Sign I, Zero Width Non-Joiner, Bengali Letter I)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xb8\xe0\xa7\x8d\xe0\xa6\xac\xe0\xa7\x80\xe0\xa6\x95\xe0\xa7\x83\xe0\xa6\xa4\xe0\xa6\xbf\xe2\x80\x8c\xe0\xa6\x87|\\n12345|\\n"
    স্বীকৃতি‌ই|
    12345|

python `wcwidth`_ measures width 5, while *mlterm* measures width 6

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db4\u0dca\u200d\u0dbb\u0d9a\u0dcf\u0dc1\u0db1\u0dba"`` (Sinhala Letter Alpapraana Payanna, Sinhala Sign Al-Lakuna, Zero Width Joiner, Sinhala Letter Rayanna, Sinhala Letter Alpapraana Kayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Taaluja Sayanna, Sinhala Letter Dantaja Nayanna, Sinhala Letter Yayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb4\xe0\xb7\x8a\xe2\x80\x8d\xe0\xb6\xbb\xe0\xb6\x9a\xe0\xb7\x8f\xe0\xb7\x81\xe0\xb6\xb1\xe0\xb6\xba|\\n12345|\\n"
    ප්‍රකාශනය|
    12345|

python `wcwidth`_ measures width 5, while *mlterm* measures width 7

Tibetan, Central
----------------

Example shell test using `printf(1)`_ of language, Tibetan, Central of python string ``"\u0f7c\u0f66\u0f0b\u0f54\u0f60\u0f72\u0f0b\u0f50\u0f7c\u0f56\u0f0b\u0f51\u0f56\u0f44\u0f0b\u0f61\u0f7c\u0f51\u0f0d"`` (Tibetan Vowel Sign O, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Pa, Tibetan Letter -A, Tibetan Vowel Sign I, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Vowel Sign O, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Da, Tibetan Letter Ba, Tibetan Letter Nga, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ya, Tibetan Vowel Sign O, Tibetan Letter Da, Tibetan Mark Shad)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xbd\xbc\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x96\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x91\xe0\xbc\x8d|\\n123456789012345|\\n"
    ོས་པའི་ཐོབ་དབང་ཡོད།|
    123456789012345|

python `wcwidth`_ measures width 15, while *mlterm* measures width 16

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cb5\u0cbe\u0c95\u0ccd\u200c\u0cb8\u0ccd\u0cb5\u0cbe\u0ca4\u0c82\u0ca4\u0ccd\u0cb0\u0ccd\u0caf"`` (Kannada Letter Va, Kannada Vowel Sign Aa, Kannada Letter Ka, Kannada Sign Virama, Zero Width Non-Joiner, Kannada Letter Sa, Kannada Sign Virama, Kannada Letter Va, Kannada Vowel Sign Aa, Kannada Letter Ta, Kannada Sign Anusvara, Kannada Letter Ta, Kannada Sign Virama, Kannada Letter Ra, Kannada Sign Virama, Kannada Letter Ya)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xb5\xe0\xb2\xbe\xe0\xb2\x95\xe0\xb3\x8d\xe2\x80\x8c\xe0\xb2\xb8\xe0\xb3\x8d\xe0\xb2\xb5\xe0\xb2\xbe\xe0\xb2\xa4\xe0\xb2\x82\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xb0\xe0\xb3\x8d\xe0\xb2\xaf|\\n12345678|\\n"
    ವಾಕ್‌ಸ್ವಾತಂತ್ರ್ಯ|
    12345678|

python `wcwidth`_ measures width 8, while *mlterm* measures width 9

.. _xfce4-terminal:

xfce4-terminal
==============

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 10.0.0 of python string ``"\U0001b00b"`` (Hentaigana Letter U-2)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2, while *xfce4-terminal* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *xfce4-terminal* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *xfce4-terminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *xfce4-terminal* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Cherokee (cased)                  1000
Tibetan, Central                   292
Pular (Adlam)                     1000
Mongolian, Halh (Mongolian)         33
Russian                           1000
Maldivian                         1000
Tamazight, Standard Morocan       1000
Assyrian Neo-Aramaic              1000
Thai                               370
Lao                                472
Vai                               1000
Tagalog (Tagalog)                   31
Nuosu                              261
Tigrigna                          1000
Tai Dam                           1000
Arabic, Standard                  1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Sanskrit (Grantha)         107
Javanese (Javanese)        107
Kannada                    109
Khmer, Central             114
Malayalam                  114
Burmese                    115
Bengali                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *xfce4-terminal* measures width 4

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *xfce4-terminal* measures width 14

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *xfce4-terminal* measures width 73

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *xfce4-terminal* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *xfce4-terminal* measures width 25

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *xfce4-terminal* measures width 21

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *xfce4-terminal* measures width 11

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *xfce4-terminal* measures width 12

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *xfce4-terminal* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *xfce4-terminal* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *xfce4-terminal* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *xfce4-terminal* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *xfce4-terminal* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *xfce4-terminal* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *xfce4-terminal* measures width 8

.. _st:

st
==

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 10.0.0 of python string ``"\U0001b00b"`` (Hentaigana Letter U-2)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2, while *st* measures width 0

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *st* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *st* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *st* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Tamazight, Standard Morocan       1000
Maldivian                         1000
Tigrigna                          1000
Russian                           1000
Cherokee (cased)                  1000
Arabic, Standard                  1000
Lao                                472
Tai Dam                           1000
Assyrian Neo-Aramaic              1000
Tagalog (Tagalog)                   31
Vai                               1000
Nuosu                              261
Thai                               370
Mongolian, Halh (Mongolian)         33
Pular (Adlam)                     1000
Tibetan, Central                   292
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Sanskrit (Grantha)         107
Javanese (Javanese)        107
Kannada                    109
Malayalam                  114
Khmer, Central             114
Bengali                    115
Burmese                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *st* measures width 4

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *st* measures width 14

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *st* measures width 73

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *st* measures width 4

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *st* measures width 21

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *st* measures width 25

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *st* measures width 12

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *st* measures width 11

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *st* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *st* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *st* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *st* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *st* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *st* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *st* measures width 8

.. _LXTerminal:

LXTerminal
==========

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 10.0.0 of python string ``"\U0001b00b"`` (Hentaigana Letter U-2)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2, while *LXTerminal* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *LXTerminal* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *LXTerminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *LXTerminal* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Tibetan, Central                   292
Vai                               1000
Russian                           1000
Lao                                472
Maldivian                         1000
Pular (Adlam)                     1000
Tai Dam                           1000
Cherokee (cased)                  1000
Tamazight, Standard Morocan       1000
Thai                               370
Tigrigna                          1000
Tagalog (Tagalog)                   31
Mongolian, Halh (Mongolian)         33
Nuosu                              261
Assyrian Neo-Aramaic              1000
Arabic, Standard                  1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Sanskrit (Grantha)         107
Javanese (Javanese)        107
Kannada                    109
Malayalam                  114
Khmer, Central             114
Burmese                    115
Bengali                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *LXTerminal* measures width 4

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *LXTerminal* measures width 14

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *LXTerminal* measures width 73

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *LXTerminal* measures width 4

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *LXTerminal* measures width 21

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *LXTerminal* measures width 25

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *LXTerminal* measures width 11

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *LXTerminal* measures width 12

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *LXTerminal* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *LXTerminal* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *LXTerminal* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *LXTerminal* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *LXTerminal* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *LXTerminal* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *LXTerminal* measures width 8

.. _zutty:

zutty
=====

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 10.0.0 of python string ``"\U0001b00b"`` (Hentaigana Letter U-2)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2, while *zutty* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *zutty* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *zutty* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *zutty* measures width 1

Language Support
----------------

The following 16 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Lao                                472
Arabic, Standard                  1000
Assyrian Neo-Aramaic              1000
Maldivian                         1000
Mongolian, Halh (Mongolian)         33
Tai Dam                           1000
Thai                               370
Vai                               1000
Russian                           1000
Nuosu                              261
Pular (Adlam)                     1000
Cherokee (cased)                  1000
Tagalog (Tagalog)                   31
Tibetan, Central                   292
Tamazight, Standard Morocan       1000
Tigrigna                          1000
===========================  =========

The following 15 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Javanese (Javanese)        107
Sanskrit (Grantha)         107
Kannada                    109
Khmer, Central             114
Malayalam                  114
Bengali                    115
Burmese                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *zutty* measures width 4

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *zutty* measures width 73

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *zutty* measures width 14

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *zutty* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *zutty* measures width 25

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *zutty* measures width 21

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *zutty* measures width 12

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *zutty* measures width 11

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *zutty* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *zutty* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *zutty* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *zutty* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *zutty* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *zutty* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *zutty* measures width 8

.. _XTerm:

XTerm
=====

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 10.0.0 of python string ``"\U0001b00b"`` (Hentaigana Letter U-2)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2, while *XTerm* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *XTerm* measures width 5

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *XTerm* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *XTerm* measures width 1

Language Support
----------------

The following 15 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Tamazight, Standard Morocan       1000
Assyrian Neo-Aramaic              1000
Maldivian                         1000
Mongolian, Halh (Mongolian)         33
Nuosu                              261
Thai                               370
Tagalog (Tagalog)                   31
Tigrigna                          1000
Vai                               1000
Lao                                472
Tai Dam                           1000
Pular (Adlam)                     1000
Cherokee (cased)                  1000
Arabic, Standard                  1000
Russian                           1000
===========================  =========

The following 16 languages are not supported or only partially supported:

===================  =========
lang                   n_total
===================  =========
Tamil                      105
Sanskrit (Grantha)         107
Javanese (Javanese)        107
Kannada                    109
Khmer, Central             114
Malayalam                  114
Bengali                    115
Burmese                    115
Khün                       121
Telugu                     141
Gujarati                   143
Hindi                      146
Panjabi, Eastern           173
Sinhala                    175
Chakma                     248
Tibetan, Central           292
===================  =========

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *XTerm* measures width 4

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *XTerm* measures width 14

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *XTerm* measures width 73

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *XTerm* measures width 4

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *XTerm* measures width 25

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *XTerm* measures width 21

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *XTerm* measures width 12

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *XTerm* measures width 11

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *XTerm* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *XTerm* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *XTerm* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *XTerm* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *XTerm* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *XTerm* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *XTerm* measures width 8

Tibetan, Central
----------------

Example shell test using `printf(1)`_ of language, Tibetan, Central of python string ``"\u0f7c\u0f66\u0f0b\u0f54\u0f60\u0f72\u0f0b\u0f50\u0f7c\u0f56\u0f0b\u0f51\u0f56\u0f44\u0f0b\u0f61\u0f7c\u0f51\u0f0d"`` (Tibetan Vowel Sign O, Tibetan Letter Sa, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Pa, Tibetan Letter -A, Tibetan Vowel Sign I, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Tha, Tibetan Vowel Sign O, Tibetan Letter Ba, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Da, Tibetan Letter Ba, Tibetan Letter Nga, Tibetan Mark Intersyllabic Tsheg, Tibetan Letter Ya, Tibetan Vowel Sign O, Tibetan Letter Da, Tibetan Mark Shad)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xbd\xbc\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x96\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x91\xe0\xbc\x8d|\\n123456789012345|\\n"
    ོས་པའི་ཐོབ་དབང་ཡོད།|
    123456789012345|

python `wcwidth`_ measures width 15, while *XTerm* measures width 16

.. _Terminal:

Terminal
========

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

Example shell test using `printf(1)`_ of a WIDE character from Unicode Version 10.0.0 of python string ``"\U0001b00b"`` (Hentaigana Letter U-2)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9b\x80\x8b|\\n12|\\n"
    𛀋|
    12|

python `wcwidth`_ measures width 2, while *Terminal* measures width 1

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

Example shell test using `printf(1)`_ of an Emoji ZWJ Sequence from Emoji Version 2.0 of python string ``"\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"`` (Man, Zero Width Joiner, Heavy Black Heart, Variation Selector-16, Zero Width Joiner, Man)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x9f\x91\xa8\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x91\xa8|\\n12|\\n"
    👨‍❤️‍👨|
    12|

python `wcwidth`_ measures width 2, while *Terminal* measures width 7

Variation Selector-16 support
-----------------------------

Emoji VS-16 results for *Terminal* is 100 errors out of 100 total codepoints tested, 0.0% success.
Example shell test using `printf(1)`_ of a NARROW Emoji made WIDE by *Variation Selector-16* of python string ``"0\ufe0f"`` (Digit Zero, Variation Selector-16)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "0\xef\xb8\x8f|\\n12|\\n"
    0️|
    12|

python `wcwidth`_ measures width 2, while *Terminal* measures width 1

Language Support
----------------

The following 15 languages were tested with 100% success:

===========================  =========
lang                           n_total
===========================  =========
Nuosu                              261
Vai                               1000
Russian                           1000
Tagalog (Tagalog)                   31
Assyrian Neo-Aramaic              1000
Lao                                472
Tibetan, Central                   292
Maldivian                         1000
Pular (Adlam)                     1000
Arabic, Standard                  1000
Cherokee (cased)                  1000
Tai Dam                           1000
Tigrigna                          1000
Thai                               370
Tamazight, Standard Morocan       1000
===========================  =========

The following 16 languages are not supported or only partially supported:

===========================  =========
lang                           n_total
===========================  =========
Javanese (Javanese)                101
Tamil                              105
Sanskrit (Grantha)                 107
Kannada                            109
Malayalam                          113
Khmer, Central                     114
Burmese                            115
Bengali                            115
Khün                               121
Telugu                             141
Gujarati                           143
Hindi                              146
Panjabi, Eastern                   173
Sinhala                            175
Chakma                             248
Mongolian, Halh (Mongolian)         33
===========================  =========

Javanese (Javanese)
-------------------

Example shell test using `printf(1)`_ of language, Javanese (Javanese) of python string ``"\ua9cb\ua9b1\ua9a7\ua9bc\ua9a4\ua9c0\ua9b2\ua9b8\ua9a9\ua9a0\ua9c0\ua9a9\ua9a4\ua9b8\ua981\ua9b1\ua9ad\ua9b2\ua9b6\ua982\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua9b2\ua98f\ua9c0\ua9b2\ua98f\ua9c0\ua98f\ua981\ua9a5\ua9ba\ua9b4\ua99d\ua9ba\ua9b4\ua9ad\ua9a4\ua9c0\ua9a5\ua9b6\ua9a4\ua9b1\ua9c0\ua99b\ua9b6\ua9ad\ua9a4\ua9c0\ua98f\ua9a4\ua9c0\ua99b\ua9b6\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua98f\ua9a7\ua9ba\ua9a7\ua9b1\ua9c0\ua9b1\ua9a4\ua9c0\ua9b2\ua9b6\ua981\ua9a7\ua98f\ua9b8\ua9a4\ua9b6\ua981\ua9b2\ua981\ua992\ua9bc\ua982\ua9b2\ua981\ua992\ua9bc\ua982\ua9c9"`` (Javanese Pada Adeg Adeg, Javanese Letter Sa, Javanese Letter Ba, Javanese Vowel Sign Pepet, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Suku, Javanese Letter Ma, Javanese Letter Ta, Javanese Pangkon, Javanese Letter Ma, Javanese Letter Na, Javanese Vowel Sign Suku, Javanese Sign Cecak, Javanese Letter Sa, Javanese Letter La, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Layar, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ha, Javanese Letter Ka, Javanese Pangkon, Javanese Letter Ka, Javanese Sign Cecak, Javanese Letter Pa, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter Dda, Javanese Vowel Sign Taling, Javanese Vowel Sign Tarung, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Pa, Javanese Vowel Sign Wulu, Javanese Letter Na, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter La, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Na, Javanese Pangkon, Javanese Letter Tta, Javanese Vowel Sign Wulu, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ka, Javanese Letter Ba, Javanese Vowel Sign Taling, Javanese Letter Ba, Javanese Letter Sa, Javanese Pangkon, Javanese Letter Sa, Javanese Letter Na, Javanese Pangkon, Javanese Letter Ha, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ba, Javanese Letter Ka, Javanese Vowel Sign Suku, Javanese Letter Na, Javanese Vowel Sign Wulu, Javanese Sign Cecak, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Letter Ha, Javanese Sign Cecak, Javanese Letter Ga, Javanese Vowel Sign Pepet, Javanese Sign Layar, Javanese Pada Lungsi)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xa9\xea\xa6\xa4\xea\xa6\xb8\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xad\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x82\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\xb2\xea\xa6\x8f\xea\xa7\x80\xea\xa6\x8f\xea\xa6\x81\xea\xa6\xa5\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x9d\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xa5\xea\xa6\xb6\xea\xa6\xa4\xea\xa6\xb1\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\xad\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x9b\xea\xa6\xb6\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\x8f\xea\xa6\xa7\xea\xa6\xba\xea\xa6\xa7\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xb1\xea\xa6\xa4\xea\xa7\x80\xea\xa6\xb2\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xa7\xea\xa6\x8f\xea\xa6\xb8\xea\xa6\xa4\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xbc\xea\xa6\x82\xea\xa7\x89|\\n123456789012345678901234567890123456789012345678901234|\\n"
    ꧋ꦱꦧꦼꦤ꧀ꦲꦸꦩꦠ꧀ꦩꦤꦸꦁꦱꦭꦲꦶꦂꦏꦤ꧀ꦛꦶꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦺꦴꦝꦺꦴꦭꦤ꧀ꦥꦶꦤꦱ꧀ꦛꦶꦭꦤ꧀ꦏꦤ꧀ꦛꦶꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦏꦧꦺꦧꦱ꧀ꦱꦤ꧀ꦲꦶꦁꦧꦏꦸꦤꦶꦁꦲꦁꦒꦼꦂꦲꦁꦒꦼꦂ꧉|
    123456789012345678901234567890123456789012345678901234|

python `wcwidth`_ measures width 54, while *Terminal* measures width 73

Tamil
-----

Example shell test using `printf(1)`_ of language, Tamil of python string ``"\u0bae\u0ba9\u0bbf\u0ba4"`` (Tamil Letter Ma, Tamil Letter Nnna, Tamil Vowel Sign I, Tamil Letter Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
    மனித|
    123|

python `wcwidth`_ measures width 3, while *Terminal* measures width 4

Sanskrit (Grantha)
------------------

Example shell test using `printf(1)`_ of language, Sanskrit (Grantha) of python string ``"\U0001132e\U0001133e\U00011328\U00011335\U0001133e\U00011327\U0001133f\U00011315\U0001133e\U00011330\U0001133e\U00011323\U0001133e\U00011302"`` (Grantha Letter Ma, Grantha Vowel Sign Aa, Grantha Letter Na, Grantha Letter Va, Grantha Vowel Sign Aa, Grantha Letter Dha, Grantha Vowel Sign I, Grantha Letter Ka, Grantha Vowel Sign Aa, Grantha Letter Ra, Grantha Vowel Sign Aa, Grantha Letter Nna, Grantha Vowel Sign Aa, Grantha Sign Anusvara)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
    𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
    1234567|

python `wcwidth`_ measures width 7, while *Terminal* measures width 14

Kannada
-------

Example shell test using `printf(1)`_ of language, Kannada of python string ``"\u0cae\u0cbe\u0ca8\u0cb5"`` (Kannada Letter Ma, Kannada Vowel Sign Aa, Kannada Letter Na, Kannada Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
    ಮಾನವ|
    123|

python `wcwidth`_ measures width 3, while *Terminal* measures width 4

Malayalam
---------

Example shell test using `printf(1)`_ of language, Malayalam of python string ``"\u0d2e\u0d28\u0d41\u0d37\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d3e\u0d36\u0d19\u0d4d\u0d19\u0d33\u0d46\u0d15\u0d4d\u0d15\u0d41\u0d31\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28"`` (Malayalam Letter Ma, Malayalam Letter Na, Malayalam Vowel Sign U, Malayalam Letter Ssa, Malayalam Sign Virama, Malayalam Letter Ya, Malayalam Vowel Sign Aa, Malayalam Letter Va, Malayalam Letter Ka, Malayalam Vowel Sign Aa, Malayalam Letter Sha, Malayalam Letter Nga, Malayalam Sign Virama, Malayalam Letter Nga, Malayalam Letter Lla, Malayalam Vowel Sign E, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Rra, Malayalam Vowel Sign I, Malayalam Letter Ka, Malayalam Sign Virama, Malayalam Letter Ka, Malayalam Vowel Sign U, Malayalam Letter Na, Malayalam Sign Virama, Malayalam Letter Na)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
    മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
    12345678901234567|

python `wcwidth`_ measures width 17, while *Terminal* measures width 21

Khmer, Central
--------------

Example shell test using `printf(1)`_ of language, Khmer, Central of python string ``"\u179f\u17c1\u1785\u1780\u17d2\u178a\u17b8\u1794\u17d2\u179a\u1780\u17b6\u179f\u1787\u17b6\u179f\u1780\u179b\u179f\u17d2\u178a\u17b8\u1796\u17b8\u179f\u17b7\u1791\u17d2\u1792\u17b7\u1798\u1793\u17bb\u179f\u17d2\u179f"`` (Khmer Letter Sa, Khmer Vowel Sign E, Khmer Letter Ca, Khmer Letter Ka, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Ba, Khmer Sign Coeng, Khmer Letter Ro, Khmer Letter Ka, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Co, Khmer Vowel Sign Aa, Khmer Letter Sa, Khmer Letter Ka, Khmer Letter Lo, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Da, Khmer Vowel Sign Ii, Khmer Letter Po, Khmer Vowel Sign Ii, Khmer Letter Sa, Khmer Vowel Sign I, Khmer Letter To, Khmer Sign Coeng, Khmer Letter Tho, Khmer Vowel Sign I, Khmer Letter Mo, Khmer Letter No, Khmer Vowel Sign U, Khmer Letter Sa, Khmer Sign Coeng, Khmer Letter Sa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
    សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
    1234567890123456789012|

python `wcwidth`_ measures width 22, while *Terminal* measures width 25

Burmese
-------

Example shell test using `printf(1)`_ of language, Burmese of python string ``"\u1021\u1015\u103c\u100a\u103a\u1015\u103c\u100a\u103a\u1006\u102d\u102f\u1004\u103a\u101b\u102c"`` (Myanmar Letter A, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Pa, Myanmar Consonant Sign Medial Ra, Myanmar Letter Nnya, Myanmar Sign Asat, Myanmar Letter Cha, Myanmar Vowel Sign I, Myanmar Vowel Sign U, Myanmar Letter Nga, Myanmar Sign Asat, Myanmar Letter Ra, Myanmar Vowel Sign Aa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
    အပြည်ပြည်ဆိုင်ရာ|
    12345678|

python `wcwidth`_ measures width 8, while *Terminal* measures width 11

Bengali
-------

Example shell test using `printf(1)`_ of language, Bengali of python string ``"\u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0\u09c7\u09b0"`` (Bengali Letter Ma, Bengali Vowel Sign Aa, Bengali Letter Na, Bengali Letter Ba, Bengali Vowel Sign Aa, Bengali Letter Dha, Bengali Vowel Sign I, Bengali Letter Ka, Bengali Vowel Sign Aa, Bengali Letter Ra, Bengali Vowel Sign E, Bengali Letter Ra)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
    মানবাধিকারের|
    1234567|

python `wcwidth`_ measures width 7, while *Terminal* measures width 12

Khün
----

Example shell test using `printf(1)`_ of language, Khün of python string ``"\u1a20\u1a32\u1a65\u1a20\u1a63\u1a45\u1a64\u1a75\u1a2f\u1a60\u1a45\u1a60\u1a3f\u1a62\u1a3e\u1a36\u1a69\u1a54\u1a29\u1a63\u1a60\u1a32"`` (Tai Tham Letter High Ka, Tai Tham Letter High Ta, Tai Tham Vowel Sign I, Tai Tham Letter High Ka, Tai Tham Vowel Sign Aa, Tai Tham Letter Wa, Tai Tham Vowel Sign Tall Aa, Tai Tham Sign Tone-1, Tai Tham Letter Da, Tai Tham Sign Sakot, Tai Tham Letter Wa, Tai Tham Sign Sakot, Tai Tham Letter Low Ya, Tai Tham Vowel Sign Mai Sat, Tai Tham Letter Ma, Tai Tham Letter Na, Tai Tham Vowel Sign U, Tai Tham Letter Great Sa, Tai Tham Letter Low Ca, Tai Tham Vowel Sign Aa, Tai Tham Sign Sakot, Tai Tham Letter High Ta)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
    ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
    123456789012|

python `wcwidth`_ measures width 12, while *Terminal* measures width 15

Telugu
------

Example shell test using `printf(1)`_ of language, Telugu of python string ``"\u0c2e\u0c3e\u0c28\u0c35\u0c38\u0c4d\u0c35\u0c24\u0c4d\u0c35\u0c2e\u0c41\u0c32"`` (Telugu Letter Ma, Telugu Vowel Sign Aa, Telugu Letter Na, Telugu Letter Va, Telugu Letter Sa, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ta, Telugu Sign Virama, Telugu Letter Va, Telugu Letter Ma, Telugu Vowel Sign U, Telugu Letter La)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
    మానవస్వత్వముల|
    123456789|

python `wcwidth`_ measures width 9, while *Terminal* measures width 10

Gujarati
--------

Example shell test using `printf(1)`_ of language, Gujarati of python string ``"\u0aae\u0abe\u0aa8\u0ab5"`` (Gujarati Letter Ma, Gujarati Vowel Sign Aa, Gujarati Letter Na, Gujarati Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
    માનવ|
    123|

python `wcwidth`_ measures width 3, while *Terminal* measures width 4

Hindi
-----

Example shell test using `printf(1)`_ of language, Hindi of python string ``"\u092e\u093e\u0928\u0935"`` (Devanagari Letter Ma, Devanagari Vowel Sign Aa, Devanagari Letter Na, Devanagari Letter Va)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
    मानव|
    123|

python `wcwidth`_ measures width 3, while *Terminal* measures width 4

Panjabi, Eastern
----------------

Example shell test using `printf(1)`_ of language, Panjabi, Eastern of python string ``"\u0a2e\u0a28\u0a41\u0a71\u0a16\u0a40"`` (Gurmukhi Letter Ma, Gurmukhi Letter Na, Gurmukhi Vowel Sign U, Gurmukhi Addak, Gurmukhi Letter Kha, Gurmukhi Vowel Sign Ii)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
    ਮਨੁੱਖੀ|
    123|

python `wcwidth`_ measures width 3, while *Terminal* measures width 4

Sinhala
-------

Example shell test using `printf(1)`_ of language, Sinhala of python string ``"\u0db8\u0dcf\u0db1\u0dc0"`` (Sinhala Letter Mayanna, Sinhala Vowel Sign Aela-Pilla, Sinhala Letter Dantaja Nayanna, Sinhala Letter Vayanna)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
    මානව|
    123|

python `wcwidth`_ measures width 3, while *Terminal* measures width 4

Chakma
------

Example shell test using `printf(1)`_ of language, Chakma of python string ``"\U0001111f\U0001111a\U0001112c\U0001112d\U00011103\U00011107\U00011134\U00011107\U00011125\U00011127\U00011101\U00011122\U00011134"`` (Chakma Letter Maa, Chakma Letter Naa, Chakma Vowel Sign E, Chakma Vowel Sign Ai, Chakma Letter Aa, Chakma Letter Kaa, Chakma Maayyaa, Chakma Letter Kaa, Chakma Letter Saa, Chakma Vowel Sign A, Chakma Sign Anusvara, Chakma Letter Raa, Chakma Maayyaa)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
    𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
    1234567|

python `wcwidth`_ measures width 7, while *Terminal* measures width 8

Mongolian, Halh (Mongolian)
---------------------------

Example shell test using `printf(1)`_ of language, Mongolian, Halh (Mongolian) of python string ``"\u1828\u1821\u1837\u180e\u1821"`` (Mongolian Letter Na, Mongolian Letter E, Mongolian Letter Ra, Mongolian Vowel Separator, Mongolian Letter E)
as a utf-8 bytestring, trailing ``'|'`` should align in output::

    $ printf "\xe1\xa0\xa8\xe1\xa0\xa1\xe1\xa0\xb7\xe1\xa0\x8e\xe1\xa0\xa1|\\n1234|\\n"
    ᠨᠡᠷ᠎ᠡ|
    1234|

python `wcwidth`_ measures width 4, while *Terminal* measures width 5

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth`: https://www.github.com/jquast/wcwidth/
