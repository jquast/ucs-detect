.. _Konsole:

Konsole
-------


Tested Software version 23.08.5 on Linux
Full results available at ucs-detect_ repository path
`data/linux-konsole-23.08.5.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-konsole-23.08.5.yaml>`_

.. _Konsolescores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *Konsole*:

.. table::
   :class: sphinx-datatable

   ============  ===========  ==============  ======================================================
   Score Type    Raw Score    Scaled Score    Calculation
   ============  ===========  ==============  ======================================================
   WIDE          72.73%       58.9%           (version_index / total_versions) × (pct_success / 100)
   ZWJ           66.67%       88.9%           (version_index / total_versions) × (pct_success / 100)
   LANG          74.75%       56.2%           geometric_mean(language_percentages)
   VS16          100.00%      100.0%          pct_success / 100
   VS15          0.00%        0.0%            pct_success / 100
   DEC Modes     N/A          N/A             modes_changeable / total_modes
   TIME          39.97s       88.7%           1 - ((elapsed - min) / (max - min)) [inverse]
   ============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 62.83%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 73.1%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _Konsolewide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Konsole appears to be 
**15.0.0**, this is from a summary of the following
results:


.. table::
   :class: sphinx-datatable

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

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ======
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ======
     1  `U+00018DAB <https://codepoints.net/U+00018DAB>`_  '\\U00018dab'  Cn                  2  na
   ===  =================================================  =============  ==========  =========  ======

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x98\xb6\xab|\\n12|\\n"
        𘶫|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width 1.

.. _Konsolezwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Konsole* appears to be 
**15.1**, this is from a summary of the following
results:


.. table::
   :class: sphinx-datatable

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
   '17.0'             58        130  55.4%
   =========  ==========  =========  =============

Sequence of an Emoji ZWJ Sequence from Emoji Version 17.0, from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =================================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =================================
     1  `U+0001F469 <https://codepoints.net/U+0001F469>`_  '\\U0001f469'  So                  2  WOMAN
     2  `U+0001F3FD <https://codepoints.net/U+0001F3FD>`_  '\\U0001f3fd'  Sk                  0  EMOJI MODIFIER FITZPATRICK TYPE-4
     3  `U+200D <https://codepoints.net/U+200D>`_          '\\u200d'      Cf                  0  ZERO WIDTH JOINER
     4  `U+0001FAEF <https://codepoints.net/U+0001FAEF>`_  '\\U0001faef'  Cn                  2  na
     5  `U+200D <https://codepoints.net/U+200D>`_          '\\u200d'      Cf                  0  ZERO WIDTH JOINER
     6  `U+0001F469 <https://codepoints.net/U+0001F469>`_  '\\U0001f469'  So                  2  WOMAN
     7  `U+0001F3FC <https://codepoints.net/U+0001F3FC>`_  '\\U0001f3fc'  Sk                  0  EMOJI MODIFIER FITZPATRICK TYPE-3
   ===  =================================================  =============  ==========  =========  =================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9f\x91\xa9\xf0\x9f\x8f\xbd\xe2\x80\x8d\xf0\x9f\xab\xaf\xe2\x80\x8d\xf0\x9f\x91\xa9\xf0\x9f\x8f\xbc|\\n12|\\n"
        👩🏽‍🫯‍👩🏼|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width 3.

.. _Konsolevs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Konsole* is 0 errors
out of 213 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.

.. _Konsolevs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *Konsole* is 158 errors
out of 158 total codepoints tested, 0.0% success.
Sequence of a WIDE Emoji made NARROW by *Variation Selector-15*, from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =====================
     1  `U+0001F3AE <https://codepoints.net/U+0001F3AE>`_  '\\U0001f3ae'  So                  2  VIDEO GAME
     2  `U+FE0E <https://codepoints.net/U+FE0E>`_          '\\ufe0e'      Mn                  0  VARIATION SELECTOR-15
   ===  =================================================  =============  ==========  =========  =====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9f\x8e\xae\xef\xb8\x8e|\\n1|\\n"
        🎮︎|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Konsole* measures width 2.


.. _Konsolelang:

Language Support
++++++++++++++++

The following 3 languages were tested with 100% success:

Chinese, Hakka, Mongolian, Halh (Mongolian), Tagalog (Tagalog).

The following 116 languages are not fully supported:

.. table::
   :class: sphinx-datatable

   ==============================================================================  ==========  =========  =============
   lang                                                                              n_errors    n_total  pct_success
   ==============================================================================  ==========  =========  =============
   :ref:`Tamil (Sri Lanka) <KonsolelangTamilSriLanka>`                                   1000       1073  6.8%
   :ref:`Tamil <KonsolelangTamil>`                                                       1000       1074  6.9%
   :ref:`Sanskrit (Grantha) <KonsolelangSanskritGrantha>`                                 894       1006  11.1%
   :ref:`Malayalam <KonsolelangMalayalam>`                                               1000       1171  14.6%
   :ref:`Khmer, Central <KonsolelangKhmerCentral>`                                        449        528  15.0%
   :ref:`Bengali <KonsolelangBengali>`                                                   1000       1176  15.0%
   :ref:`Javanese (Javanese) <KonsolelangJavaneseJavanese>`                              1000       1182  15.4%
   :ref:`Kannada <KonsolelangKannada>`                                                    897       1080  16.9%
   :ref:`Khün <KonsolelangKhn>`                                                           355        442  19.7%
   :ref:`Sanskrit <KonsolelangSanskrit>`                                                  752       1000  24.8%
   :ref:`Tamang, Eastern <KonsolelangTamangEastern>`                                       33         45  26.7%
   :ref:`Marathi <KonsolelangMarathi>`                                                   1000       1419  29.5%
   :ref:`Burmese <KonsolelangBurmese>`                                                    836       1223  31.6%
   :ref:`Nepali <KonsolelangNepali>`                                                      935       1385  32.5%
   :ref:`Gujarati <KonsolelangGujarati>`                                                 1000       1516  34.0%
   :ref:`Mon <KonsolelangMon>`                                                            598        946  36.8%
   :ref:`Maithili <KonsolelangMaithili>`                                                  953       1519  37.3%
   :ref:`Telugu <KonsolelangTelugu>`                                                      702       1129  37.8%
   :ref:`Hindi <KonsolelangHindi>`                                                       1000       1623  38.4%
   :ref:`Shan <KonsolelangShan>`                                                          540        915  41.0%
   :ref:`Panjabi, Eastern <KonsolelangPanjabiEastern>`                                   1000       1825  45.2%
   :ref:`Sinhala <KonsolelangSinhala>`                                                    888       1655  46.3%
   :ref:`Bhojpuri <KonsolelangBhojpuri>`                                                  874       1737  49.7%
   :ref:`Magahi <KonsolelangMagahi>`                                                      805       1716  53.1%
   :ref:`Chakma <KonsolelangChakma>`                                                      499       1444  65.4%
   :ref:`Chinese, Mandarin (Nanjing) <KonsolelangChineseMandarinNanjing>`                   5        212  97.6%
   :ref:`Chinese, Mandarin (Tianjin) <KonsolelangChineseMandarinTianjin>`                   5        212  97.6%
   :ref:`Japanese <KonsolelangJapanese>`                                                    7        299  97.7%
   :ref:`Japanese (Osaka) <KonsolelangJapaneseOsaka>`                                       6        308  98.1%
   :ref:`Chinese, Mandarin (Traditional) <KonsolelangChineseMandarinTraditional>`           4        210  98.1%
   :ref:`Japanese (Tokyo) <KonsolelangJapaneseTokyo>`                                       6        320  98.1%
   :ref:`Thai <KonsolelangThai>`                                                            6        341  98.2%
   :ref:`Nuosu <KonsolelangNuosu>`                                                          4        230  98.3%
   :ref:`Vietnamese (Han nom) <KonsolelangVietnameseHannom>`                                3        199  98.5%
   :ref:`(Jinan) <KonsolelangJinan>`                                                        3        211  98.6%
   :ref:`Chinese, Mandarin (Guiyang) <KonsolelangChineseMandarinGuiyang>`                   3        211  98.6%
   :ref:`Chinese, Jinyu <KonsolelangChineseJinyu>`                                          3        212  98.6%
   :ref:`Chinese, Min Nan <KonsolelangChineseMinNan>`                                       3        212  98.6%
   :ref:`Lao <KonsolelangLao>`                                                              6        425  98.6%
   :ref:`Chinese, Mandarin (Simplified) <KonsolelangChineseMandarinSimplified>`             3        225  98.7%
   :ref:`Thai (2) <KonsolelangThai2>`                                                       4        313  98.7%
   :ref:`Chinese, Gan <KonsolelangChineseGan>`                                              2        211  99.1%
   :ref:`Chinese, Wu <KonsolelangChineseWu>`                                                2        211  99.1%
   :ref:`Chinese, Xiang <KonsolelangChineseXiang>`                                          2        212  99.1%
   :ref:`Chickasaw <KonsolelangChickasaw>`                                                  5        554  99.1%
   :ref:`Bora <KonsolelangBora>`                                                           14       1598  99.1%
   :ref:`Gumuz <KonsolelangGumuz>`                                                         10       1283  99.2%
   :ref:`Shipibo-Conibo <KonsolelangShipiboConibo>`                                        19       2540  99.3%
   :ref:`Nanai <KonsolelangNanai>`                                                          9       1207  99.3%
   :ref:`Orok <KonsolelangOrok>`                                                            9       1245  99.3%
   :ref:`Yaneshaʼ <KonsolelangYanesha>`                                                    18       2536  99.3%
   :ref:`Amarakaeri <KonsolelangAmarakaeri>`                                               10       1446  99.3%
   :ref:`Navajo <KonsolelangNavajo>`                                                       11       1600  99.3%
   :ref:`Veps <KonsolelangVeps>`                                                            9       1323  99.3%
   :ref:`Siona <KonsolelangSiona>`                                                         10       1492  99.3%
   :ref:`Evenki <KonsolelangEvenki>`                                                        6        899  99.3%
   :ref:`Gilyak <KonsolelangGilyak>`                                                       10       1504  99.3%
   :ref:`South Azerbaijani <KonsolelangSouthAzerbaijani>`                                   9       1396  99.4%
   :ref:`Secoya <KonsolelangSecoya>`                                                        9       1409  99.4%
   :ref:`Colorado <KonsolelangColorado>`                                                    8       1263  99.4%
   :ref:`Korean <KonsolelangKorean>`                                                        7       1185  99.4%
   :ref:`(Yeonbyeon) <KonsolelangYeonbyeon>`                                                6       1061  99.4%
   :ref:`Tem <KonsolelangTem>`                                                              9       1659  99.5%
   :ref:`Ticuna <KonsolelangTicuna>`                                                       11       2048  99.5%
   :ref:`Catalan (2) <KonsolelangCatalan2>`                                                10       1909  99.5%
   :ref:`Maldivian <KonsolelangMaldivian>`                                                 10       1918  99.5%
   :ref:`Arabic, Standard <KonsolelangArabicStandard>`                                      7       1348  99.5%
   :ref:`Mirandese <KonsolelangMirandese>`                                                 10       1966  99.5%
   :ref:`Yiddish, Eastern <KonsolelangYiddishEastern>`                                      9       1775  99.5%
   :ref:`Pular (Adlam) <KonsolelangPularAdlam>`                                             8       1613  99.5%
   :ref:`Kabyle <KonsolelangKabyle>`                                                        9       1815  99.5%
   :ref:`Lingala (tones) <KonsolelangLingalatones>`                                         9       1818  99.5%
   :ref:`Picard <KonsolelangPicard>`                                                       10       2024  99.5%
   :ref:`Tamazight, Central Atlas <KonsolelangTamazightCentralAtlas>`                       9       1822  99.5%
   :ref:`Éwé <Konsolelangw>`                                                               11       2230  99.5%
   :ref:`Fur <KonsolelangFur>`                                                              9       1838  99.5%
   :ref:`Chinese, Mandarin (Harbin) <KonsolelangChineseMandarinHarbin>`                     1        210  99.5%
   :ref:`Chinese, Yue <KonsolelangChineseYue>`                                              1        210  99.5%
   :ref:`Chinese, Mandarin (Beijing) <KonsolelangChineseMandarinBeijing>`                   1        212  99.5%
   :ref:`French (Welche) <KonsolelangFrenchWelche>`                                         9       1928  99.5%
   :ref:`Maori (2) <KonsolelangMaori2>`                                                    11       2385  99.5%
   :ref:`Saint Lucian Creole French <KonsolelangSaintLucianCreoleFrench>`                   8       1777  99.5%
   :ref:`Dendi <KonsolelangDendi>`                                                          7       1569  99.6%
   :ref:`Mazahua Central <KonsolelangMazahuaCentral>`                                       7       1574  99.6%
   :ref:`Ga <KonsolelangGa>`                                                                9       2039  99.6%
   :ref:`Farsi, Western <KonsolelangFarsiWestern>`                                          8       1822  99.6%
   :ref:`Mixtec, Metlatónoc <KonsolelangMixtecMetlatnoc>`                                   6       1367  99.6%
   :ref:`Aja <KonsolelangAja>`                                                              9       2061  99.6%
   :ref:`Gen <KonsolelangGen>`                                                             10       2309  99.6%
   :ref:`Uduk <KonsolelangUduk>`                                                           14       3247  99.6%
   :ref:`Assyrian Neo-Aramaic <KonsolelangAssyrianNeoAramaic>`                              5       1160  99.6%
   :ref:`Dari <KonsolelangDari>`                                                            8       1872  99.6%
   :ref:`Ditammari <KonsolelangDitammari>`                                                  8       1882  99.6%
   :ref:`Mòoré <KonsolelangMor>`                                                           10       2447  99.6%
   :ref:`Yoruba <KonsolelangYoruba>`                                                       10       2454  99.6%
   :ref:`Chinantec, Chiltepec <KonsolelangChinantecChiltepec>`                              7       1729  99.6%
   :ref:`Urdu <KonsolelangUrdu>`                                                            9       2237  99.6%
   :ref:`Pashto, Northern <KonsolelangPashtoNorthern>`                                      9       2242  99.6%
   :ref:`Seraiki <KonsolelangSeraiki>`                                                      9       2242  99.6%
   :ref:`Belanda Viri <KonsolelangBelandaViri>`                                             9       2246  99.6%
   :ref:`Waama <KonsolelangWaama>`                                                          4       1000  99.6%
   :ref:`Urdu (2) <KonsolelangUrdu2>`                                                       9       2251  99.6%
   :ref:`Vietnamese <KonsolelangVietnamese>`                                               10       2502  99.6%
   :ref:`Bamun <KonsolelangBamun>`                                                          9       2285  99.6%
   :ref:`Dinka, Northeastern <KonsolelangDinkaNortheastern>`                                6       1529  99.6%
   :ref:`Dagaare, Southern <KonsolelangDagaareSouthern>`                                   10       2582  99.6%
   :ref:`Otomi, Mezquital <KonsolelangOtomiMezquital>`                                      7       1849  99.6%
   :ref:`Serer-Sine <KonsolelangSererSine>`                                                 6       1596  99.6%
   :ref:`Panjabi, Western <KonsolelangPanjabiWestern>`                                      9       2419  99.6%
   :ref:`Baatonum <KonsolelangBaatonum>`                                                    7       1939  99.6%
   :ref:`Lamnso' <KonsolelangLamnso>`                                                       8       2237  99.6%
   :ref:`Fon <KonsolelangFon>`                                                              9       2520  99.6%
   :ref:`Dangme <KonsolelangDangme>`                                                        9       2912  99.7%
   :ref:`Tai Dam <KonsolelangTaiDam>`                                                       7       2386  99.7%
   :ref:`Tibetan, Central <KonsolelangTibetanCentral>`                                      9       3174  99.7%
   :ref:`Dzongkha <KonsolelangDzongkha>`                                                    8       3060  99.7%
   ==============================================================================  ==========  =========  =============

.. _KonsolelangTamilSriLanka:

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
     2  `U+0BA9 <https://codepoints.net/U+0BA9>`_  '\\u0ba9'  Lo                  1  TAMIL LETTER NNNA
     3  `U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
     4  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
        மனித|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangTamil:

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
     2  `U+0BA9 <https://codepoints.net/U+0BA9>`_  '\\u0ba9'  Lo                  1  TAMIL LETTER NNNA
     3  `U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
     4  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xae\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xa4|\\n123|\\n"
        மனித|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangSanskritGrantha:

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =====================
     1  `U+0001132E <https://codepoints.net/U+0001132E>`_  '\\U0001132e'  Lo                  1  GRANTHA LETTER MA
     2  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
     3  `U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
     4  `U+00011335 <https://codepoints.net/U+00011335>`_  '\\U00011335'  Lo                  1  GRANTHA LETTER VA
     5  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
     6  `U+00011327 <https://codepoints.net/U+00011327>`_  '\\U00011327'  Lo                  1  GRANTHA LETTER DHA
     7  `U+0001133F <https://codepoints.net/U+0001133F>`_  '\\U0001133f'  Mc                  0  GRANTHA VOWEL SIGN I
     8  `U+00011315 <https://codepoints.net/U+00011315>`_  '\\U00011315'  Lo                  1  GRANTHA LETTER KA
     9  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
    10  `U+00011330 <https://codepoints.net/U+00011330>`_  '\\U00011330'  Lo                  1  GRANTHA LETTER RA
    11  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
    12  `U+00011323 <https://codepoints.net/U+00011323>`_  '\\U00011323'  Lo                  1  GRANTHA LETTER NNA
    13  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
    14  `U+00011302 <https://codepoints.net/U+00011302>`_  '\\U00011302'  Mc                  0  GRANTHA SIGN ANUSVARA
   ===  =================================================  =============  ==========  =========  =====================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xae\xf0\x91\x8c\xbe\xf0\x91\x8c\xa8\xf0\x91\x8c\xb5\xf0\x91\x8c\xbe\xf0\x91\x8c\xa7\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x82|\\n1234567|\\n"
        𑌮𑌾𑌨𑌵𑌾𑌧𑌿𑌕𑌾𑌰𑌾𑌣𑌾𑌂|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Konsole* measures width 13.

.. _KonsolelangMalayalam:

Malayalam
^^^^^^^^^

Sequence of language *Malayalam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0D2E <https://codepoints.net/U+0D2E>`_  '\\u0d2e'  Lo                  1  MALAYALAM LETTER MA
     2  `U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
     3  `U+0D41 <https://codepoints.net/U+0D41>`_  '\\u0d41'  Mn                  0  MALAYALAM VOWEL SIGN U
     4  `U+0D37 <https://codepoints.net/U+0D37>`_  '\\u0d37'  Lo                  1  MALAYALAM LETTER SSA
     5  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
     6  `U+0D2F <https://codepoints.net/U+0D2F>`_  '\\u0d2f'  Lo                  1  MALAYALAM LETTER YA
     7  `U+0D3E <https://codepoints.net/U+0D3E>`_  '\\u0d3e'  Mc                  0  MALAYALAM VOWEL SIGN AA
     8  `U+0D35 <https://codepoints.net/U+0D35>`_  '\\u0d35'  Lo                  1  MALAYALAM LETTER VA
     9  `U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
    10  `U+0D3E <https://codepoints.net/U+0D3E>`_  '\\u0d3e'  Mc                  0  MALAYALAM VOWEL SIGN AA
    11  `U+0D36 <https://codepoints.net/U+0D36>`_  '\\u0d36'  Lo                  1  MALAYALAM LETTER SHA
    12  `U+0D19 <https://codepoints.net/U+0D19>`_  '\\u0d19'  Lo                  1  MALAYALAM LETTER NGA
    13  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
    14  `U+0D19 <https://codepoints.net/U+0D19>`_  '\\u0d19'  Lo                  1  MALAYALAM LETTER NGA
    15  `U+0D33 <https://codepoints.net/U+0D33>`_  '\\u0d33'  Lo                  1  MALAYALAM LETTER LLA
    16  `U+0D46 <https://codepoints.net/U+0D46>`_  '\\u0d46'  Mc                  0  MALAYALAM VOWEL SIGN E
    17  `U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
    18  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
    19  `U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
    20  `U+0D41 <https://codepoints.net/U+0D41>`_  '\\u0d41'  Mn                  0  MALAYALAM VOWEL SIGN U
    21  `U+0D31 <https://codepoints.net/U+0D31>`_  '\\u0d31'  Lo                  1  MALAYALAM LETTER RRA
    22  `U+0D3F <https://codepoints.net/U+0D3F>`_  '\\u0d3f'  Mc                  0  MALAYALAM VOWEL SIGN I
    23  `U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
    24  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
    25  `U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
    26  `U+0D41 <https://codepoints.net/U+0D41>`_  '\\u0d41'  Mn                  0  MALAYALAM VOWEL SIGN U
    27  `U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
    28  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
    29  `U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 29


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb4\xae\xe0\xb4\xa8\xe0\xb5\x81\xe0\xb4\xb7\xe0\xb5\x8d\xe0\xb4\xaf\xe0\xb4\xbe\xe0\xb4\xb5\xe0\xb4\x95\xe0\xb4\xbe\xe0\xb4\xb6\xe0\xb4\x99\xe0\xb5\x8d\xe0\xb4\x99\xe0\xb4\xb3\xe0\xb5\x86\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xb1\xe0\xb4\xbf\xe0\xb4\x95\xe0\xb5\x8d\xe0\xb4\x95\xe0\xb5\x81\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xa8|\\n12345678901234567|\\n"
        മനുഷ്യാവകാശങ്ങളെക്കുറിക്കുന്ന|
        12345678901234567|

- python `wcwidth.wcswidth()`_ measures width 17,
  while *Konsole* measures width 21.

.. _KonsolelangKhmerCentral:

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
     2  `U+17C1 <https://codepoints.net/U+17C1>`_  '\\u17c1'  Mc                  0  KHMER VOWEL SIGN E
     3  `U+1785 <https://codepoints.net/U+1785>`_  '\\u1785'  Lo                  1  KHMER LETTER CA
     4  `U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
     5  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
     6  `U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
     7  `U+17B8 <https://codepoints.net/U+17B8>`_  '\\u17b8'  Mn                  0  KHMER VOWEL SIGN II
     8  `U+1794 <https://codepoints.net/U+1794>`_  '\\u1794'  Lo                  1  KHMER LETTER BA
     9  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
    10  `U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
    11  `U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
    12  `U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
    13  `U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
    14  `U+1787 <https://codepoints.net/U+1787>`_  '\\u1787'  Lo                  1  KHMER LETTER CO
    15  `U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
    16  `U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
    17  `U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
    18  `U+179B <https://codepoints.net/U+179B>`_  '\\u179b'  Lo                  1  KHMER LETTER LO
    19  `U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
    20  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
    21  `U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
    22  `U+17B8 <https://codepoints.net/U+17B8>`_  '\\u17b8'  Mn                  0  KHMER VOWEL SIGN II
    23  `U+1796 <https://codepoints.net/U+1796>`_  '\\u1796'  Lo                  1  KHMER LETTER PO
    24  `U+17B8 <https://codepoints.net/U+17B8>`_  '\\u17b8'  Mn                  0  KHMER VOWEL SIGN II
    25  `U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
    26  `U+17B7 <https://codepoints.net/U+17B7>`_  '\\u17b7'  Mn                  0  KHMER VOWEL SIGN I
    27  `U+1791 <https://codepoints.net/U+1791>`_  '\\u1791'  Lo                  1  KHMER LETTER TO
    28  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
    29  `U+1792 <https://codepoints.net/U+1792>`_  '\\u1792'  Lo                  1  KHMER LETTER THO
    30  `U+17B7 <https://codepoints.net/U+17B7>`_  '\\u17b7'  Mn                  0  KHMER VOWEL SIGN I
    31  `U+1798 <https://codepoints.net/U+1798>`_  '\\u1798'  Lo                  1  KHMER LETTER MO
    32  `U+1793 <https://codepoints.net/U+1793>`_  '\\u1793'  Lo                  1  KHMER LETTER NO
    33  `U+17BB <https://codepoints.net/U+17BB>`_  '\\u17bb'  Mn                  0  KHMER VOWEL SIGN U
    34  `U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
    35  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
    36  `U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 36


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x9f\xe1\x9f\x81\xe1\x9e\x85\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x80\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x9f\xe1\x9e\x80\xe1\x9e\x9b\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8\xe1\x9e\x96\xe1\x9e\xb8\xe1\x9e\x9f\xe1\x9e\xb7\xe1\x9e\x91\xe1\x9f\x92\xe1\x9e\x92\xe1\x9e\xb7\xe1\x9e\x98\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x9f|\\n1234567890123456789012|\\n"
        សេចក្ដីប្រកាសជាសកលស្ដីពីសិទ្ធិមនុស្ស|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *Konsole* measures width 25.

.. _KonsolelangBengali:

Bengali
^^^^^^^

Sequence of language *Bengali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+09AE <https://codepoints.net/U+09AE>`_  '\\u09ae'  Lo                  1  BENGALI LETTER MA
     2  `U+09BE <https://codepoints.net/U+09BE>`_  '\\u09be'  Mc                  0  BENGALI VOWEL SIGN AA
     3  `U+09A8 <https://codepoints.net/U+09A8>`_  '\\u09a8'  Lo                  1  BENGALI LETTER NA
     4  `U+09AC <https://codepoints.net/U+09AC>`_  '\\u09ac'  Lo                  1  BENGALI LETTER BA
     5  `U+09BE <https://codepoints.net/U+09BE>`_  '\\u09be'  Mc                  0  BENGALI VOWEL SIGN AA
     6  `U+09A7 <https://codepoints.net/U+09A7>`_  '\\u09a7'  Lo                  1  BENGALI LETTER DHA
     7  `U+09BF <https://codepoints.net/U+09BF>`_  '\\u09bf'  Mc                  0  BENGALI VOWEL SIGN I
     8  `U+0995 <https://codepoints.net/U+0995>`_  '\\u0995'  Lo                  1  BENGALI LETTER KA
     9  `U+09BE <https://codepoints.net/U+09BE>`_  '\\u09be'  Mc                  0  BENGALI VOWEL SIGN AA
    10  `U+09B0 <https://codepoints.net/U+09B0>`_  '\\u09b0'  Lo                  1  BENGALI LETTER RA
    11  `U+09C7 <https://codepoints.net/U+09C7>`_  '\\u09c7'  Mc                  0  BENGALI VOWEL SIGN E
    12  `U+09B0 <https://codepoints.net/U+09B0>`_  '\\u09b0'  Lo                  1  BENGALI LETTER RA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\xae\xe0\xa6\xbe\xe0\xa6\xa8\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\xa7\xe0\xa6\xbf\xe0\xa6\x95\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x87\xe0\xa6\xb0|\\n1234567|\\n"
        মানবাধিকারের|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Konsole* measures width 12.

.. _KonsolelangJavaneseJavanese:

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+A9B2 <https://codepoints.net/U+A9B2>`_  '\\ua9b2'  Lo                  1  JAVANESE LETTER HA
     2  `U+A9B8 <https://codepoints.net/U+A9B8>`_  '\\ua9b8'  Mn                  0  JAVANESE VOWEL SIGN SUKU
     3  `U+A9A9 <https://codepoints.net/U+A9A9>`_  '\\ua9a9'  Lo                  1  JAVANESE LETTER MA
     4  `U+A9A0 <https://codepoints.net/U+A9A0>`_  '\\ua9a0'  Lo                  1  JAVANESE LETTER TA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xa0|\\n123|\\n"
        ꦲꦸꦩꦠ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangKannada:

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0CAE <https://codepoints.net/U+0CAE>`_  '\\u0cae'  Lo                  1  KANNADA LETTER MA
     2  `U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
     3  `U+0CA8 <https://codepoints.net/U+0CA8>`_  '\\u0ca8'  Lo                  1  KANNADA LETTER NA
     4  `U+0CB5 <https://codepoints.net/U+0CB5>`_  '\\u0cb5'  Lo                  1  KANNADA LETTER VA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xa8\xe0\xb2\xb5|\\n123|\\n"
        ಮಾನವ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangKhn:

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
     2  `U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
     3  `U+1A65 <https://codepoints.net/U+1A65>`_  '\\u1a65'  Mn                  0  TAI THAM VOWEL SIGN I
     4  `U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
     5  `U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
     6  `U+1A45 <https://codepoints.net/U+1A45>`_  '\\u1a45'  Lo                  1  TAI THAM LETTER WA
     7  `U+1A64 <https://codepoints.net/U+1A64>`_  '\\u1a64'  Mc                  0  TAI THAM VOWEL SIGN TALL AA
     8  `U+1A75 <https://codepoints.net/U+1A75>`_  '\\u1a75'  Mn                  0  TAI THAM SIGN TONE-1
     9  `U+1A2F <https://codepoints.net/U+1A2F>`_  '\\u1a2f'  Lo                  1  TAI THAM LETTER DA
    10  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    11  `U+1A45 <https://codepoints.net/U+1A45>`_  '\\u1a45'  Lo                  1  TAI THAM LETTER WA
    12  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    13  `U+1A3F <https://codepoints.net/U+1A3F>`_  '\\u1a3f'  Lo                  1  TAI THAM LETTER LOW YA
    14  `U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
    15  `U+1A3E <https://codepoints.net/U+1A3E>`_  '\\u1a3e'  Lo                  1  TAI THAM LETTER MA
    16  `U+1A36 <https://codepoints.net/U+1A36>`_  '\\u1a36'  Lo                  1  TAI THAM LETTER NA
    17  `U+1A69 <https://codepoints.net/U+1A69>`_  '\\u1a69'  Mn                  0  TAI THAM VOWEL SIGN U
    18  `U+1A54 <https://codepoints.net/U+1A54>`_  '\\u1a54'  Lo                  1  TAI THAM LETTER GREAT SA
    19  `U+1A29 <https://codepoints.net/U+1A29>`_  '\\u1a29'  Lo                  1  TAI THAM LETTER LOW CA
    20  `U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
    21  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    22  `U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 22


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\x85\xe1\xa9\xa4\xe1\xa9\xb5\xe1\xa8\xaf\xe1\xa9\xa0\xe1\xa9\x85\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa9\xa2\xe1\xa8\xbe\xe1\xa8\xb6\xe1\xa9\xa9\xe1\xa9\x94\xe1\xa8\xa9\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb2|\\n123456789012|\\n"
        ᨠᨲᩥᨠᩣᩅᩤ᩵ᨯ᩠ᩅ᩠ᨿᩢᨾᨶᩩᩔᨩᩣ᩠ᨲ|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *Konsole* measures width 15.

.. _KonsolelangSanskrit:

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     3  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     4  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     5  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     6  `U+0927 <https://codepoints.net/U+0927>`_  '\\u0927'  Lo                  1  DEVANAGARI LETTER DHA
     7  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
     8  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     9  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    10  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
    11  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    12  `U+0923 <https://codepoints.net/U+0923>`_  '\\u0923'  Lo                  1  DEVANAGARI LETTER NNA
    13  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    14  `U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa7\xe0\xa4\xbf\xe0\xa4\x95\xe0\xa4\xbe\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xa3\xe0\xa4\xbe\xe0\xa4\x82|\\n1234567|\\n"
        मानवाधिकाराणां|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Konsole* measures width 13.

.. _KonsolelangTamangEastern:

Tamang, Eastern
^^^^^^^^^^^^^^^

Sequence of language *Tamang, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     2  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     3  `U+0939 <https://codepoints.net/U+0939>`_  '\\u0939'  Lo                  1  DEVANAGARI LETTER HA
     4  `U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
     5  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     6  `U+0947 <https://codepoints.net/U+0947>`_  '\\u0947'  Mn                  0  DEVANAGARI VOWEL SIGN E
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa5\x8d\xe0\xa4\xb9\xe0\xa5\x80\xe0\xa4\xb8\xe0\xa5\x87|\\n123|\\n"
        म्हीसे|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangMarathi:

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     3  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     4  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     5  `U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa5\x80|\\n123|\\n"
        मानवी|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 5.

.. _KonsolelangBurmese:

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
     2  `U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
     3  `U+103C <https://codepoints.net/U+103C>`_  '\\u103c'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL RA
     4  `U+100A <https://codepoints.net/U+100A>`_  '\\u100a'  Lo                  1  MYANMAR LETTER NNYA
     5  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
     6  `U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
     7  `U+103C <https://codepoints.net/U+103C>`_  '\\u103c'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL RA
     8  `U+100A <https://codepoints.net/U+100A>`_  '\\u100a'  Lo                  1  MYANMAR LETTER NNYA
     9  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    10  `U+1006 <https://codepoints.net/U+1006>`_  '\\u1006'  Lo                  1  MYANMAR LETTER CHA
    11  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
    12  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
    13  `U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
    14  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    15  `U+101B <https://codepoints.net/U+101B>`_  '\\u101b'  Lo                  1  MYANMAR LETTER RA
    16  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\xa1\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x95\xe1\x80\xbc\xe1\x80\x8a\xe1\x80\xba\xe1\x80\x86\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x84\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xac|\\n12345678|\\n"
        အပြည်ပြည်ဆိုင်ရာ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Konsole* measures width 11.

.. _KonsolelangNepali:

Nepali
^^^^^^

Sequence of language *Nepali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     3  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     4  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
        मानव|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangGujarati:

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0AAE <https://codepoints.net/U+0AAE>`_  '\\u0aae'  Lo                  1  GUJARATI LETTER MA
     2  `U+0ABE <https://codepoints.net/U+0ABE>`_  '\\u0abe'  Mc                  0  GUJARATI VOWEL SIGN AA
     3  `U+0AA8 <https://codepoints.net/U+0AA8>`_  '\\u0aa8'  Lo                  1  GUJARATI LETTER NA
     4  `U+0AB5 <https://codepoints.net/U+0AB5>`_  '\\u0ab5'  Lo                  1  GUJARATI LETTER VA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xa8\xe0\xaa\xb5|\\n123|\\n"
        માનવ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangMon:

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
     2  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
     3  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
     4  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
     5  `U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
     6  `U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
     7  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
     8  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
     9  `U+105A <https://codepoints.net/U+105A>`_  '\\u105a'  Lo                  1  MYANMAR LETTER MON NGA
    10  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x9c\xe1\x80\xad\xe1\x80\x80\xe1\x80\xba\xe1\x80\x9c\xe1\x80\x9c\xe1\x80\xb1\xe1\x80\xac\xe1\x81\x9a\xe1\x80\xba|\\n12345|\\n"
        လိက်လလောၚ်|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Konsole* measures width 6.

.. _KonsolelangMaithili:

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     3  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
     4  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     5  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     6  `U+092D <https://codepoints.net/U+092D>`_  '\\u092d'  Lo                  1  DEVANAGARI LETTER BHA
     7  `U+094C <https://codepoints.net/U+094C>`_  '\\u094c'  Mc                  0  DEVANAGARI VOWEL SIGN AU
     8  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa4\xbe\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xb5\xe0\xa4\xad\xe0\xa5\x8c\xe0\xa4\xae|\\n12345|\\n"
        सार्वभौम|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Konsole* measures width 7.

.. _KonsolelangTelugu:

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0C2E <https://codepoints.net/U+0C2E>`_  '\\u0c2e'  Lo                  1  TELUGU LETTER MA
     2  `U+0C3E <https://codepoints.net/U+0C3E>`_  '\\u0c3e'  Mn                  0  TELUGU VOWEL SIGN AA
     3  `U+0C28 <https://codepoints.net/U+0C28>`_  '\\u0c28'  Lo                  1  TELUGU LETTER NA
     4  `U+0C35 <https://codepoints.net/U+0C35>`_  '\\u0c35'  Lo                  1  TELUGU LETTER VA
     5  `U+0C38 <https://codepoints.net/U+0C38>`_  '\\u0c38'  Lo                  1  TELUGU LETTER SA
     6  `U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
     7  `U+0C35 <https://codepoints.net/U+0C35>`_  '\\u0c35'  Lo                  1  TELUGU LETTER VA
     8  `U+0C24 <https://codepoints.net/U+0C24>`_  '\\u0c24'  Lo                  1  TELUGU LETTER TA
     9  `U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
    10  `U+0C35 <https://codepoints.net/U+0C35>`_  '\\u0c35'  Lo                  1  TELUGU LETTER VA
    11  `U+0C2E <https://codepoints.net/U+0C2E>`_  '\\u0c2e'  Lo                  1  TELUGU LETTER MA
    12  `U+0C41 <https://codepoints.net/U+0C41>`_  '\\u0c41'  Mc                  0  TELUGU VOWEL SIGN U
    13  `U+0C32 <https://codepoints.net/U+0C32>`_  '\\u0c32'  Lo                  1  TELUGU LETTER LA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8\xe0\xb0\xb5\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xa4\xe0\xb1\x8d\xe0\xb0\xb5\xe0\xb0\xae\xe0\xb1\x81\xe0\xb0\xb2|\\n123456789|\\n"
        మానవస్వత్వముల|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Konsole* measures width 10.

.. _KonsolelangHindi:

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     3  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     4  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5|\\n123|\\n"
        मानव|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangShan:

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
     2  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
     3  `U+1075 <https://codepoints.net/U+1075>`_  '\\u1075'  Lo                  1  MYANMAR LETTER SHAN KA
     4  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
     5  `U+1088 <https://codepoints.net/U+1088>`_  '\\u1088'  Mc                  0  MYANMAR SIGN SHAN TONE-3
     6  `U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
     7  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
     8  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
     9  `U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
    10  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    11  `U+107D <https://codepoints.net/U+107D>`_  '\\u107d'  Lo                  1  MYANMAR LETTER SHAN PHA
    12  `U+1062 <https://codepoints.net/U+1062>`_  '\\u1062'  Mc                  0  MYANMAR VOWEL SIGN SGAW KAREN EU
    13  `U+101D <https://codepoints.net/U+101D>`_  '\\u101d'  Lo                  1  MYANMAR LETTER WA
    14  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    15  `U+1087 <https://codepoints.net/U+1087>`_  '\\u1087'  Mc                  0  MYANMAR SIGN SHAN TONE-2
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 15


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x9c\xe1\x80\xad\xe1\x81\xb5\xe1\x80\xba\xe1\x82\x88\xe1\x80\x95\xe1\x80\xad\xe1\x80\xaf\xe1\x81\xbc\xe1\x80\xba\xe1\x81\xbd\xe1\x81\xa2\xe1\x80\x9d\xe1\x80\xba\xe1\x82\x87|\\n123456|\\n"
        လိၵ်ႈပိုၼ်ၽၢဝ်ႇ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width 7.

.. _KonsolelangPanjabiEastern:

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0A2E <https://codepoints.net/U+0A2E>`_  '\\u0a2e'  Lo                  1  GURMUKHI LETTER MA
     2  `U+0A28 <https://codepoints.net/U+0A28>`_  '\\u0a28'  Lo                  1  GURMUKHI LETTER NA
     3  `U+0A41 <https://codepoints.net/U+0A41>`_  '\\u0a41'  Mn                  0  GURMUKHI VOWEL SIGN U
     4  `U+0A71 <https://codepoints.net/U+0A71>`_  '\\u0a71'  Mn                  0  GURMUKHI ADDAK
     5  `U+0A16 <https://codepoints.net/U+0A16>`_  '\\u0a16'  Lo                  1  GURMUKHI LETTER KHA
     6  `U+0A40 <https://codepoints.net/U+0A40>`_  '\\u0a40'  Mc                  0  GURMUKHI VOWEL SIGN II
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\xae\xe0\xa8\xa8\xe0\xa9\x81\xe0\xa9\xb1\xe0\xa8\x96\xe0\xa9\x80|\\n123|\\n"
        ਮਨੁੱਖੀ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangSinhala:

Sinhala
^^^^^^^

Sequence of language *Sinhala* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================
     1  `U+0DB8 <https://codepoints.net/U+0DB8>`_  '\\u0db8'  Lo                  1  SINHALA LETTER MAYANNA
     2  `U+0DCF <https://codepoints.net/U+0DCF>`_  '\\u0dcf'  Mc                  0  SINHALA VOWEL SIGN AELA-PILLA
     3  `U+0DB1 <https://codepoints.net/U+0DB1>`_  '\\u0db1'  Lo                  1  SINHALA LETTER DANTAJA NAYANNA
     4  `U+0DC0 <https://codepoints.net/U+0DC0>`_  '\\u0dc0'  Lo                  1  SINHALA LETTER VAYANNA
   ===  =========================================  =========  ==========  =========  ==============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb6\xb8\xe0\xb7\x8f\xe0\xb6\xb1\xe0\xb7\x80|\\n123|\\n"
        මානව|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 4.

.. _KonsolelangBhojpuri:

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     3  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     4  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     5  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     6  `U+0927 <https://codepoints.net/U+0927>`_  '\\u0927'  Lo                  1  DEVANAGARI LETTER DHA
     7  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
     8  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     9  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    10  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa7\xe0\xa4\xbf\xe0\xa4\x95\xe0\xa4\xbe\xe0\xa4\xb0|\\n123456|\\n"
        मानवाधिकार|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width 10.

.. _KonsolelangMagahi:

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     3  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     4  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     5  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     6  `U+0927 <https://codepoints.net/U+0927>`_  '\\u0927'  Lo                  1  DEVANAGARI LETTER DHA
     7  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
     8  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     9  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    10  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa7\xe0\xa4\xbf\xe0\xa4\x95\xe0\xa4\xbe\xe0\xa4\xb0|\\n123456|\\n"
        मानवाधिकार|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width 10.

.. _KonsolelangChakma:

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ====================
     1  `U+0001111F <https://codepoints.net/U+0001111F>`_  '\\U0001111f'  Lo                  1  CHAKMA LETTER MAA
     2  `U+0001111A <https://codepoints.net/U+0001111A>`_  '\\U0001111a'  Lo                  1  CHAKMA LETTER NAA
     3  `U+0001112C <https://codepoints.net/U+0001112C>`_  '\\U0001112c'  Mc                  0  CHAKMA VOWEL SIGN E
     4  `U+0001112D <https://codepoints.net/U+0001112D>`_  '\\U0001112d'  Mn                  0  CHAKMA VOWEL SIGN AI
     5  `U+00011103 <https://codepoints.net/U+00011103>`_  '\\U00011103'  Lo                  1  CHAKMA LETTER AA
     6  `U+00011107 <https://codepoints.net/U+00011107>`_  '\\U00011107'  Lo                  1  CHAKMA LETTER KAA
     7  `U+00011134 <https://codepoints.net/U+00011134>`_  '\\U00011134'  Mn                  0  CHAKMA MAAYYAA
     8  `U+00011107 <https://codepoints.net/U+00011107>`_  '\\U00011107'  Lo                  1  CHAKMA LETTER KAA
     9  `U+00011125 <https://codepoints.net/U+00011125>`_  '\\U00011125'  Lo                  1  CHAKMA LETTER SAA
    10  `U+00011127 <https://codepoints.net/U+00011127>`_  '\\U00011127'  Mn                  0  CHAKMA VOWEL SIGN A
    11  `U+00011101 <https://codepoints.net/U+00011101>`_  '\\U00011101'  Mn                  0  CHAKMA SIGN ANUSVARA
    12  `U+00011122 <https://codepoints.net/U+00011122>`_  '\\U00011122'  Lo                  1  CHAKMA LETTER RAA
    13  `U+00011134 <https://codepoints.net/U+00011134>`_  '\\U00011134'  Mn                  0  CHAKMA MAAYYAA
   ===  =================================================  =============  ==========  =========  ====================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\x9f\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xad\xf0\x91\x84\x83\xf0\x91\x84\x87\xf0\x91\x84\xb4\xf0\x91\x84\x87\xf0\x91\x84\xa5\xf0\x91\x84\xa7\xf0\x91\x84\x81\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234567|\\n"
        𑄟𑄚𑄬𑄭𑄃𑄇𑄴𑄇𑄥𑄧𑄁𑄢𑄴|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Konsole* measures width 8.

.. _KonsolelangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
     2  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     3  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     4  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
     5  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
     6  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     7  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
     8  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     9  `U+5E73 <https://codepoints.net/U+5E73>`_  '\\u5e73'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E73
    10  `U+7B49 <https://codepoints.net/U+7B49>`_  '\\u7b49'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B49
    11  `U+4FDD <https://codepoints.net/U+4FDD>`_  '\\u4fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FDD
    12  `U+62A4 <https://codepoints.net/U+62A4>`_  '\\u62a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-62A4
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe6\x9c\x89\xe6\x9d\x83\xe4\xba\xab\xe5\x8f\x97\xe6\xb3\x95\xe5\xbe\x8b\xe7\x9a\x84\xe5\xb9\xb3\xe7\xad\x89\xe4\xbf\x9d\xe6\x8a\xa4|\\n123456789012345678901234|\\n"
        并有权享受法律的平等保护|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *Konsole* measures width 6.

.. _KonsolelangChineseMandarinTianjin:

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     2  `U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
     3  `U+9876 <https://codepoints.net/U+9876>`_  '\\u9876'  Lo                  2  CJK UNIFIED IDEOGRAPH-9876
     4  `U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
     5  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     6  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     7  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
     8  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
     9  `U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
    10  `U+8FB9 <https://codepoints.net/U+8FB9>`_  '\\u8fb9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FB9
    11  `U+513F <https://codepoints.net/U+513F>`_  '\\u513f'  Lo                  2  CJK UNIFIED IDEOGRAPH-513F
    12  `U+5927 <https://codepoints.net/U+5927>`_  '\\u5927'  Lo                  2  CJK UNIFIED IDEOGRAPH-5927
    13  `U+4FDD <https://codepoints.net/U+4FDD>`_  '\\u4fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FDD
    14  `U+62A4 <https://codepoints.net/U+62A4>`_  '\\u62a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-62A4
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xba\xba\xe4\xb8\xaa\xe9\xa1\xb6\xe4\xb8\xaa\xe6\x9c\x89\xe6\x9d\x83\xe4\xba\xab\xe5\x8f\x97\xe4\xb8\x80\xe8\xbe\xb9\xe5\x84\xbf\xe5\xa4\xa7\xe4\xbf\x9d\xe6\x8a\xa4|\\n1234567890123456789012345678|\\n"
        人个顶个有权享受一边儿大保护|
        1234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 28,
  while *Konsole* measures width 16.

.. _KonsolelangJapanese:

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+793E <https://codepoints.net/U+793E>`_  '\\u793e'  Lo                  2  CJK UNIFIED IDEOGRAPH-793E
     2  `U+4F1A <https://codepoints.net/U+4F1A>`_  '\\u4f1a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F1A
     3  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     4  `U+5404 <https://codepoints.net/U+5404>`_  '\\u5404'  Lo                  2  CJK UNIFIED IDEOGRAPH-5404
     5  `U+500B <https://codepoints.net/U+500B>`_  '\\u500b'  Lo                  2  CJK UNIFIED IDEOGRAPH-500B
     6  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     7  `U+53CA <https://codepoints.net/U+53CA>`_  '\\u53ca'  Lo                  2  CJK UNIFIED IDEOGRAPH-53CA
     8  `U+3073 <https://codepoints.net/U+3073>`_  '\\u3073'  Lo                  2  HIRAGANA LETTER BI
     9  `U+5404 <https://codepoints.net/U+5404>`_  '\\u5404'  Lo                  2  CJK UNIFIED IDEOGRAPH-5404
    10  `U+6A5F <https://codepoints.net/U+6A5F>`_  '\\u6a5f'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A5F
    11  `U+95A2 <https://codepoints.net/U+95A2>`_  '\\u95a2'  Lo                  2  CJK UNIFIED IDEOGRAPH-95A2
    12  `U+304C <https://codepoints.net/U+304C>`_  '\\u304c'  Lo                  2  HIRAGANA LETTER GA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xa4\xbe\xe4\xbc\x9a\xe3\x81\xae\xe5\x90\x84\xe5\x80\x8b\xe4\xba\xba\xe5\x8f\x8a\xe3\x81\xb3\xe5\x90\x84\xe6\xa9\x9f\xe9\x96\xa2\xe3\x81\x8c|\\n123456789012345678901234|\\n"
        社会の各個人及び各機関が|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *Konsole* measures width 12.

.. _KonsolelangJapaneseOsaka:

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+3088 <https://codepoints.net/U+3088>`_  '\\u3088'  Lo                  2  HIRAGANA LETTER YO
     2  `U+3063 <https://codepoints.net/U+3063>`_  '\\u3063'  Lo                  2  HIRAGANA LETTER SMALL TU
     3  `U+3066 <https://codepoints.net/U+3066>`_  '\\u3066'  Lo                  2  HIRAGANA LETTER TE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x82\x88\xe3\x81\xa3\xe3\x81\xa6|\\n123456|\\n"
        よって|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width -38.

.. _KonsolelangChineseMandarinTraditional:

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E5D <https://codepoints.net/U+4E5D>`_  '\\u4e5d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5D
     3  `U+689D <https://codepoints.net/U+689D>`_  '\\u689d'  Lo                  2  CJK UNIFIED IDEOGRAPH-689D
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb9\x9d\xe6\xa2\x9d|\\n123456|\\n"
        第九條|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width -40.

.. _KonsolelangJapaneseTokyo:

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+52A0 <https://codepoints.net/U+52A0>`_  '\\u52a0'  Lo                  2  CJK UNIFIED IDEOGRAPH-52A0
     2  `U+76DF <https://codepoints.net/U+76DF>`_  '\\u76df'  Lo                  2  CJK UNIFIED IDEOGRAPH-76DF
     3  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     4  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     5  `U+8EAB <https://codepoints.net/U+8EAB>`_  '\\u8eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-8EAB
     6  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     7  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     8  `U+6C11 <https://codepoints.net/U+6C11>`_  '\\u6c11'  Lo                  2  CJK UNIFIED IDEOGRAPH-6C11
     9  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
    10  `U+9593 <https://codepoints.net/U+9593>`_  '\\u9593'  Lo                  2  CJK UNIFIED IDEOGRAPH-9593
    11  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
    12  `U+3082 <https://codepoints.net/U+3082>`_  '\\u3082'  Lo                  2  HIRAGANA LETTER MO
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8a\xa0\xe7\x9b\x9f\xe5\x9b\xbd\xe8\x87\xaa\xe8\xba\xab\xe3\x81\xae\xe4\xba\xba\xe6\xb0\x91\xe3\x81\xae\xe9\x96\x93\xe3\x81\xab\xe3\x82\x82|\\n123456789012345678901234|\\n"
        加盟国自身の人民の間にも|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *Konsole* measures width -14.

.. _KonsolelangThai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================
     1  `U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
     2  `U+0E1E <https://codepoints.net/U+0E1E>`_  '\\u0e1e'  Lo                  1  THAI CHARACTER PHO PHAN
     3  `U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
     4  `U+0E48 <https://codepoints.net/U+0E48>`_  '\\u0e48'  Mn                  0  THAI CHARACTER MAI EK
     5  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
     6  `U+0E43 <https://codepoints.net/U+0E43>`_  '\\u0e43'  Lo                  1  THAI CHARACTER SARA AI MAIMUAN
     7  `U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
     8  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
     9  `U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
    10  `U+0E0F <https://codepoints.net/U+0E0F>`_  '\\u0e0f'  Lo                  1  THAI CHARACTER TO PATAK
    11  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    12  `U+0E0D <https://codepoints.net/U+0E0D>`_  '\\u0e0d'  Lo                  1  THAI CHARACTER YO YING
    13  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    14  `U+0E13 <https://codepoints.net/U+0E13>`_  '\\u0e13'  Lo                  1  THAI CHARACTER NO NEN
    15  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    16  `U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
    17  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
    18  `U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
    19  `U+0E33 <https://codepoints.net/U+0E33>`_  '\\u0e33'  Lo                  1  THAI CHARACTER SARA AM
    20  `U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
    21  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    22  `U+0E47 <https://codepoints.net/U+0E47>`_  '\\u0e47'  Mn                  0  THAI CHARACTER MAITAIKHU
    23  `U+0E08 <https://codepoints.net/U+0E08>`_  '\\u0e08'  Lo                  1  THAI CHARACTER CHO CHAN
    24  `U+0E1C <https://codepoints.net/U+0E1C>`_  '\\u0e1c'  Lo                  1  THAI CHARACTER PHO PHUNG
    25  `U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
    26  `U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
    27  `U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
    28  `U+0E47 <https://codepoints.net/U+0E47>`_  '\\u0e47'  Mn                  0  THAI CHARACTER MAITAIKHU
    29  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
    30  `U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
    31  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    32  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    33  `U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
    34  `U+0E39 <https://codepoints.net/U+0E39>`_  '\\u0e39'  Mn                  0  THAI CHARACTER SARA UU
    35  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    36  `U+0E13 <https://codepoints.net/U+0E13>`_  '\\u0e13'  Lo                  1  THAI CHARACTER NO NEN
    37  `U+0E4C <https://codepoints.net/U+0E4C>`_  '\\u0e4c'  Mn                  0  THAI CHARACTER THANTHAKHAT
    38  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ==============================

Total codepoints: 38


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x80\xe0\xb8\x9e\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\xad\xe0\xb9\x83\xe0\xb8\xab\xe0\xb9\x89\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\x93\xe0\xb8\x99\xe0\xb8\xb5\xe0\xb9\x89\xe0\xb8\xaa\xe0\xb8\xb3\xe0\xb9\x80\xe0\xb8\xa3\xe0\xb9\x87\xe0\xb8\x88\xe0\xb8\x9c\xe0\xb8\xa5\xe0\xb9\x80\xe0\xb8\x95\xe0\xb9\x87\xe0\xb8\xa1\xe0\xb8\x9a\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x9a\xe0\xb8\xb9\xe0\xb8\xa3\xe0\xb8\x93\xe0\xb9\x8c.|\\n123456789012345678901234567|\\n"
        เพื่อให้ปฏิญาณนี้สำเร็จผลเต็มบริบูรณ์.|
        123456789012345678901234567|

- python `wcwidth.wcswidth()`_ measures width 27,
  while *Konsole* measures width -2.

.. _KonsolelangNuosu:

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============
     1  `U+A26C <https://codepoints.net/U+A26C>`_  '\\ua26c'  Lo                  2  YI SYLLABLE NGE
     2  `U+A1EE <https://codepoints.net/U+A1EE>`_  '\\ua1ee'  Lo                  2  YI SYLLABLE GET
     3  `U+A0C5 <https://codepoints.net/U+A0C5>`_  '\\ua0c5'  Lo                  2  YI SYLLABLE MU
     4  `U+A3E2 <https://codepoints.net/U+A3E2>`_  '\\ua3e2'  Lo                  2  YI SYLLABLE JI
     5  `U+A1C8 <https://codepoints.net/U+A1C8>`_  '\\ua1c8'  Lo                  2  YI SYLLABLE LOX
     6  `U+A109 <https://codepoints.net/U+A109>`_  '\\ua109'  Lo                  2  YI SYLLABLE DA
     7  `U+A121 <https://codepoints.net/U+A121>`_  '\\ua121'  Lo                  2  YI SYLLABLE TAT
     8  `U+A45F <https://codepoints.net/U+A45F>`_  '\\ua45f'  Lo                  2  YI SYLLABLE XI
   ===  =========================================  =========  ==========  =========  ===============

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x89\xac\xea\x87\xae\xea\x83\x85\xea\x8f\xa2\xea\x87\x88\xea\x84\x89\xea\x84\xa1\xea\x91\x9f|\\n1234567890123456|\\n"
        ꉬꇮꃅꏢꇈꄉꄡꑟ|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *Konsole* measures width -4.

.. _KonsolelangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===========================
     1  `U+7A7A <https://codepoints.net/U+7A7A>`_          '\\u7a7a'      Lo                  2  CJK UNIFIED IDEOGRAPH-7A7A
     2  `U+57C3 <https://codepoints.net/U+57C3>`_          '\\u57c3'      Lo                  2  CJK UNIFIED IDEOGRAPH-57C3
     3  `U+88AB <https://codepoints.net/U+88AB>`_          '\\u88ab'      Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
     4  `U+6252 <https://codepoints.net/U+6252>`_          '\\u6252'      Lo                  2  CJK UNIFIED IDEOGRAPH-6252
     5  `U+0002B0DA <https://codepoints.net/U+0002B0DA>`_  '\\U0002b0da'  Lo                  2  CJK UNIFIED IDEOGRAPH-2B0DA
     6  `U+6C9B <https://codepoints.net/U+6C9B>`_          '\\u6c9b'      Lo                  2  CJK UNIFIED IDEOGRAPH-6C9B
     7  `U+53C3 <https://codepoints.net/U+53C3>`_          '\\u53c3'      Lo                  2  CJK UNIFIED IDEOGRAPH-53C3
     8  `U+52A0 <https://codepoints.net/U+52A0>`_          '\\u52a0'      Lo                  2  CJK UNIFIED IDEOGRAPH-52A0
     9  `U+00020B20 <https://codepoints.net/U+00020B20>`_  '\\U00020b20'  Lo                  2  CJK UNIFIED IDEOGRAPH-20B20
    10  `U+5354 <https://codepoints.net/U+5354>`_          '\\u5354'      Lo                  2  CJK UNIFIED IDEOGRAPH-5354
    11  `U+6703 <https://codepoints.net/U+6703>`_          '\\u6703'      Lo                  2  CJK UNIFIED IDEOGRAPH-6703
    12  `U+8287 <https://codepoints.net/U+8287>`_          '\\u8287'      Lo                  2  CJK UNIFIED IDEOGRAPH-8287
   ===  =================================================  =============  ==========  =========  ===========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xa9\xba\xe5\x9f\x83\xe8\xa2\xab\xe6\x89\x92\xf0\xab\x83\x9a\xe6\xb2\x9b\xe5\x8f\x83\xe5\x8a\xa0\xf0\xa0\xac\xa0\xe5\x8d\x94\xe6\x9c\x83\xe8\x8a\x87|\\n123456789012345678901234|\\n"
        空埃被扒𫃚沛參加𠬠協會芇|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *Konsole* measures width -12.

.. _KonsolelangJinan:

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
     3  `U+4E94 <https://codepoints.net/U+4E94>`_  '\\u4e94'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E94
     4  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xba\x94\xe6\x9d\xa1|\\n12345678|\\n"
        第十五条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Konsole* measures width -10.

.. _KonsolelangChineseMandarinGuiyang:

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
     2  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     3  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     4  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
     5  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
     6  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     7  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
     8  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     9  `U+5E73 <https://codepoints.net/U+5E73>`_  '\\u5e73'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E73
    10  `U+7B49 <https://codepoints.net/U+7B49>`_  '\\u7b49'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B49
    11  `U+4FDD <https://codepoints.net/U+4FDD>`_  '\\u4fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FDD
    12  `U+62A4 <https://codepoints.net/U+62A4>`_  '\\u62a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-62A4
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe6\x9c\x89\xe6\x9d\x83\xe4\xba\xab\xe5\x8f\x97\xe6\xb3\x95\xe5\xbe\x8b\xe7\x9a\x84\xe5\xb9\xb3\xe7\xad\x89\xe4\xbf\x9d\xe6\x8a\xa4|\\n123456789012345678901234|\\n"
        并有权享受法律的平等保护|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *Konsole* measures width 2.

.. _KonsolelangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4E5F <https://codepoints.net/U+4E5F>`_  '\\u4e5f'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5F
     2  `U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
     3  `U+6562 <https://codepoints.net/U+6562>`_  '\\u6562'  Lo                  2  CJK UNIFIED IDEOGRAPH-6562
     4  `U+5426 <https://codepoints.net/U+5426>`_  '\\u5426'  Lo                  2  CJK UNIFIED IDEOGRAPH-5426
     5  `U+8BA4 <https://codepoints.net/U+8BA4>`_  '\\u8ba4'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BA4
     6  `U+5176 <https://codepoints.net/U+5176>`_  '\\u5176'  Lo                  2  CJK UNIFIED IDEOGRAPH-5176
     7  `U+6539 <https://codepoints.net/U+6539>`_  '\\u6539'  Lo                  2  CJK UNIFIED IDEOGRAPH-6539
     8  `U+53D8 <https://codepoints.net/U+53D8>`_  '\\u53d8'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D8
     9  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    10  `U+7C4D <https://codepoints.net/U+7C4D>`_  '\\u7c4d'  Lo                  2  CJK UNIFIED IDEOGRAPH-7C4D
    11  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    12  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
    13  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xb9\x9f\xe4\xb8\x8d\xe6\x95\xa2\xe5\x90\xa6\xe8\xae\xa4\xe5\x85\xb6\xe6\x94\xb9\xe5\x8f\x98\xe5\x9b\xbd\xe7\xb1\x8d\xe7\x9a\x84\xe6\x9d\x83\xe5\x88\xa9|\\n12345678901234567890123456|\\n"
        也不敢否认其改变国籍的权利|
        12345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 26,
  while *Konsole* measures width 4.

.. _KonsolelangChineseMinNan:

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
     2  `U+4F55 <https://codepoints.net/U+4F55>`_  '\\u4f55'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F55
     3  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     4  `U+5F53 <https://codepoints.net/U+5F53>`_  '\\u5f53'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F53
     5  `U+5BAA <https://codepoints.net/U+5BAA>`_  '\\u5baa'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BAA
     6  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     7  `U+6291 <https://codepoints.net/U+6291>`_  '\\u6291'  Lo                  2  CJK UNIFIED IDEOGRAPH-6291
     8  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     9  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
    10  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    11  `U+8D4B <https://codepoints.net/U+8D4B>`_  '\\u8d4b'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D4B
    12  `U+4E88 <https://codepoints.net/U+4E88>`_  '\\u4e88'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E88
    13  `U+4F0A <https://codepoints.net/U+4F0A>`_  '\\u4f0a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F0A
    14  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    15  `U+57FA <https://codepoints.net/U+57FA>`_  '\\u57fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-57FA
    16  `U+672C <https://codepoints.net/U+672C>`_  '\\u672c'  Lo                  2  CJK UNIFIED IDEOGRAPH-672C
    17  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
    18  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    19  `U+906D <https://codepoints.net/U+906D>`_  '\\u906d'  Lo                  2  CJK UNIFIED IDEOGRAPH-906D
    20  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    21  `U+8D25 <https://codepoints.net/U+8D25>`_  '\\u8d25'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D25
    22  `U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
    23  `U+65F6 <https://codepoints.net/U+65F6>`_  '\\u65f6'  Lo                  2  CJK UNIFIED IDEOGRAPH-65F6
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 23


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xbb\xe4\xbd\x95\xe4\xba\xba\xe5\xbd\x93\xe5\xae\xaa\xe6\xb3\x95\xe6\x8a\x91\xe6\xb3\x95\xe5\xbe\x8b\xe6\x89\x80\xe8\xb5\x8b\xe4\xba\x88\xe4\xbc\x8a\xe7\x9a\x84\xe5\x9f\xba\xe6\x9c\xac\xe6\x9d\x83\xe5\x88\xa9\xe9\x81\xad\xe5\x8f\x97\xe8\xb4\xa5\xe5\xae\xb3\xe6\x97\xb6|\\n1234567890123456789012345678901234567890123456|\\n"
        任何人当宪法抑法律所赋予伊的基本权利遭受败害时|
        1234567890123456789012345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 46,
  while *Konsole* measures width 37.

.. _KonsolelangLao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  =========
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  =========
     1  `U+0031 <https://codepoints.net/U+0031>`_  '1'       Nd                  1  DIGIT ONE
     2  `U+003A <https://codepoints.net/U+003A>`_  ':'       Po                  1  COLON
   ===  =========================================  ========  ==========  =========  =========

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "1:|\\n12|\\n"
        1:|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -4.

.. _KonsolelangChineseMandarinSimplified:

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
     2  `U+514D <https://codepoints.net/U+514D>`_  '\\u514d'  Lo                  2  CJK UNIFIED IDEOGRAPH-514D
     3  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
     4  `U+8FD9 <https://codepoints.net/U+8FD9>`_  '\\u8fd9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FD9
     5  `U+79CD <https://codepoints.net/U+79CD>`_  '\\u79cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-79CD
     6  `U+5E72 <https://codepoints.net/U+5E72>`_  '\\u5e72'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E72
     7  `U+6D89 <https://codepoints.net/U+6D89>`_  '\\u6d89'  Lo                  2  CJK UNIFIED IDEOGRAPH-6D89
     8  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     9  `U+653B <https://codepoints.net/U+653B>`_  '\\u653b'  Lo                  2  CJK UNIFIED IDEOGRAPH-653B
    10  `U+51FB <https://codepoints.net/U+51FB>`_  '\\u51fb'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FB
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xa5\xe5\x85\x8d\xe5\x8f\x97\xe8\xbf\x99\xe7\xa7\x8d\xe5\xb9\xb2\xe6\xb6\x89\xe6\x88\x96\xe6\x94\xbb\xe5\x87\xbb|\\n12345678901234567890|\\n"
        以免受这种干涉或攻击|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *Konsole* measures width 0.

.. _KonsolelangThai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0E1E <https://codepoints.net/U+0E1E>`_  '\\u0e1e'  Lo                  1  THAI CHARACTER PHO PHAN
     2  `U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
     3  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
     4  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
     5  `U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
     6  `U+0E1E <https://codepoints.net/U+0E1E>`_  '\\u0e1e'  Lo                  1  THAI CHARACTER PHO PHAN
     7  `U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
     8  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     9  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
    10  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
    11  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    12  `U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
    13  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    14  `U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
    15  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    16  `U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
    17  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
    18  `U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
    19  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    20  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
    21  `U+0E04 <https://codepoints.net/U+0E04>`_  '\\u0e04'  Lo                  1  THAI CHARACTER KHO KHWAI
    22  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 22


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x9e\xe0\xb8\xb7\xe0\xb9\x89\xe0\xb8\x99\xe0\xb9\x80\xe0\xb8\x9e\xe0\xb8\x97\xe0\xb8\xb2\xe0\xb8\x87\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x95\xe0\xb8\xb4\xe0\xb8\xab\xe0\xb8\xa3\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb8\xaa\xe0\xb8\xb1\xe0\xb8\x87\xe0\xb8\x84\xe0\xb8\xa1|\\n12345678901234567|\\n"
        พื้นเพทางชาติหรือสังคม|
        12345678901234567|

- python `wcwidth.wcswidth()`_ measures width 17,
  while *Konsole* measures width -10.

.. _KonsolelangChineseGan:

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
     3  `U+4E94 <https://codepoints.net/U+4E94>`_  '\\u4e94'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E94
     4  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xba\x94\xe6\x9d\xa1|\\n12345678|\\n"
        第十五条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Konsole* measures width -8.

.. _KonsolelangChineseWu:

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
     2  `U+4F55 <https://codepoints.net/U+4F55>`_  '\\u4f55'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F55
     3  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     4  `U+62C9 <https://codepoints.net/U+62C9>`_  '\\u62c9'  Lo                  2  CJK UNIFIED IDEOGRAPH-62C9
     5  `U+5BAA <https://codepoints.net/U+5BAA>`_  '\\u5baa'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BAA
     6  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     7  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     8  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     9  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
    10  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    11  `U+8D4B <https://codepoints.net/U+8D4B>`_  '\\u8d4b'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D4B
    12  `U+4E88 <https://codepoints.net/U+4E88>`_  '\\u4e88'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E88
    13  `U+4F0A <https://codepoints.net/U+4F0A>`_  '\\u4f0a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F0A
    14  `U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
    15  `U+57FA <https://codepoints.net/U+57FA>`_  '\\u57fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-57FA
    16  `U+672C <https://codepoints.net/U+672C>`_  '\\u672c'  Lo                  2  CJK UNIFIED IDEOGRAPH-672C
    17  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
    18  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    19  `U+906D <https://codepoints.net/U+906D>`_  '\\u906d'  Lo                  2  CJK UNIFIED IDEOGRAPH-906D
    20  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    21  `U+4FB5 <https://codepoints.net/U+4FB5>`_  '\\u4fb5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FB5
    22  `U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
    23  `U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
    24  `U+8FB0 <https://codepoints.net/U+8FB0>`_  '\\u8fb0'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FB0
    25  `U+5149 <https://codepoints.net/U+5149>`_  '\\u5149'  Lo                  2  CJK UNIFIED IDEOGRAPH-5149
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 25


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xbb\xe4\xbd\x95\xe4\xba\xba\xe6\x8b\x89\xe5\xae\xaa\xe6\xb3\x95\xe6\x88\x96\xe6\xb3\x95\xe5\xbe\x8b\xe6\x89\x80\xe8\xb5\x8b\xe4\xba\x88\xe4\xbc\x8a\xe4\xb8\xaa\xe5\x9f\xba\xe6\x9c\xac\xe6\x9d\x83\xe5\x88\xa9\xe9\x81\xad\xe5\x8f\x97\xe4\xbe\xb5\xe5\xae\xb3\xe4\xb8\xaa\xe8\xbe\xb0\xe5\x85\x89|\\n12345678901234567890123456789012345678901234567890|\\n"
        任何人拉宪法或法律所赋予伊个基本权利遭受侵害个辰光|
        12345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 50,
  while *Konsole* measures width 41.

.. _KonsolelangChineseXiang:

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
     3  `U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
     4  `U+4E94 <https://codepoints.net/U+4E94>`_  '\\u4e94'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E94
     5  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe5\x8d\x81\xe4\xba\x94\xe6\x9d\xa1|\\n1234567890|\\n"
        第二十五条|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Konsole* measures width -32.

.. _KonsolelangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+0048 <https://codepoints.net/U+0048>`_  'H'       Lu                  1  LATIN CAPITAL LETTER H
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Hattak|\\n123456|\\n"
        Hattak|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width -7.

.. _KonsolelangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     5  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bots\xc3\xadi|\\n123456|\\n"
        botsíi|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width -9.

.. _KonsolelangGumuz:

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
     5  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     7  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     9  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "maa\xc5\x8bgasil|\\n123456789|\\n"
        maaŋgasil|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Konsole* measures width -2.

.. _KonsolelangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jacon|\\n12345|\\n"
        jacon|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Konsole* measures width -11.

.. _KonsolelangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0427 <https://codepoints.net/U+0427>`_  '\\u0427'  Lu                  1  CYRILLIC CAPITAL LETTER CHE
     2  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     3  `U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
     4  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xa7\xd0\xb0\xd0\xb2\xd0\xb0|\\n1234|\\n"
        Чава|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width -5.

.. _KonsolelangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
     2  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     3  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
     4  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     5  `U+0447 <https://codepoints.net/U+0447>`_  '\\u0447'  Ll                  1  CYRILLIC SMALL LETTER CHE
     6  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     7  `U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
     8  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     9  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
    10  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
    11  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
    12  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
    13  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
    14  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb1\xd1\x8d\xd0\xbb\xd1\x8d\xd1\x87\xd0\xb8\xd0\xb1\xd1\x83\xd0\xb4\xd0\xb4\xd0\xbe\xcc\x84\xd1\x80\xd0\xb8|\\n1234567890123|\\n"
        бэлэчибуддо̄ри|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *Konsole* measures width -1.

.. _KonsolelangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     2  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     3  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     4  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "o'ch|\\n1234|\\n"
        o'ch|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width -3.

.. _KonsolelangAmarakaeri:

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     2  `U+0055 <https://codepoints.net/U+0055>`_  'U'       Lu                  1  LATIN CAPITAL LETTER U
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     4  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     7  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     8  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "'Urua'da|\\n12345678|\\n"
        'Urua'da|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Konsole* measures width 1.

.. _KonsolelangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yee|\\n123|\\n"
        yee|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width -12.

.. _KonsolelangVeps:

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================================
     1  `U+00DC <https://codepoints.net/U+00DC>`_  '\\xdc'    Lu                  1  LATIN CAPITAL LETTER U WITH DIAERESIS
     2  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     4  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     6  `U+017E <https://codepoints.net/U+017E>`_  '\\u017e'  Ll                  1  LATIN SMALL LETTER Z WITH CARON
     7  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     8  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     9  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
    10  `U+0076 <https://codepoints.net/U+0076>`_  'v'        Ll                  1  LATIN SMALL LETTER V
    11  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    12  `U+007A <https://codepoints.net/U+007A>`_  'z'        Ll                  1  LATIN SMALL LETTER Z
    13  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
    14  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
    15  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
    16  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
    17  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    18  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
    19  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
    20  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  =========  ==========  =========  =====================================

Total codepoints: 20


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\x9chthi\xc5\xberahvazkundanke|\\n12345678901234567890|\\n"
        Ühthižrahvazkundanke|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *Konsole* measures width 15.

.. _KonsolelangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     4  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jeo\xcc\xb1ni|\\n12345|\\n"
        jeo̱ni|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Konsole* measures width -4.

.. _KonsolelangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     2  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x8d\xd1\x80|\\n12|\\n"
        эр|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -10.

.. _KonsolelangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================================
     1  `U+049B <https://codepoints.net/U+049B>`_  '\\u049b'  Ll                  1  CYRILLIC SMALL LETTER KA WITH DESCENDER
     2  `U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
     3  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
     4  `U+04FB <https://codepoints.net/U+04FB>`_  '\\u04fb'  Ll                  1  CYRILLIC SMALL LETTER GHE WITH STROKE AND HOOK
     5  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
   ===  =========================================  =========  ==========  =========  ==============================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd2\x9b\xca\xbc\xd0\xbe\xd3\xbb\xd0\xbb|\\n12345|\\n"
        қʼоӻл|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Konsole* measures width 0.

.. _KonsolelangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ============================
     1  `U+0059 <https://codepoints.net/U+0059>`_  'Y'        Lu                  1  LATIN CAPITAL LETTER Y
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     6  `U+0131 <https://codepoints.net/U+0131>`_  '\\u0131'  Ll                  1  LATIN SMALL LETTER DOTLESS I
     7  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  ============================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Yasan\xc4\xb1n|\\n1234567|\\n"
        Yasanın|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Konsole* measures width -4.

.. _KonsolelangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xb1ese|\\n1234|\\n"
        ñese|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width -6.

.. _KonsolelangColorado:

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     6  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bolonla|\\n1234567|\\n"
        bolonla|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Konsole* measures width 0.

.. _KonsolelangKorean:

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+B300 <https://codepoints.net/U+B300>`_  '\\ub300'  Lo                  2  HANGUL SYLLABLE DAE
     2  `U+D55C <https://codepoints.net/U+D55C>`_  '\\ud55c'  Lo                  2  HANGUL SYLLABLE HAN
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xeb\x8c\x80\xed\x95\x9c|\\n1234|\\n"
        대한|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width -2.

.. _KonsolelangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+C774 <https://codepoints.net/U+C774>`_  '\\uc774'  Lo                  2  HANGUL SYLLABLE I
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x9d\xb4|\\n12|\\n"
        이|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -4.

.. _KonsolelangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     4  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     5  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     6  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     7  `U+0269 <https://codepoints.net/U+0269>`_  '\\u0269'  Ll                  1  LATIN SMALL LETTER IOTA
     8  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     9  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
    10  `U+002D <https://codepoints.net/U+002D>`_  '-'        Pd                  1  HYPHEN-MINUS
    11  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
    12  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
    13  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
    14  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc9\x9b\xcc\x81\xc9\x9b\xcc\x81d\xc9\xa9w\xc3\xa1-d\xc9\x9b\xcc\x81\xc9\x9b|\\n12345678901|\\n"
        tɛ́ɛ́dɩwá-dɛ́ɛ|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *Konsole* measures width 9.

.. _KonsolelangTicuna:

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     2  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
     3  `U+0129 <https://codepoints.net/U+0129>`_  '\\u0129'  Ll                  1  LATIN SMALL LETTER I WITH TILDE
     4  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
     5  `U+1EBD <https://codepoints.net/U+1EBD>`_  '\\u1ebd'  Ll                  1  LATIN SMALL LETTER E WITH TILDE
     6  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ix\xc4\xa9x\xe1\xba\xbd.|\\n123456|\\n"
        ixĩxẽ.|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width -1.

.. _KonsolelangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "les|\\n123|\\n"
        les|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 0.

.. _KonsolelangMaldivian:

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+078A <https://codepoints.net/U+078A>`_  '\\u078a'  Lo                  1  THAANA LETTER FAAFU
     2  `U+07A8 <https://codepoints.net/U+07A8>`_  '\\u07a8'  Mn                  0  THAANA IBIFILI
     3  `U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
     4  `U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
     5  `U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
     6  `U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
     7  `U+0782 <https://codepoints.net/U+0782>`_  '\\u0782'  Lo                  1  THAANA LETTER NOONU
     8  `U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
     9  `U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
    10  `U+07AC <https://codepoints.net/U+07AC>`_  '\\u07ac'  Mn                  0  THAANA EBEFILI
    11  `U+0783 <https://codepoints.net/U+0783>`_  '\\u0783'  Lo                  1  THAANA LETTER RAA
    12  `U+07A8 <https://codepoints.net/U+07A8>`_  '\\u07a8'  Mn                  0  THAANA IBIFILI
    13  `U+0786 <https://codepoints.net/U+0786>`_  '\\u0786'  Lo                  1  THAANA LETTER KAAFU
    14  `U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
    15  `U+0789 <https://codepoints.net/U+0789>`_  '\\u0789'  Lo                  1  THAANA LETTER MEEMU
    16  `U+07A7 <https://codepoints.net/U+07A7>`_  '\\u07a7'  Mn                  0  THAANA AABAAFILI
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x8a\xde\xa8\xde\x87\xde\xb0\xde\x8c\xde\xaa\xde\x82\xde\xb0\xde\x8c\xde\xac\xde\x83\xde\xa8\xde\x86\xde\xa6\xde\x89\xde\xa7|\\n12345678|\\n"
        ފިއްތުންތެރިކަމާ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Konsole* measures width 0.

.. _KonsolelangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
     3  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     4  `U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
     5  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     6  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
     7  `U+0643 <https://codepoints.net/U+0643>`_  '\\u0643'  Lo                  1  ARABIC LETTER KAF
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x84\xd9\x85\xd8\xb4\xd8\xaa\xd8\xb1\xd9\x83|\\n1234567|\\n"
        المشترك|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Konsole* measures width 0.

.. _KonsolelangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "na|\\n12|\\n"
        na|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -5.

.. _KonsolelangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================================
     1  `U+05D6 <https://codepoints.net/U+05D6>`_  '\\u05d6'  Lo                  1  HEBREW LETTER ZAYIN
     2  `U+05F2 <https://codepoints.net/U+05F2>`_  '\\u05f2'  Lo                  1  HEBREW LIGATURE YIDDISH DOUBLE YOD
   ===  =========================================  =========  ==========  =========  ==================================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x96\xd7\xb2|\\n12|\\n"
        זײ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width 0.

.. _KonsolelangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ========================
     1  `U+0001E93C <https://codepoints.net/U+0001E93C>`_  '\\U0001e93c'  Ll                  1  ADLAM SMALL LETTER TU
     2  `U+0001E935 <https://codepoints.net/U+0001E935>`_  '\\U0001e935'  Ll                  1  ADLAM SMALL LETTER U
     3  `U+0001E945 <https://codepoints.net/U+0001E945>`_  '\\U0001e945'  Mn                  0  ADLAM VOWEL LENGTHENER
     4  `U+0001E93A <https://codepoints.net/U+0001E93A>`_  '\\U0001e93a'  Ll                  1  ADLAM SMALL LETTER GA
     5  `U+0001E922 <https://codepoints.net/U+0001E922>`_  '\\U0001e922'  Ll                  1  ADLAM SMALL LETTER ALIF
     6  `U+0001E944 <https://codepoints.net/U+0001E944>`_  '\\U0001e944'  Mn                  0  ADLAM ALIF LENGTHENER
     7  `U+0001E923 <https://codepoints.net/U+0001E923>`_  '\\U0001e923'  Ll                  1  ADLAM SMALL LETTER DAALI
     8  `U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
   ===  =================================================  =============  ==========  =========  ========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xbc\xf0\x9e\xa4\xb5\xf0\x9e\xa5\x85\xf0\x9e\xa4\xba\xf0\x9e\xa4\xa2\xf0\x9e\xa5\x84\xf0\x9e\xa4\xa3\xf0\x9e\xa4\xab|\\n123456|\\n"
        𞤼𞤵𞥅𞤺𞤢𞥄𞤣𞤫|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width 5.

.. _KonsolelangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ad|\\n12|\\n"
        ad|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -8.

.. _KonsolelangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     2  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     3  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "o\xcc\x81yo|\\n123|\\n"
        óyo|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width -2.

.. _KonsolelangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "d\xc3\xa8s|\\n123|\\n"
        dès|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 1.

.. _KonsolelangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     4  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     7  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     9  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tigwnatin|\\n123456789|\\n"
        tigwnatin|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Konsole* measures width 1.

.. _Konsolelangw:

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "me|\\n12|\\n"
        me|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -9.

.. _KonsolelangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     2  `U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "g\xc3\xa9|\\n12|\\n"
        gé|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -6.

.. _KonsolelangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
     2  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     3  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     4  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
     5  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
     6  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     7  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
     8  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     9  `U+5E73 <https://codepoints.net/U+5E73>`_  '\\u5e73'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E73
    10  `U+7B49 <https://codepoints.net/U+7B49>`_  '\\u7b49'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B49
    11  `U+4FDD <https://codepoints.net/U+4FDD>`_  '\\u4fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FDD
    12  `U+62A4 <https://codepoints.net/U+62A4>`_  '\\u62a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-62A4
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe6\x9c\x89\xe6\x9d\x83\xe4\xba\xab\xe5\x8f\x97\xe6\xb3\x95\xe5\xbe\x8b\xe7\x9a\x84\xe5\xb9\xb3\xe7\xad\x89\xe4\xbf\x9d\xe6\x8a\xa4|\\n123456789012345678901234|\\n"
        并有权享受法律的平等保护|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *Konsole* measures width 4.

.. _KonsolelangChineseYue:

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
     3  `U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
     4  `U+4E5D <https://codepoints.net/U+4E5D>`_  '\\u4e5d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5D
     5  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe5\x8d\x81\xe4\xb9\x9d\xe6\x9d\xa1|\\n1234567890|\\n"
        第二十九条|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Konsole* measures width -30.

.. _KonsolelangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
     3  `U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
     4  `U+4E5D <https://codepoints.net/U+4E5D>`_  '\\u4e5d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5D
     5  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe5\x8d\x81\xe4\xb9\x9d\xe6\x9d\xa1|\\n1234567890|\\n"
        第二十九条|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Konsole* measures width -26.

.. _KonsolelangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+004B <https://codepoints.net/U+004B>`_  'K'        Lu                  1  LATIN CAPITAL LETTER K
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     6  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     7  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     8  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     9  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
    10  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    11  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
    12  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Konside\xcc\x81rang|\\n12345678901|\\n"
        Konsidérang|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *Konsole* measures width 4.

.. _KonsolelangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "o|\\n1|\\n"
        o|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Konsole* measures width -9.

.. _KonsolelangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     2  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     3  `U+0076 <https://codepoints.net/U+0076>`_  'v'        Ll                  1  LATIN SMALL LETTER V
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     5  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     6  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "e\xcc\x80ve\xcc\x80k|\\n1234|\\n"
        èvèk|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width -4.

.. _KonsolelangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "dira|\\n1234|\\n"
        dira|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width 2.

.. _KonsolelangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004E <https://codepoints.net/U+004E>`_  'N'       Lu                  1  LATIN CAPITAL LETTER N
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Nu|\\n12|\\n"
        Nu|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -9.

.. _KonsolelangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     2  `U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
     5  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     6  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kpa\xc5\x8bm\xc9\x94|\\n123456|\\n"
        kpaŋmɔ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width 4.

.. _KonsolelangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
     2  `U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
     3  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     4  `U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xad\xd9\x82\xd9\x88\xd9\x82|\\n1234|\\n"
        حقوق|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width -1.

.. _KonsolelangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     5  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     7  `U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
     8  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     9  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
    10  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
    11  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
    12  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "sa'ndeva'tna|\\n123456789012|\\n"
        sa'ndeva'tna|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *Konsole* measures width 9.

.. _KonsolelangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "wo|\\n12|\\n"
        wo|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width 1.

.. _KonsolelangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ke|\\n12|\\n"
        ke|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -6.

.. _KonsolelangUduk:

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mo.|\\n123|\\n"
        mo.|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width -2.

.. _KonsolelangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0718 <https://codepoints.net/U+0718>`_  '\\u0718'  Lo                  1  SYRIAC LETTER WAW
     2  `U+072C <https://codepoints.net/U+072C>`_  '\\u072c'  Lo                  1  SYRIAC LETTER TAW
     3  `U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
     4  `U+0712 <https://codepoints.net/U+0712>`_  '\\u0712'  Lo                  1  SYRIAC LETTER BETH
     5  `U+0742 <https://codepoints.net/U+0742>`_  '\\u0742'  Mn                  0  SYRIAC RUKKAKHA
     6  `U+0720 <https://codepoints.net/U+0720>`_  '\\u0720'  Lo                  1  SYRIAC LETTER LAMADH
     7  `U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
     8  `U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\x98\xdc\xac\xdc\x9d\xdc\x92\xdd\x82\xdc\xa0\xdc\x9d\xdc\x90|\\n1234567|\\n"
        ܘܬܝܒ݂ܠܝܐ|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Konsole* measures width 1.

.. _KonsolelangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     3  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     4  `U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xd9\x85\xd8\xa7\xd9\x84|\\n1234|\\n"
        کمال|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width -1.

.. _KonsolelangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nte|\\n123|\\n"
        nte|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 1.

.. _KonsolelangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n|\\n1|\\n"
        n|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Konsole* measures width -5.

.. _KonsolelangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+00EC <https://codepoints.net/U+00EC>`_  '\\xec'    Ll                  1  LATIN SMALL LETTER I WITH GRAVE
     2  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     3  `U+1ECD <https://codepoints.net/U+1ECD>`_  '\\u1ecd'  Ll                  1  LATIN SMALL LETTER O WITH DOT BELOW
     4  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     5  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     6  `U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xacd\xe1\xbb\x8d\xcc\x81gba|\\n123456|\\n"
        ìdọ́gba|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Konsole* measures width 2.

.. _KonsolelangChinantecChiltepec:

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kio|\\n123|\\n"
        kio|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 0.

.. _KonsolelangUrdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xdb\x8c|\\n12|\\n"
        کی|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -3.

.. _KonsolelangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaf|\\n1|\\n"
        د|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Konsole* measures width -2.

.. _KonsolelangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     2  `U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaa\xdb\x92|\\n12|\\n"
        تے|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -4.

.. _KonsolelangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     2  `U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "w\xc3\xa9i|\\n123|\\n"
        wéi|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width -4.

.. _KonsolelangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x9b|\\n12|\\n"
        nɛ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -6.

.. _KonsolelangUrdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+06C1 <https://codepoints.net/U+06C1>`_  '\\u06c1'  Lo                  1  ARABIC LETTER HEH GOAL
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xdb\x81|\\n12|\\n"
        کہ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -3.

.. _KonsolelangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nam|\\n123|\\n"
        nam|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width -1.

.. _KonsolelangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     2  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mbuo|\\n1234|\\n"
        mbuo|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width -1.

.. _KonsolelangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     3  `U+0308 <https://codepoints.net/U+0308>`_  '\\u0308'  Mn                  0  COMBINING DIAERESIS
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "c\xc9\x9b\xcc\x88r|\\n123|\\n"
        cɛ̈r|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 0.

.. _KonsolelangDagaareSouthern:

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ka|\\n12|\\n"
        ka|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -3.

.. _KonsolelangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "i|\\n1|\\n"
        i|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Konsole* measures width -5.

.. _KonsolelangSererSine:

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ke|\\n12|\\n"
        ke|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -6.

.. _KonsolelangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
     3  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xd8\xb1\xd8\xaf|\\n123|\\n"
        کرد|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 0.

.. _KonsolelangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "suam|\\n1234|\\n"
        suam|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width 0.

.. _KonsolelangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ker|\\n123|\\n"
        ker|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 0.

.. _KonsolelangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bonu|\\n1234|\\n"
        bonu|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Konsole* measures width 0.

.. _KonsolelangDangme:

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "si|\\n12|\\n"
        si|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -1.

.. _KonsolelangTaiDam:

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+AAB9 <https://codepoints.net/U+AAB9>`_  '\\uaab9'  Lo                  1  TAI VIET VOWEL UEA
     2  `U+AAAD <https://codepoints.net/U+AAAD>`_  '\\uaaad'  Lo                  1  TAI VIET LETTER HIGH HO
     3  `U+AAB7 <https://codepoints.net/U+AAB7>`_  '\\uaab7'  Mn                  0  TAI VIET MAI KHIT
     4  `U+AA9A <https://codepoints.net/U+AA9A>`_  '\\uaa9a'  Lo                  1  TAI VIET LETTER LOW BO
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xb9\xea\xaa\xad\xea\xaa\xb7\xea\xaa\x9a|\\n123|\\n"
        ꪹꪭꪷꪚ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Konsole* measures width 1.

.. _KonsolelangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+0F58 <https://codepoints.net/U+0F58>`_  '\\u0f58'  Lo                  1  TIBETAN LETTER MA
     2  `U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x98\xe0\xbd\xa2|\\n12|\\n"
        མར|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Konsole* measures width -4.

.. _KonsolelangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0F5A <https://codepoints.net/U+0F5A>`_  '\\u0f5a'  Lo                  1  TIBETAN LETTER TSHA
     2  `U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x9a\xe0\xbd\xb4|\\n1|\\n"
        ཚུ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Konsole* measures width -2.

.. _Konsoledecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

This Terminal does not appear capable of reporting about any DEC Private modes.

.. _Konsolereproduce:

Reproduction
++++++++++++

To reproduce these results for *Konsole*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --save-yaml=linux-konsole-23.08.5.yaml \
        --limit-codepoints=5000 \
        --limit-words=5000 \
        --limit-errors=1000

.. _Konsoletime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **39.97 seconds** (39s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
