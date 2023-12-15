.. _WezTerm:

WezTerm
-------


Tested Software version 20230712 on Darwin
Full results available at ucs-detect_ repository path
`data/macos-WezTerm-20230712.yaml <https://github.com/jquast/ucs-detect/blob/master/data/macos-WezTerm-20230712.yaml>`_

.. _WezTermwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for WezTerm appears to be 
**15.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total  pct_success
=========  ==========  =========  =============
'5.1.0'             0         26  100.0%
'5.2.0'            79        269  70.6%
'6.0.0'             0         13  100.0%
'9.0.0'             0       5000  100.0%
'10.0.0'            0        735  100.0%
'11.0.0'            0         62  100.0%
'12.0.0'            0         62  100.0%
'12.1.0'            0          1  100.0%
'13.0.0'            1        541  99.8%
'14.0.0'            0         41  100.0%
'15.0.0'            0         15  100.0%
'15.1.0'            5          5  0.0%
=========  ==========  =========  =============

Sequence of a WIDE character from Unicode Version 15.1.0, from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======
`U+2FFE <https://codepoints.net/U+2FFE>`_  '\\u2ffe'  Cn                  2  na
=========================================  =========  ==========  =========  ======

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe2\xbf\xbe|\\n12|\\n"
        ⿾|
        12|

- python `wcwidth.wcswidth()`_ measures width 2, 
  while *WezTerm* measures width 1.

.. _WezTermzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *WezTerm* appears to be 
**15.1**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total  pct_success
=========  ==========  =========  =============
'2.0'               0         22  100.0%
'4.0'               0        579  100.0%
'5.0'               0        100  100.0%
'11.0'              0         73  100.0%
'12.0'              0        112  100.0%
'12.1'              0        165  100.0%
'13.0'              0         51  100.0%
'13.1'              0         83  100.0%
'14.0'              0         20  100.0%
'15.0'              0          1  100.0%
'15.1'              0        109  100.0%
=========  ==========  =========  =============

.. _WezTermvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *WezTerm* is 100 errors
out of 100 total codepoints tested, 0.0% success.
Sequence of a NARROW Emoji made WIDE by *Variation Selector-16*, from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ======================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ======================
`U+0001F325 <https://codepoints.net/U+0001F325>`_  '\\U0001f325'  So                  1  WHITE SUN BEHIND CLOUD
`U+FE0F <https://codepoints.net/U+FE0F>`_          '\\ufe0f'      Mn                  0  VARIATION SELECTOR-16
=================================================  =============  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9f\x8c\xa5\xef\xb8\x8f|\\n12|\\n"
        🌥️|
        12|

- python `wcwidth.wcswidth()`_ measures width 2, 
  while *WezTerm* measures width 1.


.. _WezTermlang:

Language Support
++++++++++++++++

The following 94 languages were tested with 100% success:

Adyghe, Aja, Amarakaeri, Arabic, Standard, Assyrian Neo-Aramaic, Baatonum, Bamun, Bhojpuri, Bora, Burmese, Chakma, Cherokee (cased), Chickasaw, Chinantec, Chiltepec, Dagaare, Southern, Dangme, Dari, Dendi, Dinka, Northeastern, Ditammari, Dzongkha, Evenki, Farsi, Western, Fon, Fur, Ga, Gen, Gilyak, Gujarati, Gumuz, Hindi, Idoma, Javanese (Javanese), Kabardian, Kannada, Khmer, Central, Khün, Lamnso', Lao, Lingala (tones), Magahi, Maithili, Maldivian, Mazahua Central, Mixtec, Metlatónoc, Mon, Mongolian, Halh (Mongolian), Mòoré, Nanai, Navajo, Nuosu, Orok, Otomi, Mezquital, Panjabi, Eastern, Panjabi, Western, Pashto, Northern, Picard, Pular, Pular (Adlam), Sanskrit, Sanskrit (Grantha), Secoya, Seraiki, Serer-Sine, Shan, Siona, South Azerbaijani, Tagalog (Tagalog), Tai Dam, Tamang, Eastern, Tamazight, Central Atlas, Tamazight, Central Atlas (Tifinagh), Tamazight, Standard Morocan, Tamil, Tamil (Sri Lanka), Telugu, Tem, Thai, Thai (2), Tibetan, Central, Ticuna, Uduk, Urdu, Urdu (2), Vai, Veps, Vietnamese, Vietnamese (Han nom), Waama, Yaneshaʼ, Yiddish, Eastern, Yoruba, Yukaghir, Northern, Éwé.

The following 5 languages are not fully supported:

=========  ==========  =========  =============
lang         n_errors    n_total    pct_success
=========  ==========  =========  =============
Malayalam         109       1630        93.3129
Sinhala           107       1655        93.5347
Marathi             5       1614        99.6902
Nepali              3       1385        99.7834
Bengali             3       1413        99.7877
=========  ==========  =========  =============

Malayalam
^^^^^^^^^

Sequence of language *Malayalam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0D38 <https://codepoints.net/U+0D38>`_  '\\u0d38'  Lo                  1  MALAYALAM LETTER SA
`U+0D30 <https://codepoints.net/U+0D30>`_  '\\u0d30'  Lo                  1  MALAYALAM LETTER RA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
`U+0D35 <https://codepoints.net/U+0D35>`_  '\\u0d35'  Lo                  1  MALAYALAM LETTER VA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D35 <https://codepoints.net/U+0D35>`_  '\\u0d35'  Lo                  1  MALAYALAM LETTER VA
`U+0D24 <https://codepoints.net/U+0D24>`_  '\\u0d24'  Lo                  1  MALAYALAM LETTER TA
`U+0D4B <https://codepoints.net/U+0D4B>`_  '\\u0d4b'  Mc                  0  MALAYALAM VOWEL SIGN OO
`U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D2E <https://codepoints.net/U+0D2E>`_  '\\u0d2e'  Lo                  1  MALAYALAM LETTER MA
`U+0D41 <https://codepoints.net/U+0D41>`_  '\\u0d41'  Mn                  0  MALAYALAM VOWEL SIGN U
`U+0D16 <https://codepoints.net/U+0D16>`_  '\\u0d16'  Lo                  1  MALAYALAM LETTER KHA
`U+0D2E <https://codepoints.net/U+0D2E>`_  '\\u0d2e'  Lo                  1  MALAYALAM LETTER MA
`U+0D3E <https://codepoints.net/U+0D3E>`_  '\\u0d3e'  Mc                  0  MALAYALAM VOWEL SIGN AA
`U+0D2F <https://codepoints.net/U+0D2F>`_  '\\u0d2f'  Lo                  1  MALAYALAM LETTER YA
=========================================  =========  ==========  =========  =======================

Total codepoints: 17


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb4\xb8\xe0\xb4\xb0\xe0\xb5\x8d\xe2\x80\x8d\xe0\xb4\xb5\xe0\xb5\x8d\xe0\xb4\xb5\xe0\xb4\xa4\xe0\xb5\x8b\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xae\xe0\xb5\x81\xe0\xb4\x96\xe0\xb4\xae\xe0\xb4\xbe\xe0\xb4\xaf|\\n123456789|\\n"
        സര്‍വ്വതോന്മുഖമായ|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9, 
  while *WezTerm* measures width 10.

Sinhala
^^^^^^^

Sequence of language *Sinhala* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================================
`U+0DB4 <https://codepoints.net/U+0DB4>`_  '\\u0db4'  Lo                  1  SINHALA LETTER ALPAPRAANA PAYANNA
`U+0DCA <https://codepoints.net/U+0DCA>`_  '\\u0dca'  Mn                  0  SINHALA SIGN AL-LAKUNA
`U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
`U+0DBB <https://codepoints.net/U+0DBB>`_  '\\u0dbb'  Lo                  1  SINHALA LETTER RAYANNA
`U+0D9A <https://codepoints.net/U+0D9A>`_  '\\u0d9a'  Lo                  1  SINHALA LETTER ALPAPRAANA KAYANNA
`U+0DCF <https://codepoints.net/U+0DCF>`_  '\\u0dcf'  Mc                  0  SINHALA VOWEL SIGN AELA-PILLA
`U+0DC1 <https://codepoints.net/U+0DC1>`_  '\\u0dc1'  Lo                  1  SINHALA LETTER TAALUJA SAYANNA
`U+0DB1 <https://codepoints.net/U+0DB1>`_  '\\u0db1'  Lo                  1  SINHALA LETTER DANTAJA NAYANNA
`U+0DBA <https://codepoints.net/U+0DBA>`_  '\\u0dba'  Lo                  1  SINHALA LETTER YAYANNA
=========================================  =========  ==========  =========  =================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb6\xb4\xe0\xb7\x8a\xe2\x80\x8d\xe0\xb6\xbb\xe0\xb6\x9a\xe0\xb7\x8f\xe0\xb7\x81\xe0\xb6\xb1\xe0\xb6\xba|\\n12345|\\n"
        ප්‍රකාශනය|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5, 
  while *WezTerm* measures width 6.

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+0923 <https://codepoints.net/U+0923>`_  '\\u0923'  Lo                  1  DEVANAGARI LETTER NNA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
=========================================  =========  ==========  =========  ========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xb0\xe0\xa4\xa3\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe\xe0\xa4\xb0\xe0\xa5\x8d\xe2\x80\x8d\xe0\xa4\xaf\xe0\xa4\xbe|\\n12345|\\n"
        करण्यार्‍या|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5, 
  while *WezTerm* measures width 6.

Nepali
^^^^^^

Sequence of language *Nepali* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
`U+0941 <https://codepoints.net/U+0941>`_  '\\u0941'  Mn                  0  DEVANAGARI VOWEL SIGN U
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0907 <https://codepoints.net/U+0907>`_  '\\u0907'  Lo                  1  DEVANAGARI LETTER I
`U+090F <https://codepoints.net/U+090F>`_  '\\u090f'  Lo                  1  DEVANAGARI LETTER E
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
`U+094B <https://codepoints.net/U+094B>`_  '\\u094b'  Mc                  0  DEVANAGARI VOWEL SIGN O
=========================================  =========  ==========  =========  ========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xaa\xe0\xa5\x81\xe0\xa4\xb0\xe0\xa5\x8d\xe2\x80\x8d\xe0\xa4\xaf\xe0\xa4\xbe\xe0\xa4\x87\xe0\xa4\x8f\xe0\xa4\x95\xe0\xa5\x8b|\\n12345|\\n"
        पुर्‍याइएको|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5, 
  while *WezTerm* measures width 6.

Bengali
^^^^^^^

Sequence of language *Bengali* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+0989 <https://codepoints.net/U+0989>`_  '\\u0989'  Lo                  1  BENGALI LETTER U
`U+09A4 <https://codepoints.net/U+09A4>`_  '\\u09a4'  Lo                  1  BENGALI LETTER TA
`U+09CD <https://codepoints.net/U+09CD>`_  '\\u09cd'  Mn                  0  BENGALI SIGN VIRAMA
`U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
`U+09AA <https://codepoints.net/U+09AA>`_  '\\u09aa'  Lo                  1  BENGALI LETTER PA
`U+09C0 <https://codepoints.net/U+09C0>`_  '\\u09c0'  Mc                  0  BENGALI VOWEL SIGN II
`U+09A1 <https://codepoints.net/U+09A1>`_  '\\u09a1'  Lo                  1  BENGALI LETTER DDA
`U+09BC <https://codepoints.net/U+09BC>`_  '\\u09bc'  Mn                  0  BENGALI SIGN NUKTA
`U+09A8 <https://codepoints.net/U+09A8>`_  '\\u09a8'  Lo                  1  BENGALI LETTER NA
`U+09C7 <https://codepoints.net/U+09C7>`_  '\\u09c7'  Mc                  0  BENGALI VOWEL SIGN E
`U+09B0 <https://codepoints.net/U+09B0>`_  '\\u09b0'  Lo                  1  BENGALI LETTER RA
=========================================  =========  ==========  =========  =====================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\x89\xe0\xa6\xa4\xe0\xa7\x8d\xe2\x80\x8d\xe0\xa6\xaa\xe0\xa7\x80\xe0\xa6\xa1\xe0\xa6\xbc\xe0\xa6\xa8\xe0\xa7\x87\xe0\xa6\xb0|\\n12345|\\n"
        উত্‍পীড়নের|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5, 
  while *WezTerm* measures width 6.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
