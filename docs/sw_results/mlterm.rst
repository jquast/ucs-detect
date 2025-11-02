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

.. table::
   :class: sphinx-datatable

   ============  ===========  ==============  ======================================================
   Score Type    Raw Score    Scaled Score    Calculation
   ============  ===========  ==============  ======================================================
   WIDE          72.73%       58.9%           (version_index / total_versions) × (pct_success / 100)
   ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
   LANG          98.77%       99.1%           geometric_mean(language_percentages)
   VS16          0.00%        0.0%            pct_success / 100
   VS15          0.00%        0.0%            pct_success / 100
   DEC Modes     21.66%       36.0%           modes_changeable / total_modes
   TIME          56.45s       83.5%           1 - ((elapsed - min) / (max - min)) [inverse]
   ============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 32.19%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 20.8%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

**WIDE Score Details:**

Wide character support calculation:
- Best matching Unicode version: 15.0.0
- Version index: 8 of 11 versions tested
- Success rate at this version: 100.0%
- Formula: (8 / 11) × (100.0 / 100)
- Result: 72.73%

**ZWJ Score Details:**

No ZWJ support detected.

**VS16 Score Details:**

Variation Selector-16 support calculation:
- Errors: 213 of 213 codepoints tested
- Success rate: 0.0%
- Formula: 0.0 / 100
- Result: 0.00%

**VS15 Score Details:**

Variation Selector-15 support calculation:
- Errors: 158 of 158 codepoints tested
- Success rate: 0.0%
- Formula: 0.0 / 100
- Result: 0.00%

**DEC Modes Score Details:**

DEC Private Modes support calculation:
- Changeable modes: 34
- Total modes tested: 157
- Formula: 34 / 157
- Result: 21.66%

**TIME Score Details:**

Test execution time:
- Elapsed time: 56.45 seconds
- Note: This is a raw measurement; lower is better
- Scaled score uses inverse log10 scaling across all terminals
- Scaled result: 83.5%

**LANG Score Details (Geometric Mean):**

Geometric mean calculation:
- Formula: (p₁ × p₂ × ... × pₙ)^(1/n) where n = 119 languages
- About `geometric mean <https://en.wikipedia.org/wiki/Geometric_mean>`_
- Result: 98.77%

.. _mltermwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for mlterm appears to be 
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
  while *mlterm* measures width 1.

.. _mltermzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *mlterm* appears to be 
**None**, this is from a summary of the following
results:


.. table::
   :class: sphinx-datatable

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
  while *mlterm* measures width 11.

.. _mltermvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *mlterm* is 213 errors
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
  while *mlterm* measures width 1.


.. _mltermvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *mlterm* is 158 errors
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
  while *mlterm* measures width 2.


.. _mltermlang:

Language Support
++++++++++++++++

The following 2 languages were tested with 100% success:

Tagalog (Tagalog), Tamang, Eastern.

The following 117 languages are not fully supported:

.. table::
   :class: sphinx-datatable

   =============================================================================  ==========  =========  =============
   lang                                                                             n_errors    n_total  pct_success
   =============================================================================  ==========  =========  =============
   :ref:`Malayalam <mltermlangMalayalam>`                                                364       1630  77.7%
   :ref:`Javanese (Javanese) <mltermlangJavaneseJavanese>`                               241       1453  83.4%
   :ref:`Mongolian, Halh (Mongolian) <mltermlangMongolianHalhMongolian>`                   3         33  90.9%
   :ref:`Sinhala <mltermlangSinhala>`                                                    113       1655  93.2%
   :ref:`Bengali <mltermlangBengali>`                                                     84       1413  94.1%
   :ref:`Farsi, Western <mltermlangFarsiWestern>`                                         46       1822  97.5%
   :ref:`Chinese, Mandarin (Guiyang) <mltermlangChineseMandarinGuiyang>`                   5        211  97.6%
   :ref:`Chinese, Xiang <mltermlangChineseXiang>`                                          5        212  97.6%
   :ref:`Dari <mltermlangDari>`                                                           43       1872  97.7%
   :ref:`Japanese (Osaka) <mltermlangJapaneseOsaka>`                                       7        308  97.7%
   :ref:`Chinese, Mandarin (Harbin) <mltermlangChineseMandarinHarbin>`                     4        210  98.1%
   :ref:`Chinese, Wu <mltermlangChineseWu>`                                                4        211  98.1%
   :ref:`Chinese, Mandarin (Beijing) <mltermlangChineseMandarinBeijing>`                   4        212  98.1%
   :ref:`Chinese, Mandarin (Tianjin) <mltermlangChineseMandarinTianjin>`                   4        212  98.1%
   :ref:`Thai <mltermlangThai>`                                                            6        341  98.2%
   :ref:`Japanese <mltermlangJapanese>`                                                    5        299  98.3%
   :ref:`Thai (2) <mltermlangThai2>`                                                       5        313  98.4%
   :ref:`Japanese (Tokyo) <mltermlangJapaneseTokyo>`                                       5        320  98.4%
   :ref:`Chinese, Mandarin (Traditional) <mltermlangChineseMandarinTraditional>`           3        210  98.6%
   :ref:`Chinese, Mandarin (Simplified) <mltermlangChineseMandarinSimplified>`             3        225  98.7%
   :ref:`Lao <mltermlangLao>`                                                              5        425  98.8%
   :ref:`Khmer, Central <mltermlangKhmerCentral>`                                          6        528  98.9%
   :ref:`Vietnamese (Han nom) <mltermlangVietnameseHannom>`                                2        199  99.0%
   :ref:`Chinese, Yue <mltermlangChineseYue>`                                              2        210  99.0%
   :ref:`(Jinan) <mltermlangJinan>`                                                        2        211  99.1%
   :ref:`Chinese, Gan <mltermlangChineseGan>`                                              2        211  99.1%
   :ref:`Chinese, Hakka <mltermlangChineseHakka>`                                          2        212  99.1%
   :ref:`Chinese, Jinyu <mltermlangChineseJinyu>`                                          2        212  99.1%
   :ref:`Chinese, Mandarin (Nanjing) <mltermlangChineseMandarinNanjing>`                   2        212  99.1%
   :ref:`Chinese, Min Nan <mltermlangChineseMinNan>`                                       2        212  99.1%
   :ref:`Marathi <mltermlangMarathi>`                                                     15       1614  99.1%
   :ref:`Yaneshaʼ <mltermlangYanesha>`                                                    23       2536  99.1%
   :ref:`Khün <mltermlangKhn>`                                                             4        442  99.1%
   :ref:`Chickasaw <mltermlangChickasaw>`                                                  5        554  99.1%
   :ref:`Nuosu <mltermlangNuosu>`                                                          2        230  99.1%
   :ref:`Bora <mltermlangBora>`                                                           13       1598  99.2%
   :ref:`Orok <mltermlangOrok>`                                                            9       1245  99.3%
   :ref:`Shipibo-Conibo <mltermlangShipiboConibo>`                                        18       2540  99.3%
   :ref:`Gumuz <mltermlangGumuz>`                                                          9       1283  99.3%
   :ref:`Veps <mltermlangVeps>`                                                            9       1323  99.3%
   :ref:`Evenki <mltermlangEvenki>`                                                        6        899  99.3%
   :ref:`Nanai <mltermlangNanai>`                                                          8       1207  99.3%
   :ref:`Shan <mltermlangShan>`                                                            6        915  99.3%
   :ref:`Kannada <mltermlangKannada>`                                                      7       1080  99.4%
   :ref:`South Azerbaijani <mltermlangSouthAzerbaijani>`                                   9       1396  99.4%
   :ref:`Navajo <mltermlangNavajo>`                                                       10       1600  99.4%
   :ref:`Amarakaeri <mltermlangAmarakaeri>`                                                9       1446  99.4%
   :ref:`Siona <mltermlangSiona>`                                                          9       1492  99.4%
   :ref:`Gilyak <mltermlangGilyak>`                                                        9       1504  99.4%
   :ref:`Korean <mltermlangKorean>`                                                        7       1185  99.4%
   :ref:`Nepali <mltermlangNepali>`                                                        8       1385  99.4%
   :ref:`Burmese <mltermlangBurmese>`                                                      7       1223  99.4%
   :ref:`Secoya <mltermlangSecoya>`                                                        8       1409  99.4%
   :ref:`(Yeonbyeon) <mltermlangYeonbyeon>`                                                6       1061  99.4%
   :ref:`Yiddish, Eastern <mltermlangYiddishEastern>`                                     10       1775  99.4%
   :ref:`Tamil (Sri Lanka) <mltermlangTamilSriLanka>`                                      7       1261  99.4%
   :ref:`Tamil <mltermlangTamil>`                                                          7       1262  99.4%
   :ref:`Colorado <mltermlangColorado>`                                                    7       1263  99.4%
   :ref:`Kabyle <mltermlangKabyle>`                                                       10       1815  99.4%
   :ref:`Telugu <mltermlangTelugu>`                                                        6       1129  99.5%
   :ref:`Mon <mltermlangMon>`                                                              5        946  99.5%
   :ref:`Sanskrit <mltermlangSanskrit>`                                                    5       1000  99.5%
   :ref:`Sanskrit (Grantha) <mltermlangSanskritGrantha>`                                   5       1006  99.5%
   :ref:`Ticuna <mltermlangTicuna>`                                                       10       2048  99.5%
   :ref:`Tem <mltermlangTem>`                                                              8       1659  99.5%
   :ref:`Catalan (2) <mltermlangCatalan2>`                                                 9       1909  99.5%
   :ref:`Maldivian <mltermlangMaldivian>`                                                  9       1918  99.5%
   :ref:`Mirandese <mltermlangMirandese>`                                                  9       1966  99.5%
   :ref:`Panjabi, Western <mltermlangPanjabiWestern>`                                     11       2419  99.5%
   :ref:`Éwé <mltermlangw>`                                                               10       2230  99.6%
   :ref:`Arabic, Standard <mltermlangArabicStandard>`                                      6       1348  99.6%
   :ref:`Picard <mltermlangPicard>`                                                        9       2024  99.6%
   :ref:`Lingala (tones) <mltermlangLingalatones>`                                         8       1818  99.6%
   :ref:`Tamazight, Central Atlas <mltermlangTamazightCentralAtlas>`                       8       1822  99.6%
   :ref:`Mixtec, Metlatónoc <mltermlangMixtecMetlatnoc>`                                   6       1367  99.6%
   :ref:`Fur <mltermlangFur>`                                                              8       1838  99.6%
   :ref:`Pular (Adlam) <mltermlangPularAdlam>`                                             7       1613  99.6%
   :ref:`Assyrian Neo-Aramaic <mltermlangAssyrianNeoAramaic>`                              5       1160  99.6%
   :ref:`Maori (2) <mltermlangMaori2>`                                                    10       2385  99.6%
   :ref:`French (Welche) <mltermlangFrenchWelche>`                                         8       1928  99.6%
   :ref:`Urdu <mltermlangUrdu>`                                                            9       2237  99.6%
   :ref:`Uduk <mltermlangUduk>`                                                           13       3247  99.6%
   :ref:`Waama <mltermlangWaama>`                                                          4       1000  99.6%
   :ref:`Urdu (2) <mltermlangUrdu2>`                                                       9       2251  99.6%
   :ref:`Saint Lucian Creole French <mltermlangSaintLucianCreoleFrench>`                   7       1777  99.6%
   :ref:`Bamun <mltermlangBamun>`                                                          9       2285  99.6%
   :ref:`Ga <mltermlangGa>`                                                                8       2039  99.6%
   :ref:`Gen <mltermlangGen>`                                                              9       2309  99.6%
   :ref:`Aja <mltermlangAja>`                                                              8       2061  99.6%
   :ref:`Dendi <mltermlangDendi>`                                                          6       1569  99.6%
   :ref:`Mazahua Central <mltermlangMazahuaCentral>`                                       6       1574  99.6%
   :ref:`Serer-Sine <mltermlangSererSine>`                                                 6       1596  99.6%
   :ref:`Ditammari <mltermlangDitammari>`                                                  7       1882  99.6%
   :ref:`Mòoré <mltermlangMor>`                                                            9       2447  99.6%
   :ref:`Yoruba <mltermlangYoruba>`                                                        9       2454  99.6%
   :ref:`Baatonum <mltermlangBaatonum>`                                                    7       1939  99.6%
   :ref:`Vietnamese <mltermlangVietnamese>`                                                9       2502  99.6%
   :ref:`Lamnso' <mltermlangLamnso>`                                                       8       2237  99.6%
   :ref:`Pashto, Northern <mltermlangPashtoNorthern>`                                      8       2242  99.6%
   :ref:`Seraiki <mltermlangSeraiki>`                                                      8       2242  99.6%
   :ref:`Belanda Viri <mltermlangBelandaViri>`                                             8       2246  99.6%
   :ref:`Dagaare, Southern <mltermlangDagaareSouthern>`                                    9       2582  99.7%
   :ref:`Chinantec, Chiltepec <mltermlangChinantecChiltepec>`                              6       1729  99.7%
   :ref:`Chakma <mltermlangChakma>`                                                        5       1444  99.7%
   :ref:`Maithili <mltermlangMaithili>`                                                    5       1519  99.7%
   :ref:`Dinka, Northeastern <mltermlangDinkaNortheastern>`                                5       1529  99.7%
   :ref:`Gujarati <mltermlangGujarati>`                                                    5       1536  99.7%
   :ref:`Otomi, Mezquital <mltermlangOtomiMezquital>`                                      6       1849  99.7%
   :ref:`Fon <mltermlangFon>`                                                              8       2520  99.7%
   :ref:`Dangme <mltermlangDangme>`                                                        9       2912  99.7%
   :ref:`Magahi <mltermlangMagahi>`                                                        5       1716  99.7%
   :ref:`Bhojpuri <mltermlangBhojpuri>`                                                    5       1737  99.7%
   :ref:`Hindi <mltermlangHindi>`                                                          6       2128  99.7%
   :ref:`Panjabi, Eastern <mltermlangPanjabiEastern>`                                      6       2293  99.7%
   :ref:`Tibetan, Central <mltermlangTibetanCentral>`                                      8       3174  99.7%
   :ref:`Tai Dam <mltermlangTaiDam>`                                                       6       2386  99.7%
   :ref:`Dzongkha <mltermlangDzongkha>`                                                    7       3060  99.8%
   =============================================================================  ==========  =========  =============

.. _mltermlangMalayalam:

Malayalam
^^^^^^^^^

Sequence of language *Malayalam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0D32 <https://codepoints.net/U+0D32>`_  '\\u0d32'  Lo                  1  MALAYALAM LETTER LA
     2  `U+0D4B <https://codepoints.net/U+0D4B>`_  '\\u0d4b'  Mc                  0  MALAYALAM VOWEL SIGN OO
     3  `U+0D15 <https://codepoints.net/U+0D15>`_  '\\u0d15'  Lo                  1  MALAYALAM LETTER KA
     4  `U+0D24 <https://codepoints.net/U+0D24>`_  '\\u0d24'  Lo                  1  MALAYALAM LETTER TA
     5  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
     6  `U+0D24 <https://codepoints.net/U+0D24>`_  '\\u0d24'  Lo                  1  MALAYALAM LETTER TA
     7  `U+0D3F <https://codepoints.net/U+0D3F>`_  '\\u0d3f'  Mc                  0  MALAYALAM VOWEL SIGN I
     8  `U+0D32 <https://codepoints.net/U+0D32>`_  '\\u0d32'  Lo                  1  MALAYALAM LETTER LA
     9  `U+0D4D <https://codepoints.net/U+0D4D>`_  '\\u0d4d'  Mn                  0  MALAYALAM SIGN VIRAMA
    10  `U+200D <https://codepoints.net/U+200D>`_  '\\u200d'  Cf                  0  ZERO WIDTH JOINER
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb4\xb2\xe0\xb5\x8b\xe0\xb4\x95\xe0\xb4\xa4\xe0\xb5\x8d\xe0\xb4\xa4\xe0\xb4\xbf\xe0\xb4\xb2\xe0\xb5\x8d\xe2\x80\x8d|\\n12345|\\n"
        ലോകത്തില്‍|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

.. _mltermlangJavaneseJavanese:

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+A9A5 <https://codepoints.net/U+A9A5>`_  '\\ua9a5'  Lo                  1  JAVANESE LETTER PA
     2  `U+A9B1 <https://codepoints.net/U+A9B1>`_  '\\ua9b1'  Lo                  1  JAVANESE LETTER SA
     3  `U+A9AB <https://codepoints.net/U+A9AB>`_  '\\ua9ab'  Lo                  1  JAVANESE LETTER RA
     4  `U+A9BA <https://codepoints.net/U+A9BA>`_  '\\ua9ba'  Mc                  0  JAVANESE VOWEL SIGN TALING
     5  `U+A98F <https://codepoints.net/U+A98F>`_  '\\ua98f'  Lo                  1  JAVANESE LETTER KA
     6  `U+A9A0 <https://codepoints.net/U+A9A0>`_  '\\ua9a0'  Lo                  1  JAVANESE LETTER TA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\xa5\xea\xa6\xb1\xea\xa6\xab\xea\xa6\xba\xea\xa6\x8f\xea\xa6\xa0|\\n12345|\\n"
        ꦥꦱꦫꦺꦏꦠ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

.. _mltermlangMongolianHalhMongolian:

Mongolian, Halh (Mongolian)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Mongolian, Halh (Mongolian)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+1828 <https://codepoints.net/U+1828>`_  '\\u1828'  Lo                  1  MONGOLIAN LETTER NA
     2  `U+1821 <https://codepoints.net/U+1821>`_  '\\u1821'  Lo                  1  MONGOLIAN LETTER E
     3  `U+1837 <https://codepoints.net/U+1837>`_  '\\u1837'  Lo                  1  MONGOLIAN LETTER RA
     4  `U+180E <https://codepoints.net/U+180E>`_  '\\u180e'  Cf                  0  MONGOLIAN VOWEL SEPARATOR
     5  `U+1821 <https://codepoints.net/U+1821>`_  '\\u1821'  Lo                  1  MONGOLIAN LETTER E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa0\xa8\xe1\xa0\xa1\xe1\xa0\xb7\xe1\xa0\x8e\xe1\xa0\xa1|\\n1234|\\n"
        ᠨᠡᠷ᠎ᠡ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 5.

.. _mltermlangSinhala:

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
  while *mlterm* measures width 7.

.. _mltermlangBengali:

Bengali
^^^^^^^

Sequence of language *Bengali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ============================
     1  `U+09B8 <https://codepoints.net/U+09B8>`_  '\\u09b8'  Lo                  1  BENGALI LETTER SA
     2  `U+09CD <https://codepoints.net/U+09CD>`_  '\\u09cd'  Mn                  0  BENGALI SIGN VIRAMA
     3  `U+09AC <https://codepoints.net/U+09AC>`_  '\\u09ac'  Lo                  1  BENGALI LETTER BA
     4  `U+09C0 <https://codepoints.net/U+09C0>`_  '\\u09c0'  Mc                  0  BENGALI VOWEL SIGN II
     5  `U+0995 <https://codepoints.net/U+0995>`_  '\\u0995'  Lo                  1  BENGALI LETTER KA
     6  `U+09C3 <https://codepoints.net/U+09C3>`_  '\\u09c3'  Mn                  0  BENGALI VOWEL SIGN VOCALIC R
     7  `U+09A4 <https://codepoints.net/U+09A4>`_  '\\u09a4'  Lo                  1  BENGALI LETTER TA
     8  `U+09BF <https://codepoints.net/U+09BF>`_  '\\u09bf'  Mc                  0  BENGALI VOWEL SIGN I
     9  `U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
    10  `U+0987 <https://codepoints.net/U+0987>`_  '\\u0987'  Lo                  1  BENGALI LETTER I
   ===  =========================================  =========  ==========  =========  ============================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\xb8\xe0\xa7\x8d\xe0\xa6\xac\xe0\xa7\x80\xe0\xa6\x95\xe0\xa7\x83\xe0\xa6\xa4\xe0\xa6\xbf\xe2\x80\x8c\xe0\xa6\x87|\\n12345|\\n"
        স্বীকৃতি‌ই|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

.. _mltermlangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     2  `U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
     3  `U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
     4  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     5  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     6  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     7  `U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
     8  `U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
     9  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
    10  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88\xd8\xad\xd8\xb4\xdb\x8c\xd8\xa7\xd9\x86\xd9\x87\xe2\x80\x8c\xd8\xa7\xdb\x8c|\\n123456789|\\n"
        وحشیانه‌ای|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 10.

.. _mltermlangChineseMandarinGuiyang:

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

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
     7  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     8  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     9  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
    10  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    11  `U+8D4B <https://codepoints.net/U+8D4B>`_  '\\u8d4b'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D4B
    12  `U+4E88 <https://codepoints.net/U+4E88>`_  '\\u4e88'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E88
    13  `U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
    14  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    15  `U+57FA <https://codepoints.net/U+57FA>`_  '\\u57fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-57FA
    16  `U+672C <https://codepoints.net/U+672C>`_  '\\u672c'  Lo                  2  CJK UNIFIED IDEOGRAPH-672C
    17  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
    18  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    19  `U+906D <https://codepoints.net/U+906D>`_  '\\u906d'  Lo                  2  CJK UNIFIED IDEOGRAPH-906D
    20  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    21  `U+4FB5 <https://codepoints.net/U+4FB5>`_  '\\u4fb5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FB5
    22  `U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
    23  `U+65F6 <https://codepoints.net/U+65F6>`_  '\\u65f6'  Lo                  2  CJK UNIFIED IDEOGRAPH-65F6
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 23


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xbb\xe4\xbd\x95\xe4\xba\xba\xe5\xbd\x93\xe5\xae\xaa\xe6\xb3\x95\xe6\x88\x96\xe6\xb3\x95\xe5\xbe\x8b\xe6\x89\x80\xe8\xb5\x8b\xe4\xba\x88\xe4\xbb\x96\xe7\x9a\x84\xe5\x9f\xba\xe6\x9c\xac\xe6\x9d\x83\xe5\x88\xa9\xe9\x81\xad\xe5\x8f\x97\xe4\xbe\xb5\xe5\xae\xb3\xe6\x97\xb6|\\n1234567890123456789012345678901234567890123456|\\n"
        任何人当宪法或法律所赋予他的基本权利遭受侵害时|
        1234567890123456789012345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 46,
  while *mlterm* measures width 40.

.. _mltermlangChineseXiang:

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+968F <https://codepoints.net/U+968F>`_  '\\u968f'  Lo                  2  CJK UNIFIED IDEOGRAPH-968F
     2  `U+4E48 <https://codepoints.net/U+4E48>`_  '\\u4e48'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E48
     3  `U+5B50 <https://codepoints.net/U+5B50>`_  '\\u5b50'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B50
     4  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     5  `U+5F53 <https://codepoints.net/U+5F53>`_  '\\u5f53'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F53
     6  `U+5BAA <https://codepoints.net/U+5BAA>`_  '\\u5baa'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BAA
     7  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     8  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     9  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
    10  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
    11  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    12  `U+8D4B <https://codepoints.net/U+8D4B>`_  '\\u8d4b'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D4B
    13  `U+4E88 <https://codepoints.net/U+4E88>`_  '\\u4e88'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E88
    14  `U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
    15  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    16  `U+57FA <https://codepoints.net/U+57FA>`_  '\\u57fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-57FA
    17  `U+672C <https://codepoints.net/U+672C>`_  '\\u672c'  Lo                  2  CJK UNIFIED IDEOGRAPH-672C
    18  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
    19  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    20  `U+906D <https://codepoints.net/U+906D>`_  '\\u906d'  Lo                  2  CJK UNIFIED IDEOGRAPH-906D
    21  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    22  `U+4FB5 <https://codepoints.net/U+4FB5>`_  '\\u4fb5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FB5
    23  `U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
    24  `U+65F6 <https://codepoints.net/U+65F6>`_  '\\u65f6'  Lo                  2  CJK UNIFIED IDEOGRAPH-65F6
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe9\x9a\x8f\xe4\xb9\x88\xe5\xad\x90\xe4\xba\xba\xe5\xbd\x93\xe5\xae\xaa\xe6\xb3\x95\xe6\x88\x96\xe6\xb3\x95\xe5\xbe\x8b\xe6\x89\x80\xe8\xb5\x8b\xe4\xba\x88\xe4\xbb\x96\xe7\x9a\x84\xe5\x9f\xba\xe6\x9c\xac\xe6\x9d\x83\xe5\x88\xa9\xe9\x81\xad\xe5\x8f\x97\xe4\xbe\xb5\xe5\xae\xb3\xe6\x97\xb6|\\n123456789012345678901234567890123456789012345678|\\n"
        随么子人当宪法或法律所赋予他的基本权利遭受侵害时|
        123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 48,
  while *mlterm* measures width 41.

.. _mltermlangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     2  `U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
     3  `U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
     4  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     5  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     6  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     7  `U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
     8  `U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
     9  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
    10  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88\xd8\xad\xd8\xb4\xdb\x8c\xd8\xa7\xd9\x86\xd9\x87\xe2\x80\x8c\xdb\x8c\xdb\x8c|\\n123456789|\\n"
        وحشیانه‌یی|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 10.

.. _mltermlangJapaneseOsaka:

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+52A0 <https://codepoints.net/U+52A0>`_  '\\u52a0'  Lo                  2  CJK UNIFIED IDEOGRAPH-52A0
     2  `U+76DF <https://codepoints.net/U+76DF>`_  '\\u76df'  Lo                  2  CJK UNIFIED IDEOGRAPH-76DF
     3  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     4  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     5  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     6  `U+8F44 <https://codepoints.net/U+8F44>`_  '\\u8f44'  Lo                  2  CJK UNIFIED IDEOGRAPH-8F44
     7  `U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
     8  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
     9  `U+3042 <https://codepoints.net/U+3042>`_  '\\u3042'  Lo                  2  HIRAGANA LETTER A
    10  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
    11  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
    12  `U+57DF <https://codepoints.net/U+57DF>`_  '\\u57df'  Lo                  2  CJK UNIFIED IDEOGRAPH-57DF
    13  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
    14  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
    15  `U+6C11 <https://codepoints.net/U+6C11>`_  '\\u6c11'  Lo                  2  CJK UNIFIED IDEOGRAPH-6C11
    16  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
    17  `U+9593 <https://codepoints.net/U+9593>`_  '\\u9593'  Lo                  2  CJK UNIFIED IDEOGRAPH-9593
    18  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
    19  `U+3082 <https://codepoints.net/U+3082>`_  '\\u3082'  Lo                  2  HIRAGANA LETTER MO
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8a\xa0\xe7\x9b\x9f\xe5\x9b\xbd\xe3\x81\xae\xe7\xae\xa1\xe8\xbd\x84\xe4\xb8\x8b\xe3\x81\xab\xe3\x81\x82\xe3\x82\x8b\xe5\x9c\xb0\xe5\x9f\x9f\xe3\x81\xae\xe4\xba\xba\xe6\xb0\x91\xe3\x81\xae\xe9\x96\x93\xe3\x81\xab\xe3\x82\x82|\\n12345678901234567890123456789012345678|\\n"
        加盟国の管轄下にある地域の人民の間にも|
        12345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 38,
  while *mlterm* measures width 34.

.. _mltermlangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EA6 <https://codepoints.net/U+4EA6>`_  '\\u4ea6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EA6
     2  `U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
     3  `U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
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

        $ printf "\xe4\xba\xa6\xe4\xb8\x8d\xe5\xbe\x97\xe5\x90\xa6\xe8\xae\xa4\xe5\x85\xb6\xe6\x94\xb9\xe5\x8f\x98\xe5\x9b\xbd\xe7\xb1\x8d\xe7\x9a\x84\xe6\x9d\x83\xe5\x88\xa9|\\n12345678901234567890123456|\\n"
        亦不得否认其改变国籍的权利|
        12345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 26,
  while *mlterm* measures width 2.

.. _mltermlangChineseWu:

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+62D8 <https://codepoints.net/U+62D8>`_  '\\u62d8'  Lo                  2  CJK UNIFIED IDEOGRAPH-62D8
     2  `U+7981 <https://codepoints.net/U+7981>`_  '\\u7981'  Lo                  2  CJK UNIFIED IDEOGRAPH-7981
     3  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     4  `U+653E <https://codepoints.net/U+653E>`_  '\\u653e'  Lo                  2  CJK UNIFIED IDEOGRAPH-653E
     5  `U+9010 <https://codepoints.net/U+9010>`_  '\\u9010'  Lo                  2  CJK UNIFIED IDEOGRAPH-9010
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x8b\x98\xe7\xa6\x81\xe6\x88\x96\xe6\x94\xbe\xe9\x80\x90|\\n1234567890|\\n"
        拘禁或放逐|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *mlterm* measures width -12.

.. _mltermlangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

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
     7  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     8  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     9  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
    10  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    11  `U+8D4B <https://codepoints.net/U+8D4B>`_  '\\u8d4b'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D4B
    12  `U+4E88 <https://codepoints.net/U+4E88>`_  '\\u4e88'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E88
    13  `U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
    14  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    15  `U+57FA <https://codepoints.net/U+57FA>`_  '\\u57fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-57FA
    16  `U+672C <https://codepoints.net/U+672C>`_  '\\u672c'  Lo                  2  CJK UNIFIED IDEOGRAPH-672C
    17  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
    18  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    19  `U+906D <https://codepoints.net/U+906D>`_  '\\u906d'  Lo                  2  CJK UNIFIED IDEOGRAPH-906D
    20  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    21  `U+4FB5 <https://codepoints.net/U+4FB5>`_  '\\u4fb5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4FB5
    22  `U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
    23  `U+65F6 <https://codepoints.net/U+65F6>`_  '\\u65f6'  Lo                  2  CJK UNIFIED IDEOGRAPH-65F6
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 23


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xbb\xe4\xbd\x95\xe4\xba\xba\xe5\xbd\x93\xe5\xae\xaa\xe6\xb3\x95\xe6\x88\x96\xe6\xb3\x95\xe5\xbe\x8b\xe6\x89\x80\xe8\xb5\x8b\xe4\xba\x88\xe4\xbb\x96\xe7\x9a\x84\xe5\x9f\xba\xe6\x9c\xac\xe6\x9d\x83\xe5\x88\xa9\xe9\x81\xad\xe5\x8f\x97\xe4\xbe\xb5\xe5\xae\xb3\xe6\x97\xb6|\\n1234567890123456789012345678901234567890123456|\\n"
        任何人当宪法或法律所赋予他的基本权利遭受侵害时|
        1234567890123456789012345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 46,
  while *mlterm* measures width 40.

.. _mltermlangChineseMandarinTianjin:

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

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
     7  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     8  `U+6CD5 <https://codepoints.net/U+6CD5>`_  '\\u6cd5'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CD5
     9  `U+5F8B <https://codepoints.net/U+5F8B>`_  '\\u5f8b'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F8B
    10  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    11  `U+8D4B <https://codepoints.net/U+8D4B>`_  '\\u8d4b'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D4B
    12  `U+4E88 <https://codepoints.net/U+4E88>`_  '\\u4e88'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E88
    13  `U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
    14  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    15  `U+57FA <https://codepoints.net/U+57FA>`_  '\\u57fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-57FA
    16  `U+672C <https://codepoints.net/U+672C>`_  '\\u672c'  Lo                  2  CJK UNIFIED IDEOGRAPH-672C
    17  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
    18  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    19  `U+906D <https://codepoints.net/U+906D>`_  '\\u906d'  Lo                  2  CJK UNIFIED IDEOGRAPH-906D
    20  `U+7978 <https://codepoints.net/U+7978>`_  '\\u7978'  Lo                  2  CJK UNIFIED IDEOGRAPH-7978
    21  `U+7978 <https://codepoints.net/U+7978>`_  '\\u7978'  Lo                  2  CJK UNIFIED IDEOGRAPH-7978
    22  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    23  `U+5DE5 <https://codepoints.net/U+5DE5>`_  '\\u5de5'  Lo                  2  CJK UNIFIED IDEOGRAPH-5DE5
    24  `U+592B <https://codepoints.net/U+592B>`_  '\\u592b'  Lo                  2  CJK UNIFIED IDEOGRAPH-592B
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xbb\xe4\xbd\x95\xe4\xba\xba\xe5\xbd\x93\xe5\xae\xaa\xe6\xb3\x95\xe6\x88\x96\xe6\xb3\x95\xe5\xbe\x8b\xe6\x89\x80\xe8\xb5\x8b\xe4\xba\x88\xe4\xbb\x96\xe7\x9a\x84\xe5\x9f\xba\xe6\x9c\xac\xe6\x9d\x83\xe5\x88\xa9\xe9\x81\xad\xe7\xa5\xb8\xe7\xa5\xb8\xe7\x9a\x84\xe5\xb7\xa5\xe5\xa4\xab|\\n123456789012345678901234567890123456789012345678|\\n"
        任何人当宪法或法律所赋予他的基本权利遭祸祸的工夫|
        123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 48,
  while *mlterm* measures width 41.

.. _mltermlangThai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
     2  `U+0E0F <https://codepoints.net/U+0E0F>`_  '\\u0e0f'  Lo                  1  THAI CHARACTER TO PATAK
     3  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
     4  `U+0E0D <https://codepoints.net/U+0E0D>`_  '\\u0e0d'  Lo                  1  THAI CHARACTER YO YING
     5  `U+0E0D <https://codepoints.net/U+0E0D>`_  '\\u0e0d'  Lo                  1  THAI CHARACTER YO YING
     6  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     7  `U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
     8  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     9  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    10  `U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
    11  `U+0E27 <https://codepoints.net/U+0E27>`_  '\\u0e27'  Lo                  1  THAI CHARACTER WO WAEN
    12  `U+0E48 <https://codepoints.net/U+0E48>`_  '\\u0e48'  Mn                  0  THAI CHARACTER MAI EK
    13  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    14  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
    15  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
    16  `U+0E27 <https://codepoints.net/U+0E27>`_  '\\u0e27'  Lo                  1  THAI CHARACTER WO WAEN
    17  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
    18  `U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
    19  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    20  `U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
    21  `U+0E18 <https://codepoints.net/U+0E18>`_  '\\u0e18'  Lo                  1  THAI CHARACTER THO THONG
    22  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    23  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
    24  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    25  `U+0E38 <https://codepoints.net/U+0E38>`_  '\\u0e38'  Mn                  0  THAI CHARACTER SARA U
    26  `U+0E29 <https://codepoints.net/U+0E29>`_  '\\u0e29'  Lo                  1  THAI CHARACTER SO RUSI
    27  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
    28  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
    29  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    30  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    31  `U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
    32  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 32


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xa5\xe0\xb8\xa7\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\xa1\xe0\xb8\x99\xe0\xb8\xb8\xe0\xb8\xa9\xe0\xb8\xa2\xe0\xb8\x8a\xe0\xb8\x99\xe0\xb8\x99\xe0\xb8\xb5\xe0\xb9\x89|\\n123456789012345678901234|\\n"
        ปฏิญญาสากลว่าด้วยสิทธิมนุษยชนนี้|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *mlterm* measures width 8.

.. _mltermlangJapanese:

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+52A0 <https://codepoints.net/U+52A0>`_  '\\u52a0'  Lo                  2  CJK UNIFIED IDEOGRAPH-52A0
     2  `U+76DF <https://codepoints.net/U+76DF>`_  '\\u76df'  Lo                  2  CJK UNIFIED IDEOGRAPH-76DF
     3  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     4  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     5  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     6  `U+8F44 <https://codepoints.net/U+8F44>`_  '\\u8f44'  Lo                  2  CJK UNIFIED IDEOGRAPH-8F44
     7  `U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
     8  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
     9  `U+3042 <https://codepoints.net/U+3042>`_  '\\u3042'  Lo                  2  HIRAGANA LETTER A
    10  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
    11  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
    12  `U+57DF <https://codepoints.net/U+57DF>`_  '\\u57df'  Lo                  2  CJK UNIFIED IDEOGRAPH-57DF
    13  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
    14  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
    15  `U+6C11 <https://codepoints.net/U+6C11>`_  '\\u6c11'  Lo                  2  CJK UNIFIED IDEOGRAPH-6C11
    16  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
    17  `U+9593 <https://codepoints.net/U+9593>`_  '\\u9593'  Lo                  2  CJK UNIFIED IDEOGRAPH-9593
    18  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
    19  `U+3082 <https://codepoints.net/U+3082>`_  '\\u3082'  Lo                  2  HIRAGANA LETTER MO
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8a\xa0\xe7\x9b\x9f\xe5\x9b\xbd\xe3\x81\xae\xe7\xae\xa1\xe8\xbd\x84\xe4\xb8\x8b\xe3\x81\xab\xe3\x81\x82\xe3\x82\x8b\xe5\x9c\xb0\xe5\x9f\x9f\xe3\x81\xae\xe4\xba\xba\xe6\xb0\x91\xe3\x81\xae\xe9\x96\x93\xe3\x81\xab\xe3\x82\x82|\\n12345678901234567890123456789012345678|\\n"
        加盟国の管轄下にある地域の人民の間にも|
        12345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 38,
  while *mlterm* measures width 34.

.. _mltermlangThai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0E42 <https://codepoints.net/U+0E42>`_  '\\u0e42'  Lo                  1  THAI CHARACTER SARA O
     2  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
     3  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
     4  `U+0E04 <https://codepoints.net/U+0E04>`_  '\\u0e04'  Lo                  1  THAI CHARACTER KHO KHWAI
     5  `U+0E27 <https://codepoints.net/U+0E27>`_  '\\u0e27'  Lo                  1  THAI CHARACTER WO WAEN
     6  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     7  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
     8  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     9  `U+0E48 <https://codepoints.net/U+0E48>`_  '\\u0e48'  Mn                  0  THAI CHARACTER MAI EK
    10  `U+0E27 <https://codepoints.net/U+0E27>`_  '\\u0e27'  Lo                  1  THAI CHARACTER WO WAEN
    11  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
    12  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
    13  `U+0E37 <https://codepoints.net/U+0E37>`_  '\\u0e37'  Mn                  0  THAI CHARACTER SARA UEE
    14  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
    15  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    16  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    17  `U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
    18  `U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
    19  `U+0E2B <https://codepoints.net/U+0E2B>`_  '\\u0e2b'  Lo                  1  THAI CHARACTER HO HIP
    20  `U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
    21  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    22  `U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
    23  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
    24  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    25  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
    26  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    27  `U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
    28  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 28


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x82\xe0\xb8\x94\xe0\xb8\xa2\xe0\xb8\x84\xe0\xb8\xa7\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\xa3\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\xa1\xe0\xb8\xa1\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb8\x81\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\xaa\xe0\xb8\xab\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x95\xe0\xb8\xb4|\\n123456789012345678901234|\\n"
        โดยความร่วมมือกับสหประชาชาติ|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *mlterm* measures width 0.

.. _mltermlangJapaneseTokyo:

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
     4  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     5  `U+7BA1 <https://codepoints.net/U+7BA1>`_  '\\u7ba1'  Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     6  `U+8F44 <https://codepoints.net/U+8F44>`_  '\\u8f44'  Lo                  2  CJK UNIFIED IDEOGRAPH-8F44
     7  `U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
     8  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
     9  `U+3042 <https://codepoints.net/U+3042>`_  '\\u3042'  Lo                  2  HIRAGANA LETTER A
    10  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
    11  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
    12  `U+57DF <https://codepoints.net/U+57DF>`_  '\\u57df'  Lo                  2  CJK UNIFIED IDEOGRAPH-57DF
    13  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
    14  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
    15  `U+6C11 <https://codepoints.net/U+6C11>`_  '\\u6c11'  Lo                  2  CJK UNIFIED IDEOGRAPH-6C11
    16  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
    17  `U+9593 <https://codepoints.net/U+9593>`_  '\\u9593'  Lo                  2  CJK UNIFIED IDEOGRAPH-9593
    18  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
    19  `U+3082 <https://codepoints.net/U+3082>`_  '\\u3082'  Lo                  2  HIRAGANA LETTER MO
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8a\xa0\xe7\x9b\x9f\xe5\x9b\xbd\xe3\x81\xae\xe7\xae\xa1\xe8\xbd\x84\xe4\xb8\x8b\xe3\x81\xab\xe3\x81\x82\xe3\x82\x8b\xe5\x9c\xb0\xe5\x9f\x9f\xe3\x81\xae\xe4\xba\xba\xe6\xb0\x91\xe3\x81\xae\xe9\x96\x93\xe3\x81\xab\xe3\x82\x82|\\n12345678901234567890123456789012345678|\\n"
        加盟国の管轄下にある地域の人民の間にも|
        12345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 38,
  while *mlterm* measures width 34.

.. _mltermlangChineseMandarinTraditional:

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+5341 <https://codepoints.net/U+5341>`_  '\\u5341'  Lo                  2  CJK UNIFIED IDEOGRAPH-5341
     3  `U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
     4  `U+689D <https://codepoints.net/U+689D>`_  '\\u689d'  Lo                  2  CJK UNIFIED IDEOGRAPH-689D
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x80\xe6\xa2\x9d|\\n12345678|\\n"
        第十一條|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width -40.

.. _mltermlangChineseMandarinSimplified:

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E03 <https://codepoints.net/U+4E03>`_  '\\u4e03'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E03
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb8\x83\xe6\x9d\xa1|\\n123456|\\n"
        第七条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -32.

.. _mltermlangLao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0EC1 <https://codepoints.net/U+0EC1>`_  '\\u0ec1'  Lo                  1  LAO VOWEL SIGN EI
     2  `U+0EA5 <https://codepoints.net/U+0EA5>`_  '\\u0ea5'  Lo                  1  LAO LETTER LO LOOT
     3  `U+0EB0 <https://codepoints.net/U+0EB0>`_  '\\u0eb0'  Lo                  1  LAO VOWEL SIGN A
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbb\x81\xe0\xba\xa5\xe0\xba\xb0|\\n123|\\n"
        ແລະ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -6.

.. _mltermlangKhmerCentral:

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+1787 <https://codepoints.net/U+1787>`_  '\\u1787'  Lo                  1  KHMER LETTER CO
     2  `U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
     3  `U+17A7 <https://codepoints.net/U+17A7>`_  '\\u17a7'  Lo                  1  KHMER INDEPENDENT VOWEL QU
     4  `U+178F <https://codepoints.net/U+178F>`_  '\\u178f'  Lo                  1  KHMER LETTER TA
     5  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
     6  `U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
     7  `U+1798 <https://codepoints.net/U+1798>`_  '\\u1798'  Lo                  1  KHMER LETTER MO
     8  `U+1782 <https://codepoints.net/U+1782>`_  '\\u1782'  Lo                  1  KHMER LETTER KO
     9  `U+178F <https://codepoints.net/U+178F>`_  '\\u178f'  Lo                  1  KHMER LETTER TA
    10  `U+17B7 <https://codepoints.net/U+17B7>`_  '\\u17b7'  Mn                  0  KHMER VOWEL SIGN I
    11  `U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
    12  `U+17BD <https://codepoints.net/U+17BD>`_  '\\u17bd'  Mn                  0  KHMER VOWEL SIGN UA
    13  `U+1798 <https://codepoints.net/U+1798>`_  '\\u1798'  Lo                  1  KHMER LETTER MO
    14  `U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
    15  `U+17C2 <https://codepoints.net/U+17C2>`_  '\\u17c2'  Mc                  0  KHMER VOWEL SIGN AE
    16  `U+179B <https://codepoints.net/U+179B>`_  '\\u179b'  Lo                  1  KHMER LETTER LO
    17  `U+1794 <https://codepoints.net/U+1794>`_  '\\u1794'  Lo                  1  KHMER LETTER BA
    18  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
    19  `U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
    20  `U+1787 <https://codepoints.net/U+1787>`_  '\\u1787'  Lo                  1  KHMER LETTER CO
    21  `U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
    22  `U+1796 <https://codepoints.net/U+1796>`_  '\\u1796'  Lo                  1  KHMER LETTER PO
    23  `U+179B <https://codepoints.net/U+179B>`_  '\\u179b'  Lo                  1  KHMER LETTER LO
    24  `U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
    25  `U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
    26  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
    27  `U+178B <https://codepoints.net/U+178B>`_  '\\u178b'  Lo                  1  KHMER LETTER TTHA
    28  `U+1782 <https://codepoints.net/U+1782>`_  '\\u1782'  Lo                  1  KHMER LETTER KO
    29  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
    30  `U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
    31  `U+1794 <https://codepoints.net/U+1794>`_  '\\u1794'  Lo                  1  KHMER LETTER BA
    32  `U+17CB <https://codepoints.net/U+17CB>`_  '\\u17cb'  Mn                  0  KHMER SIGN BANTOC
    33  `U+17D7 <https://codepoints.net/U+17D7>`_  '\\u17d7'  Lm                  1  KHMER SIGN LEK TOO
    34  `U+1794 <https://codepoints.net/U+1794>`_  '\\u1794'  Lo                  1  KHMER LETTER BA
    35  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
    36  `U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
    37  `U+1791 <https://codepoints.net/U+1791>`_  '\\u1791'  Lo                  1  KHMER LETTER TO
    38  `U+17C1 <https://codepoints.net/U+17C1>`_  '\\u17c1'  Mc                  0  KHMER VOWEL SIGN E
    39  `U+179F <https://codepoints.net/U+179F>`_  '\\u179f'  Lo                  1  KHMER LETTER SA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 39


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\xa7\xe1\x9e\x8f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\x98\xe1\x9e\x82\xe1\x9e\x8f\xe1\x9e\xb7\xe1\x9e\x9a\xe1\x9e\xbd\xe1\x9e\x98\xe1\x9e\x8a\xe1\x9f\x82\xe1\x9e\x9b\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x87\xe1\x9e\xb6\xe1\x9e\x96\xe1\x9e\x9b\xe1\x9e\x9a\xe1\x9e\x8a\xe1\x9f\x92\xe1\x9e\x8b\xe1\x9e\x82\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x94\xe1\x9f\x8b\xe1\x9f\x97\xe1\x9e\x94\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\x91\xe1\x9f\x81\xe1\x9e\x9f|\\n123456789012345678901234567|\\n"
        ជាឧត្ដមគតិរួមដែលប្រជាពលរដ្ឋគ្រប់ៗប្រទេស|
        123456789012345678901234567|

- python `wcwidth.wcswidth()`_ measures width 27,
  while *mlterm* measures width 4.

.. _mltermlangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+689D <https://codepoints.net/U+689D>`_  '\\u689d'  Lo                  2  CJK UNIFIED IDEOGRAPH-689D
     2  `U+0031 <https://codepoints.net/U+0031>`_  '1'        Nd                  1  DIGIT ONE
     3  `U+0036 <https://codepoints.net/U+0036>`_  '6'        Nd                  1  DIGIT SIX
     4  `U+FF1A <https://codepoints.net/U+FF1A>`_  '\\uff1a'  Po                  2  FULLWIDTH COLON
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xa2\x9d16\xef\xbc\x9a|\\n123456|\\n"
        條16：|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -40.

.. _mltermlangChineseYue:

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E5D <https://codepoints.net/U+4E5D>`_  '\\u4e5d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5D
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb9\x9d\xe6\x9d\xa1|\\n123456|\\n"
        第九条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -40.

.. _mltermlangJinan:

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E5D <https://codepoints.net/U+4E5D>`_  '\\u4e5d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5D
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb9\x9d\xe6\x9d\xa1|\\n123456|\\n"
        第九条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -40.

.. _mltermlangChineseGan:

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+62D8 <https://codepoints.net/U+62D8>`_  '\\u62d8'  Lo                  2  CJK UNIFIED IDEOGRAPH-62D8
     2  `U+7981 <https://codepoints.net/U+7981>`_  '\\u7981'  Lo                  2  CJK UNIFIED IDEOGRAPH-7981
     3  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     4  `U+653E <https://codepoints.net/U+653E>`_  '\\u653e'  Lo                  2  CJK UNIFIED IDEOGRAPH-653E
     5  `U+9010 <https://codepoints.net/U+9010>`_  '\\u9010'  Lo                  2  CJK UNIFIED IDEOGRAPH-9010
     6  `U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
     7  `U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x8b\x98\xe7\xa6\x81\xe6\x88\x96\xe6\x94\xbe\xe9\x80\x90\xe4\xb8\x8d\xe5\xbe\x97|\\n12345678901234|\\n"
        拘禁或放逐不得|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *mlterm* measures width 0.

.. _mltermlangChineseHakka:

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5173 <https://codepoints.net/U+5173>`_  '\\u5173'  Lo                  2  CJK UNIFIED IDEOGRAPH-5173
     2  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     3  `U+653E <https://codepoints.net/U+653E>`_  '\\u653e'  Lo                  2  CJK UNIFIED IDEOGRAPH-653E
     4  `U+9010 <https://codepoints.net/U+9010>`_  '\\u9010'  Lo                  2  CJK UNIFIED IDEOGRAPH-9010
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\xb3\xe6\x88\x96\xe6\x94\xbe\xe9\x80\x90|\\n12345678|\\n"
        关或放逐|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width -10.

.. _mltermlangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5173 <https://codepoints.net/U+5173>`_  '\\u5173'  Lo                  2  CJK UNIFIED IDEOGRAPH-5173
     2  `U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
     3  `U+6765 <https://codepoints.net/U+6765>`_  '\\u6765'  Lo                  2  CJK UNIFIED IDEOGRAPH-6765
     4  `U+54A7 <https://codepoints.net/U+54A7>`_  '\\u54a7'  Lo                  2  CJK UNIFIED IDEOGRAPH-54A7
     5  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     6  `U+8F70 <https://codepoints.net/U+8F70>`_  '\\u8f70'  Lo                  2  CJK UNIFIED IDEOGRAPH-8F70
     7  `U+51FA <https://codepoints.net/U+51FA>`_  '\\u51fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FA
     8  `U+53BB <https://codepoints.net/U+53BB>`_  '\\u53bb'  Lo                  2  CJK UNIFIED IDEOGRAPH-53BB
     9  `U+54A7 <https://codepoints.net/U+54A7>`_  '\\u54a7'  Lo                  2  CJK UNIFIED IDEOGRAPH-54A7
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\xb3\xe8\xb5\xb7\xe6\x9d\xa5\xe5\x92\xa7\xe6\x88\x96\xe8\xbd\xb0\xe5\x87\xba\xe5\x8e\xbb\xe5\x92\xa7|\\n123456789012345678|\\n"
        关起来咧或轰出去咧|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *mlterm* measures width -2.

.. _mltermlangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E5D <https://codepoints.net/U+4E5D>`_  '\\u4e5d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5D
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb9\x9d\xe6\x9d\xa1|\\n123456|\\n"
        第九条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -40.

.. _mltermlangChineseMinNan:

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+62D8 <https://codepoints.net/U+62D8>`_  '\\u62d8'  Lo                  2  CJK UNIFIED IDEOGRAPH-62D8
     2  `U+7981 <https://codepoints.net/U+7981>`_  '\\u7981'  Lo                  2  CJK UNIFIED IDEOGRAPH-7981
     3  `U+6291 <https://codepoints.net/U+6291>`_  '\\u6291'  Lo                  2  CJK UNIFIED IDEOGRAPH-6291
     4  `U+653E <https://codepoints.net/U+653E>`_  '\\u653e'  Lo                  2  CJK UNIFIED IDEOGRAPH-653E
     5  `U+9010 <https://codepoints.net/U+9010>`_  '\\u9010'  Lo                  2  CJK UNIFIED IDEOGRAPH-9010
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x8b\x98\xe7\xa6\x81\xe6\x8a\x91\xe6\x94\xbe\xe9\x80\x90|\\n1234567890|\\n"
        拘禁抑放逐|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *mlterm* measures width -12.

.. _mltermlangMarathi:

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+091C <https://codepoints.net/U+091C>`_  '\\u091c'  Lo                  1  DEVANAGARI LETTER JA
     2  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     3  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     4  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     5  `U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
     6  `U+0905 <https://codepoints.net/U+0905>`_  '\\u0905'  Lo                  1  DEVANAGARI LETTER A
     7  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
     8  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     9  `U+0925 <https://codepoints.net/U+0925>`_  '\\u0925'  Lo                  1  DEVANAGARI LETTER THA
    10  `U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x9c\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe\xe2\x80\x8c\xe0\xa4\x85\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xa5\xe0\xa5\x80|\\n12345|\\n"
        ज्या‌अर्थी|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

.. _mltermlangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     5  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     7  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xcc\x83anaret|\\n123456|\\n"
        ̃anaret|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width 7.

.. _mltermlangKhn:

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+1A2F <https://codepoints.net/U+1A2F>`_  '\\u1a2f'  Lo                  1  TAI THAM LETTER DA
     2  `U+1A70 <https://codepoints.net/U+1A70>`_  '\\u1a70'  Mc                  0  TAI THAM VOWEL SIGN OO
     3  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
     4  `U+1A3F <https://codepoints.net/U+1A3F>`_  '\\u1a3f'  Lo                  1  TAI THAM LETTER LOW YA
     5  `U+1A37 <https://codepoints.net/U+1A37>`_  '\\u1a37'  Lo                  1  TAI THAM LETTER BA
     6  `U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
     7  `U+1A2F <https://codepoints.net/U+1A2F>`_  '\\u1a2f'  Lo                  1  TAI THAM LETTER DA
     8  `U+1A71 <https://codepoints.net/U+1A71>`_  '\\u1a71'  Mc                  0  TAI THAM VOWEL SIGN AI
     9  `U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
    10  `U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
    11  `U+1A6F <https://codepoints.net/U+1A6F>`_  '\\u1a6f'  Mc                  0  TAI THAM VOWEL SIGN AE
    12  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    13  `U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
    14  `U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
    15  `U+1A75 <https://codepoints.net/U+1A75>`_  '\\u1a75'  Mn                  0  TAI THAM SIGN TONE-1
    16  `U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
    17  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    18  `U+1A26 <https://codepoints.net/U+1A26>`_  '\\u1a26'  Lo                  1  TAI THAM LETTER NGA
    19  `U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
    20  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    21  `U+1A36 <https://codepoints.net/U+1A36>`_  '\\u1a36'  Lo                  1  TAI THAM LETTER NA
    22  `U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 22


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xaf\xe1\xa9\xb0\xe1\xa9\xa0\xe1\xa8\xbf\xe1\xa8\xb7\xe1\xa9\xa2\xe1\xa8\xaf\xe1\xa9\xb1\xe1\xa9\xa2\xe1\xa8\xb2\xe1\xa9\xaf\xe1\xa9\xa0\xe1\xa8\xa0\xe1\xa8\xb2\xe1\xa9\xb5\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xa6\xe1\xa8\xa0\xe1\xa9\xa0\xe1\xa8\xb6\xe1\xa9\xa2|\\n1234567890|\\n"
        ᨯᩰ᩠ᨿᨷᩢᨯᩱᩢᨲᩯ᩠ᨠᨲ᩵ᩣ᩠ᨦᨠ᩠ᨶᩢ|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *mlterm* measures width -5.

.. _mltermlangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     8  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nannakat|\\n12345678|\\n"
        nannakat|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width -17.

.. _mltermlangNuosu:

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================
     1  `U+A2BF <https://codepoints.net/U+A2BF>`_  '\\ua2bf'  Lo                  2  YI SYLLABLE CO
     2  `U+A0C5 <https://codepoints.net/U+A0C5>`_  '\\ua0c5'  Lo                  2  YI SYLLABLE MU
     3  `U+A1EB <https://codepoints.net/U+A1EB>`_  '\\ua1eb'  Lo                  2  YI SYLLABLE GOX
     4  `U+A25C <https://codepoints.net/U+A25C>`_  '\\ua25c'  Lo                  2  YI SYLLABLE HXEP
     5  `U+A138 <https://codepoints.net/U+A138>`_  '\\ua138'  Lo                  2  YI SYLLABLE DDI
     6  `U+A00A <https://codepoints.net/U+A00A>`_  '\\ua00a'  Lo                  2  YI SYLLABLE A
     7  `U+A246 <https://codepoints.net/U+A246>`_  '\\ua246'  Lo                  2  YI SYLLABLE HXIT
   ===  =========================================  =========  ==========  =========  ================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x8a\xbf\xea\x83\x85\xea\x87\xab\xea\x89\x9c\xea\x84\xb8\xea\x80\x8a\xea\x89\x86|\\n12345678901234|\\n"
        ꊿꃅꇫꉜꄸꀊꉆ|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *mlterm* measures width -24.

.. _mltermlangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     2  `U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'    Ll                  1  LATIN SMALL LETTER O WITH ACUTE
     3  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     6  `U+0268 <https://codepoints.net/U+0268>`_  '\\u0268'  Ll                  1  LATIN SMALL LETTER I WITH STROKE
     7  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "h\xc3\xb3jts\xc9\xa8\xcc\x81|\\n123456|\\n"
        hójtsɨ́|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -1.

.. _mltermlangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     2  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
     3  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     4  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     5  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
     6  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     7  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     8  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb4\xd0\xbe\xd1\x80\xd1\x80\xd0\xbe\xcc\x84\xd0\xbd\xd0\xb8|\\n1234567|\\n"
        дорро̄ни|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *mlterm* measures width 3.

.. _mltermlangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     2  `U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     5  `U+003B <https://codepoints.net/U+003B>`_  ';'       Po                  1  SEMICOLON
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "iqui;|\\n12345|\\n"
        iqui;|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -5.

.. _mltermlangGumuz:

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
  while *mlterm* measures width -6.

.. _mltermlangVeps:

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===================================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===================================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     2  `U+00E4 <https://codepoints.net/U+00E4>`_  '\\xe4'   Ll                  1  LATIN SMALL LETTER A WITH DIAERESIS
     3  `U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     5  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     6  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     7  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     9  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
    10  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
    11  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ===================================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "p\xc3\xa4valdoiden|\\n12345678901|\\n"
        pävaldoiden|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *mlterm* measures width 9.

.. _mltermlangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     2  `U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
     3  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     4  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     5  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb4\xd1\x8f\xd1\x80\xd0\xb8\xd0\xbd|\\n12345|\\n"
        дярин|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -1.

.. _mltermlangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0433 <https://codepoints.net/U+0433>`_  '\\u0433'  Ll                  1  CYRILLIC SMALL LETTER GHE
     2  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     3  `U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
     4  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     5  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
     6  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     7  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     8  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     9  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
    10  `U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
    11  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb3\xd1\x8d\xd0\xb1\xd1\x83\xd0\xbb\xd1\x8d\xd1\x83\xd1\x80\xd0\xb8\xd0\xb2\xd1\x8d|\\n12345678901|\\n"
        гэбулэуривэ|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *mlterm* measures width -3.

.. _mltermlangShan:

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+1075 <https://codepoints.net/U+1075>`_  '\\u1075'  Lo                  1  MYANMAR LETTER SHAN KA
     2  `U+1030 <https://codepoints.net/U+1030>`_  '\\u1030'  Mn                  0  MYANMAR VOWEL SIGN UU
     3  `U+107C <https://codepoints.net/U+107C>`_  '\\u107c'  Lo                  1  MYANMAR LETTER SHAN NA
     4  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
     5  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
     6  `U+1019 <https://codepoints.net/U+1019>`_  '\\u1019'  Lo                  1  MYANMAR LETTER MA
     7  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
     8  `U+1030 <https://codepoints.net/U+1030>`_  '\\u1030'  Mn                  0  MYANMAR VOWEL SIGN UU
     9  `U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
    10  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    11  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
    12  `U+1078 <https://codepoints.net/U+1078>`_  '\\u1078'  Lo                  1  MYANMAR LETTER SHAN CA
    13  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
    14  `U+1030 <https://codepoints.net/U+1030>`_  '\\u1030'  Mn                  0  MYANMAR VOWEL SIGN UU
    15  `U+101D <https://codepoints.net/U+101D>`_  '\\u101d'  Lo                  1  MYANMAR LETTER WA
    16  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    17  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
    18  `U+101A <https://codepoints.net/U+101A>`_  '\\u101a'  Lo                  1  MYANMAR LETTER YA
    19  `U+1030 <https://codepoints.net/U+1030>`_  '\\u1030'  Mn                  0  MYANMAR VOWEL SIGN UU
    20  `U+1087 <https://codepoints.net/U+1087>`_  '\\u1087'  Mc                  0  MYANMAR SIGN SHAN TONE-2
    21  `U+101E <https://codepoints.net/U+101E>`_  '\\u101e'  Lo                  1  MYANMAR LETTER SA
    22  `U+101D <https://codepoints.net/U+101D>`_  '\\u101d'  Lo                  1  MYANMAR LETTER WA
    23  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    24  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x81\xb5\xe1\x80\xb0\xe1\x81\xbc\xe1\x80\xba\xe1\x80\xb8\xe1\x80\x99\xe1\x80\xad\xe1\x80\xb0\xe1\x80\x84\xe1\x80\xba\xe1\x80\xb8\xe1\x81\xb8\xe1\x80\xad\xe1\x80\xb0\xe1\x80\x9d\xe1\x80\xba\xe1\x80\xb8\xe1\x80\x9a\xe1\x80\xb0\xe1\x82\x87\xe1\x80\x9e\xe1\x80\x9d\xe1\x80\xba\xe1\x80\xb8|\\n123456789|\\n"
        ၵူၼ်းမိူင်းၸိူဝ်းယူႇသဝ်း|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 8.

.. _mltermlangKannada:

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0CB5 <https://codepoints.net/U+0CB5>`_  '\\u0cb5'  Lo                  1  KANNADA LETTER VA
     2  `U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
     3  `U+0C95 <https://codepoints.net/U+0C95>`_  '\\u0c95'  Lo                  1  KANNADA LETTER KA
     4  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
     5  `U+200C <https://codepoints.net/U+200C>`_  '\\u200c'  Cf                  0  ZERO WIDTH NON-JOINER
     6  `U+0CB8 <https://codepoints.net/U+0CB8>`_  '\\u0cb8'  Lo                  1  KANNADA LETTER SA
     7  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
     8  `U+0CB5 <https://codepoints.net/U+0CB5>`_  '\\u0cb5'  Lo                  1  KANNADA LETTER VA
     9  `U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
    10  `U+0CA4 <https://codepoints.net/U+0CA4>`_  '\\u0ca4'  Lo                  1  KANNADA LETTER TA
    11  `U+0C82 <https://codepoints.net/U+0C82>`_  '\\u0c82'  Mc                  0  KANNADA SIGN ANUSVARA
    12  `U+0CA4 <https://codepoints.net/U+0CA4>`_  '\\u0ca4'  Lo                  1  KANNADA LETTER TA
    13  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
    14  `U+0CB0 <https://codepoints.net/U+0CB0>`_  '\\u0cb0'  Lo                  1  KANNADA LETTER RA
    15  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
    16  `U+0CAF <https://codepoints.net/U+0CAF>`_  '\\u0caf'  Lo                  1  KANNADA LETTER YA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\xb5\xe0\xb2\xbe\xe0\xb2\x95\xe0\xb3\x8d\xe2\x80\x8c\xe0\xb2\xb8\xe0\xb3\x8d\xe0\xb2\xb5\xe0\xb2\xbe\xe0\xb2\xa4\xe0\xb2\x82\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xb0\xe0\xb3\x8d\xe0\xb2\xaf|\\n12345678|\\n"
        ವಾಕ್‌ಸ್ವಾತಂತ್ರ್ಯ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width 9.

.. _mltermlangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     2  `U+0327 <https://codepoints.net/U+0327>`_  '\\u0327'  Mn                  0  COMBINING CEDILLA
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "c\xcc\xa7are|\\n1234|\\n"
        çare|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 0.

.. _mltermlangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     2  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     3  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     4  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     5  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     7  `U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     9  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ashdla\xca\xbcii|\\n123456789|\\n"
        ashdlaʼii|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 4.

.. _mltermlangAmarakaeri:

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     6  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     7  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "aratbut|\\n1234567|\\n"
        aratbut|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *mlterm* measures width 1.

.. _mltermlangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===================================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===================================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     5  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
   ===  =========================================  ========  ==========  =========  ===================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "saiy\xc3\xab|\\n12345|\\n"
        saiyë|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -2.

.. _mltermlangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======
     1  `U+2013 <https://codepoints.net/U+2013>`_  '\\u2013'  Pd                  1  EN DASH
   ===  =========================================  =========  ==========  =========  =======

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe2\x80\x93|\\n1|\\n"
        –|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -4.

.. _mltermlangKorean:

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+C810 <https://codepoints.net/U+C810>`_  '\\uc810'  Lo                  2  HANGUL SYLLABLE JEOM
     2  `U+C9C4 <https://codepoints.net/U+C9C4>`_  '\\uc9c4'  Lo                  2  HANGUL SYLLABLE JIN
     3  `U+C801 <https://codepoints.net/U+C801>`_  '\\uc801'  Lo                  2  HANGUL SYLLABLE JEOG
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\xa0\x90\xec\xa7\x84\xec\xa0\x81|\\n123456|\\n"
        점진적|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -2.

.. _mltermlangNepali:

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
  while *mlterm* measures width 7.

.. _mltermlangBurmese:

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
     2  `U+1030 <https://codepoints.net/U+1030>`_  '\\u1030'  Mn                  0  MYANMAR VOWEL SIGN UU
     3  `U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
     4  `U+1001 <https://codepoints.net/U+1001>`_  '\\u1001'  Lo                  1  MYANMAR LETTER KHA
     5  `U+103D <https://codepoints.net/U+103D>`_  '\\u103d'  Mn                  0  MYANMAR CONSONANT SIGN MEDIAL WA
     6  `U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
     7  `U+1037 <https://codepoints.net/U+1037>`_  '\\u1037'  Mn                  0  MYANMAR SIGN DOT BELOW
     8  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
     9  `U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
    10  `U+101B <https://codepoints.net/U+101B>`_  '\\u101b'  Lo                  1  MYANMAR LETTER RA
    11  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
    12  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
    13  `U+1019 <https://codepoints.net/U+1019>`_  '\\u1019'  Lo                  1  MYANMAR LETTER MA
    14  `U+103B <https://codepoints.net/U+103B>`_  '\\u103b'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL YA
    15  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
    16  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
    17  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
    18  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
    19  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
    20  `U+101C <https://codepoints.net/U+101C>`_  '\\u101c'  Lo                  1  MYANMAR LETTER LA
    21  `U+100A <https://codepoints.net/U+100A>`_  '\\u100a'  Lo                  1  MYANMAR LETTER NNYA
    22  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    23  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
    24  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
    25  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
    26  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
    27  `U+1004 <https://codepoints.net/U+1004>`_  '\\u1004'  Lo                  1  MYANMAR LETTER NGA
    28  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    29  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
    30  `U+104A <https://codepoints.net/U+104A>`_  '\\u104a'  Po                  1  MYANMAR SIGN LITTLE SECTION
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 30


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x9c\xe1\x80\xb0\xe1\x80\xa1\xe1\x80\x81\xe1\x80\xbd\xe1\x80\x84\xe1\x80\xb7\xe1\x80\xba\xe1\x80\xa1\xe1\x80\x9b\xe1\x80\xb1\xe1\x80\xb8\xe1\x80\x99\xe1\x80\xbb\xe1\x80\xac\xe1\x80\xb8\xe1\x80\x80\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x9c\xe1\x80\x8a\xe1\x80\xba\xe1\x80\xb8\xe1\x80\x80\xe1\x80\xb1\xe1\x80\xac\xe1\x80\x84\xe1\x80\xba\xe1\x80\xb8\xe1\x81\x8a|\\n1234567890123|\\n"
        လူအခွင့်အရေးများကိုလည်းကောင်း၊|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *mlterm* measures width -1.

.. _mltermlangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===================================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===================================
     1  `U+0059 <https://codepoints.net/U+0059>`_  'Y'       Lu                  1  LATIN CAPITAL LETTER Y
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     4  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
     5  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     7  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     8  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     9  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ===================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Yek\xc3\xabwe'na|\\n123456789|\\n"
        Yekëwe'na|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width -5.

.. _mltermlangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+C2B9 <https://codepoints.net/U+C2B9>`_  '\\uc2b9'  Lo                  2  HANGUL SYLLABLE SEUNG
     2  `U+C778 <https://codepoints.net/U+C778>`_  '\\uc778'  Lo                  2  HANGUL SYLLABLE IN
     3  `U+ACFC <https://codepoints.net/U+ACFC>`_  '\\uacfc'  Lo                  2  HANGUL SYLLABLE GWA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x8a\xb9\xec\x9d\xb8\xea\xb3\xbc|\\n123456|\\n"
        승인과|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width 1.

.. _mltermlangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+202E <https://codepoints.net/U+202E>`_  '\\u202e'  Cf                  0  RIGHT-TO-LEFT OVERRIDE
     2  `U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
     3  `U+202C <https://codepoints.net/U+202C>`_  '\\u202c'  Cf                  0  POP DIRECTIONAL FORMATTING
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe2\x80\xaeA\xe2\x80\xac|\\n1|\\n"
        ‮A‬|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width 3.

.. _mltermlangTamilSriLanka:

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
     2  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     3  `U+0BA3 <https://codepoints.net/U+0BA3>`_  '\\u0ba3'  Lo                  1  TAMIL LETTER NNA
     4  `U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
     5  `U+0BA8 <https://codepoints.net/U+0BA8>`_  '\\u0ba8'  Lo                  1  TAMIL LETTER NA
     6  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     7  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
     8  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     9  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    10  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
    11  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    12  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    13  `U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
    14  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
    15  `U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
    16  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    17  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    18  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
    19  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
    20  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    21  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
    22  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
    23  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
    24  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xa4\xe0\xaf\x81\xe0\xae\xa3\xe0\xae\xbf\xe0\xae\xa8\xe0\xaf\x8d\xe0\xae\xa4\xe0\xaf\x81\xe0\xae\xb3\xe0\xaf\x8d\xe0\xae\xb3\xe0\xae\xbe\xe0\xae\xb0\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xb3\xe0\xae\xbe\xe0\xae\xa4\xe0\xae\xb2\xe0\xae\xbe\xe0\xae\xb2\xe0\xaf\x81\xe0\xae\xae\xe0\xaf\x8d|\\n1234567890123|\\n"
        துணிந்துள்ளார்களாதலாலும்|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *mlterm* measures width 6.

.. _mltermlangTamil:

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
     2  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     3  `U+0BA3 <https://codepoints.net/U+0BA3>`_  '\\u0ba3'  Lo                  1  TAMIL LETTER NNA
     4  `U+0BBF <https://codepoints.net/U+0BBF>`_  '\\u0bbf'  Mc                  0  TAMIL VOWEL SIGN I
     5  `U+0BA8 <https://codepoints.net/U+0BA8>`_  '\\u0ba8'  Lo                  1  TAMIL LETTER NA
     6  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     7  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
     8  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     9  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    10  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
    11  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    12  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    13  `U+0BB0 <https://codepoints.net/U+0BB0>`_  '\\u0bb0'  Lo                  1  TAMIL LETTER RA
    14  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
    15  `U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
    16  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    17  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    18  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
    19  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
    20  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    21  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
    22  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
    23  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
    24  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xa4\xe0\xaf\x81\xe0\xae\xa3\xe0\xae\xbf\xe0\xae\xa8\xe0\xaf\x8d\xe0\xae\xa4\xe0\xaf\x81\xe0\xae\xb3\xe0\xaf\x8d\xe0\xae\xb3\xe0\xae\xbe\xe0\xae\xb0\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xb3\xe0\xae\xbe\xe0\xae\xa4\xe0\xae\xb2\xe0\xae\xbe\xe0\xae\xb2\xe0\xaf\x81\xe0\xae\xae\xe0\xaf\x8d|\\n1234567890123|\\n"
        துணிந்துள்ளார்களாதலாலும்|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *mlterm* measures width 6.

.. _mltermlangColorado:

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "man|\\n123|\\n"
        man|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -4.

.. _mltermlangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0071 <https://codepoints.net/U+0071>`_  'q'       Ll                  1  LATIN SMALL LETTER Q
     4  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "leqder|\\n123456|\\n"
        leqder|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width 0.

.. _mltermlangTelugu:

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0C38 <https://codepoints.net/U+0C38>`_  '\\u0c38'  Lo                  1  TELUGU LETTER SA
     2  `U+0C2E <https://codepoints.net/U+0C2E>`_  '\\u0c2e'  Lo                  1  TELUGU LETTER MA
     3  `U+0C3E <https://codepoints.net/U+0C3E>`_  '\\u0c3e'  Mn                  0  TELUGU VOWEL SIGN AA
     4  `U+0C28 <https://codepoints.net/U+0C28>`_  '\\u0c28'  Lo                  1  TELUGU LETTER NA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\xb8\xe0\xb0\xae\xe0\xb0\xbe\xe0\xb0\xa8|\\n123|\\n"
        సమాన|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -5.

.. _mltermlangMon:

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================================
     1  `U+1012 <https://codepoints.net/U+1012>`_  '\\u1012'  Lo                  1  MYANMAR LETTER DA
     2  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
     3  `U+1002 <https://codepoints.net/U+1002>`_  '\\u1002'  Lo                  1  MYANMAR LETTER GA
     4  `U+1005 <https://codepoints.net/U+1005>`_  '\\u1005'  Lo                  1  MYANMAR LETTER CA
     5  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
     6  `U+1014 <https://codepoints.net/U+1014>`_  '\\u1014'  Lo                  1  MYANMAR LETTER NA
     7  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
     8  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
     9  `U+1060 <https://codepoints.net/U+1060>`_  '\\u1060'  Mn                  0  MYANMAR CONSONANT SIGN MON MEDIAL LA
    10  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
    11  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
    12  `U+1014 <https://codepoints.net/U+1014>`_  '\\u1014'  Lo                  1  MYANMAR LETTER NA
    13  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    14  `U+101B <https://codepoints.net/U+101B>`_  '\\u101b'  Lo                  1  MYANMAR LETTER RA
    15  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
    16  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
    17  `U+105A <https://codepoints.net/U+105A>`_  '\\u105a'  Lo                  1  MYANMAR LETTER MON NGA
    18  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    19  `U+104B <https://codepoints.net/U+104B>`_  '\\u104b'  Po                  1  MYANMAR SIGN SECTION
   ===  =========================================  =========  ==========  =========  ====================================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x92\xe1\x80\xb8\xe1\x80\x82\xe1\x80\x85\xe1\x80\xac\xe1\x80\x94\xe1\x80\xba\xe1\x80\x80\xe1\x81\xa0\xe1\x80\xb1\xe1\x80\xac\xe1\x80\x94\xe1\x80\xba\xe1\x80\x9b\xe1\x80\xb1\xe1\x80\xac\xe1\x81\x9a\xe1\x80\xba\xe1\x81\x8b|\\n123456789|\\n"
        ဒးဂစာန်ကၠောန်ရောၚ်။|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width -8.

.. _mltermlangSanskrit:

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
     2  `U+0926 <https://codepoints.net/U+0926>`_  '\\u0926'  Lo                  1  DEVANAGARI LETTER DA
     3  `U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
     4  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     5  `U+0947 <https://codepoints.net/U+0947>`_  '\\u0947'  Mn                  0  DEVANAGARI VOWEL SIGN E
     6  `U+0937 <https://codepoints.net/U+0937>`_  '\\u0937'  Lo                  1  DEVANAGARI LETTER SSA
     7  `U+0941 <https://codepoints.net/U+0941>`_  '\\u0941'  Mn                  0  DEVANAGARI VOWEL SIGN U
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xa4\xe0\xa4\xa6\xe0\xa5\x80\xe0\xa4\xaf\xe0\xa5\x87\xe0\xa4\xb7\xe0\xa5\x81|\\n1234|\\n"
        तदीयेषु|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -3.

.. _mltermlangSanskritGrantha:

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =====================
     1  `U+00011324 <https://codepoints.net/U+00011324>`_  '\\U00011324'  Lo                  1  GRANTHA LETTER TA
     2  `U+00011326 <https://codepoints.net/U+00011326>`_  '\\U00011326'  Lo                  1  GRANTHA LETTER DA
     3  `U+00011340 <https://codepoints.net/U+00011340>`_  '\\U00011340'  Mn                  0  GRANTHA VOWEL SIGN II
     4  `U+0001132F <https://codepoints.net/U+0001132F>`_  '\\U0001132f'  Lo                  1  GRANTHA LETTER YA
     5  `U+00011347 <https://codepoints.net/U+00011347>`_  '\\U00011347'  Mc                  0  GRANTHA VOWEL SIGN EE
     6  `U+00011337 <https://codepoints.net/U+00011337>`_  '\\U00011337'  Lo                  1  GRANTHA LETTER SSA
     7  `U+00011341 <https://codepoints.net/U+00011341>`_  '\\U00011341'  Mc                  0  GRANTHA VOWEL SIGN U
   ===  =================================================  =============  ==========  =========  =====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xa4\xf0\x91\x8c\xa6\xf0\x91\x8d\x80\xf0\x91\x8c\xaf\xf0\x91\x8d\x87\xf0\x91\x8c\xb7\xf0\x91\x8d\x81|\\n1234|\\n"
        𑌤𑌦𑍀𑌯𑍇𑌷𑍁|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -3.

.. _mltermlangTicuna:

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
     3  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
     4  `U+00E3 <https://codepoints.net/U+00E3>`_  '\\xe3'    Ll                  1  LATIN SMALL LETTER A WITH TILDE
     5  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
     6  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     7  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     9  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
    10  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
    11  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
    12  `U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'    Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
    13  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nax\xc3\xa3xchirux\xc3\xbc\xcc\x83|\\n123456789012|\\n"
        naxãxchiruxü̃|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *mlterm* measures width 10.

.. _mltermlangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     5  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "wenb\xc3\xad|\\n12345|\\n"
        wenbí|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -3.

.. _mltermlangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "la|\\n12|\\n"
        la|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width 0.

.. _mltermlangMaldivian:

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
  while *mlterm* measures width -1.

.. _mltermlangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0066 <https://codepoints.net/U+0066>`_  'f'       Ll                  1  LATIN SMALL LETTER F
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     5  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     7  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     8  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     9  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "faborecer|\\n123456789|\\n"
        faborecer|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 8.

.. _mltermlangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     2  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     3  `U+0634 <https://codepoints.net/U+0634>`_  '\\u0634'  Lo                  1  ARABIC LETTER SHEEN
     4  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     5  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x85\xd9\x86\xd8\xb4\xd9\x88\xd8\xb1|\\n12345|\\n"
        منشور|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -1.

.. _mltermlangw:

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "m\xc9\x94|\\n12|\\n"
        mɔ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -3.

.. _mltermlangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+0641 <https://codepoints.net/U+0641>`_  '\\u0641'  Lo                  1  ARABIC LETTER FEH
     2  `U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x81\xd9\x8a|\\n12|\\n"
        في|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -3.

.. _mltermlangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "po|\\n12|\\n"
        po|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -8.

.. _mltermlangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     6  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     7  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nta\xcc\x81ngo|\\n123456|\\n"
        ntángo|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -4.

.. _mltermlangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     7  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     9  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yetteskin|\\n123456789|\\n"
        yetteskin|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 1.

.. _mltermlangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     7  `U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kunda'vi|\\n12345678|\\n"
        kunda'vi|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *mlterm* measures width 4.

.. _mltermlangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004B <https://codepoints.net/U+004B>`_  'K'       Lu                  1  LATIN CAPITAL LETTER K
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Kin|\\n123|\\n"
        Kin|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -2.

.. _mltermlangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =======================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =======================
     1  `U+0001E932 <https://codepoints.net/U+0001E932>`_  '\\U0001e932'  Ll                  1  ADLAM SMALL LETTER NUN
     2  `U+0001E922 <https://codepoints.net/U+0001E922>`_  '\\U0001e922'  Ll                  1  ADLAM SMALL LETTER ALIF
     3  `U+0001E92C <https://codepoints.net/U+0001E92C>`_  '\\U0001e92c'  Ll                  1  ADLAM SMALL LETTER FA
     4  `U+0001E92E <https://codepoints.net/U+0001E92E>`_  '\\U0001e92e'  Ll                  1  ADLAM SMALL LETTER O
     5  `U+0001E945 <https://codepoints.net/U+0001E945>`_  '\\U0001e945'  Mn                  0  ADLAM VOWEL LENGTHENER
     6  `U+0001E92A <https://codepoints.net/U+0001E92A>`_  '\\U0001e92a'  Ll                  1  ADLAM SMALL LETTER RA
     7  `U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
   ===  =================================================  =============  ==========  =========  =======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xb2\xf0\x9e\xa4\xa2\xf0\x9e\xa4\xac\xf0\x9e\xa4\xae\xf0\x9e\xa5\x85\xf0\x9e\xa4\xaa\xf0\x9e\xa4\xab|\\n123456|\\n"
        𞤲𞤢𞤬𞤮𞥅𞤪𞤫|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -1.

.. _mltermlangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0718 <https://codepoints.net/U+0718>`_  '\\u0718'  Lo                  1  SYRIAC LETTER WAW
     2  `U+0712 <https://codepoints.net/U+0712>`_  '\\u0712'  Lo                  1  SYRIAC LETTER BETH
     3  `U+072A <https://codepoints.net/U+072A>`_  '\\u072a'  Lo                  1  SYRIAC LETTER RISH
     4  `U+0712 <https://codepoints.net/U+0712>`_  '\\u0712'  Lo                  1  SYRIAC LETTER BETH
     5  `U+072A <https://codepoints.net/U+072A>`_  '\\u072a'  Lo                  1  SYRIAC LETTER RISH
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\x98\xdc\x92\xdc\xaa\xdc\x92\xdc\xaa|\\n12345|\\n"
        ܘܒܪܒܪ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 0.

.. _mltermlangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     2  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     5  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "oranga|\\n123456|\\n"
        oranga|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width -3.

.. _mltermlangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     7  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "auwrang|\\n1234567|\\n"
        auwrang|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *mlterm* measures width 1.

.. _mltermlangUrdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================================
     1  `U+0601 <https://codepoints.net/U+0601>`_  '\\u0601'  Cf                  0  ARABIC SIGN SANAH
     2  `U+06F1 <https://codepoints.net/U+06F1>`_  '\\u06f1'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT ONE
     3  `U+06F9 <https://codepoints.net/U+06F9>`_  '\\u06f9'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT NINE
     4  `U+06F4 <https://codepoints.net/U+06F4>`_  '\\u06f4'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT FOUR
     5  `U+06F8 <https://codepoints.net/U+06F8>`_  '\\u06f8'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT EIGHT
     6  `U+0621 <https://codepoints.net/U+0621>`_  '\\u0621'  Lo                  1  ARABIC LETTER HAMZA
   ===  =========================================  =========  ==========  =========  =================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\x81\xdb\xb1\xdb\xb9\xdb\xb4\xdb\xb8\xd8\xa1|\\n12345|\\n"
        ؁۱۹۴۸ء|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

.. _mltermlangUduk:

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

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
  while *mlterm* measures width -2.

.. _mltermlangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     7  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     8  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     9  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "consiroma|\\n123456789|\\n"
        consiroma|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width 4.

.. _mltermlangUrdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================================
     1  `U+0601 <https://codepoints.net/U+0601>`_  '\\u0601'  Cf                  0  ARABIC SIGN SANAH
     2  `U+06F1 <https://codepoints.net/U+06F1>`_  '\\u06f1'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT ONE
     3  `U+06F9 <https://codepoints.net/U+06F9>`_  '\\u06f9'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT NINE
     4  `U+06F4 <https://codepoints.net/U+06F4>`_  '\\u06f4'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT FOUR
     5  `U+06F8 <https://codepoints.net/U+06F8>`_  '\\u06f8'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT EIGHT
     6  `U+0621 <https://codepoints.net/U+0621>`_  '\\u0621'  Lo                  1  ARABIC LETTER HAMZA
   ===  =========================================  =========  ==========  =========  =================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\x81\xdb\xb1\xdb\xb9\xdb\xb4\xdb\xb8\xd8\xa1|\\n12345|\\n"
        ؁۱۹۴۸ء|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 6.

.. _mltermlangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+0076 <https://codepoints.net/U+0076>`_  'v'       Ll                  1  LATIN SMALL LETTER V
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "swiv|\\n1234|\\n"
        swiv|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 1.

.. _mltermlangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     2  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     4  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     5  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ghe\xcc\x81t|\\n1234|\\n"
        ghét|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 1.

.. _mltermlangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ku|\\n12|\\n"
        ku|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -3.

.. _mltermlangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ye|\\n12|\\n"
        ye|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -1.

.. _mltermlangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================
     1  `U+0189 <https://codepoints.net/U+0189>`_  '\\u0189'  Lu                  1  LATIN CAPITAL LETTER AFRICAN D
     2  `U+0045 <https://codepoints.net/U+0045>`_  'E'        Lu                  1  LATIN CAPITAL LETTER E
   ===  =========================================  =========  ==========  =========  ==============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc6\x89E|\\n12|\\n"
        ƉE|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -5.

.. _mltermlangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kuna|\\n1234|\\n"
        kuna|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -4.

.. _mltermlangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     2  `U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
     3  `U+A7B9 <https://codepoints.net/U+A7B9>`_  '\\ua7b9'  Ll                  1  LATIN SMALL LETTER U WITH STROKE
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "k'\xea\x9e\xb9|\\n123|\\n"
        k'ꞹ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -5.

.. _mltermlangSererSine:

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     2  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ole|\\n123|\\n"
        ole|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -1.

.. _mltermlangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004F <https://codepoints.net/U+004F>`_  'O'       Lu                  1  LATIN CAPITAL LETTER O
     2  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Oniti|\\n12345|\\n"
        Oniti|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 1.

.. _mltermlangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yel|\\n123|\\n"
        yel|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width 1.

.. _mltermlangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+00EC <https://codepoints.net/U+00EC>`_  '\\xec'    Ll                  1  LATIN SMALL LETTER I WITH GRAVE
     2  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     3  `U+1EB9 <https://codepoints.net/U+1EB9>`_  '\\u1eb9'  Ll                  1  LATIN SMALL LETTER E WITH DOT BELOW
     4  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     6  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     7  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     8  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
     9  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
    10  `U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'    Ll                  1  LATIN SMALL LETTER U WITH ACUTE
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xact\xe1\xba\xb9\xcc\x80s\xc3\xadw\xc3\xa1j\xc3\xba|\\n123456789|\\n"
        ìtẹ̀síwájú|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *mlterm* measures width -1.

.. _mltermlangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ba|\\n12|\\n"
        ba|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -1.

.. _mltermlangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     3  `U+00EA <https://codepoints.net/U+00EA>`_  '\\xea'    Ll                  1  LATIN SMALL LETTER E WITH CIRCUMFLEX
     4  `U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  ====================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ki\xc3\xaa\xcc\xa3n|\\n1234|\\n"
        kiện|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 0.

.. _mltermlangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+00EC <https://codepoints.net/U+00EC>`_  '\\xec'   Ll                  1  LATIN SMALL LETTER I WITH GRAVE
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "s\xc3\xacn|\\n123|\\n"
        sìn|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -1.

.. _mltermlangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     2  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     3  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     4  `U+064A <https://codepoints.net/U+064A>`_  '\\u064a'  Lo                  1  ARABIC LETTER YEH
     5  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaa\xd8\xa7\xd9\x85\xd9\x8a\xd9\x86|\\n12345|\\n"
        تامين|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width 0.

.. _mltermlangSeraiki:

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
  while *mlterm* measures width -2.

.. _mltermlangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     5  `U+0066 <https://codepoints.net/U+0066>`_  'f'       Ll                  1  LATIN SMALL LETTER F
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "garofi|\\n123456|\\n"
        garofi|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *mlterm* measures width 4.

.. _mltermlangDagaareSouthern:

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+007A <https://codepoints.net/U+007A>`_  'z'       Ll                  1  LATIN SMALL LETTER Z
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "zaa|\\n123|\\n"
        zaa|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width -3.

.. _mltermlangChinantecChiltepec:

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     5  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mako\xcc\xb1|\\n1234|\\n"
        mako̱|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 2.

.. _mltermlangChakma:

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =================
     1  `U+0001111B <https://codepoints.net/U+0001111B>`_  '\\U0001111b'  Lo                  1  CHAKMA LETTER PAA
     2  `U+00011123 <https://codepoints.net/U+00011123>`_  '\\U00011123'  Lo                  1  CHAKMA LETTER LAA
     3  `U+0001111A <https://codepoints.net/U+0001111A>`_  '\\U0001111a'  Lo                  1  CHAKMA LETTER NAA
     4  `U+00011141 <https://codepoints.net/U+00011141>`_  '\\U00011141'  Po                  1  CHAKMA DANDA
   ===  =================================================  =============  ==========  =========  =================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\x9b\xf0\x91\x84\xa3\xf0\x91\x84\x9a\xf0\x91\x85\x81|\\n1234|\\n"
        𑄛𑄣𑄚𑅁|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 0.

.. _mltermlangMaithili:

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
     2  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
     3  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xaa\xe0\xa4\xb0\xe0\xa4\xae|\\n123|\\n"
        परम|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *mlterm* measures width 0.

.. _mltermlangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     2  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     3  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     4  `U+0308 <https://codepoints.net/U+0308>`_  '\\u0308'  Mn                  0  COMBINING DIAERESIS
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "aw\xc9\x9b\xcc\x88n|\\n1234|\\n"
        awɛ̈n|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width 0.

.. _mltermlangGujarati:

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =============================
     1  `U+0AA6 <https://codepoints.net/U+0AA6>`_  '\\u0aa6'  Lo                  1  GUJARATI LETTER DA
     2  `U+0AC3 <https://codepoints.net/U+0AC3>`_  '\\u0ac3'  Mn                  0  GUJARATI VOWEL SIGN VOCALIC R
     3  `U+0AB7 <https://codepoints.net/U+0AB7>`_  '\\u0ab7'  Lo                  1  GUJARATI LETTER SSA
     4  `U+0ACD <https://codepoints.net/U+0ACD>`_  '\\u0acd'  Mn                  0  GUJARATI SIGN VIRAMA
     5  `U+0A9F <https://codepoints.net/U+0A9F>`_  '\\u0a9f'  Lo                  1  GUJARATI LETTER TTA
     6  `U+0ABF <https://codepoints.net/U+0ABF>`_  '\\u0abf'  Mc                  0  GUJARATI VOWEL SIGN I
     7  `U+0A8F <https://codepoints.net/U+0A8F>`_  '\\u0a8f'  Lo                  1  GUJARATI LETTER E
   ===  =========================================  =========  ==========  =========  =============================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\xa6\xe0\xab\x83\xe0\xaa\xb7\xe0\xab\x8d\xe0\xaa\x9f\xe0\xaa\xbf\xe0\xaa\x8f|\\n1234|\\n"
        દૃષ્ટિએ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -2.

.. _mltermlangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     4  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     5  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gotho|\\n12345|\\n"
        gotho|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *mlterm* measures width -4.

.. _mltermlangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     3  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     4  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jij\xc9\x9b|\\n1234|\\n"
        jijɛ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *mlterm* measures width -6.

.. _mltermlangDangme:

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
  while *mlterm* measures width 0.

.. _mltermlangMagahi:

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     2  `U+092C <https://codepoints.net/U+092C>`_  '\\u092c'  Lo                  1  DEVANAGARI LETTER BA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa4\xac|\\n12|\\n"
        सब|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width 0.

.. _mltermlangBhojpuri:

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+0947 <https://codepoints.net/U+0947>`_  '\\u0947'  Mn                  0  DEVANAGARI VOWEL SIGN E
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa5\x87|\\n1|\\n"
        के|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -3.

.. _mltermlangHindi:

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     2  `U+0947 <https://codepoints.net/U+0947>`_  '\\u0947'  Mn                  0  DEVANAGARI VOWEL SIGN E
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb5\xe0\xa5\x87|\\n1|\\n"
        वे|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width 0.

.. _mltermlangPanjabiEastern:

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0A26 <https://codepoints.net/U+0A26>`_  '\\u0a26'  Lo                  1  GURMUKHI LETTER DA
     2  `U+0A40 <https://codepoints.net/U+0A40>`_  '\\u0a40'  Mc                  0  GURMUKHI VOWEL SIGN II
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\xa6\xe0\xa9\x80|\\n1|\\n"
        ਦੀ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -3.

.. _mltermlangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0F62 <https://codepoints.net/U+0F62>`_  '\\u0f62'  Lo                  1  TIBETAN LETTER RA
     2  `U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa2\xe0\xbd\x84|\\n12|\\n"
        རང|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width 0.

.. _mltermlangTaiDam:

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+AABB <https://codepoints.net/U+AABB>`_  '\\uaabb'  Lo                  1  TAI VIET VOWEL AUE
     2  `U+AAAC <https://codepoints.net/U+AAAC>`_  '\\uaaac'  Lo                  1  TAI VIET LETTER LOW HO
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xbb\xea\xaa\xac|\\n12|\\n"
        ꪻꪬ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *mlterm* measures width -1.

.. _mltermlangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
     2  `U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x91\xe0\xbd\xba|\\n1|\\n"
        དེ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *mlterm* measures width -2.

.. _mltermdecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

DEC private modes results for *mlterm*: 34 changeable modes
of 47 supported out of 157 total modes tested (29.9% support, 21.7% changeable).

Complete list of DEC private modes tested:

.. table::
   :class: sphinx-datatable

   ======  =============================  =======================================================================  ===========  ============  =========
     Mode  Name                           Description                                                              Supported    Changeable    Enabled
   ======  =============================  =======================================================================  ===========  ============  =========
        1  DECCKM                         Cursor Keys Mode                                                         Yes          Yes           No
        2  DECANM                         ANSI/VT52 Mode                                                           Yes          Yes           Yes
        3  DECCOLM                        Column Mode                                                              Yes          Yes           No
        4  DECSCLM                        Scrolling Mode                                                           Yes          No            No
        5  DECSCNM                        Screen Mode (light or dark screen)                                       Yes          Yes           No
        6  DECOM                          Origin Mode                                                              Yes          Yes           No
        7  DECAWM                         Auto Wrap Mode                                                           Yes          Yes           Yes
        8  DECARM                         Auto Repeat Mode                                                         Yes          No            Yes
        9  DECINLM                        Interlace Mode / Mouse X10 tracking                                      Yes          No            No
       10  DECEDM                         Editing Mode / Show toolbar (rxvt)                                       No           No            No
       11  DECLTM                         Line Transmit Mode                                                       No           No            No
       12  DECKANAM                       Katakana Shift Mode / Blinking cursor (xterm)                            No           No            No
       13  DECSCFDM                       Space Compression/Field Delimiter Mode / Start blinking cursor (xterm)   No           No            No
       14  DECTEM                         Transmit Execution Mode / Enable XOR of blinking cursor control (xterm)  No           No            No
       16  DECEKEM                        Edit Key Execution Mode                                                  No           No            No
       18  DECPFF                         Print Form Feed                                                          No           No            No
       19  DECPEX                         Printer Extent                                                           Yes          No            Yes
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
       38  DECTEK                         Tektronix 4010/4014 Mode                                                 Yes          No            No
       40  DECCRNLM                       Carriage Return/New Line Mode / Allow 80⇒132 mode (xterm)                Yes          Yes           No
       41  DECUPM                         Unidirectional Print Mode / more(1) fix (xterm)                          No           No            No
       42  DECNRCM                        National Replacement Character Set Mode                                  No           No            No
       43  DECGEPM                        Graphics Expanded Print Mode                                             No           No            No
       44  DECGPCM                        Graphics Print Color Mode / Turn on margin bell (xterm)                  No           No            No
       45  DECGPCS                        Graphics Print Color Syntax / Reverse-wraparound mode (xterm)            Yes          No            No
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
       64  DECPCCM                        Page Cursor Coupling Mode                                                Yes          No            Yes
       65  DECBCMM                        Business Color Matching Mode                                             No           No            No
       66  DECNKM                         Numeric Keypad Mode                                                      Yes          Yes           No
       67  DECBKM                         Backarrow Key Mode                                                       Yes          Yes           No
       68  DECKBUM                        Keyboard Usage Mode                                                      No           No            No
       69  DECVSSM                        Vertical Split Screen Mode / DECLRMM - Left Right Margin Mode            Yes          Yes           No
       70  DECFPM                         Force Plot Mode                                                          No           No            No
       73  DECXRLM                        Transmission Rate Limiting                                               No           No            No
       80  DECSDM                         Sixel Display Mode                                                       Yes          Yes           No
       81  DECKPM                         Key Position Mode                                                        No           No            No
       83  WY_52_LINE                     52 line mode (WY-370)                                                    No           No            No
       84  WYENAT_OFF                     Erasable/nonerasable WYENAT Off attribute select (WY-370)                No           No            No
       85  REPLACEMENT_CHAR_COLOR         Replacement character color (WY-370)                                     No           No            No
       90  DECTHAISCM                     Thai Space Compensating Mode                                             No           No            No
       95  DECNCSM                        No Clearing Screen on Column Change Mode                                 Yes          Yes           No
       96  DECRLCM                        Right to Left Copy Mode                                                  No           No            No
       97  DECCRTSM                       CRT Save Mode                                                            No           No            No
       98  DECARSM                        Auto Resize Mode                                                         Yes          No            Yes
       99  DECMCM                         Modem Control Mode                                                       No           No            No
      100  DECAAM                         Auto Answerback Mode                                                     No           No            No
      101  DECCANSM                       Conceal Answerback Message Mode                                          No           No            No
      102  DECNULM                        Ignore Null Mode                                                         Yes          No            Yes
      103  DECHDPXM                       Half Duplex Mode                                                         No           No            No
      104  DECESKM                        Secondary Keyboard Language Mode                                         No           No            No
      106  DECOSCNM                       Overscan Mode                                                            No           No            No
      108  DECNUMLK                       NumLock Mode                                                             No           No            No
      109  DECCAPSLK                      Caps Lock Mode                                                           No           No            No
      110  DECKLHIM                       Keyboard LEDs Host Indicator Mode                                        No           No            No
      111  DECFWM                         Framed Windows Mode                                                      No           No            No
      112  DECRPL                         Review Previous Lines Mode                                               No           No            No
      113  DECHWUM                        Host Wake-Up Mode                                                        No           No            No
      114  DECATCUM                       Alternate Text Color Underline Mode                                      Yes          No            Yes
      115  DECATCBM                       Alternate Text Color Blink Mode                                          Yes          No            Yes
      116  DECBBSM                        Bold and Blink Style Mode                                                Yes          Yes           No
      117  DECECM                         Erase Color Mode                                                         Yes          Yes           Yes
     1000  MOUSE_REPORT_CLICK             Send Mouse X & Y on button press                                         Yes          Yes           No
     1001  MOUSE_HILITE_TRACKING          Use Hilite Mouse Tracking                                                Yes          No            No
     1002  MOUSE_REPORT_DRAG              Use Cell Motion Mouse Tracking                                           Yes          Yes           No
     1003  MOUSE_ALL_MOTION               Use All Motion Mouse Tracking                                            Yes          Yes           No
     1004  FOCUS_IN_OUT_EVENTS            Send FocusIn/FocusOut events                                             Yes          Yes           No
     1005  MOUSE_EXTENDED_UTF8            Enable UTF-8 Mouse Mode                                                  Yes          Yes           No
     1006  MOUSE_EXTENDED_SGR             Enable SGR Mouse Mode                                                    Yes          Yes           No
     1007  ALT_SCROLL_XTERM               Enable Alternate Scroll Mode                                             No           No            No
     1010  SCROLL_ON_TTY_OUTPUT_RXVT      Scroll to bottom on tty output                                           Yes          Yes           No
     1011  SCROLL_ON_KEYPRESS_RXVT        Scroll to bottom on key press                                            Yes          No            No
     1014  FAST_SCROLL                    Enable fastScroll resource                                               No           No            No
     1015  MOUSE_URXVT                    Enable urxvt Mouse Mode                                                  Yes          Yes           No
     1016  MOUSE_SGR_PIXELS               Enable SGR Mouse PixelMode                                               No           No            No
     1021  BOLD_ITALIC_HIGH_INTENSITY     Bold/italic implies high intensity                                       No           No            No
     1034  META_SETS_EIGHTH_BIT           Interpret "meta" key                                                     Yes          Yes           Yes
     1035  MODIFIERS_ALT_NUMLOCK          Enable special modifiers for Alt and NumLock keys                        No           No            No
     1036  META_SENDS_ESC                 Send ESC when Meta modifies a key                                        Yes          Yes           No
     1037  KP_DELETE_SENDS_DEL            Send DEL from the editing-keypad Delete key                              No           No            No
     1039  ALT_SENDS_ESC                  Send ESC when Alt modifies a key                                         No           No            No
     1040  KEEP_SELECTION_NO_HILITE       Keep selection even if not highlighted                                   No           No            No
     1041  USE_CLIPBOARD_SELECTION        Use the CLIPBOARD selection                                              No           No            No
     1042  URGENCY_ON_CTRL_G              Enable Urgency window manager hint when Control-G is received            Yes          Yes           No
     1043  RAISE_ON_CTRL_G                Enable raising of the window when Control-G is received                  No           No            No
     1044  REUSE_CLIPBOARD_DATA           Reuse the most recent data copied to CLIPBOARD                           No           No            No
     1045  EXTENDED_REVERSE_WRAPAROUND    Extended Reverse-wraparound mode (XTREVWRAP2)                            No           No            No
     1046  ALT_SCREEN_BUFFER_SWITCH       Enable switching to/from Alternate Screen Buffer                         No           No            No
     1047  ALT_SCREEN_BUFFER_XTERM        Use Alternate Screen Buffer                                              Yes          Yes           No
     1048  SAVE_CURSOR_DECSC              Save cursor as in DECSC                                                  Yes          Yes           No
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
     7727  APPLICATION_ESCAPE_KEY         Application escape key mode                                              Yes          Yes           No
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
     8452  SIXEL_SCROLLING_LEAVES_CURSOR  Sixel scrolling leaves cursor to right of graphic                        Yes          Yes           No
     8800  CHARACTER_MAPPING_SERVICE      enable/disable character mapping service                                 Yes          Yes           No
     8840  AMBIGUOUS_WIDTH_DOUBLE_WIDTH   Treat ambiguous width characters as double-width                         No           No            No
     9001  WIN32_INPUT_MODE               win32-input-mode                                                         No           No            No
    19997  KITTY_HANDLE_CTRL_C_Z          Handle Ctrl-C/Ctrl-Z mode                                                No           No            No
   ======  =============================  =======================================================================  ===========  ============  =========

**Summary**: 34 changeable, 123 not changeable.

.. _mltermreproduce:

Reproduction
++++++++++++

To reproduce these results for *mlterm*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --save-yaml=linux-mlterm-3.9.3.yaml \
        --limit-codepoints=5000 \
        --limit-words=5000 \
        --limit-errors=1000

.. _mltermtime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **56.45 seconds** (56s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
