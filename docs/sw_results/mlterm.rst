.. _mlterm:

mlterm
------


Tested Software version 3.9.3 on Linux
Full results available at ucs-detect_ repository path
`data/linux-mlterm-3.9.3.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-mlterm-3.9.3.yaml>`_

.. _mltermscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *mlterm*:

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

.. _mltermwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for mlterm appears to be 
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
  while *mlterm* measures width 1.

.. _mltermzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *mlterm* appears to be 
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
  while *mlterm* measures width 11.

.. _mltermvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *mlterm* is 213 errors
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
  while *mlterm* measures width 1.


.. _mltermvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *mlterm* are not available.

.. _mltermlang:

Language Support
++++++++++++++++

The following 2 languages were tested with 100% success:

Tagalog (Tagalog), Tamang, Eastern.

The following 117 languages are not fully supported:

===============================  ==========  =========  =============
lang                               n_errors    n_total  pct_success
===============================  ==========  =========  =============
Malayalam                               360       1630  77.9%
Javanese (Javanese)                     237       1453  83.7%
Mongolian, Halh (Mongolian)               3         33  90.9%
Sinhala                                 109       1655  93.4%
Bengali                                  82       1413  94.2%
Farsi, Western                           42       1822  97.7%
Dari                                     39       1872  97.9%
Tibetan, Central                          4        280  98.6%
Vietnamese (Han nom)                      2        199  99.0%
Japanese                                  3        299  99.0%
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
Japanese (Tokyo)                          3        320  99.1%
Chinese, Mandarin (Simplified)            2        225  99.1%
Thai                                      3        341  99.1%
Nuosu                                     2        230  99.1%
Dzongkha                                  3        359  99.2%
Lao                                       3        426  99.3%
Marathi                                  11       1614  99.3%
Japanese (Osaka)                          2        308  99.4%
Thai (2)                                  2        313  99.4%
Khmer, Central                            2        528  99.6%
Chickasaw                                 2        554  99.6%
Nepali                                    5       1385  99.6%
Yaneshaʼ                                  9       2536  99.6%
Bora                                      5       1598  99.7%
Kannada                                   3       1080  99.7%
Amarakaeri                                4       1446  99.7%
Shipibo-Conibo                            7       2540  99.7%
Navajo                                    4       1600  99.8%
Nanai                                     3       1207  99.8%
Orok                                      3       1245  99.8%
Tamil (Sri Lanka)                         3       1261  99.8%
Tamil                                     3       1262  99.8%
Colorado                                  3       1263  99.8%
Gumuz                                     3       1283  99.8%
Veps                                      3       1323  99.8%
Khün                                      1        442  99.8%
Yiddish, Eastern                          4       1775  99.8%
Evenki                                    2        899  99.8%
Shan                                      2        915  99.8%
South Azerbaijani                         3       1396  99.8%
Secoya                                    3       1409  99.8%
Mon                                       2        946  99.8%
Catalan (2)                               4       1909  99.8%
Panjabi, Western                          5       2419  99.8%
Mirandese                                 4       1966  99.8%
Siona                                     3       1492  99.8%
Sanskrit                                  2       1000  99.8%
Gilyak                                    3       1504  99.8%
Sanskrit (Grantha)                        2       1006  99.8%
Picard                                    4       2024  99.8%
Ticuna                                    4       2048  99.8%
(Yeonbyeon)                               2       1061  99.8%
Pular (Adlam)                             3       1613  99.8%
Tem                                       3       1659  99.8%
Éwé                                       4       2230  99.8%
Urdu                                      4       2237  99.8%
Urdu (2)                                  4       2251  99.8%
Telugu                                    2       1129  99.8%
Gen                                       4       2309  99.8%
Assyrian Neo-Aramaic                      2       1160  99.8%
Saint Lucian Creole French                3       1777  99.8%
Korean                                    2       1185  99.8%
Maori (2)                                 4       2385  99.8%
Kabyle                                    3       1815  99.8%
Lingala (tones)                           3       1818  99.8%
Tamazight, Central Atlas                  3       1822  99.8%
Burmese                                   2       1223  99.8%
Fur                                       3       1838  99.8%
Yoruba                                    4       2454  99.8%
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
Chakma                                    2       1444  99.9%
Lamnso'                                   3       2237  99.9%
Pashto, Northern                          3       2242  99.9%
Seraiki                                   3       2242  99.9%
Belanda Viri                              3       2246  99.9%
Maithili                                  2       1519  99.9%
Bamun                                     3       2285  99.9%
Dinka, Northeastern                       2       1529  99.9%
Gujarati                                  2       1536  99.9%
Dendi                                     2       1569  99.9%
Mazahua Central                           2       1574  99.9%
Serer-Sine                                2       1596  99.9%
Mòoré                                     3       2447  99.9%
Vietnamese                                3       2502  99.9%
Fon                                       3       2520  99.9%
Magahi                                    2       1716  99.9%
Chinantec, Chiltepec                      2       1729  99.9%
Bhojpuri                                  2       1737  99.9%
Otomi, Mezquital                          2       1849  99.9%
Dangme                                    3       2912  99.9%
Waama                                     1       1000  99.9%
Hindi                                     2       2128  99.9%
Panjabi, Eastern                          2       2293  99.9%
Tai Dam                                   2       2386  99.9%
===============================  ==========  =========  =============

Malayalam
^^^^^^^^^

Sequence of language *Malayalam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0D32 <https://codepoints.net/U+0D32>`_  '\\u0d32'  Lo                  1  MALAYALAM LETTER LA
`U+0D4B <https://codepoints.net/U+0D4B>`_  '\\u0d4b'  Mc                  0  MALAYALAM VOWEL SIGN OO
`U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
`U+0D24 <https://codepoints.net/U+0D24>`_  '\\u0d24'  Lo                  1  MALAYALAM LETTER TA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D24 <https://codepoints.net/U+0D24>`_  '\\u0d24'  Lo                  1  MALAYALAM LETTER TA
`U+0D3F <https://codepoints.net/U+0D3F>`_  '\\u0d3f'  Mc                  0  MALAYALAM VOWEL SIGN I
`U+0D32 <https://codepoints.net/U+0D32>`_  '\\u0d32'  Lo                  1  MALAYALAM LETTER LA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
=========================================  =========  ==========  =========  =======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb4\xb2\xe0\xb5\x8b\xe0\xb4\x95\xe0\xb4\xa4\xe0\xb5\x8d\xe0\xb4\xa4\xe0\xb4\xbf\xe0\xb4\xb2\xe0\xb5\x8d\xe2\x80\x8d|\\n12345|\\n"
        ലോകത്തില്‍|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+A9A5 <https://codepoints.net/U+A9A5>`_  '\\ua9a5'  Lo                  1  JAVANESE LETTER PA
`U+A9B1 <https://codepoints.net/U+A9B1>`_  '\\ua9b1'  Lo                  1  JAVANESE LETTER SA
`U+A9AB <https://codepoints.net/U+A9AB>`_  '\\ua9ab'  Lo                  1  JAVANESE LETTER RA
`U+A9BA <https://codepoints.net/U+A9BA>`_  '\\ua9ba'  Mc                  0  JAVANESE VOWEL SIGN TALING
`U+A98F <https://codepoints.net/U+A98F>`_  '\\ua98f'  Lo                  1  JAVANESE LETTER KA
`U+A9A0 <https://codepoints.net/U+A9A0>`_  '\\ua9a0'  Lo                  1  JAVANESE LETTER TA
=========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\xa5\xea\xa6\xb1\xea\xa6\xab\xea\xa6\xba\xea\xa6\x8f\xea\xa6\xa0|\\n12345|\\n"
        ꦥꦱꦫꦺꦏꦠ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

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
  while *mlterm* measures width 5.

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
  while *mlterm* measures width 7.

Bengali
^^^^^^^

Sequence of language *Bengali* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ============================
`U+09B8 <https://codepoints.net/U+09B8>`_  '\\u09b8'  Lo                  1  BENGALI LETTER SA
`U+09CD <https://codepoints.net/U+09CD>`_  '\\u09cd'  Mn                  0  BENGALI SIGN VIRAMA
`U+09AC <https://codepoints.net/U+09AC>`_  '\\u09ac'  Lo                  1  BENGALI LETTER BA
`U+09C0 <https://codepoints.net/U+09C0>`_  '\\u09c0'  Mc                  0  BENGALI VOWEL SIGN II
`U+0995 <https://codepoints.net/U+0995>`_  '\\u0995'  Lo                  1  BENGALI LETTER KA
`U+09C3 <https://codepoints.net/U+09C3>`_  '\\u09c3'  Mn                  0  BENGALI VOWEL SIGN VOCALIC R
`U+09A4 <https://codepoints.net/U+09A4>`_  '\\u09a4'  Lo                  1  BENGALI LETTER TA
`U+09BF <https://codepoints.net/U+09BF>`_  '\\u09bf'  Mc                  0  BENGALI VOWEL SIGN I
`U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
`U+0987 <https://codepoints.net/U+0987>`_  '\\u0987'  Lo                  1  BENGALI LETTER I
=========================================  =========  ==========  =========  ============================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\xb8\xe0\xa7\x8d\xe0\xa6\xac\xe0\xa7\x80\xe0\xa6\x95\xe0\xa7\x83\xe0\xa6\xa4\xe0\xa6\xbf\xe2\x80\x8c\xe0\xa6\x87|\\n12345|\\n"
        স্বীকৃতি‌ই|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

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
  while *mlterm* measures width 10.

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
  while *mlterm* measures width 10.

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F90 <https://codepoints.net/U+0F90>`_  '\\u0f90'  Mn                  0  TIBETAN SUBJOINED LETTER KA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F92 <https://codepoints.net/U+0F92>`_  '\\u0f92'  Mn                  0  TIBETAN SUBJOINED LETTER GA
`U+0FB2 <https://codepoints.net/U+0FB2>`_  '\\u0fb2'  Mn                  0  TIBETAN SUBJOINED LETTER RA
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F40 <https://codepoints.net/U+0F40>`_  '\\u0f40'  Lo                  1  TIBETAN LETTER KA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F54 <https://codepoints.net/U+0F54>`_  '\\u0f54'  Lo                  1  TIBETAN LETTER PA
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
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
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F9F <https://codepoints.net/U+0F9F>`_  '\\u0f9f'  Mn                  0  TIBETAN SUBJOINED LETTER TA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ================================

Total codepoints: 63


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa6\xe0\xbe\x90\xe0\xbe\xb1\xe0\xbd\xba\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\xbc\xe0\xbc\x8b\xe0\xbd\xa2\xe0\xbd\xba\xe0\xbc\x8b\xe0\xbd\xa2\xe0\xbd\xba\xe0\xbd\xa2\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\xa6\xe0\xbd\xa3\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\xa6\xe0\xbe\x92\xe0\xbe\xb2\xe0\xbd\x82\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x91\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x93\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\x80\xe0\xbd\xbc\xe0\xbd\x91\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\xa2\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x96\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\xa6\xe0\xbe\x9f\xe0\xbd\xba\xe0\xbc\x8d|\\n1234567890123456789012345678901234567890123456789|\\n"
        སྐྱེ་བོ་རེ་རེར་གསལ་བསྒྲགས་འདི་ནང་བཀོད་པའི་ཐོབ་ཐང་དང་རང་དབང་སྟེ།|
        1234567890123456789012345678901234567890123456789|

- python `wcwidth.wcswidth()`_ measures width 49,
  while *mlterm* measures width 37.

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+689D <https://codepoints.net/U+689D>`_  '\\u689d'  Lo                  2  CJK UNIFIED IDEOGRAPH-689D
`U+0031 <https://codepoints.net/U+0031>`_  '1'        Nd                  1  DIGIT ONE
`U+0035 <https://codepoints.net/U+0035>`_  '5'        Nd                  1  DIGIT FIVE
`U+FF1A <https://codepoints.net/U+FF1A>`_  '\\uff1a'  Po                  2  FULLWIDTH COLON
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xa2\x9d15\xef\xbc\x9a|\\n123456|\\n"
        條15：|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -74.

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
  while *mlterm* measures width -36.

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+63F4 <https://codepoints.net/U+63F4>`_  '\\u63f4'  Lo                  2  CJK UNIFIED IDEOGRAPH-63F4
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+6B64 <https://codepoints.net/U+6B64>`_  '\\u6b64'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B64
`U+79CD <https://codepoints.net/U+79CD>`_  '\\u79cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-79CD
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
=========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe5\xbe\x97\xe6\x8f\xb4\xe7\x94\xa8\xe6\xad\xa4\xe7\xa7\x8d\xe6\x9d\x83\xe5\x88\xa9|\\n1234567890123456|\\n"
        不得援用此种权利|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *mlterm* measures width -56.

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
`U+5011 <https://codepoints.net/U+5011>`_  '\\u5011'  Lo                  2  CJK UNIFIED IDEOGRAPH-5011
`U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
`U+5A5A <https://codepoints.net/U+5A5A>`_  '\\u5a5a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5A5A
`U+59FB <https://codepoints.net/U+59FB>`_  '\\u59fb'  Lo                  2  CJK UNIFIED IDEOGRAPH-59FB
`U+65B9 <https://codepoints.net/U+65B9>`_  '\\u65b9'  Lo                  2  CJK UNIFIED IDEOGRAPH-65B9
`U+9762 <https://codepoints.net/U+9762>`_  '\\u9762'  Lo                  2  CJK UNIFIED IDEOGRAPH-9762
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\x96\xe5\x80\x91\xe5\x9c\xa8\xe5\xa9\x9a\xe5\xa7\xbb\xe6\x96\xb9\xe9\x9d\xa2|\\n12345678901234|\\n"
        他們在婚姻方面|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *mlterm* measures width -4.

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5514 <https://codepoints.net/U+5514>`_  '\\u5514'  Lo                  2  CJK UNIFIED IDEOGRAPH-5514
`U+597D <https://codepoints.net/U+597D>`_  '\\u597d'  Lo                  2  CJK UNIFIED IDEOGRAPH-597D
`U+63F4 <https://codepoints.net/U+63F4>`_  '\\u63f4'  Lo                  2  CJK UNIFIED IDEOGRAPH-63F4
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+5462 <https://codepoints.net/U+5462>`_  '\\u5462'  Lo                  2  CJK UNIFIED IDEOGRAPH-5462
`U+79CD <https://codepoints.net/U+79CD>`_  '\\u79cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-79CD
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
=========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x94\x94\xe5\xa5\xbd\xe6\x8f\xb4\xe7\x94\xa8\xe5\x91\xa2\xe7\xa7\x8d\xe6\x9d\x83\xe5\x88\xa9|\\n1234567890123456|\\n"
        唔好援用呢种权利|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *mlterm* measures width -56.

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+63F4 <https://codepoints.net/U+63F4>`_  '\\u63f4'  Lo                  2  CJK UNIFIED IDEOGRAPH-63F4
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+6B64 <https://codepoints.net/U+6B64>`_  '\\u6b64'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B64
`U+79CD <https://codepoints.net/U+79CD>`_  '\\u79cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-79CD
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
=========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe5\xbe\x97\xe6\x8f\xb4\xe7\x94\xa8\xe6\xad\xa4\xe7\xa7\x8d\xe6\x9d\x83\xe5\x88\xa9|\\n1234567890123456|\\n"
        不得援用此种权利|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *mlterm* measures width -54.

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B87 <https://codepoints.net/U+7B87>`_  '\\u7b87'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B87
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
`U+63F4 <https://codepoints.net/U+63F4>`_  '\\u63f4'  Lo                  2  CJK UNIFIED IDEOGRAPH-63F4
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xae\x87\xe6\x9d\x83\xe5\x88\xa9\xe6\x8f\xb4\xe7\x94\xa8\xe4\xb8\x8d\xe5\xbe\x97|\\n12345678901234|\\n"
        箇权利援用不得|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *mlterm* measures width -54.

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+53EF <https://codepoints.net/U+53EF>`_  '\\u53ef'  Lo                  2  CJK UNIFIED IDEOGRAPH-53EF
`U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
`U+63F4 <https://codepoints.net/U+63F4>`_  '\\u63f4'  Lo                  2  CJK UNIFIED IDEOGRAPH-63F4
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+6B64 <https://codepoints.net/U+6B64>`_  '\\u6b64'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B64
`U+79CD <https://codepoints.net/U+79CD>`_  '\\u79cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-79CD
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
=========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe5\x8f\xaf\xe4\xbb\xa5\xe6\x8f\xb4\xe7\x94\xa8\xe6\xad\xa4\xe7\xa7\x8d\xe6\x9d\x83\xe5\x88\xa9|\\n123456789012345678|\\n"
        不可以援用此种权利|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *mlterm* measures width -52.

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+62C9 <https://codepoints.net/U+62C9>`_  '\\u62c9'  Lo                  2  CJK UNIFIED IDEOGRAPH-62C9
`U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
`U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
`U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+52FF <https://codepoints.net/U+52FF>`_  '\\u52ff'  Lo                  2  CJK UNIFIED IDEOGRAPH-52FF
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
`U+8131 <https://codepoints.net/U+8131>`_  '\\u8131'  Lo                  2  CJK UNIFIED IDEOGRAPH-8131
`U+4ED4 <https://codepoints.net/U+4ED4>`_  '\\u4ed4'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED4
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
`U+60C5 <https://codepoints.net/U+60C5>`_  '\\u60c5'  Lo                  2  CJK UNIFIED IDEOGRAPH-60C5
`U+51B5 <https://codepoints.net/U+51B5>`_  '\\u51b5'  Lo                  2  CJK UNIFIED IDEOGRAPH-51B5
`U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
=========================================  =========  ==========  =========  ==========================

Total codepoints: 36


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x8b\x89\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe5\x8b\xbf\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe4\xb8\xaa\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe4\xb8\xaa\xe5\xae\x97\xe6\x97\xa8\xe8\x84\xb1\xe4\xbb\x94\xe5\x8e\x9f\xe5\x88\x99\xe4\xb8\xaa\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe8\xaf\x89\xe4\xb8\xaa\xe6\x83\x85\xe5\x86\xb5\xe4\xb8\x8b|\\n123456789012345678901234567890123456789012345678901234567890123456789012|\\n"
        拉真正由于勿政治性个罪行或违背联合国个宗旨脱仔原则个行为而被起诉个情况下|
        123456789012345678901234567890123456789012345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 72,
  while *mlterm* measures width 28.

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5514 <https://codepoints.net/U+5514>`_  '\\u5514'  Lo                  2  CJK UNIFIED IDEOGRAPH-5514
`U+597D <https://codepoints.net/U+597D>`_  '\\u597d'  Lo                  2  CJK UNIFIED IDEOGRAPH-597D
`U+63F4 <https://codepoints.net/U+63F4>`_  '\\u63f4'  Lo                  2  CJK UNIFIED IDEOGRAPH-63F4
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+6B64 <https://codepoints.net/U+6B64>`_  '\\u6b64'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B64
`U+79CD <https://codepoints.net/U+79CD>`_  '\\u79cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-79CD
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
=========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x94\x94\xe5\xa5\xbd\xe6\x8f\xb4\xe7\x94\xa8\xe6\xad\xa4\xe7\xa7\x8d\xe6\x9d\x83\xe5\x88\xa9|\\n1234567890123456|\\n"
        唔好援用此种权利|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *mlterm* measures width -54.

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
  while *mlterm* measures width -52.

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
  while *mlterm* measures width 22.

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
  while *mlterm* measures width -22.

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5305 <https://codepoints.net/U+5305>`_  '\\u5305'  Lo                  2  CJK UNIFIED IDEOGRAPH-5305
`U+62EC <https://codepoints.net/U+62EC>`_  '\\u62ec'  Lo                  2  CJK UNIFIED IDEOGRAPH-62EC
`U+5176 <https://codepoints.net/U+5176>`_  '\\u5176'  Lo                  2  CJK UNIFIED IDEOGRAPH-5176
`U+672C <https://codepoints.net/U+672C>`_  '\\u672c'  Lo                  2  CJK UNIFIED IDEOGRAPH-672C
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
`U+5185 <https://codepoints.net/U+5185>`_  '\\u5185'  Lo                  2  CJK UNIFIED IDEOGRAPH-5185
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8c\x85\xe6\x8b\xac\xe5\x85\xb6\xe6\x9c\xac\xe5\x9b\xbd\xe5\x9c\xa8\xe5\x86\x85|\\n12345678901234|\\n"
        包括其本国在内|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *mlterm* measures width -16.

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
  while *mlterm* measures width 30.

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

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
`U+6253 <https://codepoints.net/U+6253>`_  '\\u6253'  Lo                  2  CJK UNIFIED IDEOGRAPH-6253
`U+5B98 <https://codepoints.net/U+5B98>`_  '\\u5b98'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B98
`U+53F8 <https://codepoints.net/U+53F8>`_  '\\u53f8'  Lo                  2  CJK UNIFIED IDEOGRAPH-53F8
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+60C5 <https://codepoints.net/U+60C5>`_  '\\u60c5'  Lo                  2  CJK UNIFIED IDEOGRAPH-60C5
`U+51B5 <https://codepoints.net/U+51B5>`_  '\\u51b5'  Lo                  2  CJK UNIFIED IDEOGRAPH-51B5
`U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
=========================================  =========  ==========  =========  ==========================

Total codepoints: 35


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe7\x9a\x84\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe7\x9a\x84\xe5\xae\x97\xe6\x97\xa8\xe5\x92\x8c\xe5\x8e\x9f\xe5\x88\x99\xe7\x9a\x84\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe6\x89\x93\xe5\xae\x98\xe5\x8f\xb8\xe7\x9a\x84\xe6\x83\x85\xe5\x86\xb5\xe4\xb8\x8b|\\n1234567890123456789012345678901234567890123456789012345678901234567890|\\n"
        在真正由于非政治性的罪行或违背联合国的宗旨和原则的行为而打官司的情况下|
        1234567890123456789012345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 70,
  while *mlterm* measures width 34.

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+FF19 <https://codepoints.net/U+FF19>`_  '\\uff19'  Nd                  2  FULLWIDTH DIGIT NINE
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xef\xbc\x99\xe6\x9d\xa1|\\n123456|\\n"
        第９条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -52.

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+8363 <https://codepoints.net/U+8363>`_  '\\u8363'  Lo                  2  CJK UNIFIED IDEOGRAPH-8363
`U+8A89 <https://codepoints.net/U+8A89>`_  '\\u8a89'  Lo                  2  CJK UNIFIED IDEOGRAPH-8A89
`U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
`U+540D <https://codepoints.net/U+540D>`_  '\\u540d'  Lo                  2  CJK UNIFIED IDEOGRAPH-540D
`U+8A89 <https://codepoints.net/U+8A89>`_  '\\u8a89'  Lo                  2  CJK UNIFIED IDEOGRAPH-8A89
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+52A0 <https://codepoints.net/U+52A0>`_  '\\u52a0'  Lo                  2  CJK UNIFIED IDEOGRAPH-52A0
`U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
`U+653B <https://codepoints.net/U+653B>`_  '\\u653b'  Lo                  2  CJK UNIFIED IDEOGRAPH-653B
`U+51FB <https://codepoints.net/U+51FB>`_  '\\u51fb'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FB
=========================================  =========  ==========  =========  ==========================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\x96\xe7\x9a\x84\xe8\x8d\xa3\xe8\xaa\x89\xe5\x92\x8c\xe5\x90\x8d\xe8\xaa\x89\xe4\xb8\x8d\xe5\xbe\x97\xe5\x8a\xa0\xe4\xbb\xa5\xe6\x94\xbb\xe5\x87\xbb|\\n12345678901234567890123456|\\n"
        他的荣誉和名誉不得加以攻击|
        12345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 26,
  while *mlterm* measures width 4.

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
  while *mlterm* measures width -26.

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
  while *mlterm* measures width -14.

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
  while *mlterm* measures width -1.

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
  while *mlterm* measures width -7.

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+091C <https://codepoints.net/U+091C>`_  '\\u091c'  Lo                  1  DEVANAGARI LETTER JA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
`U+0905 <https://codepoints.net/U+0905>`_  '\\u0905'  Lo                  1  DEVANAGARI LETTER A
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0925 <https://codepoints.net/U+0925>`_  '\\u0925'  Lo                  1  DEVANAGARI LETTER THA
`U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
=========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x9c\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe\xe2\x80\x8c\xe0\xa4\x85\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xa5\xe0\xa5\x80|\\n12345|\\n"
        ज्या‌अर्थी|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+FF19 <https://codepoints.net/U+FF19>`_  '\\uff19'  Nd                  2  FULLWIDTH DIGIT NINE
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xef\xbc\x99\xe6\x9d\xa1|\\n123456|\\n"
        第９条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -54.

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
`U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
`U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
`U+0E02 <https://codepoints.net/U+0E02>`_  '\\u0e02'  Lo                  1  THAI CHARACTER KHO KHAI
`U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
`U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
=========================================  =========  ==========  =========  ===========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x81\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\x82\xe0\xb8\xb1\xe0\xb8\x87|\\n1234|\\n"
        กักขัง|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -10.

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
`U+17C4 <https://codepoints.net/U+17C4>`_  '\\u17c4'  Mc                  0  KHMER VOWEL SIGN OO
`U+1799 <https://codepoints.net/U+1799>`_  '\\u1799'  Lo                  1  KHMER LETTER YO
`U+17A2 <https://codepoints.net/U+17A2>`_  '\\u17a2'  Lo                  1  KHMER LETTER QA
`U+17C6 <https://codepoints.net/U+17C6>`_  '\\u17c6'  Mn                  0  KHMER SIGN NIKAHIT
`U+1796 <https://codepoints.net/U+1796>`_  '\\u1796'  Lo                  1  KHMER LETTER PO
`U+17BE <https://codepoints.net/U+17BE>`_  '\\u17be'  Mc                  0  KHMER VOWEL SIGN OE
=========================================  =========  ==========  =========  ===================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x8a\xe1\x9f\x84\xe1\x9e\x99\xe1\x9e\xa2\xe1\x9f\x86\xe1\x9e\x96\xe1\x9e\xbe|\\n1234|\\n"
        ដោយអំពើ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -20.

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ki'yo.|\\n123456|\\n"
        ki'yo.|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -7.

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
  while *mlterm* measures width 7.

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
=========================================  =========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xcc\x83cohuen|\\n123456|\\n"
        ̃cohuen|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width 7.

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "im\xc3\xad|\\n123|\\n"
        imí|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -7.

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+0CB5 <https://codepoints.net/U+0CB5>`_  '\\u0cb5'  Lo                  1  KANNADA LETTER VA
`U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
`U+0C95 <https://codepoints.net/U+0C95>`_  '\\u0c95'  Lo                  1  KANNADA LETTER KA
`U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
`U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
`U+0CB8 <https://codepoints.net/U+0CB8>`_  '\\u0cb8'  Lo                  1  KANNADA LETTER SA
`U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
`U+0CB5 <https://codepoints.net/U+0CB5>`_  '\\u0cb5'  Lo                  1  KANNADA LETTER VA
`U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
`U+0CA4 <https://codepoints.net/U+0CA4>`_  '\\u0ca4'  Lo                  1  KANNADA LETTER TA
`U+0C82 <https://codepoints.net/U+0C82>`_  '\\u0c82'  Mc                  0  KANNADA SIGN ANUSVARA
`U+0CA4 <https://codepoints.net/U+0CA4>`_  '\\u0ca4'  Lo                  1  KANNADA LETTER TA
`U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
`U+0CB0 <https://codepoints.net/U+0CB0>`_  '\\u0cb0'  Lo                  1  KANNADA LETTER RA
`U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
`U+0CAF <https://codepoints.net/U+0CAF>`_  '\\u0caf'  Lo                  1  KANNADA LETTER YA
=========================================  =========  ==========  =========  =====================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\xb5\xe0\xb2\xbe\xe0\xb2\x95\xe0\xb3\x8d\xe2\x80\x8c\xe0\xb2\xb8\xe0\xb3\x8d\xe0\xb2\xb5\xe0\xb2\xbe\xe0\xb2\xa4\xe0\xb2\x82\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xb0\xe0\xb3\x8d\xe0\xb2\xaf|\\n12345678|\\n"
        ವಾಕ್‌ಸ್ವಾತಂತ್ರ್ಯ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width 9.

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
=========================================  =========  ==========  =========  ======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ke\xcc\xb1nomey|\\n1234567|\\n"
        ke̱nomey|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *mlterm* measures width -3.

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "iqui|\\n1234|\\n"
        iqui|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -7.

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ===============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nijigh\xc3\xa1o|\\n12345678|\\n"
        nijigháo|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width -2.

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
`U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
`U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
=========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb1\xd0\xb8\xd0\xbc\xd0\xb1\xd1\x8d|\\n12345|\\n"
        бимбэ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 0.

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
`U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
`U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb1\xd0\xb8\xd0\xb2\xd0\xb2\xd1\x83\xd1\x80\xd0\xb8\xd1\x82\xd1\x8d\xd0\xb8.|\\n12345678901|\\n"
        биввуритэи.|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *mlterm* measures width 7.

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0B87 <https://codepoints.net/U+0B87>`_  '\\u0b87'  Lo                  1  TAMIL LETTER I
`U+0BAA <https://codepoints.net/U+0BAA>`_  '\\u0baa'  Lo                  1  TAMIL LETTER PA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0BAA <https://codepoints.net/U+0BAA>`_  '\\u0baa'  Lo                  1  TAMIL LETTER PA
`U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
`U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
`U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
`U+0B9F <https://codepoints.net/U+0B9F>`_  '\\u0b9f'  Lo                  1  TAMIL LETTER TTA
`U+0BA9 <https://codepoints.net/U+0BA9>`_  '\\u0ba9'  Lo                  1  TAMIL LETTER NNNA
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
`U+0BC8 <https://codepoints.net/U+0BC8>`_  '\\u0bc8'  Mc                  0  TAMIL VOWEL SIGN AI
=========================================  =========  ==========  =========  ===================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x87\xe0\xae\xaa\xe0\xaf\x8d\xe0\xae\xaa\xe0\xae\xbf\xe0\xae\xb0\xe0\xae\x95\xe0\xae\x9f\xe0\xae\xa9\xe0\xae\xa4\xe0\xaf\x8d\xe0\xae\xa4\xe0\xaf\x88|\\n123456789|\\n"
        இப்பிரகடனத்தை|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width -2.

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0B87 <https://codepoints.net/U+0B87>`_  '\\u0b87'  Lo                  1  TAMIL LETTER I
`U+0BAA <https://codepoints.net/U+0BAA>`_  '\\u0baa'  Lo                  1  TAMIL LETTER PA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0BAA <https://codepoints.net/U+0BAA>`_  '\\u0baa'  Lo                  1  TAMIL LETTER PA
`U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
`U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
`U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
`U+0B9F <https://codepoints.net/U+0B9F>`_  '\\u0b9f'  Lo                  1  TAMIL LETTER TTA
`U+0BA9 <https://codepoints.net/U+0BA9>`_  '\\u0ba9'  Lo                  1  TAMIL LETTER NNNA
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
`U+0BC8 <https://codepoints.net/U+0BC8>`_  '\\u0bc8'  Mc                  0  TAMIL VOWEL SIGN AI
=========================================  =========  ==========  =========  ===================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x87\xe0\xae\xaa\xe0\xaf\x8d\xe0\xae\xaa\xe0\xae\xbf\xe0\xae\xb0\xe0\xae\x95\xe0\xae\x9f\xe0\xae\xa9\xe0\xae\xa4\xe0\xaf\x8d\xe0\xae\xa4\xe0\xaf\x88|\\n123456789|\\n"
        இப்பிரகடனத்தை|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width -2.

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tsa'chila|\\n123456789|\\n"
        tsa'chila|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 5.

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ==========
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ==========
`U+0035 <https://codepoints.net/U+0035>`_  '5'       Nd                  1  DIGIT FIVE
=========================================  ========  ==========  =========  ==========

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "5|\\n1|\\n"
        5|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -8.

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tehta|\\n12345|\\n"
        tehta|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -7.

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+1A2F <https://codepoints.net/U+1A2F>`_  '\\u1a2f'  Lo                  1  TAI THAM LETTER DA
`U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
`U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
`U+1A45 <https://codepoints.net/U+1A45>`_  '\\u1a45'  Lo                  1  TAI THAM LETTER WA
`U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
`U+1A3F <https://codepoints.net/U+1A3F>`_  '\\u1a3f'  Lo                  1  TAI THAM LETTER LOW YA
`U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
`U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
`U+1A36 <https://codepoints.net/U+1A36>`_  '\\u1a36'  Lo                  1  TAI THAM LETTER NA
`U+1A6B <https://codepoints.net/U+1A6B>`_  '\\u1a6b'  Mn                  0  TAI THAM VOWEL SIGN O
`U+1A23 <https://codepoints.net/U+1A23>`_  '\\u1a23'  Lo                  1  TAI THAM LETTER LOW KA
`U+1A6D <https://codepoints.net/U+1A6D>`_  '\\u1a6d'  Mc                  0  TAI THAM VOWEL SIGN OY
`U+1A2F <https://codepoints.net/U+1A2F>`_  '\\u1a2f'  Lo                  1  TAI THAM LETTER DA
`U+1A74 <https://codepoints.net/U+1A74>`_  '\\u1a74'  Mn                  0  TAI THAM SIGN MAI KANG
`U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
`U+1A3F <https://codepoints.net/U+1A3F>`_  '\\u1a3f'  Lo                  1  TAI THAM LETTER LOW YA
=========================================  =========  ==========  =========  ===========================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xaf\xe1\xa9\xa2\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa8\xb2\xe1\xa9\xa0\xe1\xa8\xb6\xe1\xa9\xab\xe1\xa8\xa3\xe1\xa9\xad\xe1\xa8\xaf\xe1\xa9\xb4\xe1\xa9\xa0\xe1\xa8\xbf|\\n12345678|\\n"
        ᨯᩢ᩠ᩅ᩠ᨿᨲ᩠ᨶᩫᨣᩭᨯᩴ᩠ᨿ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width -10.

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
  while *mlterm* measures width 3.

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+0414 <https://codepoints.net/U+0414>`_  '\\u0414'  Lu                  1  CYRILLIC CAPITAL LETTER DE
`U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\x94\xd1\x8f\xd0\xbd|\\n123|\\n"
        Дян|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -8.

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+1022 <https://codepoints.net/U+1022>`_  '\\u1022'  Lo                  1  MYANMAR LETTER SHAN A
`U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1075 <https://codepoints.net/U+1075>`_  '\\u1075'  Lo                  1  MYANMAR LETTER SHAN KA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1087 <https://codepoints.net/U+1087>`_  '\\u1087'  Mc                  0  MYANMAR SIGN SHAN TONE-2
`U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
`U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1019 <https://codepoints.net/U+1019>`_  '\\u1019'  Lo                  1  MYANMAR LETTER MA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+1030 <https://codepoints.net/U+1030>`_  '\\u1030'  Mn                  0  MYANMAR VOWEL SIGN UU
`U+101D <https://codepoints.net/U+101D>`_  '\\u101d'  Lo                  1  MYANMAR LETTER WA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1088 <https://codepoints.net/U+1088>`_  '\\u1088'  Mc                  0  MYANMAR SIGN SHAN TONE-3
`U+101A <https://codepoints.net/U+101A>`_  '\\u101a'  Lo                  1  MYANMAR LETTER YA
`U+1062 <https://codepoints.net/U+1062>`_  '\\u1062'  Mc                  0  MYANMAR VOWEL SIGN SGAW KAREN EU
`U+1019 <https://codepoints.net/U+1019>`_  '\\u1019'  Lo                  1  MYANMAR LETTER MA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
`U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
`U+1030 <https://codepoints.net/U+1030>`_  '\\u1030'  Mn                  0  MYANMAR VOWEL SIGN UU
`U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1089 <https://codepoints.net/U+1089>`_  '\\u1089'  Mc                  0  MYANMAR SIGN SHAN TONE-5
`U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
`U+1085 <https://codepoints.net/U+1085>`_  '\\u1085'  Mn                  0  MYANMAR VOWEL SIGN SHAN E ABOVE
`U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+104B <https://codepoints.net/U+104B>`_  '\\u104b'  Po                  1  MYANMAR SIGN SECTION
=========================================  =========  ==========  =========  ================================

Total codepoints: 33


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\xa2\xe1\x81\xbc\xe1\x80\xba\xe1\x81\xb5\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x82\x87\xe1\x80\x95\xe1\x81\xbc\xe1\x80\xba\xe1\x80\x99\xe1\x80\xad\xe1\x80\xb0\xe1\x80\x9d\xe1\x80\xba\xe1\x82\x88\xe1\x80\x9a\xe1\x81\xa2\xe1\x80\x99\xe1\x80\xba\xe1\x80\xb8\xe1\x80\x95\xe1\x80\xb0\xe1\x81\xbc\xe1\x80\xba\xe1\x82\x89\xe1\x80\x95\xe1\x82\x85\xe1\x81\xbc\xe1\x80\xba\xe1\x81\x8b|\\n123456789012345|\\n"
        ဢၼ်ၵိုင်ႇပၼ်မိူဝ်ႈယၢမ်းပူၼ်ႉပႅၼ်။|
        123456789012345|

- python `wcwidth.wcswidth()`_ measures width 15,
  while *mlterm* measures width 9.

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ============================
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0131 <https://codepoints.net/U+0131>`_  '\\u0131'  Ll                  1  LATIN SMALL LETTER DOTLESS I
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
=========================================  =========  ==========  =========  ============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "aras\xc4\xb1nda|\\n12345678|\\n"
        arasında|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width 3.

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pa'iye|\\n123456|\\n"
        pa'iye|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -2.

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+1019 <https://codepoints.net/U+1019>`_  '\\u1019'  Lo                  1  MYANMAR LETTER MA
`U+1012 <https://codepoints.net/U+1012>`_  '\\u1012'  Lo                  1  MYANMAR LETTER DA
`U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
`U+1014 <https://codepoints.net/U+1014>`_  '\\u1014'  Lo                  1  MYANMAR LETTER NA
`U+103D <https://codepoints.net/U+103D>`_  '\\u103d'  Mn                  0  MYANMAR CONSONANT SIGN MEDIAL WA
`U+1036 <https://codepoints.net/U+1036>`_  '\\u1036'  Mn                  0  MYANMAR SIGN ANUSVARA
`U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
`U+1035 <https://codepoints.net/U+1035>`_  '\\u1035'  Mn                  0  MYANMAR VOWEL SIGN E ABOVE
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
=========================================  =========  ==========  =========  ================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x99\xe1\x80\x92\xe1\x80\xb8\xe1\x80\x94\xe1\x80\xbd\xe1\x80\xb6\xe1\x80\x80\xe1\x80\xb5\xe1\x80\xaf|\\n1234|\\n"
        မဒးနွံကဵု|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -3.

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tant|\\n1234|\\n"
        tant|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -3.

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0633 <https://codepoints.net/U+0633>`_  '\\u0633'  Lo                  1  ARABIC LETTER SEEN
`U+0637 <https://codepoints.net/U+0637>`_  '\\u0637'  Lo                  1  ARABIC LETTER TAH
`U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
=========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88\xd8\xa7\xd8\xb3\xd8\xb7\xdb\x92|\\n12345|\\n"
        واسطے|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 2.

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
=========================================  =========  ==========  =========  ===========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "d\xe2\x80\x99adonde|\\n12345678|\\n"
        d’adonde|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width -2.

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ==========
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ==========
`U+0034 <https://codepoints.net/U+0034>`_  '4'       Nd                  1  DIGIT FOUR
`U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
=========================================  ========  ==========  =========  ==========

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "4.|\\n12|\\n"
        4.|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -7.

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
`U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
=========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe\xe0\xa4\xaa\xe0\xa4\xbf|\\n1234|\\n"
        कस्यापि|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 2.

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================================
`U+04FF <https://codepoints.net/U+04FF>`_  '\\u04ff'  Ll                  1  CYRILLIC SMALL LETTER HA WITH STROKE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
=========================================  =========  ==========  =========  ====================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd3\xbf\xd0\xb0\xd1\x80\xd0\xb0|\\n1234|\\n"
        ӿара|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -9.

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =================
`U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
=================================================  =============  ==========  =========  =================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xa8|\\n1|\\n"
        𑌨|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -12.

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

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
  while *mlterm* measures width -4.

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===================================
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'   Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
`U+0078 <https://codepoints.net/U+0078>`_  'x'       Ll                  1  LATIN SMALL LETTER X
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ===================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "w\xc3\xbcxi|\\n1234|\\n"
        wüxi|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -6.

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+B9D0 <https://codepoints.net/U+B9D0>`_  '\\ub9d0'  Lo                  2  HANGUL SYLLABLE MAL
=========================================  =========  ==========  =========  ===================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xeb\xa7\x90|\\n12|\\n"
        말|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -6.

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =======================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =======================
`U+0001E92D <https://codepoints.net/U+0001E92D>`_  '\\U0001e92d'  Ll                  1  ADLAM SMALL LETTER I
`U+0001E932 <https://codepoints.net/U+0001E932>`_  '\\U0001e932'  Ll                  1  ADLAM SMALL LETTER NUN
`U+0001E922 <https://codepoints.net/U+0001E922>`_  '\\U0001e922'  Ll                  1  ADLAM SMALL LETTER ALIF
=================================================  =============  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xad\xf0\x9e\xa4\xb2\xf0\x9e\xa4\xa2|\\n123|\\n"
        𞤭𞤲𞤢|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -3.

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==============================
`U+0256 <https://codepoints.net/U+0256>`_  '\\u0256'  Ll                  1  LATIN SMALL LETTER D WITH TAIL
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0256 <https://codepoints.net/U+0256>`_  '\\u0256'  Ll                  1  LATIN SMALL LETTER D WITH TAIL
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
=========================================  =========  ==========  =========  ==============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc9\x96eciri\xc9\x96i|\\n12345678|\\n"
        ɖeciriɖi|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width 2.

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kadodo|\\n123456|\\n"
        kadodo|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width 4.

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
  while *mlterm* measures width 6.

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
  while *mlterm* measures width 6.

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0C17 <https://codepoints.net/U+0C17>`_  '\\u0c17'  Lo                  1  TELUGU LETTER GA
`U+0C3E <https://codepoints.net/U+0C3E>`_  '\\u0c3e'  Mn                  0  TELUGU VOWEL SIGN AA
`U+0C28 <https://codepoints.net/U+0C28>`_  '\\u0c28'  Lo                  1  TELUGU LETTER NA
`U+0C3F <https://codepoints.net/U+0C3F>`_  '\\u0c3f'  Mn                  0  TELUGU VOWEL SIGN I
=========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\x97\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xbf|\\n12|\\n"
        గాని|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -3.

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
=========================================  =========  ==========  =========  =========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "am\xc9\x9b\xc5\x8but\xc9\x94\xcc\x81|\\n1234567|\\n"
        amɛŋutɔ́|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *mlterm* measures width 2.

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0721 <https://codepoints.net/U+0721>`_  '\\u0721'  Lo                  1  SYRIAC LETTER MIM
`U+071A <https://codepoints.net/U+071A>`_  '\\u071a'  Lo                  1  SYRIAC LETTER HETH
`U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
`U+072C <https://codepoints.net/U+072C>`_  '\\u072c'  Lo                  1  SYRIAC LETTER TAW
`U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
=========================================  =========  ==========  =========  ===================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\xa1\xdc\x9a\xdc\x9d\xdc\xac\xdc\x90|\\n12345|\\n"
        ܡܚܝܬܐ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -1.

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ni|\\n12|\\n"
        ni|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -2.

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+B300 <https://codepoints.net/U+B300>`_  '\\ub300'  Lo                  2  HANGUL SYLLABLE DAE
`U+D55C <https://codepoints.net/U+D55C>`_  '\\ud55c'  Lo                  2  HANGUL SYLLABLE HAN
=========================================  =========  ==========  =========  ===================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xeb\x8c\x80\xed\x95\x9c|\\n1234|\\n"
        대한|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -2.

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

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
  while *mlterm* measures width -4.

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
  while *mlterm* measures width -5.

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
=========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "o\xcc\x81yo|\\n123|\\n"
        óyo|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -5.

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

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
  while *mlterm* measures width -5.

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+1019 <https://codepoints.net/U+1019>`_  '\\u1019'  Lo                  1  MYANMAR LETTER MA
`U+103B <https://codepoints.net/U+103B>`_  '\\u103b'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL YA
`U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
`U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
`U+101E <https://codepoints.net/U+101E>`_  '\\u101e'  Lo                  1  MYANMAR LETTER SA
`U+100A <https://codepoints.net/U+100A>`_  '\\u100a'  Lo                  1  MYANMAR LETTER NNYA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
=========================================  =========  ==========  =========  ================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x99\xe1\x80\xbb\xe1\x80\xac\xe1\x80\xb8\xe1\x80\x9e\xe1\x80\x8a\xe1\x80\xba|\\n123|\\n"
        များသည်|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -2.

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xa1|\\n1|\\n"
        á|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -9.

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================================
`U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'    Ll                  1  LATIN SMALL LETTER E WITH GRAVE
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+00F2 <https://codepoints.net/U+00F2>`_  '\\xf2'    Ll                  1  LATIN SMALL LETTER O WITH GRAVE
`U+2010 <https://codepoints.net/U+2010>`_  '\\u2010'  Pd                  1  HYPHEN
`U+00EC <https://codepoints.net/U+00EC>`_  '\\xec'    Ll                  1  LATIN SMALL LETTER I WITH GRAVE
`U+1E63 <https://codepoints.net/U+1E63>`_  '\\u1e63'  Ll                  1  LATIN SMALL LETTER S WITH DOT BELOW
`U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'    Ll                  1  LATIN SMALL LETTER E WITH GRAVE
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'    Ll                  1  LATIN SMALL LETTER U WITH ACUTE
=========================================  =========  ==========  =========  ===================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xa8t\xc3\xb2\xe2\x80\x90\xc3\xac\xe1\xb9\xa3\xc3\xa8l\xc3\xba|\\n123456789|\\n"
        ètò‐ìṣèlú|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 3.

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "be|\\n12|\\n"
        be|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width 0.

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0790 <https://codepoints.net/U+0790>`_  '\\u0790'  Lo                  1  THAANA LETTER SEENU
`U+07A8 <https://codepoints.net/U+07A8>`_  '\\u07a8'  Mn                  0  THAANA IBIFILI
`U+0794 <https://codepoints.net/U+0794>`_  '\\u0794'  Lo                  1  THAANA LETTER YAA
`U+07A7 <https://codepoints.net/U+07A7>`_  '\\u07a7'  Mn                  0  THAANA AABAAFILI
`U+0790 <https://codepoints.net/U+0790>`_  '\\u0790'  Lo                  1  THAANA LETTER SEENU
`U+07A9 <https://codepoints.net/U+07A9>`_  '\\u07a9'  Mn                  0  THAANA EEBEEFILI
=========================================  =========  ==========  =========  ===================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x90\xde\xa8\xde\x94\xde\xa7\xde\x90\xde\xa9|\\n123|\\n"
        ސިޔާސީ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -3.

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
=========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "chke\xcc\x80|\\n1234|\\n"
        chkè|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -4.

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yelerre|\\n1234567|\\n"
        yelerre|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *mlterm* measures width 6.

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

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
  while *mlterm* measures width -2.

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gwo|\\n123|\\n"
        gwo|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -2.

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+0632 <https://codepoints.net/U+0632>`_  '\\u0632'  Lo                  1  ARABIC LETTER ZAIN
`U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
`U+0629 <https://codepoints.net/U+0629>`_  '\\u0629'  Lo                  1  ARABIC LETTER TEH MARBUTA
=========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x86\xd8\xb2\xd9\x8a\xd9\x87\xd8\xa9|\\n12345|\\n"
        نزيهة|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -2.

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
=========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ak\xc9\x9b|\\n123|\\n"
        akɛ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -2.

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===========
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===========
`U+0037 <https://codepoints.net/U+0037>`_  '7'       Nd                  1  DIGIT SEVEN
=========================================  ========  ==========  =========  ===========

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "7|\\n1|\\n"
        7|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -7.

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
=========================================  =========  ==========  =========  =========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "m\xc9\x94|\\n12|\\n"
        mɔ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -10.

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ==================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ==================
`U+00011117 <https://codepoints.net/U+00011117>`_  '\\U00011117'  Lo                  1  CHAKMA LETTER THAA
`U+0001111A <https://codepoints.net/U+0001111A>`_  '\\U0001111a'  Lo                  1  CHAKMA LETTER NAA
`U+00011122 <https://codepoints.net/U+00011122>`_  '\\U00011122'  Lo                  1  CHAKMA LETTER RAA
`U+00011134 <https://codepoints.net/U+00011134>`_  '\\U00011134'  Mn                  0  CHAKMA MAAYYAA
=================================================  =============  ==========  =========  ==================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\x97\xf0\x91\x84\x9a\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n123|\\n"
        𑄗𑄚𑄢𑄴|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -1.

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ye|\\n12|\\n"
        ye|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -2.

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
`U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
`U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
=========================================  =========  ==========  =========  ==================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa8\xd8\xb1\xd8\xa7\xd8\xa8\xd8\xb1|\\n12345|\\n"
        برابر|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 2.

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
`U+0641 <https://codepoints.net/U+0641>`_  '\\u0641'  Lo                  1  ARABIC LETTER FEH
`U+0639 <https://codepoints.net/U+0639>`_  '\\u0639'  Lo                  1  ARABIC LETTER AIN
`U+06C1 <https://codepoints.net/U+06C1>`_  '\\u06c1'  Lo                  1  ARABIC LETTER HEH GOAL
=========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaf\xd9\x81\xd8\xb9\xdb\x81|\\n1234|\\n"
        دفعہ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 2.

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "k\xc3\xa1|\\n12|\\n"
        ká|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width 0.

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+091C <https://codepoints.net/U+091C>`_  '\\u091c'  Lo                  1  DEVANAGARI LETTER JA
`U+0901 <https://codepoints.net/U+0901>`_  '\\u0901'  Mn                  0  DEVANAGARI SIGN CANDRABINDU
=========================================  =========  ==========  =========  ===========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x9c\xe0\xa4\x81|\\n1|\\n"
        जँ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -2.

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
=========================================  =========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mente\xcc\x80n|\\n123456|\\n"
        mentèn|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width 3.

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "looi|\\n1234|\\n"
        looi|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 0.

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0AAA <https://codepoints.net/U+0AAA>`_  '\\u0aaa'  Lo                  1  GUJARATI LETTER PA
`U+0AA3 <https://codepoints.net/U+0AA3>`_  '\\u0aa3'  Lo                  1  GUJARATI LETTER NNA
=========================================  =========  ==========  =========  ===================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\xaa\xe0\xaa\xa3|\\n12|\\n"
        પણ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -2.

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "goosi|\\n12345|\\n"
        goosi|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 2.

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0044 <https://codepoints.net/U+0044>`_  'D'       Lu                  1  LATIN CAPITAL LETTER D
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+007A <https://codepoints.net/U+007A>`_  'z'       Ll                  1  LATIN SMALL LETTER Z
=========================================  ========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Dyz|\\n123|\\n"
        Dyz|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -7.

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "we|\\n12|\\n"
        we|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -6.

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "laloa|\\n12345|\\n"
        laloa|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 0.

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0111 <https://codepoints.net/U+0111>`_  '\\u0111'  Ll                  1  LATIN SMALL LETTER D WITH STROKE
`U+0103 <https://codepoints.net/U+0103>`_  '\\u0103'  Ll                  1  LATIN SMALL LETTER A WITH BREVE
`U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
=========================================  =========  ==========  =========  ================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc4\x91\xc4\x83\xcc\xa3t|\\n123|\\n"
        đặt|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -1.

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ma|\\n12|\\n"
        ma|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -1.

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
`U+090F <https://codepoints.net/U+090F>`_  '\\u090f'  Lo                  1  DEVANAGARI LETTER E
`U+0932 <https://codepoints.net/U+0932>`_  '\\u0932'  Lo                  1  DEVANAGARI LETTER LA
=========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\x8f\xe0\xa4\xb2|\\n123|\\n"
        कएल|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width 2.

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kur\xc3\xa9e|\\n12345|\\n"
        kurée|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 1.

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+091B <https://codepoints.net/U+091B>`_  '\\u091b'  Lo                  1  DEVANAGARI LETTER CHA
`U+094B <https://codepoints.net/U+094B>`_  '\\u094b'  Mc                  0  DEVANAGARI VOWEL SIGN O
`U+0921 <https://codepoints.net/U+0921>`_  '\\u0921'  Lo                  1  DEVANAGARI LETTER DDA
`U+0947 <https://codepoints.net/U+0947>`_  '\\u0947'  Mn                  0  DEVANAGARI VOWEL SIGN E
`U+093C <https://codepoints.net/U+093C>`_  '\\u093c'  Mn                  0  DEVANAGARI SIGN NUKTA
=========================================  =========  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x9b\xe0\xa5\x8b\xe0\xa4\xa1\xe0\xa5\x87\xe0\xa4\xbc|\\n12|\\n"
        छोडे़|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width 0.

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "goti'ki|\\n1234567|\\n"
        goti'ki|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *mlterm* measures width 5.

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
=========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ye\xc9\x94|\\n123|\\n"
        yeɔ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width 2.

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ta|\\n12|\\n"
        ta|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -4.

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+0947 <https://codepoints.net/U+0947>`_  '\\u0947'  Mn                  0  DEVANAGARI VOWEL SIGN E
=========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa5\x87|\\n1|\\n"
        से|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -2.

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0A32 <https://codepoints.net/U+0A32>`_  '\\u0a32'  Lo                  1  GURMUKHI LETTER LA
`U+0A08 <https://codepoints.net/U+0A08>`_  '\\u0a08'  Lo                  1  GURMUKHI LETTER II
=========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\xb2\xe0\xa8\x88|\\n12|\\n"
        ਲਈ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -1.

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+AA81 <https://codepoints.net/U+AA81>`_  '\\uaa81'  Lo                  1  TAI VIET LETTER HIGH KO
`U+AAB7 <https://codepoints.net/U+AAB7>`_  '\\uaab7'  Mn                  0  TAI VIET MAI KHIT
=========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\x81\xea\xaa\xb7|\\n1|\\n"
        ꪁꪷ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -2.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
