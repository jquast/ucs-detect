.. _GnomeTerminal:

Gnome Terminal
--------------


Tested Software version 3.52.0(VTE/7600) on Linux
Full results available at ucs-detect_ repository path
`data/linux-gnome-terminal-3.52.0.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-gnome-terminal-3.52.0.yaml>`_

.. _GnomeTerminalscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *Gnome Terminal*:

============  ===========  ==============  ======================================================
Score Type    Raw Score    Scaled Score    Calculation
============  ===========  ==============  ======================================================
WIDE          72.73%       59.2%           (version_index / total_versions) × (pct_success / 100)
ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
LANG          1.68%        2.1%            languages_supported / total_languages
VS16          0.00%        0.0%            pct_success / 100
VS15          0.00%        0.0%            pct_success / 100
DEC Modes     81.53%       79.4%           modes_supported / total_modes
TIME          2845.60s     24.6%           1 - ((elapsed - min) / (max - min)) [inverse]
============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 25.99%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 31.6%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _GnomeTerminalwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Gnome Terminal appears to be 
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
  while *Gnome Terminal* measures width 1.

.. _GnomeTerminalzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Gnome Terminal* appears to be 
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
  while *Gnome Terminal* measures width 9.

.. _GnomeTerminalvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Gnome Terminal* is 213 errors
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
  while *Gnome Terminal* measures width 1.


.. _GnomeTerminalvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *Gnome Terminal* are not available.

.. _GnomeTerminallang:

Language Support
++++++++++++++++

The following 2 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog).

The following 117 languages are not fully supported:

====================================================================================  ==========  =========  =============
lang                                                                                    n_errors    n_total  pct_success
====================================================================================  ==========  =========  =============
:ref:`Shan <GnomeTerminallangShan>`                                                          869        915  5.0%
:ref:`Tamil (Sri Lanka) <GnomeTerminallangTamilSriLanka>`                                   1000       1074  6.9%
:ref:`Tamil <GnomeTerminallangTamil>`                                                       1000       1075  7.0%
:ref:`Sanskrit (Grantha) <GnomeTerminallangSanskritGrantha>`                                 894       1006  11.1%
:ref:`Javanese (Javanese) <GnomeTerminallangJavaneseJavanese>`                              1000       1133  11.7%
:ref:`Malayalam <GnomeTerminallangMalayalam>`                                               1000       1154  13.3%
:ref:`Bengali <GnomeTerminallangBengali>`                                                   1000       1166  14.2%
:ref:`Khmer, Central <GnomeTerminallangKhmerCentral>`                                        448        528  15.2%
:ref:`Kannada <GnomeTerminallangKannada>`                                                    902       1080  16.5%
:ref:`Khün <GnomeTerminallangKhn>`                                                           361        442  18.3%
:ref:`Burmese <GnomeTerminallangBurmese>`                                                    975       1223  20.3%
:ref:`Sanskrit <GnomeTerminallangSanskrit>`                                                  756       1000  24.4%
:ref:`Tamang, Eastern <GnomeTerminallangTamangEastern>`                                       33         45  26.7%
:ref:`Mon <GnomeTerminallangMon>`                                                            677        946  28.4%
:ref:`Marathi <GnomeTerminallangMarathi>`                                                   1000       1421  29.6%
:ref:`Nepali <GnomeTerminallangNepali>`                                                      931       1385  32.8%
:ref:`Gujarati <GnomeTerminallangGujarati>`                                                 1000       1520  34.2%
:ref:`Telugu <GnomeTerminallangTelugu>`                                                      716       1129  36.6%
:ref:`Maithili <GnomeTerminallangMaithili>`                                                  953       1519  37.3%
:ref:`Hindi <GnomeTerminallangHindi>`                                                       1000       1631  38.7%
:ref:`Panjabi, Eastern <GnomeTerminallangPanjabiEastern>`                                   1000       1829  45.3%
:ref:`Sinhala <GnomeTerminallangSinhala>`                                                    887       1655  46.4%
:ref:`Bhojpuri <GnomeTerminallangBhojpuri>`                                                  880       1737  49.3%
:ref:`Magahi <GnomeTerminallangMagahi>`                                                      812       1716  52.7%
:ref:`Chakma <GnomeTerminallangChakma>`                                                      493       1444  65.9%
:ref:`Tibetan, Central <GnomeTerminallangTibetanCentral>`                                      5        279  98.2%
:ref:`Chinese, Mandarin (Harbin) <GnomeTerminallangChineseMandarinHarbin>`                     3        210  98.6%
:ref:`Chinese, Yue <GnomeTerminallangChineseYue>`                                              3        210  98.6%
:ref:`Chinese, Gan <GnomeTerminallangChineseGan>`                                              3        211  98.6%
:ref:`Chinese, Wu <GnomeTerminallangChineseWu>`                                                3        211  98.6%
:ref:`Chinese, Hakka <GnomeTerminallangChineseHakka>`                                          3        212  98.6%
:ref:`Chinese, Mandarin (Beijing) <GnomeTerminallangChineseMandarinBeijing>`                   3        212  98.6%
:ref:`Chinese, Mandarin (Tianjin) <GnomeTerminallangChineseMandarinTianjin>`                   3        212  98.6%
:ref:`Chinese, Xiang <GnomeTerminallangChineseXiang>`                                          3        212  98.6%
:ref:`Dzongkha <GnomeTerminallangDzongkha>`                                                    5        359  98.6%
:ref:`Japanese <GnomeTerminallangJapanese>`                                                    4        299  98.7%
:ref:`Chinese, Mandarin (Simplified) <GnomeTerminallangChineseMandarinSimplified>`             3        225  98.7%
:ref:`Nuosu <GnomeTerminallangNuosu>`                                                          3        230  98.7%
:ref:`Japanese (Osaka) <GnomeTerminallangJapaneseOsaka>`                                       4        308  98.7%
:ref:`Japanese (Tokyo) <GnomeTerminallangJapaneseTokyo>`                                       4        320  98.8%
:ref:`Thai <GnomeTerminallangThai>`                                                            4        341  98.8%
:ref:`Vietnamese (Han nom) <GnomeTerminallangVietnameseHannom>`                                2        199  99.0%
:ref:`Thai (2) <GnomeTerminallangThai2>`                                                       3        313  99.0%
:ref:`Chinese, Mandarin (Traditional) <GnomeTerminallangChineseMandarinTraditional>`           2        210  99.0%
:ref:`(Jinan) <GnomeTerminallangJinan>`                                                        2        211  99.1%
:ref:`Chinese, Mandarin (Guiyang) <GnomeTerminallangChineseMandarinGuiyang>`                   2        211  99.1%
:ref:`Chinese, Jinyu <GnomeTerminallangChineseJinyu>`                                          2        212  99.1%
:ref:`Chinese, Mandarin (Nanjing) <GnomeTerminallangChineseMandarinNanjing>`                   2        212  99.1%
:ref:`Chinese, Min Nan <GnomeTerminallangChineseMinNan>`                                       2        212  99.1%
:ref:`Lao <GnomeTerminallangLao>`                                                              3        426  99.3%
:ref:`Bora <GnomeTerminallangBora>`                                                            7       1598  99.6%
:ref:`Orok <GnomeTerminallangOrok>`                                                            5       1245  99.6%
:ref:`Shipibo-Conibo <GnomeTerminallangShipiboConibo>`                                        10       2540  99.6%
:ref:`Gumuz <GnomeTerminallangGumuz>`                                                          5       1283  99.6%
:ref:`Navajo <GnomeTerminallangNavajo>`                                                        6       1600  99.6%
:ref:`Chickasaw <GnomeTerminallangChickasaw>`                                                  2        554  99.6%
:ref:`South Azerbaijani <GnomeTerminallangSouthAzerbaijani>`                                   5       1396  99.6%
:ref:`Yaneshaʼ <GnomeTerminallangYanesha>`                                                     9       2536  99.6%
:ref:`Amarakaeri <GnomeTerminallangAmarakaeri>`                                                5       1446  99.7%
:ref:`Siona <GnomeTerminallangSiona>`                                                          5       1492  99.7%
:ref:`Evenki <GnomeTerminallangEvenki>`                                                        3        899  99.7%
:ref:`Gilyak <GnomeTerminallangGilyak>`                                                        5       1504  99.7%
:ref:`Nanai <GnomeTerminallangNanai>`                                                          4       1207  99.7%
:ref:`Colorado <GnomeTerminallangColorado>`                                                    4       1263  99.7%
:ref:`Veps <GnomeTerminallangVeps>`                                                            4       1323  99.7%
:ref:`Secoya <GnomeTerminallangSecoya>`                                                        4       1409  99.7%
:ref:`(Yeonbyeon) <GnomeTerminallangYeonbyeon>`                                                3       1061  99.7%
:ref:`Yiddish, Eastern <GnomeTerminallangYiddishEastern>`                                      5       1775  99.7%
:ref:`Kabyle <GnomeTerminallangKabyle>`                                                        5       1815  99.7%
:ref:`Catalan (2) <GnomeTerminallangCatalan2>`                                                 5       1909  99.7%
:ref:`Maldivian <GnomeTerminallangMaldivian>`                                                  5       1918  99.7%
:ref:`Assyrian Neo-Aramaic <GnomeTerminallangAssyrianNeoAramaic>`                              3       1160  99.7%
:ref:`Mirandese <GnomeTerminallangMirandese>`                                                  5       1966  99.7%
:ref:`Korean <GnomeTerminallangKorean>`                                                        3       1185  99.7%
:ref:`Pular (Adlam) <GnomeTerminallangPularAdlam>`                                             4       1613  99.8%
:ref:`Picard <GnomeTerminallangPicard>`                                                        5       2024  99.8%
:ref:`Ticuna <GnomeTerminallangTicuna>`                                                        5       2048  99.8%
:ref:`Tem <GnomeTerminallangTem>`                                                              4       1659  99.8%
:ref:`Saint Lucian Creole French <GnomeTerminallangSaintLucianCreoleFrench>`                   4       1777  99.8%
:ref:`Éwé <GnomeTerminallangw>`                                                                5       2230  99.8%
:ref:`Arabic, Standard <GnomeTerminallangArabicStandard>`                                      3       1348  99.8%
:ref:`Lingala (tones) <GnomeTerminallangLingalatones>`                                         4       1818  99.8%
:ref:`Farsi, Western <GnomeTerminallangFarsiWestern>`                                          4       1822  99.8%
:ref:`Tamazight, Central Atlas <GnomeTerminallangTamazightCentralAtlas>`                       4       1822  99.8%
:ref:`Mixtec, Metlatónoc <GnomeTerminallangMixtecMetlatnoc>`                                   3       1367  99.8%
:ref:`Bamun <GnomeTerminallangBamun>`                                                          5       2285  99.8%
:ref:`Fur <GnomeTerminallangFur>`                                                              4       1838  99.8%
:ref:`Gen <GnomeTerminallangGen>`                                                              5       2309  99.8%
:ref:`Uduk <GnomeTerminallangUduk>`                                                            7       3247  99.8%
:ref:`Dari <GnomeTerminallangDari>`                                                            4       1872  99.8%
:ref:`Ditammari <GnomeTerminallangDitammari>`                                                  4       1882  99.8%
:ref:`Maori (2) <GnomeTerminallangMaori2>`                                                     5       2385  99.8%
:ref:`French (Welche) <GnomeTerminallangFrenchWelche>`                                         4       1928  99.8%
:ref:`Panjabi, Western <GnomeTerminallangPanjabiWestern>`                                      5       2419  99.8%
:ref:`Baatonum <GnomeTerminallangBaatonum>`                                                    4       1939  99.8%
:ref:`Mòoré <GnomeTerminallangMor>`                                                            5       2447  99.8%
:ref:`Yoruba <GnomeTerminallangYoruba>`                                                        5       2454  99.8%
:ref:`Waama <GnomeTerminallangWaama>`                                                          2       1000  99.8%
:ref:`Vietnamese <GnomeTerminallangVietnamese>`                                                5       2502  99.8%
:ref:`Dinka, Northeastern <GnomeTerminallangDinkaNortheastern>`                                3       1529  99.8%
:ref:`Ga <GnomeTerminallangGa>`                                                                4       2039  99.8%
:ref:`Aja <GnomeTerminallangAja>`                                                              4       2061  99.8%
:ref:`Dagaare, Southern <GnomeTerminallangDagaareSouthern>`                                    5       2582  99.8%
:ref:`Dendi <GnomeTerminallangDendi>`                                                          3       1569  99.8%
:ref:`Mazahua Central <GnomeTerminallangMazahuaCentral>`                                       3       1574  99.8%
:ref:`Serer-Sine <GnomeTerminallangSererSine>`                                                 3       1596  99.8%
:ref:`Lamnso' <GnomeTerminallangLamnso>`                                                       4       2237  99.8%
:ref:`Urdu <GnomeTerminallangUrdu>`                                                            4       2237  99.8%
:ref:`Pashto, Northern <GnomeTerminallangPashtoNorthern>`                                      4       2242  99.8%
:ref:`Seraiki <GnomeTerminallangSeraiki>`                                                      4       2242  99.8%
:ref:`Belanda Viri <GnomeTerminallangBelandaViri>`                                             4       2246  99.8%
:ref:`Urdu (2) <GnomeTerminallangUrdu2>`                                                       4       2251  99.8%
:ref:`Chinantec, Chiltepec <GnomeTerminallangChinantecChiltepec>`                              3       1729  99.8%
:ref:`Dangme <GnomeTerminallangDangme>`                                                        5       2912  99.8%
:ref:`Otomi, Mezquital <GnomeTerminallangOtomiMezquital>`                                      3       1849  99.8%
:ref:`Fon <GnomeTerminallangFon>`                                                              4       2520  99.8%
:ref:`Tai Dam <GnomeTerminallangTaiDam>`                                                       3       2386  99.9%
====================================================================================  ==========  =========  =============

.. _GnomeTerminallangShan:

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
  while *Gnome Terminal* measures width 9.

.. _GnomeTerminallangTamilSriLanka:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangTamil:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangSanskritGrantha:

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
  while *Gnome Terminal* measures width 14.

.. _GnomeTerminallangJavaneseJavanese:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangMalayalam:

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
  while *Gnome Terminal* measures width 21.

.. _GnomeTerminallangBengali:

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
  while *Gnome Terminal* measures width 12.

.. _GnomeTerminallangKhmerCentral:

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
  while *Gnome Terminal* measures width 25.

.. _GnomeTerminallangKannada:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangKhn:

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
  while *Gnome Terminal* measures width 15.

.. _GnomeTerminallangBurmese:

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
  while *Gnome Terminal* measures width 11.

.. _GnomeTerminallangSanskrit:

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
  while *Gnome Terminal* measures width 13.

.. _GnomeTerminallangTamangEastern:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangMon:

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
  while *Gnome Terminal* measures width 7.

.. _GnomeTerminallangMarathi:

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
  while *Gnome Terminal* measures width 5.

.. _GnomeTerminallangNepali:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangGujarati:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangTelugu:

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
  while *Gnome Terminal* measures width 10.

.. _GnomeTerminallangMaithili:

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
  while *Gnome Terminal* measures width 7.

.. _GnomeTerminallangHindi:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangPanjabiEastern:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangSinhala:

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
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangBhojpuri:

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
  while *Gnome Terminal* measures width 10.

.. _GnomeTerminallangMagahi:

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
  while *Gnome Terminal* measures width 10.

.. _GnomeTerminallangChakma:

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
  while *Gnome Terminal* measures width 8.

.. _GnomeTerminallangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================================
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F92 <https://codepoints.net/U+0F92>`_  '\\u0f92'  Mn                  0  TIBETAN SUBJOINED LETTER GA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0FA4 <https://codepoints.net/U+0FA4>`_  '\\u0fa4'  Mn                  0  TIBETAN SUBJOINED LETTER PA
`U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F50 <https://codepoints.net/U+0F50>`_  '\\u0f50'  Lo                  1  TIBETAN LETTER THA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F5A <https://codepoints.net/U+0F5A>`_  '\\u0f5a'  Lo                  1  TIBETAN LETTER TSHA
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F58 <https://codepoints.net/U+0F58>`_  '\\u0f58'  Lo                  1  TIBETAN LETTER MA
`U+0F50 <https://codepoints.net/U+0F50>`_  '\\u0f50'  Lo                  1  TIBETAN LETTER THA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F4F <https://codepoints.net/U+0F4F>`_  '\\u0f4f'  Lo                  1  TIBETAN LETTER TA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0C <https://codepoints.net/U+0F0C>`_  '\\u0f0c'  Po                  1  TIBETAN MARK DELIMITER TSHEG BSTAR
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ==================================

Total codepoints: 51


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa2\xe0\xbe\x92\xe0\xbe\xb1\xe0\xbd\xa3\xe0\xbc\x8b\xe0\xbd\xa6\xe0\xbe\xa4\xe0\xbe\xb1\xe0\xbd\xb2\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\xb4\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\xba\xe0\xbd\xa0\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\x93\xe0\xbd\xa6\xe0\xbc\x8b\xe0\xbd\x9a\xe0\xbd\x91\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\xbc\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x98\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\xa2\xe0\xbc\x8b\xe0\xbd\x82\xe0\xbd\x8f\xe0\xbd\xbc\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x84\xe0\xbc\x8c\xe0\xbc\x8d|\\n12345678901234567890123456789012345678|\\n"
        རྒྱལ་སྤྱིའི་ཐོག་དུ་དེའི་གནས་ཚད་གོང་མཐོར་གཏོང་བ་དང༌།|
        12345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 38,
  while *Gnome Terminal* measures width -14.

.. _GnomeTerminallangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
`U+4F55 <https://codepoints.net/U+4F55>`_  '\\u4f55'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F55
`U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
`U+5F53 <https://codepoints.net/U+5F53>`_  '\\u5f53'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F53
`U+5BAA <https://codepoints.net/U+5BAA>`_  '\\u5baa'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BAA
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
`U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
`U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
`U+8D4B <https://codepoints.net/U+8D4B>`_  '\\u8d4b'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D4B
`U+4E88 <https://codepoints.net/U+4E88>`_  '\\u4e88'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E88
`U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
`U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
`U+57FA <https://codepoints.net/U+57FA>`_  '\\u57fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-57FA
`U+672C <https://codepoints.net/U+672C>`_  '\\u672c'  Lo                  2  CJK UNIFIED IDEOGRAPH-672C
`U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
`U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
`U+906D <https://codepoints.net/U+906D>`_  '\\u906d'  Lo                  2  CJK UNIFIED IDEOGRAPH-906D
`U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
`U+4FB5 <https://codepoints.net/U+4FB5>`_  '\\u4fb5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FB5
`U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
`U+65F6 <https://codepoints.net/U+65F6>`_  '\\u65f6'  Lo                  2  CJK UNIFIED IDEOGRAPH-65F6
=========================================  =========  ==========  =========  ==========================

Total codepoints: 23


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xbb\xe4\xbd\x95\xe4\xba\xba\xe5\xbd\x93\xe5\xae\xaa\xe6\xb3\x95\xe6\x88\x96\xe6\xb3\x95\xe5\xbe\x8b\xe6\x89\x80\xe8\xb5\x8b\xe4\xba\x88\xe4\xbb\x96\xe7\x9a\x84\xe5\x9f\xba\xe6\x9c\xac\xe6\x9d\x83\xe5\x88\xa9\xe9\x81\xad\xe5\x8f\x97\xe4\xbe\xb5\xe5\xae\xb3\xe6\x97\xb6|\\n1234567890123456789012345678901234567890123456|\\n"
        任何人当宪法或法律所赋予他的基本权利遭受侵害时|
        1234567890123456789012345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 46,
  while *Gnome Terminal* measures width 39.

.. _GnomeTerminallangChineseYue:

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5514 <https://codepoints.net/U+5514>`_  '\\u5514'  Lo                  2  CJK UNIFIED IDEOGRAPH-5514
`U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
`U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
`U+4F55 <https://codepoints.net/U+4F55>`_  '\\u4f55'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F55
`U+6B67 <https://codepoints.net/U+6B67>`_  '\\u6b67'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B67
`U+89C6 <https://codepoints.net/U+89C6>`_  '\\u89c6'  Lo                  2  CJK UNIFIED IDEOGRAPH-89C6
=========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x94\x94\xe5\x8f\x97\xe4\xbb\xbb\xe4\xbd\x95\xe6\xad\xa7\xe8\xa7\x86|\\n123456789012|\\n"
        唔受任何歧视|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *Gnome Terminal* measures width -12.

.. _GnomeTerminallangChineseGan:

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+62D8 <https://codepoints.net/U+62D8>`_  '\\u62d8'  Lo                  2  CJK UNIFIED IDEOGRAPH-62D8
`U+7981 <https://codepoints.net/U+7981>`_  '\\u7981'  Lo                  2  CJK UNIFIED IDEOGRAPH-7981
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+653E <https://codepoints.net/U+653E>`_  '\\u653e'  Lo                  2  CJK UNIFIED IDEOGRAPH-653E
`U+9010 <https://codepoints.net/U+9010>`_  '\\u9010'  Lo                  2  CJK UNIFIED IDEOGRAPH-9010
`U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
`U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
=========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x8b\x98\xe7\xa6\x81\xe6\x88\x96\xe6\x94\xbe\xe9\x80\x90\xe4\xb8\x8d\xe5\xbe\x97|\\n12345678901234|\\n"
        拘禁或放逐不得|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangChineseWu:

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+516B <https://codepoints.net/U+516B>`_  '\\u516b'  Lo                  2  CJK UNIFIED IDEOGRAPH-516B
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x85\xab\xe6\x9d\xa1|\\n123456|\\n"
        第八条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width -58.

.. _GnomeTerminallangChineseHakka:

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5173 <https://codepoints.net/U+5173>`_  '\\u5173'  Lo                  2  CJK UNIFIED IDEOGRAPH-5173
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+653E <https://codepoints.net/U+653E>`_  '\\u653e'  Lo                  2  CJK UNIFIED IDEOGRAPH-653E
`U+9010 <https://codepoints.net/U+9010>`_  '\\u9010'  Lo                  2  CJK UNIFIED IDEOGRAPH-9010
=========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\xb3\xe6\x88\x96\xe6\x94\xbe\xe9\x80\x90|\\n12345678|\\n"
        关或放逐|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Gnome Terminal* measures width -10.

.. _GnomeTerminallangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+516B <https://codepoints.net/U+516B>`_  '\\u516b'  Lo                  2  CJK UNIFIED IDEOGRAPH-516B
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x85\xab\xe6\x9d\xa1|\\n123456|\\n"
        第八条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width -54.

.. _GnomeTerminallangChineseMandarinTianjin:

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
  while *Gnome Terminal* measures width -42.

.. _GnomeTerminallangChineseXiang:

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
`U+516B <https://codepoints.net/U+516B>`_  '\\u516b'  Lo                  2  CJK UNIFIED IDEOGRAPH-516B
`U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x85\xab\xe6\x9d\xa1|\\n123456|\\n"
        第八条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width -58.

.. _GnomeTerminallangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F63 <https://codepoints.net/U+0F63>`_  '\\u0f63'  Lo                  1  TIBETAN LETTER LA
`U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
`U+0FA9 <https://codepoints.net/U+0FA9>`_  '\\u0fa9'  Mn                  0  TIBETAN SUBJOINED LETTER TSA
`U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F58 <https://codepoints.net/U+0F58>`_  '\\u0f58'  Lo                  1  TIBETAN LETTER MA
`U+0F50 <https://codepoints.net/U+0F50>`_  '\\u0f50'  Lo                  1  TIBETAN LETTER THA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F50 <https://codepoints.net/U+0F50>`_  '\\u0f50'  Lo                  1  TIBETAN LETTER THA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
`U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0FB2 <https://codepoints.net/U+0FB2>`_  '\\u0fb2'  Mn                  0  TIBETAN SUBJOINED LETTER RA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F58 <https://codepoints.net/U+0F58>`_  '\\u0f58'  Lo                  1  TIBETAN LETTER MA
`U+0F49 <https://codepoints.net/U+0F49>`_  '\\u0f49'  Lo                  1  TIBETAN LETTER NYA
`U+0F58 <https://codepoints.net/U+0F58>`_  '\\u0f58'  Lo                  1  TIBETAN LETTER MA
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
`U+0FA6 <https://codepoints.net/U+0FA6>`_  '\\u0fa6'  Mn                  0  TIBETAN SUBJOINED LETTER BA
`U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
`U+0F0B <https://codepoints.net/U+0F0B>`_  '\\u0f0b'  Po                  1  TIBETAN MARK INTERSYLLABIC TSHEG
`U+0F61 <https://codepoints.net/U+0F61>`_  '\\u0f61'  Lo                  1  TIBETAN LETTER YA
`U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
`U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
`U+0F0D <https://codepoints.net/U+0F0D>`_  '\\u0f0d'  Po                  1  TIBETAN MARK SHAD
=========================================  =========  ==========  =========  ================================

Total codepoints: 44


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x82\xe0\xbc\x8b\xe0\xbd\xa2\xe0\xbc\x8b\xe0\xbd\xa3\xe0\xbd\xb4\xe0\xbc\x8b\xe0\xbd\x96\xe0\xbd\xa2\xe0\xbe\xa9\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x98\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\x90\xe0\xbd\xbc\xe0\xbd\x96\xe0\xbc\x8b\xe0\xbd\x91\xe0\xbd\x96\xe0\xbd\x84\xe0\xbc\x8b\xe0\xbd\xa0\xe0\xbd\x91\xe0\xbe\xb2\xe0\xbc\x8b\xe0\xbd\x98\xe0\xbd\x89\xe0\xbd\x98\xe0\xbc\x8b\xe0\xbd\xa6\xe0\xbe\xa6\xe0\xbd\xba\xe0\xbc\x8b\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x91\xe0\xbc\x8d|\\n12345678901234567890123456789012345|\\n"
        ག་ར་ལུ་བརྩི་མཐོང་དང་ཐོབ་དབང་འདྲ་མཉམ་སྦེ་ཡོད།|
        12345678901234567890123456789012345|

- python `wcwidth.wcswidth()`_ measures width 35,
  while *Gnome Terminal* measures width -5.

.. _GnomeTerminallangJapanese:

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
`U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
`U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
`U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
`U+57DF <https://codepoints.net/U+57DF>`_  '\\u57df'  Lo                  2  CJK UNIFIED IDEOGRAPH-57DF
`U+3067 <https://codepoints.net/U+3067>`_  '\\u3067'  Lo                  2  HIRAGANA LETTER DE
`U+3042 <https://codepoints.net/U+3042>`_  '\\u3042'  Lo                  2  HIRAGANA LETTER A
`U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
`U+3068 <https://codepoints.net/U+3068>`_  '\\u3068'  Lo                  2  HIRAGANA LETTER TO
=========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe9\x9d\x9e\xe8\x87\xaa\xe6\xb2\xbb\xe5\x9c\xb0\xe5\x9f\x9f\xe3\x81\xa7\xe3\x81\x82\xe3\x82\x8b\xe3\x81\xa8|\\n123456789012345678|\\n"
        非自治地域であると|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangChineseMandarinSimplified:

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
  while *Gnome Terminal* measures width -22.

.. _GnomeTerminallangNuosu:

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
  while *Gnome Terminal* measures width -42.

.. _GnomeTerminallangJapaneseOsaka:

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
  while *Gnome Terminal* measures width -52.

.. _GnomeTerminallangJapaneseTokyo:

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
  while *Gnome Terminal* measures width -52.

.. _GnomeTerminallangThai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===========================
`U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
`U+0E1C <https://codepoints.net/U+0E1C>`_  '\\u0e1c'  Lo                  1  THAI CHARACTER PHO PHUNG
`U+0E48 <https://codepoints.net/U+0E48>`_  '\\u0e48'  Mn                  0  THAI CHARACTER MAI EK
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E1E <https://codepoints.net/U+0E1E>`_  '\\u0e1e'  Lo                  1  THAI CHARACTER PHO PHAN
`U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
`U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
`U+0E18 <https://codepoints.net/U+0E18>`_  '\\u0e18'  Lo                  1  THAI CHARACTER THO THONG
`U+0E38 <https://codepoints.net/U+0E38>`_  '\\u0e38'  Mn                  0  THAI CHARACTER SARA U
`U+0E4C <https://codepoints.net/U+0E4C>`_  '\\u0e4c'  Mn                  0  THAI CHARACTER THANTHAKHAT
`U+0E41 <https://codepoints.net/U+0E41>`_  '\\u0e41'  Lo                  1  THAI CHARACTER SARA AE
`U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
`U+0E48 <https://codepoints.net/U+0E48>`_  '\\u0e48'  Mn                  0  THAI CHARACTER MAI EK
`U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
`U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
`U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
=========================================  =========  ==========  =========  ===========================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x80\xe0\xb8\x9c\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xb1\xe0\xb8\x99\xe0\xb8\x98\xe0\xb8\xb8\xe0\xb9\x8c\xe0\xb9\x81\xe0\xb8\xab\xe0\xb9\x88\xe0\xb8\x87\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x95\xe0\xb8\xb4|\\n123456789012|\\n"
        เผ่าพันธุ์แห่งชาติ|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *Gnome Terminal* measures width -15.

.. _GnomeTerminallangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+689D <https://codepoints.net/U+689D>`_  '\\u689d'  Lo                  2  CJK UNIFIED IDEOGRAPH-689D
`U+0039 <https://codepoints.net/U+0039>`_  '9'        Nd                  1  DIGIT NINE
`U+FF1A <https://codepoints.net/U+FF1A>`_  '\\uff1a'  Po                  2  FULLWIDTH COLON
=========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xa2\x9d9\xef\xbc\x9a|\\n12345|\\n"
        條9：|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width -69.

.. _GnomeTerminallangThai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
`U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
`U+0E0E <https://codepoints.net/U+0E0E>`_  '\\u0e0e'  Lo                  1  THAI CHARACTER DO CHADA
`U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
`U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
`U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
`U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
=========================================  =========  ==========  =========  =========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x97\xe0\xb8\xb2\xe0\xb8\x87\xe0\xb8\x81\xe0\xb8\x8e\xe0\xb8\xab\xe0\xb8\xa1\xe0\xb8\xb2\xe0\xb8\xa2|\\n123456789|\\n"
        ทางกฎหมาย|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Gnome Terminal* measures width -17.

.. _GnomeTerminallangChineseMandarinTraditional:

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

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
  while *Gnome Terminal* measures width -12.

.. _GnomeTerminallangJinan:

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
  while *Gnome Terminal* measures width -12.

.. _GnomeTerminallangChineseMandarinGuiyang:

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
  while *Gnome Terminal* measures width -12.

.. _GnomeTerminallangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5173 <https://codepoints.net/U+5173>`_  '\\u5173'  Lo                  2  CJK UNIFIED IDEOGRAPH-5173
`U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
`U+6765 <https://codepoints.net/U+6765>`_  '\\u6765'  Lo                  2  CJK UNIFIED IDEOGRAPH-6765
`U+54A7 <https://codepoints.net/U+54A7>`_  '\\u54a7'  Lo                  2  CJK UNIFIED IDEOGRAPH-54A7
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+8F70 <https://codepoints.net/U+8F70>`_  '\\u8f70'  Lo                  2  CJK UNIFIED IDEOGRAPH-8F70
`U+51FA <https://codepoints.net/U+51FA>`_  '\\u51fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FA
`U+53BB <https://codepoints.net/U+53BB>`_  '\\u53bb'  Lo                  2  CJK UNIFIED IDEOGRAPH-53BB
`U+54A7 <https://codepoints.net/U+54A7>`_  '\\u54a7'  Lo                  2  CJK UNIFIED IDEOGRAPH-54A7
=========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\xb3\xe8\xb5\xb7\xe6\x9d\xa5\xe5\x92\xa7\xe6\x88\x96\xe8\xbd\xb0\xe5\x87\xba\xe5\x8e\xbb\xe5\x92\xa7|\\n123456789012345678|\\n"
        关起来咧或轰出去咧|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==========================
`U+5173 <https://codepoints.net/U+5173>`_  '\\u5173'  Lo                  2  CJK UNIFIED IDEOGRAPH-5173
`U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
`U+6765 <https://codepoints.net/U+6765>`_  '\\u6765'  Lo                  2  CJK UNIFIED IDEOGRAPH-6765
`U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
`U+8005 <https://codepoints.net/U+8005>`_  '\\u8005'  Lo                  2  CJK UNIFIED IDEOGRAPH-8005
`U+8D76 <https://codepoints.net/U+8D76>`_  '\\u8d76'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D76
`U+51FA <https://codepoints.net/U+51FA>`_  '\\u51fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FA
`U+53BB <https://codepoints.net/U+53BB>`_  '\\u53bb'  Lo                  2  CJK UNIFIED IDEOGRAPH-53BB
=========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\xb3\xe8\xb5\xb7\xe6\x9d\xa5\xe6\x88\x96\xe8\x80\x85\xe8\xb5\xb6\xe5\x87\xba\xe5\x8e\xbb|\\n1234567890123456|\\n"
        关起来或者赶出去|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *Gnome Terminal* measures width -6.

.. _GnomeTerminallangChineseMinNan:

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

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
  while *Gnome Terminal* measures width -36.

.. _GnomeTerminallangLao:

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
  while *Gnome Terminal* measures width -10.

.. _GnomeTerminallangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'   Ll                  1  LATIN SMALL LETTER O WITH ACUTE
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
=========================================  ========  ==========  =========  ===============================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "men\xc3\xa9hn\xc3\xadll\xc3\xa9\xc3\xadtyur\xc3\xb3ne.|\\n1234567890123456789|\\n"
        menéhnílléítyuróne.|
        1234567890123456789|

- python `wcwidth.wcswidth()`_ measures width 19,
  while *Gnome Terminal* measures width 11.

.. _GnomeTerminallangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================================
`U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
`U+0458 <https://codepoints.net/U+0458>`_  '\\u0458'  Ll                  1  CYRILLIC SMALL LETTER JE
`U+04E3 <https://codepoints.net/U+04E3>`_  '\\u04e3'  Ll                  1  CYRILLIC SMALL LETTER I WITH MACRON
`U+0447 <https://codepoints.net/U+0447>`_  '\\u0447'  Ll                  1  CYRILLIC SMALL LETTER CHE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ===================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb1\xd1\x98\xd3\xa3\xd1\x87\xd0\xb8.|\\n123456|\\n"
        бјӣчи.|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width -5.

.. _GnomeTerminallangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0053 <https://codepoints.net/U+0053>`_  'S'        Lu                  1  LATIN CAPITAL LETTER S
`U+0048 <https://codepoints.net/U+0048>`_  'H'        Lu                  1  LATIN CAPITAL LETTER H
`U+0049 <https://codepoints.net/U+0049>`_  'I'        Lu                  1  LATIN CAPITAL LETTER I
`U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
`U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
`U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
`U+0053 <https://codepoints.net/U+0053>`_  'S'        Lu                  1  LATIN CAPITAL LETTER S
`U+0308 <https://codepoints.net/U+0308>`_  '\\u0308'  Mn                  0  COMBINING DIAERESIS
`U+0048 <https://codepoints.net/U+0048>`_  'H'        Lu                  1  LATIN CAPITAL LETTER H
`U+004F <https://codepoints.net/U+004F>`_  'O'        Lu                  1  LATIN CAPITAL LETTER O
`U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
=========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "SHINANS\xcc\x88HON|\\n1234567890|\\n"
        SHINANS̈HON|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangGumuz:

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "shooka|\\n123456|\\n"
        shooka|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ================================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
`U+0105 <https://codepoints.net/U+0105>`_  '\\u0105'  Ll                  1  LATIN SMALL LETTER A WITH OGONEK
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0105 <https://codepoints.net/U+0105>`_  '\\u0105'  Ll                  1  LATIN SMALL LETTER A WITH OGONEK
`U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
`U+012F <https://codepoints.net/U+012F>`_  '\\u012f'  Ll                  1  LATIN SMALL LETTER I WITH OGONEK
`U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
=========================================  =========  ==========  =========  ================================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nin\xc3\xa1n\xc3\xadl\xca\xbc\xc4\x85\xcc\x81\xc4\x85j\xc4\xaf\xca\xbc|\\n1234567890123|\\n"
        ninánílʼą́ąjįʼ|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
=========================================  ========  ==========  =========  ====================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "imalhpi'sa.|\\n12345678901|\\n"
        imalhpi'sa.|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *Gnome Terminal* measures width -8.

.. _GnomeTerminallangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "hak|\\n123|\\n"
        hak|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width 1.

.. _GnomeTerminallangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
=========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xb1e\xc3\xb1t|\\n1234|\\n"
        ñeñt|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangAmarakaeri:

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
=========================================  ========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Aratbut|\\n1234567|\\n"
        Aratbut|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Gnome Terminal* measures width 3.

.. _GnomeTerminallangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0054 <https://codepoints.net/U+0054>`_  'T'       Lu                  1  LATIN CAPITAL LETTER T
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Te'o|\\n1234|\\n"
        Te'o|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width 1.

.. _GnomeTerminallangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================================
`U+041D <https://codepoints.net/U+041D>`_  '\\u041d'  Lu                  1  CYRILLIC CAPITAL LETTER EN
`U+044E <https://codepoints.net/U+044E>`_  '\\u044e'  Ll                  1  CYRILLIC SMALL LETTER YU
`U+04A3 <https://codepoints.net/U+04A3>`_  '\\u04a3'  Ll                  1  CYRILLIC SMALL LETTER EN WITH DESCENDER
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
=========================================  =========  ==========  =========  =======================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\x9d\xd1\x8e\xd2\xa3\xd0\xb8\xcc\x84|\\n1234|\\n"
        Нюңӣ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width -6.

.. _GnomeTerminallangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
`U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
=========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x82\xd1\x83|\\n12|\\n"
        ту|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Gnome Terminal* measures width -1.

.. _GnomeTerminallangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
`U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
`U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
`U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
=========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb4\xd0\xb8\xd0\xb0\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb8|\\n1234567|\\n"
        диавари|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Gnome Terminal* measures width 2.

.. _GnomeTerminallangColorado:

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

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
  while *Gnome Terminal* measures width -6.

.. _GnomeTerminallangVeps:

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
=========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nimitadud|\\n123456789|\\n"
        nimitadud|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Gnome Terminal* measures width 5.

.. _GnomeTerminallangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "koni|\\n1234|\\n"
        koni|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width -4.

.. _GnomeTerminallangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =====================
`U+BC1B <https://codepoints.net/U+BC1B>`_  '\\ubc1b'  Lo                  2  HANGUL SYLLABLE BAD
`U+C54A <https://codepoints.net/U+C54A>`_  '\\uc54a'  Lo                  2  HANGUL SYLLABLE ANH
`U+B294 <https://codepoints.net/U+B294>`_  '\\ub294'  Lo                  2  HANGUL SYLLABLE NEUN
`U+AD8C <https://codepoints.net/U+AD8C>`_  '\\uad8c'  Lo                  2  HANGUL SYLLABLE GWEON
`U+B9AC <https://codepoints.net/U+B9AC>`_  '\\ub9ac'  Lo                  2  HANGUL SYLLABLE RI
`U+AC00 <https://codepoints.net/U+AC00>`_  '\\uac00'  Lo                  2  HANGUL SYLLABLE GA
=========================================  =========  ==========  =========  =====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xeb\xb0\x9b\xec\x95\x8a\xeb\x8a\x94\xea\xb6\x8c\xeb\xa6\xac\xea\xb0\x80|\\n123456789012|\\n"
        받않는권리가|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *Gnome Terminal* measures width 6.

.. _GnomeTerminallangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+05D1 <https://codepoints.net/U+05D1>`_  '\\u05d1'  Lo                  1  HEBREW LETTER BET
`U+05D0 <https://codepoints.net/U+05D0>`_  '\\u05d0'  Lo                  1  HEBREW LETTER ALEF
`U+05B7 <https://codepoints.net/U+05B7>`_  '\\u05b7'  Mn                  0  HEBREW POINT PATAH
`U+05E8 <https://codepoints.net/U+05E8>`_  '\\u05e8'  Lo                  1  HEBREW LETTER RESH
`U+05E2 <https://codepoints.net/U+05E2>`_  '\\u05e2'  Lo                  1  HEBREW LETTER AYIN
`U+05DB <https://codepoints.net/U+05DB>`_  '\\u05db'  Lo                  1  HEBREW LETTER KAF
`U+05D8 <https://codepoints.net/U+05D8>`_  '\\u05d8'  Lo                  1  HEBREW LETTER TET
`U+05D9 <https://codepoints.net/U+05D9>`_  '\\u05d9'  Lo                  1  HEBREW LETTER YOD
`U+05E7 <https://codepoints.net/U+05E7>`_  '\\u05e7'  Lo                  1  HEBREW LETTER QOF
`U+05D8 <https://codepoints.net/U+05D8>`_  '\\u05d8'  Lo                  1  HEBREW LETTER TET
=========================================  =========  ==========  =========  ==================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x91\xd7\x90\xd6\xb7\xd7\xa8\xd7\xa2\xd7\x9b\xd7\x98\xd7\x99\xd7\xa7\xd7\x98|\\n123456789|\\n"
        באַרעכטיקט|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Gnome Terminal* measures width 6.

.. _GnomeTerminallangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tilelliyin|\\n1234567890|\\n"
        tilelliyin|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Gnome Terminal* measures width 3.

.. _GnomeTerminallangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

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
  while *Gnome Terminal* measures width -12.

.. _GnomeTerminallangMaldivian:

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+078A <https://codepoints.net/U+078A>`_  '\\u078a'  Lo                  1  THAANA LETTER FAAFU
`U+07A8 <https://codepoints.net/U+07A8>`_  '\\u07a8'  Mn                  0  THAANA IBIFILI
`U+0794 <https://codepoints.net/U+0794>`_  '\\u0794'  Lo                  1  THAANA LETTER YAA
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+0788 <https://codepoints.net/U+0788>`_  '\\u0788'  Lo                  1  THAANA LETTER VAAVU
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+0785 <https://codepoints.net/U+0785>`_  '\\u0785'  Lo                  1  THAANA LETTER LHAVIYANI
`U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
`U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
`U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
`U+0786 <https://codepoints.net/U+0786>`_  '\\u0786'  Lo                  1  THAANA LETTER KAAFU
`U+07AC <https://codepoints.net/U+07AC>`_  '\\u07ac'  Mn                  0  THAANA EBEFILI
`U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
`U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
=========================================  =========  ==========  =========  =======================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x8a\xde\xa8\xde\x94\xde\xa6\xde\x88\xde\xa6\xde\x85\xde\xaa\xde\x8c\xde\xa6\xde\x86\xde\xac\xde\x87\xde\xb0|\\n1234567|\\n"
        ފިޔަވަޅުތަކެއް|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Gnome Terminal* measures width 3.

.. _GnomeTerminallangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==================
`U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
`U+0722 <https://codepoints.net/U+0722>`_  '\\u0722'  Lo                  1  SYRIAC LETTER NUN
=========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\x9d\xdc\xa2|\\n12|\\n"
        ܝܢ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Gnome Terminal* measures width -3.

.. _GnomeTerminallangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+0327 <https://codepoints.net/U+0327>`_  '\\u0327'  Mn                  0  COMBINING CEDILLA
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
=========================================  =========  ==========  =========  ====================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "aplicac\xcc\xa7on|\\n123456789|\\n"
        aplicaçon|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Gnome Terminal* measures width 6.

.. _GnomeTerminallangKorean:

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+B610 <https://codepoints.net/U+B610>`_  '\\ub610'  Lo                  2  HANGUL SYLLABLE DDO
`U+B294 <https://codepoints.net/U+B294>`_  '\\ub294'  Lo                  2  HANGUL SYLLABLE NEUN
=========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xeb\x98\x90\xeb\x8a\x94|\\n1234|\\n"
        또는|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width -4.

.. _GnomeTerminallangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

=================================================  =============  ==========  =========  ======================
Codepoint                                          Python         Category      wcwidth  Name
=================================================  =============  ==========  =========  ======================
`U+0001E931 <https://codepoints.net/U+0001E931>`_  '\\U0001e931'  Ll                  1  ADLAM SMALL LETTER WAW
`U+0001E92E <https://codepoints.net/U+0001E92E>`_  '\\U0001e92e'  Ll                  1  ADLAM SMALL LETTER O
`U+0001E932 <https://codepoints.net/U+0001E932>`_  '\\U0001e932'  Ll                  1  ADLAM SMALL LETTER NUN
`U+0001E92D <https://codepoints.net/U+0001E92D>`_  '\\U0001e92d'  Ll                  1  ADLAM SMALL LETTER I
=================================================  =============  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xb1\xf0\x9e\xa4\xae\xf0\x9e\xa4\xb2\xf0\x9e\xa4\xad|\\n1234|\\n"
        𞤱𞤮𞤲𞤭|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width 1.

.. _GnomeTerminallangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "todi|\\n1234|\\n"
        todi|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width -13.

.. _GnomeTerminallangTicuna:

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
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===============================
`U+0269 <https://codepoints.net/U+0269>`_  '\\u0269'  Ll                  1  LATIN SMALL LETTER IOTA
`U+0256 <https://codepoints.net/U+0256>`_  '\\u0256'  Ll                  1  LATIN SMALL LETTER D WITH TAIL
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
`U+007A <https://codepoints.net/U+007A>`_  'z'        Ll                  1  LATIN SMALL LETTER Z
`U+0269 <https://codepoints.net/U+0269>`_  '\\u0269'  Ll                  1  LATIN SMALL LETTER IOTA
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
=========================================  =========  ==========  =========  ===============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc9\xa9\xc9\x96\xc9\x9b\xc9\x9bz\xc9\xa9n\xc3\xa1|\\n12345678|\\n"
        ɩɖɛɛzɩná|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "langaj|\\n123456|\\n"
        langaj|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width 2.

.. _GnomeTerminallangw:

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0058 <https://codepoints.net/U+0058>`_  'X'       Lu                  1  LATIN CAPITAL LETTER X
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0078 <https://codepoints.net/U+0078>`_  'x'       Ll                  1  LATIN SMALL LETTER X
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Xexeme|\\n123456|\\n"
        Xexeme|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0633 <https://codepoints.net/U+0633>`_  '\\u0633'  Lo                  1  ARABIC LETTER SEEN
`U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+0629 <https://codepoints.net/U+0629>`_  '\\u0629'  Lo                  1  ARABIC LETTER TEH MARBUTA
=========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85\xd8\xa9|\\n123456|\\n"
        وسلامة|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width -1.

.. _GnomeTerminallangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
=========================================  =========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mosu\xcc\x81su|\\n123456|\\n"
        mosúsu|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ===================================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ===================================
`U+0622 <https://codepoints.net/U+0622>`_  '\\u0622'  Lo                  1  ARABIC LETTER ALEF WITH MADDA ABOVE
`U+0632 <https://codepoints.net/U+0632>`_  '\\u0632'  Lo                  1  ARABIC LETTER ZAIN
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
=========================================  =========  ==========  =========  ===================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa2\xd8\xb2\xd8\xa7\xd8\xaf\xdb\x8c|\\n12345|\\n"
        آزادی|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "akken|\\n12345|\\n"
        akken|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
=========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xb1atu|\\n1234|\\n"
        ñatu|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ====================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0307 <https://codepoints.net/U+0307>`_  '\\u0307'  Mn                  0  COMBINING DOT ABOVE
`U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
=========================================  =========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xcc\x87wet|\\n1234|\\n"
        ṅwet|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width 2.

.. _GnomeTerminallangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ere|\\n123|\\n"
        ere|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width -3.

.. _GnomeTerminallangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

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
  while *Gnome Terminal* measures width -4.

.. _GnomeTerminallangUduk:

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
`U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mo.|\\n123|\\n"
        mo.|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width -1.

.. _GnomeTerminallangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =======================
`U+063A <https://codepoints.net/U+063A>`_  '\\u063a'  Lo                  1  ARABIC LETTER GHAIN
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
`U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
=========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xba\xdb\x8c\xd8\xb1|\\n123|\\n"
        غیر|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width 1.

.. _GnomeTerminallangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
=========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc5\x8bmanti|\\n123456|\\n"
        ŋmanti|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width 4.

.. _GnomeTerminallangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

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
  while *Gnome Terminal* measures width -14.

.. _GnomeTerminallangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
=========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "le\xcc\x81|\\n12|\\n"
        lé|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Gnome Terminal* measures width -5.

.. _GnomeTerminallangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
`U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
`U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
`U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
`U+06C1 <https://codepoints.net/U+06C1>`_  '\\u06c1'  Lo                  1  ARABIC LETTER HEH GOAL
=========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x85\xd8\xaa\xd8\xad\xd8\xaf\xdb\x81|\\n12345|\\n"
        متحدہ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
=========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "m\xc9\x94nu|\\n1234|\\n"
        mɔnu|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "paasde|\\n123456|\\n"
        paasde|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width 3.

.. _GnomeTerminallangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ===============================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ===============================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
`U+00E0 <https://codepoints.net/U+00E0>`_  '\\xe0'   Ll                  1  LATIN SMALL LETTER A WITH GRAVE
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
=========================================  ========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "l\xc3\xa1\xc3\xa0rin|\\n123456|\\n"
        láàrin|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Gnome Terminal* measures width -1.

.. _GnomeTerminallangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
`U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
=========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yiro|\\n1234|\\n"
        yiro|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width 2.

.. _GnomeTerminallangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
`U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "qua|\\n123|\\n"
        qua|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======================
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
`U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
`U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
=========================================  =========  ==========  =========  ======================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "eloo\xc5\x8biic.|\\n123456789|\\n"
        elooŋiic.|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Gnome Terminal* measures width 3.

.. _GnomeTerminallangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
`U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
`U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kwraa|\\n12345|\\n"
        kwraa|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width 3.

.. _GnomeTerminallangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
`U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
=========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "d\xc9\x94kun|\\n12345|\\n"
        dɔkun|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width -1.

.. _GnomeTerminallangDagaareSouthern:

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
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
`U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nna|\\n123|\\n"
        nna|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width -4.

.. _GnomeTerminallangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ======================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ======================
`U+0050 <https://codepoints.net/U+0050>`_  'P'       Lu                  1  LATIN CAPITAL LETTER P
`U+0045 <https://codepoints.net/U+0045>`_  'E'       Lu                  1  LATIN CAPITAL LETTER E
`U+005A <https://codepoints.net/U+005A>`_  'Z'       Lu                  1  LATIN CAPITAL LETTER Z
`U+0048 <https://codepoints.net/U+0048>`_  'H'       Lu                  1  LATIN CAPITAL LETTER H
`U+0045 <https://codepoints.net/U+0045>`_  'E'       Lu                  1  LATIN CAPITAL LETTER E
=========================================  ========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "PEZHE|\\n12345|\\n"
        PEZHE|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width -1.

.. _GnomeTerminallangSererSine:

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ==============================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ==============================
`U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
`U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
`U+0257 <https://codepoints.net/U+0257>`_  '\\u0257'  Ll                  1  LATIN SMALL LETTER D WITH HOOK
=========================================  =========  ==========  =========  ==============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "oa\xc9\x97|\\n123|\\n"
        oaɗ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
=========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "se|\\n12|\\n"
        se|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Gnome Terminal* measures width -2.

.. _GnomeTerminallangUrdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
`U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
`U+06C1 <https://codepoints.net/U+06C1>`_  '\\u06c1'  Lo                  1  ARABIC LETTER HEH GOAL
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
`U+06BA <https://codepoints.net/U+06BA>`_  '\\u06ba'  Lo                  1  ARABIC LETTER NOON GHUNNA
=========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x86\xdb\x81\xdb\x8c\xda\xba|\\n12345|\\n"
        انہیں|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width 2.

.. _GnomeTerminallangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =================
`U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
`U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
`U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
=========================================  =========  ==========  =========  =================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xad\xd9\x82\xd9\x88\xd9\x82\xd9\x88|\\n12345|\\n"
        حقوقو|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Gnome Terminal* measures width 2.

.. _GnomeTerminallangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
`U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
`U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
`U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
=========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xdb\x8c\xd8\xaa\xdb\x92|\\n1234|\\n"
        کیتے|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangBelandaViri:

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
  while *Gnome Terminal* measures width -3.

.. _GnomeTerminallangUrdu2:

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
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangChinantecChiltepec:

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

=========================================  ========  ==========  =========  ====================
Codepoint                                  Python    Category      wcwidth  Name
=========================================  ========  ==========  =========  ====================
`U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
`U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
`U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
=========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "le'|\\n123|\\n"
        le'|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width 1.

.. _GnomeTerminallangDangme:

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
`U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
`U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
=========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x94s\xc9\x94|\\n1234|\\n"
        nɔsɔ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Gnome Terminal* measures width -1.

.. _GnomeTerminallangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

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
  while *Gnome Terminal* measures width -3.

.. _GnomeTerminallangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  =========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  =========================
`U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
`U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
`U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
=========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "en\xc9\x9b|\\n123|\\n"
        enɛ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminallangTaiDam:

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ========================
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ========================
`U+AA80 <https://codepoints.net/U+AA80>`_  '\\uaa80'  Lo                  1  TAI VIET LETTER LOW KO
`U+AAAE <https://codepoints.net/U+AAAE>`_  '\\uaaae'  Lo                  1  TAI VIET LETTER LOW O
`U+AA89 <https://codepoints.net/U+AA89>`_  '\\uaa89'  Lo                  1  TAI VIET LETTER HIGH NGO
=========================================  =========  ==========  =========  ========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\x80\xea\xaa\xae\xea\xaa\x89|\\n123|\\n"
        ꪀꪮꪉ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Gnome Terminal* measures width 0.

.. _GnomeTerminaldecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

DEC private modes results for *Gnome Terminal*: 128 supported modes
out of 157 total modes tested (81.5% support).

Complete list of DEC private modes tested:

.. _GnomeTerminaldecmode1:

.. _GnomeTerminaldecmode2:

.. _GnomeTerminaldecmode3:

.. _GnomeTerminaldecmode4:

.. _GnomeTerminaldecmode5:

.. _GnomeTerminaldecmode6:

.. _GnomeTerminaldecmode7:

.. _GnomeTerminaldecmode8:

.. _GnomeTerminaldecmode9:

.. _GnomeTerminaldecmode10:

.. _GnomeTerminaldecmode11:

.. _GnomeTerminaldecmode12:

.. _GnomeTerminaldecmode13:

.. _GnomeTerminaldecmode14:

.. _GnomeTerminaldecmode16:

.. _GnomeTerminaldecmode18:

.. _GnomeTerminaldecmode19:

.. _GnomeTerminaldecmode25:

.. _GnomeTerminaldecmode30:

.. _GnomeTerminaldecmode34:

.. _GnomeTerminaldecmode35:

.. _GnomeTerminaldecmode36:

.. _GnomeTerminaldecmode38:

.. _GnomeTerminaldecmode40:

.. _GnomeTerminaldecmode41:

.. _GnomeTerminaldecmode42:

.. _GnomeTerminaldecmode43:

.. _GnomeTerminaldecmode44:

.. _GnomeTerminaldecmode45:

.. _GnomeTerminaldecmode46:

.. _GnomeTerminaldecmode47:

.. _GnomeTerminaldecmode53:

.. _GnomeTerminaldecmode57:

.. _GnomeTerminaldecmode58:

.. _GnomeTerminaldecmode59:

.. _GnomeTerminaldecmode60:

.. _GnomeTerminaldecmode61:

.. _GnomeTerminaldecmode64:

.. _GnomeTerminaldecmode66:

.. _GnomeTerminaldecmode67:

.. _GnomeTerminaldecmode68:

.. _GnomeTerminaldecmode69:

.. _GnomeTerminaldecmode73:

.. _GnomeTerminaldecmode80:

.. _GnomeTerminaldecmode81:

.. _GnomeTerminaldecmode83:

.. _GnomeTerminaldecmode84:

.. _GnomeTerminaldecmode85:

.. _GnomeTerminaldecmode90:

.. _GnomeTerminaldecmode95:

.. _GnomeTerminaldecmode96:

.. _GnomeTerminaldecmode97:

.. _GnomeTerminaldecmode98:

.. _GnomeTerminaldecmode99:

.. _GnomeTerminaldecmode100:

.. _GnomeTerminaldecmode101:

.. _GnomeTerminaldecmode102:

.. _GnomeTerminaldecmode103:

.. _GnomeTerminaldecmode104:

.. _GnomeTerminaldecmode106:

.. _GnomeTerminaldecmode108:

.. _GnomeTerminaldecmode109:

.. _GnomeTerminaldecmode110:

.. _GnomeTerminaldecmode111:

.. _GnomeTerminaldecmode112:

.. _GnomeTerminaldecmode113:

.. _GnomeTerminaldecmode114:

.. _GnomeTerminaldecmode115:

.. _GnomeTerminaldecmode116:

.. _GnomeTerminaldecmode117:

.. _GnomeTerminaldecmode1000:

.. _GnomeTerminaldecmode1001:

.. _GnomeTerminaldecmode1002:

.. _GnomeTerminaldecmode1003:

.. _GnomeTerminaldecmode1004:

.. _GnomeTerminaldecmode1005:

.. _GnomeTerminaldecmode1006:

.. _GnomeTerminaldecmode1007:

.. _GnomeTerminaldecmode1010:

.. _GnomeTerminaldecmode1011:

.. _GnomeTerminaldecmode1014:

.. _GnomeTerminaldecmode1015:

.. _GnomeTerminaldecmode1016:

.. _GnomeTerminaldecmode1021:

.. _GnomeTerminaldecmode1034:

.. _GnomeTerminaldecmode1035:

.. _GnomeTerminaldecmode1036:

.. _GnomeTerminaldecmode1037:

.. _GnomeTerminaldecmode1039:

.. _GnomeTerminaldecmode1040:

.. _GnomeTerminaldecmode1041:

.. _GnomeTerminaldecmode1042:

.. _GnomeTerminaldecmode1043:

.. _GnomeTerminaldecmode1044:

.. _GnomeTerminaldecmode1046:

.. _GnomeTerminaldecmode1047:

.. _GnomeTerminaldecmode1048:

.. _GnomeTerminaldecmode1049:

.. _GnomeTerminaldecmode1050:

.. _GnomeTerminaldecmode1051:

.. _GnomeTerminaldecmode1052:

.. _GnomeTerminaldecmode1053:

.. _GnomeTerminaldecmode1060:

.. _GnomeTerminaldecmode1061:

.. _GnomeTerminaldecmode1070:

.. _GnomeTerminaldecmode1243:

.. _GnomeTerminaldecmode2001:

.. _GnomeTerminaldecmode2002:

.. _GnomeTerminaldecmode2003:

.. _GnomeTerminaldecmode2004:

.. _GnomeTerminaldecmode2005:

.. _GnomeTerminaldecmode2006:

.. _GnomeTerminaldecmode2026:

.. _GnomeTerminaldecmode2500:

.. _GnomeTerminaldecmode2501:

.. _GnomeTerminaldecmode7700:

.. _GnomeTerminaldecmode7711:

.. _GnomeTerminaldecmode7727:

.. _GnomeTerminaldecmode7728:

.. _GnomeTerminaldecmode7730:

.. _GnomeTerminaldecmode7766:

.. _GnomeTerminaldecmode7767:

.. _GnomeTerminaldecmode7783:

.. _GnomeTerminaldecmode7786:

.. _GnomeTerminaldecmode7787:

.. _GnomeTerminaldecmode7796:

.. _GnomeTerminaldecmode8452:

.. _GnomeTerminaldecmode8800:

==============  =============================  =======================================================================  ===========  ============
Mode            Name                           Description                                                              Supported    Changeable
==============  =============================  =======================================================================  ===========  ============
DEC Mode 1      DECCKM                         Cursor Keys Mode                                                         Yes          Yes
DEC Mode 2      DECANM                         ANSI/VT52 Mode                                                           Yes          No
DEC Mode 3      DECCOLM                        Column Mode                                                              Yes          Yes
DEC Mode 4      DECSCLM                        Scrolling Mode                                                           Yes          No
DEC Mode 5      DECSCNM                        Screen Mode (light or dark screen)                                       Yes          Yes
DEC Mode 6      DECOM                          Origin Mode                                                              Yes          Yes
DEC Mode 7      DECAWM                         Auto Wrap Mode                                                           Yes          Yes
DEC Mode 8      DECARM                         Auto Repeat Mode                                                         Yes          No
DEC Mode 9      DECINLM                        Interlace Mode / Mouse X10 tracking                                      Yes          Yes
DEC Mode 10     DECEDM                         Editing Mode / Show toolbar (rxvt)                                       Yes          No
DEC Mode 11     DECLTM                         Line Transmit Mode                                                       Yes          No
DEC Mode 12     DECKANAM                       Katakana Shift Mode / Blinking cursor (xterm)                            Yes          No
DEC Mode 13     DECSCFDM                       Space Compression/Field Delimiter Mode / Start blinking cursor (xterm)   Yes          No
DEC Mode 14     DECTEM                         Transmit Execution Mode / Enable XOR of blinking cursor control (xterm)  Yes          No
DEC Mode 16     DECEKEM                        Edit Key Execution Mode                                                  Yes          No
DEC Mode 18     DECPFF                         Print Form Feed                                                          Yes          No
DEC Mode 19     DECPEX                         Printer Extent                                                           Yes          No
DEC Mode 20     OV1                            Overstrike                                                               No           No
DEC Mode 21     BA1                            Local BASIC                                                              No           No
DEC Mode 22     BA2                            Host BASIC                                                               No           No
DEC Mode 23     PK1                            Programmable Keypad                                                      No           No
DEC Mode 24     AH1                            Auto Hardcopy                                                            No           No
DEC Mode 25     DECTCEM                        Text Cursor Enable Mode                                                  Yes          Yes
DEC Mode 27     DECPSP                         Proportional Spacing                                                     No           No
DEC Mode 29     DECPSM                         Pitch Select Mode                                                        No           No
DEC Mode 30     SHOW_SCROLLBAR_RXVT            Show scrollbar (rxvt)                                                    Yes          No
DEC Mode 34     DECRLM                         Cursor Right to Left Mode                                                Yes          No
DEC Mode 35     DECHEBM                        Hebrew (Keyboard) Mode / Enable font-shifting functions (rxvt)           Yes          No
DEC Mode 36     DECHEM                         Hebrew Encoding Mode                                                     Yes          No
DEC Mode 38     DECTEK                         Tektronix 4010/4014 Mode                                                 Yes          No
DEC Mode 40     DECCRNLM                       Carriage Return/New Line Mode / Allow 80⇒132 mode (xterm)                Yes          Yes
DEC Mode 41     DECUPM                         Unidirectional Print Mode / more(1) fix (xterm)                          Yes          No
DEC Mode 42     DECNRCM                        National Replacement Character Set Mode                                  Yes          No
DEC Mode 43     DECGEPM                        Graphics Expanded Print Mode                                             Yes          No
DEC Mode 44     DECGPCM                        Graphics Print Color Mode / Turn on margin bell (xterm)                  Yes          No
DEC Mode 45     DECGPCS                        Graphics Print Color Syntax / Reverse-wraparound mode (xterm)            Yes          No
DEC Mode 46     DECGPBM                        Graphics Print Background Mode / Start logging (xterm)                   Yes          No
DEC Mode 47     DECGRPM                        Graphics Rotated Print Mode / Use Alternate Screen Buffer (xterm)        Yes          Yes
DEC Mode 49     DECTHAIM                       Thai Input Mode                                                          No           No
DEC Mode 50     DECTHAICM                      Thai Cursor Mode                                                         No           No
DEC Mode 51     DECBWRM                        Black/White Reversal Mode                                                No           No
DEC Mode 52     DECOPM                         Origin Placement Mode                                                    No           No
DEC Mode 53     DEC131TM                       VT131 Transmit Mode                                                      Yes          No
DEC Mode 55     DECBPM                         Bold Page Mode                                                           No           No
DEC Mode 57     DECNAKB                        Greek/N-A Keyboard Mapping Mode                                          Yes          No
DEC Mode 58     DECIPEM                        Enter IBM Proprinter Emulation Mode                                      Yes          No
DEC Mode 59     DECKKDM                        Kanji/Katakana Display Mode                                              Yes          No
DEC Mode 60     DECHCCM                        Horizontal Cursor Coupling                                               Yes          No
DEC Mode 61     DECVCCM                        Vertical Cursor Coupling Mode                                            Yes          No
DEC Mode 64     DECPCCM                        Page Cursor Coupling Mode                                                Yes          No
DEC Mode 65     DECBCMM                        Business Color Matching Mode                                             No           No
DEC Mode 66     DECNKM                         Numeric Keypad Mode                                                      Yes          Yes
DEC Mode 67     DECBKM                         Backarrow Key Mode                                                       Yes          No
DEC Mode 68     DECKBUM                        Keyboard Usage Mode                                                      Yes          No
DEC Mode 69     DECVSSM                        Vertical Split Screen Mode / DECLRMM - Left Right Margin Mode            Yes          Yes
DEC Mode 70     DECFPM                         Force Plot Mode                                                          No           No
DEC Mode 73     DECXRLM                        Transmission Rate Limiting                                               Yes          No
DEC Mode 80     DECSDM                         Sixel Display Mode                                                       Yes          Yes
DEC Mode 81     DECKPM                         Key Position Mode                                                        Yes          No
DEC Mode 83     WY_52_LINE                     52 line mode (WY-370)                                                    Yes          No
DEC Mode 84     WYENAT_OFF                     Erasable/nonerasable WYENAT Off attribute select (WY-370)                Yes          No
DEC Mode 85     REPLACEMENT_CHAR_COLOR         Replacement character color (WY-370)                                     Yes          No
DEC Mode 90     DECTHAISCM                     Thai Space Compensating Mode                                             Yes          No
DEC Mode 95     DECNCSM                        No Clearing Screen on Column Change Mode                                 Yes          No
DEC Mode 96     DECRLCM                        Right to Left Copy Mode                                                  Yes          No
DEC Mode 97     DECCRTSM                       CRT Save Mode                                                            Yes          No
DEC Mode 98     DECARSM                        Auto Resize Mode                                                         Yes          No
DEC Mode 99     DECMCM                         Modem Control Mode                                                       Yes          No
DEC Mode 100    DECAAM                         Auto Answerback Mode                                                     Yes          No
DEC Mode 101    DECCANSM                       Conceal Answerback Message Mode                                          Yes          No
DEC Mode 102    DECNULM                        Ignore Null Mode                                                         Yes          No
DEC Mode 103    DECHDPXM                       Half Duplex Mode                                                         Yes          No
DEC Mode 104    DECESKM                        Secondary Keyboard Language Mode                                         Yes          No
DEC Mode 106    DECOSCNM                       Overscan Mode                                                            Yes          No
DEC Mode 108    DECNUMLK                       NumLock Mode                                                             Yes          No
DEC Mode 109    DECCAPSLK                      Caps Lock Mode                                                           Yes          No
DEC Mode 110    DECKLHIM                       Keyboard LEDs Host Indicator Mode                                        Yes          No
DEC Mode 111    DECFWM                         Framed Windows Mode                                                      Yes          No
DEC Mode 112    DECRPL                         Review Previous Lines Mode                                               Yes          No
DEC Mode 113    DECHWUM                        Host Wake-Up Mode                                                        Yes          No
DEC Mode 114    DECATCUM                       Alternate Text Color Underline Mode                                      Yes          No
DEC Mode 115    DECATCBM                       Alternate Text Color Blink Mode                                          Yes          No
DEC Mode 116    DECBBSM                        Bold and Blink Style Mode                                                Yes          No
DEC Mode 117    DECECM                         Erase Color Mode                                                         Yes          No
DEC Mode 1000   MOUSE_REPORT_CLICK             Send Mouse X & Y on button press                                         Yes          Yes
DEC Mode 1001   MOUSE_HILITE_TRACKING          Use Hilite Mouse Tracking                                                Yes          Yes
DEC Mode 1002   MOUSE_REPORT_DRAG              Use Cell Motion Mouse Tracking                                           Yes          Yes
DEC Mode 1003   MOUSE_ALL_MOTION               Use All Motion Mouse Tracking                                            Yes          Yes
DEC Mode 1004   FOCUS_IN_OUT_EVENTS            Send FocusIn/FocusOut events                                             Yes          Yes
DEC Mode 1005   MOUSE_EXTENDED_UTF8            Enable UTF-8 Mouse Mode                                                  Yes          No
DEC Mode 1006   MOUSE_EXTENDED_SGR             Enable SGR Mouse Mode                                                    Yes          Yes
DEC Mode 1007   ALT_SCROLL_XTERM               Enable Alternate Scroll Mode                                             Yes          Yes
DEC Mode 1010   SCROLL_ON_TTY_OUTPUT_RXVT      Scroll to bottom on tty output                                           Yes          No
DEC Mode 1011   SCROLL_ON_KEYPRESS_RXVT        Scroll to bottom on key press                                            Yes          No
DEC Mode 1014   FAST_SCROLL                    Enable fastScroll resource                                               Yes          No
DEC Mode 1015   MOUSE_URXVT                    Enable urxvt Mouse Mode                                                  Yes          No
DEC Mode 1016   MOUSE_SGR_PIXELS               Enable SGR Mouse PixelMode                                               Yes          No
DEC Mode 1021   BOLD_ITALIC_HIGH_INTENSITY     Bold/italic implies high intensity                                       Yes          No
DEC Mode 1034   META_SETS_EIGHTH_BIT           Interpret "meta" key                                                     Yes          No
DEC Mode 1035   MODIFIERS_ALT_NUMLOCK          Enable special modifiers for Alt and NumLock keys                        Yes          No
DEC Mode 1036   META_SENDS_ESC                 Send ESC when Meta modifies a key                                        Yes          Yes
DEC Mode 1037   KP_DELETE_SENDS_DEL            Send DEL from the editing-keypad Delete key                              Yes          No
DEC Mode 1039   ALT_SENDS_ESC                  Send ESC when Alt modifies a key                                         Yes          No
DEC Mode 1040   KEEP_SELECTION_NO_HILITE       Keep selection even if not highlighted                                   Yes          No
DEC Mode 1041   USE_CLIPBOARD_SELECTION        Use the CLIPBOARD selection                                              Yes          No
DEC Mode 1042   URGENCY_ON_CTRL_G              Enable Urgency window manager hint when Control-G is received            Yes          No
DEC Mode 1043   RAISE_ON_CTRL_G                Enable raising of the window when Control-G is received                  Yes          No
DEC Mode 1044   REUSE_CLIPBOARD_DATA           Reuse the most recent data copied to CLIPBOARD                           Yes          No
DEC Mode 1045   EXTENDED_REVERSE_WRAPAROUND    Extended Reverse-wraparound mode (XTREVWRAP2)                            No           No
DEC Mode 1046   ALT_SCREEN_BUFFER_SWITCH       Enable switching to/from Alternate Screen Buffer                         Yes          No
DEC Mode 1047   ALT_SCREEN_BUFFER_XTERM        Use Alternate Screen Buffer                                              Yes          Yes
DEC Mode 1048   SAVE_CURSOR_DECSC              Save cursor as in DECSC                                                  Yes          Yes
DEC Mode 1049   ALT_SCREEN_AND_SAVE_CLEAR      Save cursor as in DECSC and use alternate screen buffer                  Yes          Yes
DEC Mode 1050   TERMINFO_FUNC_KEY_MODE         Set terminfo/termcap function-key mode                                   Yes          No
DEC Mode 1051   SUN_FUNC_KEY_MODE              Set Sun function-key mode                                                Yes          No
DEC Mode 1052   HP_FUNC_KEY_MODE               Set HP function-key mode                                                 Yes          No
DEC Mode 1053   SCO_FUNC_KEY_MODE              Set SCO function-key mode                                                Yes          No
DEC Mode 1060   LEGACY_KBD_X11R6               Set legacy keyboard emulation, i.e, X11R6                                Yes          No
DEC Mode 1061   VT220_KBD_EMULATION            Set VT220 keyboard emulation                                             Yes          No
DEC Mode 1070   SIXEL_PRIVATE_PALETTE          Use private color registers for each graphic                             Yes          Yes
DEC Mode 1243   BIDI_ARROW_KEY_SWAPPING        Arrow keys swapping (BiDi)                                               Yes          Yes
DEC Mode 1337   ITERM2_REPORT_KEY_UP           Report Key Up                                                            No           No
DEC Mode 2001   READLINE_MOUSE_BUTTON_1        Enable readline mouse button-1                                           Yes          No
DEC Mode 2002   READLINE_MOUSE_BUTTON_2        Enable readline mouse button-2                                           Yes          No
DEC Mode 2003   READLINE_MOUSE_BUTTON_3        Enable readline mouse button-3                                           Yes          No
DEC Mode 2004   BRACKETED_PASTE                Set bracketed paste mode                                                 Yes          Yes
DEC Mode 2005   READLINE_CHARACTER_QUOTING     Enable readline character-quoting                                        Yes          No
DEC Mode 2006   READLINE_NEWLINE_PASTING       Enable readline newline pasting                                          Yes          No
DEC Mode 2026   SYNCHRONIZED_OUTPUT            Synchronized Output                                                      Yes          No
DEC Mode 2027   GRAPHEME_CLUSTERING            Grapheme Clustering                                                      No           No
DEC Mode 2028   TEXT_REFLOW                    Text reflow                                                              No           No
DEC Mode 2029   PASSIVE_MOUSE_TRACKING         Passive Mouse Tracking                                                   No           No
DEC Mode 2030   REPORT_GRID_CELL_SELECTION     Report grid cell selection                                               No           No
DEC Mode 2031   COLOR_PALETTE_UPDATES          Color palette updates                                                    No           No
DEC Mode 2048   IN_BAND_WINDOW_RESIZE          In-Band Window Resize Notifications                                      No           No
DEC Mode 2500   MIRROR_BOX_DRAWING             Mirror box drawing characters                                            Yes          Yes
DEC Mode 2501   BIDI_AUTODETECTION             BiDi autodetection                                                       Yes          Yes
DEC Mode 7700   AMBIGUOUS_WIDTH_REPORTING      Ambiguous width reporting                                                Yes          No
DEC Mode 7711   SCROLL_MARKERS                 Scroll markers (prompt start)                                            Yes          No
DEC Mode 7723   REWRAP_ON_RESIZE_MINTTY        Rewrap on resize                                                         No           No
DEC Mode 7727   APPLICATION_ESCAPE_KEY         Application escape key mode                                              Yes          No
DEC Mode 7728   ESC_KEY_SENDS_BACKSLASH        Send ^\ instead of the standard ^[ for the ESC key                       Yes          No
DEC Mode 7730   GRAPHICS_POSITION              Graphics position                                                        Yes          No
DEC Mode 7765   ALT_MODIFIED_MOUSEWHEEL        Alt-modified mousewheel mode                                             No           No
DEC Mode 7766   SHOW_HIDE_SCROLLBAR            Show/hide scrollbar                                                      Yes          No
DEC Mode 7767   FONT_CHANGE_REPORTING          Font change reporting                                                    Yes          No
DEC Mode 7780   GRAPHICS_POSITION_2            Graphics position                                                        No           No
DEC Mode 7783   SHORTCUT_KEY_MODE              Shortcut key mode                                                        Yes          No
DEC Mode 7786   MOUSEWHEEL_REPORTING           Mousewheel reporting                                                     Yes          No
DEC Mode 7787   APPLICATION_MOUSEWHEEL         Application mousewheel mode                                              Yes          No
DEC Mode 7796   BIDI_CURRENT_LINE              BiDi on current line                                                     Yes          No
DEC Mode 8200   TTCTH                          Terminal-to-Computer Talk-back Handler                                   No           No
DEC Mode 8452   SIXEL_SCROLLING_LEAVES_CURSOR  Sixel scrolling leaves cursor to right of graphic                        Yes          No
DEC Mode 8800   CHARACTER_MAPPING_SERVICE      enable/disable character mapping service                                 Yes          No
DEC Mode 8840   AMBIGUOUS_WIDTH_DOUBLE_WIDTH   Treat ambiguous width characters as double-width                         No           No
DEC Mode 9001   WIN32_INPUT_MODE               win32-input-mode                                                         No           No
DEC Mode 19997  KITTY_HANDLE_CTRL_C_Z          Handle Ctrl-C/Ctrl-Z mode                                                No           No
==============  =============================  =======================================================================  ===========  ============

**Summary**: 128 supported, 29 unsupported.

.. _GnomeTerminaltime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **2845.60 seconds** (2845s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
