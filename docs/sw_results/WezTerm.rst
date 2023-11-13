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
'5.1.0'             1         26  96.2%
'5.2.0'            88        269  67.3%
'6.0.0'             0         13  100.0%
'9.0.0'           250       5000  95.0%
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

None

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

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9f\x8c\xa5\xef\xb8\x8f|\\n12|\\n"
        🌥️|
        12|

- python `wcwidth.wcswidth()`_ measures width 2, 
  while *WezTerm* measures width 1.


.. _WezTermlang:

Language Support
++++++++++++++++

The following 111 languages were tested with 100% success:

Adyghe, Aja, Amarakaeri, Arabic, Standard, Assyrian Neo-Aramaic, Azerbaijani, North (Latin), Baatonum, Bamun, Belarusan, Bhojpuri, Bora, Burmese, Cashinahua, Chakma, Cherokee (cased), Chickasaw, Chinantec, Chiltepec, Chinese, Yue, Crimean Tatar, Crioulo, Upper Guinea (008), Dagaare, Southern, Dangme, Dari, Dendi, Dinka, Northeastern, Ditammari, Dzongkha, Evenki, Farsi, Western, Fon, Fur, Ga, Garifuna, Gilyak, Gujarati, Gumuz, Hausa, Hindi, Hmong Njua, Hmong, Northern Qiandong, Icelandic, Idoma, Javanese (Javanese), Kabardian, Kannada, Khmer, Central, Khün, Ladino, Lamnso', Lao, Latin (1), Lingala (tones), Magahi, Maithili, Mazahua Central, Mixtec, Metlatónoc, Mon, Mongolian, Halh (Mongolian), Montenegrin, Mòoré, Nanai, Navajo, Nuosu, Orok, Otomi, Mezquital, Panjabi, Eastern, Panjabi, Western, Pashto, Northern, Picard, Pular, Quechua, Ayacucho, Quechua, Cajamarca, Quechua, Cusco, Romansch (Surmiran), Rundi, Secoya, Seraiki, Serer-Sine, Shan, Siona, Sorbian, Upper, South Azerbaijani, Swati, Tagalog (Tagalog), Tai Dam, Tamang, Eastern, Tamazight, Central Atlas, Tamazight, Central Atlas (Tifinagh), Tamazight, Standard Morocan, Tamil, Tamil (Sri Lanka), Telugu, Tem, Thai, Thai (2), Tibetan, Central, Ticuna, Uduk, Urdu, Urdu (2), Uzbek, Northern (Cyrillic), Vai, Veps, Vietnamese, Vietnamese (Han nom), Waama, Yaneshaʼ, Yiddish, Eastern, Yoruba, Yukaghir, Northern, Éwé.

The following 21 languages are not fully supported:

=====================  ==========  =========  =============
lang                     n_errors    n_total    pct_success
=====================  ==========  =========  =============
Bulgarian                     500        525        4.7619
Purepecha                     500        529        5.48204
Sukuma                        500        533        6.19137
Walloon                       500        545        8.25688
Cree, Swampy                  500        547        8.59232
Greek (polytonic)             500        550        9.09091
Seselwa Creole French         500        569       12.1265
Gen                           500        574       12.892
(Yeonbyeon)                   500        596       16.1074
Pular (Adlam)                 500        770       35.0649
Sanskrit                      500        781       35.9795
Sanskrit (Grantha)            500        893       44.009
Achuar-Shiwiar (1)            268       1242       78.4219
(Bizisa)                      268       1545       82.6537
Maldivian                     139       1917       92.7491
Malayalam                     109       1630       93.3129
Sinhala                       107       1655       93.5347
Pijin                          31       1784       98.2623
Marathi                         5       1614       99.6902
Nepali                          3       1385       99.7834
Bengali                         3       1413       99.7877
=====================  ==========  =========  =============

Bulgarian
^^^^^^^^^

Sequence of language *Bulgarian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =============================
`U+0412 <https://codepoints.net/U+0412>`_  '\\u0412'  Lu                  1  CYRILLIC CAPITAL LETTER VE
`U+0421 <https://codepoints.net/U+0421>`_  '\\u0421'  Lu                  1  CYRILLIC CAPITAL LETTER ES
`U+0415 <https://codepoints.net/U+0415>`_  '\\u0415'  Lu                  1  CYRILLIC CAPITAL LETTER IE
`U+041E <https://codepoints.net/U+041E>`_  '\\u041e'  Lu                  1  CYRILLIC CAPITAL LETTER O
`U+0411 <https://codepoints.net/U+0411>`_  '\\u0411'  Lu                  1  CYRILLIC CAPITAL LETTER BE
`U+0429 <https://codepoints.net/U+0429>`_  '\\u0429'  Lu                  1  CYRILLIC CAPITAL LETTER SHCHA
`U+0410 <https://codepoints.net/U+0410>`_  '\\u0410'  Lu                  1  CYRILLIC CAPITAL LETTER A
=========================================  =========  ==========  =========  =============================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\x92\xd0\xa1\xd0\x95\xd0\x9e\xd0\x91\xd0\xa9\xd0\x90|\\n1234567|\\n"
        ВСЕОБЩА|
        1234567|

- Cursor Y-Position moved 19 rows where no movement is expected.

Purepecha
^^^^^^^^^

Sequence of language *Purepecha* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0055 <https://codepoints.net/U+0055>`_  'U'       Lu                  1  LATIN CAPITAL LETTER U
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+004E <https://codepoints.net/U+004E>`_  'N'       Lu                  1  LATIN CAPITAL LETTER N
`U+0044 <https://codepoints.net/U+0044>`_  'D'       Lu                  1  LATIN CAPITAL LETTER D
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+004B <https://codepoints.net/U+004B>`_  'K'       Lu                  1  LATIN CAPITAL LETTER K
`U+0055 <https://codepoints.net/U+0055>`_  'U'       Lu                  1  LATIN CAPITAL LETTER U
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
=========================================  ========  ==========  =========  ======================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "UANDAKUA|\\n12345678|\\n"
        UANDAKUA|
        12345678|

- Cursor Y-Position moved 19 rows where no movement is expected.

Sukuma
^^^^^^

Sequence of language *Sukuma* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
`U+004C <https://codepoints.net/U+004C>`_  'L'       Lu                  1  LATIN CAPITAL LETTER L
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+004B <https://codepoints.net/U+004B>`_  'K'       Lu                  1  LATIN CAPITAL LETTER K
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
=========================================  ========  ==========  =========  ======================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ILAKA|\\n12345|\\n"
        ILAKA|
        12345|

- Cursor Y-Position moved 19 rows where no movement is expected.

Walloon
^^^^^^^

Sequence of language *Walloon* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================================
`U+0044 <https://codepoints.net/U+0044>`_  'D'       Lu                  1  LATIN CAPITAL LETTER D
`U+00C9 <https://codepoints.net/U+00C9>`_  '\\xc9'   Lu                  1  LATIN CAPITAL LETTER E WITH ACUTE
`U+0043 <https://codepoints.net/U+0043>`_  'C'       Lu                  1  LATIN CAPITAL LETTER C
`U+004C <https://codepoints.net/U+004C>`_  'L'       Lu                  1  LATIN CAPITAL LETTER L
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+0052 <https://codepoints.net/U+0052>`_  'R'       Lu                  1  LATIN CAPITAL LETTER R
`U+00C5 <https://codepoints.net/U+00C5>`_  '\\xc5'   Lu                  1  LATIN CAPITAL LETTER A WITH RING ABOVE
`U+0043 <https://codepoints.net/U+0043>`_  'C'       Lu                  1  LATIN CAPITAL LETTER C
`U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
`U+004F <https://codepoints.net/U+004F>`_  'O'       Lu                  1  LATIN CAPITAL LETTER O
`U+004E <https://codepoints.net/U+004E>`_  'N'       Lu                  1  LATIN CAPITAL LETTER N
=========================================  ========  ==========  =========  ======================================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "D\xc3\x89CLAR\xc3\x85CION|\\n12345678901|\\n"
        DÉCLARÅCION|
        12345678901|

- Cursor Y-Position moved 19 rows where no movement is expected.

Cree, Swampy
^^^^^^^^^^^^

Sequence of language *Cree, Swampy* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================================
`U+1401 <https://codepoints.net/U+1401>`_  '\\u1401'  Lo                  1  CANADIAN SYLLABICS E
`U+1422 <https://codepoints.net/U+1422>`_  '\\u1422'  Lo                  1  CANADIAN SYLLABICS FINAL TOP HALF RING
`U+1431 <https://codepoints.net/U+1431>`_  '\\u1431'  Lo                  1  CANADIAN SYLLABICS PI
`U+1455 <https://codepoints.net/U+1455>`_  '\\u1455'  Lo                  1  CANADIAN SYLLABICS TA
`U+1422 <https://codepoints.net/U+1422>`_  '\\u1422'  Lo                  1  CANADIAN SYLLABICS FINAL TOP HALF RING
`U+1472 <https://codepoints.net/U+1472>`_  '\\u1472'  Lo                  1  CANADIAN SYLLABICS KA
`U+14A5 <https://codepoints.net/U+14A5>`_  '\\u14a5'  Lo                  1  CANADIAN SYLLABICS MI
`U+1472 <https://codepoints.net/U+1472>`_  '\\u1472'  Lo                  1  CANADIAN SYLLABICS KA
`U+1420 <https://codepoints.net/U+1420>`_  '\\u1420'  Lo                  1  CANADIAN SYLLABICS FINAL GRAVE
=========================================  =========  ==========  =========  ======================================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x90\x81\xe1\x90\xa2\xe1\x90\xb1\xe1\x91\x95\xe1\x90\xa2\xe1\x91\xb2\xe1\x92\xa5\xe1\x91\xb2\xe1\x90\xa0|\\n123456789|\\n"
        ᐁᐢᐱᑕᐢᑲᒥᑲᐠ|
        123456789|

- Cursor Y-Position moved 19 rows where no movement is expected.

Greek (polytonic)
^^^^^^^^^^^^^^^^^

Sequence of language *Greek (polytonic)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ============================
`U+039F <https://codepoints.net/U+039F>`_  '\\u039f'  Lu                  1  GREEK CAPITAL LETTER OMICRON
`U+0399 <https://codepoints.net/U+0399>`_  '\\u0399'  Lu                  1  GREEK CAPITAL LETTER IOTA
`U+039A <https://codepoints.net/U+039A>`_  '\\u039a'  Lu                  1  GREEK CAPITAL LETTER KAPPA
`U+039F <https://codepoints.net/U+039F>`_  '\\u039f'  Lu                  1  GREEK CAPITAL LETTER OMICRON
`U+03A5 <https://codepoints.net/U+03A5>`_  '\\u03a5'  Lu                  1  GREEK CAPITAL LETTER UPSILON
`U+039C <https://codepoints.net/U+039C>`_  '\\u039c'  Lu                  1  GREEK CAPITAL LETTER MU
`U+0395 <https://codepoints.net/U+0395>`_  '\\u0395'  Lu                  1  GREEK CAPITAL LETTER EPSILON
`U+039D <https://codepoints.net/U+039D>`_  '\\u039d'  Lu                  1  GREEK CAPITAL LETTER NU
`U+0399 <https://codepoints.net/U+0399>`_  '\\u0399'  Lu                  1  GREEK CAPITAL LETTER IOTA
`U+039A <https://codepoints.net/U+039A>`_  '\\u039a'  Lu                  1  GREEK CAPITAL LETTER KAPPA
`U+0397 <https://codepoints.net/U+0397>`_  '\\u0397'  Lu                  1  GREEK CAPITAL LETTER ETA
=========================================  =========  ==========  =========  ============================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xce\x9f\xce\x99\xce\x9a\xce\x9f\xce\xa5\xce\x9c\xce\x95\xce\x9d\xce\x99\xce\x9a\xce\x97|\\n12345678901|\\n"
        ΟΙΚΟΥΜΕΝΙΚΗ|
        12345678901|

- Cursor Y-Position moved 5 rows where no movement is expected.

Seselwa Creole French
^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Seselwa Creole French* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0044 <https://codepoints.net/U+0044>`_  'D'       Lu                  1  LATIN CAPITAL LETTER D
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ======================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Deklarasyon|\\n12345678901|\\n"
        Deklarasyon|
        12345678901|

- Cursor Y-Position moved 19 rows where no movement is expected.

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0058 <https://codepoints.net/U+0058>`_  'X'       Lu                  1  LATIN CAPITAL LETTER X
`U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
`U+0058 <https://codepoints.net/U+0058>`_  'X'       Lu                  1  LATIN CAPITAL LETTER X
`U+0045 <https://codepoints.net/U+0045>`_  'E'       Lu                  1  LATIN CAPITAL LETTER E
=========================================  ========  ==========  =========  ======================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "XIXE|\\n1234|\\n"
        XIXE|
        1234|

- Cursor Y-Position moved 19 rows where no movement is expected.

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+C138 <https://codepoints.net/U+C138>`_  '\\uc138'  Lo                  2  HANGUL SYLLABLE SE
`U+ACC4 <https://codepoints.net/U+ACC4>`_  '\\uacc4'  Lo                  2  HANGUL SYLLABLE GYE
`U+C778 <https://codepoints.net/U+C778>`_  '\\uc778'  Lo                  2  HANGUL SYLLABLE IN
`U+AD8C <https://codepoints.net/U+AD8C>`_  '\\uad8c'  Lo                  2  HANGUL SYLLABLE GWEON
`U+C120 <https://codepoints.net/U+C120>`_  '\\uc120'  Lo                  2  HANGUL SYLLABLE SEON
`U+C5B8 <https://codepoints.net/U+C5B8>`_  '\\uc5b8'  Lo                  2  HANGUL SYLLABLE EON
=========================================  =========  ==========  =========  =====================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x84\xb8\xea\xb3\x84\xec\x9d\xb8\xea\xb6\x8c\xec\x84\xa0\xec\x96\xb8|\\n123456789012|\\n"
        세계인권선언|
        123456789012|

- Cursor Y-Position moved 19 rows where no movement is expected.

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =======================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =======================
`U+0001E938 <https://codepoints.net/U+0001E938>`_  '\\U0001e938'  Ll                  1  ADLAM SMALL LETTER HA
`U+0001E922 <https://codepoints.net/U+0001E922>`_  '\\U0001e922'  Ll                  1  ADLAM SMALL LETTER ALIF
`U+0001E933 <https://codepoints.net/U+0001E933>`_  '\\U0001e933'  Ll                  1  ADLAM SMALL LETTER KAF
`U+0001E946 <https://codepoints.net/U+0001E946>`_  '\\U0001e946'  Mn                  0  ADLAM GEMINATION MARK
`U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
`U+0001E945 <https://codepoints.net/U+0001E945>`_  '\\U0001e945'  Mn                  0  ADLAM VOWEL LENGTHENER
`U+0001E936 <https://codepoints.net/U+0001E936>`_  '\\U0001e936'  Ll                  1  ADLAM SMALL LETTER JIIM
`U+0001E92D <https://codepoints.net/U+0001E92D>`_  '\\U0001e92d'  Ll                  1  ADLAM SMALL LETTER I
=================================================  =============  ==========  =========  =======================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xb8\xf0\x9e\xa4\xa2\xf0\x9e\xa4\xb3\xf0\x9e\xa5\x86\xf0\x9e\xa4\xab\xf0\x9e\xa5\x85\xf0\x9e\xa4\xb6\xf0\x9e\xa4\xad|\\n123456|\\n"
        𞤸𞤢𞤳𞥆𞤫𞥅𞤶𞤭|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6, 
  while *WezTerm* measures width -1.

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0906 <https://codepoints.net/U+0906>`_  '\\u0906'  Lo                  1  DEVANAGARI LETTER AA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+0936 <https://codepoints.net/U+0936>`_  '\\u0936'  Lo                  1  DEVANAGARI LETTER SHA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+0947 <https://codepoints.net/U+0947>`_  '\\u0947'  Mn                  0  DEVANAGARI VOWEL SIGN E
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+002D <https://codepoints.net/U+002D>`_  '-'        Pd                  1  HYPHEN-MINUS
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
=========================================  =========  ==========  =========  ========================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x86\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xae\xe0\xa4\xaa\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa4\xb6\xe0\xa4\xbe\xe0\xa4\xb8\xe0\xa4\xa8\xe0\xa5\x87\xe0\xa4\xa4\xe0\xa4\xb0-\xe0\xa4\xa4\xe0\xa4\xa8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xaf|\\n12345678901234567|\\n"
        आत्मप्रशासनेतर-तन्त्रस्य|
        12345678901234567|

- python `wcwidth.wcswidth()`_ measures width 17, 
  while *WezTerm* measures width -1.

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ====================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ====================
`U+0001131C <https://codepoints.net/U+0001131C>`_  '\\U0001131c'  Lo                  1  GRANTHA LETTER JA
`U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
`U+00011303 <https://codepoints.net/U+00011303>`_  '\\U00011303'  Mc                  0  GRANTHA SIGN VISARGA
=================================================  =============  ==========  =========  ====================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\x9c\xf0\x91\x8c\xa8\xf0\x91\x8c\x83|\\n12|\\n"
        𑌜𑌨𑌃|
        12|

- python `wcwidth.wcswidth()`_ measures width 2, 
  while *WezTerm* measures width -1.

Achuar-Shiwiar (1)
^^^^^^^^^^^^^^^^^^

Sequence of language *Achuar-Shiwiar (1)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+004D <https://codepoints.net/U+004D>`_  'M'       Lu                  1  LATIN CAPITAL LETTER M
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+0053 <https://codepoints.net/U+0053>`_  'S'       Lu                  1  LATIN CAPITAL LETTER S
`U+0048 <https://codepoints.net/U+0048>`_  'H'       Lu                  1  LATIN CAPITAL LETTER H
=========================================  ========  ==========  =========  ======================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "MASH|\\n1234|\\n"
        MASH|
        1234|

- Cursor Y-Position moved 19 rows where no movement is expected.

(Bizisa)
^^^^^^^^

Sequence of language *(Bizisa)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0053 <https://codepoints.net/U+0053>`_  'S'       Lu                  1  LATIN CAPITAL LETTER S
`U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
`U+0046 <https://codepoints.net/U+0046>`_  'F'       Lu                  1  LATIN CAPITAL LETTER F
`U+0047 <https://codepoints.net/U+0047>`_  'G'       Lu                  1  LATIN CAPITAL LETTER G
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
`U+0046 <https://codepoints.net/U+0046>`_  'F'       Lu                  1  LATIN CAPITAL LETTER F
=========================================  ========  ==========  =========  ======================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "SIFGAIF|\\n1234567|\\n"
        SIFGAIF|
        1234567|

- Cursor Y-Position moved 19 rows where no movement is expected.

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0799 <https://codepoints.net/U+0799>`_  '\\u0799'  Lo                  1  THAANA LETTER HHAA
`U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
`U+0783 <https://codepoints.net/U+0783>`_  '\\u0783'  Lo                  1  THAANA LETTER RAA
`U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
`U+0789 <https://codepoints.net/U+0789>`_  '\\u0789'  Lo                  1  THAANA LETTER MEEMU
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
`U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
=========================================  =========  ==========  =========  ===================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x99\xde\xaa\xde\x83\xde\xaa\xde\x89\xde\xa6\xde\x8c\xde\xb0|\\n1234|\\n"
        ޙުރުމަތް|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4, 
  while *WezTerm* measures width -1.

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

None

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

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb6\xb4\xe0\xb7\x8a\xe2\x80\x8d\xe0\xb6\xbb\xe0\xb6\x9a\xe0\xb7\x8f\xe0\xb7\x81\xe0\xb6\xb1\xe0\xb6\xba|\\n12345|\\n"
        ප්‍රකාශනය|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5, 
  while *WezTerm* measures width 6.

Pijin
^^^^^

Sequence of language *Pijin* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0055 <https://codepoints.net/U+0055>`_  'U'       Lu                  1  LATIN CAPITAL LETTER U
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
=========================================  ========  ==========  =========  ======================

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Universol|\\n123456789|\\n"
        Universol|
        123456789|

- Cursor Y-Position moved 19 rows where no movement is expected.

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

None

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

None

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

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\x89\xe0\xa6\xa4\xe0\xa7\x8d\xe2\x80\x8d\xe0\xa6\xaa\xe0\xa7\x80\xe0\xa6\xa1\xe0\xa6\xbc\xe0\xa6\xa8\xe0\xa7\x87\xe0\xa6\xb0|\\n12345|\\n"
        উত্‍পীড়নের|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5, 
  while *WezTerm* measures width 6.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
