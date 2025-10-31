.. _LXTerminal:

LXTerminal
----------


Tested Software version 0.4.0(VTE/7600) on Linux
Full results available at ucs-detect_ repository path
`data/linux-LXTerminal-0.4.0.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-LXTerminal-0.4.0.yaml>`_

.. _LXTerminalscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *LXTerminal*:

============  ===========  ==============  ======================================================
Score Type    Raw Score    Scaled Score    Calculation
============  ===========  ==============  ======================================================
WIDE          72.73%       59.2%           (version_index / total_versions) × (pct_success / 100)
ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
LANG          1.68%        1.7%            languages_supported / total_languages
VS16          0.00%        0.0%            pct_success / 100
VS15          0.00%        0.0%            pct_success / 100
============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 14.88%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15) / 5
  the categorized 'average' absolute support level of this terminal

- Scaled Final Score: 9.2%
  (normalized across all terminals tested).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _LXTerminalwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for LXTerminal appears to be 
**15.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total  pct_success
=========  ==========  =========  =============
'9.0.0'             0       5000  100.0%
'10.0.0'            0        745  100.0%
'11.0.0'            0         72  100.0%
'12.0.0'            0         76  100.0%
'12.1.0'            0          1  100.0%
'13.0.0'            0        552  100.0%
'14.0.0'            0         54  100.0%
'15.0.0'            0         22  100.0%
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
  while *LXTerminal* measures width 1.

.. _LXTerminalzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *LXTerminal* appears to be 
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
  while *LXTerminal* measures width 9.

.. _LXTerminalvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *LXTerminal* is 213 errors
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
  while *LXTerminal* measures width 1.


.. _LXTerminalvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *LXTerminal* are not available.

.. _LXTerminallang:

Language Support
++++++++++++++++

The following 2 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog).

The following 117 languages are not fully supported:

===============================  ==========  =========  =============
lang                               n_errors    n_total  pct_success
===============================  ==========  =========  =============
Shan                                    868        915  5.1%
Tamil (Sri Lanka)                      1000       1074  6.9%
Tamil                                  1000       1075  7.0%
Sanskrit (Grantha)                      894       1006  11.1%
Javanese (Javanese)                    1000       1127  11.3%
Malayalam                              1000       1156  13.5%
Bengali                                1000       1165  14.2%
Khmer, Central                          448        528  15.2%
Kannada                                 902       1080  16.5%
Khün                                    361        442  18.3%
Burmese                                 974       1223  20.4%
Sanskrit                                753       1000  24.7%
Tamang, Eastern                          33         45  26.7%
Mon                                     677        946  28.4%
Marathi                                1000       1421  29.6%
Nepali                                  931       1385  32.8%
Gujarati                               1000       1520  34.2%
Telugu                                  714       1129  36.8%
Maithili                                955       1519  37.1%
Hindi                                  1000       1631  38.7%
Panjabi, Eastern                       1000       1831  45.4%
Sinhala                                 886       1655  46.5%
Bhojpuri                                880       1737  49.3%
Magahi                                  812       1716  52.7%
Chakma                                  494       1444  65.8%
Tibetan, Central                          4        280  98.6%
Japanese                                  4        299  98.7%
Nuosu                                     3        230  98.7%
Japanese (Osaka)                          4        308  98.7%
Japanese (Tokyo)                          4        320  98.8%
Dzongkha                                  4        359  98.9%
Vietnamese (Han nom)                      2        199  99.0%
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
Lao                                       4        426  99.1%
Chinese, Mandarin (Simplified)            2        225  99.1%
Thai                                      3        341  99.1%
Bora                                      6       1598  99.6%
Chickasaw                                 2        554  99.6%
Shipibo-Conibo                            9       2540  99.6%
Amarakaeri                                5       1446  99.7%
Evenki                                    3        899  99.7%
Nanai                                     4       1207  99.7%
Orok                                      4       1245  99.7%
Yaneshaʼ                                  8       2536  99.7%
Navajo                                    5       1600  99.7%
Gumuz                                     4       1283  99.7%
Veps                                      4       1323  99.7%
South Azerbaijani                         4       1396  99.7%
Secoya                                    4       1409  99.7%
(Yeonbyeon)                               3       1061  99.7%
Siona                                     4       1492  99.7%
Gilyak                                    4       1504  99.7%
Catalan (2)                               5       1909  99.7%
Mirandese                                 5       1966  99.7%
Korean                                    3       1185  99.7%
Pular (Adlam)                             4       1613  99.8%
Picard                                    5       2024  99.8%
Ticuna                                    5       2048  99.8%
Tem                                       4       1659  99.8%
Colorado                                  3       1263  99.8%
Yiddish, Eastern                          4       1775  99.8%
Saint Lucian Creole French                4       1777  99.8%
Éwé                                       5       2230  99.8%
Arabic, Standard                          3       1348  99.8%
Kabyle                                    4       1815  99.8%
Lingala (tones)                           4       1818  99.8%
Tamazight, Central Atlas                  4       1822  99.8%
Mixtec, Metlatónoc                        3       1367  99.8%
Fur                                       4       1838  99.8%
Gen                                       5       2309  99.8%
Uduk                                      7       3247  99.8%
Dari                                      4       1872  99.8%
Ditammari                                 4       1882  99.8%
Maori (2)                                 5       2385  99.8%
Maldivian                                 4       1918  99.8%
French (Welche)                           4       1928  99.8%
Yoruba                                    5       2454  99.8%
Waama                                     2       1000  99.8%
Dinka, Northeastern                       3       1529  99.8%
Ga                                        4       2039  99.8%
Aja                                       4       2061  99.8%
Dagaare, Southern                         5       2582  99.8%
Dendi                                     3       1569  99.8%
Mazahua Central                           3       1574  99.8%
Serer-Sine                                3       1596  99.8%
Lamnso'                                   4       2237  99.8%
Urdu                                      4       2237  99.8%
Pashto, Northern                          4       2242  99.8%
Seraiki                                   4       2242  99.8%
Belanda Viri                              4       2246  99.8%
Urdu (2)                                  4       2251  99.8%
Bamun                                     4       2285  99.8%
Chinantec, Chiltepec                      3       1729  99.8%
Assyrian Neo-Aramaic                      2       1160  99.8%
Panjabi, Western                          4       2419  99.8%
Farsi, Western                            3       1822  99.8%
Mòoré                                     4       2447  99.8%
Otomi, Mezquital                          3       1849  99.8%
Vietnamese                                4       2502  99.8%
Fon                                       4       2520  99.8%
Baatonum                                  3       1939  99.8%
Dangme                                    4       2912  99.9%
Tai Dam                                   3       2386  99.9%
===============================  ==========  =========  =============

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
  while *LXTerminal* measures width 9.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 14.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 21.

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
  while *LXTerminal* measures width 12.

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
  while *LXTerminal* measures width 25.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 15.

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
  while *LXTerminal* measures width 11.

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
  while *LXTerminal* measures width 13.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 7.

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
  while *LXTerminal* measures width 5.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 10.

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
  while *LXTerminal* measures width 7.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 4.

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
  while *LXTerminal* measures width 10.

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
  while *LXTerminal* measures width 10.

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
  while *LXTerminal* measures width 8.

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F5A <https://codepoints.net/U+0F5A>`_  '\\u0f5a'  Lo                  1  TIBETAN LETTER TSHA
`U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F45 <https://codepoints.net/U+0F45>`_  '\\u0f45'  Lo                  1  TIBETAN LETTER CA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F45 <https://codepoints.net/U+0F45>`_  '\\u0f45'  Lo                  1  TIBETAN LETTER CA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F54 <https://codepoints.net/U+0F54>`_  '\\u0f54'  Lo                  1  TIBETAN LETTER PA
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ================================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x91\xe0\xbd\xbc\xe0\xbd\x93\xe0\xbc\x8b\xe0\xbd\x9a\xe0\xbd\x93\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\x85\xe0\xbd\xb4\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\x85\xe0\xbd\xb2\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbc\x8d|\\n123456789012345|\\n"
        དོན་ཚན་བཅུ་གཅིག་པ།|
        123456789012345|

- python `wcwidth.wcswidth()`_ measures width 15,
  while *LXTerminal* measures width -52.

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
`U+3079 <https://codepoints.net/U+3079>`_  '\\u3079'  Lo                  2  HIRAGANA LETTER BE
`U+3066 <https://codepoints.net/U+3066>`_  '\\u3066'  Lo                  2  HIRAGANA LETTER TE
`U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
`U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
`U+306F <https://codepoints.net/U+306F>`_  '\\u306f'  Lo                  2  HIRAGANA LETTER HA
=========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\x99\xe3\x81\xb9\xe3\x81\xa6\xe3\x81\xae\xe4\xba\xba\xe3\x81\xaf|\\n123456789012|\\n"
        すべての人は|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *LXTerminal* measures width 6.

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============
`U+A22C <https://codepoints.net/U+A22C>`_  '\\ua22c'  Lo                  2  YI SYLLABLE GGU
`U+A3E2 <https://codepoints.net/U+A3E2>`_  '\\ua3e2'  Lo                  2  YI SYLLABLE JI
`U+A3E1 <https://codepoints.net/U+A3E1>`_  '\\ua3e1'  Lo                  2  YI SYLLABLE JIX
`U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
=========================================  =========  ==========  =========  ===============

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x88\xac\xea\x8f\xa2\xea\x8f\xa1\xea\x8c\xa0|\\n12345678|\\n"
        ꈬꏢꏡꌠ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width -50.

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+FF14 <https://codepoints.net/U+FF14>`_  '\\uff14'  Nd                  2  FULLWIDTH DIGIT FOUR
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xef\xbc\x94\xe6\x9d\xa1|\\n123456|\\n"
        第４条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -32.

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+3044 <https://codepoints.net/U+3044>`_  '\\u3044'  Lo                  2  HIRAGANA LETTER I
`U+304B <https://codepoints.net/U+304B>`_  '\\u304b'  Lo                  2  HIRAGANA LETTER KA
`U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
`U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
`U+5F62 <https://codepoints.net/U+5F62>`_  '\\u5f62'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F62
`U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
`U+304A <https://codepoints.net/U+304A>`_  '\\u304a'  Lo                  2  HIRAGANA LETTER O
`U+3044 <https://codepoints.net/U+3044>`_  '\\u3044'  Lo                  2  HIRAGANA LETTER I
`U+3066 <https://codepoints.net/U+3066>`_  '\\u3066'  Lo                  2  HIRAGANA LETTER TE
`U+3082 <https://codepoints.net/U+3082>`_  '\\u3082'  Lo                  2  HIRAGANA LETTER MO
`U+7981 <https://codepoints.net/U+7981>`_  '\\u7981'  Lo                  2  CJK UNIFIED IDEOGRAPH-7981
`U+6B62 <https://codepoints.net/U+6B62>`_  '\\u6b62'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B62
`U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
`U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
=========================================  =========  ==========  =========  ==========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\x84\xe3\x81\x8b\xe3\x81\xaa\xe3\x82\x8b\xe5\xbd\xa2\xe3\x81\xab\xe3\x81\x8a\xe3\x81\x84\xe3\x81\xa6\xe3\x82\x82\xe7\xa6\x81\xe6\xad\xa2\xe3\x81\x99\xe3\x82\x8b|\\n1234567890123456789012345678|\\n"
        いかなる形においても禁止する|
        1234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 28,
  while *LXTerminal* measures width 8.

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F64 <https://codepoints.net/U+0F64>`_  '\\u0f64'  Lo                  1  TIBETAN LETTER SHA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F40 <https://codepoints.net/U+0F40>`_  '\\u0f40'  Lo                  1  TIBETAN LETTER KA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
=========================================  =========  ==========  =========  ================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa4\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\x80\xe0\xbe\xb1\xe0\xbd\x82|\\n12345|\\n"
        ཤ་བཀྱག|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *LXTerminal* measures width -18.

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ===========================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ===========================
`U+8ABF <https://codepoints.net/U+8ABF>`_          '\\u8abf'      Lo                  2  CJK UNIFIED IDEOGRAPH-8ABF
`U+0002338F <https://codepoints.net/U+0002338F>`_  '\\U0002338f'  Lo                  2  CJK UNIFIED IDEOGRAPH-2338F
`U+6B0A <https://codepoints.net/U+6B0A>`_          '\\u6b0a'      Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
`U+5F97 <https://codepoints.net/U+5F97>`_          '\\u5f97'      Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+00020B20 <https://codepoints.net/U+00020B20>`_  '\\U00020b20'  Lo                  2  CJK UNIFIED IDEOGRAPH-20B20
`U+5EA7 <https://codepoints.net/U+5EA7>`_          '\\u5ea7'      Lo                  2  CJK UNIFIED IDEOGRAPH-5EA7
`U+6848 <https://codepoints.net/U+6848>`_          '\\u6848'      Lo                  2  CJK UNIFIED IDEOGRAPH-6848
`U+7368 <https://codepoints.net/U+7368>`_          '\\u7368'      Lo                  2  CJK UNIFIED IDEOGRAPH-7368
`U+7ACB <https://codepoints.net/U+7ACB>`_          '\\u7acb'      Lo                  2  CJK UNIFIED IDEOGRAPH-7ACB
`U+5427 <https://codepoints.net/U+5427>`_          '\\u5427'      Lo                  2  CJK UNIFIED IDEOGRAPH-5427
`U+7121 <https://codepoints.net/U+7121>`_          '\\u7121'      Lo                  2  CJK UNIFIED IDEOGRAPH-7121
`U+79C1 <https://codepoints.net/U+79C1>`_          '\\u79c1'      Lo                  2  CJK UNIFIED IDEOGRAPH-79C1
`U+5206 <https://codepoints.net/U+5206>`_          '\\u5206'      Lo                  2  CJK UNIFIED IDEOGRAPH-5206
`U+8655 <https://codepoints.net/U+8655>`_          '\\u8655'      Lo                  2  CJK UNIFIED IDEOGRAPH-8655
`U+516C <https://codepoints.net/U+516C>`_          '\\u516c'      Lo                  2  CJK UNIFIED IDEOGRAPH-516C
`U+5E73 <https://codepoints.net/U+5E73>`_          '\\u5e73'      Lo                  2  CJK UNIFIED IDEOGRAPH-5E73
`U+5427 <https://codepoints.net/U+5427>`_          '\\u5427'      Lo                  2  CJK UNIFIED IDEOGRAPH-5427
`U+516C <https://codepoints.net/U+516C>`_          '\\u516c'      Lo                  2  CJK UNIFIED IDEOGRAPH-516C
`U+958B <https://codepoints.net/U+958B>`_          '\\u958b'      Lo                  2  CJK UNIFIED IDEOGRAPH-958B
`U+62B5 <https://codepoints.net/U+62B5>`_          '\\u62b5'      Lo                  2  CJK UNIFIED IDEOGRAPH-62B5
`U+78BA <https://codepoints.net/U+78BA>`_          '\\u78ba'      Lo                  2  CJK UNIFIED IDEOGRAPH-78BA
`U+5B9A <https://codepoints.net/U+5B9A>`_          '\\u5b9a'      Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
`U+6B0A <https://codepoints.net/U+6B0A>`_          '\\u6b0a'      Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
=================================================  =============  ==========  =========  ===========================

Total codepoints: 23


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\xaa\xbf\xf0\xa3\x8e\x8f\xe6\xac\x8a\xe5\xbe\x97\xf0\xa0\xac\xa0\xe5\xba\xa7\xe6\xa1\x88\xe7\x8d\xa8\xe7\xab\x8b\xe5\x90\xa7\xe7\x84\xa1\xe7\xa7\x81\xe5\x88\x86\xe8\x99\x95\xe5\x85\xac\xe5\xb9\xb3\xe5\x90\xa7\xe5\x85\xac\xe9\x96\x8b\xe6\x8a\xb5\xe7\xa2\xba\xe5\xae\x9a\xe6\xac\x8a|\\n1234567890123456789012345678901234567890123456|\\n"
        調𣎏權得𠬠座案獨立吧無私分處公平吧公開抵確定權|
        1234567890123456789012345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 46,
  while *LXTerminal* measures width 28.

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
`U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
`U+0E20 <https://codepoints.net/U+0E20>`_  '\\u0e20'  Lo                  1  THAI CHARACTER PHO SAMPHAO
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E1E <https://codepoints.net/U+0E1E>`_  '\\u0e1e'  Lo                  1  THAI CHARACTER PHO PHAN
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x80\xe0\xb8\xaa\xe0\xb8\xa3\xe0\xb8\xb5\xe0\xb8\xa0\xe0\xb8\xb2\xe0\xb8\x9e|\\n123456|\\n"
        เสรีภาพ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -11.

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe6\x9d\xa1|\\n123456|\\n"
        第十条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -4.

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+70BA <https://codepoints.net/U+70BA>`_  '\\u70ba'  Lo                  2  CJK UNIFIED IDEOGRAPH-70BA
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe5\xbe\x97\xe8\xa2\xab\xe5\x88\xa4\xe7\x82\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n12345678901234567890|\\n"
        不得被判為犯有刑事罪|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *LXTerminal* measures width -22.

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+51E1 <https://codepoints.net/U+51E1>`_  '\\u51e1'  Lo                  2  CJK UNIFIED IDEOGRAPH-51E1
`U+4FC2 <https://codepoints.net/U+4FC2>`_  '\\u4fc2'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FC2
`U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+63A7 <https://codepoints.net/U+63A7>`_  '\\u63a7'  Lo                  2  CJK UNIFIED IDEOGRAPH-63A7
`U+544A <https://codepoints.net/U+544A>`_  '\\u544a'  Lo                  2  CJK UNIFIED IDEOGRAPH-544A
`U+5605 <https://codepoints.net/U+5605>`_  '\\u5605'  Lo                  2  CJK UNIFIED IDEOGRAPH-5605
`U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
=========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x87\xa1\xe4\xbf\x82\xe5\x8f\x97\xe5\x88\x91\xe4\xba\x8b\xe6\x8e\xa7\xe5\x91\x8a\xe5\x98\x85\xe4\xba\xba|\\n123456789012345678|\\n"
        凡係受刑事控告嘅人|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *LXTerminal* measures width 7.

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x80\xe6\x9d\xa1|\\n12345678|\\n"
        第十一条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width -40.

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x80\xe6\x9d\xa1|\\n12345678|\\n"
        第十一条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width -40.

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe6\x9d\xa1|\\n123456|\\n"
        第十条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -4.

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x80\xe6\x9d\xa1|\\n12345678|\\n"
        第十一条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width -42.

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+51E1 <https://codepoints.net/U+51E1>`_  '\\u51e1'  Lo                  2  CJK UNIFIED IDEOGRAPH-51E1
`U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+63A7 <https://codepoints.net/U+63A7>`_  '\\u63a7'  Lo                  2  CJK UNIFIED IDEOGRAPH-63A7
`U+544A <https://codepoints.net/U+544A>`_  '\\u544a'  Lo                  2  CJK UNIFIED IDEOGRAPH-544A
`U+8005 <https://codepoints.net/U+8005>`_  '\\u8005'  Lo                  2  CJK UNIFIED IDEOGRAPH-8005
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x87\xa1\xe5\x8f\x97\xe5\x88\x91\xe4\xba\x8b\xe6\x8e\xa7\xe5\x91\x8a\xe8\x80\x85|\\n12345678901234|\\n"
        凡受刑事控告者|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *LXTerminal* measures width 6.

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x80\xe6\x9d\xa1|\\n12345678|\\n"
        第十一条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width -40.

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+62D8 <https://codepoints.net/U+62D8>`_  '\\u62d8'  Lo                  2  CJK UNIFIED IDEOGRAPH-62D8
`U+7981 <https://codepoints.net/U+7981>`_  '\\u7981'  Lo                  2  CJK UNIFIED IDEOGRAPH-7981
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+653E <https://codepoints.net/U+653E>`_  '\\u653e'  Lo                  2  CJK UNIFIED IDEOGRAPH-653E
`U+9010 <https://codepoints.net/U+9010>`_  '\\u9010'  Lo                  2  CJK UNIFIED IDEOGRAPH-9010
=========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x8b\x98\xe7\xa6\x81\xe6\x88\x96\xe6\x94\xbe\xe9\x80\x90|\\n1234567890|\\n"
        拘禁或放逐|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *LXTerminal* measures width -12.

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x80\xe6\x9d\xa1|\\n12345678|\\n"
        第十一条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width -40.

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
`U+786E <https://codepoints.net/U+786E>`_  '\\u786e'  Lo                  2  CJK UNIFIED IDEOGRAPH-786E
`U+5B9A <https://codepoints.net/U+5B9A>`_  '\\u5b9a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
`U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
`U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
`U+4E49 <https://codepoints.net/U+4E49>`_  '\\u4e49'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E49
`U+52A1 <https://codepoints.net/U+52A1>`_  '\\u52a1'  Lo                  2  CJK UNIFIED IDEOGRAPH-52A1
`U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+5B9A <https://codepoints.net/U+5B9A>`_  '\\u5b9a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
`U+5BF9 <https://codepoints.net/U+5BF9>`_  '\\u5bf9'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BF9
`U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
`U+63D0 <https://codepoints.net/U+63D0>`_  '\\u63d0'  Lo                  2  CJK UNIFIED IDEOGRAPH-63D0
`U+51FA <https://codepoints.net/U+51FA>`_  '\\u51fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FA
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
`U+4F55 <https://codepoints.net/U+4F55>`_  '\\u4f55'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F55
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+6307 <https://codepoints.net/U+6307>`_  '\\u6307'  Lo                  2  CJK UNIFIED IDEOGRAPH-6307
`U+63A7 <https://codepoints.net/U+63A7>`_  '\\u63a7'  Lo                  2  CJK UNIFIED IDEOGRAPH-63A7
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
=========================================  =========  ==========  =========  ==========================

Total codepoints: 27


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xa5\xe7\xa1\xae\xe5\xae\x9a\xe4\xbb\x96\xe7\x9a\x84\xe6\x9d\x83\xe5\x88\xa9\xe5\x92\x8c\xe4\xb9\x89\xe5\x8a\xa1\xe5\xb9\xb6\xe5\x88\xa4\xe5\xae\x9a\xe5\xaf\xb9\xe4\xbb\x96\xe6\x8f\x90\xe5\x87\xba\xe7\x9a\x84\xe4\xbb\xbb\xe4\xbd\x95\xe5\x88\x91\xe4\xba\x8b\xe6\x8c\x87\xe6\x8e\xa7\xe7\x9a\x84\xe6\x9d\x83\xe5\x88\xa9|\\n123456789012345678901234567890123456789012345678901234|\\n"
        以确定他的权利和义务并判定对他提出的任何刑事指控的权利|
        123456789012345678901234567890123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 54,
  while *LXTerminal* measures width -12.

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
`U+786E <https://codepoints.net/U+786E>`_  '\\u786e'  Lo                  2  CJK UNIFIED IDEOGRAPH-786E
`U+5B9A <https://codepoints.net/U+5B9A>`_  '\\u5b9a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
`U+4F0A <https://codepoints.net/U+4F0A>`_  '\\u4f0a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F0A
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+4E49 <https://codepoints.net/U+4E49>`_  '\\u4e49'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E49
`U+52A1 <https://codepoints.net/U+52A1>`_  '\\u52a1'  Lo                  2  CJK UNIFIED IDEOGRAPH-52A1
`U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+5B9A <https://codepoints.net/U+5B9A>`_  '\\u5b9a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
`U+5BF9 <https://codepoints.net/U+5BF9>`_  '\\u5bf9'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BF9
`U+4F0A <https://codepoints.net/U+4F0A>`_  '\\u4f0a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F0A
`U+63D0 <https://codepoints.net/U+63D0>`_  '\\u63d0'  Lo                  2  CJK UNIFIED IDEOGRAPH-63D0
`U+51FA <https://codepoints.net/U+51FA>`_  '\\u51fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FA
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
`U+4F55 <https://codepoints.net/U+4F55>`_  '\\u4f55'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F55
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+6307 <https://codepoints.net/U+6307>`_  '\\u6307'  Lo                  2  CJK UNIFIED IDEOGRAPH-6307
`U+63A7 <https://codepoints.net/U+63A7>`_  '\\u63a7'  Lo                  2  CJK UNIFIED IDEOGRAPH-63A7
=========================================  =========  ==========  =========  ==========================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xa5\xe7\xa1\xae\xe5\xae\x9a\xe4\xbc\x8a\xe7\x9a\x84\xe6\x9d\x83\xe5\x88\xa9\xe5\x90\x88\xe4\xb9\x89\xe5\x8a\xa1\xe5\xb9\xb6\xe5\x88\xa4\xe5\xae\x9a\xe5\xaf\xb9\xe4\xbc\x8a\xe6\x8f\x90\xe5\x87\xba\xe7\x9a\x84\xe4\xbb\xbb\xe4\xbd\x95\xe5\x88\x91\xe4\xba\x8b\xe6\x8c\x87\xe6\x8e\xa7|\\n123456789012345678901234567890123456789012345678|\\n"
        以确定伊的权利合义务并判定对伊提出的任何刑事指控|
        123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 48,
  while *LXTerminal* measures width -14.

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe6\x9d\xa1|\\n123456|\\n"
        第十条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -4.

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0EC1 <https://codepoints.net/U+0EC1>`_  '\\u0ec1'  Lo                  1  LAO VOWEL SIGN EI
`U+0EA5 <https://codepoints.net/U+0EA5>`_  '\\u0ea5'  Lo                  1  LAO LETTER LO LOOT
`U+0EB0 <https://codepoints.net/U+0EB0>`_  '\\u0eb0'  Lo                  1  LAO VOWEL SIGN A
=========================================  =========  ==========  =========  ==================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbb\x81\xe0\xba\xa5\xe0\xba\xb0|\\n123|\\n"
        ແລະ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width -15.

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E5D <https://codepoints.net/U+4E5D>`_  '\\u4e5d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5D
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb9\x9d\xe6\x9d\xa1|\\n123456|\\n"
        第九条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -40.

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
`U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
`U+0E20 <https://codepoints.net/U+0E20>`_  '\\u0e20'  Lo                  1  THAI CHARACTER PHO SAMPHAO
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E1E <https://codepoints.net/U+0E1E>`_  '\\u0e1e'  Lo                  1  THAI CHARACTER PHO PHAN
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x80\xe0\xb8\xaa\xe0\xb8\xa3\xe0\xb8\xb5\xe0\xb8\xa0\xe0\xb8\xb2\xe0\xb8\x9e|\\n123456|\\n"
        เสรีภาพ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -17.

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0268 <https://codepoints.net/U+0268>`_  '\\u0268'  Ll                  1  LATIN SMALL LETTER I WITH STROKE
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0076 <https://codepoints.net/U+0076>`_  'v'        Ll                  1  LATIN SMALL LETTER V
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
=========================================  =========  ==========  =========  ================================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc9\xa8\xcc\x81tsaav\xc3\xa9m\xc3\xa9|\\n123456789|\\n"
        ɨ́tsaavémé|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *LXTerminal* measures width 3.

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kanihmi|\\n1234567|\\n"
        kanihmi|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *LXTerminal* measures width 1.

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ===============================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pec\xc3\xa1oritaanan|\\n1234567890123|\\n"
        pecáoritaanan|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *LXTerminal* measures width 11.

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ka'dik|\\n123456|\\n"
        ka'dik|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -2.

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================================
`U+04A3 <https://codepoints.net/U+04A3>`_  '\\u04a3'  Ll                  1  CYRILLIC SMALL LETTER EN WITH DESCENDER
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+002D <https://codepoints.net/U+002D>`_  '-'        Pd                  1  HYPHEN-MINUS
`U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
`U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
=========================================  =========  ==========  =========  =======================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd2\xa3\xd0\xb8-\xd0\xb2\xd1\x8d\xd0\xbb|\\n123456|\\n"
        ңи-вэл|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width -6.

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+043F <https://codepoints.net/U+043F>`_  '\\u043f'  Ll                  1  CYRILLIC SMALL LETTER PE
`U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+043A <https://codepoints.net/U+043A>`_  '\\u043a'  Ll                  1  CYRILLIC SMALL LETTER KA
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
=========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb8\xd0\xba\xd0\xb0\xd0\xb2\xd0\xb0|\\n1234567890|\\n"
        политикава|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *LXTerminal* measures width 2.

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
=========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x81\xd0\xb8\xd0\xbb\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb4\xd0\xb4\xd0\xb0|\\n1234567890|\\n"
        силланидда|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *LXTerminal* measures width 1.

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "cohuen|\\n123456|\\n"
        cohuen|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 0.

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'    Ll                  1  LATIN SMALL LETTER O WITH ACUTE
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+012F <https://codepoints.net/U+012F>`_  '\\u012f'  Ll                  1  LATIN SMALL LETTER I WITH OGONEK
`U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
=========================================  =========  ==========  =========  ================================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bee\xca\xbcaah\xc3\xb3ch\xc4\xaf\xca\xbc\xc3\xadg\xc3\xad\xc3\xad|\\n1234567890123456|\\n"
        beeʼaahóchįʼígíí|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *LXTerminal* measures width 13.

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+004B <https://codepoints.net/U+004B>`_  'K'        Lu                  1  LATIN CAPITAL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+0327 <https://codepoints.net/U+0327>`_  '\\u0327'  Mn                  0  COMBINING CEDILLA
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
=========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Kababac\xcc\xa7ama|\\n1234567890|\\n"
        Kababaçama|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *LXTerminal* measures width 6.

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "vai|\\n123|\\n"
        vai|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width -6.

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "olarak|\\n123456|\\n"
        olarak|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 1.

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ai|\\n12|\\n"
        ai|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -3.

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+CE68 <https://codepoints.net/U+CE68>`_  '\\uce68'  Lo                  2  HANGUL SYLLABLE CIM
`U+D574 <https://codepoints.net/U+D574>`_  '\\ud574'  Lo                  2  HANGUL SYLLABLE HAE
`U+BC1B <https://codepoints.net/U+BC1B>`_  '\\ubc1b'  Lo                  2  HANGUL SYLLABLE BAD
`U+B2E4 <https://codepoints.net/U+B2E4>`_  '\\ub2e4'  Lo                  2  HANGUL SYLLABLE DA
=========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\xb9\xa8\xed\x95\xb4\xeb\xb0\x9b\xeb\x8b\xa4|\\n12345678|\\n"
        침해받다|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width -2.

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===================================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
=========================================  ========  ==========  =========  ===================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yequ\xc3\xab|\\n12345|\\n"
        yequë|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *LXTerminal* measures width -2.

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================================
`U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
`U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
`U+043F <https://codepoints.net/U+043F>`_  '\\u043f'  Ll                  1  CYRILLIC SMALL LETTER PE
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
`U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
`U+0493 <https://codepoints.net/U+0493>`_  '\\u0493'  Ll                  1  CYRILLIC SMALL LETTER GHE WITH STROKE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
=========================================  =========  ==========  =========  =====================================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbc\xd0\xb5\xd1\x80\xd0\xbe\xd0\xbf\xd1\x80\xd1\x8f\xd1\x82\xd0\xb8\xd0\xb5\xd2\x93\xd1\x83\xd0\xbd|\\n1234567890123|\\n"
        меропрятиеғун|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *LXTerminal* measures width 5.

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "humans|\\n123456|\\n"
        humans|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 0.

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "lhibres|\\n1234567|\\n"
        lhibres|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *LXTerminal* measures width 2.

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+C81C <https://codepoints.net/U+C81C>`_  '\\uc81c'  Lo                  2  HANGUL SYLLABLE JE
=========================================  =========  ==========  =========  ==================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\xa0\x9c|\\n12|\\n"
        제|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -7.

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =======================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =======================
`U+0001E92C <https://codepoints.net/U+0001E92C>`_  '\\U0001e92c'  Ll                  1  ADLAM SMALL LETTER FA
`U+0001E92E <https://codepoints.net/U+0001E92E>`_  '\\U0001e92e'  Ll                  1  ADLAM SMALL LETTER O
`U+0001E93C <https://codepoints.net/U+0001E93C>`_  '\\U0001e93c'  Ll                  1  ADLAM SMALL LETTER TU
`U+0001E922 <https://codepoints.net/U+0001E922>`_  '\\U0001e922'  Ll                  1  ADLAM SMALL LETTER ALIF
`U+0001E944 <https://codepoints.net/U+0001E944>`_  '\\U0001e944'  Mn                  0  ADLAM ALIF LENGTHENER
`U+0001E932 <https://codepoints.net/U+0001E932>`_  '\\U0001e932'  Ll                  1  ADLAM SMALL LETTER NUN
`U+0001E92D <https://codepoints.net/U+0001E92D>`_  '\\U0001e92d'  Ll                  1  ADLAM SMALL LETTER I
=================================================  =============  ==========  =========  =======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xac\xf0\x9e\xa4\xae\xf0\x9e\xa4\xbc\xf0\x9e\xa4\xa2\xf0\x9e\xa5\x84\xf0\x9e\xa4\xb2\xf0\x9e\xa4\xad|\\n123456|\\n"
        𞤬𞤮𞤼𞤢𞥄𞤲𞤭|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 2.

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc3\xa8res|\\n12345|\\n"
        tères|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *LXTerminal* measures width 1.

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "i|\\n1|\\n"
        i|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *LXTerminal* measures width -8.

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "y\xc3\xa1\xc3\xa1|\\n123|\\n"
        yáá|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width -7.

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "weyanteri|\\n123456789|\\n"
        weyanteri|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *LXTerminal* measures width 2.

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+05D0 <https://codepoints.net/U+05D0>`_  '\\u05d0'  Lo                  1  HEBREW LETTER ALEF
`U+05B8 <https://codepoints.net/U+05B8>`_  '\\u05b8'  Mn                  0  HEBREW POINT QAMATS
`U+05D3 <https://codepoints.net/U+05D3>`_  '\\u05d3'  Lo                  1  HEBREW LETTER DALET
`U+05E2 <https://codepoints.net/U+05E2>`_  '\\u05e2'  Lo                  1  HEBREW LETTER AYIN
`U+05E8 <https://codepoints.net/U+05E8>`_  '\\u05e8'  Lo                  1  HEBREW LETTER RESH
=========================================  =========  ==========  =========  ===================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x90\xd6\xb8\xd7\x93\xd7\xa2\xd7\xa8|\\n1234|\\n"
        אָדער|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width -6.

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "di|\\n12|\\n"
        di|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -2.

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
=========================================  =========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kata\xcc\x83|\\n1234|\\n"
        katã|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width -6.

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0633 <https://codepoints.net/U+0633>`_  '\\u0633'  Lo                  1  ARABIC LETTER SEEN
`U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
`U+0629 <https://codepoints.net/U+0629>`_  '\\u0629'  Lo                  1  ARABIC LETTER TEH MARBUTA
=========================================  =========  ==========  =========  =========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x84\xd9\x82\xd8\xa7\xd8\xb3\xd9\x8a\xd8\xa9|\\n1234567|\\n"
        القاسية|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *LXTerminal* measures width -2.

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ilmend|\\n123456|\\n"
        ilmend|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 2.

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
=========================================  =========  ==========  =========  =========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ns\xc9\x94\xcc\x81mi\xcc\x81|\\n12345|\\n"
        nsɔ́mí|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *LXTerminal* measures width -1.

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+002D <https://codepoints.net/U+002D>`_  '-'       Pd                  1  HYPHEN-MINUS
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ghur-s|\\n123456|\\n"
        ghur-s|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 1.

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kunda'v\xc3\xad|\\n12345678|\\n"
        kunda'ví|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width 6.

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Inn\xc3\xa1|\\n1234|\\n"
        Inná|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width 0.

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  =================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  =================
`U+0028 <https://codepoints.net/U+0028>`_  '('       Ps                  1  LEFT PARENTHESIS
`U+0031 <https://codepoints.net/U+0031>`_  '1'       Nd                  1  DIGIT ONE
`U+0029 <https://codepoints.net/U+0029>`_  ')'       Pe                  1  RIGHT PARENTHESIS
=========================================  ========  ==========  =========  =================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "(1)|\\n123|\\n"
        (1)|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width -6.

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yansan|\\n123456|\\n"
        yansan|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 3.

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================
`U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
=========================================  =========  ==========  =========  =================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa8\xd9\x87|\\n12|\\n"
        به|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -4.

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yi|\\n12|\\n"
        yi|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -2.

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
  while *LXTerminal* measures width -3.

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+07A2 <https://codepoints.net/U+07A2>`_  '\\u07a2'  Lo                  1  THAANA LETTER AINU
`U+07A7 <https://codepoints.net/U+07A7>`_  '\\u07a7'  Mn                  0  THAANA AABAAFILI
`U+0782 <https://codepoints.net/U+0782>`_  '\\u0782'  Lo                  1  THAANA LETTER NOONU
`U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
`U+0789 <https://codepoints.net/U+0789>`_  '\\u0789'  Lo                  1  THAANA LETTER MEEMU
`U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
=========================================  =========  ==========  =========  ===================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\xa2\xde\xa7\xde\x82\xde\xb0\xde\x89\xde\xaa|\\n123|\\n"
        ޢާންމު|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width -3.

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+002D <https://codepoints.net/U+002D>`_  '-'        Pd                  1  HYPHEN-MINUS
`U+007A <https://codepoints.net/U+007A>`_  'z'        Ll                  1  LATIN SMALL LETTER Z
`U+002D <https://codepoints.net/U+002D>`_  '-'        Pd                  1  HYPHEN-MINUS
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
=========================================  =========  ==========  =========  ======================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "de\xcc\x81-z-aut|\\n12345678|\\n"
        dé-z-aut|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *LXTerminal* measures width 3.

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

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
  while *LXTerminal* measures width -2.

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "da|\\n12|\\n"
        da|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -6.

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bi|\\n12|\\n"
        bi|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -2.

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

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
  while *LXTerminal* measures width 0.

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nu|\\n12|\\n"
        nu|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -6.

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
=========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "p\xc9\x94ge|\\n1234|\\n"
        pɔge|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width 2.

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mani|\\n1234|\\n"
        mani|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width 0.

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ra|\\n12|\\n"
        ra|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -2.

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kiin.|\\n12345|\\n"
        kiin.|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *LXTerminal* measures width 3.

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+00EC <https://codepoints.net/U+00EC>`_  '\\xec'   Ll                  1  LATIN SMALL LETTER I WITH GRAVE
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
=========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "l\xc3\xacm|\\n123|\\n"
        lìm|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width 2.

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
=========================================  =========  ==========  =========  ==================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x88\xd8\xb1|\\n123|\\n"
        اور|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width -1.

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
=========================================  =========  ==========  =========  ==================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x85\xd9\x8a\xd9\x86\xd9\x8a|\\n1234|\\n"
        ميني|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width 0.

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
=========================================  =========  ==========  =========  ===================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xd9\x88|\\n12|\\n"
        کو|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -6.

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nako|\\n1234|\\n"
        nako|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width -2.

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================================
`U+0622 <https://codepoints.net/U+0622>`_  '\\u0622'  Lo                  1  ARABIC LETTER ALEF WITH MADDA ABOVE
`U+0632 <https://codepoints.net/U+0632>`_  '\\u0632'  Lo                  1  ARABIC LETTER ZAIN
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
=========================================  =========  ==========  =========  ===================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa2\xd8\xb2\xd8\xa7\xd8\xaf|\\n1234|\\n"
        آزاد|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width -2.

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
=========================================  =========  ==========  =========  ===========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "lo\xe2\x80\x99|\\n123|\\n"
        lo’|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width 0.

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0268 <https://codepoints.net/U+0268>`_  '\\u0268'  Ll                  1  LATIN SMALL LETTER I WITH STROKE
=========================================  =========  ==========  =========  ================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mugu\xc9\xa8|\\n12345|\\n"
        muguɨ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *LXTerminal* measures width 1.

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0721 <https://codepoints.net/U+0721>`_  '\\u0721'  Lo                  1  SYRIAC LETTER MIM
`U+0720 <https://codepoints.net/U+0720>`_  '\\u0720'  Lo                  1  SYRIAC LETTER LAMADH
`U+0718 <https://codepoints.net/U+0718>`_  '\\u0718'  Lo                  1  SYRIAC LETTER WAW
`U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
`U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
=========================================  =========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\xa1\xdc\xa0\xdc\x98\xdc\x90\xdc\x90|\\n12345|\\n"
        ܡܠܘܐܐ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *LXTerminal* measures width -2.

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================
`U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
=========================================  =========  ==========  =========  =================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xad\xd9\x82\xd9\x88\xd9\x82|\\n1234|\\n"
        حقوق|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width 2.

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+062C <https://codepoints.net/U+062C>`_  '\\u062c'  Lo                  1  ARABIC LETTER JEEM
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0632 <https://codepoints.net/U+0632>`_  '\\u0632'  Lo                  1  ARABIC LETTER ZAIN
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
=========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x85\xd8\xac\xd8\xa7\xd8\xb2\xd8\xa7\xd8\xaa|\\n123456|\\n"
        مجازات|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 4.

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "soaba.|\\n123456|\\n"
        soaba.|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *LXTerminal* measures width 5.

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+004B <https://codepoints.net/U+004B>`_  'K'        Lu                  1  LATIN CAPITAL LETTER K
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
=========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Ku\xcc\xb1ta|\\n1234|\\n"
        Ku̱ta|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *LXTerminal* measures width -3.

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================================
`U+0111 <https://codepoints.net/U+0111>`_  '\\u0111'  Ll                  1  LATIN SMALL LETTER D WITH STROKE
`U+00EA <https://codepoints.net/U+00EA>`_  '\\xea'    Ll                  1  LATIN SMALL LETTER E WITH CIRCUMFLEX
`U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
=========================================  =========  ==========  =========  ====================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc4\x91\xc3\xaa\xcc\x80u|\\n123|\\n"
        đều|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width -2.

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==============================
`U+0256 <https://codepoints.net/U+0256>`_  '\\u0256'  Ll                  1  LATIN SMALL LETTER D WITH TAIL
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
=========================================  =========  ==========  =========  ==============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc9\x96i|\\n12|\\n"
        ɖi|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -4.

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ka|\\n12|\\n"
        ka|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -6.

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0066 <https://codepoints.net/U+0066>`_  'f'        Ll                  1  LATIN SMALL LETTER F
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
=========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "f\xc9\x9b\xc9\x9b|\\n123|\\n"
        fɛɛ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *LXTerminal* measures width 1.

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+AAB9 <https://codepoints.net/U+AAB9>`_  '\\uaab9'  Lo                  1  TAI VIET VOWEL UEA
`U+AA8F <https://codepoints.net/U+AA8F>`_  '\\uaa8f'  Lo                  1  TAI VIET LETTER HIGH SO
`U+AAB7 <https://codepoints.net/U+AAB7>`_  '\\uaab7'  Mn                  0  TAI VIET MAI KHIT
=========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xb9\xea\xaa\x8f\xea\xaa\xb7|\\n12|\\n"
        ꪹꪏꪷ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *LXTerminal* measures width -1.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
