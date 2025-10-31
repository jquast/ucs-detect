.. _WezTerm:

WezTerm
-------


Tested Software version 20240203-110809-5046fc22 on Linux
Full results available at ucs-detect_ repository path
`data/linux-wezterm-20240203-110809-5046fc22.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-wezterm-20240203-110809-5046fc22.yaml>`_

.. _WezTermscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *WezTerm*:

============  ===========  ==============  ======================================================
Score Type    Raw Score    Scaled Score    Calculation
============  ===========  ==============  ======================================================
WIDE          72.73%       59.2%           (version_index / total_versions) × (pct_success / 100)
ZWJ           75.00%       100.0%          (version_index / total_versions) × (pct_success / 100)
LANG          2.52%        2.6%            languages_supported / total_languages
VS16          0.00%        0.0%            pct_success / 100
VS15          0.00%        0.0%            pct_success / 100
============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 30.05%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15) / 5
  the categorized 'average' absolute support level of this terminal

- Scaled Final Score: 28.5%
  (normalized across all terminals tested).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _WezTermwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for WezTerm appears to be 
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
  while *WezTerm* measures width 1.

.. _WezTermzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *WezTerm* appears to be 
**17.0**, this is from a summary of the following
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
'17.0'              0        130  100.0%
=========  ==========  =========  =============

.. _WezTermvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *WezTerm* is 213 errors
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
  while *WezTerm* measures width 1.


.. _WezTermvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *WezTerm* are not available.

.. _WezTermlang:

Language Support
++++++++++++++++

The following 3 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog), Tamang, Eastern.

The following 116 languages are not fully supported:

===============================  ==========  =========  =============
lang                               n_errors    n_total  pct_success
===============================  ==========  =========  =============
Malayalam                               113       1630  93.1%
Sinhala                                 110       1655  93.4%
Tibetan, Central                          4        280  98.6%
Dzongkha                                  4        359  98.9%
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
Lao                                       4        426  99.1%
Japanese (Tokyo)                          3        320  99.1%
Chinese, Mandarin (Simplified)            2        225  99.1%
Thai                                      3        341  99.1%
Nuosu                                     2        230  99.1%
Marathi                                   8       1614  99.5%
Khün                                      2        442  99.5%
Khmer, Central                            2        528  99.6%
Bora                                      6       1598  99.6%
Chickasaw                                 2        554  99.6%
Nepali                                    5       1385  99.6%
Bengali                                   5       1413  99.6%
Evenki                                    3        899  99.7%
Nanai                                     4       1207  99.7%
Orok                                      4       1245  99.7%
Yaneshaʼ                                  8       2536  99.7%
Shipibo-Conibo                            8       2540  99.7%
Navajo                                    5       1600  99.7%
Gumuz                                     4       1283  99.7%
Veps                                      4       1323  99.7%
South Azerbaijani                         4       1396  99.7%
Secoya                                    4       1409  99.7%
(Yeonbyeon)                               3       1061  99.7%
Amarakaeri                                4       1446  99.7%
Siona                                     4       1492  99.7%
Gilyak                                    4       1504  99.7%
Telugu                                    3       1129  99.7%
Korean                                    3       1185  99.7%
Burmese                                   3       1223  99.8%
Tem                                       4       1659  99.8%
Tamil (Sri Lanka)                         3       1261  99.8%
Tamil                                     3       1262  99.8%
Colorado                                  3       1263  99.8%
Yiddish, Eastern                          4       1775  99.8%
Éwé                                       5       2230  99.8%
Arabic, Standard                          3       1348  99.8%
Kabyle                                    4       1815  99.8%
Lingala (tones)                           4       1818  99.8%
Tamazight, Central Atlas                  4       1822  99.8%
Mixtec, Metlatónoc                        3       1367  99.8%
Shan                                      2        915  99.8%
Fur                                       4       1838  99.8%
Mon                                       2        946  99.8%
Catalan (2)                               4       1909  99.8%
Maldivian                                 4       1918  99.8%
French (Welche)                           4       1928  99.8%
Mirandese                                 4       1966  99.8%
Sanskrit                                  2       1000  99.8%
Sanskrit (Grantha)                        2       1006  99.8%
Picard                                    4       2024  99.8%
Ga                                        4       2039  99.8%
Ticuna                                    4       2048  99.8%
Aja                                       4       2061  99.8%
Dendi                                     3       1569  99.8%
Mazahua Central                           3       1574  99.8%
Serer-Sine                                3       1596  99.8%
Pular (Adlam)                             3       1613  99.8%
Kannada                                   2       1080  99.8%
Uduk                                      6       3247  99.8%
Urdu                                      4       2237  99.8%
Pashto, Northern                          4       2242  99.8%
Seraiki                                   4       2242  99.8%
Belanda Viri                              4       2246  99.8%
Urdu (2)                                  4       2251  99.8%
Bamun                                     4       2285  99.8%
Chinantec, Chiltepec                      3       1729  99.8%
Gen                                       4       2309  99.8%
Assyrian Neo-Aramaic                      2       1160  99.8%
Saint Lucian Creole French                3       1777  99.8%
Maori (2)                                 4       2385  99.8%
Panjabi, Western                          4       2419  99.8%
Farsi, Western                            3       1822  99.8%
Mòoré                                     4       2447  99.8%
Yoruba                                    4       2454  99.8%
Otomi, Mezquital                          3       1849  99.8%
Dari                                      3       1872  99.8%
Vietnamese                                4       2502  99.8%
Ditammari                                 3       1882  99.8%
Fon                                       4       2520  99.8%
Dagaare, Southern                         4       2582  99.8%
Baatonum                                  3       1939  99.8%
Hindi                                     3       2128  99.9%
Chakma                                    2       1444  99.9%
Javanese (Javanese)                       2       1453  99.9%
Dangme                                    4       2912  99.9%
Lamnso'                                   3       2237  99.9%
Maithili                                  2       1519  99.9%
Panjabi, Eastern                          3       2293  99.9%
Dinka, Northeastern                       2       1529  99.9%
Gujarati                                  2       1536  99.9%
Tai Dam                                   3       2386  99.9%
Magahi                                    2       1716  99.9%
Bhojpuri                                  2       1737  99.9%
Waama                                     1       1000  99.9%
===============================  ==========  =========  =============

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
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F54 <https://codepoints.net/U+0F54>`_  '\\u0f54'  Lo                  1  TIBETAN LETTER PA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ================================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x91\xe0\xbd\xbc\xe0\xbd\x93\xe0\xbc\x8b\xe0\xbd\x9a\xe0\xbd\x93\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbd\xbc\xe0\xbc\x8d|\\n12345678901|\\n"
        དོན་ཚན་དང་པོ།|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *WezTerm* measures width -77.

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F61 <https://codepoints.net/U+0F61>`_  '\\u0f61'  Lo                  1  TIBETAN LETTER YA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
=========================================  =========  ==========  =========  ================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa1\xe0\xbd\x84\xe0\xbd\x93\xe0\xbc\x8b|\\n1234|\\n"
        ཡངན་|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -18.

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
  while *WezTerm* measures width 28.

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -32.

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
`U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
`U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
`U+304A <https://codepoints.net/U+304A>`_  '\\u304a'  Lo                  2  HIRAGANA LETTER O
`U+3044 <https://codepoints.net/U+3044>`_  '\\u3044'  Lo                  2  HIRAGANA LETTER I
`U+3066 <https://codepoints.net/U+3066>`_  '\\u3066'  Lo                  2  HIRAGANA LETTER TE
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xb3\x95\xe3\x81\xae\xe4\xb8\x8b\xe3\x81\xab\xe3\x81\x8a\xe3\x81\x84\xe3\x81\xa6|\\n12345678901234|\\n"
        法の下において|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *WezTerm* measures width -8.

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+0E44 <https://codepoints.net/U+0E44>`_  '\\u0e44'  Lo                  1  THAI CHARACTER SARA AI MAIMALAI
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
`U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
`U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
`U+0E38 <https://codepoints.net/U+0E38>`_  '\\u0e38'  Mn                  0  THAI CHARACTER SARA U
`U+0E29 <https://codepoints.net/U+0E29>`_  '\\u0e29'  Lo                  1  THAI CHARACTER SO RUSI
`U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
`U+0E18 <https://codepoints.net/U+0E18>`_  '\\u0e18'  Lo                  1  THAI CHARACTER THO THONG
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
`U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
`U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
=========================================  =========  ==========  =========  ===============================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x84\xe0\xb8\xa3\xe0\xb9\x89\xe0\xb8\xa1\xe0\xb8\x99\xe0\xb8\xb8\xe0\xb8\xa9\xe0\xb8\xa2\xe0\xb8\x98\xe0\xb8\xa3\xe0\xb8\xa3\xe0\xb8\xa1\xe0\xb8\xab\xe0\xb8\xa3\xe0\xb8\xb7\xe0\xb8\xad|\\n1234567890123|\\n"
        ไร้มนุษยธรรมหรือ|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *WezTerm* measures width -38.

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe5\xbe\x97\xe8\xa2\xab\xe5\x88\xa4\xe4\xb8\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n12345678901234567890|\\n"
        不得被判为犯有刑事罪|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *WezTerm* measures width -22.

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
  while *WezTerm* measures width -22.

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5514 <https://codepoints.net/U+5514>`_  '\\u5514'  Lo                  2  CJK UNIFIED IDEOGRAPH-5514
`U+597D <https://codepoints.net/U+597D>`_  '\\u597d'  Lo                  2  CJK UNIFIED IDEOGRAPH-597D
`U+4FFE <https://codepoints.net/U+4FFE>`_  '\\u4ffe'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FFE
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x94\x94\xe5\xa5\xbd\xe4\xbf\xbe\xe5\x88\xa4\xe4\xb8\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n12345678901234567890|\\n"
        唔好俾判为犯有刑事罪|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *WezTerm* measures width -24.

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe5\xbe\x97\xe8\xa2\xab\xe5\x88\xa4\xe4\xb8\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n12345678901234567890|\\n"
        不得被判为犯有刑事罪|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *WezTerm* measures width -22.

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+7F5A <https://codepoints.net/U+7F5A>`_  '\\u7f5a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F5A
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+8BB8 <https://codepoints.net/U+8BB8>`_  '\\u8bb8'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BB8
`U+91CD <https://codepoints.net/U+91CD>`_  '\\u91cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-91CD
`U+4F3C <https://codepoints.net/U+4F3C>`_  '\\u4f3c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F3C
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+65F6 <https://codepoints.net/U+65F6>`_  '\\u65f6'  Lo                  2  CJK UNIFIED IDEOGRAPH-65F6
`U+9002 <https://codepoints.net/U+9002>`_  '\\u9002'  Lo                  2  CJK UNIFIED IDEOGRAPH-9002
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
`U+89C4 <https://codepoints.net/U+89C4>`_  '\\u89c4'  Lo                  2  CJK UNIFIED IDEOGRAPH-89C4
`U+5B9A <https://codepoints.net/U+5B9A>`_  '\\u5b9a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x88\x91\xe7\xbd\x9a\xe4\xb8\x8d\xe8\xae\xb8\xe9\x87\x8d\xe4\xbc\xbc\xe7\x8a\xaf\xe7\xbd\xaa\xe6\x97\xb6\xe9\x80\x82\xe7\x94\xa8\xe4\xb8\xaa\xe6\xb3\x95\xe5\xbe\x8b\xe8\xa7\x84\xe5\xae\x9a|\\n12345678901234567890123456789012|\\n"
        刑罚不许重似犯罪时适用个法律规定|
        12345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 32,
  while *WezTerm* measures width 10.

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe5\xbe\x97\xe8\xa2\xab\xe5\x88\xa4\xe4\xb8\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n12345678901234567890|\\n"
        不得被判为犯有刑事罪|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *WezTerm* measures width -22.

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+52FF <https://codepoints.net/U+52FF>`_  '\\u52ff'  Lo                  2  CJK UNIFIED IDEOGRAPH-52FF
`U+8981 <https://codepoints.net/U+8981>`_  '\\u8981'  Lo                  2  CJK UNIFIED IDEOGRAPH-8981
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8b\xbf\xe8\xa6\x81\xe8\xa2\xab\xe5\x88\xa4\xe4\xb8\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n12345678901234567890|\\n"
        勿要被判为犯有刑事罪|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *WezTerm* measures width -26.

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+7F5A <https://codepoints.net/U+7F5A>`_  '\\u7f5a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F5A
`U+5514 <https://codepoints.net/U+5514>`_  '\\u5514'  Lo                  2  CJK UNIFIED IDEOGRAPH-5514
`U+597D <https://codepoints.net/U+597D>`_  '\\u597d'  Lo                  2  CJK UNIFIED IDEOGRAPH-597D
`U+91CD <https://codepoints.net/U+91CD>`_  '\\u91cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-91CD
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+65F6 <https://codepoints.net/U+65F6>`_  '\\u65f6'  Lo                  2  CJK UNIFIED IDEOGRAPH-65F6
`U+9002 <https://codepoints.net/U+9002>`_  '\\u9002'  Lo                  2  CJK UNIFIED IDEOGRAPH-9002
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
`U+89C4 <https://codepoints.net/U+89C4>`_  '\\u89c4'  Lo                  2  CJK UNIFIED IDEOGRAPH-89C4
`U+5B9A <https://codepoints.net/U+5B9A>`_  '\\u5b9a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x88\x91\xe7\xbd\x9a\xe5\x94\x94\xe5\xa5\xbd\xe9\x87\x8d\xe4\xba\x8e\xe7\x8a\xaf\xe7\xbd\xaa\xe6\x97\xb6\xe9\x80\x82\xe7\x94\xa8\xe4\xb8\xaa\xe6\xb3\x95\xe5\xbe\x8b\xe8\xa7\x84\xe5\xae\x9a|\\n12345678901234567890123456789012|\\n"
        刑罚唔好重于犯罪时适用个法律规定|
        12345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 32,
  while *WezTerm* measures width 8.

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+7F5A <https://codepoints.net/U+7F5A>`_  '\\u7f5a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F5A
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+6562 <https://codepoints.net/U+6562>`_  '\\u6562'  Lo                  2  CJK UNIFIED IDEOGRAPH-6562
`U+91CD <https://codepoints.net/U+91CD>`_  '\\u91cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-91CD
`U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
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

        $ printf "\xe5\x88\x91\xe7\xbd\x9a\xe4\xb8\x8d\xe6\x95\xa2\xe9\x87\x8d\xe4\xba\x8e\xe7\x8a\xaf\xe4\xba\x8b\xe6\x97\xb6\xe9\x80\x82\xe7\x94\xa8\xe7\x9a\x84\xe6\xb3\x95\xe5\xbe\x8b\xe8\xa7\x84\xe5\xae\x9a|\\n12345678901234567890123456789012|\\n"
        刑罚不敢重于犯事时适用的法律规定|
        12345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 32,
  while *WezTerm* measures width 10.

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+752D <https://codepoints.net/U+752D>`_  '\\u752d'  Lo                  2  CJK UNIFIED IDEOGRAPH-752D
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+8D81 <https://codepoints.net/U+8D81>`_  '\\u8d81'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D81
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\x94\xad\xe8\xa2\xab\xe5\x88\xa4\xe4\xb8\xba\xe8\xb6\x81\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n1234567890123456|\\n"
        甭被判为趁刑事罪|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *WezTerm* measures width -26.

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+4F5C <https://codepoints.net/U+4F5C>`_  '\\u4f5c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F5C
`U+5174 <https://codepoints.net/U+5174>`_  '\\u5174'  Lo                  2  CJK UNIFIED IDEOGRAPH-5174
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb8\x8d\xe4\xbd\x9c\xe5\x85\xb4\xe8\xa2\xab\xe5\x88\xa4\xe4\xb8\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n1234567890123456789012|\\n"
        不作兴被判为犯有刑事罪|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *WezTerm* measures width -22.

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
`U+672A <https://codepoints.net/U+672A>`_  '\\u672a'  Lo                  2  CJK UNIFIED IDEOGRAPH-672A
`U+7ECF <https://codepoints.net/U+7ECF>`_  '\\u7ecf'  Lo                  2  CJK UNIFIED IDEOGRAPH-7ECF
`U+83B7 <https://codepoints.net/U+83B7>`_  '\\u83b7'  Lo                  2  CJK UNIFIED IDEOGRAPH-83B7
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+8FA9 <https://codepoints.net/U+8FA9>`_  '\\u8fa9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FA9
`U+62A4 <https://codepoints.net/U+62A4>`_  '\\u62a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-62A4
`U+4E0A <https://codepoints.net/U+4E0A>`_  '\\u4e0a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0A
`U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
`U+9700 <https://codepoints.net/U+9700>`_  '\\u9700'  Lo                  2  CJK UNIFIED IDEOGRAPH-9700
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
`U+5207 <https://codepoints.net/U+5207>`_  '\\u5207'  Lo                  2  CJK UNIFIED IDEOGRAPH-5207
`U+4FDD <https://codepoints.net/U+4FDD>`_  '\\u4fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FDD
`U+8BC1 <https://codepoints.net/U+8BC1>`_  '\\u8bc1'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC1
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+5B98 <https://codepoints.net/U+5B98>`_  '\\u5b98'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B98
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+5BA1 <https://codepoints.net/U+5BA1>`_  '\\u5ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BA1
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
`U+4F9D <https://codepoints.net/U+4F9D>`_  '\\u4f9d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F9D
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+8BC1 <https://codepoints.net/U+8BC1>`_  '\\u8bc1'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC1
`U+5B9E <https://codepoints.net/U+5B9E>`_  '\\u5b9e'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B9E
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
`U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
`U+524D <https://codepoints.net/U+524D>`_  '\\u524d'  Lo                  2  CJK UNIFIED IDEOGRAPH-524D
=========================================  =========  ==========  =========  ==========================

Total codepoints: 30


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe6\x9c\xaa\xe7\xbb\x8f\xe8\x8e\xb7\xe5\xbe\x97\xe8\xbe\xa9\xe6\x8a\xa4\xe4\xb8\x8a\xe6\x89\x80\xe9\x9c\x80\xe7\x9a\x84\xe4\xb8\x80\xe5\x88\x87\xe4\xbf\x9d\xe8\xaf\x81\xe7\x9a\x84\xe5\xae\x98\xe7\x9a\x84\xe7\x9a\x84\xe5\xae\xa1\xe5\x88\xa4\xe8\x80\x8c\xe4\xbe\x9d\xe6\xb3\x95\xe8\xaf\x81\xe5\xae\x9e\xe6\x9c\x89\xe7\xbd\xaa\xe4\xbb\xa5\xe5\x89\x8d|\\n123456789012345678901234567890123456789012345678901234567890|\\n"
        在未经获得辩护上所需的一切保证的官的的审判而依法证实有罪以前|
        123456789012345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 60,
  while *WezTerm* measures width 46.

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+52FF <https://codepoints.net/U+52FF>`_  '\\u52ff'  Lo                  2  CJK UNIFIED IDEOGRAPH-52FF
`U+4F1A <https://codepoints.net/U+4F1A>`_  '\\u4f1a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F1A
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+4E92 <https://codepoints.net/U+4E92>`_  '\\u4e92'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E92
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8b\xbf\xe4\xbc\x9a\xe7\x94\xa8\xe4\xba\x92\xe5\x88\xa4\xe4\xb8\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n1234567890123456789012|\\n"
        勿会用互判为犯有刑事罪|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *WezTerm* measures width -22.

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+83AB <https://codepoints.net/U+83AB>`_  '\\u83ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-83AB
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+72AF <https://codepoints.net/U+72AF>`_  '\\u72af'  Lo                  2  CJK UNIFIED IDEOGRAPH-72AF
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+5211 <https://codepoints.net/U+5211>`_  '\\u5211'  Lo                  2  CJK UNIFIED IDEOGRAPH-5211
`U+4E8B <https://codepoints.net/U+4E8B>`_  '\\u4e8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8B
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x8e\xab\xe8\xa2\xab\xe5\x88\xa4\xe4\xb8\xba\xe7\x8a\xaf\xe6\x9c\x89\xe5\x88\x91\xe4\xba\x8b\xe7\xbd\xaa|\\n123456789012345678|\\n"
        莫被判为犯有刑事罪|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *WezTerm* measures width -24.

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
  while *WezTerm* measures width -18.

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4F55 <https://codepoints.net/U+4F55>`_  '\\u4f55'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F55
`U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
`U+3082 <https://codepoints.net/U+3082>`_  '\\u3082'  Lo                  2  HIRAGANA LETTER MO
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbd\x95\xe4\xba\xba\xe3\x82\x82|\\n123456|\\n"
        何人も|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -3.

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

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
=========================================  =========  ==========  =========  ==========================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xa5\xe7\xa1\xae\xe5\xae\x9a\xe4\xbb\x96\xe7\x9a\x84\xe6\x9d\x83\xe5\x88\xa9\xe5\x92\x8c\xe4\xb9\x89\xe5\x8a\xa1\xe5\xb9\xb6\xe5\x88\xa4\xe5\xae\x9a\xe5\xaf\xb9\xe4\xbb\x96\xe6\x8f\x90\xe5\x87\xba\xe7\x9a\x84\xe4\xbb\xbb\xe4\xbd\x95\xe5\x88\x91\xe4\xba\x8b\xe6\x8c\x87\xe6\x8e\xa7|\\n123456789012345678901234567890123456789012345678|\\n"
        以确定他的权利和义务并判定对他提出的任何刑事指控|
        123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 48,
  while *WezTerm* measures width -16.

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+0E08 <https://codepoints.net/U+0E08>`_  '\\u0e08'  Lo                  1  THAI CHARACTER CHO CHAN
`U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
`U+0E16 <https://codepoints.net/U+0E16>`_  '\\u0e16'  Lo                  1  THAI CHARACTER THO THUNG
`U+0E39 <https://codepoints.net/U+0E39>`_  '\\u0e39'  Mn                  0  THAI CHARACTER SARA UU
`U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
`U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
`U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
`U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
`U+0E44 <https://codepoints.net/U+0E44>`_  '\\u0e44'  Lo                  1  THAI CHARACTER SARA AI MAIMALAI
`U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
`U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
`U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
`U+0E1C <https://codepoints.net/U+0E1C>`_  '\\u0e1c'  Lo                  1  THAI CHARACTER PHO PHUNG
`U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
`U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
`U+0E0F <https://codepoints.net/U+0E0F>`_  '\\u0e0f'  Lo                  1  THAI CHARACTER TO PATAK
`U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
`U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
`U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
`U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
`U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
=========================================  =========  ==========  =========  ===============================

Total codepoints: 29


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x88\xe0\xb8\xb0\xe0\xb8\x96\xe0\xb8\xb9\xe0\xb8\x81\xe0\xb8\x97\xe0\xb8\xa3\xe0\xb8\xa1\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xab\xe0\xb8\xa3\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x9c\xe0\xb8\xa5\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x9a\xe0\xb8\xb1\xe0\xb8\x95\xe0\xb8\xb4|\\n1234567890123456789012|\\n"
        จะถูกทรมานหรือได้รับผลปฏิบัติ|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *WezTerm* measures width 21.

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============
`U+A2AF <https://codepoints.net/U+A2AF>`_  '\\ua2af'  Lo                  2  YI SYLLABLE CIX
`U+A2AA <https://codepoints.net/U+A2AA>`_  '\\ua2aa'  Lo                  2  YI SYLLABLE ZY
`U+A3E1 <https://codepoints.net/U+A3E1>`_  '\\ua3e1'  Lo                  2  YI SYLLABLE JIX
`U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
=========================================  =========  ==========  =========  ===============

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x8a\xaf\xea\x8a\xaa\xea\x8f\xa1\xea\x8c\xa0|\\n12345678|\\n"
        ꊯꊪꏡꌠ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width -50.

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+0942 <https://codepoints.net/U+0942>`_  '\\u0942'  Mn                  0  DEVANAGARI VOWEL SIGN UU
`U+0932 <https://codepoints.net/U+0932>`_  '\\u0932'  Lo                  1  DEVANAGARI LETTER LA
`U+092D <https://codepoints.net/U+092D>`_  '\\u092d'  Lo                  1  DEVANAGARI LETTER BHA
`U+0942 <https://codepoints.net/U+0942>`_  '\\u0942'  Mn                  0  DEVANAGARI VOWEL SIGN UU
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
=========================================  =========  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa5\x82\xe0\xa4\xb2\xe0\xa4\xad\xe0\xa5\x82\xe0\xa4\xa4|\\n1234|\\n"
        मूलभूत|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -1.

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+1A37 <https://codepoints.net/U+1A37>`_  '\\u1a37'  Lo                  1  TAI THAM LETTER BA
`U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
`U+1A23 <https://codepoints.net/U+1A23>`_  '\\u1a23'  Lo                  1  TAI THAM LETTER LOW KA
`U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
=========================================  =========  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xb7\xe1\xa9\xa2\xe1\xa8\xa3\xe1\xa9\xa2|\\n12|\\n"
        ᨷᩢᨣᩢ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -15.

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
`U+17C2 <https://codepoints.net/U+17C2>`_  '\\u17c2'  Mc                  0  KHMER VOWEL SIGN AE
`U+179B <https://codepoints.net/U+179B>`_  '\\u179b'  Lo                  1  KHMER LETTER LO
`U+178F <https://codepoints.net/U+178F>`_  '\\u178f'  Lo                  1  KHMER LETTER TA
`U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
`U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
`U+17BC <https://codepoints.net/U+17BC>`_  '\\u17bc'  Mn                  0  KHMER VOWEL SIGN UU
`U+179C <https://codepoints.net/U+179C>`_  '\\u179c'  Lo                  1  KHMER LETTER VO
`U+1794 <https://codepoints.net/U+1794>`_  '\\u1794'  Lo                  1  KHMER LETTER BA
`U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
`U+1793 <https://codepoints.net/U+1793>`_  '\\u1793'  Lo                  1  KHMER LETTER NO
`U+1791 <https://codepoints.net/U+1791>`_  '\\u1791'  Lo                  1  KHMER LETTER TO
`U+1791 <https://codepoints.net/U+1791>`_  '\\u1791'  Lo                  1  KHMER LETTER TO
`U+17BD <https://codepoints.net/U+17BD>`_  '\\u17bd'  Mn                  0  KHMER VOWEL SIGN UA
`U+179B <https://codepoints.net/U+179B>`_  '\\u179b'  Lo                  1  KHMER LETTER LO
`U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
`U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
`U+1782 <https://codepoints.net/U+1782>`_  '\\u1782'  Lo                  1  KHMER LETTER KO
`U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
`U+179B <https://codepoints.net/U+179B>`_  '\\u179b'  Lo                  1  KHMER LETTER LO
`U+17CB <https://codepoints.net/U+17CB>`_  '\\u17cb'  Mn                  0  KHMER SIGN BANTOC
=========================================  =========  ==========  =========  ===================

Total codepoints: 21


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x8a\xe1\x9f\x82\xe1\x9e\x9b\xe1\x9e\x8f\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\xbc\xe1\x9e\x9c\xe1\x9e\x94\xe1\x9e\xb6\xe1\x9e\x93\xe1\x9e\x91\xe1\x9e\x91\xe1\x9e\xbd\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x82\xe1\x9e\xb6\xe1\x9e\x9b\xe1\x9f\x8b|\\n1234567890123|\\n"
        ដែលត្រូវបានទទួលស្គាល់|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *WezTerm* measures width -26.

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'   Ll                  1  LATIN SMALL LETTER U WITH ACUTE
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tsahd\xc3\xbar\xc3\xa9|\\n12345678|\\n"
        tsahdúré|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width -3.

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
`U+0031 <https://codepoints.net/U+0031>`_  '1'       Nd                  1  DIGIT ONE
=========================================  ========  ==========  =========  ======================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "AnompaKanihmo'si11|\\n123456789012345678|\\n"
        AnompaKanihmo'si11|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *WezTerm* measures width 3.

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

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+0415 <https://codepoints.net/U+0415>`_  '\\u0415'  Lu                  1  CYRILLIC CAPITAL LETTER IE
`U+0433 <https://codepoints.net/U+0433>`_  '\\u0433'  Ll                  1  CYRILLIC SMALL LETTER GHE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\x95\xd0\xb3\xd0\xb8\xcc\x84|\\n123|\\n"
        Егӣ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width -11.

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======
`U+2013 <https://codepoints.net/U+2013>`_  '\\u2013'  Pd                  1  EN DASH
=========================================  =========  ==========  =========  =======

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe2\x80\x93|\\n1|\\n"
        –|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -4.

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
=========================================  =========  ==========  =========  ========================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb0\xd0\xb1\xd0\xb4\xd1\x83\xd0\xbb\xd1\x83\xd1\x81\xd0\xb0\xd0\xbb\xd0\xb4\xd0\xb4\xd0\xb0\xcc\x84|\\n123456789012|\\n"
        абдулусалдда̄|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *WezTerm* measures width 6.

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "e'\xc3\xb1e|\\n1234|\\n"
        e'ñe|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -3.

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jay\xc3\xa1|\\n1234|\\n"
        jayá|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -2.

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'   Ll                  1  LATIN SMALL LETTER O WITH ACUTE
`U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'   Ll                  1  LATIN SMALL LETTER O WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "d\xc3\xb3\xc3\xb3|\\n123|\\n"
        dóó|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 0.

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
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
=========================================  ========  ==========  =========  ====================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kamakaalash|\\n12345678901|\\n"
        kamakaalash|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *WezTerm* measures width 1.

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pohjal|\\n123456|\\n"
        pohjal|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -2.

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "onur|\\n1234|\\n"
        onur|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width 1.

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pa'ye|\\n12345|\\n"
        pa'ye|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -4.

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+AD8C <https://codepoints.net/U+AD8C>`_  '\\uad8c'  Lo                  2  HANGUL SYLLABLE GWEON
`U+B9AC <https://codepoints.net/U+B9AC>`_  '\\ub9ac'  Lo                  2  HANGUL SYLLABLE RI
`U+D558 <https://codepoints.net/U+D558>`_  '\\ud558'  Lo                  2  HANGUL SYLLABLE HA
`U+ACE0 <https://codepoints.net/U+ACE0>`_  '\\uace0'  Lo                  2  HANGUL SYLLABLE GO
=========================================  =========  ==========  =========  =====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xb6\x8c\xeb\xa6\xac\xed\x95\x98\xea\xb3\xa0|\\n12345678|\\n"
        권리하고|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 4.

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
`U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
=========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "o\xcc\xb1'ne|\\n1234|\\n"
        o̱'ne|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -5.

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -2.

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================================
`U+0447 <https://codepoints.net/U+0447>`_  '\\u0447'  Ll                  1  CYRILLIC SMALL LETTER CHE
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
`U+0493 <https://codepoints.net/U+0493>`_  '\\u0493'  Ll                  1  CYRILLIC SMALL LETTER GHE WITH STROKE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
=========================================  =========  ==========  =========  =====================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x87\xd0\xbb\xd0\xb5\xd0\xbd\xd2\x93\xd1\x83\xd0\xbd|\\n1234567|\\n"
        членғун|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *WezTerm* measures width 2.

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0C05 <https://codepoints.net/U+0C05>`_  '\\u0c05'  Lo                  1  TELUGU LETTER A
`U+0C24 <https://codepoints.net/U+0C24>`_  '\\u0c24'  Lo                  1  TELUGU LETTER TA
`U+0C28 <https://codepoints.net/U+0C28>`_  '\\u0c28'  Lo                  1  TELUGU LETTER NA
`U+0C3F <https://codepoints.net/U+0C3F>`_  '\\u0c3f'  Mn                  0  TELUGU VOWEL SIGN I
=========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\x85\xe0\xb0\xa4\xe0\xb0\xa8\xe0\xb0\xbf|\\n123|\\n"
        అతని|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width -3.

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+AC00 <https://codepoints.net/U+AC00>`_  '\\uac00'  Lo                  2  HANGUL SYLLABLE GA
`U+C9C4 <https://codepoints.net/U+C9C4>`_  '\\uc9c4'  Lo                  2  HANGUL SYLLABLE JIN
`U+B2E4 <https://codepoints.net/U+B2E4>`_  '\\ub2e4'  Lo                  2  HANGUL SYLLABLE DA
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xb0\x80\xec\xa7\x84\xeb\x8b\xa4.|\\n1234567|\\n"
        가진다.|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *WezTerm* measures width 1.

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+1005 <https://codepoints.net/U+1005>`_  '\\u1005'  Lo                  1  MYANMAR LETTER CA
`U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
`U+1001 <https://codepoints.net/U+1001>`_  '\\u1001'  Lo                  1  MYANMAR LETTER KHA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
`U+1001 <https://codepoints.net/U+1001>`_  '\\u1001'  Lo                  1  MYANMAR LETTER KHA
`U+103C <https://codepoints.net/U+103C>`_  '\\u103c'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL RA
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
`U+104A <https://codepoints.net/U+104A>`_  '\\u104a'  Po                  1  MYANMAR SIGN LITTLE SECTION
=========================================  =========  ==========  =========  ================================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x85\xe1\x80\xb1\xe1\x80\x81\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\xb8\xe1\x80\x81\xe1\x80\xbc\xe1\x80\x84\xe1\x80\xba\xe1\x80\xb8\xe1\x81\x8a|\\n123456|\\n"
        စေခိုင်းခြင်း၊|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 2.

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
  while *WezTerm* measures width -7.

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0B89 <https://codepoints.net/U+0B89>`_  '\\u0b89'  Lo                  1  TAMIL LETTER U
`U+0BB1 <https://codepoints.net/U+0BB1>`_  '\\u0bb1'  Lo                  1  TAMIL LETTER RRA
`U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
`U+0BAA <https://codepoints.net/U+0BAA>`_  '\\u0baa'  Lo                  1  TAMIL LETTER PA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0BAA <https://codepoints.net/U+0BAA>`_  '\\u0baa'  Lo                  1  TAMIL LETTER PA
`U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
`U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
`U+0BC8 <https://codepoints.net/U+0BC8>`_  '\\u0bc8'  Mc                  0  TAMIL VOWEL SIGN AI
=========================================  =========  ==========  =========  ===================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x89\xe0\xae\xb1\xe0\xaf\x81\xe0\xae\xaa\xe0\xaf\x8d\xe0\xae\xaa\xe0\xaf\x81\xe0\xae\xb0\xe0\xaf\x88|\\n12345|\\n"
        உறுப்புரை|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -6.

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===========
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===========
`U+0033 <https://codepoints.net/U+0033>`_  '3'       Nd                  1  DIGIT THREE
=========================================  ========  ==========  =========  ===========

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "3|\\n1|\\n"
        3|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -4.

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kela|\\n1234|\\n"
        kela|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -1.

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
  while *WezTerm* measures width -6.

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "blibo|\\n12345|\\n"
        blibo|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -3.

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================================
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
`U+0643 <https://codepoints.net/U+0643>`_  '\\u0643'  Lo                  1  ARABIC LETTER KAF
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0641 <https://codepoints.net/U+0641>`_  '\\u0641'  Lo                  1  ARABIC LETTER FEH
`U+0626 <https://codepoints.net/U+0626>`_  '\\u0626'  Lo                  1  ARABIC LETTER YEH WITH HAMZA ABOVE
`U+0629 <https://codepoints.net/U+0629>`_  '\\u0629'  Lo                  1  ARABIC LETTER TEH MARBUTA
=========================================  =========  ==========  =========  ==================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x85\xd8\xaa\xd9\x83\xd8\xa7\xd9\x81\xd8\xa6\xd8\xa9|\\n1234567|\\n"
        متكافئة|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *WezTerm* measures width 1.

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
  while *WezTerm* measures width -5.

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0059 <https://codepoints.net/U+0059>`_  'Y'       Lu                  1  LATIN CAPITAL LETTER Y
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
=========================================  ========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "YA|\\n12|\\n"
        YA|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -3.

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
=========================================  =========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "r\xcc\xa3r\xcc\xa3ay|\\n1234|\\n"
        ṛṛay|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width 3.

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "su'uva|\\n123456|\\n"
        su'uva|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 2.

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+101E <https://codepoints.net/U+101E>`_  '\\u101e'  Lo                  1  MYANMAR LETTER SA
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1087 <https://codepoints.net/U+1087>`_  '\\u1087'  Mc                  0  MYANMAR SIGN SHAN TONE-2
`U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
`U+1086 <https://codepoints.net/U+1086>`_  '\\u1086'  Mn                  0  MYANMAR VOWEL SIGN SHAN FINAL Y
`U+1088 <https://codepoints.net/U+1088>`_  '\\u1088'  Mc                  0  MYANMAR SIGN SHAN TONE-3
=========================================  =========  ==========  =========  ===============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x9e\xe1\x80\xaf\xe1\x81\xbc\xe1\x80\xba\xe1\x82\x87\xe1\x80\x9c\xe1\x82\x86\xe1\x82\x88|\\n123|\\n"
        သုၼ်ႇလႆႈ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width -6.

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
=========================================  =========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc3\xa9rr\xc3\xad\xc5\x8b|\\n123456|\\n"
        térríŋ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 4.

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
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
`U+1010 <https://codepoints.net/U+1010>`_  '\\u1010'  Lo                  1  MYANMAR LETTER TA
`U+103C <https://codepoints.net/U+103C>`_  '\\u103c'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL RA
`U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
`U+100F <https://codepoints.net/U+100F>`_  '\\u100f'  Lo                  1  MYANMAR LETTER NNA
`U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1002 <https://codepoints.net/U+1002>`_  '\\u1002'  Lo                  1  MYANMAR LETTER GA
`U+103E <https://codepoints.net/U+103E>`_  '\\u103e'  Mn                  0  MYANMAR CONSONANT SIGN MEDIAL HA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
=========================================  =========  ==========  =========  ================================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x9c\xe1\x80\xad\xe1\x80\x80\xe1\x80\xba\xe1\x80\x9c\xe1\x80\x9c\xe1\x80\xb1\xe1\x80\xac\xe1\x81\x9a\xe1\x80\xba\xe1\x80\x90\xe1\x80\xbc\xe1\x80\xb8\xe1\x80\x8f\xe1\x80\xa1\xe1\x80\xba\xe1\x80\x82\xe1\x80\xbe\xe1\x80\xba|\\n123456789|\\n"
        လိက်လလောၚ်တြးဏအ်ဂှ်|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *WezTerm* measures width 7.

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "amb|\\n123|\\n"
        amb|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 0.

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================
`U+0784 <https://codepoints.net/U+0784>`_  '\\u0784'  Lo                  1  THAANA LETTER BAA
`U+07A7 <https://codepoints.net/U+07A7>`_  '\\u07a7'  Mn                  0  THAANA AABAAFILI
`U+0783 <https://codepoints.net/U+0783>`_  '\\u0783'  Lo                  1  THAANA LETTER RAA
`U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
=========================================  =========  ==========  =========  =================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x84\xde\xa7\xde\x83\xde\xaa|\\n12|\\n"
        ބާރު|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -4.

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0066 <https://codepoints.net/U+0066>`_  'f'        Ll                  1  LATIN SMALL LETTER F
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
=========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "fe\xcc\x80|\\n12|\\n"
        fè|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -3.

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0054 <https://codepoints.net/U+0054>`_  'T'       Lu                  1  LATIN CAPITAL LETTER T
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Todos|\\n12345|\\n"
        Todos|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 2.

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0927 <https://codepoints.net/U+0927>`_  '\\u0927'  Lo                  1  DEVANAGARI LETTER DHA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
`U+0964 <https://codepoints.net/U+0964>`_  '\\u0964'  Po                  1  DEVANAGARI DANDA
=========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xa7\xe0\xa4\xbe\xe0\xa4\xb0\xe0\xa4\xaf\xe0\xa4\xa4\xe0\xa4\xbf\xe0\xa5\xa4|\\n12345|\\n"
        धारयति।|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 1.

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =====================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =====================
`U+00011327 <https://codepoints.net/U+00011327>`_  '\\U00011327'  Lo                  1  GRANTHA LETTER DHA
`U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
`U+00011330 <https://codepoints.net/U+00011330>`_  '\\U00011330'  Lo                  1  GRANTHA LETTER RA
`U+0001132F <https://codepoints.net/U+0001132F>`_  '\\U0001132f'  Lo                  1  GRANTHA LETTER YA
`U+00011324 <https://codepoints.net/U+00011324>`_  '\\U00011324'  Lo                  1  GRANTHA LETTER TA
`U+0001133F <https://codepoints.net/U+0001133F>`_  '\\U0001133f'  Mc                  0  GRANTHA VOWEL SIGN I
`U+0964 <https://codepoints.net/U+0964>`_          '\\u0964'      Po                  1  DEVANAGARI DANDA
=================================================  =============  ==========  =========  =====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xa7\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xaf\xf0\x91\x8c\xa4\xf0\x91\x8c\xbf\xe0\xa5\xa4|\\n12345|\\n"
        𑌧𑌾𑌰𑌯𑌤𑌿।|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 1.

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+00FB <https://codepoints.net/U+00FB>`_  '\\xfb'   Ll                  1  LATIN SMALL LETTER U WITH CIRCUMFLEX
=========================================  ========  ==========  =========  ====================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "le\xc3\xbb|\\n123|\\n"
        leû|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 1.

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
=========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x9b\xc9\x9b|\\n123|\\n"
        nɛɛ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width -3.

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
  while *WezTerm* measures width -5.

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -4.

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  =================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  =================
`U+0028 <https://codepoints.net/U+0028>`_  '('       Ps                  1  LEFT PARENTHESIS
`U+0038 <https://codepoints.net/U+0038>`_  '8'       Nd                  1  DIGIT EIGHT
`U+0029 <https://codepoints.net/U+0029>`_  ')'       Pe                  1  RIGHT PARENTHESIS
=========================================  ========  ==========  =========  =================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "(8)|\\n123|\\n"
        (8)|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width -7.

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yo|\\n12|\\n"
        yo|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -4.

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yaq|\\n123|\\n"
        yaq|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width -2.

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =======================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =======================
`U+0001E933 <https://codepoints.net/U+0001E933>`_  '\\U0001e933'  Ll                  1  ADLAM SMALL LETTER KAF
`U+0001E92E <https://codepoints.net/U+0001E92E>`_  '\\U0001e92e'  Ll                  1  ADLAM SMALL LETTER O
`U+0001E934 <https://codepoints.net/U+0001E934>`_  '\\U0001e934'  Ll                  1  ADLAM SMALL LETTER YA
`U+0001E932 <https://codepoints.net/U+0001E932>`_  '\\U0001e932'  Ll                  1  ADLAM SMALL LETTER NUN
`U+0001E92E <https://codepoints.net/U+0001E92E>`_  '\\U0001e92e'  Ll                  1  ADLAM SMALL LETTER O
`U+0001E945 <https://codepoints.net/U+0001E945>`_  '\\U0001e945'  Mn                  0  ADLAM VOWEL LENGTHENER
`U+0001E936 <https://codepoints.net/U+0001E936>`_  '\\U0001e936'  Ll                  1  ADLAM SMALL LETTER JIIM
`U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
`U+002E <https://codepoints.net/U+002E>`_          '.'            Po                  1  FULL STOP
=================================================  =============  ==========  =========  =======================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xb3\xf0\x9e\xa4\xae\xf0\x9e\xa4\xb4\xf0\x9e\xa4\xb2\xf0\x9e\xa4\xae\xf0\x9e\xa5\x85\xf0\x9e\xa4\xb6\xf0\x9e\xa4\xab.|\\n12345678|\\n"
        𞤳𞤮𞤴𞤲𞤮𞥅𞤶𞤫.|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 3.

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0CB8 <https://codepoints.net/U+0CB8>`_  '\\u0cb8'  Lo                  1  KANNADA LETTER SA
`U+0CC6 <https://codepoints.net/U+0CC6>`_  '\\u0cc6'  Mn                  0  KANNADA VOWEL SIGN E
`U+0CB0 <https://codepoints.net/U+0CB0>`_  '\\u0cb0'  Lo                  1  KANNADA LETTER RA
`U+0CC6 <https://codepoints.net/U+0CC6>`_  '\\u0cc6'  Mn                  0  KANNADA VOWEL SIGN E
=========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\xb8\xe0\xb3\x86\xe0\xb2\xb0\xe0\xb3\x86|\\n12|\\n"
        ಸೆರೆ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -2.

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mo|\\n12|\\n"
        mo|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -4.

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+06F2 <https://codepoints.net/U+06F2>`_  '\\u06f2'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT TWO
`U+06D4 <https://codepoints.net/U+06D4>`_  '\\u06d4'  Po                  1  ARABIC FULL STOP
=========================================  =========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdb\xb2\xdb\x94|\\n12|\\n"
        ۲۔|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -2.

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
`U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
=========================================  =========  ==========  =========  ==================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x85\xd9\x86\xd9\x8a\xd8\xaa|\\n12345|\\n"
        امنيت|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 0.

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+062C <https://codepoints.net/U+062C>`_  '\\u062c'  Lo                  1  ARABIC LETTER JEEM
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
=========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xac\xd9\x88|\\n12|\\n"
        جو|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -2.

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "w\xc3\xadl\xc3\xa1|\\n1234|\\n"
        wílá|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -1.

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+06F2 <https://codepoints.net/U+06F2>`_  '\\u06f2'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT TWO
=========================================  =========  ==========  =========  ===============================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdb\xb2|\\n1|\\n"
        ۲|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -3.

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
=========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ke\xcc\x81|\\n12|\\n"
        ké|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -1.

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -5.

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0076 <https://codepoints.net/U+0076>`_  'v'        Ll                  1  LATIN SMALL LETTER V
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ===============================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x94\xcc\x81visil\xc3\xa9l\xc3\xa9.|\\n12345678901|\\n"
        nɔ́visilélé.|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *WezTerm* measures width 8.

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0721 <https://codepoints.net/U+0721>`_  '\\u0721'  Lo                  1  SYRIAC LETTER MIM
`U+071A <https://codepoints.net/U+071A>`_  '\\u071a'  Lo                  1  SYRIAC LETTER HETH
`U+0726 <https://codepoints.net/U+0726>`_  '\\u0726'  Lo                  1  SYRIAC LETTER PE
`U+0720 <https://codepoints.net/U+0720>`_  '\\u0720'  Lo                  1  SYRIAC LETTER LAMADH
`U+072C <https://codepoints.net/U+072C>`_  '\\u072c'  Lo                  1  SYRIAC LETTER TAW
`U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
=========================================  =========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\xa1\xdc\x9a\xdc\xa6\xdc\xa0\xdc\xac\xdc\x90|\\n123456|\\n"
        ܡܚܦܠܬܐ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 4.

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
`U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
=========================================  =========  ==========  =========  ===========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ko\xcc\x80\xe2\x80\x99y|\\n1234|\\n"
        kò’y|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -3.

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
  while *WezTerm* measures width -2.

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
`U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
=========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaf\xdb\x92|\\n12|\\n"
        دے|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -1.

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+062E <https://codepoints.net/U+062E>`_  '\\u062e'  Lo                  1  ARABIC LETTER KHAH
`U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
=========================================  =========  ==========  =========  ===================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xb4\xd9\x86\xd8\xa7\xd8\xae\xd8\xaa\xd9\x87|\\n123456|\\n"
        شناخته|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 1.

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ne|\\n12|\\n"
        ne|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -5.

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================================
`U+1EB8 <https://codepoints.net/U+1EB8>`_  '\\u1eb8'  Lu                  1  LATIN CAPITAL LETTER E WITH DOT BELOW
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+00EC <https://codepoints.net/U+00EC>`_  '\\xec'    Ll                  1  LATIN SMALL LETTER I WITH GRAVE
=========================================  =========  ==========  =========  =====================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xba\xb8n\xc3\xac|\\n123|\\n"
        Ẹnì|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width -2.

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -3.

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
`U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ===================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa8\xd8\xa7\xd8\xb4\xd8\xaf.|\\n12345|\\n"
        باشد.|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -4.

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==============================
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+01B0 <https://codepoints.net/U+01B0>`_  '\\u01b0'  Ll                  1  LATIN SMALL LETTER U WITH HORN
`U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
=========================================  =========  ==========  =========  ==============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc6\xb0\xcc\xa3|\\n12|\\n"
        tự|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width 0.

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ci|\\n12|\\n"
        ci|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -1.

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -3.

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "o|\\n1|\\n"
        o|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -2.

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bu|\\n12|\\n"
        bu|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -4.

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0939 <https://codepoints.net/U+0939>`_  '\\u0939'  Lo                  1  DEVANAGARI LETTER HA
`U+094B <https://codepoints.net/U+094B>`_  '\\u094b'  Mc                  0  DEVANAGARI VOWEL SIGN O
`U+0917 <https://codepoints.net/U+0917>`_  '\\u0917'  Lo                  1  DEVANAGARI LETTER GA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
=========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb9\xe0\xa5\x8b\xe0\xa4\x97\xe0\xa4\xbe|\\n12|\\n"
        होगा|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -4.

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ===================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ===================
`U+00011103 <https://codepoints.net/U+00011103>`_  '\\U00011103'  Lo                  1  CHAKMA LETTER AA
`U+00011127 <https://codepoints.net/U+00011127>`_  '\\U00011127'  Mn                  0  CHAKMA VOWEL SIGN A
`U+0001111D <https://codepoints.net/U+0001111D>`_  '\\U0001111d'  Lo                  1  CHAKMA LETTER BAA
`U+00011127 <https://codepoints.net/U+00011127>`_  '\\U00011127'  Mn                  0  CHAKMA VOWEL SIGN A
`U+00011122 <https://codepoints.net/U+00011122>`_  '\\U00011122'  Lo                  1  CHAKMA LETTER RAA
`U+00011116 <https://codepoints.net/U+00011116>`_  '\\U00011116'  Lo                  1  CHAKMA LETTER TAA
`U+00011134 <https://codepoints.net/U+00011134>`_  '\\U00011134'  Mn                  0  CHAKMA MAAYYAA
=================================================  =============  ==========  =========  ===================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\x83\xf0\x91\x84\xa7\xf0\x91\x84\x9d\xf0\x91\x84\xa7\xf0\x91\x84\xa2\xf0\x91\x84\x96\xf0\x91\x84\xb4|\\n1234|\\n"
        𑄃𑄧𑄝𑄧𑄢𑄖𑄴|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -1.

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+A9C8 <https://codepoints.net/U+A9C8>`_  '\\ua9c8'  Po                  1  JAVANESE PADA LINGSA
=========================================  =========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa7\x88|\\n1|\\n"
        ꧈|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -7.

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ji|\\n12|\\n"
        ji|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width 0.

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "moo|\\n123|\\n"
        moo|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 0.

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0939 <https://codepoints.net/U+0939>`_  '\\u0939'  Lo                  1  DEVANAGARI LETTER HA
`U+094B <https://codepoints.net/U+094B>`_  '\\u094b'  Mc                  0  DEVANAGARI VOWEL SIGN O
=========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb9\xe0\xa5\x8b|\\n1|\\n"
        हो|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -2.

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0A35 <https://codepoints.net/U+0A35>`_  '\\u0a35'  Lo                  1  GURMUKHI LETTER VA
`U+0A30 <https://codepoints.net/U+0A30>`_  '\\u0a30'  Lo                  1  GURMUKHI LETTER RA
`U+0A24 <https://codepoints.net/U+0A24>`_  '\\u0a24'  Lo                  1  GURMUKHI LETTER TA
`U+0A3E <https://codepoints.net/U+0A3E>`_  '\\u0a3e'  Mc                  0  GURMUKHI VOWEL SIGN AA
`U+0A13 <https://codepoints.net/U+0A13>`_  '\\u0a13'  Lo                  1  GURMUKHI LETTER OO
=========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\xb5\xe0\xa8\xb0\xe0\xa8\xa4\xe0\xa8\xbe\xe0\xa8\x93|\\n1234|\\n"
        ਵਰਤਾਓ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -1.

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0057 <https://codepoints.net/U+0057>`_  'W'       Lu                  1  LATIN CAPITAL LETTER W
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Wien|\\n1234|\\n"
        Wien|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -3.

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0AB8 <https://codepoints.net/U+0AB8>`_  '\\u0ab8'  Lo                  1  GUJARATI LETTER SA
`U+0AC1 <https://codepoints.net/U+0AC1>`_  '\\u0ac1'  Mn                  0  GUJARATI VOWEL SIGN U
`U+0AA8 <https://codepoints.net/U+0AA8>`_  '\\u0aa8'  Lo                  1  GUJARATI LETTER NA
`U+0ABE <https://codepoints.net/U+0ABE>`_  '\\u0abe'  Mc                  0  GUJARATI VOWEL SIGN AA
`U+0AB5 <https://codepoints.net/U+0AB5>`_  '\\u0ab5'  Lo                  1  GUJARATI LETTER VA
`U+0AA3 <https://codepoints.net/U+0AA3>`_  '\\u0aa3'  Lo                  1  GUJARATI LETTER NNA
`U+0AC0 <https://codepoints.net/U+0AC0>`_  '\\u0ac0'  Mc                  0  GUJARATI VOWEL SIGN II
=========================================  =========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\xb8\xe0\xab\x81\xe0\xaa\xa8\xe0\xaa\xbe\xe0\xaa\xb5\xe0\xaa\xa3\xe0\xab\x80|\\n1234|\\n"
        સુનાવણી|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width 1.

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+AAB9 <https://codepoints.net/U+AAB9>`_  '\\uaab9'  Lo                  1  TAI VIET VOWEL UEA
`U+AA8B <https://codepoints.net/U+AA8B>`_  '\\uaa8b'  Lo                  1  TAI VIET LETTER HIGH CO
=========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xb9\xea\xaa\x8b|\\n12|\\n"
        ꪹꪋ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -2.

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
=========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa4\x95|\\n12|\\n"
        सक|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width 1.

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
=========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xa8\xe0\xa4\xbe|\\n1|\\n"
        ना|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -2.

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "na|\\n12|\\n"
        na|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -3.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
