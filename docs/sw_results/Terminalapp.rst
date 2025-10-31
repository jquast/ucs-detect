.. _Terminalapp:

Terminal.app
------------


Tested Software version 2.15 (464) on Darwin
Full results available at ucs-detect_ repository path
`data/macos-Terminal-2.15.yaml <https://github.com/jquast/ucs-detect/blob/master/data/macos-Terminal-2.15.yaml>`_

.. _Terminalappscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *Terminal.app*:

============  ===========  ==============  ======================================================
Score Type    Raw Score    Scaled Score    Calculation
============  ===========  ==============  ======================================================
WIDE          90.91%       86.4%           (version_index / total_versions) × (pct_success / 100)
ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
LANG          0.84%        0.9%            languages_supported / total_languages
VS16          0.00%        0.0%            pct_success / 100
VS15          0.00%        0.0%            pct_success / 100
============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 18.35%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15) / 5
  the categorized 'average' absolute support level of this terminal

- Scaled Final Score: 13.6%
  (normalized across all terminals tested).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _Terminalappwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Terminal.app appears to be 
**16.0.0**, this is from a summary of the following
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
'15.1.0'            0          5  100.0%
'16.0.0'            0        198  100.0%
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
  while *Terminal.app* measures width 1.

.. _Terminalappzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Terminal.app* appears to be 
**None**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total  pct_success
=========  ==========  =========  =============
'2.0'              22         22  0.0%
'4.0'             579        579  0.0%
'5.0'             100        100  0.0%
'11.0'             73         73  0.0%
'12.0'            112        112  0.0%
'12.1'            165        165  0.0%
'13.0'             51         51  0.0%
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
  while *Terminal.app* measures width 11.

.. _Terminalappvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Terminal.app* is 213 errors
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
  while *Terminal.app* measures width 1.


.. _Terminalappvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *Terminal.app* are not available.

.. _Terminalapplang:

Language Support
++++++++++++++++

The following 1 languages were tested with 100% success:

Tagalog (Tagalog).

The following 118 languages are not fully supported:

===============================  ==========  =========  =============
lang                               n_errors    n_total  pct_success
===============================  ==========  =========  =============
Javanese (Javanese)                    1000       1027  2.6%
Shan                                    868        915  5.1%
Tamil (Sri Lanka)                      1000       1074  6.9%
Tamil                                  1000       1075  7.0%
Malayalam                              1000       1098  8.9%
Sanskrit (Grantha)                      893       1006  11.2%
Bengali                                1000       1161  13.9%
Khmer, Central                          448        528  15.2%
Kannada                                 903       1080  16.4%
Khün                                    362        442  18.1%
Burmese                                 974       1223  20.4%
Sanskrit                                755       1000  24.5%
Tamang, Eastern                          33         45  26.7%
Mon                                     676        946  28.5%
Marathi                                1000       1420  29.6%
Nepali                                  931       1385  32.8%
Gujarati                               1000       1519  34.2%
Telugu                                  716       1129  36.6%
Maithili                                955       1519  37.1%
Hindi                                  1000       1624  38.4%
Panjabi, Eastern                       1000       1831  45.4%
Sinhala                                 888       1655  46.3%
Bhojpuri                                880       1737  49.3%
Magahi                                  812       1716  52.7%
Chakma                                  492       1444  65.9%
Mongolian, Halh (Mongolian)               3         33  90.9%
Farsi, Western                           43       1822  97.6%
Dari                                     40       1872  97.9%
Tibetan, Central                          4        280  98.6%
Chinese, Mandarin (Tianjin)               3        212  98.6%
Japanese                                  4        299  98.7%
Chinese, Mandarin (Simplified)            3        225  98.7%
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
Chinese, Min Nan                          2        212  99.1%
Chinese, Xiang                            2        212  99.1%
Lao                                       4        426  99.1%
Thai                                      3        341  99.1%
Bora                                      7       1598  99.6%
Gumuz                                     5       1283  99.6%
Chickasaw                                 2        554  99.6%
Yaneshaʼ                                  9       2536  99.6%
Shipibo-Conibo                            9       2540  99.6%
Amarakaeri                                5       1446  99.7%
Siona                                     5       1492  99.7%
Evenki                                    3        899  99.7%
Gilyak                                    5       1504  99.7%
Nanai                                     4       1207  99.7%
Orok                                      4       1245  99.7%
Navajo                                    5       1600  99.7%
Veps                                      4       1323  99.7%
South Azerbaijani                         4       1396  99.7%
Secoya                                    4       1409  99.7%
(Yeonbyeon)                               3       1061  99.7%
Yiddish, Eastern                          5       1775  99.7%
Catalan (2)                               5       1909  99.7%
Mirandese                                 5       1966  99.7%
Korean                                    3       1185  99.7%
Panjabi, Western                          6       2419  99.8%
Pular (Adlam)                             4       1613  99.8%
Picard                                    5       2024  99.8%
Ticuna                                    5       2048  99.8%
Tem                                       4       1659  99.8%
Colorado                                  3       1263  99.8%
Saint Lucian Creole French                4       1777  99.8%
Éwé                                       5       2230  99.8%
Urdu                                      5       2237  99.8%
Arabic, Standard                          3       1348  99.8%
Urdu (2)                                  5       2251  99.8%
Kabyle                                    4       1815  99.8%
Lingala (tones)                           4       1818  99.8%
Tamazight, Central Atlas                  4       1822  99.8%
Mixtec, Metlatónoc                        3       1367  99.8%
Fur                                       4       1838  99.8%
Gen                                       5       2309  99.8%
Uduk                                      7       3247  99.8%
Ditammari                                 4       1882  99.8%
Maori (2)                                 5       2385  99.8%
Maldivian                                 4       1918  99.8%
French (Welche)                           4       1928  99.8%
Mòoré                                     5       2447  99.8%
Yoruba                                    5       2454  99.8%
Waama                                     2       1000  99.8%
Vietnamese                                5       2502  99.8%
Dinka, Northeastern                       3       1529  99.8%
Ga                                        4       2039  99.8%
Aja                                       4       2061  99.8%
Dagaare, Southern                         5       2582  99.8%
Dendi                                     3       1569  99.8%
Mazahua Central                           3       1574  99.8%
Serer-Sine                                3       1596  99.8%
Lamnso'                                   4       2237  99.8%
Pashto, Northern                          4       2242  99.8%
Seraiki                                   4       2242  99.8%
Belanda Viri                              4       2246  99.8%
Bamun                                     4       2285  99.8%
Chinantec, Chiltepec                      3       1729  99.8%
Assyrian Neo-Aramaic                      2       1160  99.8%
Otomi, Mezquital                          3       1849  99.8%
Fon                                       4       2520  99.8%
Baatonum                                  3       1939  99.8%
Dangme                                    4       2912  99.9%
Tai Dam                                   3       2386  99.9%
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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 9.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 21.

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
  while *Terminal.app* measures width 14.

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
  while *Terminal.app* measures width 12.

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
  while *Terminal.app* measures width 25.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 15.

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
  while *Terminal.app* measures width 11.

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
  while *Terminal.app* measures width 13.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 7.

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
  while *Terminal.app* measures width 5.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 10.

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
  while *Terminal.app* measures width 7.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 4.

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
  while *Terminal.app* measures width 10.

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
  while *Terminal.app* measures width 10.

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
  while *Terminal.app* measures width 8.

Mongolian, Halh (Mongolian)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Mongolian, Halh (Mongolian)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+1828 <https://codepoints.net/U+1828>`_  '\\u1828'  Lo                  1  MONGOLIAN LETTER NA
`U+1821 <https://codepoints.net/U+1821>`_  '\\u1821'  Lo                  1  MONGOLIAN LETTER E
`U+1837 <https://codepoints.net/U+1837>`_  '\\u1837'  Lo                  1  MONGOLIAN LETTER RA
`U+180E <https://codepoints.net/U+180E>`_  '\\u180e'  Cf                  0  MONGOLIAN VOWEL SEPARATOR
`U+1821 <https://codepoints.net/U+1821>`_  '\\u1821'  Lo                  1  MONGOLIAN LETTER E
=========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa0\xa8\xe1\xa0\xa1\xe1\xa0\xb7\xe1\xa0\x8e\xe1\xa0\xa1|\\n1234|\\n"
        ᠨᠡᠷ᠎ᠡ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width 5.

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
`U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
`U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
=========================================  =========  ==========  =========  =======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88\xd8\xad\xd8\xb4\xdb\x8c\xd8\xa7\xd9\x86\xd9\x87\xe2\x80\x8c\xd8\xa7\xdb\x8c|\\n123456789|\\n"
        وحشیانه‌ای|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Terminal.app* measures width 10.

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
`U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
`U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
=========================================  =========  ==========  =========  =======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88\xd8\xad\xd8\xb4\xdb\x8c\xd8\xa7\xd9\x86\xd9\x87\xe2\x80\x8c\xdb\x8c\xdb\x8c|\\n123456789|\\n"
        وحشیانه‌یی|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Terminal.app* measures width 10.

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F50 <https://codepoints.net/U+0F50>`_  '\\u0f50'  Lo                  1  TIBETAN LETTER THA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F50 <https://codepoints.net/U+0F50>`_  '\\u0f50'  Lo                  1  TIBETAN LETTER THA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F90 <https://codepoints.net/U+0F90>`_  '\\u0f90'  Mn                  0  TIBETAN SUBJOINED LETTER KA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F50 <https://codepoints.net/U+0F50>`_  '\\u0f50'  Lo                  1  TIBETAN LETTER THA
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F45 <https://codepoints.net/U+0F45>`_  '\\u0f45'  Lo                  1  TIBETAN LETTER CA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F54 <https://codepoints.net/U+0F54>`_  '\\u0f54'  Lo                  1  TIBETAN LETTER PA
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ================================

Total codepoints: 44


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x82\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\xbc\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x82\xe0\xbd\x93\xe0\xbc\x8b\xe0\xbd\xa6\xe0\xbe\x90\xe0\xbd\xbc\xe0\xbd\xa2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\x85\xe0\xbd\xbc\xe0\xbd\x91\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbe\xb1\xe0\xbd\xba\xe0\xbd\x91\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbc\x8d|\\n123456789012345678901234567890123456|\\n"
        གང་གི་ཐོབ་ཐང་དང་འོས་འགན་སྐོར་ཐག་གཅོད་བྱེད་པ།|
        123456789012345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 36,
  while *Terminal.app* measures width -55.

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -42.

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+53C8 <https://codepoints.net/U+53C8>`_  '\\u53c8'  Lo                  2  CJK UNIFIED IDEOGRAPH-53C8
`U+306F <https://codepoints.net/U+306F>`_  '\\u306f'  Lo                  2  HIRAGANA LETTER HA
`U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
`U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
`U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
`U+3093 <https://codepoints.net/U+3093>`_  '\\u3093'  Lo                  2  HIRAGANA LETTER N
`U+3089 <https://codepoints.net/U+3089>`_  '\\u3089'  Lo                  2  HIRAGANA LETTER RA
`U+304B <https://codepoints.net/U+304B>`_  '\\u304b'  Lo                  2  HIRAGANA LETTER KA
`U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
`U+4E3B <https://codepoints.net/U+4E3B>`_  '\\u4e3b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3B
`U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
`U+5236 <https://codepoints.net/U+5236>`_  '\\u5236'  Lo                  2  CJK UNIFIED IDEOGRAPH-5236
`U+9650 <https://codepoints.net/U+9650>`_  '\\u9650'  Lo                  2  CJK UNIFIED IDEOGRAPH-9650
`U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
`U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
`U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
`U+3042 <https://codepoints.net/U+3042>`_  '\\u3042'  Lo                  2  HIRAGANA LETTER A
`U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
`U+3068 <https://codepoints.net/U+3068>`_  '\\u3068'  Lo                  2  HIRAGANA LETTER TO
`U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
`U+554F <https://codepoints.net/U+554F>`_  '\\u554f'  Lo                  2  CJK UNIFIED IDEOGRAPH-554F
`U+308F <https://codepoints.net/U+308F>`_  '\\u308f'  Lo                  2  HIRAGANA LETTER WA
`U+305A <https://codepoints.net/U+305A>`_  '\\u305a'  Lo                  2  HIRAGANA LETTER ZU
=========================================  =========  ==========  =========  ==========================

Total codepoints: 23


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8f\x88\xe3\x81\xaf\xe4\xbb\x96\xe3\x81\xae\xe3\x81\xaa\xe3\x82\x93\xe3\x82\x89\xe3\x81\x8b\xe3\x81\xae\xe4\xb8\xbb\xe6\xa8\xa9\xe5\x88\xb6\xe9\x99\x90\xe3\x81\xae\xe4\xb8\x8b\xe3\x81\xab\xe3\x81\x82\xe3\x82\x8b\xe3\x81\xa8\xe3\x82\x92\xe5\x95\x8f\xe3\x82\x8f\xe3\x81\x9a|\\n1234567890123456789012345678901234567890123456|\\n"
        又は他のなんらかの主権制限の下にあるとを問わず|
        1234567890123456789012345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 46,
  while *Terminal.app* measures width 26.

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+516D <https://codepoints.net/U+516D>`_  '\\u516d'  Lo                  2  CJK UNIFIED IDEOGRAPH-516D
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x85\xad\xe6\x9d\xa1|\\n123456|\\n"
        第六条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width -22.

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================
`U+A246 <https://codepoints.net/U+A246>`_  '\\ua246'  Lo                  2  YI SYLLABLE HXIT
`U+A3E2 <https://codepoints.net/U+A3E2>`_  '\\ua3e2'  Lo                  2  YI SYLLABLE JI
`U+A3E1 <https://codepoints.net/U+A3E1>`_  '\\ua3e1'  Lo                  2  YI SYLLABLE JIX
`U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
=========================================  =========  ==========  =========  ================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x89\x86\xea\x8f\xa2\xea\x8f\xa1\xea\x8c\xa0|\\n12345678|\\n"
        ꉆꏢꏡꌠ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Terminal.app* measures width -42.

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+FF13 <https://codepoints.net/U+FF13>`_  '\\uff13'  Nd                  2  FULLWIDTH DIGIT THREE
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xef\xbc\x93\xe6\x9d\xa1|\\n123456|\\n"
        第３条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width -52.

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+FF13 <https://codepoints.net/U+FF13>`_  '\\uff13'  Nd                  2  FULLWIDTH DIGIT THREE
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xef\xbc\x93\xe6\x9d\xa1|\\n123456|\\n"
        第３条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width -52.

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F45 <https://codepoints.net/U+0F45>`_  '\\u0f45'  Lo                  1  TIBETAN LETTER CA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F45 <https://codepoints.net/U+0F45>`_  '\\u0f45'  Lo                  1  TIBETAN LETTER CA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0FA4 <https://codepoints.net/U+0FA4>`_  '\\u0fa4'  Mn                  0  TIBETAN SUBJOINED LETTER PA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F46 <https://codepoints.net/U+0F46>`_  '\\u0f46'  Lo                  1  TIBETAN LETTER CHA
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F64 <https://codepoints.net/U+0F64>`_  '\\u0f64'  Lo                  1  TIBETAN LETTER SHA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F90 <https://codepoints.net/U+0F90>`_  '\\u0f90'  Mn                  0  TIBETAN SUBJOINED LETTER KA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F50 <https://codepoints.net/U+0F50>`_  '\\u0f50'  Lo                  1  TIBETAN LETTER THA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
`U+0F71 <https://codepoints.net/U+0F71>`_  '\\u0f71'  Mn                  0  TIBETAN VOWEL SIGN AA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ================================

Total codepoints: 59


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x82\xe0\xbd\x85\xe0\xbd\xb2\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\xb2\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\x85\xe0\xbd\xb2\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\xa3\xe0\xbd\xb4\xe0\xbc\x8b\xe0\xbd\xa6\xe0\xbe\xa4\xe0\xbd\xb4\xe0\xbd\x93\xe0\xbc\x8b\xe0\xbd\x86\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x91\xe0\xbd\xb4\xe0\xbc\x8b\xe0\xbd\xa4\xe0\xbd\xba\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\xa6\xe0\xbe\x90\xe0\xbe\xb1\xe0\xbd\xba\xe0\xbd\x91\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\xa3\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\xa3\xe0\xbd\xb1\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x96\xe0\xbd\x91\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x82\xe0\xbd\xbc\xe0\xbc\x8d|\\n12345678901234567890123456789012345678901234|\\n"
        གཅིག་གིས་གཅིག་ལུ་སྤུན་ཆའི་འདུ་ཤེས་བསྐྱེད་ཐོག་ལས་ལཱ་འབད་དགོ།|
        12345678901234567890123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 44,
  while *Terminal.app* measures width 22.

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
  while *Terminal.app* measures width 26.

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
  while *Terminal.app* measures width -25.

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -12.

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
`U+689D <https://codepoints.net/U+689D>`_  '\\u689d'  Lo                  2  CJK UNIFIED IDEOGRAPH-689D
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe6\xa2\x9d|\\n123456|\\n"
        第十條|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width -4.

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -42.

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -12.

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -8.

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -12.

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
`U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
`U+683C <https://codepoints.net/U+683C>`_  '\\u683c'  Lo                  2  CJK UNIFIED IDEOGRAPH-683C
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+5EAD <https://codepoints.net/U+5EAD>`_  '\\u5ead'  Lo                  2  CJK UNIFIED IDEOGRAPH-5EAD
`U+5BF9 <https://codepoints.net/U+5BF9>`_  '\\u5bf9'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BF9
`U+63B0 <https://codepoints.net/U+63B0>`_  '\\u63b0'  Lo                  2  CJK UNIFIED IDEOGRAPH-63B0
`U+6392 <https://codepoints.net/U+6392>`_  '\\u6392'  Lo                  2  CJK UNIFIED IDEOGRAPH-6392
`U+91CC <https://codepoints.net/U+91CC>`_  '\\u91cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-91CC
`U+4FB5 <https://codepoints.net/U+4FB5>`_  '\\u4fb5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FB5
`U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
`U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+4F5C <https://codepoints.net/U+4F5C>`_  '\\u4f5c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F5C
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+6548 <https://codepoints.net/U+6548>`_  '\\u6548'  Lo                  2  CJK UNIFIED IDEOGRAPH-6548
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+8865 <https://codepoints.net/U+8865>`_  '\\u8865'  Lo                  2  CJK UNIFIED IDEOGRAPH-8865
`U+6551 <https://codepoints.net/U+6551>`_  '\\u6551'  Lo                  2  CJK UNIFIED IDEOGRAPH-6551
=========================================  =========  ==========  =========  ==========================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x9c\x89\xe6\x9d\x83\xe7\x94\xb1\xe5\x90\x88\xe6\xa0\xbc\xe4\xb8\xaa\xe5\x9b\xbd\xe5\xae\xb6\xe6\xb3\x95\xe5\xba\xad\xe5\xaf\xb9\xe6\x8e\xb0\xe6\x8e\x92\xe9\x87\x8c\xe4\xbe\xb5\xe5\xae\xb3\xe8\xa1\x8c\xe4\xb8\xba\xe4\xbd\x9c\xe6\x9c\x89\xe6\x95\x88\xe4\xb8\xaa\xe8\xa1\xa5\xe6\x95\x91|\\n123456789012345678901234567890123456789012345678|\\n"
        有权由合格个国家法庭对掰排里侵害行为作有效个补救|
        123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 48,
  while *Terminal.app* measures width -2.

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -2.

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -12.

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -46.

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -12.

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -4.

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -10.

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
  while *Terminal.app* measures width -9.

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0E46 <https://codepoints.net/U+0E46>`_  '\\u0e46'  Lm                  1  THAI CHARACTER MAIYAMOK
=========================================  =========  ==========  =========  =======================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x86|\\n1|\\n"
        ๆ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Terminal.app* measures width -24.

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0050 <https://codepoints.net/U+0050>`_  'P'       Lu                  1  LATIN CAPITAL LETTER P
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "'P\xc3\xa1n\xc3\xa9|\\n12345|\\n"
        'Páné|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width -4.

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "polotika|\\n12345678|\\n"
        polotika|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Terminal.app* measures width 0.

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
=========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yamma\xcc\xb1|\\n12345|\\n"
        yamma̱|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width -2.

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "o'ch|\\n1234|\\n"
        o'ch|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width -2.

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "shinan|\\n123456|\\n"
        shinan|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width 1.

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
`U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
=========================================  =========  ==========  =========  ======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nopoe\xcc\xb1'dik|\\n123456789|\\n"
        nopoe̱'dik|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Terminal.app* measures width -2.

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===================================
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ===================================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "goachase's\xc3\xabte|\\n1234567890123|\\n"
        goachase'sëte|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *Terminal.app* measures width 9.

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+044E <https://codepoints.net/U+044E>`_  '\\u044e'  Ll                  1  CYRILLIC SMALL LETTER YU
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
=========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb4\xd1\x8e\xd0\xbb\xd1\x8d\xd0\xb4\xd1\x83\xd0\xbd|\\n1234567|\\n"
        дюлэдун|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Terminal.app* measures width 4.

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================================
`U+043F <https://codepoints.net/U+043F>`_  '\\u043f'  Ll                  1  CYRILLIC SMALL LETTER PE
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
`U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
`U+0493 <https://codepoints.net/U+0493>`_  '\\u0493'  Ll                  1  CYRILLIC SMALL LETTER GHE WITH STROKE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
=========================================  =========  ==========  =========  =====================================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbe\xd2\x93\xd1\x83\xd0\xbd|\\n12345678|\\n"
        правоғун|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Terminal.app* measures width 5.

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
=========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb1\xd0\xb8\xd0\xbc\xd0\xb8\xd1\x83|\\n12345|\\n"
        бимиу|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width 1.

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0445 <https://codepoints.net/U+0445>`_  '\\u0445'  Ll                  1  CYRILLIC SMALL LETTER HA
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
=========================================  =========  ==========  =========  ========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x85\xd0\xb0\xd0\xb8\xd0\xb2\xd0\xb0\xd0\xb4\xd0\xb4\xd0\xb0\xcc\x84|\\n12345678|\\n"
        хаивадда̄|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Terminal.app* measures width -5.

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  =================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  =================================
`U+00C1 <https://codepoints.net/U+00C1>`_  '\\xc1'   Lu                  1  LATIN CAPITAL LETTER A WITH ACUTE
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'   Ll                  1  LATIN SMALL LETTER O WITH ACUTE
`U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'   Ll                  1  LATIN SMALL LETTER O WITH ACUTE
=========================================  ========  ==========  =========  =================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\x81\xc3\xa1d\xc3\xb3\xc3\xb3|\\n12345|\\n"
        Áádóó|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width -7.

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
=========================================  =========  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pol\xe2\x80\x99|\\n1234|\\n"
        pol’|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width -1.

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0308 <https://codepoints.net/U+0308>`_  '\\u0308'  Mn                  0  COMBINING DIAERESIS
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
=========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "u\xcc\x88ye|\\n123|\\n"
        üye|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width 0.

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===================================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
=========================================  ========  ==========  =========  ===================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yek\xc3\xab|\\n1234|\\n"
        yekë|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width -3.

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+BCF4 <https://codepoints.net/U+BCF4>`_  '\\ubcf4'  Lo                  2  HANGUL SYLLABLE BO
`U+D638 <https://codepoints.net/U+D638>`_  '\\ud638'  Lo                  2  HANGUL SYLLABLE HO
`U+B97C <https://codepoints.net/U+B97C>`_  '\\ub97c'  Lo                  2  HANGUL SYLLABLE REUL
=========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xeb\xb3\xb4\xed\x98\xb8\xeb\xa5\xbc|\\n123456|\\n"
        보호를|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width -2.

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+202E <https://codepoints.net/U+202E>`_  '\\u202e'  Cf                  0  RIGHT-TO-LEFT OVERRIDE
`U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
`U+202C <https://codepoints.net/U+202C>`_  '\\u202c'  Cf                  0  POP DIRECTIONAL FORMATTING
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe2\x80\xaeA\xe2\x80\xac|\\n1|\\n"
        ‮A‬|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Terminal.app* measures width 3.

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "membres|\\n1234567|\\n"
        membres|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Terminal.app* measures width 1.

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "cumo|\\n1234|\\n"
        cumo|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width -3.

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+C794 <https://codepoints.net/U+C794>`_  '\\uc794'  Lo                  2  HANGUL SYLLABLE JAN
`U+D639 <https://codepoints.net/U+D639>`_  '\\ud639'  Lo                  2  HANGUL SYLLABLE HOG
`U+D558 <https://codepoints.net/U+D558>`_  '\\ud558'  Lo                  2  HANGUL SYLLABLE HA
`U+AC70 <https://codepoints.net/U+AC70>`_  '\\uac70'  Lo                  2  HANGUL SYLLABLE GEO
`U+B098 <https://codepoints.net/U+B098>`_  '\\ub098'  Lo                  2  HANGUL SYLLABLE NA
=========================================  =========  ==========  =========  ===================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x9e\x94\xed\x98\xb9\xed\x95\x98\xea\xb1\xb0\xeb\x82\x98|\\n1234567890|\\n"
        잔혹하거나|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Terminal.app* measures width 6.

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
`U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
=========================================  =========  ==========  =========  ===================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xd8\xb1\xd9\x88\xd8\xa7\xd9\x86|\\n12345|\\n"
        کروان|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width 0.

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
  while *Terminal.app* measures width -5.

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "r\xc3\xa8y\xc3\xa9le|\\n123456|\\n"
        rèyéle|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width 0.

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
  while *Terminal.app* measures width -8.

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+028A <https://codepoints.net/U+028A>`_  '\\u028a'  Ll                  1  LATIN SMALL LETTER UPSILON
`U+028A <https://codepoints.net/U+028A>`_  '\\u028a'  Ll                  1  LATIN SMALL LETTER UPSILON
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
=========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tan\xca\x8a\xca\x8a\xcc\x81|\\n12345|\\n"
        tanʊʊ́|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width -4.

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "i'toe|\\n12345|\\n"
        i'toe|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width -1.

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
=========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "e\xcc\x81ben|\\n1234|\\n"
        ében|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width -4.

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "siwo|\\n1234|\\n"
        siwo|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width -9.

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================================
`U+0601 <https://codepoints.net/U+0601>`_  '\\u0601'  Cf                  0  ARABIC SIGN SANAH
`U+06F1 <https://codepoints.net/U+06F1>`_  '\\u06f1'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT ONE
`U+06F9 <https://codepoints.net/U+06F9>`_  '\\u06f9'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT NINE
`U+06F4 <https://codepoints.net/U+06F4>`_  '\\u06f4'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT FOUR
`U+06F8 <https://codepoints.net/U+06F8>`_  '\\u06f8'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT EIGHT
`U+0621 <https://codepoints.net/U+0621>`_  '\\u0621'  Lo                  1  ARABIC LETTER HAMZA
=========================================  =========  ==========  =========  =================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\x81\xdb\xb1\xdb\xb9\xdb\xb4\xdb\xb8\xd8\xa1|\\n12345|\\n"
        ؁۱۹۴۸ء|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width 6.

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
`U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
`U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
=========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x84\xd8\xb1\xd9\x82\xd9\x8a\xd9\x82|\\n123456|\\n"
        الرقيق|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width 0.

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================================
`U+0601 <https://codepoints.net/U+0601>`_  '\\u0601'  Cf                  0  ARABIC SIGN SANAH
`U+06F1 <https://codepoints.net/U+06F1>`_  '\\u06f1'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT ONE
`U+06F9 <https://codepoints.net/U+06F9>`_  '\\u06f9'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT NINE
`U+06F4 <https://codepoints.net/U+06F4>`_  '\\u06f4'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT FOUR
`U+06F8 <https://codepoints.net/U+06F8>`_  '\\u06f8'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT EIGHT
`U+0621 <https://codepoints.net/U+0621>`_  '\\u0621'  Lo                  1  ARABIC LETTER HAMZA
=========================================  =========  ==========  =========  =================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\x81\xdb\xb1\xdb\xb9\xdb\xb4\xdb\xb8\xd8\xa1|\\n12345|\\n"
        ؁۱۹۴۸ء|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width 6.

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n|\\n1|\\n"
        n|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Terminal.app* measures width -5.

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+030C <https://codepoints.net/U+030C>`_  '\\u030c'  Mn                  0  COMBINING CARON
=========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "to\xcc\x8c|\\n12|\\n"
        tǒ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Terminal.app* measures width -3.

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "sen|\\n123|\\n"
        sen|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width -1.

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "i'yandiosi|\\n1234567890|\\n"
        i'yandiosi|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Terminal.app* measures width 5.

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+0289 <https://codepoints.net/U+0289>`_  '\\u0289'  Ll                  1  LATIN SMALL LETTER U BAR
=========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ba\xcc\xb1r\xca\x89|\\n1234|\\n"
        ba̱rʉ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width -1.

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
=========================================  =========  ==========  =========  =========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x9bn\xc9\x9bake|\\n1234567|\\n"
        nɛnɛake|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Terminal.app* measures width 0.

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mii|\\n123|\\n"
        mii|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width -4.

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "oniti|\\n12345|\\n"
        oniti|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width -2.

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  =========
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  =========
`U+0031 <https://codepoints.net/U+0031>`_  '1'       Nd                  1  DIGIT ONE
=========================================  ========  ==========  =========  =========

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "1|\\n1|\\n"
        1|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Terminal.app* measures width -7.

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+0782 <https://codepoints.net/U+0782>`_  '\\u0782'  Lo                  1  THAANA LETTER NOONU
`U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
`U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+0782 <https://codepoints.net/U+0782>`_  '\\u0782'  Lo                  1  THAANA LETTER NOONU
`U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
`U+078E <https://codepoints.net/U+078E>`_  '\\u078e'  Lo                  1  THAANA LETTER GAAFU
`U+07AC <https://codepoints.net/U+07AC>`_  '\\u07ac'  Mn                  0  THAANA EBEFILI
=========================================  =========  ==========  =========  ===================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x8c\xde\xa6\xde\x82\xde\xb0\xde\x8c\xde\xa6\xde\x82\xde\xaa\xde\x8e\xde\xac|\\n12345|\\n"
        ތަންތަނުގެ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width 0.

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "surtou|\\n123456|\\n"
        surtou|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width -2.

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+00F5 <https://codepoints.net/U+00F5>`_  '\\xf5'   Ll                  1  LATIN SMALL LETTER O WITH TILDE
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
=========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "y\xc3\xb5od|\\n1234|\\n"
        yõod|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width -5.

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+00E0 <https://codepoints.net/U+00E0>`_  '\\xe0'   Ll                  1  LATIN SMALL LETTER A WITH GRAVE
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xa0ti|\\n123|\\n"
        àti|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width -1.

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ti|\\n12|\\n"
        ti|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Terminal.app* measures width -6.

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
=========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mo\xcc\xa3i|\\n123|\\n"
        mọi|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width 1.

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
  while *Terminal.app* measures width -2.

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "aji|\\n123|\\n"
        aji|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width 1.

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+007A <https://codepoints.net/U+007A>`_  'z'       Ll                  1  LATIN SMALL LETTER Z
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "zeto|\\n1234|\\n"
        zeto|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width 2.

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gane|\\n1234|\\n"
        gane|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width 3.

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n|\\n1|\\n"
        n|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Terminal.app* measures width -7.

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
`U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+A7B9 <https://codepoints.net/U+A7B9>`_  '\\ua7b9'  Ll                  1  LATIN SMALL LETTER U WITH STROKE
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pjor\xea\x9e\xb9.|\\n123456|\\n"
        pjorꞹ.|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Terminal.app* measures width 3.

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
=========================================  ========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Ar|\\n12|\\n"
        Ar|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Terminal.app* measures width -4.

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

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
  while *Terminal.app* measures width -2.

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================================
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
`U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
`U+0685 <https://codepoints.net/U+0685>`_  '\\u0685'  Lo                  1  ARABIC LETTER HAH WITH THREE DOTS ABOVE
=========================================  =========  ==========  =========  =======================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x87\xd9\x8a\xda\x85|\\n123|\\n"
        هيڅ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width 1.

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==============================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==============================================
`U+068B <https://codepoints.net/U+068B>`_  '\\u068b'  Lo                  1  ARABIC LETTER DAL WITH DOT BELOW AND SMALL TAH
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
`U+0633 <https://codepoints.net/U+0633>`_  '\\u0633'  Lo                  1  ARABIC LETTER SEEN
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
=========================================  =========  ==========  =========  ==============================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\x8b\xd9\x88\xdb\x8c\xd8\xb3\xd9\x86|\\n12345|\\n"
        ڋویسن|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Terminal.app* measures width -2.

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "vamurub\xc3\xa1|\\n12345678|\\n"
        vamurubá|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Terminal.app* measures width 6.

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "me|\\n12|\\n"
        me|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Terminal.app* measures width -2.

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "juu|\\n123|\\n"
        juu|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width -2.

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+071A <https://codepoints.net/U+071A>`_  '\\u071a'  Lo                  1  SYRIAC LETTER HETH
`U+0715 <https://codepoints.net/U+0715>`_  '\\u0715'  Lo                  1  SYRIAC LETTER DALATH
=========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\x9a\xdc\x95|\\n12|\\n"
        ܚܕ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Terminal.app* measures width 0.

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0047 <https://codepoints.net/U+0047>`_  'G'       Lu                  1  LATIN CAPITAL LETTER G
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Goo|\\n123|\\n"
        Goo|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Terminal.app* measures width -4.

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
=========================================  =========  ==========  =========  =========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gb\xc9\x9bwiwa|\\n1234567|\\n"
        gbɛwiwa|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Terminal.app* measures width 5.

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "sere|\\n1234|\\n"
        sere|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Terminal.app* measures width 2.

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
=========================================  =========  ==========  =========  =========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x9b|\\n12|\\n"
        nɛ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Terminal.app* measures width -3.

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+AABB <https://codepoints.net/U+AABB>`_  '\\uaabb'  Lo                  1  TAI VIET VOWEL AUE
`U+AAAC <https://codepoints.net/U+AAAC>`_  '\\uaaac'  Lo                  1  TAI VIET LETTER LOW HO
=========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xbb\xea\xaa\xac|\\n12|\\n"
        ꪻꪬ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Terminal.app* measures width -1.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
