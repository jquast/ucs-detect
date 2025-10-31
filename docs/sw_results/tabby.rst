.. _tabby:

tabby
-----


Tested Software version 1.0.228 on Darwin
Full results available at ucs-detect_ repository path
`data/macos-tabby-1.0.228-no-emit.yaml <https://github.com/jquast/ucs-detect/blob/master/data/macos-tabby-1.0.228-no-emit.yaml>`_

.. _tabbyscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *tabby*:

============  ===========  ==============  ======================================================
Score Type    Raw Score    Scaled Score    Calculation
============  ===========  ==============  ======================================================
WIDE          36.36%       4.8%            (version_index / total_versions) × (pct_success / 100)
ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
LANG          1.68%        1.7%            languages_supported / total_languages
VS16          0.00%        0.0%            pct_success / 100
VS15          0.00%        0.0%            pct_success / 100
============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 7.61%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15) / 5
  the categorized 'average' absolute support level of this terminal

- Scaled Final Score: 0.0%
  (normalized across all terminals tested).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _tabbywide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for tabby appears to be 
**12.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total  pct_success
=========  ==========  =========  =============
'9.0.0'             0       5000  100.0%
'10.0.0'            0        745  100.0%
'11.0.0'            0         72  100.0%
'12.0.0'            0         76  100.0%
'12.1.0'            0          1  100.0%
'13.0.0'          552        552  0.0%
'14.0.0'           54         54  0.0%
'15.0.0'           22         22  0.0%
'15.1.0'            5          5  0.0%
'16.0.0'          198        198  0.0%
'17.0.0'          157        157  0.0%
=========  ==========  =========  =============

Sequence of a WIDE character from Unicode Version 17.0.0, from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ======
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ======
`U+00018DAB <https://codepoints.net/U+00018DAB>`_  '\\U00018dab'  Cn                  2  na
=================================================  =============  ==========  =========  ======

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x98\xb6\xab|\\n12|\\n"
        𘶫|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width 1.

.. _tabbyzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *tabby* appears to be 
**None**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total  pct_success
=========  ==========  =========  =============
'2.0'              21         22  4.5%
'4.0'             571        579  1.4%
'5.0'             100        100  0.0%
'11.0'             73         73  0.0%
'12.0'            112        112  0.0%
'12.1'            165        165  0.0%
'13.0'             50         51  2.0%
'13.1'             83         83  0.0%
'14.0'             20         20  0.0%
'15.0'              1          1  0.0%
'15.1'            109        109  0.0%
'17.0'            130        130  0.0%
=========  ==========  =========  =============

Sequence of an Emoji ZWJ Sequence from Emoji Version 17.0, from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =================================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =================================
`U+0001F469 <https://codepoints.net/U+0001F469>`_  '\\U0001f469'  So                  2  WOMAN
`U+0001F3FE <https://codepoints.net/U+0001F3FE>`_  '\\U0001f3fe'  Sk                  0  EMOJI MODIFIER FITZPATRICK TYPE-5
`U+200D <https://codepoints.net/U+200D>`_          '\\u200d'      Cf                  0  ZERO WIDTH JOINER
`U+0001FAEF <https://codepoints.net/U+0001FAEF>`_  '\\U0001faef'  Cn                  2  na
`U+200D <https://codepoints.net/U+200D>`_          '\\u200d'      Cf                  0  ZERO WIDTH JOINER
`U+0001F469 <https://codepoints.net/U+0001F469>`_  '\\U0001f469'  So                  2  WOMAN
`U+0001F3FF <https://codepoints.net/U+0001F3FF>`_  '\\U0001f3ff'  Sk                  0  EMOJI MODIFIER FITZPATRICK TYPE-6
=================================================  =============  ==========  =========  =================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9f\x91\xa9\xf0\x9f\x8f\xbe\xe2\x80\x8d\xf0\x9f\xab\xaf\xe2\x80\x8d\xf0\x9f\x91\xa9\xf0\x9f\x8f\xbf|\\n12|\\n"
        👩🏾‍🫯‍👩🏿|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width 9.

.. _tabbyvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *tabby* is 213 errors
out of 213 total codepoints tested, 0.0% success.
Sequence of a NARROW Emoji made WIDE by *Variation Selector-16*, from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+2733 <https://codepoints.net/U+2733>`_  '\\u2733'  So                  1  EIGHT SPOKED ASTERISK
`U+FE0F <https://codepoints.net/U+FE0F>`_  '\\ufe0f'  Mn                  0  VARIATION SELECTOR-16
=========================================  =========  ==========  =========  =====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe2\x9c\xb3\xef\xb8\x8f|\\n12|\\n"
        ✳️|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width 1.


.. _tabbyvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *tabby* are not available.

.. _tabbylang:

Language Support
++++++++++++++++

The following 2 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog).

The following 117 languages are not fully supported:

===============================  ==========  =========  =============
lang                               n_errors    n_total  pct_success
===============================  ==========  =========  =============
Javanese (Javanese)                    1000       1020  2.0%
Shan                                    868        915  5.1%
Tamil (Sri Lanka)                      1000       1074  6.9%
Tamil                                  1000       1075  7.0%
Sanskrit (Grantha)                      894       1006  11.1%
Malayalam                              1000       1156  13.5%
Bengali                                1000       1166  14.2%
Khmer, Central                          448        528  15.2%
Kannada                                 903       1080  16.4%
Khün                                    361        442  18.3%
Burmese                                 976       1223  20.2%
Sanskrit                                754       1000  24.6%
Tamang, Eastern                          33         45  26.7%
Mon                                     677        946  28.4%
Marathi                                1000       1419  29.5%
Nepali                                  931       1385  32.8%
Gujarati                               1000       1518  34.1%
Telugu                                  715       1129  36.7%
Maithili                                953       1519  37.3%
Hindi                                  1000       1631  38.7%
Panjabi, Eastern                       1000       1834  45.5%
Sinhala                                 887       1655  46.4%
Bhojpuri                                878       1737  49.5%
Magahi                                  810       1716  52.8%
Chakma                                  495       1444  65.7%
Tibetan, Central                          5        280  98.2%
Vietnamese (Han nom)                      2        199  99.0%
Japanese                                  3        299  99.0%
Japanese (Osaka)                          3        308  99.0%
Thai (2)                                  3        313  99.0%
Chinese, Mandarin (Harbin)                2        210  99.0%
Chinese, Mandarin (Traditional)           2        210  99.0%
Chinese, Yue                              2        210  99.0%
(Jinan)                                   2        211  99.1%
Chinese, Gan                              2        211  99.1%
Chinese, Mandarin (Guiyang)               2        211  99.1%
Chinese, Wu                               2        211  99.1%
Chinese, Hakka                            2        212  99.1%
Chinese, Jinyu                            2        212  99.1%
Chinese, Mandarin (Beijing)               2        212  99.1%
Chinese, Mandarin (Nanjing)               2        212  99.1%
Chinese, Mandarin (Tianjin)               2        212  99.1%
Chinese, Min Nan                          2        212  99.1%
Chinese, Xiang                            2        212  99.1%
Chinese, Mandarin (Simplified)            2        225  99.1%
Thai                                      3        341  99.1%
Nuosu                                     2        230  99.1%
Dzongkha                                  3        359  99.2%
Lao                                       3        426  99.3%
Japanese (Tokyo)                          2        320  99.4%
Chickasaw                                 2        554  99.6%
Yaneshaʼ                                  8       2536  99.7%
Bora                                      5       1598  99.7%
Amarakaeri                                4       1446  99.7%
Shipibo-Conibo                            7       2540  99.7%
Navajo                                    4       1600  99.8%
Nanai                                     3       1207  99.8%
Orok                                      3       1245  99.8%
Colorado                                  3       1263  99.8%
Gumuz                                     3       1283  99.8%
Veps                                      3       1323  99.8%
Evenki                                    2        899  99.8%
South Azerbaijani                         3       1396  99.8%
Secoya                                    3       1409  99.8%
Catalan (2)                               4       1909  99.8%
Mirandese                                 4       1966  99.8%
Siona                                     3       1492  99.8%
Gilyak                                    3       1504  99.8%
Picard                                    4       2024  99.8%
Ticuna                                    4       2048  99.8%
(Yeonbyeon)                               2       1061  99.8%
Pular (Adlam)                             3       1613  99.8%
Tem                                       3       1659  99.8%
Éwé                                       4       2230  99.8%
Gen                                       4       2309  99.8%
Assyrian Neo-Aramaic                      2       1160  99.8%
Yiddish, Eastern                          3       1775  99.8%
Saint Lucian Creole French                3       1777  99.8%
Korean                                    2       1185  99.8%
Maori (2)                                 4       2385  99.8%
Kabyle                                    3       1815  99.8%
Lingala (tones)                           3       1818  99.8%
Farsi, Western                            3       1822  99.8%
Tamazight, Central Atlas                  3       1822  99.8%
Fur                                       3       1838  99.8%
Yoruba                                    4       2454  99.8%
Dari                                      3       1872  99.8%
Vietnamese                                4       2502  99.8%
Ditammari                                 3       1882  99.8%
Maldivian                                 3       1918  99.8%
French (Welche)                           3       1928  99.8%
Dagaare, Southern                         4       2582  99.8%
Baatonum                                  3       1939  99.8%
Uduk                                      5       3247  99.8%
Arabic, Standard                          2       1348  99.9%
Ga                                        3       2039  99.9%
Mixtec, Metlatónoc                        2       1367  99.9%
Aja                                       3       2061  99.9%
Lamnso'                                   3       2237  99.9%
Urdu                                      3       2237  99.9%
Pashto, Northern                          3       2242  99.9%
Seraiki                                   3       2242  99.9%
Belanda Viri                              3       2246  99.9%
Urdu (2)                                  3       2251  99.9%
Bamun                                     3       2285  99.9%
Dinka, Northeastern                       2       1529  99.9%
Dendi                                     2       1569  99.9%
Mazahua Central                           2       1574  99.9%
Serer-Sine                                2       1596  99.9%
Panjabi, Western                          3       2419  99.9%
Mòoré                                     3       2447  99.9%
Fon                                       3       2520  99.9%
Chinantec, Chiltepec                      2       1729  99.9%
Otomi, Mezquital                          2       1849  99.9%
Dangme                                    3       2912  99.9%
Waama                                     1       1000  99.9%
Tai Dam                                   2       2386  99.9%
===============================  ==========  =========  =============

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+A9B2 <https://codepoints.net/U+A9B2>`_  '\\ua9b2'  Lo                  1  JAVANESE LETTER HA
`U+A9B8 <https://codepoints.net/U+A9B8>`_  '\\ua9b8'  Mn                  0  JAVANESE VOWEL SIGN SUKU
`U+A9A9 <https://codepoints.net/U+A9A9>`_  '\\ua9a9'  Lo                  1  JAVANESE LETTER MA
`U+A9A0 <https://codepoints.net/U+A9A0>`_  '\\ua9a0'  Lo                  1  JAVANESE LETTER TA
=========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0|\\n123|\\n"
        ꦲꦸꦩꦠ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+1075 <https://codepoints.net/U+1075>`_  '\\u1075'  Lo                  1  MYANMAR LETTER SHAN KA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1088 <https://codepoints.net/U+1088>`_  '\\u1088'  Mc                  0  MYANMAR SIGN SHAN TONE-3
`U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+107D <https://codepoints.net/U+107D>`_  '\\u107d'  Lo                  1  MYANMAR LETTER SHAN PHA
`U+1062 <https://codepoints.net/U+1062>`_  '\\u1062'  Mc                  0  MYANMAR VOWEL SIGN SGAW KAREN EU
`U+101D <https://codepoints.net/U+101D>`_  '\\u101d'  Lo                  1  MYANMAR LETTER WA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1087 <https://codepoints.net/U+1087>`_  '\\u1087'  Mc                  0  MYANMAR SIGN SHAN TONE-2
=========================================  =========  ==========  =========  ================================

Total codepoints: 15


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x9c\xe1\x80\xad\xe1\x81\xb5\xe1\x80\xba\xe1\x82\x88\xe1\x80\x95\xe1\x80\xad\xe1\x80\xaf\xe1\x81\xbc\xe1\x80\xba\xe1\x81\xbd\xe1\x81\xa2\xe1\x80\x9d\xe1\x80\xba\xe1\x82\x87|\\n123456|\\n"
        လိၵ်ႈပိုၼ်ၽၢဝ်ႇ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 9.

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
`U+0BA9 <https://codepoints.net/U+0BA9>`_  '\\u0ba9'  Lo                  1  TAMIL LETTER NNNA
`U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
=========================================  =========  ==========  =========  ==================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
        மனித|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
`U+0BA9 <https://codepoints.net/U+0BA9>`_  '\\u0ba9'  Lo                  1  TAMIL LETTER NNNA
`U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
=========================================  =========  ==========  =========  ==================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
        மனித|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =====================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =====================
`U+0001132E <https://codepoints.net/U+0001132E>`_  '\\U0001132e'  Lo                  1  GRANTHA LETTER MA
`U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
`U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
`U+00011335 <https://codepoints.net/U+00011335>`_  '\\U00011335'  Lo                  1  GRANTHA LETTER VA
`U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
`U+00011327 <https://codepoints.net/U+00011327>`_  '\\U00011327'  Lo                  1  GRANTHA LETTER DHA
`U+0001133F <https://codepoints.net/U+0001133F>`_  '\\U0001133f'  Mc                  0  GRANTHA VOWEL SIGN I
`U+00011315 <https://codepoints.net/U+00011315>`_  '\\U00011315'  Lo                  1  GRANTHA LETTER KA
`U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
`U+00011330 <https://codepoints.net/U+00011330>`_  '\\U00011330'  Lo                  1  GRANTHA LETTER RA
`U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
`U+00011323 <https://codepoints.net/U+00011323>`_  '\\U00011323'  Lo                  1  GRANTHA LETTER NNA
`U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
`U+00011302 <https://codepoints.net/U+00011302>`_  '\\U00011302'  Mc                  0  GRANTHA SIGN ANUSVARA
=================================================  =============  ==========  =========  =====================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
        𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 14.

Malayalam
^^^^^^^^^

Sequence of language *Malayalam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0D2E <https://codepoints.net/U+0D2E>`_  '\\u0d2e'  Lo                  1  MALAYALAM LETTER MA
`U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
`U+0D41 <https://codepoints.net/U+0D41>`_  '\\u0d41'  Mn                  0  MALAYALAM VOWEL SIGN U
`U+0D37 <https://codepoints.net/U+0D37>`_  '\\u0d37'  Lo                  1  MALAYALAM LETTER SSA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D2F <https://codepoints.net/U+0D2F>`_  '\\u0d2f'  Lo                  1  MALAYALAM LETTER YA
`U+0D3E <https://codepoints.net/U+0D3E>`_  '\\u0d3e'  Mc                  0  MALAYALAM VOWEL SIGN AA
`U+0D35 <https://codepoints.net/U+0D35>`_  '\\u0d35'  Lo                  1  MALAYALAM LETTER VA
`U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
`U+0D3E <https://codepoints.net/U+0D3E>`_  '\\u0d3e'  Mc                  0  MALAYALAM VOWEL SIGN AA
`U+0D36 <https://codepoints.net/U+0D36>`_  '\\u0d36'  Lo                  1  MALAYALAM LETTER SHA
`U+0D19 <https://codepoints.net/U+0D19>`_  '\\u0d19'  Lo                  1  MALAYALAM LETTER NGA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D19 <https://codepoints.net/U+0D19>`_  '\\u0d19'  Lo                  1  MALAYALAM LETTER NGA
`U+0D33 <https://codepoints.net/U+0D33>`_  '\\u0d33'  Lo                  1  MALAYALAM LETTER LLA
`U+0D46 <https://codepoints.net/U+0D46>`_  '\\u0d46'  Mc                  0  MALAYALAM VOWEL SIGN E
`U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
`U+0D41 <https://codepoints.net/U+0D41>`_  '\\u0d41'  Mn                  0  MALAYALAM VOWEL SIGN U
`U+0D31 <https://codepoints.net/U+0D31>`_  '\\u0d31'  Lo                  1  MALAYALAM LETTER RRA
`U+0D3F <https://codepoints.net/U+0D3F>`_  '\\u0d3f'  Mc                  0  MALAYALAM VOWEL SIGN I
`U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
`U+0D41 <https://codepoints.net/U+0D41>`_  '\\u0d41'  Mn                  0  MALAYALAM VOWEL SIGN U
`U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
=========================================  =========  ==========  =========  =======================

Total codepoints: 29


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
        മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
        12345678901234567|

- python `wcwidth.wcswidth()`_ measures width 17,
  while *tabby* measures width 21.

Bengali
^^^^^^^

Sequence of language *Bengali* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+09AE <https://codepoints.net/U+09AE>`_  '\\u09ae'  Lo                  1  BENGALI LETTER MA
`U+09BE <https://codepoints.net/U+09BE>`_  '\\u09be'  Mc                  0  BENGALI VOWEL SIGN AA
`U+09A8 <https://codepoints.net/U+09A8>`_  '\\u09a8'  Lo                  1  BENGALI LETTER NA
`U+09AC <https://codepoints.net/U+09AC>`_  '\\u09ac'  Lo                  1  BENGALI LETTER BA
`U+09BE <https://codepoints.net/U+09BE>`_  '\\u09be'  Mc                  0  BENGALI VOWEL SIGN AA
`U+09A7 <https://codepoints.net/U+09A7>`_  '\\u09a7'  Lo                  1  BENGALI LETTER DHA
`U+09BF <https://codepoints.net/U+09BF>`_  '\\u09bf'  Mc                  0  BENGALI VOWEL SIGN I
`U+0995 <https://codepoints.net/U+0995>`_  '\\u0995'  Lo                  1  BENGALI LETTER KA
`U+09BE <https://codepoints.net/U+09BE>`_  '\\u09be'  Mc                  0  BENGALI VOWEL SIGN AA
`U+09B0 <https://codepoints.net/U+09B0>`_  '\\u09b0'  Lo                  1  BENGALI LETTER RA
`U+09C7 <https://codepoints.net/U+09C7>`_  '\\u09c7'  Mc                  0  BENGALI VOWEL SIGN E
`U+09B0 <https://codepoints.net/U+09B0>`_  '\\u09b0'  Lo                  1  BENGALI LETTER RA
=========================================  =========  ==========  =========  =====================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
        মানবাধিকারের|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 12.

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
`U+17C1 <https://codepoints.net/U+17C1>`_  '\\u17c1'  Mc                  0  KHMER VOWEL SIGN E
`U+1785 <https://codepoints.net/U+1785>`_  '\\u1785'  Lo                  1  KHMER LETTER CA
`U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
`U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
`U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
`U+17B8 <https://codepoints.net/U+17B8>`_  '\\u17b8'  Mn                  0  KHMER VOWEL SIGN II
`U+1794 <https://codepoints.net/U+1794>`_  '\\u1794'  Lo                  1  KHMER LETTER BA
`U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
`U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
`U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
`U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
`U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
`U+1787 <https://codepoints.net/U+1787>`_  '\\u1787'  Lo                  1  KHMER LETTER CO
`U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
`U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
`U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
`U+179B <https://codepoints.net/U+179B>`_  '\\u179b'  Lo                  1  KHMER LETTER LO
`U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
`U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
`U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
`U+17B8 <https://codepoints.net/U+17B8>`_  '\\u17b8'  Mn                  0  KHMER VOWEL SIGN II
`U+1796 <https://codepoints.net/U+1796>`_  '\\u1796'  Lo                  1  KHMER LETTER PO
`U+17B8 <https://codepoints.net/U+17B8>`_  '\\u17b8'  Mn                  0  KHMER VOWEL SIGN II
`U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
`U+17B7 <https://codepoints.net/U+17B7>`_  '\\u17b7'  Mn                  0  KHMER VOWEL SIGN I
`U+1791 <https://codepoints.net/U+1791>`_  '\\u1791'  Lo                  1  KHMER LETTER TO
`U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
`U+1792 <https://codepoints.net/U+1792>`_  '\\u1792'  Lo                  1  KHMER LETTER THO
`U+17B7 <https://codepoints.net/U+17B7>`_  '\\u17b7'  Mn                  0  KHMER VOWEL SIGN I
`U+1798 <https://codepoints.net/U+1798>`_  '\\u1798'  Lo                  1  KHMER LETTER MO
`U+1793 <https://codepoints.net/U+1793>`_  '\\u1793'  Lo                  1  KHMER LETTER NO
`U+17BB <https://codepoints.net/U+17BB>`_  '\\u17bb'  Mn                  0  KHMER VOWEL SIGN U
`U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
`U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
`U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
=========================================  =========  ==========  =========  ===================

Total codepoints: 36


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
        សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *tabby* measures width 25.

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+0CAE <https://codepoints.net/U+0CAE>`_  '\\u0cae'  Lo                  1  KANNADA LETTER MA
`U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
`U+0CA8 <https://codepoints.net/U+0CA8>`_  '\\u0ca8'  Lo                  1  KANNADA LETTER NA
`U+0CB5 <https://codepoints.net/U+0CB5>`_  '\\u0cb5'  Lo                  1  KANNADA LETTER VA
=========================================  =========  ==========  =========  =====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
        ಮಾನವ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
`U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
`U+1A65 <https://codepoints.net/U+1A65>`_  '\\u1a65'  Mn                  0  TAI THAM VOWEL SIGN I
`U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
`U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
`U+1A45 <https://codepoints.net/U+1A45>`_  '\\u1a45'  Lo                  1  TAI THAM LETTER WA
`U+1A64 <https://codepoints.net/U+1A64>`_  '\\u1a64'  Mc                  0  TAI THAM VOWEL SIGN TALL AA
`U+1A75 <https://codepoints.net/U+1A75>`_  '\\u1a75'  Mn                  0  TAI THAM SIGN TONE-1
`U+1A2F <https://codepoints.net/U+1A2F>`_  '\\u1a2f'  Lo                  1  TAI THAM LETTER DA
`U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
`U+1A45 <https://codepoints.net/U+1A45>`_  '\\u1a45'  Lo                  1  TAI THAM LETTER WA
`U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
`U+1A3F <https://codepoints.net/U+1A3F>`_  '\\u1a3f'  Lo                  1  TAI THAM LETTER LOW YA
`U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
`U+1A3E <https://codepoints.net/U+1A3E>`_  '\\u1a3e'  Lo                  1  TAI THAM LETTER MA
`U+1A36 <https://codepoints.net/U+1A36>`_  '\\u1a36'  Lo                  1  TAI THAM LETTER NA
`U+1A69 <https://codepoints.net/U+1A69>`_  '\\u1a69'  Mn                  0  TAI THAM VOWEL SIGN U
`U+1A54 <https://codepoints.net/U+1A54>`_  '\\u1a54'  Lo                  1  TAI THAM LETTER GREAT SA
`U+1A29 <https://codepoints.net/U+1A29>`_  '\\u1a29'  Lo                  1  TAI THAM LETTER LOW CA
`U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
`U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
`U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
=========================================  =========  ==========  =========  ===========================

Total codepoints: 22


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
        ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *tabby* measures width 15.

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
`U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
`U+103C <https://codepoints.net/U+103C>`_  '\\u103c'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL RA
`U+100A <https://codepoints.net/U+100A>`_  '\\u100a'  Lo                  1  MYANMAR LETTER NNYA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
`U+103C <https://codepoints.net/U+103C>`_  '\\u103c'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL RA
`U+100A <https://codepoints.net/U+100A>`_  '\\u100a'  Lo                  1  MYANMAR LETTER NNYA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1006 <https://codepoints.net/U+1006>`_  '\\u1006'  Lo                  1  MYANMAR LETTER CHA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+101B <https://codepoints.net/U+101B>`_  '\\u101b'  Lo                  1  MYANMAR LETTER RA
`U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
=========================================  =========  ==========  =========  ================================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
        အပြည်ပြည်ဆိုင်ရာ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 11.

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0927 <https://codepoints.net/U+0927>`_  '\\u0927'  Lo                  1  DEVANAGARI LETTER DHA
`U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0923 <https://codepoints.net/U+0923>`_  '\\u0923'  Lo                  1  DEVANAGARI LETTER NNA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
=========================================  =========  ==========  =========  ========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa7\xe0\xa4\xbf\xe0\xa4\x95\xe0\xa4\xbe\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xa3\xe0\xa4\xbe\xe0\xa4\x82|\\n1234567|\\n"
        मानवाधिकाराणां|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 13.

Tamang, Eastern
^^^^^^^^^^^^^^^

Sequence of language *Tamang, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0939 <https://codepoints.net/U+0939>`_  '\\u0939'  Lo                  1  DEVANAGARI LETTER HA
`U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+0947 <https://codepoints.net/U+0947>`_  '\\u0947'  Mn                  0  DEVANAGARI VOWEL SIGN E
=========================================  =========  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa5\x8d\xe0\xa4\xb9\xe0\xa5\x80\xe0\xa4\xb8\xe0\xa5\x87|\\n123|\\n"
        म्हीसे|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
`U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
`U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
`U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
`U+105A <https://codepoints.net/U+105A>`_  '\\u105a'  Lo                  1  MYANMAR LETTER MON NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
=========================================  =========  ==========  =========  ======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x9c\xe1\x80\xad\xe1\x80\x80\xe1\x80\xba\xe1\x80\x9c\xe1\x80\x9c\xe1\x80\xb1\xe1\x80\xac\xe1\x81\x9a\xe1\x80\xba|\\n12345|\\n"
        လိက်လလောၚ်|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 7.

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
`U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
=========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa5\x80|\\n123|\\n"
        मानवी|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 5.

Nepali
^^^^^^

Sequence of language *Nepali* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
=========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
        मानव|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0AAE <https://codepoints.net/U+0AAE>`_  '\\u0aae'  Lo                  1  GUJARATI LETTER MA
`U+0ABE <https://codepoints.net/U+0ABE>`_  '\\u0abe'  Mc                  0  GUJARATI VOWEL SIGN AA
`U+0AA8 <https://codepoints.net/U+0AA8>`_  '\\u0aa8'  Lo                  1  GUJARATI LETTER NA
`U+0AB5 <https://codepoints.net/U+0AB5>`_  '\\u0ab5'  Lo                  1  GUJARATI LETTER VA
=========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
        માનવ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0C2E <https://codepoints.net/U+0C2E>`_  '\\u0c2e'  Lo                  1  TELUGU LETTER MA
`U+0C3E <https://codepoints.net/U+0C3E>`_  '\\u0c3e'  Mn                  0  TELUGU VOWEL SIGN AA
`U+0C28 <https://codepoints.net/U+0C28>`_  '\\u0c28'  Lo                  1  TELUGU LETTER NA
`U+0C35 <https://codepoints.net/U+0C35>`_  '\\u0c35'  Lo                  1  TELUGU LETTER VA
`U+0C38 <https://codepoints.net/U+0C38>`_  '\\u0c38'  Lo                  1  TELUGU LETTER SA
`U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
`U+0C35 <https://codepoints.net/U+0C35>`_  '\\u0c35'  Lo                  1  TELUGU LETTER VA
`U+0C24 <https://codepoints.net/U+0C24>`_  '\\u0c24'  Lo                  1  TELUGU LETTER TA
`U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
`U+0C35 <https://codepoints.net/U+0C35>`_  '\\u0c35'  Lo                  1  TELUGU LETTER VA
`U+0C2E <https://codepoints.net/U+0C2E>`_  '\\u0c2e'  Lo                  1  TELUGU LETTER MA
`U+0C41 <https://codepoints.net/U+0C41>`_  '\\u0c41'  Mc                  0  TELUGU VOWEL SIGN U
`U+0C32 <https://codepoints.net/U+0C32>`_  '\\u0c32'  Lo                  1  TELUGU LETTER LA
=========================================  =========  ==========  =========  ====================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
        మానవస్వత్వముల|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *tabby* measures width 10.

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
`U+092D <https://codepoints.net/U+092D>`_  '\\u092d'  Lo                  1  DEVANAGARI LETTER BHA
`U+094C <https://codepoints.net/U+094C>`_  '\\u094c'  Mc                  0  DEVANAGARI VOWEL SIGN AU
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
=========================================  =========  ==========  =========  ========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa4\xbe\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xb5\xe0\xa4\xad\xe0\xa5\x8c\xe0\xa4\xae|\\n12345|\\n"
        सार्वभौम|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 7.

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
=========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
        मानव|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0A2E <https://codepoints.net/U+0A2E>`_  '\\u0a2e'  Lo                  1  GURMUKHI LETTER MA
`U+0A28 <https://codepoints.net/U+0A28>`_  '\\u0a28'  Lo                  1  GURMUKHI LETTER NA
`U+0A41 <https://codepoints.net/U+0A41>`_  '\\u0a41'  Mn                  0  GURMUKHI VOWEL SIGN U
`U+0A71 <https://codepoints.net/U+0A71>`_  '\\u0a71'  Mn                  0  GURMUKHI ADDAK
`U+0A16 <https://codepoints.net/U+0A16>`_  '\\u0a16'  Lo                  1  GURMUKHI LETTER KHA
`U+0A40 <https://codepoints.net/U+0A40>`_  '\\u0a40'  Mc                  0  GURMUKHI VOWEL SIGN II
=========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
        ਮਨੁੱਖੀ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Sinhala
^^^^^^^

Sequence of language *Sinhala* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==============================
`U+0DB8 <https://codepoints.net/U+0DB8>`_  '\\u0db8'  Lo                  1  SINHALA LETTER MAYANNA
`U+0DCF <https://codepoints.net/U+0DCF>`_  '\\u0dcf'  Mc                  0  SINHALA VOWEL SIGN AELA-PILLA
`U+0DB1 <https://codepoints.net/U+0DB1>`_  '\\u0db1'  Lo                  1  SINHALA LETTER DANTAJA NAYANNA
`U+0DC0 <https://codepoints.net/U+0DC0>`_  '\\u0dc0'  Lo                  1  SINHALA LETTER VAYANNA
=========================================  =========  ==========  =========  ==============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
        මානව|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 4.

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0927 <https://codepoints.net/U+0927>`_  '\\u0927'  Lo                  1  DEVANAGARI LETTER DHA
`U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
=========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa7\xe0\xa4\xbf\xe0\xa4\x95\xe0\xa4\xbe\xe0\xa4\xb0|\\n123456|\\n"
        मानवाधिकार|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 10.

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0927 <https://codepoints.net/U+0927>`_  '\\u0927'  Lo                  1  DEVANAGARI LETTER DHA
`U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
=========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa7\xe0\xa4\xbf\xe0\xa4\x95\xe0\xa4\xbe\xe0\xa4\xb0|\\n123456|\\n"
        मानवाधिकार|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 10.

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ====================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ====================
`U+0001111F <https://codepoints.net/U+0001111F>`_  '\\U0001111f'  Lo                  1  CHAKMA LETTER MAA
`U+0001111A <https://codepoints.net/U+0001111A>`_  '\\U0001111a'  Lo                  1  CHAKMA LETTER NAA
`U+0001112C <https://codepoints.net/U+0001112C>`_  '\\U0001112c'  Mc                  0  CHAKMA VOWEL SIGN E
`U+0001112D <https://codepoints.net/U+0001112D>`_  '\\U0001112d'  Mn                  0  CHAKMA VOWEL SIGN AI
`U+00011103 <https://codepoints.net/U+00011103>`_  '\\U00011103'  Lo                  1  CHAKMA LETTER AA
`U+00011107 <https://codepoints.net/U+00011107>`_  '\\U00011107'  Lo                  1  CHAKMA LETTER KAA
`U+00011134 <https://codepoints.net/U+00011134>`_  '\\U00011134'  Mn                  0  CHAKMA MAAYYAA
`U+00011107 <https://codepoints.net/U+00011107>`_  '\\U00011107'  Lo                  1  CHAKMA LETTER KAA
`U+00011125 <https://codepoints.net/U+00011125>`_  '\\U00011125'  Lo                  1  CHAKMA LETTER SAA
`U+00011127 <https://codepoints.net/U+00011127>`_  '\\U00011127'  Mn                  0  CHAKMA VOWEL SIGN A
`U+00011101 <https://codepoints.net/U+00011101>`_  '\\U00011101'  Mn                  0  CHAKMA SIGN ANUSVARA
`U+00011122 <https://codepoints.net/U+00011122>`_  '\\U00011122'  Lo                  1  CHAKMA LETTER RAA
`U+00011134 <https://codepoints.net/U+00011134>`_  '\\U00011134'  Mn                  0  CHAKMA MAAYYAA
=================================================  =============  ==========  =========  ====================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
        𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 8.

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F41 <https://codepoints.net/U+0F41>`_  '\\u0f41'  Lo                  1  TIBETAN LETTER KHA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F5A <https://codepoints.net/U+0F5A>`_  '\\u0f5a'  Lo                  1  TIBETAN LETTER TSHA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0FB3 <https://codepoints.net/U+0FB3>`_  '\\u0fb3'  Mn                  0  TIBETAN SUBJOINED LETTER LA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0FA9 <https://codepoints.net/U+0FA9>`_  '\\u0fa9'  Mn                  0  TIBETAN SUBJOINED LETTER TSA
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F58 <https://codepoints.net/U+0F58>`_  '\\u0f58'  Lo                  1  TIBETAN LETTER MA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F5A <https://codepoints.net/U+0F5A>`_  '\\u0f5a'  Lo                  1  TIBETAN LETTER TSHA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F5F <https://codepoints.net/U+0F5F>`_  '\\u0f5f'  Lo                  1  TIBETAN LETTER ZA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F54 <https://codepoints.net/U+0F54>`_  '\\u0f54'  Lo                  1  TIBETAN LETTER PA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F54 <https://codepoints.net/U+0F54>`_  '\\u0f54'  Lo                  1  TIBETAN LETTER PA
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F40 <https://codepoints.net/U+0F40>`_  '\\u0f40'  Lo                  1  TIBETAN LETTER KA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F61 <https://codepoints.net/U+0F61>`_  '\\u0f61'  Lo                  1  TIBETAN LETTER YA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ================================

Total codepoints: 70


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x81\xe0\xbd\xbc\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x9a\xe0\xbd\xbc\xe0\xbd\xa2\xe0\xbc\x8b\xe0\xbd\xa2\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbe\xb1\xe0\xbd\xb4\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbe\xb3\xe0\xbd\xbc\xe0\xbc\x8b\xe0\xbd\xa2\xe0\xbe\xa9\xe0\xbd\xa3\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\xa6\xe0\xbd\x98\xe0\xbc\x8b\xe0\xbd\x9a\xe0\xbd\xb4\xe0\xbd\xa3\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\x9f\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbd\xbc\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x91\xe0\xbd\xbc\xe0\xbd\x93\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\xbc\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\x96\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x80\xe0\xbe\xb1\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x91\xe0\xbc\x8d|\\n1234567890123456789012345678901234567890123456789012345|\\n"
        ཁོང་ཚོར་རང་བྱུང་གི་བློ་རྩལ་དང་བསམ་ཚུལ་བཟང་པོ་འདོན་པའི་འོས་བབས་ཀྱང་ཡོད།|
        1234567890123456789012345678901234567890123456789012345|

- python `wcwidth.wcswidth()`_ measures width 55,
  while *tabby* measures width 27.

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ===========================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ===========================
`U+6BCF <https://codepoints.net/U+6BCF>`_          '\\u6bcf'      Lo                  2  CJK UNIFIED IDEOGRAPH-6BCF
`U+0002029B <https://codepoints.net/U+0002029B>`_  '\\U0002029b'  Lo                  2  CJK UNIFIED IDEOGRAPH-2029B
`U+8ABF <https://codepoints.net/U+8ABF>`_          '\\u8abf'      Lo                  2  CJK UNIFIED IDEOGRAPH-8ABF
`U+0002338F <https://codepoints.net/U+0002338F>`_  '\\U0002338f'  Lo                  2  CJK UNIFIED IDEOGRAPH-2338F
`U+6B0A <https://codepoints.net/U+6B0A>`_          '\\u6b0a'      Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
`U+00022D10 <https://codepoints.net/U+00022D10>`_  '\\U00022d10'  Lo                  2  CJK UNIFIED IDEOGRAPH-22D10
`U+584A <https://codepoints.net/U+584A>`_          '\\u584a'      Lo                  2  CJK UNIFIED IDEOGRAPH-584A
`U+4E0D <https://codepoints.net/U+4E0D>`_          '\\u4e0d'      Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+64DA <https://codepoints.net/U+64DA>`_          '\\u64da'      Lo                  2  CJK UNIFIED IDEOGRAPH-64DA
`U+6E03 <https://codepoints.net/U+6E03>`_          '\\u6e03'      Lo                  2  CJK UNIFIED IDEOGRAPH-6E03
`U+8287 <https://codepoints.net/U+8287>`_          '\\u8287'      Lo                  2  CJK UNIFIED IDEOGRAPH-8287
=================================================  =============  ==========  =========  ===========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xaf\x8f\xf0\xa0\x8a\x9b\xe8\xaa\xbf\xf0\xa3\x8e\x8f\xe6\xac\x8a\xf0\xa2\xb4\x90\xe5\xa1\x8a\xe4\xb8\x8d\xe6\x93\x9a\xe6\xb8\x83\xe8\x8a\x87|\\n1234567890123456789012|\\n"
        每𠊛調𣎏權𢴐塊不據渃芇|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *tabby* measures width -20.

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+307E <https://codepoints.net/U+307E>`_  '\\u307e'  Lo                  2  HIRAGANA LETTER MA
`U+305F <https://codepoints.net/U+305F>`_  '\\u305f'  Lo                  2  HIRAGANA LETTER TA
=========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\xbe\xe3\x81\x9f|\\n1234|\\n"
        また|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -36.

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+307E <https://codepoints.net/U+307E>`_  '\\u307e'  Lo                  2  HIRAGANA LETTER MA
`U+305F <https://codepoints.net/U+305F>`_  '\\u305f'  Lo                  2  HIRAGANA LETTER TA
=========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\xbe\xe3\x81\x9f|\\n1234|\\n"
        また|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -36.

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0E02 <https://codepoints.net/U+0E02>`_  '\\u0e02'  Lo                  1  THAI CHARACTER KHO KHAI
`U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
`U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
=========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x82\xe0\xb9\x89\xe0\xb8\xad|\\n12|\\n"
        ข้อ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -30.

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
`U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
`U+9053 <https://codepoints.net/U+9053>`_  '\\u9053'  Lo                  2  CJK UNIFIED IDEOGRAPH-9053
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
`U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
`U+80CC <https://codepoints.net/U+80CC>`_  '\\u80cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-80CC
`U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
`U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
`U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
`U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
`U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
`U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+52BF <https://codepoints.net/U+52BF>`_  '\\u52bf'  Lo                  2  CJK UNIFIED IDEOGRAPH-52BF
`U+5934 <https://codepoints.net/U+5934>`_  '\\u5934'  Lo                  2  CJK UNIFIED IDEOGRAPH-5934
`U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
=========================================  =========  ==========  =========  ==========================

Total codepoints: 36


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe5\x9c\xb0\xe9\x81\x93\xe7\x9a\x84\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe7\x9a\x84\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe7\x9a\x84\xe5\xae\x97\xe6\x97\xa8\xe5\x92\x8c\xe5\x8e\x9f\xe5\x88\x99\xe7\x9a\x84\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe8\xaf\x89\xe7\x9a\x84\xe5\x8a\xbf\xe5\xa4\xb4\xe4\xb8\x8b|\\n123456789012345678901234567890123456789012345678901234567890123456789012|\\n"
        在地道的由于非政治性的罪行或违背联合国的宗旨和原则的行为而被起诉的势头下|
        123456789012345678901234567890123456789012345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 72,
  while *tabby* measures width 30.

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4EA6 <https://codepoints.net/U+4EA6>`_  '\\u4ea6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EA6
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+5426 <https://codepoints.net/U+5426>`_  '\\u5426'  Lo                  2  CJK UNIFIED IDEOGRAPH-5426
`U+8A8D <https://codepoints.net/U+8A8D>`_  '\\u8a8d'  Lo                  2  CJK UNIFIED IDEOGRAPH-8A8D
`U+5176 <https://codepoints.net/U+5176>`_  '\\u5176'  Lo                  2  CJK UNIFIED IDEOGRAPH-5176
`U+6539 <https://codepoints.net/U+6539>`_  '\\u6539'  Lo                  2  CJK UNIFIED IDEOGRAPH-6539
`U+8B8A <https://codepoints.net/U+8B8A>`_  '\\u8b8a'  Lo                  2  CJK UNIFIED IDEOGRAPH-8B8A
`U+570B <https://codepoints.net/U+570B>`_  '\\u570b'  Lo                  2  CJK UNIFIED IDEOGRAPH-570B
`U+7C4D <https://codepoints.net/U+7C4D>`_  '\\u7c4d'  Lo                  2  CJK UNIFIED IDEOGRAPH-7C4D
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+6B0A <https://codepoints.net/U+6B0A>`_  '\\u6b0a'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
=========================================  =========  ==========  =========  ==========================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xba\xa6\xe4\xb8\x8d\xe5\xbe\x97\xe5\x90\xa6\xe8\xaa\x8d\xe5\x85\xb6\xe6\x94\xb9\xe8\xae\x8a\xe5\x9c\x8b\xe7\xb1\x8d\xe7\x9a\x84\xe6\xac\x8a\xe5\x88\xa9|\\n12345678901234567890123456|\\n"
        亦不得否認其改變國籍的權利|
        12345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 26,
  while *tabby* measures width 2.

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+55BA <https://codepoints.net/U+55BA>`_  '\\u55ba'  Lo                  2  CJK UNIFIED IDEOGRAPH-55BA
`U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
`U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
`U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
`U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
`U+5605 <https://codepoints.net/U+5605>`_  '\\u5605'  Lo                  2  CJK UNIFIED IDEOGRAPH-5605
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
`U+80CC <https://codepoints.net/U+80CC>`_  '\\u80cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-80CC
`U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+5605 <https://codepoints.net/U+5605>`_  '\\u5605'  Lo                  2  CJK UNIFIED IDEOGRAPH-5605
`U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
`U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
`U+540C <https://codepoints.net/U+540C>`_  '\\u540c'  Lo                  2  CJK UNIFIED IDEOGRAPH-540C
`U+57CB <https://codepoints.net/U+57CB>`_  '\\u57cb'  Lo                  2  CJK UNIFIED IDEOGRAPH-57CB
`U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
`U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
`U+5605 <https://codepoints.net/U+5605>`_  '\\u5605'  Lo                  2  CJK UNIFIED IDEOGRAPH-5605
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
`U+4FFE <https://codepoints.net/U+4FFE>`_  '\\u4ffe'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FFE
`U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
`U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
`U+5605 <https://codepoints.net/U+5605>`_  '\\u5605'  Lo                  2  CJK UNIFIED IDEOGRAPH-5605
`U+60C5 <https://codepoints.net/U+60C5>`_  '\\u60c5'  Lo                  2  CJK UNIFIED IDEOGRAPH-60C5
`U+51B5 <https://codepoints.net/U+51B5>`_  '\\u51b5'  Lo                  2  CJK UNIFIED IDEOGRAPH-51B5
`U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
=========================================  =========  ==========  =========  ==========================

Total codepoints: 36


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x96\xba\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe5\x98\x85\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe5\x98\x85\xe5\xae\x97\xe6\x97\xa8\xe5\x90\x8c\xe5\x9f\x8b\xe5\x8e\x9f\xe5\x88\x99\xe5\x98\x85\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe4\xbf\xbe\xe8\xb5\xb7\xe8\xaf\x89\xe5\x98\x85\xe6\x83\x85\xe5\x86\xb5\xe4\xb8\x8b|\\n123456789012345678901234567890123456789012345678901234567890123456789012|\\n"
        喺真正由于非政治性嘅罪行或违背联合国嘅宗旨同埋原则嘅行为而俾起诉嘅情况下|
        123456789012345678901234567890123456789012345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 72,
  while *tabby* measures width 30.

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+4E09 <https://codepoints.net/U+4E09>`_  '\\u4e09'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E09
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x89\xe6\x9d\xa1|\\n12345678|\\n"
        第十三条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -14.

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
`U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
`U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
`U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
`U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+6627 <https://codepoints.net/U+6627>`_  '\\u6627'  Lo                  2  CJK UNIFIED IDEOGRAPH-6627
`U+5230 <https://codepoints.net/U+5230>`_  '\\u5230'  Lo                  2  CJK UNIFIED IDEOGRAPH-5230
`U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
`U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
`U+8DDF <https://codepoints.net/U+8DDF>`_  '\\u8ddf'  Lo                  2  CJK UNIFIED IDEOGRAPH-8DDF
`U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
`U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
`U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
`U+6B65 <https://codepoints.net/U+6B65>`_  '\\u6b65'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B65
=========================================  =========  ==========  =========  ==========================

Total codepoints: 34


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe4\xb8\xaa\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe6\x98\xa7\xe5\x88\xb0\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe4\xb8\xaa\xe5\xae\x97\xe6\x97\xa8\xe8\xb7\x9f\xe5\x8e\x9f\xe5\x88\x99\xe4\xb8\xaa\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe8\xaf\x89\xe4\xb8\xaa\xe5\x9c\xb0\xe6\xad\xa5|\\n12345678901234567890123456789012345678901234567890123456789012345678|\\n"
        在真正由于非政治性个罪行或昧到联合国个宗旨跟原则个行为而被起诉个地步|
        12345678901234567890123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 68,
  while *tabby* measures width 26.

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+4E09 <https://codepoints.net/U+4E09>`_  '\\u4e09'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E09
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x89\xe6\x9d\xa1|\\n12345678|\\n"
        第十三条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -14.

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
`U+52FF <https://codepoints.net/U+52FF>`_  '\\u52ff'  Lo                  2  CJK UNIFIED IDEOGRAPH-52FF
`U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
`U+63B0 <https://codepoints.net/U+63B0>`_  '\\u63b0'  Lo                  2  CJK UNIFIED IDEOGRAPH-63B0
`U+6392 <https://codepoints.net/U+6392>`_  '\\u6392'  Lo                  2  CJK UNIFIED IDEOGRAPH-6392
`U+91CC <https://codepoints.net/U+91CC>`_  '\\u91cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-91CC
`U+5E72 <https://codepoints.net/U+5E72>`_  '\\u5e72'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E72
`U+6D89 <https://codepoints.net/U+6D89>`_  '\\u6d89'  Lo                  2  CJK UNIFIED IDEOGRAPH-6D89
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+653B <https://codepoints.net/U+653B>`_  '\\u653b'  Lo                  2  CJK UNIFIED IDEOGRAPH-653B
`U+51FB <https://codepoints.net/U+51FB>`_  '\\u51fb'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FB
=========================================  =========  ==========  =========  ==========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xa5\xe5\x8b\xbf\xe5\x8f\x97\xe6\x8e\xb0\xe6\x8e\x92\xe9\x87\x8c\xe5\xb9\xb2\xe6\xb6\x89\xe6\x88\x96\xe6\x94\xbb\xe5\x87\xbb|\\n1234567890123456789012|\\n"
        以勿受掰排里干涉或攻击|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *tabby* measures width 2.

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
`U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
`U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
`U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
`U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
`U+80CC <https://codepoints.net/U+80CC>`_  '\\u80cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-80CC
`U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
`U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
`U+540C <https://codepoints.net/U+540C>`_  '\\u540c'  Lo                  2  CJK UNIFIED IDEOGRAPH-540C
`U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
`U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+6C14 <https://codepoints.net/U+6C14>`_  '\\u6c14'  Lo                  2  CJK UNIFIED IDEOGRAPH-6C14
`U+8C61 <https://codepoints.net/U+8C61>`_  '\\u8c61'  Lo                  2  CJK UNIFIED IDEOGRAPH-8C61
`U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
=========================================  =========  ==========  =========  ==========================

Total codepoints: 35


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe4\xb8\xaa\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe4\xb8\xaa\xe5\xae\x97\xe6\x97\xa8\xe5\x90\x8c\xe5\x8e\x9f\xe5\x88\x99\xe4\xb8\xaa\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe4\xba\x8b\xe4\xb8\xaa\xe6\xb0\x94\xe8\xb1\xa1\xe4\xb8\x8b|\\n1234567890123456789012345678901234567890123456789012345678901234567890|\\n"
        在真正由于非政治性个罪行或违背联合国个宗旨同原则个行为而被起事个气象下|
        1234567890123456789012345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 70,
  while *tabby* measures width 28.

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+6562 <https://codepoints.net/U+6562>`_  '\\u6562'  Lo                  2  CJK UNIFIED IDEOGRAPH-6562
`U+63F4 <https://codepoints.net/U+63F4>`_  '\\u63f4'  Lo                  2  CJK UNIFIED IDEOGRAPH-63F4
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+6B64 <https://codepoints.net/U+6B64>`_  '\\u6b64'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B64
`U+79CD <https://codepoints.net/U+79CD>`_  '\\u79cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-79CD
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
=========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe6\x95\xa2\xe6\x8f\xb4\xe7\x94\xa8\xe6\xad\xa4\xe7\xa7\x8d\xe6\x9d\x83\xe5\x88\xa9|\\n1234567890123456|\\n"
        不敢援用此种权利|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *tabby* measures width -52.

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
`U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
`U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
`U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
`U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
`U+80CC <https://codepoints.net/U+80CC>`_  '\\u80cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-80CC
`U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
`U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
`U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
`U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
`U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
`U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+78B4 <https://codepoints.net/U+78B4>`_  '\\u78b4'  Lo                  2  CJK UNIFIED IDEOGRAPH-78B4
`U+513F <https://codepoints.net/U+513F>`_  '\\u513f'  Lo                  2  CJK UNIFIED IDEOGRAPH-513F
=========================================  =========  ==========  =========  ==========================

Total codepoints: 34


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe7\x9a\x84\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe7\x9a\x84\xe5\xae\x97\xe6\x97\xa8\xe5\x92\x8c\xe5\x8e\x9f\xe5\x88\x99\xe7\x9a\x84\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe8\xaf\x89\xe7\x9a\x84\xe7\xa2\xb4\xe5\x84\xbf|\\n12345678901234567890123456789012345678901234567890123456789012345678|\\n"
        在真正由于非政治性的罪行或违背联合国的宗旨和原则的行为而被起诉的碴儿|
        12345678901234567890123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 68,
  while *tabby* measures width 22.

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+514D <https://codepoints.net/U+514D>`_  '\\u514d'  Lo                  2  CJK UNIFIED IDEOGRAPH-514D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
`U+8FEB <https://codepoints.net/U+8FEB>`_  '\\u8feb'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FEB
`U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
=========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\x8d\xe5\xbe\x97\xe5\x8f\x97\xe8\xbf\xab\xe5\xae\xb3|\\n1234567890|\\n"
        免得受迫害|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *tabby* measures width -22.

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+7F5A <https://codepoints.net/U+7F5A>`_  '\\u7f5a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F5A
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+91CD <https://codepoints.net/U+91CD>`_  '\\u91cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-91CD
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+5DE5 <https://codepoints.net/U+5DE5>`_  '\\u5de5'  Lo                  2  CJK UNIFIED IDEOGRAPH-5DE5
`U+592B <https://codepoints.net/U+592B>`_  '\\u592b'  Lo                  2  CJK UNIFIED IDEOGRAPH-592B
`U+9002 <https://codepoints.net/U+9002>`_  '\\u9002'  Lo                  2  CJK UNIFIED IDEOGRAPH-9002
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
`U+89C4 <https://codepoints.net/U+89C4>`_  '\\u89c4'  Lo                  2  CJK UNIFIED IDEOGRAPH-89C4
`U+5B9A <https://codepoints.net/U+5B9A>`_  '\\u5b9a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x88\x91\xe7\xbd\x9a\xe4\xb8\x8d\xe5\xbe\x97\xe9\x87\x8d\xe4\xba\x8e\xe7\x8a\xaf\xe7\xbd\xaa\xe7\x9a\x84\xe5\xb7\xa5\xe5\xa4\xab\xe9\x80\x82\xe7\x94\xa8\xe7\x9a\x84\xe6\xb3\x95\xe5\xbe\x8b\xe8\xa7\x84\xe5\xae\x9a|\\n123456789012345678901234567890123456|\\n"
        刑罚不得重于犯罪的工夫适用的法律规定|
        123456789012345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 36,
  while *tabby* measures width 16.

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
`U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
`U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
`U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+65E0 <https://codepoints.net/U+65E0>`_  '\\u65e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E0
`U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+6291 <https://codepoints.net/U+6291>`_  '\\u6291'  Lo                  2  CJK UNIFIED IDEOGRAPH-6291
`U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
`U+9006 <https://codepoints.net/U+9006>`_  '\\u9006'  Lo                  2  CJK UNIFIED IDEOGRAPH-9006
`U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
`U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
`U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
`U+4E92 <https://codepoints.net/U+4E92>`_  '\\u4e92'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E92
`U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
`U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+4EE3 <https://codepoints.net/U+4EE3>`_  '\\u4ee3'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE3
`U+5FD7 <https://codepoints.net/U+5FD7>`_  '\\u5fd7'  Lo                  2  CJK UNIFIED IDEOGRAPH-5FD7
`U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
=========================================  =========  ==========  =========  ==========================

Total codepoints: 35


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe6\x97\xa0\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe7\x9a\x84\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x8a\x91\xe8\xbf\x9d\xe9\x80\x86\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe7\x9a\x84\xe5\xae\x97\xe6\x97\xa8\xe5\x90\x88\xe5\x8e\x9f\xe5\x88\x99\xe7\x9a\x84\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe4\xba\x92\xe8\xb5\xb7\xe8\xaf\x89\xe7\x9a\x84\xe4\xbb\xa3\xe5\xbf\x97\xe4\xb8\x8b|\\n1234567890123456789012345678901234567890123456789012345678901234567890|\\n"
        在真正由于无政治性的罪行抑违逆联合国的宗旨合原则的行为而互起诉的代志下|
        1234567890123456789012345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 70,
  while *tabby* measures width 30.

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+6253 <https://codepoints.net/U+6253>`_  '\\u6253'  Lo                  2  CJK UNIFIED IDEOGRAPH-6253
`U+56DE <https://codepoints.net/U+56DE>`_  '\\u56de'  Lo                  2  CJK UNIFIED IDEOGRAPH-56DE
`U+8F6C <https://codepoints.net/U+8F6C>`_  '\\u8f6c'  Lo                  2  CJK UNIFIED IDEOGRAPH-8F6C
=========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe6\x9c\x89\xe6\x9d\x83\xe6\x89\x93\xe5\x9b\x9e\xe8\xbd\xac|\\n123456789012|\\n"
        并有权打回转|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *tabby* measures width -4.

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+7F5A <https://codepoints.net/U+7F5A>`_  '\\u7f5a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F5A
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+91CD <https://codepoints.net/U+91CD>`_  '\\u91cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-91CD
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+65F6 <https://codepoints.net/U+65F6>`_  '\\u65f6'  Lo                  2  CJK UNIFIED IDEOGRAPH-65F6
`U+9002 <https://codepoints.net/U+9002>`_  '\\u9002'  Lo                  2  CJK UNIFIED IDEOGRAPH-9002
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
`U+89C4 <https://codepoints.net/U+89C4>`_  '\\u89c4'  Lo                  2  CJK UNIFIED IDEOGRAPH-89C4
`U+5B9A <https://codepoints.net/U+5B9A>`_  '\\u5b9a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x88\x91\xe7\xbd\x9a\xe4\xb8\x8d\xe5\xbe\x97\xe9\x87\x8d\xe4\xba\x8e\xe7\x8a\xaf\xe7\xbd\xaa\xe6\x97\xb6\xe9\x80\x82\xe7\x94\xa8\xe7\x9a\x84\xe6\xb3\x95\xe5\xbe\x8b\xe8\xa7\x84\xe5\xae\x9a|\\n12345678901234567890123456789012|\\n"
        刑罚不得重于犯罪时适用的法律规定|
        12345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 32,
  while *tabby* measures width 12.

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0E02 <https://codepoints.net/U+0E02>`_  '\\u0e02'  Lo                  1  THAI CHARACTER KHO KHAI
`U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
`U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
=========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x82\xe0\xb9\x89\xe0\xb8\xad|\\n12|\\n"
        ข้อ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -32.

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================
`U+A1EC <https://codepoints.net/U+A1EC>`_  '\\ua1ec'  Lo                  2  YI SYLLABLE GO
`U+A3E2 <https://codepoints.net/U+A3E2>`_  '\\ua3e2'  Lo                  2  YI SYLLABLE JI
`U+A1CB <https://codepoints.net/U+A1CB>`_  '\\ua1cb'  Lo                  2  YI SYLLABLE LEX
`U+A1EC <https://codepoints.net/U+A1EC>`_  '\\ua1ec'  Lo                  2  YI SYLLABLE GO
`U+A052 <https://codepoints.net/U+A052>`_  '\\ua052'  Lo                  2  YI SYLLABLE PY
`U+A400 <https://codepoints.net/U+A400>`_  '\\ua400'  Lo                  2  YI SYLLABLE QIET
`U+A00B <https://codepoints.net/U+A00B>`_  '\\ua00b'  Lo                  2  YI SYLLABLE AP
`U+A246 <https://codepoints.net/U+A246>`_  '\\ua246'  Lo                  2  YI SYLLABLE HXIT
=========================================  =========  ==========  =========  ================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x87\xac\xea\x8f\xa2\xea\x87\x8b\xea\x87\xac\xea\x81\x92\xea\x90\x80\xea\x80\x8b\xea\x89\x86|\\n1234567890123456|\\n"
        ꇬꏢꇋꇬꁒꐀꀋꉆ|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *tabby* measures width -14.

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0FA1 <https://codepoints.net/U+0FA1>`_  '\\u0fa1'  Mn                  0  TIBETAN SUBJOINED LETTER DA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0FA4 <https://codepoints.net/U+0FA4>`_  '\\u0fa4'  Mn                  0  TIBETAN SUBJOINED LETTER PA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0FA9 <https://codepoints.net/U+0FA9>`_  '\\u0fa9'  Mn                  0  TIBETAN SUBJOINED LETTER TSA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ================================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa6\xe0\xbe\xa1\xe0\xbd\xb4\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\xa6\xe0\xbe\xa4\xe0\xbe\xb1\xe0\xbd\xbc\xe0\xbd\x91\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\x91\xe0\xbd\xb4\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\xa2\xe0\xbe\xa9\xe0\xbd\xb4\xe0\xbd\x96\xe0\xbc\x8d|\\n1234567890123456|\\n"
        སྡུག་སྤྱོད་དང་གདུག་རྩུབ།|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *tabby* measures width -1.

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+0EAB <https://codepoints.net/U+0EAB>`_  '\\u0eab'  Lo                  1  LAO LETTER HO SUNG
`U+0EBC <https://codepoints.net/U+0EBC>`_  '\\u0ebc'  Mn                  0  LAO SEMIVOWEL SIGN LO
`U+0EB7 <https://codepoints.net/U+0EB7>`_  '\\u0eb7'  Mn                  0  LAO VOWEL SIGN YY
=========================================  =========  ==========  =========  =====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xba\xab\xe0\xba\xbc\xe0\xba\xb7|\\n1|\\n"
        ຫຼື|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *tabby* measures width -7.

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
`U+9650 <https://codepoints.net/U+9650>`_  '\\u9650'  Lo                  2  CJK UNIFIED IDEOGRAPH-9650
`U+304C <https://codepoints.net/U+304C>`_  '\\u304c'  Lo                  2  HIRAGANA LETTER GA
`U+3042 <https://codepoints.net/U+3042>`_  '\\u3042'  Lo                  2  HIRAGANA LETTER A
`U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+5185 <https://codepoints.net/U+5185>`_  '\\u5185'  Lo                  2  CJK UNIFIED IDEOGRAPH-5185
`U+88C1 <https://codepoints.net/U+88C1>`_  '\\u88c1'  Lo                  2  CJK UNIFIED IDEOGRAPH-88C1
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
`U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
`U+3088 <https://codepoints.net/U+3088>`_  '\\u3088'  Lo                  2  HIRAGANA LETTER YO
`U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
`U+52B9 <https://codepoints.net/U+52B9>`_  '\\u52b9'  Lo                  2  CJK UNIFIED IDEOGRAPH-52B9
`U+679C <https://codepoints.net/U+679C>`_  '\\u679c'  Lo                  2  CJK UNIFIED IDEOGRAPH-679C
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
`U+6551 <https://codepoints.net/U+6551>`_  '\\u6551'  Lo                  2  CJK UNIFIED IDEOGRAPH-6551
`U+6E08 <https://codepoints.net/U+6E08>`_  '\\u6e08'  Lo                  2  CJK UNIFIED IDEOGRAPH-6E08
`U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
`U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
`U+3051 <https://codepoints.net/U+3051>`_  '\\u3051'  Lo                  2  HIRAGANA LETTER KE
`U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
`U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
`U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
`U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
=========================================  =========  ==========  =========  ==========================

Total codepoints: 29


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xa8\xa9\xe9\x99\x90\xe3\x81\x8c\xe3\x81\x82\xe3\x82\x8b\xe5\x9b\xbd\xe5\x86\x85\xe8\xa3\x81\xe5\x88\xa4\xe6\x89\x80\xe3\x81\xab\xe3\x82\x88\xe3\x82\x8b\xe5\x8a\xb9\xe6\x9e\x9c\xe7\x9a\x84\xe3\x81\xaa\xe6\x95\x91\xe6\xb8\x88\xe3\x82\x92\xe5\x8f\x97\xe3\x81\x91\xe3\x82\x8b\xe6\xa8\xa9\xe5\x88\xa9\xe3\x82\x92\xe6\x9c\x89\xe3\x81\x99\xe3\x82\x8b|\\n1234567890123456789012345678901234567890123456789012345678|\\n"
        権限がある国内裁判所による効果的な救済を受ける権利を有する|
        1234567890123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 58,
  while *tabby* measures width -2.

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+004B <https://codepoints.net/U+004B>`_  'K'       Lu                  1  LATIN CAPITAL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0031 <https://codepoints.net/U+0031>`_  '1'       Nd                  1  DIGIT ONE
`U+0032 <https://codepoints.net/U+0032>`_  '2'       Nd                  1  DIGIT TWO
=========================================  ========  ==========  =========  ======================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "AnompaKanihmo'si12|\\n123456789012345678|\\n"
        AnompaKanihmo'si12|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *tabby* measures width -1.

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+0308 <https://codepoints.net/U+0308>`_  '\\u0308'  Mn                  0  COMBINING DIAERESIS
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
=========================================  =========  ==========  =========  ====================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xcc\x83yeyc\xcc\x88hena|\\n12345678|\\n"
        ̃yeyc̈hena|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 9.

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'   Ll                  1  LATIN SMALL LETTER U WITH ACUTE
`U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'   Ll                  1  LATIN SMALL LETTER U WITH ACUTE
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 21


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ma\xc3\xa1vyej\xc3\xba\xc3\xball\xc3\xa9jcats\xc3\xadmy\xc3\xa9|\\n123456789012345678901|\\n"
        maávyejúúlléjcatsímyé|
        123456789012345678901|

- python `wcwidth.wcswidth()`_ measures width 21,
  while *tabby* measures width 12.

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ta'baere|\\n12345678|\\n"
        ta'baere|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 2.

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jonibo|\\n123456|\\n"
        jonibo|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 0.

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0059 <https://codepoints.net/U+0059>`_  'Y'       Lu                  1  LATIN CAPITAL LETTER Y
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+007A <https://codepoints.net/U+007A>`_  'z'       Ll                  1  LATIN SMALL LETTER Z
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Yisdzoh\xc3\xadg\xc3\xad\xc3\xad|\\n12345678901|\\n"
        Yisdzohígíí|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *tabby* measures width 6.

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+0433 <https://codepoints.net/U+0433>`_  '\\u0433'  Ll                  1  CYRILLIC SMALL LETTER GHE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
=========================================  =========  ==========  =========  =========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x82\xd1\x83\xd1\x80\xd0\xb3\xd1\x83\xd0\xbd\xd0\xb4\xd1\x83\xd0\xbb\xd1\x8d\xd0\xbd\xd0\xb8|\\n123456789012|\\n"
        тургундулэни|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *tabby* measures width 0.

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0447 <https://codepoints.net/U+0447>`_  '\\u0447'  Ll                  1  CYRILLIC SMALL LETTER CHE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+043F <https://codepoints.net/U+043F>`_  '\\u043f'  Ll                  1  CYRILLIC SMALL LETTER PE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
=========================================  =========  ==========  =========  =========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x87\xd0\xb8\xd0\xbf\xd0\xb0\xcc\x84\xd0\xbb\xd0\xb8|\\n123456|\\n"
        чипа̄ли|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width -3.

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "niyaketi|\\n12345678|\\n"
        niyaketi|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -1.

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kamakodama|\\n1234567890|\\n"
        kamakodama|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *tabby* measures width 4.

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ei|\\n12|\\n"
        ei|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -4.

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
=========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb4\xd1\x8f\xd1\x80\xd0\xb8\xd0\xbd|\\n12345|\\n"
        дярин|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 2.

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0306 <https://codepoints.net/U+0306>`_  '\\u0306'  Mn                  0  COMBINING BREVE
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
=========================================  =========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "dig\xcc\x86er|\\n12345|\\n"
        diğer|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width -3.

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "peoyeje|\\n1234567|\\n"
        peoyeje|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 1.

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
=========================================  ========  ==========  =========  ====================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "internacional|\\n1234567890123|\\n"
        internacional|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *tabby* measures width 11.

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
=========================================  =========  ==========  =========  ======================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "juri\xcc\x81dico|\\n12345678|\\n"
        jurídico|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -1.

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bai'ye|\\n123456|\\n"
        bai'ye|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 0.

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================================
`U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+04CA <https://codepoints.net/U+04CA>`_  '\\u04ca'  Ll                  1  CYRILLIC SMALL LETTER EN WITH TAIL
=========================================  =========  ==========  =========  ==================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x8d\xd0\xbd\xd0\xb0\xd3\x8a|\\n1234|\\n"
        энаӊ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width 0.

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ou|\\n12|\\n"
        ou|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -7.

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===================================
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'   Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
=========================================  ========  ==========  =========  ===================================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "r\xc3\xbc|\\n12|\\n"
        rü|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -2.

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+B098 <https://codepoints.net/U+B098>`_  '\\ub098'  Lo                  2  HANGUL SYLLABLE NA
`U+B77C <https://codepoints.net/U+B77C>`_  '\\ub77c'  Lo                  2  HANGUL SYLLABLE RA
`U+BC95 <https://codepoints.net/U+BC95>`_  '\\ubc95'  Lo                  2  HANGUL SYLLABLE BEOB
=========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xeb\x82\x98\xeb\x9d\xbc\xeb\xb2\x95|\\n123456|\\n"
        나라법|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width -2.

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ====================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ====================
`U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
=================================================  =============  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xab|\\n1|\\n"
        𞤫|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *tabby* measures width -5.

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kpataa|\\n123456|\\n"
        kpataa|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width -1.

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0047 <https://codepoints.net/U+0047>`_  'G'       Lu                  1  LATIN CAPITAL LETTER G
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Gawu|\\n1234|\\n"
        Gawu|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width 2.

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
=========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gblam\xc9\x9b|\\n123456|\\n"
        gblamɛ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width -2.

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0722 <https://codepoints.net/U+0722>`_  '\\u0722'  Lo                  1  SYRIAC LETTER NUN
`U+071B <https://codepoints.net/U+071B>`_  '\\u071b'  Lo                  1  SYRIAC LETTER TETH
`U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
`U+072A <https://codepoints.net/U+072A>`_  '\\u072a'  Lo                  1  SYRIAC LETTER RISH
`U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
=========================================  =========  ==========  =========  ===================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\xa2\xdc\x9b\xdc\x9d\xdc\xaa\xdc\x90|\\n12345|\\n"
        ܢܛܝܪܐ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 1.

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+05D0 <https://codepoints.net/U+05D0>`_  '\\u05d0'  Lo                  1  HEBREW LETTER ALEF
`U+05D9 <https://codepoints.net/U+05D9>`_  '\\u05d9'  Lo                  1  HEBREW LETTER YOD
`U+05DF <https://codepoints.net/U+05DF>`_  '\\u05df'  Lo                  1  HEBREW LETTER FINAL NUN
=========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x90\xd7\x99\xd7\x9f|\\n123|\\n"
        אין|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -4.

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ki|\\n12|\\n"
        ki|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -4.

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+C0AC <https://codepoints.net/U+C0AC>`_  '\\uc0ac'  Lo                  2  HANGUL SYLLABLE SA
`U+B78C <https://codepoints.net/U+B78C>`_  '\\ub78c'  Lo                  2  HANGUL SYLLABLE RAM
`U+C740 <https://codepoints.net/U+C740>`_  '\\uc740'  Lo                  2  HANGUL SYLLABLE EUN
=========================================  =========  ==========  =========  ===================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x82\xac\xeb\x9e\x8c\xec\x9d\x80|\\n123456|\\n"
        사람은|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 2.

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "e|\\n1|\\n"
        e|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *tabby* measures width -10.

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "wis|\\n123|\\n"
        wis|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -4.

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
=========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "se\xcc\x81|\\n12|\\n"
        sé|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -8.

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
=========================================  =========  ==========  =========  ==================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x82\xd8\xa7\xd9\x86\xd9\x88\xd9\x86|\\n12345|\\n"
        قانون|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width -1.

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ara|\\n123|\\n"
        ara|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -4.

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "k\xc3\xad|\\n12|\\n"
        kí|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -5.

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================================
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+1EB9 <https://codepoints.net/U+1EB9>`_  '\\u1eb9'  Ll                  1  LATIN SMALL LETTER E WITH DOT BELOW
`U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
=========================================  =========  ==========  =========  ===================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "r\xe1\xba\xb9\xcc\x80|\\n12|\\n"
        rẹ̀|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -7.

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
`U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
`U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
=========================================  =========  ==========  =========  =====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa8\xd9\x87\xd8\xb1\xd9\x87\xe2\x80\x8c\xd9\x85\xd9\x86\xd8\xaf|\\n1234567|\\n"
        بهره‌مند|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 2.

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================================
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+00F4 <https://codepoints.net/U+00F4>`_  '\\xf4'    Ll                  1  LATIN SMALL LETTER O WITH CIRCUMFLEX
`U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
=========================================  =========  ==========  =========  ====================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "m\xc3\xb4\xcc\xa3t|\\n123|\\n"
        một|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 1.

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ko|\\n12|\\n"
        ko|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -4.

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0784 <https://codepoints.net/U+0784>`_  '\\u0784'  Lo                  1  THAANA LETTER BAA
`U+07A7 <https://codepoints.net/U+07A7>`_  '\\u07a7'  Mn                  0  THAANA AABAAFILI
`U+0788 <https://codepoints.net/U+0788>`_  '\\u0788'  Lo                  1  THAANA LETTER VAAVU
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
`U+07AC <https://codepoints.net/U+07AC>`_  '\\u07ac'  Mn                  0  THAANA EBEFILI
`U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
`U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
`U+078E <https://codepoints.net/U+078E>`_  '\\u078e'  Lo                  1  THAANA LETTER GAAFU
`U+07AC <https://codepoints.net/U+07AC>`_  '\\u07ac'  Mn                  0  THAANA EBEFILI
=========================================  =========  ==========  =========  ===================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x84\xde\xa7\xde\x88\xde\xa6\xde\x8c\xde\xac\xde\x87\xde\xb0\xde\x8e\xde\xac|\\n12345|\\n"
        ބާވަތެއްގެ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 1.

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
=========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "le\xcc\x80|\\n12|\\n"
        lè|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width 1.

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "taa|\\n123|\\n"
        taa|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -3.

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "baawere|\\n1234567|\\n"
        baawere|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 2.

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
=========================================  =========  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe2\x80\x99kus|\\n1234|\\n"
        ’kus|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width 2.

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ==========
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ==========
`U+0031 <https://codepoints.net/U+0031>`_  '1'       Nd                  1  DIGIT ONE
`U+0030 <https://codepoints.net/U+0030>`_  '0'       Nd                  1  DIGIT ZERO
=========================================  ========  ==========  =========  ==========

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "10|\\n12|\\n"
        10|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -4.

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
=========================================  =========  ==========  =========  =========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gb\xc9\x94m\xc9\x94h\xc9\x94\xc9\x94m\xc9\x94|\\n1234567890|\\n"
        gbɔmɔhɔɔmɔ|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *tabby* measures width 8.

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "chi|\\n123|\\n"
        chi|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -3.

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kodo|\\n1234|\\n"
        kodo|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width 0.

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
`U+00F2 <https://codepoints.net/U+00F2>`_  '\\xf2'    Ll                  1  LATIN SMALL LETTER O WITH GRAVE
`U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
=========================================  =========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "w\xc3\xb2\xc5\x8b|\\n123|\\n"
        wòŋ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 0.

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0633 <https://codepoints.net/U+0633>`_  '\\u0633'  Lo                  1  ARABIC LETTER SEEN
=========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd8\xb3|\\n12|\\n"
        اس|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width 0.

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================
`U+067E <https://codepoints.net/U+067E>`_  '\\u067e'  Lo                  1  ARABIC LETTER PEH
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
=========================================  =========  ==========  =========  =================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\xbe\xd9\x87|\\n12|\\n"
        په|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -3.

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================
`U+0639 <https://codepoints.net/U+0639>`_  '\\u0639'  Lo                  1  ARABIC LETTER AIN
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
`U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
=========================================  =========  ==========  =========  =================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xb9\xd9\x82\xd9\x84|\\n123|\\n"
        عقل|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 0.

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc3\xa1a|\\n123|\\n"
        táa|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -1.

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
=========================================  =========  ==========  =========  =======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x84\xd8\xa7\xd9\x82\xd9\x88\xd8\xa7\xd9\x85\xdb\x8c|\\n12345678|\\n"
        الاقوامی|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 4.

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nga|\\n123|\\n"
        nga|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 1.

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===================================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+00F6 <https://codepoints.net/U+00F6>`_  '\\xf6'   Ll                  1  LATIN SMALL LETTER O WITH DIAERESIS
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ===================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "l\xc3\xb6i|\\n123|\\n"
        löi|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 0.

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
`U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "b\xc9\x94\xcc\x83\xc5\x8b\xc9\x94.|\\n12345|\\n"
        bɔ̃ŋɔ.|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width -2.

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pjekjo|\\n123456|\\n"
        pjekjo|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 3.

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "wara|\\n1234|\\n"
        wara|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width 3.

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================
`U+06D4 <https://codepoints.net/U+06D4>`_  '\\u06d4'  Po                  1  ARABIC FULL STOP
=========================================  =========  ==========  =========  ================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdb\x94|\\n1|\\n"
        ۔|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *tabby* measures width -3.

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "a|\\n1|\\n"
        a|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *tabby* measures width -4.

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "e|\\n1|\\n"
        e|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *tabby* measures width -2.

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tin\xc3\xad|\\n1234|\\n"
        tiní|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -2.

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0047 <https://codepoints.net/U+0047>`_  'G'        Lu                  1  LATIN CAPITAL LETTER G
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
`U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
=========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Gu\xcc\xb1jto|\\n12345|\\n"
        Gu̱jto|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 0.

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "e|\\n1|\\n"
        e|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *tabby* measures width -2.

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yon|\\n123|\\n"
        yon|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 1.

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+AA95 <https://codepoints.net/U+AA95>`_  '\\uaa95'  Lo                  1  TAI VIET LETTER HIGH TO
`U+AAB0 <https://codepoints.net/U+AAB0>`_  '\\uaab0'  Mn                  0  TAI VIET MAI KANG
`U+AA92 <https://codepoints.net/U+AA92>`_  '\\uaa92'  Lo                  1  TAI VIET LETTER LOW DO
=========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\x95\xea\xaa\xb0\xea\xaa\x92|\\n12|\\n"
        ꪕꪰꪒ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -1.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
