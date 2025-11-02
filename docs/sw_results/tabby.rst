.. _tabby:

tabby
-----


Tested Software version 1.0.228 on Darwin
Full results available at ucs-detect_ repository path
`data/macos-tabby-1.0.228.yaml <https://github.com/jquast/ucs-detect/blob/master/data/macos-tabby-1.0.228.yaml>`_

.. _tabbyscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *tabby*:

.. table::
   :class: sphinx-datatable

   ============  ===========  ==============  ======================================================
   Score Type    Raw Score    Scaled Score    Calculation
   ============  ===========  ==============  ======================================================
   WIDE          36.36%       0.0%            (version_index / total_versions) × (pct_success / 100)
   ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
   LANG          71.79%       50.9%           geometric_mean(language_percentages)
   VS16          0.00%        0.0%            pct_success / 100
   VS15          0.00%        0.0%            pct_success / 100
   DEC Modes     11.95%       5.5%            modes_changeable / total_modes
   TIME          162.19s      67.7%           1 - ((elapsed - min) / (max - min)) [inverse]
   ============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 20.02%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 0.0%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _tabbywide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for tabby appears to be 
**12.0.0**, this is from a summary of the following
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
   '13.0.0'          552        552  0.0%
   '14.0.0'           54         54  0.0%
   '15.0.0'           22         22  0.0%
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
  while *tabby* measures width 1.

.. _tabbyzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *tabby* appears to be 
**None**, this is from a summary of the following
results:


.. table::
   :class: sphinx-datatable

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

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =================================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =================================
     1  `U+0001F469 <https://codepoints.net/U+0001F469>`_  '\\U0001f469'  So                  2  WOMAN
     2  `U+0001F3FE <https://codepoints.net/U+0001F3FE>`_  '\\U0001f3fe'  Sk                  0  EMOJI MODIFIER FITZPATRICK TYPE-5
     3  `U+200D <https://codepoints.net/U+200D>`_          '\\u200d'      Cf                  0  ZERO WIDTH JOINER
     4  `U+0001FAEF <https://codepoints.net/U+0001FAEF>`_  '\\U0001faef'  Cn                  2  na
     5  `U+200D <https://codepoints.net/U+200D>`_          '\\u200d'      Cf                  0  ZERO WIDTH JOINER
     6  `U+0001F469 <https://codepoints.net/U+0001F469>`_  '\\U0001f469'  So                  2  WOMAN
     7  `U+0001F3FF <https://codepoints.net/U+0001F3FF>`_  '\\U0001f3ff'  Sk                  0  EMOJI MODIFIER FITZPATRICK TYPE-6
   ===  =================================================  =============  ==========  =========  =================================

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

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+2733 <https://codepoints.net/U+2733>`_  '\\u2733'  So                  1  EIGHT SPOKED ASTERISK
     2  `U+FE0F <https://codepoints.net/U+FE0F>`_  '\\ufe0f'  Mn                  0  VARIATION SELECTOR-16
   ===  =========================================  =========  ==========  =========  =====================

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

Emoji VS-15 results for *tabby* is 158 errors
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
  while *tabby* measures width 2.


.. _tabbylang:

Language Support
++++++++++++++++

The following 2 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog).

The following 117 languages are not fully supported:

.. table::
   :class: sphinx-datatable

   ============================================================================  ==========  =========  =============
   lang                                                                            n_errors    n_total  pct_success
   ============================================================================  ==========  =========  =============
   :ref:`Javanese (Javanese) <tabbylangJavaneseJavanese>`                              1000       1028  2.7%
   :ref:`Shan <tabbylangShan>`                                                          868        915  5.1%
   :ref:`Tamil (Sri Lanka) <tabbylangTamilSriLanka>`                                   1000       1074  6.9%
   :ref:`Tamil <tabbylangTamil>`                                                       1000       1075  7.0%
   :ref:`Sanskrit (Grantha) <tabbylangSanskritGrantha>`                                 894       1006  11.1%
   :ref:`Malayalam <tabbylangMalayalam>`                                               1000       1154  13.3%
   :ref:`Bengali <tabbylangBengali>`                                                   1000       1165  14.2%
   :ref:`Khmer, Central <tabbylangKhmerCentral>`                                        449        528  15.0%
   :ref:`Kannada <tabbylangKannada>`                                                    903       1080  16.4%
   :ref:`Khün <tabbylangKhn>`                                                           363        442  17.9%
   :ref:`Burmese <tabbylangBurmese>`                                                    977       1223  20.1%
   :ref:`Sanskrit <tabbylangSanskrit>`                                                  756       1000  24.4%
   :ref:`Tamang, Eastern <tabbylangTamangEastern>`                                       33         45  26.7%
   :ref:`Mon <tabbylangMon>`                                                            679        946  28.2%
   :ref:`Marathi <tabbylangMarathi>`                                                   1000       1420  29.6%
   :ref:`Nepali <tabbylangNepali>`                                                      933       1385  32.6%
   :ref:`Gujarati <tabbylangGujarati>`                                                 1000       1518  34.1%
   :ref:`Telugu <tabbylangTelugu>`                                                      717       1129  36.5%
   :ref:`Maithili <tabbylangMaithili>`                                                  954       1519  37.2%
   :ref:`Hindi <tabbylangHindi>`                                                       1000       1631  38.7%
   :ref:`Panjabi, Eastern <tabbylangPanjabiEastern>`                                   1000       1825  45.2%
   :ref:`Sinhala <tabbylangSinhala>`                                                    886       1655  46.5%
   :ref:`Bhojpuri <tabbylangBhojpuri>`                                                  880       1737  49.3%
   :ref:`Magahi <tabbylangMagahi>`                                                      813       1716  52.6%
   :ref:`Chakma <tabbylangChakma>`                                                      497       1444  65.6%
   :ref:`Nuosu <tabbylangNuosu>`                                                          5        230  97.8%
   :ref:`Chinese, Mandarin (Harbin) <tabbylangChineseMandarinHarbin>`                     4        210  98.1%
   :ref:`Chinese, Mandarin (Traditional) <tabbylangChineseMandarinTraditional>`           4        210  98.1%
   :ref:`(Jinan) <tabbylangJinan>`                                                        4        211  98.1%
   :ref:`Chinese, Gan <tabbylangChineseGan>`                                              4        211  98.1%
   :ref:`Chinese, Hakka <tabbylangChineseHakka>`                                          4        212  98.1%
   :ref:`Chinese, Jinyu <tabbylangChineseJinyu>`                                          4        212  98.1%
   :ref:`Chinese, Mandarin (Beijing) <tabbylangChineseMandarinBeijing>`                   4        212  98.1%
   :ref:`Chinese, Mandarin (Nanjing) <tabbylangChineseMandarinNanjing>`                   4        212  98.1%
   :ref:`Chinese, Mandarin (Tianjin) <tabbylangChineseMandarinTianjin>`                   4        212  98.1%
   :ref:`Chinese, Xiang <tabbylangChineseXiang>`                                          4        212  98.1%
   :ref:`Japanese (Tokyo) <tabbylangJapaneseTokyo>`                                       6        320  98.1%
   :ref:`Chinese, Mandarin (Simplified) <tabbylangChineseMandarinSimplified>`             4        225  98.2%
   :ref:`Japanese <tabbylangJapanese>`                                                    5        299  98.3%
   :ref:`Japanese (Osaka) <tabbylangJapaneseOsaka>`                                       5        308  98.4%
   :ref:`Thai (2) <tabbylangThai2>`                                                       5        313  98.4%
   :ref:`Chinese, Yue <tabbylangChineseYue>`                                              3        210  98.6%
   :ref:`Chinese, Mandarin (Guiyang) <tabbylangChineseMandarinGuiyang>`                   3        211  98.6%
   :ref:`Chinese, Wu <tabbylangChineseWu>`                                                3        211  98.6%
   :ref:`Chinese, Min Nan <tabbylangChineseMinNan>`                                       3        212  98.6%
   :ref:`Lao <tabbylangLao>`                                                              5        426  98.8%
   :ref:`Vietnamese (Han nom) <tabbylangVietnameseHannom>`                                2        199  99.0%
   :ref:`Yaneshaʼ <tabbylangYanesha>`                                                    23       2536  99.1%
   :ref:`Thai <tabbylangThai>`                                                            3        341  99.1%
   :ref:`Chickasaw <tabbylangChickasaw>`                                                  4        554  99.3%
   :ref:`Bora <tabbylangBora>`                                                           10       1598  99.4%
   :ref:`Orok <tabbylangOrok>`                                                            7       1245  99.4%
   :ref:`Shipibo-Conibo <tabbylangShipiboConibo>`                                        14       2540  99.4%
   :ref:`Gumuz <tabbylangGumuz>`                                                          7       1283  99.5%
   :ref:`South Azerbaijani <tabbylangSouthAzerbaijani>`                                   7       1396  99.5%
   :ref:`Navajo <tabbylangNavajo>`                                                        8       1600  99.5%
   :ref:`Nanai <tabbylangNanai>`                                                          6       1207  99.5%
   :ref:`Amarakaeri <tabbylangAmarakaeri>`                                                7       1446  99.5%
   :ref:`Siona <tabbylangSiona>`                                                          7       1492  99.5%
   :ref:`Gilyak <tabbylangGilyak>`                                                        7       1504  99.5%
   :ref:`Veps <tabbylangVeps>`                                                            6       1323  99.5%
   :ref:`Evenki <tabbylangEvenki>`                                                        4        899  99.6%
   :ref:`Secoya <tabbylangSecoya>`                                                        6       1409  99.6%
   :ref:`Korean <tabbylangKorean>`                                                        5       1185  99.6%
   :ref:`Colorado <tabbylangColorado>`                                                    5       1263  99.6%
   :ref:`Yiddish, Eastern <tabbylangYiddishEastern>`                                      7       1775  99.6%
   :ref:`Ticuna <tabbylangTicuna>`                                                        8       2048  99.6%
   :ref:`Kabyle <tabbylangKabyle>`                                                        7       1815  99.6%
   :ref:`(Yeonbyeon) <tabbylangYeonbyeon>`                                                4       1061  99.6%
   :ref:`Pular (Adlam) <tabbylangPularAdlam>`                                             6       1613  99.6%
   :ref:`Arabic, Standard <tabbylangArabicStandard>`                                      5       1348  99.6%
   :ref:`Catalan (2) <tabbylangCatalan2>`                                                 7       1909  99.6%
   :ref:`Mixtec, Metlatónoc <tabbylangMixtecMetlatnoc>`                                   5       1367  99.6%
   :ref:`Maldivian <tabbylangMaldivian>`                                                  7       1918  99.6%
   :ref:`Tem <tabbylangTem>`                                                              6       1659  99.6%
   :ref:`Éwé <tabbylangw>`                                                                8       2230  99.6%
   :ref:`Mirandese <tabbylangMirandese>`                                                  7       1966  99.6%
   :ref:`Picard <tabbylangPicard>`                                                        7       2024  99.7%
   :ref:`Assyrian Neo-Aramaic <tabbylangAssyrianNeoAramaic>`                              4       1160  99.7%
   :ref:`Saint Lucian Creole French <tabbylangSaintLucianCreoleFrench>`                   6       1777  99.7%
   :ref:`Maori (2) <tabbylangMaori2>`                                                     8       2385  99.7%
   :ref:`Lingala (tones) <tabbylangLingalatones>`                                         6       1818  99.7%
   :ref:`Farsi, Western <tabbylangFarsiWestern>`                                          6       1822  99.7%
   :ref:`Tamazight, Central Atlas <tabbylangTamazightCentralAtlas>`                       6       1822  99.7%
   :ref:`Fur <tabbylangFur>`                                                              6       1838  99.7%
   :ref:`Dari <tabbylangDari>`                                                            6       1872  99.7%
   :ref:`Ditammari <tabbylangDitammari>`                                                  6       1882  99.7%
   :ref:`Dendi <tabbylangDendi>`                                                          5       1569  99.7%
   :ref:`Mazahua Central <tabbylangMazahuaCentral>`                                       5       1574  99.7%
   :ref:`French (Welche) <tabbylangFrenchWelche>`                                         6       1928  99.7%
   :ref:`Uduk <tabbylangUduk>`                                                           10       3247  99.7%
   :ref:`Bamun <tabbylangBamun>`                                                          7       2285  99.7%
   :ref:`Gen <tabbylangGen>`                                                              7       2309  99.7%
   :ref:`Waama <tabbylangWaama>`                                                          3       1000  99.7%
   :ref:`Ga <tabbylangGa>`                                                                6       2039  99.7%
   :ref:`Aja <tabbylangAja>`                                                              6       2061  99.7%
   :ref:`Panjabi, Western <tabbylangPanjabiWestern>`                                      7       2419  99.7%
   :ref:`Chinantec, Chiltepec <tabbylangChinantecChiltepec>`                              5       1729  99.7%
   :ref:`Mòoré <tabbylangMor>`                                                            7       2447  99.7%
   :ref:`Yoruba <tabbylangYoruba>`                                                        7       2454  99.7%
   :ref:`Vietnamese <tabbylangVietnamese>`                                                7       2502  99.7%
   :ref:`Dagaare, Southern <tabbylangDagaareSouthern>`                                    7       2582  99.7%
   :ref:`Otomi, Mezquital <tabbylangOtomiMezquital>`                                      5       1849  99.7%
   :ref:`Lamnso' <tabbylangLamnso>`                                                       6       2237  99.7%
   :ref:`Urdu <tabbylangUrdu>`                                                            6       2237  99.7%
   :ref:`Pashto, Northern <tabbylangPashtoNorthern>`                                      6       2242  99.7%
   :ref:`Seraiki <tabbylangSeraiki>`                                                      6       2242  99.7%
   :ref:`Belanda Viri <tabbylangBelandaViri>`                                             6       2246  99.7%
   :ref:`Urdu (2) <tabbylangUrdu2>`                                                       6       2251  99.7%
   :ref:`Dinka, Northeastern <tabbylangDinkaNortheastern>`                                4       1529  99.7%
   :ref:`Baatonum <tabbylangBaatonum>`                                                    5       1939  99.7%
   :ref:`Serer-Sine <tabbylangSererSine>`                                                 4       1596  99.7%
   :ref:`Dangme <tabbylangDangme>`                                                        7       2912  99.8%
   :ref:`Fon <tabbylangFon>`                                                              6       2520  99.8%
   :ref:`Tai Dam <tabbylangTaiDam>`                                                       5       2386  99.8%
   :ref:`Dzongkha <tabbylangDzongkha>`                                                    6       3060  99.8%
   :ref:`Tibetan, Central <tabbylangTibetanCentral>`                                      6       3174  99.8%
   ============================================================================  ==========  =========  =============

.. _tabbylangJavaneseJavanese:

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
  while *tabby* measures width 4.

.. _tabbylangShan:

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
  while *tabby* measures width 9.

.. _tabbylangTamilSriLanka:

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
  while *tabby* measures width 4.

.. _tabbylangTamil:

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
  while *tabby* measures width 4.

.. _tabbylangSanskritGrantha:

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
  while *tabby* measures width 14.

.. _tabbylangMalayalam:

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
  while *tabby* measures width 21.

.. _tabbylangBengali:

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
  while *tabby* measures width 12.

.. _tabbylangKhmerCentral:

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
  while *tabby* measures width 25.

.. _tabbylangKannada:

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
  while *tabby* measures width 4.

.. _tabbylangKhn:

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
  while *tabby* measures width 15.

.. _tabbylangBurmese:

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
  while *tabby* measures width 11.

.. _tabbylangSanskrit:

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
  while *tabby* measures width 13.

.. _tabbylangTamangEastern:

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
  while *tabby* measures width 4.

.. _tabbylangMon:

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
  while *tabby* measures width 7.

.. _tabbylangMarathi:

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
  while *tabby* measures width 5.

.. _tabbylangNepali:

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
  while *tabby* measures width 4.

.. _tabbylangGujarati:

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
  while *tabby* measures width 4.

.. _tabbylangTelugu:

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
  while *tabby* measures width 10.

.. _tabbylangMaithili:

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
  while *tabby* measures width 7.

.. _tabbylangHindi:

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
  while *tabby* measures width 4.

.. _tabbylangPanjabiEastern:

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
  while *tabby* measures width 4.

.. _tabbylangSinhala:

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
  while *tabby* measures width 4.

.. _tabbylangBhojpuri:

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
  while *tabby* measures width 10.

.. _tabbylangMagahi:

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
  while *tabby* measures width 10.

.. _tabbylangChakma:

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
  while *tabby* measures width 8.

.. _tabbylangNuosu:

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================
     1  `U+A3F1 <https://codepoints.net/U+A3F1>`_  '\\ua3f1'  Lo                  2  YI SYLLABLE JUX
     2  `U+A3E6 <https://codepoints.net/U+A3E6>`_  '\\ua3e6'  Lo                  2  YI SYLLABLE JIE
     3  `U+A00B <https://codepoints.net/U+A00B>`_  '\\ua00b'  Lo                  2  YI SYLLABLE AP
     4  `U+A26C <https://codepoints.net/U+A26C>`_  '\\ua26c'  Lo                  2  YI SYLLABLE NGE
     5  `U+A010 <https://codepoints.net/U+A010>`_  '\\ua010'  Lo                  2  YI SYLLABLE OX
     6  `U+A1EC <https://codepoints.net/U+A1EC>`_  '\\ua1ec'  Lo                  2  YI SYLLABLE GO
     7  `U+A1E9 <https://codepoints.net/U+A1E9>`_  '\\ua1e9'  Lo                  2  YI SYLLABLE GUOP
     8  `U+A3E4 <https://codepoints.net/U+A3E4>`_  '\\ua3e4'  Lo                  2  YI SYLLABLE JIET
     9  `U+A1E2 <https://codepoints.net/U+A1E2>`_  '\\ua1e2'  Lo                  2  YI SYLLABLE GAT
    10  `U+A2AD <https://codepoints.net/U+A2AD>`_  '\\ua2ad'  Lo                  2  YI SYLLABLE ZYR
    11  `U+A425 <https://codepoints.net/U+A425>`_  '\\ua425'  Lo                  2  YI SYLLABLE JJO
    12  `U+A42F <https://codepoints.net/U+A42F>`_  '\\ua42f'  Lo                  2  YI SYLLABLE JJY
    13  `U+A00B <https://codepoints.net/U+A00B>`_  '\\ua00b'  Lo                  2  YI SYLLABLE AP
    14  `U+A489 <https://codepoints.net/U+A489>`_  '\\ua489'  Lo                  2  YI SYLLABLE YY
    15  `U+A489 <https://codepoints.net/U+A489>`_  '\\ua489'  Lo                  2  YI SYLLABLE YY
    16  `U+A138 <https://codepoints.net/U+A138>`_  '\\ua138'  Lo                  2  YI SYLLABLE DDI
   ===  =========================================  =========  ==========  =========  ================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x8f\xb1\xea\x8f\xa6\xea\x80\x8b\xea\x89\xac\xea\x80\x90\xea\x87\xac\xea\x87\xa9\xea\x8f\xa4\xea\x87\xa2\xea\x8a\xad\xea\x90\xa5\xea\x90\xaf\xea\x80\x8b\xea\x92\x89\xea\x92\x89\xea\x84\xb8|\\n12345678901234567890123456789012|\\n"
        ꏱꏦꀋꉬꀐꇬꇩꏤꇢꊭꐥꐯꀋꒉꒉꄸ|
        12345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 32,
  while *tabby* measures width -2.

.. _tabbylangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6258 <https://codepoints.net/U+6258>`_  '\\u6258'  Lo                  2  CJK UNIFIED IDEOGRAPH-6258
     2  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     3  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
     4  `U+7247 <https://codepoints.net/U+7247>`_  '\\u7247'  Lo                  2  CJK UNIFIED IDEOGRAPH-7247
     5  `U+513F <https://codepoints.net/U+513F>`_  '\\u513f'  Lo                  2  CJK UNIFIED IDEOGRAPH-513F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x89\x98\xe7\xae\xa1\xe5\x9c\xb0\xe7\x89\x87\xe5\x84\xbf|\\n1234567890|\\n"
        托管地片儿|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *tabby* measures width -14.

.. _tabbylangChineseMandarinTraditional:

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     2  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     3  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     4  `U+6B0A <https://codepoints.net/U+6B0A>`_  '\\u6b0a'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
     5  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
     6  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     7  `U+751F <https://codepoints.net/U+751F>`_  '\\u751f'  Lo                  2  CJK UNIFIED IDEOGRAPH-751F
     8  `U+547D <https://codepoints.net/U+547D>`_  '\\u547d'  Lo                  2  CJK UNIFIED IDEOGRAPH-547D
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xba\xba\xe4\xba\xba\xe6\x9c\x89\xe6\xac\x8a\xe4\xba\xab\xe6\x9c\x89\xe7\x94\x9f\xe5\x91\xbd|\\n1234567890123456|\\n"
        人人有權享有生命|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *tabby* measures width 10.

.. _tabbylangJinan:

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6258 <https://codepoints.net/U+6258>`_  '\\u6258'  Lo                  2  CJK UNIFIED IDEOGRAPH-6258
     2  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     3  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
     4  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x89\x98\xe7\xae\xa1\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678|\\n"
        托管领土|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -12.

.. _tabbylangChineseGan:

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6258 <https://codepoints.net/U+6258>`_  '\\u6258'  Lo                  2  CJK UNIFIED IDEOGRAPH-6258
     2  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     3  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
     4  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x89\x98\xe7\xae\xa1\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678|\\n"
        托管领土|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -12.

.. _tabbylangChineseHakka:

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6258 <https://codepoints.net/U+6258>`_  '\\u6258'  Lo                  2  CJK UNIFIED IDEOGRAPH-6258
     2  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     3  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
     4  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x89\x98\xe7\xae\xa1\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678|\\n"
        托管领土|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -12.

.. _tabbylangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6258 <https://codepoints.net/U+6258>`_  '\\u6258'  Lo                  2  CJK UNIFIED IDEOGRAPH-6258
     2  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     3  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
     4  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x89\x98\xe7\xae\xa1\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678|\\n"
        托管领土|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -12.

.. _tabbylangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
     2  `U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
     3  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     4  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     5  `U+8005 <https://codepoints.net/U+8005>`_  '\\u8005'  Lo                  2  CJK UNIFIED IDEOGRAPH-8005
     6  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     7  `U+9645 <https://codepoints.net/U+9645>`_  '\\u9645'  Lo                  2  CJK UNIFIED IDEOGRAPH-9645
     8  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     9  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
    10  `U+4F4D <https://codepoints.net/U+4F4D>`_  '\\u4f4d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F4D
    11  `U+4E4B <https://codepoints.net/U+4E4B>`_  '\\u4e4b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E4B
    12  `U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
    13  `U+540C <https://codepoints.net/U+540C>`_  '\\u540c'  Lo                  2  CJK UNIFIED IDEOGRAPH-540C
    14  `U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
    15  `U+8D81 <https://codepoints.net/U+8D81>`_  '\\u8d81'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D81
    16  `U+533A <https://codepoints.net/U+533A>`_  '\\u533a'  Lo                  2  CJK UNIFIED IDEOGRAPH-533A
    17  `U+522B <https://codepoints.net/U+522B>`_  '\\u522b'  Lo                  2  CJK UNIFIED IDEOGRAPH-522B
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 17


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\xa1\x8c\xe6\x94\xbf\xe7\x9a\x84\xe6\x88\x96\xe8\x80\x85\xe5\x9b\xbd\xe9\x99\x85\xe7\x9a\x84\xe5\x9c\xb0\xe4\xbd\x8d\xe4\xb9\x8b\xe4\xb8\x8d\xe5\x90\x8c\xe8\x80\x8c\xe8\xb6\x81\xe5\x8c\xba\xe5\x88\xab|\\n1234567890123456789012345678901234|\\n"
        行政的或者国际的地位之不同而趁区别|
        1234567890123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 34,
  while *tabby* measures width -2.

.. _tabbylangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+65E0 <https://codepoints.net/U+65E0>`_  '\\u65e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E0
     2  `U+8BBA <https://codepoints.net/U+8BBA>`_  '\\u8bba'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BBA
     3  `U+8BE5 <https://codepoints.net/U+8BE5>`_  '\\u8be5'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BE5
     4  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
     5  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
     6  `U+662F <https://codepoints.net/U+662F>`_  '\\u662f'  Lo                  2  CJK UNIFIED IDEOGRAPH-662F
     7  `U+72EC <https://codepoints.net/U+72EC>`_  '\\u72ec'  Lo                  2  CJK UNIFIED IDEOGRAPH-72EC
     8  `U+7ACB <https://codepoints.net/U+7ACB>`_  '\\u7acb'  Lo                  2  CJK UNIFIED IDEOGRAPH-7ACB
     9  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
    10  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x97\xa0\xe8\xae\xba\xe8\xaf\xa5\xe9\xa2\x86\xe5\x9c\x9f\xe6\x98\xaf\xe7\x8b\xac\xe7\xab\x8b\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678901234567890|\\n"
        无论该领土是独立领土|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *tabby* measures width -16.

.. _tabbylangChineseMandarinTianjin:

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
     2  `U+4E14 <https://codepoints.net/U+4E14>`_  '\\u4e14'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E14
     3  `U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
     4  `U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
     5  `U+56E0 <https://codepoints.net/U+56E0>`_  '\\u56e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-56E0
     6  `U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
     7  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     8  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
     9  `U+5C5E <https://codepoints.net/U+5C5E>`_  '\\u5c5e'  Lo                  2  CJK UNIFIED IDEOGRAPH-5C5E
    10  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    11  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    12  `U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
    13  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
    14  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
    15  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
    16  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    17  `U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
    18  `U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
    19  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe4\xb8\x94\xe4\xb8\x8d\xe5\xbe\x97\xe5\x9b\xa0\xe4\xb8\x80\xe4\xba\xba\xe6\x89\x80\xe5\xb1\x9e\xe7\x9a\x84\xe5\x9b\xbd\xe5\xae\xb6\xe6\x88\x96\xe9\xa2\x86\xe5\x9c\x9f\xe7\x9a\x84\xe6\x94\xbf\xe6\xb2\xbb\xe7\x9a\x84|\\n12345678901234567890123456789012345678|\\n"
        并且不得因一人所属的国家或领土的政治的|
        12345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 38,
  while *tabby* measures width 14.

.. _tabbylangChineseXiang:

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+65E0 <https://codepoints.net/U+65E0>`_  '\\u65e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E0
     2  `U+8BBA <https://codepoints.net/U+8BBA>`_  '\\u8bba'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BBA
     3  `U+8BE5 <https://codepoints.net/U+8BE5>`_  '\\u8be5'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BE5
     4  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
     5  `U+76D8 <https://codepoints.net/U+76D8>`_  '\\u76d8'  Lo                  2  CJK UNIFIED IDEOGRAPH-76D8
     6  `U+5B50 <https://codepoints.net/U+5B50>`_  '\\u5b50'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B50
     7  `U+662F <https://codepoints.net/U+662F>`_  '\\u662f'  Lo                  2  CJK UNIFIED IDEOGRAPH-662F
     8  `U+72EC <https://codepoints.net/U+72EC>`_  '\\u72ec'  Lo                  2  CJK UNIFIED IDEOGRAPH-72EC
     9  `U+7ACB <https://codepoints.net/U+7ACB>`_  '\\u7acb'  Lo                  2  CJK UNIFIED IDEOGRAPH-7ACB
    10  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
    11  `U+76D8 <https://codepoints.net/U+76D8>`_  '\\u76d8'  Lo                  2  CJK UNIFIED IDEOGRAPH-76D8
    12  `U+5B50 <https://codepoints.net/U+5B50>`_  '\\u5b50'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B50
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x97\xa0\xe8\xae\xba\xe8\xaf\xa5\xe5\x9c\xb0\xe7\x9b\x98\xe5\xad\x90\xe6\x98\xaf\xe7\x8b\xac\xe7\xab\x8b\xe5\x9c\xb0\xe7\x9b\x98\xe5\xad\x90|\\n123456789012345678901234|\\n"
        无论该地盘子是独立地盘子|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *tabby* measures width -12.

.. _tabbylangJapaneseTokyo:

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+3053 <https://codepoints.net/U+3053>`_  '\\u3053'  Lo                  2  HIRAGANA LETTER KO
     2  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     3  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     4  `U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
     5  `U+5BA3 <https://codepoints.net/U+5BA3>`_  '\\u5ba3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BA3
     6  `U+8A00 <https://codepoints.net/U+8A00>`_  '\\u8a00'  Lo                  2  CJK UNIFIED IDEOGRAPH-8A00
     7  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
     8  `U+516C <https://codepoints.net/U+516C>`_  '\\u516c'  Lo                  2  CJK UNIFIED IDEOGRAPH-516C
     9  `U+5E03 <https://codepoints.net/U+5E03>`_  '\\u5e03'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E03
    10  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
    11  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\x93\xe3\x81\xae\xe4\xba\xba\xe6\xa8\xa9\xe5\xae\xa3\xe8\xa8\x80\xe3\x82\x92\xe5\x85\xac\xe5\xb8\x83\xe3\x81\x99\xe3\x82\x8b|\\n1234567890123456789012|\\n"
        この人権宣言を公布する|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *tabby* measures width -30.

.. _tabbylangChineseMandarinSimplified:

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     2  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     3  `U+751F <https://codepoints.net/U+751F>`_  '\\u751f'  Lo                  2  CJK UNIFIED IDEOGRAPH-751F
     4  `U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
     5  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     6  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xba\xba\xe4\xba\xba\xe7\x94\x9f\xe8\x80\x8c\xe8\x87\xaa\xe7\x94\xb1|\\n123456789012|\\n"
        人人生而自由|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *tabby* measures width 6.

.. _tabbylangJapanese:

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+3053 <https://codepoints.net/U+3053>`_  '\\u3053'  Lo                  2  HIRAGANA LETTER KO
     2  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     3  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     4  `U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
     5  `U+5BA3 <https://codepoints.net/U+5BA3>`_  '\\u5ba3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BA3
     6  `U+8A00 <https://codepoints.net/U+8A00>`_  '\\u8a00'  Lo                  2  CJK UNIFIED IDEOGRAPH-8A00
     7  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
     8  `U+516C <https://codepoints.net/U+516C>`_  '\\u516c'  Lo                  2  CJK UNIFIED IDEOGRAPH-516C
     9  `U+5E03 <https://codepoints.net/U+5E03>`_  '\\u5e03'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E03
    10  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
    11  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\x93\xe3\x81\xae\xe4\xba\xba\xe6\xa8\xa9\xe5\xae\xa3\xe8\xa8\x80\xe3\x82\x92\xe5\x85\xac\xe5\xb8\x83\xe3\x81\x99\xe3\x82\x8b|\\n1234567890123456789012|\\n"
        この人権宣言を公布する|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *tabby* measures width -34.

.. _tabbylangJapaneseOsaka:

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+3053 <https://codepoints.net/U+3053>`_  '\\u3053'  Lo                  2  HIRAGANA LETTER KO
     2  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     3  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     4  `U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
     5  `U+5BA3 <https://codepoints.net/U+5BA3>`_  '\\u5ba3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BA3
     6  `U+8A00 <https://codepoints.net/U+8A00>`_  '\\u8a00'  Lo                  2  CJK UNIFIED IDEOGRAPH-8A00
     7  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
     8  `U+516C <https://codepoints.net/U+516C>`_  '\\u516c'  Lo                  2  CJK UNIFIED IDEOGRAPH-516C
     9  `U+5E03 <https://codepoints.net/U+5E03>`_  '\\u5e03'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E03
    10  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
    11  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\x93\xe3\x81\xae\xe4\xba\xba\xe6\xa8\xa9\xe5\xae\xa3\xe8\xa8\x80\xe3\x82\x92\xe5\x85\xac\xe5\xb8\x83\xe3\x81\x99\xe3\x82\x8b|\\n1234567890123456789012|\\n"
        この人権宣言を公布する|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *tabby* measures width -34.

.. _tabbylangThai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0E42 <https://codepoints.net/U+0E42>`_  '\\u0e42'  Lo                  1  THAI CHARACTER SARA O
     2  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
     3  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
     4  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
     5  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     6  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     7  `U+0E04 <https://codepoints.net/U+0E04>`_  '\\u0e04'  Lo                  1  THAI CHARACTER KHO KHWAI
     8  `U+0E33 <https://codepoints.net/U+0E33>`_  '\\u0e33'  Lo                  1  THAI CHARACTER SARA AM
     9  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    10  `U+0E36 <https://codepoints.net/U+0E36>`_  '\\u0e36'  Mn                  0  THAI CHARACTER SARA UE
    11  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
    12  `U+0E16 <https://codepoints.net/U+0E16>`_  '\\u0e16'  Lo                  1  THAI CHARACTER THO THUNG
    13  `U+0E36 <https://codepoints.net/U+0E36>`_  '\\u0e36'  Mn                  0  THAI CHARACTER SARA UE
    14  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
    15  `U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
    16  `U+0E0F <https://codepoints.net/U+0E0F>`_  '\\u0e0f'  Lo                  1  THAI CHARACTER TO PATAK
    17  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    18  `U+0E0D <https://codepoints.net/U+0E0D>`_  '\\u0e0d'  Lo                  1  THAI CHARACTER YO YING
    19  `U+0E0D <https://codepoints.net/U+0E0D>`_  '\\u0e0d'  Lo                  1  THAI CHARACTER YO YING
    20  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    21  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    22  `U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
    23  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
    24  `U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
    25  `U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
    26  `U+0E47 <https://codepoints.net/U+0E47>`_  '\\u0e47'  Mn                  0  THAI CHARACTER MAITAIKHU
    27  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    28  `U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
    29  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    30  `U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
    31  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
    32  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
    33  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    34  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    35  `U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
    36  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
    37  `U+0E4C <https://codepoints.net/U+0E4C>`_  '\\u0e4c'  Mn                  0  THAI CHARACTER THANTHAKHAT
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 37


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x82\xe0\xb8\x94\xe0\xb8\xa2\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\x84\xe0\xb8\xb3\xe0\xb8\x99\xe0\xb8\xb6\xe0\xb8\x87\xe0\xb8\x96\xe0\xb8\xb6\xe0\xb8\x87\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xb5\xe0\xb9\x89\xe0\xb9\x80\xe0\xb8\x9b\xe0\xb9\x87\xe0\xb8\x99\xe0\xb9\x80\xe0\xb8\x99\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb8\x87\xe0\xb8\x99\xe0\xb8\xb4\xe0\xb8\x95\xe0\xb8\xa2\xe0\xb9\x8c|\\n1234567890123456789012345678|\\n"
        โดยการคำนึงถึงปฏิญญานี้เป็นเนืองนิตย์|
        1234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 28,
  while *tabby* measures width 0.

.. _tabbylangChineseYue:

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5514 <https://codepoints.net/U+5514>`_  '\\u5514'  Lo                  2  CJK UNIFIED IDEOGRAPH-5514
     2  `U+8BBA <https://codepoints.net/U+8BBA>`_  '\\u8bba'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BBA
     3  `U+8BE5 <https://codepoints.net/U+8BE5>`_  '\\u8be5'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BE5
     4  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
     5  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
     6  `U+4FC2 <https://codepoints.net/U+4FC2>`_  '\\u4fc2'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FC2
     7  `U+72EC <https://codepoints.net/U+72EC>`_  '\\u72ec'  Lo                  2  CJK UNIFIED IDEOGRAPH-72EC
     8  `U+7ACB <https://codepoints.net/U+7ACB>`_  '\\u7acb'  Lo                  2  CJK UNIFIED IDEOGRAPH-7ACB
     9  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
    10  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x94\x94\xe8\xae\xba\xe8\xaf\xa5\xe9\xa2\x86\xe5\x9c\x9f\xe4\xbf\x82\xe7\x8b\xac\xe7\xab\x8b\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678901234567890|\\n"
        唔论该领土係独立领土|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *tabby* measures width -14.

.. _tabbylangChineseMandarinGuiyang:

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+65E0 <https://codepoints.net/U+65E0>`_  '\\u65e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E0
     2  `U+8BBA <https://codepoints.net/U+8BBA>`_  '\\u8bba'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BBA
     3  `U+8BE5 <https://codepoints.net/U+8BE5>`_  '\\u8be5'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BE5
     4  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
     5  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
     6  `U+662F <https://codepoints.net/U+662F>`_  '\\u662f'  Lo                  2  CJK UNIFIED IDEOGRAPH-662F
     7  `U+72EC <https://codepoints.net/U+72EC>`_  '\\u72ec'  Lo                  2  CJK UNIFIED IDEOGRAPH-72EC
     8  `U+7ACB <https://codepoints.net/U+7ACB>`_  '\\u7acb'  Lo                  2  CJK UNIFIED IDEOGRAPH-7ACB
     9  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
    10  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x97\xa0\xe8\xae\xba\xe8\xaf\xa5\xe9\xa2\x86\xe5\x9c\x9f\xe6\x98\xaf\xe7\x8b\xac\xe7\xab\x8b\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678901234567890|\\n"
        无论该领土是独立领土|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *tabby* measures width -16.

.. _tabbylangChineseWu:

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6258 <https://codepoints.net/U+6258>`_  '\\u6258'  Lo                  2  CJK UNIFIED IDEOGRAPH-6258
     2  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     3  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
     4  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x89\x98\xe7\xae\xa1\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678|\\n"
        托管领土|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width -14.

.. _tabbylangChineseMinNan:

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6258 <https://codepoints.net/U+6258>`_  '\\u6258'  Lo                  2  CJK UNIFIED IDEOGRAPH-6258
     2  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     3  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x89\x98\xe7\xae\xa1\xe5\x9c\xb0|\\n123456|\\n"
        托管地|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width -12.

.. _tabbylangLao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0EAB <https://codepoints.net/U+0EAB>`_  '\\u0eab'  Lo                  1  LAO LETTER HO SUNG
     2  `U+0EBC <https://codepoints.net/U+0EBC>`_  '\\u0ebc'  Mn                  0  LAO SEMIVOWEL SIGN LO
     3  `U+0EB7 <https://codepoints.net/U+0EB7>`_  '\\u0eb7'  Mn                  0  LAO VOWEL SIGN YY
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xba\xab\xe0\xba\xbc\xe0\xba\xb7|\\n1|\\n"
        ຫຼື|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *tabby* measures width -31.

.. _tabbylangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===========================
     1  `U+6CD5 <https://codepoints.net/U+6CD5>`_          '\\u6cd5'      Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     2  `U+6B0A <https://codepoints.net/U+6B0A>`_          '\\u6b0a'      Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
     3  `U+548D <https://codepoints.net/U+548D>`_          '\\u548d'      Lo                  2  CJK UNIFIED IDEOGRAPH-548D
     4  `U+570B <https://codepoints.net/U+570B>`_          '\\u570b'      Lo                  2  CJK UNIFIED IDEOGRAPH-570B
     5  `U+969B <https://codepoints.net/U+969B>`_          '\\u969b'      Lo                  2  CJK UNIFIED IDEOGRAPH-969B
     6  `U+00027D51 <https://codepoints.net/U+00027D51>`_  '\\U00027d51'  Lo                  2  CJK UNIFIED IDEOGRAPH-27D51
     7  `U+570B <https://codepoints.net/U+570B>`_          '\\u570b'      Lo                  2  CJK UNIFIED IDEOGRAPH-570B
     8  `U+5BB6 <https://codepoints.net/U+5BB6>`_          '\\u5bb6'      Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
     9  `U+548D <https://codepoints.net/U+548D>`_          '\\u548d'      Lo                  2  CJK UNIFIED IDEOGRAPH-548D
    10  `U+9818 <https://codepoints.net/U+9818>`_          '\\u9818'      Lo                  2  CJK UNIFIED IDEOGRAPH-9818
    11  `U+571F <https://codepoints.net/U+571F>`_          '\\u571f'      Lo                  2  CJK UNIFIED IDEOGRAPH-571F
    12  `U+000264E1 <https://codepoints.net/U+000264E1>`_  '\\U000264e1'  Lo                  2  CJK UNIFIED IDEOGRAPH-264E1
    13  `U+00020B20 <https://codepoints.net/U+00020B20>`_  '\\U00020b20'  Lo                  2  CJK UNIFIED IDEOGRAPH-20B20
    14  `U+0002029B <https://codepoints.net/U+0002029B>`_  '\\U0002029b'  Lo                  2  CJK UNIFIED IDEOGRAPH-2029B
    15  `U+51FA <https://codepoints.net/U+51FA>`_          '\\u51fa'      Lo                  2  CJK UNIFIED IDEOGRAPH-51FA
    16  `U+8EAB <https://codepoints.net/U+8EAB>`_          '\\u8eab'      Lo                  2  CJK UNIFIED IDEOGRAPH-8EAB
   ===  =================================================  =============  ==========  =========  ===========================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xb3\x95\xe6\xac\x8a\xe5\x92\x8d\xe5\x9c\x8b\xe9\x9a\x9b\xf0\xa7\xb5\x91\xe5\x9c\x8b\xe5\xae\xb6\xe5\x92\x8d\xe9\xa0\x98\xe5\x9c\x9f\xf0\xa6\x93\xa1\xf0\xa0\xac\xa0\xf0\xa0\x8a\x9b\xe5\x87\xba\xe8\xba\xab|\\n12345678901234567890123456789012|\\n"
        法權咍國際𧵑國家咍領土𦓡𠬠𠊛出身|
        12345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 32,
  while *tabby* measures width 4.

.. _tabbylangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
     4  `U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'    Ll                  1  LATIN SMALL LETTER N WITH TILDE
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xcc\x83e'\xc3\xb1e|\\n1234|\\n"
        ̃e'ñe|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width 5.

.. _tabbylangThai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================
     1  `U+0E43 <https://codepoints.net/U+0E43>`_  '\\u0e43'  Lo                  1  THAI CHARACTER SARA AI MAIMUAN
     2  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
     3  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
     4  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
     5  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
     6  `U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
     7  `U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
     8  `U+0E48 <https://codepoints.net/U+0E48>`_  '\\u0e48'  Mn                  0  THAI CHARACTER MAI EK
     9  `U+0E08 <https://codepoints.net/U+0E08>`_  '\\u0e08'  Lo                  1  THAI CHARACTER CHO CHAN
    10  `U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
    11  `U+0E43 <https://codepoints.net/U+0E43>`_  '\\u0e43'  Lo                  1  THAI CHARACTER SARA AI MAIMUAN
    12  `U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
    13  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
    14  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
    15  `U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
    16  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    17  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    18  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    19  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
    20  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
    21  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
    22  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    23  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    24  `U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
    25  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    26  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    27  `U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
    28  `U+0E16 <https://codepoints.net/U+0E16>`_  '\\u0e16'  Lo                  1  THAI CHARACTER THO THUNG
    29  `U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
    30  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
   ===  =========================================  =========  ==========  =========  ==============================

Total codepoints: 30


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x83\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xb1\xe0\xb8\x99\xe0\xb8\x97\xe0\xb8\xb5\xe0\xb9\x88\xe0\xb8\x88\xe0\xb8\xb0\xe0\xb9\x83\xe0\xb8\xab\xe0\xb9\x89\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb8\xad\xe0\xb8\xa1\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x99\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x96\xe0\xb8\xb7\xe0\xb8\xad|\\n1234567890123456789012|\\n"
        ในอันที่จะให้มีการยอมรับนับถือ|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *tabby* measures width -24.

.. _tabbylangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     2  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     4  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     5  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     6  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     8  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     9  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
    10  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "itt\xc3\xadllawwi|\\n1234567890|\\n"
        ittíllawwi|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *tabby* measures width 3.

.. _tabbylangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     2  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     6  `U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'   Ll                  1  LATIN SMALL LETTER U WITH ACUTE
     7  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     8  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     9  `U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xadmity\xc3\xbane.|\\n123456789|\\n"
        ímityúne.|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *tabby* measures width -5.

.. _tabbylangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
     2  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     3  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
     4  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
     5  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     6  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     7  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
     8  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     9  `U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
    10  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbc\xd1\x83\xd1\x82\xd1\x82\xd1\x8d\xd0\xb8\xd1\x82\xd1\x8d\xd0\xbc\xd0\xb8|\\n1234567890|\\n"
        муттэитэми|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *tabby* measures width 4.

.. _tabbylangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     5  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     8  `U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
     9  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
    10  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
    11  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "quescaaquin|\\n12345678901|\\n"
        quescaaquin|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *tabby* measures width 6.

.. _tabbylangGumuz:

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     6  `U+0066 <https://codepoints.net/U+0066>`_  'f'        Ll                  1  LATIN SMALL LETTER F
     7  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     8  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     9  `U+A78C <https://codepoints.net/U+A78C>`_  '\\ua78c'  Ll                  1  LATIN SMALL LETTER SALTILLO
    10  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    11  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
    12  `U+A78C <https://codepoints.net/U+A78C>`_  '\\ua78c'  Ll                  1  LATIN SMALL LETTER SALTILLO
    13  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
    14  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kamaafuc\xea\x9e\x8cak\xea\x9e\x8cwa|\\n12345678901234|\\n"
        kamaafucꞌakꞌwa|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *tabby* measures width 3.

.. _tabbylangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ============================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     2  `U+0327 <https://codepoints.net/U+0327>`_  '\\u0327'  Mn                  0  COMBINING CEDILLA
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     5  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     6  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     8  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     9  `U+0131 <https://codepoints.net/U+0131>`_  '\\u0131'  Ll                  1  LATIN SMALL LETTER DOTLESS I
   ===  =========================================  =========  ==========  =========  ============================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "s\xcc\xa7artlar\xc4\xb1|\\n12345678|\\n"
        şartları|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 3.

.. _tabbylangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     3  `U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     5  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     6  `U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'    Ll                  1  LATIN SMALL LETTER O WITH ACUTE
     7  `U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'    Ll                  1  LATIN SMALL LETTER O WITH ACUTE
     8  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     9  `U+0105 <https://codepoints.net/U+0105>`_  '\\u0105'  Ll                  1  LATIN SMALL LETTER A WITH OGONEK
    10  `U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
    11  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
    12  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
    13  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
    14  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "do\xca\xbcah\xc3\xb3\xc3\xb3t\xc4\x85\xca\xbc\xc3\xadg\xc3\xad\xc3\xad|\\n12345678901234|\\n"
        doʼahóótąʼígíí|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *tabby* measures width 11.

.. _tabbylangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0422 <https://codepoints.net/U+0422>`_  '\\u0422'  Lu                  1  CYRILLIC CAPITAL LETTER TE
     2  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     3  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     4  `U+0306 <https://codepoints.net/U+0306>`_  '\\u0306'  Mn                  0  COMBINING BREVE
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xa2\xd1\x8d\xd0\xb8\xcc\x86|\\n123|\\n"
        Тэй|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -7.

.. _tabbylangAmarakaeri:

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "huadak|\\n123456|\\n"
        huadak|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 1.

.. _tabbylangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
     2  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Iye|\\n123|\\n"
        Iye|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -2.

.. _tabbylangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================================
     1  `U+049B <https://codepoints.net/U+049B>`_  '\\u049b'  Ll                  1  CYRILLIC SMALL LETTER KA WITH DESCENDER
     2  `U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
     3  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     4  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
     5  `U+044C <https://codepoints.net/U+044C>`_  '\\u044c'  Ll                  1  CYRILLIC SMALL LETTER SOFT SIGN
     6  `U+0433 <https://codepoints.net/U+0433>`_  '\\u0433'  Ll                  1  CYRILLIC SMALL LETTER GHE
     7  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     8  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
   ===  =========================================  =========  ==========  =========  =======================================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd2\x9b\xca\xbc\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb3\xd1\x83\xd0\xbd|\\n12345678|\\n"
        қʼатьгун|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 4.

.. _tabbylangVeps:

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "meles|\\n12345|\\n"
        meles|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width -2.

.. _tabbylangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     2  `U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
     3  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     4  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     5  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
     6  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     7  `U+044B <https://codepoints.net/U+044B>`_  '\\u044b'  Ll                  1  CYRILLIC SMALL LETTER YERU
     8  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     9  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
    10  `U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
    11  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
    12  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb0\xd1\x8f\xd1\x80\xd0\xb0\xd0\xbb\xd0\xb4\xd1\x8b\xcc\x84\xd0\xb4\xd1\x8f\xd0\xbd\xd0\xb0|\\n12345678901|\\n"
        аяралды̄дяна|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *tabby* measures width 1.

.. _tabbylangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     7  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     9  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
    10  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
    11  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
    12  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
    13  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
    14  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
    15  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
    16  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
    17  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
    18  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tsi'sisikua'ija're|\\n123456789012345678|\\n"
        tsi'sisikua'ija're|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *tabby* measures width 11.

.. _tabbylangKorean:

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+C591 <https://codepoints.net/U+C591>`_  '\\uc591'  Lo                  2  HANGUL SYLLABLE YANG
     2  `U+C2EC <https://codepoints.net/U+C2EC>`_  '\\uc2ec'  Lo                  2  HANGUL SYLLABLE SIM
     3  `U+C744 <https://codepoints.net/U+C744>`_  '\\uc744'  Lo                  2  HANGUL SYLLABLE EUL
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x96\x91\xec\x8b\xac\xec\x9d\x84|\\n123456|\\n"
        양심을|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 0.

.. _tabbylangColorado:

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     2  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     4  `U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "eke.|\\n1234|\\n"
        eke.|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -4.

.. _tabbylangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+05D0 <https://codepoints.net/U+05D0>`_  '\\u05d0'  Lo                  1  HEBREW LETTER ALEF
     2  `U+05D5 <https://codepoints.net/U+05D5>`_  '\\u05d5'  Lo                  1  HEBREW LETTER VAV
     3  `U+05DF <https://codepoints.net/U+05DF>`_  '\\u05df'  Lo                  1  HEBREW LETTER FINAL NUN
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x90\xd7\x95\xd7\x9f|\\n123|\\n"
        און|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 0.

.. _tabbylangTicuna:

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "name|\\n1234|\\n"
        name|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -4.

.. _tabbylangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "akk|\\n123|\\n"
        akk|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -5.

.. _tabbylangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+C0AC <https://codepoints.net/U+C0AC>`_  '\\uc0ac'  Lo                  2  HANGUL SYLLABLE SA
     2  `U+D68C <https://codepoints.net/U+D68C>`_  '\\ud68c'  Lo                  2  HANGUL SYLLABLE HOE
     3  `U+CD9C <https://codepoints.net/U+CD9C>`_  '\\ucd9c'  Lo                  2  HANGUL SYLLABLE CUL
     4  `U+C2E0 <https://codepoints.net/U+C2E0>`_  '\\uc2e0'  Lo                  2  HANGUL SYLLABLE SIN
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x82\xac\xed\x9a\x8c\xec\xb6\x9c\xec\x8b\xa0|\\n12345678|\\n"
        사회출신|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 3.

.. _tabbylangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =============================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =============================
     1  `U+0001E927 <https://codepoints.net/U+0001E927>`_  '\\U0001e927'  Ll                  1  ADLAM SMALL LETTER SINNYIIYHE
     2  `U+0001E922 <https://codepoints.net/U+0001E922>`_  '\\U0001e922'  Ll                  1  ADLAM SMALL LETTER ALIF
     3  `U+0001E92A <https://codepoints.net/U+0001E92A>`_  '\\U0001e92a'  Ll                  1  ADLAM SMALL LETTER RA
     4  `U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
     5  `U+0001E945 <https://codepoints.net/U+0001E945>`_  '\\U0001e945'  Mn                  0  ADLAM VOWEL LENGTHENER
   ===  =================================================  =============  ==========  =========  =============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xa7\xf0\x9e\xa4\xa2\xf0\x9e\xa4\xaa\xf0\x9e\xa4\xab\xf0\x9e\xa5\x85|\\n1234|\\n"
        𞤧𞤢𞤪𞤫𞥅|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -8.

.. _tabbylangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     2  `U+0636 <https://codepoints.net/U+0636>`_  '\\u0636'  Lo                  1  ARABIC LETTER DAD
     3  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     4  `U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
     5  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
     6  `U+064B <https://codepoints.net/U+064B>`_  '\\u064b'  Mn                  0  ARABIC FATHATAN
     7  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88\xd8\xb6\xd9\x85\xd9\x8a\xd8\xb1\xd9\x8b\xd8\xa7|\\n123456|\\n"
        وضميرًا|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 2.

.. _tabbylangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

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
  while *tabby* measures width -5.

.. _tabbylangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004E <https://codepoints.net/U+004E>`_  'N'       Lu                  1  LATIN CAPITAL LETTER N
     2  `U+0044 <https://codepoints.net/U+0044>`_  'D'       Lu                  1  LATIN CAPITAL LETTER D
     3  `U+0045 <https://codepoints.net/U+0045>`_  'E'       Lu                  1  LATIN CAPITAL LETTER E
     4  `U+0056 <https://codepoints.net/U+0056>`_  'V'       Lu                  1  LATIN CAPITAL LETTER V
     5  `U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
     6  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     7  `U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "NDEVA'A|\\n1234567|\\n"
        NDEVA'A|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 3.

.. _tabbylangMaldivian:

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0789 <https://codepoints.net/U+0789>`_  '\\u0789'  Lo                  1  THAANA LETTER MEEMU
     2  `U+07A7 <https://codepoints.net/U+07A7>`_  '\\u07a7'  Mn                  0  THAANA AABAAFILI
     3  `U+0799 <https://codepoints.net/U+0799>`_  '\\u0799'  Lo                  1  THAANA LETTER HHAA
     4  `U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
     5  `U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
     6  `U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
     7  `U+078D <https://codepoints.net/U+078D>`_  '\\u078d'  Lo                  1  THAANA LETTER LAAMU
     8  `U+07AC <https://codepoints.net/U+07AC>`_  '\\u07ac'  Mn                  0  THAANA EBEFILI
     9  `U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
    10  `U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
    11  `U+078E <https://codepoints.net/U+078E>`_  '\\u078e'  Lo                  1  THAANA LETTER GAAFU
    12  `U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
    13  `U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
    14  `U+07A8 <https://codepoints.net/U+07A8>`_  '\\u07a8'  Mn                  0  THAANA IBIFILI
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x89\xde\xa7\xde\x99\xde\xa6\xde\x87\xde\xaa\xde\x8d\xde\xac\xde\x87\xde\xb0\xde\x8e\xde\xa6\xde\x87\xde\xa8|\\n1234567|\\n"
        މާޙައުލެއްގައި|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 4.

.. _tabbylangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     2  `U+0269 <https://codepoints.net/U+0269>`_  '\\u0269'  Ll                  1  LATIN SMALL LETTER IOTA
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     4  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "r\xc9\xa9\xcc\x81\xc5\x8ba|\\n1234|\\n"
        rɩ́ŋa|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -3.

.. _tabbylangw:

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
  while *tabby* measures width -6.

.. _tabbylangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "destes|\\n123456|\\n"
        destes|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width -1.

.. _tabbylangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
     2  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     5  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     7  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     9  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
    10  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xa8gadjemint|\\n1234567890|\\n"
        ègadjemint|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *tabby* measures width 7.

.. _tabbylangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0715 <https://codepoints.net/U+0715>`_  '\\u0715'  Lo                  1  SYRIAC LETTER DALATH
     2  `U+071A <https://codepoints.net/U+071A>`_  '\\u071a'  Lo                  1  SYRIAC LETTER HETH
     3  `U+0715 <https://codepoints.net/U+0715>`_  '\\u0715'  Lo                  1  SYRIAC LETTER DALATH
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\x95\xdc\x9a\xdc\x95|\\n123|\\n"
        ܕܚܕ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -1.

.. _tabbylangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "an|\\n12|\\n"
        an|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -9.

.. _tabbylangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "atu|\\n123|\\n"
        atu|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -1.

.. _tabbylangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     3  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     4  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     7  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ny\xc9\x94\xcc\x81ns\xc9\x94|\\n123456|\\n"
        nyɔ́nsɔ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 2.

.. _tabbylangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     2  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     3  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     4  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     5  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     6  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x85\xdb\x8c\xd8\xa7\xdb\x8c\xd9\x86\xd8\xaf|\\n123456|\\n"
        میایند|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 1.

.. _tabbylangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     5  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     7  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     8  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tamatawt|\\n12345678|\\n"
        tamatawt|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 1.

.. _tabbylangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     2  `U+01CE <https://codepoints.net/U+01CE>`_  '\\u01ce'  Ll                  1  LATIN SMALL LETTER A WITH CARON
     3  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     4  `U+0268 <https://codepoints.net/U+0268>`_  '\\u0268'  Ll                  1  LATIN SMALL LETTER I WITH STROKE
     5  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "k\xc7\x8e\xcc\xb1\xc9\xa8.|\\n1234|\\n"
        kǎ̱ɨ.|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -3.

.. _tabbylangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     2  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     3  `U+0654 <https://codepoints.net/U+0654>`_  '\\u0654'  Mn                  0  ARABIC HAMZA ABOVE
     4  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     5  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     6  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaa\xd8\xa7\xd9\x94\xd9\x85\xdb\x8c\xd9\x86|\\n12345|\\n"
        تأمین|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width -3.

.. _tabbylangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     3  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "y\xc9\x9b\xcc\x83|\\n12|\\n"
        yɛ̃|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -2.

.. _tabbylangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "h\xc9\x9bi|\\n123|\\n"
        hɛi|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -3.

.. _tabbylangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nesta|\\n12345|\\n"
        nesta|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width -4.

.. _tabbylangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "le\xcc\x81|\\n12|\\n"
        lé|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -7.

.. _tabbylangUduk:

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+1E35 <https://codepoints.net/U+1E35>`_  '\\u1e35'  Ll                  1  LATIN SMALL LETTER K WITH LINE BELOW
     5  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     7  `U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
     8  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
   ===  =========================================  =========  ==========  =========  ====================================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nya\xe1\xb8\xb5ka\xe2\x80\x99d|\\n12345678|\\n"
        nyaḵka’d|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *tabby* measures width 5.

.. _tabbylangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     3  `U+0302 <https://codepoints.net/U+0302>`_  '\\u0302'  Mn                  0  COMBINING CIRCUMFLEX ACCENT
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gu\xcc\x82|\\n12|\\n"
        gû|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -4.

.. _tabbylangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'   Ll                  1  LATIN SMALL LETTER U WITH ACUTE
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     4  `U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'   Ll                  1  LATIN SMALL LETTER U WITH ACUTE
     5  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     6  `U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'   Ll                  1  LATIN SMALL LETTER U WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc3\xbat\xc3\xbat\xc3\xba|\\n123456|\\n"
        tútútú|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 0.

.. _tabbylangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

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
  while *tabby* measures width -1.

.. _tabbylangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
     4  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     6  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "je\xc5\x8bmaji|\\n1234567|\\n"
        jeŋmaji|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *tabby* measures width 4.

.. _tabbylangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ko|\\n12|\\n"
        ko|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -6.

.. _tabbylangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     2  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     3  `U+06BA <https://codepoints.net/U+06BA>`_  '\\u06ba'  Lo                  1  ARABIC LETTER NOON GHUNNA
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaa\xd9\x88\xda\xba|\\n123|\\n"
        توں|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 0.

.. _tabbylangChinantecChiltepec:

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     3  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yo\xcc\xb1|\\n12|\\n"
        yo̱|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -3.

.. _tabbylangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+00F5 <https://codepoints.net/U+00F5>`_  '\\xf5'   Ll                  1  LATIN SMALL LETTER O WITH TILDE
     3  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "s\xc3\xb5ma|\\n1234|\\n"
        sõma|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width 1.

.. _tabbylangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     2  `U+1EB9 <https://codepoints.net/U+1EB9>`_  '\\u1eb9'  Ll                  1  LATIN SMALL LETTER E WITH DOT BELOW
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "j\xe1\xba\xb9\xcc\x81|\\n12|\\n"
        jẹ́|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width 0.

.. _tabbylangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================================
     1  `U+0110 <https://codepoints.net/U+0110>`_  '\\u0110'  Lu                  1  LATIN CAPITAL LETTER D WITH STROKE
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ==================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc4\x90a\xcc\xa3i|\\n123|\\n"
        Đại|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 0.

.. _tabbylangDagaareSouthern:

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ne\xc9\x9b|\\n123|\\n"
        neɛ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -4.

.. _tabbylangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pudi|\\n1234|\\n"
        pudi|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width 0.

.. _tabbylangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     2  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'    Ll                  1  LATIN SMALL LETTER E WITH GRAVE
     3  `U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
     4  `U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
     5  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "y\xc3\xa8\xe2\x80\x99\xc3\xa9y|\\n12345|\\n"
        yè’éy|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 1.

.. _tabbylangUrdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
     2  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     3  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     4  `U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaf\xdb\x8c\xd9\x86\xdb\x92|\\n1234|\\n"
        دینے|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *tabby* measures width -2.

.. _tabbylangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+0632 <https://codepoints.net/U+0632>`_  '\\u0632'  Lo                  1  ARABIC LETTER ZAIN
     3  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     4  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
     5  `U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
     6  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd8\xb2\xd8\xa7\xd8\xaf\xd9\x8a\xd9\x88|\\n123456|\\n"
        ازاديو|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *tabby* measures width 4.

.. _tabbylangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
     2  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaf\xdb\x8c|\\n12|\\n"
        دی|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -2.

.. _tabbylangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     2  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ij|\\n12|\\n"
        ij|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -2.

.. _tabbylangUrdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     2  `U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
     3  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     4  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     5  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaa\xd9\x82\xd9\x88\xdb\x8c\xd8\xaa|\\n12345|\\n"
        تقویت|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 3.

.. _tabbylangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kemen|\\n12345|\\n"
        kemen|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *tabby* measures width 2.

.. _tabbylangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004B <https://codepoints.net/U+004B>`_  'K'       Lu                  1  LATIN CAPITAL LETTER K
     2  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Kpa|\\n123|\\n"
        Kpa|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -4.

.. _tabbylangSererSine:

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "baa|\\n123|\\n"
        baa|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -6.

.. _tabbylangDangme:

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0042 <https://codepoints.net/U+0042>`_  'B'        Lu                  1  LATIN CAPITAL LETTER B
     2  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     3  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Bl\xc9\x94|\\n123|\\n"
        Blɔ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width -1.

.. _tabbylangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc9\x94n|\\n123|\\n"
        tɔn|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 0.

.. _tabbylangTaiDam:

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+AAB5 <https://codepoints.net/U+AAB5>`_  '\\uaab5'  Lo                  1  TAI VIET VOWEL E
     2  `U+AA94 <https://codepoints.net/U+AA94>`_  '\\uaa94'  Lo                  1  TAI VIET LETTER LOW TO
     3  `U+AA89 <https://codepoints.net/U+AA89>`_  '\\uaa89'  Lo                  1  TAI VIET LETTER HIGH NGO
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xb5\xea\xaa\x94\xea\xaa\x89|\\n123|\\n"
        ꪵꪔꪉ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *tabby* measures width 1.

.. _tabbylangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+0F61 <https://codepoints.net/U+0F61>`_  '\\u0f61'  Lo                  1  TIBETAN LETTER YA
     2  `U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa1\xe0\xbd\xa2|\\n12|\\n"
        ཡར|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -1.

.. _tabbylangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
     2  `U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
     3  `U+0FB2 <https://codepoints.net/U+0FB2>`_  '\\u0fb2'  Mn                  0  TIBETAN SUBJOINED LETTER RA
     4  `U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa0\xe0\xbd\x82\xe0\xbe\xb2\xe0\xbd\xbc|\\n12|\\n"
        འགྲོ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *tabby* measures width -2.

.. _tabbydecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

DEC private modes results for *tabby*: 19 changeable modes
of 23 supported out of 159 total modes tested (14.5% support, 11.9% changeable).

Complete list of DEC private modes tested:

.. _tabbydecmode1:

.. _tabbydecmode6:

.. _tabbydecmode7:

.. _tabbydecmode9:

.. _tabbydecmode12:

.. _tabbydecmode25:

.. _tabbydecmode45:

.. _tabbydecmode47:

.. _tabbydecmode66:

.. _tabbydecmode1000:

.. _tabbydecmode1002:

.. _tabbydecmode1003:

.. _tabbydecmode1004:

.. _tabbydecmode1006:

.. _tabbydecmode1016:

.. _tabbydecmode1047:

.. _tabbydecmode1048:

.. _tabbydecmode1049:

.. _tabbydecmode2004:

.. table::
   :class: sphinx-datatable

   ======  =============================  =======================================================================  ===========  ============  =========
     Mode  Name                           Description                                                              Supported    Changeable    Enabled
   ======  =============================  =======================================================================  ===========  ============  =========
        1  DECCKM                         Cursor Keys Mode                                                         Yes          Yes           No
        2  DECANM                         ANSI/VT52 Mode                                                           No           No            No
        3  DECCOLM                        Column Mode                                                              No           No            No
        4  DECSCLM                        Scrolling Mode                                                           No           No            No
        5  DECSCNM                        Screen Mode (light or dark screen)                                       No           No            No
        6  DECOM                          Origin Mode                                                              Yes          Yes           No
        7  DECAWM                         Auto Wrap Mode                                                           Yes          Yes           Yes
        8  DECARM                         Auto Repeat Mode                                                         Yes          No            Yes
        9  DECINLM                        Interlace Mode / Mouse X10 tracking                                      Yes          Yes           No
       10  DECEDM                         Editing Mode / Show toolbar (rxvt)                                       No           No            No
       11  DECLTM                         Line Transmit Mode                                                       No           No            No
       12  DECKANAM                       Katakana Shift Mode / Blinking cursor (xterm)                            Yes          Yes           No
       13  DECSCFDM                       Space Compression/Field Delimiter Mode / Start blinking cursor (xterm)   No           No            No
       14  DECTEM                         Transmit Execution Mode / Enable XOR of blinking cursor control (xterm)  No           No            No
       16  DECEKEM                        Edit Key Execution Mode                                                  No           No            No
       18  DECPFF                         Print Form Feed                                                          No           No            No
       19  DECPEX                         Printer Extent                                                           No           No            No
       20  OV1                            Overstrike                                                               No           No            No
       21  BA1                            Local BASIC                                                              No           No            No
       22  BA2                            Host BASIC                                                               No           No            No
       23  PK1                            Programmable Keypad                                                      No           No            No
       24  AH1                            Auto Hardcopy                                                            No           No            No
       25  DECTCEM                        Text Cursor Enable Mode                                                  Yes          Yes           Yes
       27  DECPSP                         Proportional Spacing                                                     No           No            No
       29  DECPSM                         Pitch Select Mode                                                        No           No            No
       30  SHOW_SCROLLBAR_RXVT            Show scrollbar (rxvt)                                                    No           No            No
       34  DECRLM                         Cursor Right to Left Mode                                                No           No            No
       35  DECHEBM                        Hebrew (Keyboard) Mode / Enable font-shifting functions (rxvt)           No           No            No
       36  DECHEM                         Hebrew Encoding Mode                                                     No           No            No
       38  DECTEK                         Tektronix 4010/4014 Mode                                                 No           No            No
       40  DECCRNLM                       Carriage Return/New Line Mode / Allow 80⇒132 mode (xterm)                No           No            No
       41  DECUPM                         Unidirectional Print Mode / more(1) fix (xterm)                          No           No            No
       42  DECNRCM                        National Replacement Character Set Mode                                  No           No            No
       43  DECGEPM                        Graphics Expanded Print Mode                                             No           No            No
       44  DECGPCM                        Graphics Print Color Mode / Turn on margin bell (xterm)                  No           No            No
       45  DECGPCS                        Graphics Print Color Syntax / Reverse-wraparound mode (xterm)            Yes          Yes           No
       46  DECGPBM                        Graphics Print Background Mode / Start logging (xterm)                   No           No            No
       47  DECGRPM                        Graphics Rotated Print Mode / Use Alternate Screen Buffer (xterm)        Yes          Yes           No
       49  DECTHAIM                       Thai Input Mode                                                          No           No            No
       50  DECTHAICM                      Thai Cursor Mode                                                         No           No            No
       51  DECBWRM                        Black/White Reversal Mode                                                No           No            No
       52  DECOPM                         Origin Placement Mode                                                    No           No            No
       53  DEC131TM                       VT131 Transmit Mode                                                      No           No            No
       55  DECBPM                         Bold Page Mode                                                           No           No            No
       57  DECNAKB                        Greek/N-A Keyboard Mapping Mode                                          No           No            No
       58  DECIPEM                        Enter IBM Proprinter Emulation Mode                                      No           No            No
       59  DECKKDM                        Kanji/Katakana Display Mode                                              No           No            No
       60  DECHCCM                        Horizontal Cursor Coupling                                               No           No            No
       61  DECVCCM                        Vertical Cursor Coupling Mode                                            No           No            No
       64  DECPCCM                        Page Cursor Coupling Mode                                                No           No            No
       65  DECBCMM                        Business Color Matching Mode                                             No           No            No
       66  DECNKM                         Numeric Keypad Mode                                                      Yes          Yes           No
       67  DECBKM                         Backarrow Key Mode                                                       Yes          No            No
       68  DECKBUM                        Keyboard Usage Mode                                                      No           No            No
       69  DECVSSM                        Vertical Split Screen Mode / DECLRMM - Left Right Margin Mode            No           No            No
       70  DECFPM                         Force Plot Mode                                                          No           No            No
       73  DECXRLM                        Transmission Rate Limiting                                               No           No            No
       80  DECSDM                         Sixel Display Mode                                                       No           No            No
       81  DECKPM                         Key Position Mode                                                        No           No            No
       83  WY_52_LINE                     52 line mode (WY-370)                                                    No           No            No
       84  WYENAT_OFF                     Erasable/nonerasable WYENAT Off attribute select (WY-370)                No           No            No
       85  REPLACEMENT_CHAR_COLOR         Replacement character color (WY-370)                                     No           No            No
       90  DECTHAISCM                     Thai Space Compensating Mode                                             No           No            No
       95  DECNCSM                        No Clearing Screen on Column Change Mode                                 No           No            No
       96  DECRLCM                        Right to Left Copy Mode                                                  No           No            No
       97  DECCRTSM                       CRT Save Mode                                                            No           No            No
       98  DECARSM                        Auto Resize Mode                                                         No           No            No
       99  DECMCM                         Modem Control Mode                                                       No           No            No
      100  DECAAM                         Auto Answerback Mode                                                     No           No            No
      101  DECCANSM                       Conceal Answerback Message Mode                                          No           No            No
      102  DECNULM                        Ignore Null Mode                                                         No           No            No
      103  DECHDPXM                       Half Duplex Mode                                                         No           No            No
      104  DECESKM                        Secondary Keyboard Language Mode                                         No           No            No
      106  DECOSCNM                       Overscan Mode                                                            No           No            No
      108  DECNUMLK                       NumLock Mode                                                             No           No            No
      109  DECCAPSLK                      Caps Lock Mode                                                           No           No            No
      110  DECKLHIM                       Keyboard LEDs Host Indicator Mode                                        No           No            No
      111  DECFWM                         Framed Windows Mode                                                      No           No            No
      112  DECRPL                         Review Previous Lines Mode                                               No           No            No
      113  DECHWUM                        Host Wake-Up Mode                                                        No           No            No
      114  DECATCUM                       Alternate Text Color Underline Mode                                      No           No            No
      115  DECATCBM                       Alternate Text Color Blink Mode                                          No           No            No
      116  DECBBSM                        Bold and Blink Style Mode                                                No           No            No
      117  DECECM                         Erase Color Mode                                                         No           No            No
     1000  MOUSE_REPORT_CLICK             Send Mouse X & Y on button press                                         Yes          Yes           No
     1001  MOUSE_HILITE_TRACKING          Use Hilite Mouse Tracking                                                No           No            No
     1002  MOUSE_REPORT_DRAG              Use Cell Motion Mouse Tracking                                           Yes          Yes           No
     1003  MOUSE_ALL_MOTION               Use All Motion Mouse Tracking                                            Yes          Yes           No
     1004  FOCUS_IN_OUT_EVENTS            Send FocusIn/FocusOut events                                             Yes          Yes           No
     1005  MOUSE_EXTENDED_UTF8            Enable UTF-8 Mouse Mode                                                  Yes          No            No
     1006  MOUSE_EXTENDED_SGR             Enable SGR Mouse Mode                                                    Yes          Yes           No
     1007  ALT_SCROLL_XTERM               Enable Alternate Scroll Mode                                             No           No            No
     1010  SCROLL_ON_TTY_OUTPUT_RXVT      Scroll to bottom on tty output                                           No           No            No
     1011  SCROLL_ON_KEYPRESS_RXVT        Scroll to bottom on key press                                            No           No            No
     1014  FAST_SCROLL                    Enable fastScroll resource                                               No           No            No
     1015  MOUSE_URXVT                    Enable urxvt Mouse Mode                                                  Yes          No            No
     1016  MOUSE_SGR_PIXELS               Enable SGR Mouse PixelMode                                               Yes          Yes           No
     1021  BOLD_ITALIC_HIGH_INTENSITY     Bold/italic implies high intensity                                       No           No            No
     1034  META_SETS_EIGHTH_BIT           Interpret "meta" key                                                     No           No            No
     1035  MODIFIERS_ALT_NUMLOCK          Enable special modifiers for Alt and NumLock keys                        No           No            No
     1036  META_SENDS_ESC                 Send ESC when Meta modifies a key                                        No           No            No
     1037  KP_DELETE_SENDS_DEL            Send DEL from the editing-keypad Delete key                              No           No            No
     1039  ALT_SENDS_ESC                  Send ESC when Alt modifies a key                                         No           No            No
     1040  KEEP_SELECTION_NO_HILITE       Keep selection even if not highlighted                                   No           No            No
     1041  USE_CLIPBOARD_SELECTION        Use the CLIPBOARD selection                                              No           No            No
     1042  URGENCY_ON_CTRL_G              Enable Urgency window manager hint when Control-G is received            No           No            No
     1043  RAISE_ON_CTRL_G                Enable raising of the window when Control-G is received                  No           No            No
     1044  REUSE_CLIPBOARD_DATA           Reuse the most recent data copied to CLIPBOARD                           No           No            No
     1045  EXTENDED_REVERSE_WRAPAROUND    Extended Reverse-wraparound mode (XTREVWRAP2)                            No           No            No
     1046  ALT_SCREEN_BUFFER_SWITCH       Enable switching to/from Alternate Screen Buffer                         No           No            No
     1047  ALT_SCREEN_BUFFER_XTERM        Use Alternate Screen Buffer                                              Yes          Yes           No
     1048  SAVE_CURSOR_DECSC              Save cursor as in DECSC                                                  Yes          Yes           Yes
     1049  ALT_SCREEN_AND_SAVE_CLEAR      Save cursor as in DECSC and use alternate screen buffer                  Yes          Yes           No
     1050  TERMINFO_FUNC_KEY_MODE         Set terminfo/termcap function-key mode                                   No           No            No
     1051  SUN_FUNC_KEY_MODE              Set Sun function-key mode                                                No           No            No
     1052  HP_FUNC_KEY_MODE               Set HP function-key mode                                                 No           No            No
     1053  SCO_FUNC_KEY_MODE              Set SCO function-key mode                                                No           No            No
     1060  LEGACY_KBD_X11R6               Set legacy keyboard emulation, i.e, X11R6                                No           No            No
     1061  VT220_KBD_EMULATION            Set VT220 keyboard emulation                                             No           No            No
     1070  SIXEL_PRIVATE_PALETTE          Use private color registers for each graphic                             No           No            No
     1243  BIDI_ARROW_KEY_SWAPPING        Arrow keys swapping (BiDi)                                               No           No            No
     1337  ITERM2_REPORT_KEY_UP           Report Key Up                                                            No           No            No
     2001  READLINE_MOUSE_BUTTON_1        Enable readline mouse button-1                                           No           No            No
     2002  READLINE_MOUSE_BUTTON_2        Enable readline mouse button-2                                           No           No            No
     2003  READLINE_MOUSE_BUTTON_3        Enable readline mouse button-3                                           No           No            No
     2004  BRACKETED_PASTE                Set bracketed paste mode                                                 Yes          Yes           No
     2005  READLINE_CHARACTER_QUOTING     Enable readline character-quoting                                        No           No            No
     2006  READLINE_NEWLINE_PASTING       Enable readline newline pasting                                          No           No            No
     2026  SYNCHRONIZED_OUTPUT            Synchronized Output                                                      No           No            No
     2027  GRAPHEME_CLUSTERING            Grapheme Clustering                                                      No           No            No
     2028  TEXT_REFLOW                    Text reflow                                                              No           No            No
     2029  PASSIVE_MOUSE_TRACKING         Passive Mouse Tracking                                                   No           No            No
     2030  REPORT_GRID_CELL_SELECTION     Report grid cell selection                                               No           No            No
     2031  COLOR_PALETTE_UPDATES          Color palette updates                                                    No           No            No
     2048  IN_BAND_WINDOW_RESIZE          In-Band Window Resize Notifications                                      No           No            No
     2500  MIRROR_BOX_DRAWING             Mirror box drawing characters                                            No           No            No
     2501  BIDI_AUTODETECTION             BiDi autodetection                                                       No           No            No
     7700  AMBIGUOUS_WIDTH_REPORTING      Ambiguous width reporting                                                No           No            No
     7711  SCROLL_MARKERS                 Scroll markers (prompt start)                                            No           No            No
     7723  REWRAP_ON_RESIZE_MINTTY        Rewrap on resize                                                         No           No            No
     7727  APPLICATION_ESCAPE_KEY         Application escape key mode                                              No           No            No
     7728  ESC_KEY_SENDS_BACKSLASH        Send ^\ instead of the standard ^[ for the ESC key                       No           No            No
     7730  GRAPHICS_POSITION              Graphics position                                                        No           No            No
     7765  ALT_MODIFIED_MOUSEWHEEL        Alt-modified mousewheel mode                                             No           No            No
     7766  SHOW_HIDE_SCROLLBAR            Show/hide scrollbar                                                      No           No            No
     7767  FONT_CHANGE_REPORTING          Font change reporting                                                    No           No            No
     7780  GRAPHICS_POSITION_2            Graphics position                                                        No           No            No
     7783  SHORTCUT_KEY_MODE              Shortcut key mode                                                        No           No            No
     7786  MOUSEWHEEL_REPORTING           Mousewheel reporting                                                     No           No            No
     7787  APPLICATION_MOUSEWHEEL         Application mousewheel mode                                              No           No            No
     7796  BIDI_CURRENT_LINE              BiDi on current line                                                     No           No            No
     8200  TTCTH                          Terminal-to-Computer Talk-back Handler                                   No           No            No
     8452  SIXEL_SCROLLING_LEAVES_CURSOR  Sixel scrolling leaves cursor to right of graphic                        No           No            No
     8800  CHARACTER_MAPPING_SERVICE      enable/disable character mapping service                                 No           No            No
     8840  AMBIGUOUS_WIDTH_DOUBLE_WIDTH   Treat ambiguous width characters as double-width                         No           No            No
     9001  WIN32_INPUT_MODE               win32-input-mode                                                         No           No            No
    19997  KITTY_HANDLE_CTRL_C_Z          Handle Ctrl-C/Ctrl-Z mode                                                No           No            No
    77096  MINTTY_BIDI                    BiDi                                                                     No           No            No
   737769  INPUT_METHOD_EDITOR            Input Method Editor (IME) mode                                           No           No            No
   ======  =============================  =======================================================================  ===========  ============  =========

**Summary**: 19 changeable, 140 not changeable.

.. _tabbyreproduce:

Reproduction
++++++++++++

To reproduce these results for *tabby*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --save-yaml=macos-tabby-1.0.228.yaml \
        --limit-codepoints=5000 \
        --limit-words=5000 \
        --limit-errors=1000

.. _tabbytime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **162.19 seconds** (162s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
