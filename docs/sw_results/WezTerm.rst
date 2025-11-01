.. _WezTerm:

WezTerm
-------


Tested Software version 20251025-070338-b6e75fd7 on Linux
Full results available at ucs-detect_ repository path
`data/linux-wezterm-20251025-070338-b6e75fd7.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-wezterm-20251025-070338-b6e75fd7.yaml>`_

.. _WezTermscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *WezTerm*:

============  ===========  ==============  ======================================================
Score Type    Raw Score    Scaled Score    Calculation
============  ===========  ==============  ======================================================
WIDE          90.91%       86.4%           (version_index / total_versions) × (pct_success / 100)
ZWJ           75.00%       100.0%          (version_index / total_versions) × (pct_success / 100)
LANG          1.68%        2.1%            languages_supported / total_languages
VS16          0.00%        0.0%            pct_success / 100
VS15          0.00%        0.0%            pct_success / 100
DEC Modes     14.65%       5.0%            modes_supported / total_modes
TIME          465.48s      51.8%           1 - ((elapsed - min) / (max - min)) [inverse]
============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 30.37%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 39.7%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _WezTermwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for WezTerm appears to be 
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

Emoji VS-15 results for *WezTerm* is 158 errors
out of 158 total codepoints tested, 0.0% success.
Sequence of a WIDE Emoji made NARROW by *Variation Selector-15*, from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =====================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =====================
`U+0001F3AE <https://codepoints.net/U+0001F3AE>`_  '\\U0001f3ae'  So                  2  VIDEO GAME
`U+FE0E <https://codepoints.net/U+FE0E>`_          '\\ufe0e'      Mn                  0  VARIATION SELECTOR-15
=================================================  =============  ==========  =========  =====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9f\x8e\xae\xef\xb8\x8e|\\n1|\\n"
        🎮︎|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width 2.


.. _WezTermlang:

Language Support
++++++++++++++++

The following 2 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog).

The following 117 languages are not fully supported:

==============================================================================  ==========  =========  =============
lang                                                                              n_errors    n_total  pct_success
==============================================================================  ==========  =========  =============
:ref:`Malayalam <WezTermlangMalayalam>`                                                133       1630  91.8%
:ref:`Sanskrit <WezTermlangSanskrit>`                                                   80       1000  92.0%
:ref:`Sinhala <WezTermlangSinhala>`                                                    112       1655  93.2%
:ref:`Telugu <WezTermlangTelugu>`                                                       55       1129  95.1%
:ref:`Nepali <WezTermlangNepali>`                                                       63       1385  95.5%
:ref:`Maithili <WezTermlangMaithili>`                                                   66       1519  95.7%
:ref:`Marathi <WezTermlangMarathi>`                                                     70       1614  95.7%
:ref:`Chinese, Mandarin (Tianjin) <WezTermlangChineseMandarinTianjin>`                   5        212  97.6%
:ref:`Hindi <WezTermlangHindi>`                                                         50       2128  97.7%
:ref:`Tamang, Eastern <WezTermlangTamangEastern>`                                        1         45  97.8%
:ref:`Vietnamese (Han nom) <WezTermlangVietnameseHannom>`                                4        199  98.0%
:ref:`Gujarati <WezTermlangGujarati>`                                                   30       1536  98.0%
:ref:`Japanese (Osaka) <WezTermlangJapaneseOsaka>`                                       6        308  98.1%
:ref:`Thai (2) <WezTermlangThai2>`                                                       6        313  98.1%
:ref:`(Jinan) <WezTermlangJinan>`                                                        4        211  98.1%
:ref:`Chinese, Wu <WezTermlangChineseWu>`                                                4        211  98.1%
:ref:`Chinese, Mandarin (Nanjing) <WezTermlangChineseMandarinNanjing>`                   4        212  98.1%
:ref:`Chinese, Min Nan <WezTermlangChineseMinNan>`                                       4        212  98.1%
:ref:`Bhojpuri <WezTermlangBhojpuri>`                                                   32       1737  98.2%
:ref:`Nuosu <WezTermlangNuosu>`                                                          4        230  98.3%
:ref:`Bengali <WezTermlangBengali>`                                                     24       1413  98.3%
:ref:`Japanese <WezTermlangJapanese>`                                                    5        299  98.3%
:ref:`Magahi <WezTermlangMagahi>`                                                       27       1716  98.4%
:ref:`Japanese (Tokyo) <WezTermlangJapaneseTokyo>`                                       5        320  98.4%
:ref:`Thai <WezTermlangThai>`                                                            5        341  98.5%
:ref:`Chinese, Mandarin (Harbin) <WezTermlangChineseMandarinHarbin>`                     3        210  98.6%
:ref:`Chinese, Mandarin (Traditional) <WezTermlangChineseMandarinTraditional>`           3        210  98.6%
:ref:`Chinese, Yue <WezTermlangChineseYue>`                                              3        210  98.6%
:ref:`Chinese, Gan <WezTermlangChineseGan>`                                              3        211  98.6%
:ref:`Chinese, Mandarin (Guiyang) <WezTermlangChineseMandarinGuiyang>`                   3        211  98.6%
:ref:`Chinese, Mandarin (Beijing) <WezTermlangChineseMandarinBeijing>`                   3        212  98.6%
:ref:`Chinese, Xiang <WezTermlangChineseXiang>`                                          3        212  98.6%
:ref:`Chinese, Mandarin (Simplified) <WezTermlangChineseMandarinSimplified>`             3        225  98.7%
:ref:`Lao <WezTermlangLao>`                                                              5        426  98.8%
:ref:`Khmer, Central <WezTermlangKhmerCentral>`                                          5        528  99.1%
:ref:`Chinese, Hakka <WezTermlangChineseHakka>`                                          2        212  99.1%
:ref:`Chinese, Jinyu <WezTermlangChineseJinyu>`                                          2        212  99.1%
:ref:`Chickasaw <WezTermlangChickasaw>`                                                  4        554  99.3%
:ref:`Bora <WezTermlangBora>`                                                           11       1598  99.3%
:ref:`Khün <WezTermlangKhn>`                                                             3        442  99.3%
:ref:`Gumuz <WezTermlangGumuz>`                                                          8       1283  99.4%
:ref:`Shipibo-Conibo <WezTermlangShipiboConibo>`                                        15       2540  99.4%
:ref:`Nanai <WezTermlangNanai>`                                                          7       1207  99.4%
:ref:`Navajo <WezTermlangNavajo>`                                                        9       1600  99.4%
:ref:`Orok <WezTermlangOrok>`                                                            7       1245  99.4%
:ref:`Evenki <WezTermlangEvenki>`                                                        5        899  99.4%
:ref:`Amarakaeri <WezTermlangAmarakaeri>`                                                8       1446  99.4%
:ref:`Yaneshaʼ <WezTermlangYanesha>`                                                    14       2536  99.4%
:ref:`Shan <WezTermlangShan>`                                                            5        915  99.5%
:ref:`Siona <WezTermlangSiona>`                                                          8       1492  99.5%
:ref:`Gilyak <WezTermlangGilyak>`                                                        8       1504  99.5%
:ref:`Veps <WezTermlangVeps>`                                                            7       1323  99.5%
:ref:`South Azerbaijani <WezTermlangSouthAzerbaijani>`                                   7       1396  99.5%
:ref:`Secoya <WezTermlangSecoya>`                                                        7       1409  99.5%
:ref:`Tamil (Sri Lanka) <WezTermlangTamilSriLanka>`                                      6       1261  99.5%
:ref:`Tamil <WezTermlangTamil>`                                                          6       1262  99.5%
:ref:`Colorado <WezTermlangColorado>`                                                    6       1263  99.5%
:ref:`(Yeonbyeon) <WezTermlangYeonbyeon>`                                                5       1061  99.5%
:ref:`Kannada <WezTermlangKannada>`                                                      5       1080  99.5%
:ref:`Mon <WezTermlangMon>`                                                              4        946  99.6%
:ref:`Korean <WezTermlangKorean>`                                                        5       1185  99.6%
:ref:`Tem <WezTermlangTem>`                                                              7       1659  99.6%
:ref:`Catalan (2) <WezTermlangCatalan2>`                                                 8       1909  99.6%
:ref:`Burmese <WezTermlangBurmese>`                                                      5       1223  99.6%
:ref:`Mirandese <WezTermlangMirandese>`                                                  8       1966  99.6%
:ref:`Éwé <WezTermlangw>`                                                                9       2230  99.6%
:ref:`Sanskrit (Grantha) <WezTermlangSanskritGrantha>`                                   4       1006  99.6%
:ref:`Picard <WezTermlangPicard>`                                                        8       2024  99.6%
:ref:`Yiddish, Eastern <WezTermlangYiddishEastern>`                                      7       1775  99.6%
:ref:`Ticuna <WezTermlangTicuna>`                                                        8       2048  99.6%
:ref:`Kabyle <WezTermlangKabyle>`                                                        7       1815  99.6%
:ref:`Lingala (tones) <WezTermlangLingalatones>`                                         7       1818  99.6%
:ref:`Tamazight, Central Atlas <WezTermlangTamazightCentralAtlas>`                       7       1822  99.6%
:ref:`Fur <WezTermlangFur>`                                                              7       1838  99.6%
:ref:`Pular (Adlam) <WezTermlangPularAdlam>`                                             6       1613  99.6%
:ref:`Arabic, Standard <WezTermlangArabicStandard>`                                      5       1348  99.6%
:ref:`Mixtec, Metlatónoc <WezTermlangMixtecMetlatnoc>`                                   5       1367  99.6%
:ref:`Maldivian <WezTermlangMaldivian>`                                                  7       1918  99.6%
:ref:`French (Welche) <WezTermlangFrenchWelche>`                                         7       1928  99.6%
:ref:`Gen <WezTermlangGen>`                                                              8       2309  99.7%
:ref:`Assyrian Neo-Aramaic <WezTermlangAssyrianNeoAramaic>`                              4       1160  99.7%
:ref:`Ga <WezTermlangGa>`                                                                7       2039  99.7%
:ref:`Aja <WezTermlangAja>`                                                              7       2061  99.7%
:ref:`Uduk <WezTermlangUduk>`                                                           11       3247  99.7%
:ref:`Saint Lucian Creole French <WezTermlangSaintLucianCreoleFrench>`                   6       1777  99.7%
:ref:`Maori (2) <WezTermlangMaori2>`                                                     8       2385  99.7%
:ref:`Farsi, Western <WezTermlangFarsiWestern>`                                          6       1822  99.7%
:ref:`Dinka, Northeastern <WezTermlangDinkaNortheastern>`                                5       1529  99.7%
:ref:`Yoruba <WezTermlangYoruba>`                                                        8       2454  99.7%
:ref:`Dari <WezTermlangDari>`                                                            6       1872  99.7%
:ref:`Vietnamese <WezTermlangVietnamese>`                                                8       2502  99.7%
:ref:`Ditammari <WezTermlangDitammari>`                                                  6       1882  99.7%
:ref:`Dendi <WezTermlangDendi>`                                                          5       1569  99.7%
:ref:`Mazahua Central <WezTermlangMazahuaCentral>`                                       5       1574  99.7%
:ref:`Serer-Sine <WezTermlangSererSine>`                                                 5       1596  99.7%
:ref:`Urdu <WezTermlangUrdu>`                                                            7       2237  99.7%
:ref:`Pashto, Northern <WezTermlangPashtoNorthern>`                                      7       2242  99.7%
:ref:`Seraiki <WezTermlangSeraiki>`                                                      7       2242  99.7%
:ref:`Belanda Viri <WezTermlangBelandaViri>`                                             7       2246  99.7%
:ref:`Urdu (2) <WezTermlangUrdu2>`                                                       7       2251  99.7%
:ref:`Dagaare, Southern <WezTermlangDagaareSouthern>`                                    8       2582  99.7%
:ref:`Baatonum <WezTermlangBaatonum>`                                                    6       1939  99.7%
:ref:`Bamun <WezTermlangBamun>`                                                          7       2285  99.7%
:ref:`Waama <WezTermlangWaama>`                                                          3       1000  99.7%
:ref:`Panjabi, Western <WezTermlangPanjabiWestern>`                                      7       2419  99.7%
:ref:`Chinantec, Chiltepec <WezTermlangChinantecChiltepec>`                              5       1729  99.7%
:ref:`Mòoré <WezTermlangMor>`                                                            7       2447  99.7%
:ref:`Fon <WezTermlangFon>`                                                              7       2520  99.7%
:ref:`Chakma <WezTermlangChakma>`                                                        4       1444  99.7%
:ref:`Javanese (Javanese) <WezTermlangJavaneseJavanese>`                                 4       1453  99.7%
:ref:`Otomi, Mezquital <WezTermlangOtomiMezquital>`                                      5       1849  99.7%
:ref:`Lamnso' <WezTermlangLamnso>`                                                       6       2237  99.7%
:ref:`Dangme <WezTermlangDangme>`                                                        7       2912  99.8%
:ref:`Tibetan, Central <WezTermlangTibetanCentral>`                                      7       3174  99.8%
:ref:`Panjabi, Eastern <WezTermlangPanjabiEastern>`                                      5       2293  99.8%
:ref:`Tai Dam <WezTermlangTaiDam>`                                                       5       2386  99.8%
:ref:`Dzongkha <WezTermlangDzongkha>`                                                    6       3060  99.8%
==============================================================================  ==========  =========  =============

.. _WezTermlangMalayalam:

Malayalam
^^^^^^^^^

Sequence of language *Malayalam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+0D38 <https://codepoints.net/U+0D38>`_  '\\u0d38'  Lo                  1  MALAYALAM LETTER SA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D35 <https://codepoints.net/U+0D35>`_  '\\u0d35'  Lo                  1  MALAYALAM LETTER VA
`U+0D3E <https://codepoints.net/U+0D3E>`_  '\\u0d3e'  Mc                  0  MALAYALAM VOWEL SIGN AA
`U+0D24 <https://codepoints.net/U+0D24>`_  '\\u0d24'  Lo                  1  MALAYALAM LETTER TA
`U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D24 <https://codepoints.net/U+0D24>`_  '\\u0d24'  Lo                  1  MALAYALAM LETTER TA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D30 <https://codepoints.net/U+0D30>`_  '\\u0d30'  Lo                  1  MALAYALAM LETTER RA
`U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
`U+0D2F <https://codepoints.net/U+0D2F>`_  '\\u0d2f'  Lo                  1  MALAYALAM LETTER YA
`U+0D02 <https://codepoints.net/U+0D02>`_  '\\u0d02'  Mc                  0  MALAYALAM SIGN ANUSVARA
=========================================  =========  ==========  =========  =======================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb4\xb8\xe0\xb5\x8d\xe0\xb4\xb5\xe0\xb4\xbe\xe0\xb4\xa4\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa4\xe0\xb5\x8d\xe0\xb4\xb0\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\x82|\\n1234567|\\n"
        സ്വാതന്ത്ര്യം|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *WezTerm* measures width 5.

.. _WezTermlangSanskrit:

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
`U+0917 <https://codepoints.net/U+0917>`_  '\\u0917'  Lo                  1  DEVANAGARI LETTER GA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
`U+0936 <https://codepoints.net/U+0936>`_  '\\u0936'  Lo                  1  DEVANAGARI LETTER SHA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+091A <https://codepoints.net/U+091A>`_  '\\u091a'  Lo                  1  DEVANAGARI LETTER CA
`U+007D <https://codepoints.net/U+007D>`_  '}'        Pe                  1  RIGHT CURLY BRACKET
=========================================  =========  ==========  =========  ========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa4\xbe\xe0\xa4\xae\xe0\xa4\x97\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xb6\xe0\xa5\x8d\xe0\xa4\x9a}|\\n12345678|\\n"
        सामग्र्यश्च}|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 7.

.. _WezTermlangSinhala:

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

.. _WezTermlangTelugu:

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0C38 <https://codepoints.net/U+0C38>`_  '\\u0c38'  Lo                  1  TELUGU LETTER SA
`U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
`U+0C35 <https://codepoints.net/U+0C35>`_  '\\u0c35'  Lo                  1  TELUGU LETTER VA
`U+0C3E <https://codepoints.net/U+0C3E>`_  '\\u0c3e'  Mn                  0  TELUGU VOWEL SIGN AA
`U+0C24 <https://codepoints.net/U+0C24>`_  '\\u0c24'  Lo                  1  TELUGU LETTER TA
`U+0C02 <https://codepoints.net/U+0C02>`_  '\\u0c02'  Mc                  0  TELUGU SIGN ANUSVARA
`U+0C24 <https://codepoints.net/U+0C24>`_  '\\u0c24'  Lo                  1  TELUGU LETTER TA
`U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
`U+0C30 <https://codepoints.net/U+0C30>`_  '\\u0c30'  Lo                  1  TELUGU LETTER RA
`U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
`U+0C2F <https://codepoints.net/U+0C2F>`_  '\\u0c2f'  Lo                  1  TELUGU LETTER YA
=========================================  =========  ==========  =========  ====================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xbe\xe0\xb0\xa4\xe0\xb0\x82\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb0\xe0\xb1\x8d\xe0\xb0\xaf|\\n123456|\\n"
        స్వాతంత్ర్య|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 5.

.. _WezTermlangNepali:

Nepali
^^^^^^

Sequence of language *Nepali* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
=========================================  =========  ==========  =========  ========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xb5\xe0\xa4\xa4\xe0\xa4\xa8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa4\xa4\xe0\xa4\xbe|\\n1234567|\\n"
        स्वतन्त्रता|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *WezTerm* measures width 6.

.. _WezTermlangMaithili:

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0028 <https://codepoints.net/U+0028>`_  '('        Ps                  1  LEFT PARENTHESIS
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0937 <https://codepoints.net/U+0937>`_  '\\u0937'  Lo                  1  DEVANAGARI LETTER SSA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+091F <https://codepoints.net/U+091F>`_  '\\u091f'  Lo                  1  DEVANAGARI LETTER TTA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
`U+0918 <https://codepoints.net/U+0918>`_  '\\u0918'  Lo                  1  DEVANAGARI LETTER GHA
`U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
=========================================  =========  ==========  =========  ========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "(\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xb7\xe0\xa5\x8d\xe0\xa4\x9f\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa4\xb8\xe0\xa4\x82\xe0\xa4\x98\xe0\xa4\x95|\\n12345678|\\n"
        (राष्ट्रसंघक|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 7.

.. _WezTermlangMarathi:

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
=========================================  =========  ==========  =========  ========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa4\xe0\xa4\x82\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xaf|\\n123456|\\n"
        स्वातंत्र्य|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 5.

.. _WezTermlangChineseMandarinTianjin:

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -20.

.. _WezTermlangHindi:

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0937 <https://codepoints.net/U+0937>`_  '\\u0937'  Lo                  1  DEVANAGARI LETTER SSA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+091F <https://codepoints.net/U+091F>`_  '\\u091f'  Lo                  1  DEVANAGARI LETTER TTA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+094B <https://codepoints.net/U+094B>`_  '\\u094b'  Mc                  0  DEVANAGARI VOWEL SIGN O
`U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
=========================================  =========  ==========  =========  ========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xb7\xe0\xa5\x8d\xe0\xa4\x9f\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa5\x8b\xe0\xa4\x82|\\n1234|\\n"
        राष्ट्रों|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width 3.

.. _WezTermlangTamangEastern:

Tamang, Eastern
^^^^^^^^^^^^^^^

Sequence of language *Tamang, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0028 <https://codepoints.net/U+0028>`_  '('        Ps                  1  LEFT PARENTHESIS
`U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+0029 <https://codepoints.net/U+0029>`_  ')'        Pe                  1  RIGHT PARENTHESIS
=========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "(\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xb5\xe0\xa4\xa4\xe0\xa4\xa8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xb0)|\\n12345678|\\n"
        (स्वतन्त्र)|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 7.

.. _WezTermlangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+689D <https://codepoints.net/U+689D>`_  '\\u689d'  Lo                  2  CJK UNIFIED IDEOGRAPH-689D
`U+0032 <https://codepoints.net/U+0032>`_  '2'        Nd                  1  DIGIT TWO
`U+FF1A <https://codepoints.net/U+FF1A>`_  '\\uff1a'  Po                  2  FULLWIDTH COLON
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xa2\x9d2\xef\xbc\x9a|\\n12345|\\n"
        條2：|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -45.

.. _WezTermlangGujarati:

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0AAE <https://codepoints.net/U+0AAE>`_  '\\u0aae'  Lo                  1  GUJARATI LETTER MA
`U+0AB9 <https://codepoints.net/U+0AB9>`_  '\\u0ab9'  Lo                  1  GUJARATI LETTER HA
`U+0AA4 <https://codepoints.net/U+0AA4>`_  '\\u0aa4'  Lo                  1  GUJARATI LETTER TA
`U+0ACD <https://codepoints.net/U+0ACD>`_  '\\u0acd'  Mn                  0  GUJARATI SIGN VIRAMA
`U+0AA4 <https://codepoints.net/U+0AA4>`_  '\\u0aa4'  Lo                  1  GUJARATI LETTER TA
`U+0ACD <https://codepoints.net/U+0ACD>`_  '\\u0acd'  Mn                  0  GUJARATI SIGN VIRAMA
`U+0AB5 <https://codepoints.net/U+0AB5>`_  '\\u0ab5'  Lo                  1  GUJARATI LETTER VA
`U+0ABE <https://codepoints.net/U+0ABE>`_  '\\u0abe'  Mc                  0  GUJARATI VOWEL SIGN AA
`U+0A95 <https://codepoints.net/U+0A95>`_  '\\u0a95'  Lo                  1  GUJARATI LETTER KA
`U+0ABE <https://codepoints.net/U+0ABE>`_  '\\u0abe'  Mc                  0  GUJARATI VOWEL SIGN AA
`U+0A82 <https://codepoints.net/U+0A82>`_  '\\u0a82'  Mn                  0  GUJARATI SIGN ANUSVARA
`U+0A95 <https://codepoints.net/U+0A95>`_  '\\u0a95'  Lo                  1  GUJARATI LETTER KA
`U+0ACD <https://codepoints.net/U+0ACD>`_  '\\u0acd'  Mn                  0  GUJARATI SIGN VIRAMA
`U+0AB7 <https://codepoints.net/U+0AB7>`_  '\\u0ab7'  Lo                  1  GUJARATI LETTER SSA
`U+0ABE <https://codepoints.net/U+0ABE>`_  '\\u0abe'  Mc                  0  GUJARATI VOWEL SIGN AA
=========================================  =========  ==========  =========  ======================

Total codepoints: 15


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\xae\xe0\xaa\xb9\xe0\xaa\xa4\xe0\xab\x8d\xe0\xaa\xa4\xe0\xab\x8d\xe0\xaa\xb5\xe0\xaa\xbe\xe0\xaa\x95\xe0\xaa\xbe\xe0\xaa\x82\xe0\xaa\x95\xe0\xab\x8d\xe0\xaa\xb7\xe0\xaa\xbe|\\n12345678|\\n"
        મહત્ત્વાકાંક્ષા|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 7.

.. _WezTermlangJapaneseOsaka:

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
  while *WezTerm* measures width -20.

.. _WezTermlangThai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+0E41 <https://codepoints.net/U+0E41>`_  '\\u0e41'  Lo                  1  THAI CHARACTER SARA AE
`U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
`U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
`U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
`U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
`U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
`U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
`U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
`U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
`U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
`U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
`U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
=========================================  =========  ==========  =========  ===========================

Total codepoints: 20


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x81\xe0\xb8\xa5\xe0\xb8\xb0\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x95\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\xb1\xe0\xb9\x89\xe0\xb8\x87\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb2\xe0\xb8\xa2|\\n12345678901234567|\\n"
        และประชาชาติทั้งหลาย|
        12345678901234567|

- python `wcwidth.wcswidth()`_ measures width 17,
  while *WezTerm* measures width -29.

.. _WezTermlangJinan:

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -20.

.. _WezTermlangChineseWu:

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -20.

.. _WezTermlangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+65E0 <https://codepoints.net/U+65E0>`_  '\\u65e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E0
`U+8BBA <https://codepoints.net/U+8BBA>`_  '\\u8bba'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BBA
`U+8BE5 <https://codepoints.net/U+8BE5>`_  '\\u8be5'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BE5
`U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
`U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
`U+662F <https://codepoints.net/U+662F>`_  '\\u662f'  Lo                  2  CJK UNIFIED IDEOGRAPH-662F
`U+72EC <https://codepoints.net/U+72EC>`_  '\\u72ec'  Lo                  2  CJK UNIFIED IDEOGRAPH-72EC
`U+7ACB <https://codepoints.net/U+7ACB>`_  '\\u7acb'  Lo                  2  CJK UNIFIED IDEOGRAPH-7ACB
`U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
`U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
=========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x97\xa0\xe8\xae\xba\xe8\xaf\xa5\xe9\xa2\x86\xe5\x9c\x9f\xe6\x98\xaf\xe7\x8b\xac\xe7\xab\x8b\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678901234567890|\\n"
        无论该领土是独立领土|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *WezTerm* measures width -16.

.. _WezTermlangChineseMinNan:

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
`U+4E14 <https://codepoints.net/U+4E14>`_  '\\u4e14'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E14
`U+52FF <https://codepoints.net/U+52FF>`_  '\\u52ff'  Lo                  2  CJK UNIFIED IDEOGRAPH-52FF
`U+4F1A <https://codepoints.net/U+4F1A>`_  '\\u4f1a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F1A
`U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
`U+56E0 <https://codepoints.net/U+56E0>`_  '\\u56e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-56E0
`U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
`U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
`U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
`U+5C5E <https://codepoints.net/U+5C5E>`_  '\\u5c5e'  Lo                  2  CJK UNIFIED IDEOGRAPH-5C5E
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
`U+6291 <https://codepoints.net/U+6291>`_  '\\u6291'  Lo                  2  CJK UNIFIED IDEOGRAPH-6291
`U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
=========================================  =========  ==========  =========  ==========================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe4\xb8\x94\xe5\x8b\xbf\xe4\xbc\x9a\xe7\x94\xa8\xe5\x9b\xa0\xe4\xb8\x80\xe4\xba\xba\xe6\x89\x80\xe5\xb1\x9e\xe7\x9a\x84\xe5\x9b\xbd\xe5\xae\xb6\xe6\x8a\x91\xe5\x9c\xb0\xe7\x9a\x84\xe6\x94\xbf\xe6\xb2\xbb\xe7\x9a\x84|\\n12345678901234567890123456789012345678|\\n"
        并且勿会用因一人所属的国家抑地的政治的|
        12345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 38,
  while *WezTerm* measures width 14.

.. _WezTermlangBhojpuri:

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0937 <https://codepoints.net/U+0937>`_  '\\u0937'  Lo                  1  DEVANAGARI LETTER SSA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+091F <https://codepoints.net/U+091F>`_  '\\u091f'  Lo                  1  DEVANAGARI LETTER TTA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
=========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xb7\xe0\xa5\x8d\xe0\xa4\x9f\xe0\xa5\x8d\xe0\xa4\xb0|\\n1234|\\n"
        राष्ट्र|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width 3.

.. _WezTermlangNuosu:

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================
`U+A354 <https://codepoints.net/U+A354>`_  '\\ua354'  Lo                  2  YI SYLLABLE ZHEP
`U+A35E <https://codepoints.net/U+A35E>`_  '\\ua35e'  Lo                  2  YI SYLLABLE ZHYP
`U+A30B <https://codepoints.net/U+A30B>`_  '\\ua30b'  Lo                  2  YI SYLLABLE SI
`U+A180 <https://codepoints.net/U+A180>`_  '\\ua180'  Lo                  2  YI SYLLABLE NIP
`U+A009 <https://codepoints.net/U+A009>`_  '\\ua009'  Lo                  2  YI SYLLABLE AX
`U+A041 <https://codepoints.net/U+A041>`_  '\\ua041'  Lo                  2  YI SYLLABLE PA
`U+A45E <https://codepoints.net/U+A45E>`_  '\\ua45e'  Lo                  2  YI SYLLABLE XIX
`U+A25C <https://codepoints.net/U+A25C>`_  '\\ua25c'  Lo                  2  YI SYLLABLE HXEP
`U+A428 <https://codepoints.net/U+A428>`_  '\\ua428'  Lo                  2  YI SYLLABLE JJUX
=========================================  =========  ==========  =========  ================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x8d\x94\xea\x8d\x9e\xea\x8c\x8b\xea\x86\x80\xea\x80\x89\xea\x81\x81\xea\x91\x9e\xea\x89\x9c\xea\x90\xa8|\\n123456789012345678|\\n"
        ꍔꍞꌋꆀꀉꁁꑞꉜꐨ|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *WezTerm* measures width 10.

.. _WezTermlangBengali:

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

.. _WezTermlangJapanese:

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
  while *WezTerm* measures width -42.

.. _WezTermlangMagahi:

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
`U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
`U+0937 <https://codepoints.net/U+0937>`_  '\\u0937'  Lo                  1  DEVANAGARI LETTER SSA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+091F <https://codepoints.net/U+091F>`_  '\\u091f'  Lo                  1  DEVANAGARI LETTER TTA
`U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
`U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
=========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xb7\xe0\xa5\x8d\xe0\xa4\x9f\xe0\xa5\x8d\xe0\xa4\xb0|\\n1234|\\n"
        राष्ट्र|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width 3.

.. _WezTermlangJapaneseTokyo:

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5168 <https://codepoints.net/U+5168>`_  '\\u5168'  Lo                  2  CJK UNIFIED IDEOGRAPH-5168
`U+90E8 <https://codepoints.net/U+90E8>`_  '\\u90e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-90E8
`U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
`U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
`U+306F <https://codepoints.net/U+306F>`_  '\\u306f'  Lo                  2  HIRAGANA LETTER HA
=========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\xa8\xe9\x83\xa8\xe3\x81\xae\xe4\xba\xba\xe3\x81\xaf|\\n1234567890|\\n"
        全部の人は|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *WezTerm* measures width -42.

.. _WezTermlangThai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0E42 <https://codepoints.net/U+0E42>`_  '\\u0e42'  Lo                  1  THAI CHARACTER SARA O
`U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
`U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
`U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
`U+0E33 <https://codepoints.net/U+0E33>`_  '\\u0e33'  Lo                  1  THAI CHARACTER SARA AM
`U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
`U+0E36 <https://codepoints.net/U+0E36>`_  '\\u0e36'  Mn                  0  THAI CHARACTER SARA UE
`U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
`U+0E16 <https://codepoints.net/U+0E16>`_  '\\u0e16'  Lo                  1  THAI CHARACTER THO THUNG
`U+0E36 <https://codepoints.net/U+0E36>`_  '\\u0e36'  Mn                  0  THAI CHARACTER SARA UE
`U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
`U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
`U+0E0F <https://codepoints.net/U+0E0F>`_  '\\u0e0f'  Lo                  1  THAI CHARACTER TO PATAK
`U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
`U+0E0D <https://codepoints.net/U+0E0D>`_  '\\u0e0d'  Lo                  1  THAI CHARACTER YO YING
`U+0E0D <https://codepoints.net/U+0E0D>`_  '\\u0e0d'  Lo                  1  THAI CHARACTER YO YING
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
`U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
`U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
`U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
`U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
`U+0E47 <https://codepoints.net/U+0E47>`_  '\\u0e47'  Mn                  0  THAI CHARACTER MAITAIKHU
`U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
`U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
`U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
`U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
`U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
`U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
`U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
`U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
`U+0E08 <https://codepoints.net/U+0E08>`_  '\\u0e08'  Lo                  1  THAI CHARACTER CHO CHAN
=========================================  =========  ==========  =========  ========================

Total codepoints: 35


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x82\xe0\xb8\x94\xe0\xb8\xa2\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa3\xe0\xb8\xb3\xe0\xb8\xa5\xe0\xb8\xb6\xe0\xb8\x81\xe0\xb8\x96\xe0\xb8\xb6\xe0\xb8\x87\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xb5\xe0\xb9\x89\xe0\xb9\x80\xe0\xb8\x9b\xe0\xb9\x87\xe0\xb8\x99\xe0\xb9\x80\xe0\xb8\x99\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb8\x87\xe0\xb8\x99\xe0\xb8\xb4\xe0\xb8\x88|\\n123456789012345678901234567|\\n"
        โดยการรำลึกถึงปฏิญญานี้เป็นเนืองนิจ|
        123456789012345678901234567|

- python `wcwidth.wcswidth()`_ measures width 27,
  while *WezTerm* measures width -6.

.. _WezTermlangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
`U+4E14 <https://codepoints.net/U+4E14>`_  '\\u4e14'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E14
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
`U+56E0 <https://codepoints.net/U+56E0>`_  '\\u56e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-56E0
`U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
`U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
`U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
`U+5C5E <https://codepoints.net/U+5C5E>`_  '\\u5c5e'  Lo                  2  CJK UNIFIED IDEOGRAPH-5C5E
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
`U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
`U+7247 <https://codepoints.net/U+7247>`_  '\\u7247'  Lo                  2  CJK UNIFIED IDEOGRAPH-7247
`U+513F <https://codepoints.net/U+513F>`_  '\\u513f'  Lo                  2  CJK UNIFIED IDEOGRAPH-513F
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
=========================================  =========  ==========  =========  ==========================

Total codepoints: 20


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe4\xb8\x94\xe4\xb8\x8d\xe5\xbe\x97\xe5\x9b\xa0\xe4\xb8\x80\xe4\xba\xba\xe6\x89\x80\xe5\xb1\x9e\xe7\x9a\x84\xe5\x9b\xbd\xe5\xae\xb6\xe6\x88\x96\xe5\x9c\xb0\xe7\x89\x87\xe5\x84\xbf\xe7\x9a\x84\xe6\x94\xbf\xe6\xb2\xbb\xe7\x9a\x84|\\n1234567890123456789012345678901234567890|\\n"
        并且不得因一人所属的国家或地片儿的政治的|
        1234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 40,
  while *WezTerm* measures width 16.

.. _WezTermlangChineseMandarinTraditional:

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
`U+689D <https://codepoints.net/U+689D>`_  '\\u689d'  Lo                  2  CJK UNIFIED IDEOGRAPH-689D
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\xa2\x9d|\\n123456|\\n"
        第二條|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -20.

.. _WezTermlangChineseYue:

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -24.

.. _WezTermlangChineseGan:

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -16.

.. _WezTermlangChineseMandarinGuiyang:

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -22.

.. _WezTermlangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+80A4 <https://codepoints.net/U+80A4>`_  '\\u80a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-80A4
`U+8272 <https://codepoints.net/U+8272>`_  '\\u8272'  Lo                  2  CJK UNIFIED IDEOGRAPH-8272
=========================================  =========  ==========  =========  ==========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x82\xa4\xe8\x89\xb2|\\n1234|\\n"
        肤色|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -4.

.. _WezTermlangChineseXiang:

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+8272 <https://codepoints.net/U+8272>`_  '\\u8272'  Lo                  2  CJK UNIFIED IDEOGRAPH-8272
`U+6C14 <https://codepoints.net/U+6C14>`_  '\\u6c14'  Lo                  2  CJK UNIFIED IDEOGRAPH-6C14
=========================================  =========  ==========  =========  ==========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x89\xb2\xe6\xb0\x94|\\n1234|\\n"
        色气|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -4.

.. _WezTermlangChineseMandarinSimplified:

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
`U+89C6 <https://codepoints.net/U+89C6>`_  '\\u89c6'  Lo                  2  CJK UNIFIED IDEOGRAPH-89C6
`U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
`U+65E0 <https://codepoints.net/U+65E0>`_  '\\u65e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E0
`U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x9c\x89\xe6\x9d\x83\xe8\xa2\xab\xe8\xa7\x86\xe4\xb8\xba\xe6\x97\xa0\xe7\xbd\xaa|\\n12345678901234|\\n"
        有权被视为无罪|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *WezTerm* measures width -44.

.. _WezTermlangLao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -4.

.. _WezTermlangKhmerCentral:

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+1791 <https://codepoints.net/U+1791>`_  '\\u1791'  Lo                  1  KHMER LETTER TO
`U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
`U+17C6 <https://codepoints.net/U+17C6>`_  '\\u17c6'  Mn                  0  KHMER SIGN NIKAHIT
`U+1784 <https://codepoints.net/U+1784>`_  '\\u1784'  Lo                  1  KHMER LETTER NGO
`U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
`U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
`U+1793 <https://codepoints.net/U+1793>`_  '\\u1793'  Lo                  1  KHMER LETTER NO
`U+17BB <https://codepoints.net/U+17BB>`_  '\\u17bb'  Mn                  0  KHMER VOWEL SIGN U
`U+1784 <https://codepoints.net/U+1784>`_  '\\u1784'  Lo                  1  KHMER LETTER NGO
`U+1785 <https://codepoints.net/U+1785>`_  '\\u1785'  Lo                  1  KHMER LETTER CA
`U+17C6 <https://codepoints.net/U+17C6>`_  '\\u17c6'  Mn                  0  KHMER SIGN NIKAHIT
`U+178E <https://codepoints.net/U+178E>`_  '\\u178e'  Lo                  1  KHMER LETTER NNO
`U+17C4 <https://codepoints.net/U+17C4>`_  '\\u17c4'  Mc                  0  KHMER VOWEL SIGN OO
`U+1798 <https://codepoints.net/U+1798>`_  '\\u1798'  Lo                  1  KHMER LETTER MO
=========================================  =========  ==========  =========  ===================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x91\xe1\x9e\xb6\xe1\x9f\x86\xe1\x9e\x84\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x84\xe1\x9e\x85\xe1\x9f\x86\xe1\x9e\x8e\xe1\x9f\x84\xe1\x9e\x98|\\n12345678|\\n"
        ទាំងក្នុងចំណោម|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width -16.

.. _WezTermlangChineseHakka:

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -20.

.. _WezTermlangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+80A4 <https://codepoints.net/U+80A4>`_  '\\u80a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-80A4
`U+8272 <https://codepoints.net/U+8272>`_  '\\u8272'  Lo                  2  CJK UNIFIED IDEOGRAPH-8272
=========================================  =========  ==========  =========  ==========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x82\xa4\xe8\x89\xb2|\\n1234|\\n"
        肤色|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -6.

.. _WezTermlangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "holisso|\\n1234567|\\n"
        holisso|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *WezTerm* measures width -8.

.. _WezTermlangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tsaate|\\n123456|\\n"
        tsaate|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 1.

.. _WezTermlangKhn:

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ============================
`U+1A21 <https://codepoints.net/U+1A21>`_  '\\u1a21'  Lo                  1  TAI THAM LETTER HIGH KHA
`U+1A73 <https://codepoints.net/U+1A73>`_  '\\u1a73'  Mn                  0  TAI THAM VOWEL SIGN OA ABOVE
`U+1A76 <https://codepoints.net/U+1A76>`_  '\\u1a76'  Mn                  0  TAI THAM SIGN TONE-2
=========================================  =========  ==========  =========  ============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xa1\xe1\xa9\xb3\xe1\xa9\xb6|\\n1|\\n"
        ᨡᩳ᩶|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -13.

.. _WezTermlangGumuz:

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+A78C <https://codepoints.net/U+A78C>`_  '\\ua78c'  Ll                  1  LATIN SMALL LETTER SALTILLO
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
=========================================  =========  ==========  =========  ===========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kamaab\xea\x9e\x8cushil|\\n123456789012|\\n"
        kamaabꞌushil|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *WezTerm* measures width 6.

.. _WezTermlangShipiboConibo:

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
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jonibaon|\\n12345678|\\n"
        jonibaon|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width -9.

.. _WezTermlangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
`U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x81\xd0\xb0\xcc\x84\xd0\xbc\xd0\xb8.|\\n12345|\\n"
        са̄ми.|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -2.

.. _WezTermlangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'    Ll                  1  LATIN SMALL LETTER O WITH ACUTE
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ===============================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "hw\xc3\xadid\xc3\xb3one\xca\xbc.|\\n12345678901|\\n"
        hwíidóoneʼ.|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *WezTerm* measures width 5.

.. _WezTermlangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0410 <https://codepoints.net/U+0410>`_  '\\u0410'  Lu                  1  CYRILLIC CAPITAL LETTER A
`U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
`U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
`U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
`U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
`U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
`U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
`U+0458 <https://codepoints.net/U+0458>`_  '\\u0458'  Ll                  1  CYRILLIC SMALL LETTER JE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
=========================================  =========  ==========  =========  =========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\x90\xd1\x81\xd1\x81\xd0\xb0\xd0\xbc\xd0\xb1\xd0\xbb\xd0\xb5\xcc\x84\xd1\x98\xd0\xb0|\\n1234567890|\\n"
        Ассамбле̄ја|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *WezTerm* measures width 0.

.. _WezTermlangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
`U+044B <https://codepoints.net/U+044B>`_  '\\u044b'  Ll                  1  CYRILLIC SMALL LETTER YERU
`U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb4\xd1\x8f\xd1\x80\xd0\xb8\xd1\x82\xd1\x8b\xd0\xbd.|\\n12345678|\\n"
        дяритын.|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 4.

.. _WezTermlangAmarakaeri:

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
`U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
`U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
=========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "oknopoe\xcc\xb1'po|\\n1234567890|\\n"
        oknopoe̱'po|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *WezTerm* measures width 6.

.. _WezTermlangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "derechos|\\n12345678|\\n"
        derechos|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 2.

.. _WezTermlangShan:

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
`U+1035 <https://codepoints.net/U+1035>`_  '\\u1035'  Mn                  0  MYANMAR VOWEL SIGN E ABOVE
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
`U+1075 <https://codepoints.net/U+1075>`_  '\\u1075'  Lo                  1  MYANMAR LETTER SHAN KA
`U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+104B <https://codepoints.net/U+104B>`_  '\\u104b'  Po                  1  MYANMAR SIGN SECTION
=========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x95\xe1\x80\xb5\xe1\x80\x84\xe1\x80\xba\xe1\x80\xb8\xe1\x81\xb5\xe1\x81\xbc\xe1\x80\xba\xe1\x81\x8b|\\n12345|\\n"
        ပဵင်းၵၼ်။|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -1.

.. _WezTermlangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===================================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===================================
`U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ===================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xabm\xc3\xabhua'ti|\\n123456789|\\n"
        ëmëhua'ti|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *WezTerm* measures width -4.

.. _WezTermlangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
`U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+043A <https://codepoints.net/U+043A>`_  '\\u043a'  Ll                  1  CYRILLIC SMALL LETTER KA
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+030C <https://codepoints.net/U+030C>`_  '\\u030c'  Mn                  0  COMBINING CARON
=========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x82\xd0\xbe\xd1\x80\xd0\xba\xd0\xb8\xd1\x80\xcc\x8c|\\n123456|\\n"
        торкир̌|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -3.

.. _WezTermlangVeps:

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tegend|\\n123456|\\n"
        tegend|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 3.

.. _WezTermlangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ============================
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0131 <https://codepoints.net/U+0131>`_  '\\u0131'  Ll                  1  LATIN SMALL LETTER DOTLESS I
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
=========================================  =========  ==========  =========  ============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kad\xc4\xb1n|\\n12345|\\n"
        kadın|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -3.

.. _WezTermlangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "de'oye|\\n123456|\\n"
        de'oye|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 2.

.. _WezTermlangTamilSriLanka:

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0BB5 <https://codepoints.net/U+0BB5>`_  '\\u0bb5'  Lo                  1  TAMIL LETTER VA
`U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
`U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
`U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
`U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
`U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
`U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
`U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
`U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
=========================================  =========  ==========  =========  ==================

Total codepoints: 15


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xb5\xe0\xae\xbf\xe0\xae\xb3\xe0\xae\x95\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xae\xe0\xae\xbf\xe0\xae\xb0\xe0\xaf\x81\xe0\xae\xa4\xe0\xaf\x8d\xe0\xae\xa4\xe0\xae\xb2\xe0\xaf\x8d|\\n123456789|\\n"
        விளக்கமிருத்தல்|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *WezTerm* measures width 7.

.. _WezTermlangTamil:

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0B9A <https://codepoints.net/U+0B9A>`_  '\\u0b9a'  Lo                  1  TAMIL LETTER CA
`U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
`U+0BA8 <https://codepoints.net/U+0BA8>`_  '\\u0ba8'  Lo                  1  TAMIL LETTER NA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
`U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
`U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
`U+0B99 <https://codepoints.net/U+0B99>`_  '\\u0b99'  Lo                  1  TAMIL LETTER NGA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
`U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
`U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
`U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
=========================================  =========  ==========  =========  ==================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x9a\xe0\xaf\x81\xe0\xae\xa4\xe0\xae\xa8\xe0\xaf\x8d\xe0\xae\xa4\xe0\xae\xbf\xe0\xae\xb0\xe0\xae\x99\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xb3\xe0\xaf\x8d|\\n12345678|\\n"
        சுதந்திரங்கள்|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 1.

.. _WezTermlangColorado:

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "sele|\\n1234|\\n"
        sele|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -5.

.. _WezTermlangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================
`U+C774 <https://codepoints.net/U+C774>`_  '\\uc774'  Lo                  2  HANGUL SYLLABLE I
=========================================  =========  ==========  =========  =================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x9d\xb4|\\n12|\\n"
        이|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -3.

.. _WezTermlangKannada:

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0C98 <https://codepoints.net/U+0C98>`_  '\\u0c98'  Lo                  1  KANNADA LETTER GHA
`U+0CA8 <https://codepoints.net/U+0CA8>`_  '\\u0ca8'  Lo                  1  KANNADA LETTER NA
`U+0CA4 <https://codepoints.net/U+0CA4>`_  '\\u0ca4'  Lo                  1  KANNADA LETTER TA
`U+0CC6 <https://codepoints.net/U+0CC6>`_  '\\u0cc6'  Mn                  0  KANNADA VOWEL SIGN E
=========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\x98\xe0\xb2\xa8\xe0\xb2\xa4\xe0\xb3\x86|\\n123|\\n"
        ಘನತೆ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 1.

.. _WezTermlangMon:

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
`U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
`U+1036 <https://codepoints.net/U+1036>`_  '\\u1036'  Mn                  0  MYANMAR SIGN ANUSVARA
=========================================  =========  ==========  =========  =====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x80\xe1\x80\xb1\xe1\x80\xaf\xe1\x80\xac\xe1\x80\xb6|\\n1|\\n"
        ကေုာံ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -13.

.. _WezTermlangKorean:

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
  while *WezTerm* measures width -8.

.. _WezTermlangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
`U+028A <https://codepoints.net/U+028A>`_  '\\u028a'  Ll                  1  LATIN SMALL LETTER UPSILON
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+0269 <https://codepoints.net/U+0269>`_  '\\u0269'  Ll                  1  LATIN SMALL LETTER IOTA
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "b\xc9\x94w\xca\x8a\xcc\x81t\xc9\xa9|\\n123456|\\n"
        bɔwʊ́tɩ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -1.

.. _WezTermlangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -8.

.. _WezTermlangBurmese:

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+1011 <https://codepoints.net/U+1011>`_  '\\u1011'  Lo                  1  MYANMAR LETTER THA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+1014 <https://codepoints.net/U+1014>`_  '\\u1014'  Lo                  1  MYANMAR LETTER NA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+1036 <https://codepoints.net/U+1036>`_  '\\u1036'  Mn                  0  MYANMAR SIGN ANUSVARA
`U+1010 <https://codepoints.net/U+1010>`_  '\\u1010'  Lo                  1  MYANMAR LETTER TA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+1037 <https://codepoints.net/U+1037>`_  '\\u1037'  Mn                  0  MYANMAR SIGN DOT BELOW
`U+104F <https://codepoints.net/U+104F>`_  '\\u104f'  Po                  1  MYANMAR SYMBOL GENITIVE
`U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
`U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
`U+100F <https://codepoints.net/U+100F>`_  '\\u100f'  Lo                  1  MYANMAR LETTER NNA
`U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
`U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
`U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
`U+1010 <https://codepoints.net/U+1010>`_  '\\u1010'  Lo                  1  MYANMAR LETTER TA
`U+103D <https://codepoints.net/U+103D>`_  '\\u103d'  Mn                  0  MYANMAR CONSONANT SIGN MEDIAL WA
`U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
`U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
`U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
`U+101B <https://codepoints.net/U+101B>`_  '\\u101b'  Lo                  1  MYANMAR LETTER RA
`U+103E <https://codepoints.net/U+103E>`_  '\\u103e'  Mn                  0  MYANMAR CONSONANT SIGN MEDIAL HA
`U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
=========================================  =========  ==========  =========  ================================

Total codepoints: 33


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x91\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x94\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x84\xe1\x80\xb6\xe1\x80\x90\xe1\x80\xad\xe1\x80\xaf\xe1\x80\xb7\xe1\x81\x8f\xe1\x80\xa1\xe1\x80\xac\xe1\x80\x8f\xe1\x80\xac\xe1\x80\x95\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\xa1\xe1\x80\x90\xe1\x80\xbd\xe1\x80\x84\xe1\x80\xba\xe1\x80\xb8\xe1\x80\x9b\xe1\x80\xbe\xe1\x80\xad|\\n12345678901234|\\n"
        ထိုနိုင်ငံတို့၏အာဏာပိုင်အတွင်းရှိ|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *WezTerm* measures width -2.

.. _WezTermlangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "las|\\n123|\\n"
        las|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 1.

.. _WezTermlangw:

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -2.

.. _WezTermlangSanskritGrantha:

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  =====================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  =====================
`U+00011338 <https://codepoints.net/U+00011338>`_  '\\U00011338'  Lo                  1  GRANTHA LETTER SA
`U+00011341 <https://codepoints.net/U+00011341>`_  '\\U00011341'  Mc                  0  GRANTHA VOWEL SIGN U
`U+00011338 <https://codepoints.net/U+00011338>`_  '\\U00011338'  Lo                  1  GRANTHA LETTER SA
`U+0001132E <https://codepoints.net/U+0001132E>`_  '\\U0001132e'  Lo                  1  GRANTHA LETTER MA
`U+0001134D <https://codepoints.net/U+0001134D>`_  '\\U0001134d'  Mc                  0  GRANTHA SIGN VIRAMA
`U+0001132A <https://codepoints.net/U+0001132A>`_  '\\U0001132a'  Lo                  1  GRANTHA LETTER PA
`U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
`U+0001134D <https://codepoints.net/U+0001134D>`_  '\\U0001134d'  Mc                  0  GRANTHA SIGN VIRAMA
`U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
`U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
`U+00011303 <https://codepoints.net/U+00011303>`_  '\\U00011303'  Mc                  0  GRANTHA SIGN VISARGA
=================================================  =============  ==========  =========  =====================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xb8\xf0\x91\x8d\x81\xf0\x91\x8c\xb8\xf0\x91\x8c\xae\xf0\x91\x8d\x8d\xf0\x91\x8c\xaa\xf0\x91\x8c\xa8\xf0\x91\x8d\x8d\xf0\x91\x8c\xa8\xf0\x91\x8c\xbe\xf0\x91\x8c\x83|\\n123456|\\n"
        𑌸𑍁𑌸𑌮𑍍𑌪𑌨𑍍𑌨𑌾𑌃|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width -7.

.. _WezTermlangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  =========
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  =========
`U+003B <https://codepoints.net/U+003B>`_  ';'       Po                  1  SEMICOLON
=========================================  ========  ==========  =========  =========

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf ";|\\n1|\\n"
        ;|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -7.

.. _WezTermlangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+05DE <https://codepoints.net/U+05DE>`_  '\\u05de'  Lo                  1  HEBREW LETTER MEM
`U+05E7 <https://codepoints.net/U+05E7>`_  '\\u05e7'  Lo                  1  HEBREW LETTER QOF
`U+05D5 <https://codepoints.net/U+05D5>`_  '\\u05d5'  Lo                  1  HEBREW LETTER VAV
`U+05D9 <https://codepoints.net/U+05D9>`_  '\\u05d9'  Lo                  1  HEBREW LETTER YOD
`U+05DD <https://codepoints.net/U+05DD>`_  '\\u05dd'  Lo                  1  HEBREW LETTER FINAL MEM
=========================================  =========  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x9e\xd7\xa7\xd7\x95\xd7\x99\xd7\x9d|\\n12345|\\n"
        מקוים|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 2.

.. _WezTermlangTicuna:

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -5.

.. _WezTermlangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+0263 <https://codepoints.net/U+0263>`_  '\\u0263'  Ll                  1  LATIN SMALL LETTER GAMMA
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+002D <https://codepoints.net/U+002D>`_  '-'        Pd                  1  HYPHEN-MINUS
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
=========================================  =========  ==========  =========  ========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "al\xc9\xa3u-agi|\\n12345678|\\n"
        alɣu-agi|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 3.

.. _WezTermlangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
=========================================  =========  ==========  =========  =========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mol\xc9\x94\xcc\x81ng\xc9\x94\xcc\x81|\\n1234567|\\n"
        molɔ́ngɔ́|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *WezTerm* measures width 5.

.. _WezTermlangTamazightCentralAtlas:

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
  while *WezTerm* measures width -8.

.. _WezTermlangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "sabar|\\n12345|\\n"
        sabar|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -3.

.. _WezTermlangPularAdlam:

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
  while *WezTerm* measures width -2.

.. _WezTermlangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0630 <https://codepoints.net/U+0630>`_  '\\u0630'  Lo                  1  ARABIC LETTER THAL
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
`U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
=========================================  =========  ==========  =========  ==================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xb0\xd8\xa7\xd8\xaa\xd9\x87\xd8\xa7|\\n12345|\\n"
        ذاتها|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -2.

.. _WezTermlangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "takatu'u|\\n12345678|\\n"
        takatu'u|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 1.

.. _WezTermlangMaldivian:

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================
`U+0799 <https://codepoints.net/U+0799>`_  '\\u0799'  Lo                  1  THAANA LETTER HHAA
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
`U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
`U+07A4 <https://codepoints.net/U+07A4>`_  '\\u07a4'  Lo                  1  THAANA LETTER QAAFU
`U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
`U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
`U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
=========================================  =========  ==========  =========  ===================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x99\xde\xa6\xde\x87\xde\xb0\xde\xa4\xde\xaa\xde\x8c\xde\xa6\xde\x87\xde\xb0|\\n12345|\\n"
        ޙައްޤުތައް|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 3.

.. _WezTermlangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
=========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "de\xcc\x81|\\n12|\\n"
        dé|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -8.

.. _WezTermlangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
=========================================  =========  ==========  =========  =========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ac\xc9\x9bkpadu|\\n12345678|\\n"
        acɛkpadu|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *WezTerm* measures width 6.

.. _WezTermlangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0718 <https://codepoints.net/U+0718>`_  '\\u0718'  Lo                  1  SYRIAC LETTER WAW
`U+0720 <https://codepoints.net/U+0720>`_  '\\u0720'  Lo                  1  SYRIAC LETTER LAMADH
`U+072B <https://codepoints.net/U+072B>`_  '\\u072b'  Lo                  1  SYRIAC LETTER SHIN
`U+0722 <https://codepoints.net/U+0722>`_  '\\u0722'  Lo                  1  SYRIAC LETTER NUN
`U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
=========================================  =========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\x98\xdc\xa0\xdc\xab\xdc\xa2\xdc\x90|\\n12345|\\n"
        ܘܠܫܢܐ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 0.

.. _WezTermlangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
=========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "hew\xc9\x94|\\n1234|\\n"
        hewɔ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -2.

.. _WezTermlangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

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
  while *WezTerm* measures width 0.

.. _WezTermlangUduk:

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gi|\\n12|\\n"
        gi|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -4.

.. _WezTermlangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0044 <https://codepoints.net/U+0044>`_  'D'       Lu                  1  LATIN CAPITAL LETTER D
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Dwa|\\n123|\\n"
        Dwa|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width -6.

.. _WezTermlangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tika|\\n1234|\\n"
        tika|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width 0.

.. _WezTermlangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
`U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
=========================================  =========  ==========  =========  ==================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x85\xd9\x84\xd9\x84|\\n123|\\n"
        ملل|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 0.

.. _WezTermlangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kenic|\\n12345|\\n"
        kenic|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 0.

.. _WezTermlangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================================
`U+00E0 <https://codepoints.net/U+00E0>`_  '\\xe0'    Ll                  1  LATIN SMALL LETTER A WITH GRAVE
`U+1E63 <https://codepoints.net/U+1E63>`_  '\\u1e63'  Ll                  1  LATIN SMALL LETTER S WITH DOT BELOW
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
=========================================  =========  ==========  =========  ===================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xa0\xe1\xb9\xa3eyege|\\n1234567|\\n"
        àṣeyege|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *WezTerm* measures width 5.

.. _WezTermlangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
=========================================  =========  ==========  =========  =================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88|\\n1|\\n"
        و|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -2.

.. _WezTermlangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
`U+00E2 <https://codepoints.net/U+00E2>`_  '\\xe2'    Ll                  1  LATIN SMALL LETTER A WITH CIRCUMFLEX
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
=========================================  =========  ==========  =========  ====================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nh\xc3\xa2\xcc\x81t|\\n1234|\\n"
        nhất|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -1.

.. _WezTermlangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0169 <https://codepoints.net/U+0169>`_  '\\u0169'  Ll                  1  LATIN SMALL LETTER U WITH TILDE
=========================================  =========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "y\xc9\x9bm\xc9\x94\xc5\xa9|\\n12345|\\n"
        yɛmɔũ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width -1.

.. _WezTermlangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
=========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc5\x8bmaani|\\n123456|\\n"
        ŋmaani|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 1.

.. _WezTermlangMazahuaCentral:

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
  while *WezTerm* measures width -7.

.. _WezTermlangSererSine:

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
  while *WezTerm* measures width -2.

.. _WezTermlangUrdu:

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
  while *WezTerm* measures width -2.

.. _WezTermlangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+067C <https://codepoints.net/U+067C>`_  '\\u067c'  Lo                  1  ARABIC LETTER TEH WITH RING
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
=========================================  =========  ==========  =========  ===========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\xbc\xd9\x88\xd9\x84|\\n123|\\n"
        ټول|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 1.

.. _WezTermlangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+06C1 <https://codepoints.net/U+06C1>`_  '\\u06c1'  Lo                  1  ARABIC LETTER HEH GOAL
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
`U+06BA <https://codepoints.net/U+06BA>`_  '\\u06ba'  Lo                  1  ARABIC LETTER NOON GHUNNA
=========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdb\x81\xdb\x8c\xda\xba|\\n123|\\n"
        ہیں|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 1.

.. _WezTermlangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "noo|\\n123|\\n"
        noo|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 0.

.. _WezTermlangUrdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -2.

.. _WezTermlangDagaareSouthern:

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -2.

.. _WezTermlangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+00E0 <https://codepoints.net/U+00E0>`_  '\\xe0'   Ll                  1  LATIN SMALL LETTER A WITH GRAVE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "b\xc3\xa0|\\n12|\\n"
        bà|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -3.

.. _WezTermlangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pa|\\n12|\\n"
        pa|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -2.

.. _WezTermlangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
=========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ya\xc5\x8bisi|\\n123456|\\n"
        yaŋisi|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *WezTerm* measures width 2.

.. _WezTermlangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
=========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaf\xdb\x8c|\\n12|\\n"
        دی|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -3.

.. _WezTermlangChinantecChiltepec:

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'   Ll                  1  LATIN SMALL LETTER O WITH ACUTE
=========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ki\xc3\xb3|\\n123|\\n"
        kió|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 0.

.. _WezTermlangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0044 <https://codepoints.net/U+0044>`_  'D'       Lu                  1  LATIN CAPITAL LETTER D
=========================================  ========  ==========  =========  ======================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "D|\\n1|\\n"
        D|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width -5.

.. _WezTermlangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
=========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jij\xc9\x9b|\\n1234|\\n"
        jijɛ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width -6.

.. _WezTermlangChakma:

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ===================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ===================
`U+00011125 <https://codepoints.net/U+00011125>`_  '\\U00011125'  Lo                  1  CHAKMA LETTER SAA
`U+00011127 <https://codepoints.net/U+00011127>`_  '\\U00011127'  Mn                  0  CHAKMA VOWEL SIGN A
`U+0001111F <https://codepoints.net/U+0001111F>`_  '\\U0001111f'  Lo                  1  CHAKMA LETTER MAA
`U+00011134 <https://codepoints.net/U+00011134>`_  '\\U00011134'  Mn                  0  CHAKMA MAAYYAA
`U+0001111B <https://codepoints.net/U+0001111B>`_  '\\U0001111b'  Lo                  1  CHAKMA LETTER PAA
`U+00011127 <https://codepoints.net/U+00011127>`_  '\\U00011127'  Mn                  0  CHAKMA VOWEL SIGN A
`U+00011116 <https://codepoints.net/U+00011116>`_  '\\U00011116'  Lo                  1  CHAKMA LETTER TAA
`U+00011128 <https://codepoints.net/U+00011128>`_  '\\U00011128'  Mn                  0  CHAKMA VOWEL SIGN I
`U+00011128 <https://codepoints.net/U+00011128>`_  '\\U00011128'  Mn                  0  CHAKMA VOWEL SIGN I
=================================================  =============  ==========  =========  ===================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x9f\xf0\x91\x84\xb4\xf0\x91\x84\x9b\xf0\x91\x84\xa7\xf0\x91\x84\x96\xf0\x91\x84\xa8\xf0\x91\x84\xa8|\\n1234|\\n"
        𑄥𑄧𑄟𑄴𑄛𑄧𑄖𑄨𑄨|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *WezTerm* measures width 0.

.. _WezTermlangJavaneseJavanese:

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+A98F <https://codepoints.net/U+A98F>`_  '\\ua98f'  Lo                  1  JAVANESE LETTER KA
`U+A981 <https://codepoints.net/U+A981>`_  '\\ua981'  Mn                  0  JAVANESE SIGN CECAK
`U+A992 <https://codepoints.net/U+A992>`_  '\\ua992'  Lo                  1  JAVANESE LETTER GA
`U+A9BA <https://codepoints.net/U+A9BA>`_  '\\ua9ba'  Mc                  0  JAVANESE VOWEL SIGN TALING
`U+A9B4 <https://codepoints.net/U+A9B4>`_  '\\ua9b4'  Mc                  0  JAVANESE VOWEL SIGN TARUNG
`U+A98F <https://codepoints.net/U+A98F>`_  '\\ua98f'  Lo                  1  JAVANESE LETTER KA
`U+A9B1 <https://codepoints.net/U+A9B1>`_  '\\ua9b1'  Lo                  1  JAVANESE LETTER SA
`U+A9B6 <https://codepoints.net/U+A9B6>`_  '\\ua9b6'  Mn                  0  JAVANESE VOWEL SIGN WULU
`U+A9AD <https://codepoints.net/U+A9AD>`_  '\\ua9ad'  Lo                  1  JAVANESE LETTER LA
=========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\x8f\xea\xa6\x81\xea\xa6\x92\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x8f\xea\xa6\xb1\xea\xa6\xb6\xea\xa6\xad|\\n12345|\\n"
        ꦏꦁꦒꦺꦴꦏꦱꦶꦭ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 2.

.. _WezTermlangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ma'mu|\\n12345|\\n"
        ma'mu|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 2.

.. _WezTermlangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

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
  while *WezTerm* measures width -5.

.. _WezTermlangDangme:

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pe|\\n12|\\n"
        pe|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -1.

.. _WezTermlangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0F5A <https://codepoints.net/U+0F5A>`_  '\\u0f5a'  Lo                  1  TIBETAN LETTER TSHA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
=========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x9a\xe0\xbd\xb4\xe0\xbd\xa3|\\n12|\\n"
        ཚུལ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *WezTerm* measures width -1.

.. _WezTermlangPanjabiEastern:

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0A10 <https://codepoints.net/U+0A10>`_  '\\u0a10'  Lo                  1  GURMUKHI LETTER AI
`U+0A32 <https://codepoints.net/U+0A32>`_  '\\u0a32'  Lo                  1  GURMUKHI LETTER LA
`U+0A3E <https://codepoints.net/U+0A3E>`_  '\\u0a3e'  Mc                  0  GURMUKHI VOWEL SIGN AA
`U+0A28 <https://codepoints.net/U+0A28>`_  '\\u0a28'  Lo                  1  GURMUKHI LETTER NA
`U+0A28 <https://codepoints.net/U+0A28>`_  '\\u0a28'  Lo                  1  GURMUKHI LETTER NA
`U+0A3E <https://codepoints.net/U+0A3E>`_  '\\u0a3e'  Mc                  0  GURMUKHI VOWEL SIGN AA
`U+0A2E <https://codepoints.net/U+0A2E>`_  '\\u0a2e'  Lo                  1  GURMUKHI LETTER MA
`U+0A47 <https://codepoints.net/U+0A47>`_  '\\u0a47'  Mn                  0  GURMUKHI VOWEL SIGN EE
=========================================  =========  ==========  =========  ======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\x90\xe0\xa8\xb2\xe0\xa8\xbe\xe0\xa8\xa8\xe0\xa8\xa8\xe0\xa8\xbe\xe0\xa8\xae\xe0\xa9\x87|\\n12345|\\n"
        ਐਲਾਨਨਾਮੇ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *WezTerm* measures width 3.

.. _WezTermlangTaiDam:

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+AAB9 <https://codepoints.net/U+AAB9>`_  '\\uaab9'  Lo                  1  TAI VIET VOWEL UEA
`U+AA9C <https://codepoints.net/U+AA9C>`_  '\\uaa9c'  Lo                  1  TAI VIET LETTER LOW PO
`U+AAB8 <https://codepoints.net/U+AAB8>`_  '\\uaab8'  Mn                  0  TAI VIET VOWEL IA
`U+AA99 <https://codepoints.net/U+AA99>`_  '\\uaa99'  Lo                  1  TAI VIET LETTER HIGH NO
=========================================  =========  ==========  =========  =======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xb9\xea\xaa\x9c\xea\xaa\xb8\xea\xaa\x99|\\n123|\\n"
        ꪹꪜꪸꪙ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *WezTerm* measures width 0.

.. _WezTermlangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0F58 <https://codepoints.net/U+0F58>`_  '\\u0f58'  Lo                  1  TIBETAN LETTER MA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
=========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x98\xe0\xbd\xb2|\\n1|\\n"
        མི|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *WezTerm* measures width 0.

.. _WezTermdecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

DEC private modes results for *WezTerm*: 23 supported modes
out of 157 total modes tested (14.6% support).

Complete list of DEC private modes tested:

.. _WezTermdecmode1:

.. _WezTermdecmode2:

.. _WezTermdecmode3:

.. _WezTermdecmode6:

.. _WezTermdecmode7:

.. _WezTermdecmode12:

.. _WezTermdecmode25:

.. _WezTermdecmode45:

.. _WezTermdecmode69:

.. _WezTermdecmode80:

.. _WezTermdecmode1000:

.. _WezTermdecmode1002:

.. _WezTermdecmode1003:

.. _WezTermdecmode1004:

.. _WezTermdecmode1005:

.. _WezTermdecmode1006:

.. _WezTermdecmode1016:

.. _WezTermdecmode1070:

.. _WezTermdecmode2004:

.. _WezTermdecmode2026:

.. _WezTermdecmode2027:

.. _WezTermdecmode8452:

.. _WezTermdecmode9001:

==============  =============================  =======================================================================  ===========  ============
Mode            Name                           Description                                                              Supported    Changeable
==============  =============================  =======================================================================  ===========  ============
DEC Mode 1      DECCKM                         Cursor Keys Mode                                                         Yes          Yes
DEC Mode 2      DECANM                         ANSI/VT52 Mode                                                           Yes          Yes
DEC Mode 3      DECCOLM                        Column Mode                                                              Yes          Yes
DEC Mode 4      DECSCLM                        Scrolling Mode                                                           No           No
DEC Mode 5      DECSCNM                        Screen Mode (light or dark screen)                                       No           No
DEC Mode 6      DECOM                          Origin Mode                                                              Yes          Yes
DEC Mode 7      DECAWM                         Auto Wrap Mode                                                           Yes          Yes
DEC Mode 8      DECARM                         Auto Repeat Mode                                                         No           No
DEC Mode 9      DECINLM                        Interlace Mode / Mouse X10 tracking                                      No           No
DEC Mode 10     DECEDM                         Editing Mode / Show toolbar (rxvt)                                       No           No
DEC Mode 11     DECLTM                         Line Transmit Mode                                                       No           No
DEC Mode 12     DECKANAM                       Katakana Shift Mode / Blinking cursor (xterm)                            Yes          Yes
DEC Mode 13     DECSCFDM                       Space Compression/Field Delimiter Mode / Start blinking cursor (xterm)   No           No
DEC Mode 14     DECTEM                         Transmit Execution Mode / Enable XOR of blinking cursor control (xterm)  No           No
DEC Mode 16     DECEKEM                        Edit Key Execution Mode                                                  No           No
DEC Mode 18     DECPFF                         Print Form Feed                                                          No           No
DEC Mode 19     DECPEX                         Printer Extent                                                           No           No
DEC Mode 20     OV1                            Overstrike                                                               No           No
DEC Mode 21     BA1                            Local BASIC                                                              No           No
DEC Mode 22     BA2                            Host BASIC                                                               No           No
DEC Mode 23     PK1                            Programmable Keypad                                                      No           No
DEC Mode 24     AH1                            Auto Hardcopy                                                            No           No
DEC Mode 25     DECTCEM                        Text Cursor Enable Mode                                                  Yes          Yes
DEC Mode 27     DECPSP                         Proportional Spacing                                                     No           No
DEC Mode 29     DECPSM                         Pitch Select Mode                                                        No           No
DEC Mode 30     SHOW_SCROLLBAR_RXVT            Show scrollbar (rxvt)                                                    No           No
DEC Mode 34     DECRLM                         Cursor Right to Left Mode                                                No           No
DEC Mode 35     DECHEBM                        Hebrew (Keyboard) Mode / Enable font-shifting functions (rxvt)           No           No
DEC Mode 36     DECHEM                         Hebrew Encoding Mode                                                     No           No
DEC Mode 38     DECTEK                         Tektronix 4010/4014 Mode                                                 No           No
DEC Mode 40     DECCRNLM                       Carriage Return/New Line Mode / Allow 80⇒132 mode (xterm)                No           No
DEC Mode 41     DECUPM                         Unidirectional Print Mode / more(1) fix (xterm)                          No           No
DEC Mode 42     DECNRCM                        National Replacement Character Set Mode                                  No           No
DEC Mode 43     DECGEPM                        Graphics Expanded Print Mode                                             No           No
DEC Mode 44     DECGPCM                        Graphics Print Color Mode / Turn on margin bell (xterm)                  No           No
DEC Mode 45     DECGPCS                        Graphics Print Color Syntax / Reverse-wraparound mode (xterm)            Yes          Yes
DEC Mode 46     DECGPBM                        Graphics Print Background Mode / Start logging (xterm)                   No           No
DEC Mode 47     DECGRPM                        Graphics Rotated Print Mode / Use Alternate Screen Buffer (xterm)        No           No
DEC Mode 49     DECTHAIM                       Thai Input Mode                                                          No           No
DEC Mode 50     DECTHAICM                      Thai Cursor Mode                                                         No           No
DEC Mode 51     DECBWRM                        Black/White Reversal Mode                                                No           No
DEC Mode 52     DECOPM                         Origin Placement Mode                                                    No           No
DEC Mode 53     DEC131TM                       VT131 Transmit Mode                                                      No           No
DEC Mode 55     DECBPM                         Bold Page Mode                                                           No           No
DEC Mode 57     DECNAKB                        Greek/N-A Keyboard Mapping Mode                                          No           No
DEC Mode 58     DECIPEM                        Enter IBM Proprinter Emulation Mode                                      No           No
DEC Mode 59     DECKKDM                        Kanji/Katakana Display Mode                                              No           No
DEC Mode 60     DECHCCM                        Horizontal Cursor Coupling                                               No           No
DEC Mode 61     DECVCCM                        Vertical Cursor Coupling Mode                                            No           No
DEC Mode 64     DECPCCM                        Page Cursor Coupling Mode                                                No           No
DEC Mode 65     DECBCMM                        Business Color Matching Mode                                             No           No
DEC Mode 66     DECNKM                         Numeric Keypad Mode                                                      No           No
DEC Mode 67     DECBKM                         Backarrow Key Mode                                                       No           No
DEC Mode 68     DECKBUM                        Keyboard Usage Mode                                                      No           No
DEC Mode 69     DECVSSM                        Vertical Split Screen Mode / DECLRMM - Left Right Margin Mode            Yes          Yes
DEC Mode 70     DECFPM                         Force Plot Mode                                                          No           No
DEC Mode 73     DECXRLM                        Transmission Rate Limiting                                               No           No
DEC Mode 80     DECSDM                         Sixel Display Mode                                                       Yes          Yes
DEC Mode 81     DECKPM                         Key Position Mode                                                        No           No
DEC Mode 83     WY_52_LINE                     52 line mode (WY-370)                                                    No           No
DEC Mode 84     WYENAT_OFF                     Erasable/nonerasable WYENAT Off attribute select (WY-370)                No           No
DEC Mode 85     REPLACEMENT_CHAR_COLOR         Replacement character color (WY-370)                                     No           No
DEC Mode 90     DECTHAISCM                     Thai Space Compensating Mode                                             No           No
DEC Mode 95     DECNCSM                        No Clearing Screen on Column Change Mode                                 No           No
DEC Mode 96     DECRLCM                        Right to Left Copy Mode                                                  No           No
DEC Mode 97     DECCRTSM                       CRT Save Mode                                                            No           No
DEC Mode 98     DECARSM                        Auto Resize Mode                                                         No           No
DEC Mode 99     DECMCM                         Modem Control Mode                                                       No           No
DEC Mode 100    DECAAM                         Auto Answerback Mode                                                     No           No
DEC Mode 101    DECCANSM                       Conceal Answerback Message Mode                                          No           No
DEC Mode 102    DECNULM                        Ignore Null Mode                                                         No           No
DEC Mode 103    DECHDPXM                       Half Duplex Mode                                                         No           No
DEC Mode 104    DECESKM                        Secondary Keyboard Language Mode                                         No           No
DEC Mode 106    DECOSCNM                       Overscan Mode                                                            No           No
DEC Mode 108    DECNUMLK                       NumLock Mode                                                             No           No
DEC Mode 109    DECCAPSLK                      Caps Lock Mode                                                           No           No
DEC Mode 110    DECKLHIM                       Keyboard LEDs Host Indicator Mode                                        No           No
DEC Mode 111    DECFWM                         Framed Windows Mode                                                      No           No
DEC Mode 112    DECRPL                         Review Previous Lines Mode                                               No           No
DEC Mode 113    DECHWUM                        Host Wake-Up Mode                                                        No           No
DEC Mode 114    DECATCUM                       Alternate Text Color Underline Mode                                      No           No
DEC Mode 115    DECATCBM                       Alternate Text Color Blink Mode                                          No           No
DEC Mode 116    DECBBSM                        Bold and Blink Style Mode                                                No           No
DEC Mode 117    DECECM                         Erase Color Mode                                                         No           No
DEC Mode 1000   MOUSE_REPORT_CLICK             Send Mouse X & Y on button press                                         Yes          Yes
DEC Mode 1001   MOUSE_HILITE_TRACKING          Use Hilite Mouse Tracking                                                No           No
DEC Mode 1002   MOUSE_REPORT_DRAG              Use Cell Motion Mouse Tracking                                           Yes          Yes
DEC Mode 1003   MOUSE_ALL_MOTION               Use All Motion Mouse Tracking                                            Yes          Yes
DEC Mode 1004   FOCUS_IN_OUT_EVENTS            Send FocusIn/FocusOut events                                             Yes          Yes
DEC Mode 1005   MOUSE_EXTENDED_UTF8            Enable UTF-8 Mouse Mode                                                  Yes          Yes
DEC Mode 1006   MOUSE_EXTENDED_SGR             Enable SGR Mouse Mode                                                    Yes          Yes
DEC Mode 1007   ALT_SCROLL_XTERM               Enable Alternate Scroll Mode                                             No           No
DEC Mode 1010   SCROLL_ON_TTY_OUTPUT_RXVT      Scroll to bottom on tty output                                           No           No
DEC Mode 1011   SCROLL_ON_KEYPRESS_RXVT        Scroll to bottom on key press                                            No           No
DEC Mode 1014   FAST_SCROLL                    Enable fastScroll resource                                               No           No
DEC Mode 1015   MOUSE_URXVT                    Enable urxvt Mouse Mode                                                  No           No
DEC Mode 1016   MOUSE_SGR_PIXELS               Enable SGR Mouse PixelMode                                               Yes          Yes
DEC Mode 1021   BOLD_ITALIC_HIGH_INTENSITY     Bold/italic implies high intensity                                       No           No
DEC Mode 1034   META_SETS_EIGHTH_BIT           Interpret "meta" key                                                     No           No
DEC Mode 1035   MODIFIERS_ALT_NUMLOCK          Enable special modifiers for Alt and NumLock keys                        No           No
DEC Mode 1036   META_SENDS_ESC                 Send ESC when Meta modifies a key                                        No           No
DEC Mode 1037   KP_DELETE_SENDS_DEL            Send DEL from the editing-keypad Delete key                              No           No
DEC Mode 1039   ALT_SENDS_ESC                  Send ESC when Alt modifies a key                                         No           No
DEC Mode 1040   KEEP_SELECTION_NO_HILITE       Keep selection even if not highlighted                                   No           No
DEC Mode 1041   USE_CLIPBOARD_SELECTION        Use the CLIPBOARD selection                                              No           No
DEC Mode 1042   URGENCY_ON_CTRL_G              Enable Urgency window manager hint when Control-G is received            No           No
DEC Mode 1043   RAISE_ON_CTRL_G                Enable raising of the window when Control-G is received                  No           No
DEC Mode 1044   REUSE_CLIPBOARD_DATA           Reuse the most recent data copied to CLIPBOARD                           No           No
DEC Mode 1045   EXTENDED_REVERSE_WRAPAROUND    Extended Reverse-wraparound mode (XTREVWRAP2)                            No           No
DEC Mode 1046   ALT_SCREEN_BUFFER_SWITCH       Enable switching to/from Alternate Screen Buffer                         No           No
DEC Mode 1047   ALT_SCREEN_BUFFER_XTERM        Use Alternate Screen Buffer                                              No           No
DEC Mode 1048   SAVE_CURSOR_DECSC              Save cursor as in DECSC                                                  No           No
DEC Mode 1049   ALT_SCREEN_AND_SAVE_CLEAR      Save cursor as in DECSC and use alternate screen buffer                  No           No
DEC Mode 1050   TERMINFO_FUNC_KEY_MODE         Set terminfo/termcap function-key mode                                   No           No
DEC Mode 1051   SUN_FUNC_KEY_MODE              Set Sun function-key mode                                                No           No
DEC Mode 1052   HP_FUNC_KEY_MODE               Set HP function-key mode                                                 No           No
DEC Mode 1053   SCO_FUNC_KEY_MODE              Set SCO function-key mode                                                No           No
DEC Mode 1060   LEGACY_KBD_X11R6               Set legacy keyboard emulation, i.e, X11R6                                No           No
DEC Mode 1061   VT220_KBD_EMULATION            Set VT220 keyboard emulation                                             No           No
DEC Mode 1070   SIXEL_PRIVATE_PALETTE          Use private color registers for each graphic                             Yes          Yes
DEC Mode 1243   BIDI_ARROW_KEY_SWAPPING        Arrow keys swapping (BiDi)                                               No           No
DEC Mode 1337   ITERM2_REPORT_KEY_UP           Report Key Up                                                            No           No
DEC Mode 2001   READLINE_MOUSE_BUTTON_1        Enable readline mouse button-1                                           No           No
DEC Mode 2002   READLINE_MOUSE_BUTTON_2        Enable readline mouse button-2                                           No           No
DEC Mode 2003   READLINE_MOUSE_BUTTON_3        Enable readline mouse button-3                                           No           No
DEC Mode 2004   BRACKETED_PASTE                Set bracketed paste mode                                                 Yes          Yes
DEC Mode 2005   READLINE_CHARACTER_QUOTING     Enable readline character-quoting                                        No           No
DEC Mode 2006   READLINE_NEWLINE_PASTING       Enable readline newline pasting                                          No           No
DEC Mode 2026   SYNCHRONIZED_OUTPUT            Synchronized Output                                                      Yes          Yes
DEC Mode 2027   GRAPHEME_CLUSTERING            Grapheme Clustering                                                      Yes          No
DEC Mode 2028   TEXT_REFLOW                    Text reflow                                                              No           No
DEC Mode 2029   PASSIVE_MOUSE_TRACKING         Passive Mouse Tracking                                                   No           No
DEC Mode 2030   REPORT_GRID_CELL_SELECTION     Report grid cell selection                                               No           No
DEC Mode 2031   COLOR_PALETTE_UPDATES          Color palette updates                                                    No           No
DEC Mode 2048   IN_BAND_WINDOW_RESIZE          In-Band Window Resize Notifications                                      No           No
DEC Mode 2500   MIRROR_BOX_DRAWING             Mirror box drawing characters                                            No           No
DEC Mode 2501   BIDI_AUTODETECTION             BiDi autodetection                                                       No           No
DEC Mode 7700   AMBIGUOUS_WIDTH_REPORTING      Ambiguous width reporting                                                No           No
DEC Mode 7711   SCROLL_MARKERS                 Scroll markers (prompt start)                                            No           No
DEC Mode 7723   REWRAP_ON_RESIZE_MINTTY        Rewrap on resize                                                         No           No
DEC Mode 7727   APPLICATION_ESCAPE_KEY         Application escape key mode                                              No           No
DEC Mode 7728   ESC_KEY_SENDS_BACKSLASH        Send ^\ instead of the standard ^[ for the ESC key                       No           No
DEC Mode 7730   GRAPHICS_POSITION              Graphics position                                                        No           No
DEC Mode 7765   ALT_MODIFIED_MOUSEWHEEL        Alt-modified mousewheel mode                                             No           No
DEC Mode 7766   SHOW_HIDE_SCROLLBAR            Show/hide scrollbar                                                      No           No
DEC Mode 7767   FONT_CHANGE_REPORTING          Font change reporting                                                    No           No
DEC Mode 7780   GRAPHICS_POSITION_2            Graphics position                                                        No           No
DEC Mode 7783   SHORTCUT_KEY_MODE              Shortcut key mode                                                        No           No
DEC Mode 7786   MOUSEWHEEL_REPORTING           Mousewheel reporting                                                     No           No
DEC Mode 7787   APPLICATION_MOUSEWHEEL         Application mousewheel mode                                              No           No
DEC Mode 7796   BIDI_CURRENT_LINE              BiDi on current line                                                     No           No
DEC Mode 8200   TTCTH                          Terminal-to-Computer Talk-back Handler                                   No           No
DEC Mode 8452   SIXEL_SCROLLING_LEAVES_CURSOR  Sixel scrolling leaves cursor to right of graphic                        Yes          Yes
DEC Mode 8800   CHARACTER_MAPPING_SERVICE      enable/disable character mapping service                                 No           No
DEC Mode 8840   AMBIGUOUS_WIDTH_DOUBLE_WIDTH   Treat ambiguous width characters as double-width                         No           No
DEC Mode 9001   WIN32_INPUT_MODE               win32-input-mode                                                         Yes          Yes
DEC Mode 19997  KITTY_HANDLE_CTRL_C_Z          Handle Ctrl-C/Ctrl-Z mode                                                No           No
==============  =============================  =======================================================================  ===========  ============

**Summary**: 23 supported, 134 unsupported.

.. _WezTermtime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **465.48 seconds** (465s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
