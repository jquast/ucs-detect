.. _coolretroterm:

cool-retro-term
---------------


Tested Software version 1.2.0 on Darwin
Full results available at ucs-detect_ repository path
`data/macos-cool-retro-term-1.2.0.yaml <https://github.com/jquast/ucs-detect/blob/master/data/macos-cool-retro-term-1.2.0.yaml>`_

.. _coolretrotermscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *cool-retro-term*:

.. table::
   :class: sphinx-datatable

   ============  ===========  ==============  ======================================================
   Score Type    Raw Score    Scaled Score    Calculation
   ============  ===========  ==============  ======================================================
   WIDE          72.73%       58.9%           (version_index / total_versions) × (pct_success / 100)
   ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
   LANG          99.27%       100.0%          geometric_mean(language_percentages)
   VS16          0.00%        0.0%            pct_success / 100
   VS15          0.00%        0.0%            pct_success / 100
   DEC Modes     N/A          N/A             modes_changeable / total_modes
   TIME          72.09s       79.9%           1 - ((elapsed - min) / (max - min)) [inverse]
   ============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 34.40%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 24.5%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _coolretrotermwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for cool-retro-term appears to be 
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
  while *cool-retro-term* measures width 0.

.. _coolretrotermzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *cool-retro-term* appears to be 
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
  while *cool-retro-term* measures width 8.

.. _coolretrotermvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *cool-retro-term* is 213 errors
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
  while *cool-retro-term* measures width 1.


.. _coolretrotermvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *cool-retro-term* is 158 errors
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
  while *cool-retro-term* measures width 2.


.. _coolretrotermlang:

Language Support
++++++++++++++++

The following 3 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog), Tamang, Eastern.

The following 116 languages are not fully supported:

.. table::
   :class: sphinx-datatable

   ====================================================================================  ==========  =========  =============
   lang                                                                                    n_errors    n_total  pct_success
   ====================================================================================  ==========  =========  =============
   :ref:`Malayalam <coolretrotermlangMalayalam>`                                                116       1630  92.9%
   :ref:`Sinhala <coolretrotermlangSinhala>`                                                    112       1655  93.2%
   :ref:`Japanese (Osaka) <coolretrotermlangJapaneseOsaka>`                                       7        308  97.7%
   :ref:`(Jinan) <coolretrotermlangJinan>`                                                        4        211  98.1%
   :ref:`Chinese, Wu <coolretrotermlangChineseWu>`                                                4        211  98.1%
   :ref:`Chinese, Mandarin (Nanjing) <coolretrotermlangChineseMandarinNanjing>`                   4        212  98.1%
   :ref:`Chinese, Mandarin (Tianjin) <coolretrotermlangChineseMandarinTianjin>`                   4        212  98.1%
   :ref:`Chinese, Xiang <coolretrotermlangChineseXiang>`                                          4        212  98.1%
   :ref:`Thai <coolretrotermlangThai>`                                                            6        341  98.2%
   :ref:`Japanese <coolretrotermlangJapanese>`                                                    5        299  98.3%
   :ref:`Thai (2) <coolretrotermlangThai2>`                                                       5        313  98.4%
   :ref:`Japanese (Tokyo) <coolretrotermlangJapaneseTokyo>`                                       5        320  98.4%
   :ref:`Vietnamese (Han nom) <coolretrotermlangVietnameseHannom>`                                3        199  98.5%
   :ref:`Chinese, Mandarin (Harbin) <coolretrotermlangChineseMandarinHarbin>`                     3        210  98.6%
   :ref:`Chinese, Yue <coolretrotermlangChineseYue>`                                              3        210  98.6%
   :ref:`Chinese, Gan <coolretrotermlangChineseGan>`                                              3        211  98.6%
   :ref:`Chinese, Mandarin (Guiyang) <coolretrotermlangChineseMandarinGuiyang>`                   3        211  98.6%
   :ref:`Chinese, Hakka <coolretrotermlangChineseHakka>`                                          3        212  98.6%
   :ref:`Chinese, Mandarin (Beijing) <coolretrotermlangChineseMandarinBeijing>`                   3        212  98.6%
   :ref:`Chinese, Min Nan <coolretrotermlangChineseMinNan>`                                       3        212  98.6%
   :ref:`Lao <coolretrotermlangLao>`                                                              6        426  98.6%
   :ref:`Chinese, Mandarin (Simplified) <coolretrotermlangChineseMandarinSimplified>`             3        225  98.7%
   :ref:`Nuosu <coolretrotermlangNuosu>`                                                          3        230  98.7%
   :ref:`Chinese, Mandarin (Traditional) <coolretrotermlangChineseMandarinTraditional>`           2        210  99.0%
   :ref:`Khmer, Central <coolretrotermlangKhmerCentral>`                                          5        528  99.1%
   :ref:`Chinese, Jinyu <coolretrotermlangChineseJinyu>`                                          2        212  99.1%
   :ref:`Khün <coolretrotermlangKhn>`                                                             4        442  99.1%
   :ref:`Chickasaw <coolretrotermlangChickasaw>`                                                  4        554  99.3%
   :ref:`Bora <coolretrotermlangBora>`                                                           11       1598  99.3%
   :ref:`Gumuz <coolretrotermlangGumuz>`                                                          8       1283  99.4%
   :ref:`Marathi <coolretrotermlangMarathi>`                                                     10       1614  99.4%
   :ref:`Shipibo-Conibo <coolretrotermlangShipiboConibo>`                                        15       2540  99.4%
   :ref:`Nanai <coolretrotermlangNanai>`                                                          7       1207  99.4%
   :ref:`Navajo <coolretrotermlangNavajo>`                                                        9       1600  99.4%
   :ref:`Orok <coolretrotermlangOrok>`                                                            7       1245  99.4%
   :ref:`Evenki <coolretrotermlangEvenki>`                                                        5        899  99.4%
   :ref:`Amarakaeri <coolretrotermlangAmarakaeri>`                                                8       1446  99.4%
   :ref:`Yaneshaʼ <coolretrotermlangYanesha>`                                                    14       2536  99.4%
   :ref:`Shan <coolretrotermlangShan>`                                                            5        915  99.5%
   :ref:`Siona <coolretrotermlangSiona>`                                                          8       1492  99.5%
   :ref:`Gilyak <coolretrotermlangGilyak>`                                                        8       1504  99.5%
   :ref:`Veps <coolretrotermlangVeps>`                                                            7       1323  99.5%
   :ref:`Nepali <coolretrotermlangNepali>`                                                        7       1385  99.5%
   :ref:`South Azerbaijani <coolretrotermlangSouthAzerbaijani>`                                   7       1396  99.5%
   :ref:`Secoya <coolretrotermlangSecoya>`                                                        7       1409  99.5%
   :ref:`Bengali <coolretrotermlangBengali>`                                                      7       1413  99.5%
   :ref:`Burmese <coolretrotermlangBurmese>`                                                      6       1223  99.5%
   :ref:`Tamil (Sri Lanka) <coolretrotermlangTamilSriLanka>`                                      6       1261  99.5%
   :ref:`Tamil <coolretrotermlangTamil>`                                                          6       1262  99.5%
   :ref:`Colorado <coolretrotermlangColorado>`                                                    6       1263  99.5%
   :ref:`(Yeonbyeon) <coolretrotermlangYeonbyeon>`                                                5       1061  99.5%
   :ref:`Kannada <coolretrotermlangKannada>`                                                      5       1080  99.5%
   :ref:`Telugu <coolretrotermlangTelugu>`                                                        5       1129  99.6%
   :ref:`Mon <coolretrotermlangMon>`                                                              4        946  99.6%
   :ref:`Korean <coolretrotermlangKorean>`                                                        5       1185  99.6%
   :ref:`Tem <coolretrotermlangTem>`                                                              7       1659  99.6%
   :ref:`Catalan (2) <coolretrotermlangCatalan2>`                                                 8       1909  99.6%
   :ref:`Maldivian <coolretrotermlangMaldivian>`                                                  8       1918  99.6%
   :ref:`Mirandese <coolretrotermlangMirandese>`                                                  8       1966  99.6%
   :ref:`Éwé <coolretrotermlangw>`                                                                9       2230  99.6%
   :ref:`Sanskrit <coolretrotermlangSanskrit>`                                                    4       1000  99.6%
   :ref:`Sanskrit (Grantha) <coolretrotermlangSanskritGrantha>`                                   4       1006  99.6%
   :ref:`Picard <coolretrotermlangPicard>`                                                        8       2024  99.6%
   :ref:`Yiddish, Eastern <coolretrotermlangYiddishEastern>`                                      7       1775  99.6%
   :ref:`Ticuna <coolretrotermlangTicuna>`                                                        8       2048  99.6%
   :ref:`Kabyle <coolretrotermlangKabyle>`                                                        7       1815  99.6%
   :ref:`Lingala (tones) <coolretrotermlangLingalatones>`                                         7       1818  99.6%
   :ref:`Tamazight, Central Atlas <coolretrotermlangTamazightCentralAtlas>`                       7       1822  99.6%
   :ref:`Fur <coolretrotermlangFur>`                                                              7       1838  99.6%
   :ref:`Pular (Adlam) <coolretrotermlangPularAdlam>`                                             6       1613  99.6%
   :ref:`Arabic, Standard <coolretrotermlangArabicStandard>`                                      5       1348  99.6%
   :ref:`Mixtec, Metlatónoc <coolretrotermlangMixtecMetlatnoc>`                                   5       1367  99.6%
   :ref:`French (Welche) <coolretrotermlangFrenchWelche>`                                         7       1928  99.6%
   :ref:`Gen <coolretrotermlangGen>`                                                              8       2309  99.7%
   :ref:`Assyrian Neo-Aramaic <coolretrotermlangAssyrianNeoAramaic>`                              4       1160  99.7%
   :ref:`Ga <coolretrotermlangGa>`                                                                7       2039  99.7%
   :ref:`Aja <coolretrotermlangAja>`                                                              7       2061  99.7%
   :ref:`Uduk <coolretrotermlangUduk>`                                                           11       3247  99.7%
   :ref:`Saint Lucian Creole French <coolretrotermlangSaintLucianCreoleFrench>`                   6       1777  99.7%
   :ref:`Maori (2) <coolretrotermlangMaori2>`                                                     8       2385  99.7%
   :ref:`Farsi, Western <coolretrotermlangFarsiWestern>`                                          6       1822  99.7%
   :ref:`Maithili <coolretrotermlangMaithili>`                                                    5       1519  99.7%
   :ref:`Dinka, Northeastern <coolretrotermlangDinkaNortheastern>`                                5       1529  99.7%
   :ref:`Mòoré <coolretrotermlangMor>`                                                            8       2447  99.7%
   :ref:`Yoruba <coolretrotermlangYoruba>`                                                        8       2454  99.7%
   :ref:`Dari <coolretrotermlangDari>`                                                            6       1872  99.7%
   :ref:`Vietnamese <coolretrotermlangVietnamese>`                                                8       2502  99.7%
   :ref:`Ditammari <coolretrotermlangDitammari>`                                                  6       1882  99.7%
   :ref:`Dendi <coolretrotermlangDendi>`                                                          5       1569  99.7%
   :ref:`Mazahua Central <coolretrotermlangMazahuaCentral>`                                       5       1574  99.7%
   :ref:`Serer-Sine <coolretrotermlangSererSine>`                                                 5       1596  99.7%
   :ref:`Urdu <coolretrotermlangUrdu>`                                                            7       2237  99.7%
   :ref:`Pashto, Northern <coolretrotermlangPashtoNorthern>`                                      7       2242  99.7%
   :ref:`Seraiki <coolretrotermlangSeraiki>`                                                      7       2242  99.7%
   :ref:`Belanda Viri <coolretrotermlangBelandaViri>`                                             7       2246  99.7%
   :ref:`Urdu (2) <coolretrotermlangUrdu2>`                                                       7       2251  99.7%
   :ref:`Dagaare, Southern <coolretrotermlangDagaareSouthern>`                                    8       2582  99.7%
   :ref:`Baatonum <coolretrotermlangBaatonum>`                                                    6       1939  99.7%
   :ref:`Bamun <coolretrotermlangBamun>`                                                          7       2285  99.7%
   :ref:`Waama <coolretrotermlangWaama>`                                                          3       1000  99.7%
   :ref:`Panjabi, Western <coolretrotermlangPanjabiWestern>`                                      7       2419  99.7%
   :ref:`Chinantec, Chiltepec <coolretrotermlangChinantecChiltepec>`                              5       1729  99.7%
   :ref:`Fon <coolretrotermlangFon>`                                                              7       2520  99.7%
   :ref:`Chakma <coolretrotermlangChakma>`                                                        4       1444  99.7%
   :ref:`Javanese (Javanese) <coolretrotermlangJavaneseJavanese>`                                 4       1453  99.7%
   :ref:`Otomi, Mezquital <coolretrotermlangOtomiMezquital>`                                      5       1849  99.7%
   :ref:`Lamnso' <coolretrotermlangLamnso>`                                                       6       2237  99.7%
   :ref:`Gujarati <coolretrotermlangGujarati>`                                                    4       1536  99.7%
   :ref:`Dangme <coolretrotermlangDangme>`                                                        7       2912  99.8%
   :ref:`Hindi <coolretrotermlangHindi>`                                                          5       2128  99.8%
   :ref:`Magahi <coolretrotermlangMagahi>`                                                        4       1716  99.8%
   :ref:`Bhojpuri <coolretrotermlangBhojpuri>`                                                    4       1737  99.8%
   :ref:`Tibetan, Central <coolretrotermlangTibetanCentral>`                                      7       3174  99.8%
   :ref:`Panjabi, Eastern <coolretrotermlangPanjabiEastern>`                                      5       2293  99.8%
   :ref:`Tai Dam <coolretrotermlangTaiDam>`                                                       5       2386  99.8%
   :ref:`Dzongkha <coolretrotermlangDzongkha>`                                                    6       3060  99.8%
   ====================================================================================  ==========  =========  =============

.. _coolretrotermlangMalayalam:

Malayalam
^^^^^^^^^

Sequence of language *Malayalam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0D38 <https://codepoints.net/U+0D38>`_  '\\u0d38'  Lo                  1  MALAYALAM LETTER SA
     2  `U+0D30 <https://codepoints.net/U+0D30>`_  '\\u0d30'  Lo                  1  MALAYALAM LETTER RA
     3  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
     4  `U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
     5  `U+0D35 <https://codepoints.net/U+0D35>`_  '\\u0d35'  Lo                  1  MALAYALAM LETTER VA
     6  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
     7  `U+0D35 <https://codepoints.net/U+0D35>`_  '\\u0d35'  Lo                  1  MALAYALAM LETTER VA
     8  `U+0D24 <https://codepoints.net/U+0D24>`_  '\\u0d24'  Lo                  1  MALAYALAM LETTER TA
     9  `U+0D4B <https://codepoints.net/U+0D4B>`_  '\\u0d4b'  Mc                  0  MALAYALAM VOWEL SIGN OO
    10  `U+0D28 <https://codepoints.net/U+0D28>`_  '\\u0d28'  Lo                  1  MALAYALAM LETTER NA
    11  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
    12  `U+0D2E <https://codepoints.net/U+0D2E>`_  '\\u0d2e'  Lo                  1  MALAYALAM LETTER MA
    13  `U+0D41 <https://codepoints.net/U+0D41>`_  '\\u0d41'  Mn                  0  MALAYALAM VOWEL SIGN U
    14  `U+0D16 <https://codepoints.net/U+0D16>`_  '\\u0d16'  Lo                  1  MALAYALAM LETTER KHA
    15  `U+0D2E <https://codepoints.net/U+0D2E>`_  '\\u0d2e'  Lo                  1  MALAYALAM LETTER MA
    16  `U+0D3E <https://codepoints.net/U+0D3E>`_  '\\u0d3e'  Mc                  0  MALAYALAM VOWEL SIGN AA
    17  `U+0D2F <https://codepoints.net/U+0D2F>`_  '\\u0d2f'  Lo                  1  MALAYALAM LETTER YA
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 17


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb4\xb8\xe0\xb4\xb0\xe0\xb5\x8d\xe2\x80\x8d\xe0\xb4\xb5\xe0\xb5\x8d\xe0\xb4\xb5\xe0\xb4\xa4\xe0\xb5\x8b\xe0\xb4\xa8\xe0\xb5\x8d\xe0\xb4\xae\xe0\xb5\x81\xe0\xb4\x96\xe0\xb4\xae\xe0\xb4\xbe\xe0\xb4\xaf|\\n123456789|\\n"
        സര്‍വ്വതോന്മുഖമായ|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *cool-retro-term* measures width 10.

.. _coolretrotermlangSinhala:

Sinhala
^^^^^^^

Sequence of language *Sinhala* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================================
     1  `U+0DB4 <https://codepoints.net/U+0DB4>`_  '\\u0db4'  Lo                  1  SINHALA LETTER ALPAPRAANA PAYANNA
     2  `U+0DCA <https://codepoints.net/U+0DCA>`_  '\\u0dca'  Mn                  0  SINHALA SIGN AL-LAKUNA
     3  `U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
     4  `U+0DBB <https://codepoints.net/U+0DBB>`_  '\\u0dbb'  Lo                  1  SINHALA LETTER RAYANNA
     5  `U+0D9A <https://codepoints.net/U+0D9A>`_  '\\u0d9a'  Lo                  1  SINHALA LETTER ALPAPRAANA KAYANNA
     6  `U+0DCF <https://codepoints.net/U+0DCF>`_  '\\u0dcf'  Mc                  0  SINHALA VOWEL SIGN AELA-PILLA
     7  `U+0DC1 <https://codepoints.net/U+0DC1>`_  '\\u0dc1'  Lo                  1  SINHALA LETTER TAALUJA SAYANNA
     8  `U+0DB1 <https://codepoints.net/U+0DB1>`_  '\\u0db1'  Lo                  1  SINHALA LETTER DANTAJA NAYANNA
     9  `U+0DBA <https://codepoints.net/U+0DBA>`_  '\\u0dba'  Lo                  1  SINHALA LETTER YAYANNA
   ===  =========================================  =========  ==========  =========  =================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb6\xb4\xe0\xb7\x8a\xe2\x80\x8d\xe0\xb6\xbb\xe0\xb6\x9a\xe0\xb7\x8f\xe0\xb7\x81\xe0\xb6\xb1\xe0\xb6\xba|\\n12345|\\n"
        ප්‍රකාශනය|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width 6.

.. _coolretrotermlangJapaneseOsaka:

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+307E <https://codepoints.net/U+307E>`_  '\\u307e'  Lo                  2  HIRAGANA LETTER MA
     2  `U+305F <https://codepoints.net/U+305F>`_  '\\u305f'  Lo                  2  HIRAGANA LETTER TA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\xbe\xe3\x81\x9f|\\n1234|\\n"
        また|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -20.

.. _coolretrotermlangJinan:

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -20.

.. _coolretrotermlangChineseWu:

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -20.

.. _coolretrotermlangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -22.

.. _coolretrotermlangChineseMandarinTianjin:

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
     5  `U+751F <https://codepoints.net/U+751F>`_  '\\u751f'  Lo                  2  CJK UNIFIED IDEOGRAPH-751F
     6  `U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
     7  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     8  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xba\xba\xe4\xb8\xaa\xe9\xa1\xb6\xe4\xb8\xaa\xe7\x94\x9f\xe8\x80\x8c\xe8\x87\xaa\xe7\x94\xb1|\\n1234567890123456|\\n"
        人个顶个生而自由|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *cool-retro-term* measures width 9.

.. _coolretrotermlangChineseXiang:

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
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -20.

.. _coolretrotermlangThai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0E42 <https://codepoints.net/U+0E42>`_  '\\u0e42'  Lo                  1  THAI CHARACTER SARA O
     2  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
     3  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
     4  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
     5  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     6  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     7  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     8  `U+0E33 <https://codepoints.net/U+0E33>`_  '\\u0e33'  Lo                  1  THAI CHARACTER SARA AM
     9  `U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
    10  `U+0E36 <https://codepoints.net/U+0E36>`_  '\\u0e36'  Mn                  0  THAI CHARACTER SARA UE
    11  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
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
    35  `U+0E08 <https://codepoints.net/U+0E08>`_  '\\u0e08'  Lo                  1  THAI CHARACTER CHO CHAN
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 35


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x82\xe0\xb8\x94\xe0\xb8\xa2\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa3\xe0\xb8\xb3\xe0\xb8\xa5\xe0\xb8\xb6\xe0\xb8\x81\xe0\xb8\x96\xe0\xb8\xb6\xe0\xb8\x87\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xb5\xe0\xb9\x89\xe0\xb9\x80\xe0\xb8\x9b\xe0\xb9\x87\xe0\xb8\x99\xe0\xb9\x80\xe0\xb8\x99\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb8\x87\xe0\xb8\x99\xe0\xb8\xb4\xe0\xb8\x88|\\n123456789012345678901234567|\\n"
        โดยการรำลึกถึงปฏิญญานี้เป็นเนืองนิจ|
        123456789012345678901234567|

- python `wcwidth.wcswidth()`_ measures width 27,
  while *cool-retro-term* measures width -7.

.. _coolretrotermlangJapanese:

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+3044 <https://codepoints.net/U+3044>`_  '\\u3044'  Lo                  2  HIRAGANA LETTER I
     2  `U+304B <https://codepoints.net/U+304B>`_  '\\u304b'  Lo                  2  HIRAGANA LETTER KA
     3  `U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
     4  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
     5  `U+5DEE <https://codepoints.net/U+5DEE>`_  '\\u5dee'  Lo                  2  CJK UNIFIED IDEOGRAPH-5DEE
     6  `U+5225 <https://codepoints.net/U+5225>`_  '\\u5225'  Lo                  2  CJK UNIFIED IDEOGRAPH-5225
     7  `U+3082 <https://codepoints.net/U+3082>`_  '\\u3082'  Lo                  2  HIRAGANA LETTER MO
     8  `U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
     9  `U+3057 <https://codepoints.net/U+3057>`_  '\\u3057'  Lo                  2  HIRAGANA LETTER SI
    10  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
    11  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
    12  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
    13  `U+5E73 <https://codepoints.net/U+5E73>`_  '\\u5e73'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E73
    14  `U+7B49 <https://codepoints.net/U+7B49>`_  '\\u7b49'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B49
    15  `U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
    16  `U+4FDD <https://codepoints.net/U+4FDD>`_  '\\u4fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FDD
    17  `U+8B77 <https://codepoints.net/U+8B77>`_  '\\u8b77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8B77
    18  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
    19  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    20  `U+3051 <https://codepoints.net/U+3051>`_  '\\u3051'  Lo                  2  HIRAGANA LETTER KE
    21  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
    22  `U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
    23  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    24  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
    25  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
    26  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
    27  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 27


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\x84\xe3\x81\x8b\xe3\x81\xaa\xe3\x82\x8b\xe5\xb7\xae\xe5\x88\xa5\xe3\x82\x82\xe3\x81\xaa\xe3\x81\x97\xe3\x81\xab\xe6\xb3\x95\xe3\x81\xae\xe5\xb9\xb3\xe7\xad\x89\xe3\x81\xaa\xe4\xbf\x9d\xe8\xad\xb7\xe3\x82\x92\xe5\x8f\x97\xe3\x81\x91\xe3\x82\x8b\xe6\xa8\xa9\xe5\x88\xa9\xe3\x82\x92\xe6\x9c\x89\xe3\x81\x99\xe3\x82\x8b|\\n123456789012345678901234567890123456789012345678901234|\\n"
        いかなる差別もなしに法の平等な保護を受ける権利を有する|
        123456789012345678901234567890123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 54,
  while *cool-retro-term* measures width 50.

.. _coolretrotermlangThai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0E41 <https://codepoints.net/U+0E41>`_  '\\u0e41'  Lo                  1  THAI CHARACTER SARA AE
     2  `U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
     3  `U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
     4  `U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
     5  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     6  `U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
     7  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
     8  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     9  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
    10  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    11  `U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
    12  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    13  `U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
    14  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    15  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
    16  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
    17  `U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
    18  `U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
    19  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    20  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 20


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x81\xe0\xb8\xa5\xe0\xb8\xb0\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x95\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\xb1\xe0\xb9\x89\xe0\xb8\x87\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb2\xe0\xb8\xa2|\\n12345678901234567|\\n"
        และประชาชาติทั้งหลาย|
        12345678901234567|

- python `wcwidth.wcswidth()`_ measures width 17,
  while *cool-retro-term* measures width -29.

.. _coolretrotermlangJapaneseTokyo:

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5168 <https://codepoints.net/U+5168>`_  '\\u5168'  Lo                  2  CJK UNIFIED IDEOGRAPH-5168
     2  `U+90E8 <https://codepoints.net/U+90E8>`_  '\\u90e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-90E8
     3  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     4  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     5  `U+306F <https://codepoints.net/U+306F>`_  '\\u306f'  Lo                  2  HIRAGANA LETTER HA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\xa8\xe9\x83\xa8\xe3\x81\xae\xe4\xba\xba\xe3\x81\xaf|\\n1234567890|\\n"
        全部の人は|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *cool-retro-term* measures width -42.

.. _coolretrotermlangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===========================
     1  `U+8B49 <https://codepoints.net/U+8B49>`_          '\\u8b49'      Lo                  2  CJK UNIFIED IDEOGRAPH-8B49
     2  `U+660E <https://codepoints.net/U+660E>`_          '\\u660e'      Lo                  2  CJK UNIFIED IDEOGRAPH-660E
     3  `U+5F97 <https://codepoints.net/U+5F97>`_          '\\u5f97'      Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
     4  `U+7F6A <https://codepoints.net/U+7F6A>`_          '\\u7f6a'      Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
     5  `U+72C0 <https://codepoints.net/U+72C0>`_          '\\u72c0'      Lo                  2  CJK UNIFIED IDEOGRAPH-72C0
     6  `U+00027D51 <https://codepoints.net/U+00027D51>`_  '\\U00027d51'  Lo                  2  CJK UNIFIED IDEOGRAPH-27D51
     7  `U+0002029B <https://codepoints.net/U+0002029B>`_  '\\U0002029b'  Lo                  2  CJK UNIFIED IDEOGRAPH-2029B
     8  `U+0002A986 <https://codepoints.net/U+0002A986>`_  '\\U0002a986'  Lo                  2  CJK UNIFIED IDEOGRAPH-2A986
     9  `U+8C6B <https://codepoints.net/U+8C6B>`_          '\\u8c6b'      Lo                  2  CJK UNIFIED IDEOGRAPH-8C6B
    10  `U+0002856D <https://codepoints.net/U+0002856D>`_  '\\U0002856d'  Lo                  2  CJK UNIFIED IDEOGRAPH-2856D
    11  `U+57FA <https://codepoints.net/U+57FA>`_          '\\u57fa'      Lo                  2  CJK UNIFIED IDEOGRAPH-57FA
    12  `U+790E <https://codepoints.net/U+790E>`_          '\\u790e'      Lo                  2  CJK UNIFIED IDEOGRAPH-790E
    13  `U+5F8B <https://codepoints.net/U+5F8B>`_          '\\u5f8b'      Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
    14  `U+6CD5 <https://codepoints.net/U+6CD5>`_          '\\u6cd5'      Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
   ===  =================================================  =============  ==========  =========  ===========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\xad\x89\xe6\x98\x8e\xe5\xbe\x97\xe7\xbd\xaa\xe7\x8b\x80\xf0\xa7\xb5\x91\xf0\xa0\x8a\x9b\xf0\xaa\xa6\x86\xe8\xb1\xab\xf0\xa8\x95\xad\xe5\x9f\xba\xe7\xa4\x8e\xe5\xbe\x8b\xe6\xb3\x95|\\n1234567890123456789012345678|\\n"
        證明得罪狀𧵑𠊛𪦆豫𨕭基礎律法|
        1234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 28,
  while *cool-retro-term* measures width -8.

.. _coolretrotermlangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+80A4 <https://codepoints.net/U+80A4>`_  '\\u80a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-80A4
     2  `U+8272 <https://codepoints.net/U+8272>`_  '\\u8272'  Lo                  2  CJK UNIFIED IDEOGRAPH-8272
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x82\xa4\xe8\x89\xb2|\\n1234|\\n"
        肤色|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -4.

.. _coolretrotermlangChineseYue:

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
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -24.

.. _coolretrotermlangChineseGan:

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -16.

.. _coolretrotermlangChineseMandarinGuiyang:

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

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
  while *cool-retro-term* measures width 5.

.. _coolretrotermlangChineseHakka:

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E8C <https://codepoints.net/U+4E8C>`_  '\\u4e8c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8C
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xba\x8c\xe6\x9d\xa1|\\n123456|\\n"
        第二条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -20.

.. _coolretrotermlangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+80A4 <https://codepoints.net/U+80A4>`_  '\\u80a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-80A4
     2  `U+8272 <https://codepoints.net/U+8272>`_  '\\u8272'  Lo                  2  CJK UNIFIED IDEOGRAPH-8272
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x82\xa4\xe8\x89\xb2|\\n1234|\\n"
        肤色|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -4.

.. _coolretrotermlangChineseMinNan:

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
     2  `U+4E14 <https://codepoints.net/U+4E14>`_  '\\u4e14'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E14
     3  `U+52FF <https://codepoints.net/U+52FF>`_  '\\u52ff'  Lo                  2  CJK UNIFIED IDEOGRAPH-52FF
     4  `U+4F1A <https://codepoints.net/U+4F1A>`_  '\\u4f1a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F1A
     5  `U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
     6  `U+56E0 <https://codepoints.net/U+56E0>`_  '\\u56e0'  Lo                  2  CJK UNIFIED IDEOGRAPH-56E0
     7  `U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
     8  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     9  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    10  `U+5C5E <https://codepoints.net/U+5C5E>`_  '\\u5c5e'  Lo                  2  CJK UNIFIED IDEOGRAPH-5C5E
    11  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    12  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    13  `U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
    14  `U+6291 <https://codepoints.net/U+6291>`_  '\\u6291'  Lo                  2  CJK UNIFIED IDEOGRAPH-6291
    15  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
    16  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    17  `U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
    18  `U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
    19  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe4\xb8\x94\xe5\x8b\xbf\xe4\xbc\x9a\xe7\x94\xa8\xe5\x9b\xa0\xe4\xb8\x80\xe4\xba\xba\xe6\x89\x80\xe5\xb1\x9e\xe7\x9a\x84\xe5\x9b\xbd\xe5\xae\xb6\xe6\x8a\x91\xe5\x9c\xb0\xe7\x9a\x84\xe6\x94\xbf\xe6\xb2\xbb\xe7\x9a\x84|\\n12345678901234567890123456789012345678|\\n"
        并且勿会用因一人所属的国家抑地的政治的|
        12345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 38,
  while *cool-retro-term* measures width 14.

.. _coolretrotermlangLao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+0EA1 <https://codepoints.net/U+0EA1>`_  '\\u0ea1'  Lo                  1  LAO LETTER MO
     2  `U+0EB2 <https://codepoints.net/U+0EB2>`_  '\\u0eb2'  Lo                  1  LAO VOWEL SIGN AA
     3  `U+0E94 <https://codepoints.net/U+0E94>`_  '\\u0e94'  Lo                  1  LAO LETTER DO
     4  `U+0E95 <https://codepoints.net/U+0E95>`_  '\\u0e95'  Lo                  1  LAO LETTER TO
     5  `U+0EB2 <https://codepoints.net/U+0EB2>`_  '\\u0eb2'  Lo                  1  LAO VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xba\xa1\xe0\xba\xb2\xe0\xba\x94\xe0\xba\x95\xe0\xba\xb2|\\n12345|\\n"
        ມາດຕາ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -21.

.. _coolretrotermlangChineseMandarinSimplified:

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
     3  `U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
     4  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x80\xe6\x9d\xa1|\\n12345678|\\n"
        第十一条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *cool-retro-term* measures width -40.

.. _coolretrotermlangNuosu:

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================
     1  `U+A2BE <https://codepoints.net/U+A2BE>`_  '\\ua2be'  Lo                  2  YI SYLLABLE COX
     2  `U+A0B7 <https://codepoints.net/U+A0B7>`_  '\\ua0b7'  Lo                  2  YI SYLLABLE MA
     3  `U+A200 <https://codepoints.net/U+A200>`_  '\\ua200'  Lo                  2  YI SYLLABLE KAX
     4  `U+A425 <https://codepoints.net/U+A425>`_  '\\ua425'  Lo                  2  YI SYLLABLE JJO
     5  `U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
     6  `U+A0C5 <https://codepoints.net/U+A0C5>`_  '\\ua0c5'  Lo                  2  YI SYLLABLE MU
     7  `U+A11C <https://codepoints.net/U+A11C>`_  '\\ua11c'  Lo                  2  YI SYLLABLE TI
     8  `U+A2CA <https://codepoints.net/U+A2CA>`_  '\\ua2ca'  Lo                  2  YI SYLLABLE CYT
     9  `U+A12F <https://codepoints.net/U+A12F>`_  '\\ua12f'  Lo                  2  YI SYLLABLE TEP
    10  `U+A489 <https://codepoints.net/U+A489>`_  '\\ua489'  Lo                  2  YI SYLLABLE YY
    11  `U+A1EC <https://codepoints.net/U+A1EC>`_  '\\ua1ec'  Lo                  2  YI SYLLABLE GO
    12  `U+A151 <https://codepoints.net/U+A151>`_  '\\ua151'  Lo                  2  YI SYLLABLE NDIT
    13  `U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
    14  `U+A305 <https://codepoints.net/U+A305>`_  '\\ua305'  Lo                  2  YI SYLLABLE NZY
    15  `U+A14D <https://codepoints.net/U+A14D>`_  '\\ua14d'  Lo                  2  YI SYLLABLE DDU
    16  `U+A30B <https://codepoints.net/U+A30B>`_  '\\ua30b'  Lo                  2  YI SYLLABLE SI
    17  `U+A180 <https://codepoints.net/U+A180>`_  '\\ua180'  Lo                  2  YI SYLLABLE NIP
    18  `U+A13F <https://codepoints.net/U+A13F>`_  '\\ua13f'  Lo                  2  YI SYLLABLE DDA
    19  `U+A428 <https://codepoints.net/U+A428>`_  '\\ua428'  Lo                  2  YI SYLLABLE JJUX
    20  `U+A1B9 <https://codepoints.net/U+A1B9>`_  '\\ua1b9'  Lo                  2  YI SYLLABLE LI
   ===  =========================================  =========  ==========  =========  ================

Total codepoints: 20


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x8a\xbe\xea\x82\xb7\xea\x88\x80\xea\x90\xa5\xea\x8c\xa0\xea\x83\x85\xea\x84\x9c\xea\x8b\x8a\xea\x84\xaf\xea\x92\x89\xea\x87\xac\xea\x85\x91\xea\x8c\xa0\xea\x8c\x85\xea\x85\x8d\xea\x8c\x8b\xea\x86\x80\xea\x84\xbf\xea\x90\xa8\xea\x86\xb9|\\n1234567890123456789012345678901234567890|\\n"
        ꊾꂷꈀꐥꌠꃅꄜꋊꄯꒉꇬꅑꌠꌅꅍꌋꆀꄿꐨꆹ|
        1234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 40,
  while *cool-retro-term* measures width 32.

.. _coolretrotermlangChineseMandarinTraditional:

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
  while *cool-retro-term* measures width 5.

.. _coolretrotermlangKhmerCentral:

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+1791 <https://codepoints.net/U+1791>`_  '\\u1791'  Lo                  1  KHMER LETTER TO
     2  `U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
     3  `U+17C6 <https://codepoints.net/U+17C6>`_  '\\u17c6'  Mn                  0  KHMER SIGN NIKAHIT
     4  `U+1784 <https://codepoints.net/U+1784>`_  '\\u1784'  Lo                  1  KHMER LETTER NGO
     5  `U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
     6  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
     7  `U+1793 <https://codepoints.net/U+1793>`_  '\\u1793'  Lo                  1  KHMER LETTER NO
     8  `U+17BB <https://codepoints.net/U+17BB>`_  '\\u17bb'  Mn                  0  KHMER VOWEL SIGN U
     9  `U+1784 <https://codepoints.net/U+1784>`_  '\\u1784'  Lo                  1  KHMER LETTER NGO
    10  `U+1785 <https://codepoints.net/U+1785>`_  '\\u1785'  Lo                  1  KHMER LETTER CA
    11  `U+17C6 <https://codepoints.net/U+17C6>`_  '\\u17c6'  Mn                  0  KHMER SIGN NIKAHIT
    12  `U+178E <https://codepoints.net/U+178E>`_  '\\u178e'  Lo                  1  KHMER LETTER NNO
    13  `U+17C4 <https://codepoints.net/U+17C4>`_  '\\u17c4'  Mc                  0  KHMER VOWEL SIGN OO
    14  `U+1798 <https://codepoints.net/U+1798>`_  '\\u1798'  Lo                  1  KHMER LETTER MO
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x91\xe1\x9e\xb6\xe1\x9f\x86\xe1\x9e\x84\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x93\xe1\x9e\xbb\xe1\x9e\x84\xe1\x9e\x85\xe1\x9f\x86\xe1\x9e\x8e\xe1\x9f\x84\xe1\x9e\x98|\\n12345678|\\n"
        ទាំងក្នុងចំណោម|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *cool-retro-term* measures width -16.

.. _coolretrotermlangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+80A4 <https://codepoints.net/U+80A4>`_  '\\u80a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-80A4
     2  `U+8272 <https://codepoints.net/U+8272>`_  '\\u8272'  Lo                  2  CJK UNIFIED IDEOGRAPH-8272
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x82\xa4\xe8\x89\xb2|\\n1234|\\n"
        肤色|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -6.

.. _coolretrotermlangKhn:

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ============================
     1  `U+1A21 <https://codepoints.net/U+1A21>`_  '\\u1a21'  Lo                  1  TAI THAM LETTER HIGH KHA
     2  `U+1A73 <https://codepoints.net/U+1A73>`_  '\\u1a73'  Mn                  0  TAI THAM VOWEL SIGN OA ABOVE
     3  `U+1A76 <https://codepoints.net/U+1A76>`_  '\\u1a76'  Mn                  0  TAI THAM SIGN TONE-2
   ===  =========================================  =========  ==========  =========  ============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xa1\xe1\xa9\xb3\xe1\xa9\xb6|\\n1|\\n"
        ᨡᩳ᩶|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *cool-retro-term* measures width -13.

.. _coolretrotermlangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     7  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "holisso|\\n1234567|\\n"
        holisso|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *cool-retro-term* measures width -9.

.. _coolretrotermlangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     5  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tsaate|\\n123456|\\n"
        tsaate|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width 1.

.. _coolretrotermlangGumuz:

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "haaga|\\n12345|\\n"
        haaga|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangMarathi:

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
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     5  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     7  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     8  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jonibaon|\\n12345678|\\n"
        jonibaon|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *cool-retro-term* measures width -9.

.. _coolretrotermlangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
     2  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     3  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     4  `U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
     5  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     6  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x81\xd0\xb0\xcc\x84\xd0\xbc\xd0\xb8.|\\n12345|\\n"
        са̄ми.|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "b\xc3\xa1|\\n12|\\n"
        bá|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -12.

.. _coolretrotermlangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0413 <https://codepoints.net/U+0413>`_  '\\u0413'  Lu                  1  CYRILLIC CAPITAL LETTER GHE
     2  `U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
     3  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     4  `U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
     5  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     6  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     7  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     8  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
     9  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
    10  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
    11  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\x93\xd0\xb5\xd0\xbd\xd0\xb5\xd1\x80\xd0\xb0\xcc\x84\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0|\\n1234567890|\\n"
        Генера̄лина|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *cool-retro-term* measures width 3.

.. _coolretrotermlangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     2  `U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
     3  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     4  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     5  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
     6  `U+044B <https://codepoints.net/U+044B>`_  '\\u044b'  Ll                  1  CYRILLIC SMALL LETTER YERU
     7  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     8  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb4\xd1\x8f\xd1\x80\xd0\xb8\xd1\x82\xd1\x8b\xd0\xbd.|\\n12345678|\\n"
        дяритын.|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *cool-retro-term* measures width 3.

.. _coolretrotermlangAmarakaeri:

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
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     2  `U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     5  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "e\xc3\xb1all|\\n12345|\\n"
        eñall|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangShan:

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
     2  `U+1084 <https://codepoints.net/U+1084>`_  '\\u1084'  Mc                  0  MYANMAR VOWEL SIGN SHAN E
     3  `U+1088 <https://codepoints.net/U+1088>`_  '\\u1088'  Mc                  0  MYANMAR SIGN SHAN TONE-3
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x9c\xe1\x82\x84\xe1\x82\x88|\\n1|\\n"
        လႄႈ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *cool-retro-term* measures width -24.

.. _coolretrotermlangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     4  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     5  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "deo'ye|\\n123456|\\n"
        deo'ye|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -2.

.. _coolretrotermlangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+043F <https://codepoints.net/U+043F>`_  '\\u043f'  Ll                  1  CYRILLIC SMALL LETTER PE
     2  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     3  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     4  `U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
     5  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbe|\\n12345|\\n"
        право|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangVeps:

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     6  `U+007A <https://codepoints.net/U+007A>`_  'z'       Ll                  1  LATIN SMALL LETTER Z
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     8  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     9  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
    10  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "oiktuziden|\\n1234567890|\\n"
        oiktuziden|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *cool-retro-term* measures width 5.

.. _coolretrotermlangNepali:

Nepali
^^^^^^

Sequence of language *Nepali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
     2  `U+0941 <https://codepoints.net/U+0941>`_  '\\u0941'  Mn                  0  DEVANAGARI VOWEL SIGN U
     3  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
     4  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     5  `U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
     6  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     7  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     8  `U+0907 <https://codepoints.net/U+0907>`_  '\\u0907'  Lo                  1  DEVANAGARI LETTER I
     9  `U+090F <https://codepoints.net/U+090F>`_  '\\u090f'  Lo                  1  DEVANAGARI LETTER E
    10  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
    11  `U+094B <https://codepoints.net/U+094B>`_  '\\u094b'  Mc                  0  DEVANAGARI VOWEL SIGN O
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xaa\xe0\xa5\x81\xe0\xa4\xb0\xe0\xa5\x8d\xe2\x80\x8d\xe0\xa4\xaf\xe0\xa4\xbe\xe0\xa4\x87\xe0\xa4\x8f\xe0\xa4\x95\xe0\xa5\x8b|\\n12345|\\n"
        पुर्‍याइएको|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width 6.

.. _coolretrotermlangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ve|\\n12|\\n"
        ve|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -9.

.. _coolretrotermlangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===================================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===================================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     4  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     7  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     8  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     9  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
   ===  =========================================  ========  ==========  =========  ===================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jeowesow\xc3\xab|\\n123456789|\\n"
        jeowesowë|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *cool-retro-term* measures width 2.

.. _coolretrotermlangBengali:

Bengali
^^^^^^^

Sequence of language *Bengali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0989 <https://codepoints.net/U+0989>`_  '\\u0989'  Lo                  1  BENGALI LETTER U
     2  `U+09A4 <https://codepoints.net/U+09A4>`_  '\\u09a4'  Lo                  1  BENGALI LETTER TA
     3  `U+09CD <https://codepoints.net/U+09CD>`_  '\\u09cd'  Mn                  0  BENGALI SIGN VIRAMA
     4  `U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
     5  `U+09AA <https://codepoints.net/U+09AA>`_  '\\u09aa'  Lo                  1  BENGALI LETTER PA
     6  `U+09C0 <https://codepoints.net/U+09C0>`_  '\\u09c0'  Mc                  0  BENGALI VOWEL SIGN II
     7  `U+09A1 <https://codepoints.net/U+09A1>`_  '\\u09a1'  Lo                  1  BENGALI LETTER DDA
     8  `U+09BC <https://codepoints.net/U+09BC>`_  '\\u09bc'  Mn                  0  BENGALI SIGN NUKTA
     9  `U+09A8 <https://codepoints.net/U+09A8>`_  '\\u09a8'  Lo                  1  BENGALI LETTER NA
    10  `U+09C7 <https://codepoints.net/U+09C7>`_  '\\u09c7'  Mc                  0  BENGALI VOWEL SIGN E
    11  `U+09B0 <https://codepoints.net/U+09B0>`_  '\\u09b0'  Lo                  1  BENGALI LETTER RA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\x89\xe0\xa6\xa4\xe0\xa7\x8d\xe2\x80\x8d\xe0\xa6\xaa\xe0\xa7\x80\xe0\xa6\xa1\xe0\xa6\xbc\xe0\xa6\xa8\xe0\xa7\x87\xe0\xa6\xb0|\\n12345|\\n"
        উত্‍পীড়নের|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width 6.

.. _coolretrotermlangBurmese:

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+1001 <https://codepoints.net/U+1001>`_  '\\u1001'  Lo                  1  MYANMAR LETTER KHA
     2  `U+103D <https://codepoints.net/U+103D>`_  '\\u103d'  Mn                  0  MYANMAR CONSONANT SIGN MEDIAL WA
     3  `U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
     4  `U+1037 <https://codepoints.net/U+1037>`_  '\\u1037'  Mn                  0  MYANMAR SIGN DOT BELOW
     5  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
     6  `U+1019 <https://codepoints.net/U+1019>`_  '\\u1019'  Lo                  1  MYANMAR LETTER MA
     7  `U+103B <https://codepoints.net/U+103B>`_  '\\u103b'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL YA
     8  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
     9  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
    10  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
    11  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
    12  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x81\xe1\x80\xbd\xe1\x80\x84\xe1\x80\xb7\xe1\x80\xba\xe1\x80\x99\xe1\x80\xbb\xe1\x80\xac\xe1\x80\xb8\xe1\x80\x80\xe1\x80\xad\xe1\x80\xaf|\\n1234|\\n"
        ခွင့်များကို|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangTamilSriLanka:

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0B87 <https://codepoints.net/U+0B87>`_  '\\u0b87'  Lo                  1  TAMIL LETTER I
     2  `U+0BB5 <https://codepoints.net/U+0BB5>`_  '\\u0bb5'  Lo                  1  TAMIL LETTER VA
     3  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     4  `U+0BB5 <https://codepoints.net/U+0BB5>`_  '\\u0bb5'  Lo                  1  TAMIL LETTER VA
     5  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     6  `U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
     7  `U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
     8  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
     9  `U+0BC8 <https://codepoints.net/U+0BC8>`_  '\\u0bc8'  Mc                  0  TAMIL VOWEL SIGN AI
    10  `U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
    11  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    12  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x87\xe0\xae\xb5\xe0\xaf\x8d\xe0\xae\xb5\xe0\xaf\x81\xe0\xae\xb0\xe0\xae\xbf\xe0\xae\xae\xe0\xaf\x88\xe0\xae\x95\xe0\xae\xb3\xe0\xaf\x8d|\\n1234567|\\n"
        இவ்வுரிமைகள்|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *cool-retro-term* measures width -6.

.. _coolretrotermlangTamil:

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0B9A <https://codepoints.net/U+0B9A>`_  '\\u0b9a'  Lo                  1  TAMIL LETTER CA
     2  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     3  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
     4  `U+0BA8 <https://codepoints.net/U+0BA8>`_  '\\u0ba8'  Lo                  1  TAMIL LETTER NA
     5  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     6  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
     7  `U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
     8  `U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
     9  `U+0B99 <https://codepoints.net/U+0B99>`_  '\\u0b99'  Lo                  1  TAMIL LETTER NGA
    10  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
    11  `U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
    12  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    13  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x9a\xe0\xaf\x81\xe0\xae\xa4\xe0\xae\xa8\xe0\xaf\x8d\xe0\xae\xa4\xe0\xae\xbf\xe0\xae\xb0\xe0\xae\x99\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xb3\xe0\xaf\x8d|\\n12345678|\\n"
        சுதந்திரங்கள்|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *cool-retro-term* measures width 1.

.. _coolretrotermlangColorado:

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     5  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "junshi|\\n123456|\\n"
        junshi|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+C18C <https://codepoints.net/U+C18C>`_  '\\uc18c'  Lo                  2  HANGUL SYLLABLE SO
     2  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x86\x8c.|\\n123|\\n"
        소.|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangKannada:

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0C9C <https://codepoints.net/U+0C9C>`_  '\\u0c9c'  Lo                  1  KANNADA LETTER JA
     2  `U+0CA8 <https://codepoints.net/U+0CA8>`_  '\\u0ca8'  Lo                  1  KANNADA LETTER NA
     3  `U+0CBF <https://codepoints.net/U+0CBF>`_  '\\u0cbf'  Mn                  0  KANNADA VOWEL SIGN I
     4  `U+0CB8 <https://codepoints.net/U+0CB8>`_  '\\u0cb8'  Lo                  1  KANNADA LETTER SA
     5  `U+0CBF <https://codepoints.net/U+0CBF>`_  '\\u0cbf'  Mn                  0  KANNADA VOWEL SIGN I
     6  `U+0CA6 <https://codepoints.net/U+0CA6>`_  '\\u0ca6'  Lo                  1  KANNADA LETTER DA
     7  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
     8  `U+0CA6 <https://codepoints.net/U+0CA6>`_  '\\u0ca6'  Lo                  1  KANNADA LETTER DA
     9  `U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
    10  `U+0CB0 <https://codepoints.net/U+0CB0>`_  '\\u0cb0'  Lo                  1  KANNADA LETTER RA
    11  `U+0CC6 <https://codepoints.net/U+0CC6>`_  '\\u0cc6'  Mn                  0  KANNADA VOWEL SIGN E
    12  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\x9c\xe0\xb2\xa8\xe0\xb2\xbf\xe0\xb2\xb8\xe0\xb2\xbf\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb2\xbe\xe0\xb2\xb0\xe0\xb3\x86.|\\n1234567|\\n"
        ಜನಿಸಿದ್ದಾರೆ.|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangTelugu:

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  =========
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  =========
     1  `U+0032 <https://codepoints.net/U+0032>`_  '2'       Nd                  1  DIGIT TWO
     2  `U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
   ===  =========================================  ========  ==========  =========  =========

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "2.|\\n12|\\n"
        2.|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -5.

.. _coolretrotermlangMon:

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================================
     1  `U+1015 <https://codepoints.net/U+1015>`_  '\\u1015'  Lo                  1  MYANMAR LETTER PA
     2  `U+1039 <https://codepoints.net/U+1039>`_  '\\u1039'  Mn                  0  MYANMAR SIGN VIRAMA
     3  `U+100D <https://codepoints.net/U+100D>`_  '\\u100d'  Lo                  1  MYANMAR LETTER DDA
     4  `U+1032 <https://codepoints.net/U+1032>`_  '\\u1032'  Mn                  0  MYANMAR VOWEL SIGN AI
     5  `U+1012 <https://codepoints.net/U+1012>`_  '\\u1012'  Lo                  1  MYANMAR LETTER DA
     6  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
     7  `U+101E <https://codepoints.net/U+101E>`_  '\\u101e'  Lo                  1  MYANMAR LETTER SA
     8  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
     9  `U+105F <https://codepoints.net/U+105F>`_  '\\u105f'  Mn                  0  MYANMAR CONSONANT SIGN MON MEDIAL MA
    10  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
    11  `U+1014 <https://codepoints.net/U+1014>`_  '\\u1014'  Lo                  1  MYANMAR LETTER NA
    12  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    13  `U+100D <https://codepoints.net/U+100D>`_  '\\u100d'  Lo                  1  MYANMAR LETTER DDA
    14  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
    15  `U+105A <https://codepoints.net/U+105A>`_  '\\u105a'  Lo                  1  MYANMAR LETTER MON NGA
    16  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
   ===  =========================================  =========  ==========  =========  ====================================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x95\xe1\x80\xb9\xe1\x80\x8d\xe1\x80\xb2\xe1\x80\x92\xe1\x80\xb1\xe1\x80\x9e\xe1\x80\x80\xe1\x81\x9f\xe1\x80\xad\xe1\x80\x94\xe1\x80\xba\xe1\x80\x8d\xe1\x80\xaf\xe1\x81\x9a\xe1\x80\xba|\\n12345678|\\n"
        ပ္ဍဲဒေသကၟိန်ဍုၚ်|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *cool-retro-term* measures width 4.

.. _coolretrotermlangKorean:

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+D560 <https://codepoints.net/U+D560>`_  '\\ud560'  Lo                  2  HANGUL SYLLABLE HAL
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xed\x95\xa0|\\n12|\\n"
        할|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -8.

.. _coolretrotermlangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     2  `U+0269 <https://codepoints.net/U+0269>`_  '\\u0269'  Ll                  1  LATIN SMALL LETTER IOTA
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc9\xa9|\\n12|\\n"
        tɩ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "que|\\n123|\\n"
        que|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width -8.

.. _coolretrotermlangMaldivian:

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
     2  `U+07A8 <https://codepoints.net/U+07A8>`_  '\\u07a8'  Mn                  0  THAANA IBIFILI
     3  `U+0782 <https://codepoints.net/U+0782>`_  '\\u0782'  Lo                  1  THAANA LETTER NOONU
     4  `U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
     5  `U+0790 <https://codepoints.net/U+0790>`_  '\\u0790'  Lo                  1  THAANA LETTER SEENU
     6  `U+07A7 <https://codepoints.net/U+07A7>`_  '\\u07a7'  Mn                  0  THAANA AABAAFILI
     7  `U+0782 <https://codepoints.net/U+0782>`_  '\\u0782'  Lo                  1  THAANA LETTER NOONU
     8  `U+07A9 <https://codepoints.net/U+07A9>`_  '\\u07a9'  Mn                  0  THAANA EEBEEFILI
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x87\xde\xa8\xde\x82\xde\xb0\xde\x90\xde\xa7\xde\x82\xde\xa9|\\n1234|\\n"
        އިންސާނީ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangMirandese:

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
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "de|\\n12|\\n"
        de|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -10.

.. _coolretrotermlangw:

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+007A <https://codepoints.net/U+007A>`_  'z'       Ll                  1  LATIN SMALL LETTER Z
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "dzi|\\n123|\\n"
        dzi|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width -8.

.. _coolretrotermlangSanskrit:

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     2  `U+0941 <https://codepoints.net/U+0941>`_  '\\u0941'  Mn                  0  DEVANAGARI VOWEL SIGN U
     3  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     4  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     5  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     6  `U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
     7  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     8  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     9  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
    10  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    11  `U+0903 <https://codepoints.net/U+0903>`_  '\\u0903'  Mc                  0  DEVANAGARI SIGN VISARGA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa5\x81\xe0\xa4\xb8\xe0\xa4\xae\xe0\xa5\x8d\xe0\xa4\xaa\xe0\xa4\xa8\xe0\xa5\x8d\xe0\xa4\xa8\xe0\xa4\xbe\xe0\xa4\x83|\\n123456|\\n"
        सुसम्पन्नाः|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -7.

.. _coolretrotermlangSanskritGrantha:

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =====================
     1  `U+00011338 <https://codepoints.net/U+00011338>`_  '\\U00011338'  Lo                  1  GRANTHA LETTER SA
     2  `U+00011341 <https://codepoints.net/U+00011341>`_  '\\U00011341'  Mc                  0  GRANTHA VOWEL SIGN U
     3  `U+00011338 <https://codepoints.net/U+00011338>`_  '\\U00011338'  Lo                  1  GRANTHA LETTER SA
     4  `U+0001132E <https://codepoints.net/U+0001132E>`_  '\\U0001132e'  Lo                  1  GRANTHA LETTER MA
     5  `U+0001134D <https://codepoints.net/U+0001134D>`_  '\\U0001134d'  Mc                  0  GRANTHA SIGN VIRAMA
     6  `U+0001132A <https://codepoints.net/U+0001132A>`_  '\\U0001132a'  Lo                  1  GRANTHA LETTER PA
     7  `U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
     8  `U+0001134D <https://codepoints.net/U+0001134D>`_  '\\U0001134d'  Mc                  0  GRANTHA SIGN VIRAMA
     9  `U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
    10  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
    11  `U+00011303 <https://codepoints.net/U+00011303>`_  '\\U00011303'  Mc                  0  GRANTHA SIGN VISARGA
   ===  =================================================  =============  ==========  =========  =====================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xb8\xf0\x91\x8d\x81\xf0\x91\x8c\xb8\xf0\x91\x8c\xae\xf0\x91\x8d\x8d\xf0\x91\x8c\xaa\xf0\x91\x8c\xa8\xf0\x91\x8d\x8d\xf0\x91\x8c\xa8\xf0\x91\x8c\xbe\xf0\x91\x8c\x83|\\n123456|\\n"
        𑌸𑍁𑌸𑌮𑍍𑌪𑌨𑍍𑌨𑌾𑌃|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -7.

.. _coolretrotermlangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "d's\xc3\xa8s|\\n12345|\\n"
        d'sès|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width 3.

.. _coolretrotermlangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+05D3 <https://codepoints.net/U+05D3>`_  '\\u05d3'  Lo                  1  HEBREW LETTER DALET
     2  `U+05D9 <https://codepoints.net/U+05D9>`_  '\\u05d9'  Lo                  1  HEBREW LETTER YOD
     3  `U+05BE <https://codepoints.net/U+05BE>`_  '\\u05be'  Pd                  1  HEBREW PUNCTUATION MAQAF
     4  `U+05D0 <https://codepoints.net/U+05D0>`_  '\\u05d0'  Lo                  1  HEBREW LETTER ALEF
     5  `U+05B8 <https://codepoints.net/U+05B8>`_  '\\u05b8'  Mn                  0  HEBREW POINT QAMATS
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x93\xd7\x99\xd6\xbe\xd7\x90\xd6\xb8|\\n1234|\\n"
        די־אָ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangTicuna:

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     4  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     5  `U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'    Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
     6  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     7  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
     8  `U+1EBD <https://codepoints.net/U+1EBD>`_  '\\u1ebd'  Ll                  1  LATIN SMALL LETTER E WITH TILDE
     9  `U+1EBD <https://codepoints.net/U+1EBD>`_  '\\u1ebd'  Ll                  1  LATIN SMALL LETTER E WITH TILDE
    10  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
    11  `U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'    Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
    12  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
    13  `U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'    Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
    14  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
    15  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
    16  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    17  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
    18  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nang\xc3\xbc\xcc\x83x\xe1\xba\xbd\xe1\xba\xbdg\xc3\xbcx\xc3\xbc\xcc\x83ca\xcc\xb1x|\\n123456789012345|\\n"
        nangü̃xẽẽgüxü̃ca̱x|
        123456789012345|

- python `wcwidth.wcswidth()`_ measures width 15,
  while *cool-retro-term* measures width 11.

.. _coolretrotermlangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "belli|\\n12345|\\n"
        belli|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -5.

.. _coolretrotermlangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     4  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     5  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     6  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yango\xcc\x81|\\n12345|\\n"
        yangó|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
     2  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Imi|\\n123|\\n"
        Imi|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width -8.

.. _coolretrotermlangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
     2  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     3  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
     4  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xa1l\xc3\xa1\xc5\x8b|\\n1234|\\n"
        áláŋ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =======================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =======================
     1  `U+0001E934 <https://codepoints.net/U+0001E934>`_  '\\U0001e934'  Ll                  1  ADLAM SMALL LETTER YA
     2  `U+0001E92D <https://codepoints.net/U+0001E92D>`_  '\\U0001e92d'  Ll                  1  ADLAM SMALL LETTER I
     3  `U+0001E925 <https://codepoints.net/U+0001E925>`_  '\\U0001e925'  Ll                  1  ADLAM SMALL LETTER MIIM
     4  `U+0001E929 <https://codepoints.net/U+0001E929>`_  '\\U0001e929'  Ll                  1  ADLAM SMALL LETTER BHE
     5  `U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
   ===  =================================================  =============  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xb4\xf0\x9e\xa4\xad\xf0\x9e\xa4\xa5\xf0\x9e\xa4\xa9\xf0\x9e\xa4\xab|\\n12345|\\n"
        𞤴𞤭𞤥𞤩𞤫|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -8.

.. _coolretrotermlangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0641 <https://codepoints.net/U+0641>`_  '\\u0641'  Lo                  1  ARABIC LETTER FEH
     2  `U+0639 <https://codepoints.net/U+0639>`_  '\\u0639'  Lo                  1  ARABIC LETTER AIN
     3  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     4  `U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
     5  `U+0629 <https://codepoints.net/U+0629>`_  '\\u0629'  Lo                  1  ARABIC LETTER TEH MARBUTA
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x81\xd8\xb9\xd8\xa7\xd9\x84\xd8\xa9|\\n12345|\\n"
        فعالة|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     2  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "chi|\\n123|\\n"
        chi|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width -8.

.. _coolretrotermlangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "de\xcc\x81|\\n12|\\n"
        dé|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -10.

.. _coolretrotermlangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     3  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     4  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "dom\xc9\x9b|\\n1234|\\n"
        domɛ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0718 <https://codepoints.net/U+0718>`_  '\\u0718'  Lo                  1  SYRIAC LETTER WAW
     2  `U+0722 <https://codepoints.net/U+0722>`_  '\\u0722'  Lo                  1  SYRIAC LETTER NUN
     3  `U+072B <https://codepoints.net/U+072B>`_  '\\u072b'  Lo                  1  SYRIAC LETTER SHIN
     4  `U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\x98\xdc\xa2\xdc\xab\xdc\x90|\\n1234|\\n"
        ܘܢܫܐ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "koni|\\n1234|\\n"
        koni|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width 2.

.. _coolretrotermlangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x94|\\n12|\\n"
        nɔ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangUduk:

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     2  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "imina|\\n12345|\\n"
        imina|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width 1.

.. _coolretrotermlangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004B <https://codepoints.net/U+004B>`_  'K'       Lu                  1  LATIN CAPITAL LETTER K
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Ka|\\n12|\\n"
        Ka|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -9.

.. _coolretrotermlangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

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
  while *cool-retro-term* measures width -4.

.. _coolretrotermlangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+062C <https://codepoints.net/U+062C>`_  '\\u062c'  Lo                  1  ARABIC LETTER JEEM
     3  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
     4  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     5  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd8\xac\xd8\xb1\xd8\xa7\xdb\x8c|\\n12345|\\n"
        اجرای|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width 4.

.. _coolretrotermlangMaithili:

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0906 <https://codepoints.net/U+0906>`_  '\\u0906'  Lo                  1  DEVANAGARI LETTER AA
     2  `U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x86\xca\xbc|\\n12|\\n"
        आʼ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     2  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     8  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "eyithiic|\\n12345678|\\n"
        eyithiic|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *cool-retro-term* measures width 4.

.. _coolretrotermlangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     5  `U+00E3 <https://codepoints.net/U+00E3>`_  '\\xe3'   Ll                  1  LATIN SMALL LETTER A WITH TILDE
     6  `U+002E <https://codepoints.net/U+002E>`_  '.'       Po                  1  FULL STOP
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nins\xc3\xa3.|\\n123456|\\n"
        ninsã.|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width 2.

.. _coolretrotermlangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     2  `U+1ECD <https://codepoints.net/U+1ECD>`_  '\\u1ecd'  Ll                  1  LATIN SMALL LETTER O WITH DOT BELOW
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "j\xe1\xbb\x8d|\\n12|\\n"
        jọ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     2  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
     3  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     4  `U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
     5  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     6  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaa\xd8\xaf\xd8\xa7\xd8\xa8\xdb\x8c\xd8\xb1|\\n123456|\\n"
        تدابیر|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width 4.

.. _coolretrotermlangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     3  `U+0309 <https://codepoints.net/U+0309>`_  '\\u0309'  Mn                  0  COMBINING HOOK ABOVE
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "cu\xcc\x89a|\\n123|\\n"
        của|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangDitammari:

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
     3  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     4  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     5  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     6  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "y\xc9\x9bh\xc9\x9bk\xc9\x9b|\\n123456|\\n"
        yɛhɛkɛ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "w\xc9\x94|\\n12|\\n"
        wɔ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -5.

.. _coolretrotermlangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jo'o|\\n1234|\\n"
        jo'o|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width 2.

.. _coolretrotermlangSererSine:

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
     2  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     6  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     8  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Artiikal|\\n12345678|\\n"
        Artiikal|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *cool-retro-term* measures width 4.

.. _coolretrotermlangUrdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
     2  `U+062E <https://codepoints.net/U+062E>`_  '\\u062e'  Lo                  1  ARABIC LETTER KHAH
     3  `U+0635 <https://codepoints.net/U+0635>`_  '\\u0635'  Lo                  1  ARABIC LETTER SAD
     4  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     5  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xb4\xd8\xae\xd8\xb5\xdb\x8c\xd8\xaa|\\n12345|\\n"
        شخصیت|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+067E <https://codepoints.net/U+067E>`_  '\\u067e'  Lo                  1  ARABIC LETTER PEH
     2  `U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\xbe\xd9\x87|\\n12|\\n"
        په|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     3  `U+06BA <https://codepoints.net/U+06BA>`_  '\\u06ba'  Lo                  1  ARABIC LETTER NOON GHUNNA
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xd9\x88\xda\xba|\\n123|\\n"
        کوں|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ta|\\n12|\\n"
        ta|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -2.

.. _coolretrotermlangUrdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

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
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangDagaareSouthern:

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+003A <https://codepoints.net/U+003A>`_  ':'       Po                  1  COLON
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "la:|\\n123|\\n"
        la:|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width -2.

.. _coolretrotermlangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

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
  while *cool-retro-term* measures width -2.

.. _coolretrotermlangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     4  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nju\xcc\x81|\\n123|\\n"
        njú|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "karan|\\n12345|\\n"
        karan|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width -3.

.. _coolretrotermlangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
     2  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     3  `U+06C1 <https://codepoints.net/U+06C1>`_  '\\u06c1'  Lo                  1  ARABIC LETTER HEH GOAL
     4  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     5  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     6  `U+06BA <https://codepoints.net/U+06BA>`_  '\\u06ba'  Lo                  1  ARABIC LETTER NOON GHUNNA
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x84\xd9\x88\xdb\x81\xd9\x86\xd8\xa7\xda\xba|\\n123456|\\n"
        لوہناں|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *cool-retro-term* measures width 3.

.. _coolretrotermlangChinantecChiltepec:

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     5  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "juso\xcc\xb1|\\n1234|\\n"
        juso̱|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width 1.

.. _coolretrotermlangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "sisi|\\n1234|\\n"
        sisi|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width 1.

.. _coolretrotermlangChakma:

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =================
     1  `U+0001111D <https://codepoints.net/U+0001111D>`_  '\\U0001111d'  Lo                  1  CHAKMA LETTER BAA
   ===  =================================================  =============  ==========  =========  =================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\x9d|\\n1|\\n"
        𑄝|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *cool-retro-term* measures width -2.

.. _coolretrotermlangJavaneseJavanese:

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+A98F <https://codepoints.net/U+A98F>`_  '\\ua98f'  Lo                  1  JAVANESE LETTER KA
     2  `U+A981 <https://codepoints.net/U+A981>`_  '\\ua981'  Mn                  0  JAVANESE SIGN CECAK
     3  `U+A992 <https://codepoints.net/U+A992>`_  '\\ua992'  Lo                  1  JAVANESE LETTER GA
     4  `U+A9BA <https://codepoints.net/U+A9BA>`_  '\\ua9ba'  Mc                  0  JAVANESE VOWEL SIGN TALING
     5  `U+A9B4 <https://codepoints.net/U+A9B4>`_  '\\ua9b4'  Mc                  0  JAVANESE VOWEL SIGN TARUNG
     6  `U+A98F <https://codepoints.net/U+A98F>`_  '\\ua98f'  Lo                  1  JAVANESE LETTER KA
     7  `U+A9B1 <https://codepoints.net/U+A9B1>`_  '\\ua9b1'  Lo                  1  JAVANESE LETTER SA
     8  `U+A9B6 <https://codepoints.net/U+A9B6>`_  '\\ua9b6'  Mn                  0  JAVANESE VOWEL SIGN WULU
     9  `U+A9AD <https://codepoints.net/U+A9AD>`_  '\\ua9ad'  Lo                  1  JAVANESE LETTER LA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\x8f\xea\xa6\x81\xea\xa6\x92\xea\xa6\xba\xea\xa6\xb4\xea\xa6\x8f\xea\xa6\xb1\xea\xa6\xb6\xea\xa6\xad|\\n12345|\\n"
        ꦏꦁꦒꦺꦴꦏꦱꦶꦭ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *cool-retro-term* measures width 2.

.. _coolretrotermlangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     5  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     6  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     7  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bini'ju|\\n1234567|\\n"
        bini'ju|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *cool-retro-term* measures width 4.

.. _coolretrotermlangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

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
  while *cool-retro-term* measures width -2.

.. _coolretrotermlangGujarati:

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0A95 <https://codepoints.net/U+0A95>`_  '\\u0a95'  Lo                  1  GUJARATI LETTER KA
     2  `U+0ACB <https://codepoints.net/U+0ACB>`_  '\\u0acb'  Mc                  0  GUJARATI VOWEL SIGN O
     3  `U+0A87 <https://codepoints.net/U+0A87>`_  '\\u0a87'  Lo                  1  GUJARATI LETTER I
     4  `U+0AAA <https://codepoints.net/U+0AAA>`_  '\\u0aaa'  Lo                  1  GUJARATI LETTER PA
     5  `U+0AA3 <https://codepoints.net/U+0AA3>`_  '\\u0aa3'  Lo                  1  GUJARATI LETTER NNA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\x95\xe0\xab\x8b\xe0\xaa\x87\xe0\xaa\xaa\xe0\xaa\xa3|\\n1234|\\n"
        કોઇપણ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *cool-retro-term* measures width 1.

.. _coolretrotermlangDangme:

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc9\x94|\\n1|\\n"
        ɔ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *cool-retro-term* measures width -1.

.. _coolretrotermlangHindi:

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     2  `U+0939 <https://codepoints.net/U+0939>`_  '\\u0939'  Lo                  1  DEVANAGARI LETTER HA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xaf\xe0\xa4\xb9|\\n12|\\n"
        यह|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangMagahi:

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     2  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     3  `U+0925 <https://codepoints.net/U+0925>`_  '\\u0925'  Lo                  1  DEVANAGARI LETTER THA
     4  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
     5  `U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
     6  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa5\xe0\xa4\xbf\xe0\xa4\xa4\xe0\xa4\xbf|\\n123|\\n"
        स्थिति|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangBhojpuri:

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb5\xe0\xa4\xbe|\\n1|\\n"
        वा|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *cool-retro-term* measures width -4.

.. _coolretrotermlangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
     2  `U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
     3  `U+0F9F <https://codepoints.net/U+0F9F>`_  '\\u0f9f'  Mn                  0  TIBETAN SUBJOINED LETTER TA
     4  `U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x96\xe0\xbd\xa6\xe0\xbe\x9f\xe0\xbd\xa2|\\n123|\\n"
        བསྟར|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width 0.

.. _coolretrotermlangPanjabiEastern:

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0A38 <https://codepoints.net/U+0A38>`_  '\\u0a38'  Lo                  1  GURMUKHI LETTER SA
     2  `U+0A2E <https://codepoints.net/U+0A2E>`_  '\\u0a2e'  Lo                  1  GURMUKHI LETTER MA
     3  `U+0A3E <https://codepoints.net/U+0A3E>`_  '\\u0a3e'  Mc                  0  GURMUKHI VOWEL SIGN AA
     4  `U+0A1C <https://codepoints.net/U+0A1C>`_  '\\u0a1c'  Lo                  1  GURMUKHI LETTER JA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\xb8\xe0\xa8\xae\xe0\xa8\xbe\xe0\xa8\x9c|\\n123|\\n"
        ਸਮਾਜ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *cool-retro-term* measures width 2.

.. _coolretrotermlangTaiDam:

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+AA8B <https://codepoints.net/U+AA8B>`_  '\\uaa8b'  Lo                  1  TAI VIET LETTER HIGH CO
     2  `U+AAB4 <https://codepoints.net/U+AAB4>`_  '\\uaab4'  Mn                  0  TAI VIET VOWEL U
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\x8b\xea\xaa\xb4|\\n1|\\n"
        ꪋꪴ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *cool-retro-term* measures width -2.

.. _coolretrotermlangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
     2  `U+0FB2 <https://codepoints.net/U+0FB2>`_  '\\u0fb2'  Mn                  0  TIBETAN SUBJOINED LETTER RA
     3  `U+0F74 <https://codepoints.net/U+0F74>`_  '\\u0f74'  Mn                  0  TIBETAN VOWEL SIGN U
     4  `U+0F56 <https://codepoints.net/U+0F56>`_  '\\u0f56'  Lo                  1  TIBETAN LETTER BA
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x82\xe0\xbe\xb2\xe0\xbd\xb4\xe0\xbd\x96|\\n12|\\n"
        གྲུབ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *cool-retro-term* measures width -1.

.. _coolretrotermdecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

This Terminal does not appear capable of reporting about any DEC Private modes.

.. _coolretrotermreproduce:

Reproduction
++++++++++++

To reproduce these results for *cool-retro-term*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --save-yaml=macos-cool-retro-term-1.2.0.yaml \
        --limit-codepoints=5000 \
        --limit-words=5000 \
        --limit-errors=1000

.. _coolretrotermtime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **72.09 seconds** (72s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
