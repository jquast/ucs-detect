.. _LinuxFramebuffer:

Linux Framebuffer
-----------------


Tested Software version 6.14.0-33 on Linux
Full results available at ucs-detect_ repository path
`data/linux-6.14.0-33-fbdev.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-6.14.0-33-fbdev.yaml>`_

.. _LinuxFramebufferscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *Linux Framebuffer*:

.. table::
   :class: sphinx-datatable

   ============  ===========  ==============  ======================================================
   Score Type    Raw Score    Scaled Score    Calculation
   ============  ===========  ==============  ======================================================
   WIDE          81.82%       73.6%           (version_index / total_versions) × (pct_success / 100)
   ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
   LANG          48.11%       8.6%            geometric_mean(language_percentages)
   VS16          100.00%      100.0%          pct_success / 100
   VS15          0.00%        0.0%            pct_success / 100
   DEC Modes     N/A          N/A             modes_changeable / total_modes
   TIME          31.67s       92.2%           1 - ((elapsed - min) / (max - min)) [inverse]
   ============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 45.99%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 44.3%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

**WIDE Score Details:**

Wide character support calculation:
- Best matching Unicode version: 15.1.0
- Version index: 9 of 11 versions tested
- Success rate at this version: 100.0%
- Formula: (9 / 11) × (100.0 / 100)
- Result: 81.82%

**ZWJ Score Details:**

No ZWJ support detected.

**VS16 Score Details:**

Variation Selector-16 support calculation:
- Errors: 0 of 213 codepoints tested
- Success rate: 100.0%
- Formula: 100.0 / 100
- Result: 100.00%

**VS15 Score Details:**

Variation Selector-15 support calculation:
- Errors: 158 of 158 codepoints tested
- Success rate: 0.0%
- Formula: 0.0 / 100
- Result: 0.00%

**DEC Modes Score Details:**

DEC Modes results not available.

**TIME Score Details:**

Test execution time:
- Elapsed time: 31.67 seconds
- Note: This is a raw measurement; lower is better
- Scaled score uses inverse log10 scaling across all terminals
- Scaled result: 92.2%

**LANG Score Details (Geometric Mean):**

Geometric mean calculation:
- Formula: (p₁ × p₂ × ... × pₙ)^(1/n) where n = 119 languages
- About `geometric mean <https://en.wikipedia.org/wiki/Geometric_mean>`_
- Result: 48.11%

.. _LinuxFramebufferwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for Linux Framebuffer appears to be 
**15.1.0**, this is from a summary of the following
results:


.. table::
   :class: sphinx-datatable

   =========  ==========  =========  =============
   version      n_errors    n_total  pct_success
   =========  ==========  =========  =============
   '9.0.0'          1000       1000  0.0%
   '10.0.0'          744        745  0.1%
   '11.0.0'           71         72  1.4%
   '12.0.0'           76         76  0.0%
   '12.1.0'            0          1  100.0%
   '13.0.0'          547        552  0.9%
   '14.0.0'           54         54  0.0%
   '15.0.0'           22         22  0.0%
   '15.1.0'            0          5  100.0%
   '16.0.0'          132        198  33.3%
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
  while *Linux Framebuffer* measures width 1.

.. _LinuxFramebufferzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *Linux Framebuffer* appears to be 
**None**, this is from a summary of the following
results:


.. table::
   :class: sphinx-datatable

   =========  ==========  =========  =============
   version      n_errors    n_total  pct_success
   =========  ==========  =========  =============
   '2.0'              22         22  0.0%
   '4.0'             549        579  5.2%
   '5.0'             100        100  0.0%
   '11.0'             65         73  11.0%
   '12.0'            105        112  6.2%
   '12.1'            145        165  12.1%
   '13.0'             46         51  9.8%
   '13.1'             81         83  2.4%
   '14.0'             20         20  0.0%
   '15.0'              0          1  100.0%
   '15.1'            105        109  3.7%
   '17.0'            129        130  0.8%
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
     7  `U+0001F3FD <https://codepoints.net/U+0001F3FD>`_  '\\U0001f3fd'  Sk                  0  EMOJI MODIFIER FITZPATRICK TYPE-4
   ===  =================================================  =============  ==========  =========  =================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9f\x91\xa9\xf0\x9f\x8f\xbe\xe2\x80\x8d\xf0\x9f\xab\xaf\xe2\x80\x8d\xf0\x9f\x91\xa9\xf0\x9f\x8f\xbd|\\n12|\\n"
        👩🏾‍🫯‍👩🏽|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebuffervs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *Linux Framebuffer* is 0 errors
out of 213 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.

.. _LinuxFramebuffervs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *Linux Framebuffer* is 158 errors
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
  while *Linux Framebuffer* measures width 2.


.. _LinuxFramebufferlang:

Language Support
++++++++++++++++

No languages were tested with 100% success.

The following 119 languages are not fully supported:

.. table::
   :class: sphinx-datatable

   =======================================================================================  ==========  =========  =============
   lang                                                                                       n_errors    n_total  pct_success
   =======================================================================================  ==========  =========  =============
   :ref:`Maldivian <LinuxFramebufferlangMaldivian>`                                               1000       1029  2.8%
   :ref:`Tamil <LinuxFramebufferlangTamil>`                                                       1000       1029  2.8%
   :ref:`Tamil (Sri Lanka) <LinuxFramebufferlangTamilSriLanka>`                                   1000       1029  2.8%
   :ref:`Burmese <LinuxFramebufferlangBurmese>`                                                   1000       1032  3.1%
   :ref:`Mon <LinuxFramebufferlangMon>`                                                            910        946  3.8%
   :ref:`Shan <LinuxFramebufferlangShan>`                                                          880        915  3.8%
   :ref:`Javanese (Javanese) <LinuxFramebufferlangJavaneseJavanese>`                              1000       1055  5.2%
   :ref:`Gujarati <LinuxFramebufferlangGujarati>`                                                 1000       1061  5.7%
   :ref:`Malayalam <LinuxFramebufferlangMalayalam>`                                               1000       1062  5.8%
   :ref:`Kannada <LinuxFramebufferlangKannada>`                                                   1000       1069  6.5%
   :ref:`Khün <LinuxFramebufferlangKhn>`                                                           413        442  6.6%
   :ref:`Tamang, Eastern <LinuxFramebufferlangTamangEastern>`                                       42         45  6.7%
   :ref:`Khmer, Central <LinuxFramebufferlangKhmerCentral>`                                        492        528  6.8%
   :ref:`Chakma <LinuxFramebufferlangChakma>`                                                     1000       1078  7.2%
   :ref:`Bengali <LinuxFramebufferlangBengali>`                                                   1000       1085  7.8%
   :ref:`Telugu <LinuxFramebufferlangTelugu>`                                                     1000       1090  8.3%
   :ref:`Sanskrit <LinuxFramebufferlangSanskrit>`                                                  891       1000  10.9%
   :ref:`Sanskrit (Grantha) <LinuxFramebufferlangSanskritGrantha>`                                 893       1006  11.2%
   :ref:`Marathi <LinuxFramebufferlangMarathi>`                                                   1000       1150  13.0%
   :ref:`Nepali <LinuxFramebufferlangNepali>`                                                     1000       1159  13.7%
   :ref:`Thai (2) <LinuxFramebufferlangThai2>`                                                     268        313  14.4%
   :ref:`Sinhala <LinuxFramebufferlangSinhala>`                                                   1000       1168  14.4%
   :ref:`Hindi <LinuxFramebufferlangHindi>`                                                       1000       1171  14.6%
   :ref:`Panjabi, Eastern <LinuxFramebufferlangPanjabiEastern>`                                   1000       1177  15.0%
   :ref:`Bhojpuri <LinuxFramebufferlangBhojpuri>`                                                 1000       1204  16.9%
   :ref:`Maithili <LinuxFramebufferlangMaithili>`                                                 1000       1218  17.9%
   :ref:`Thai <LinuxFramebufferlangThai>`                                                          274        341  19.6%
   :ref:`Magahi <LinuxFramebufferlangMagahi>`                                                     1000       1309  23.6%
   :ref:`Vietnamese <LinuxFramebufferlangVietnamese>`                                             1000       1320  24.2%
   :ref:`Tagalog (Tagalog) <LinuxFramebufferlangTagalogTagalog>`                                    21         31  32.3%
   :ref:`Tibetan, Central <LinuxFramebufferlangTibetanCentral>`                                   1000       1509  33.7%
   :ref:`Lao <LinuxFramebufferlangLao>`                                                            272        426  36.2%
   :ref:`Dzongkha <LinuxFramebufferlangDzongkha>`                                                 1000       1571  36.3%
   :ref:`Lingala (tones) <LinuxFramebufferlangLingalatones>`                                      1000       1726  42.1%
   :ref:`French (Welche) <LinuxFramebufferlangFrenchWelche>`                                      1000       1912  47.7%
   :ref:`Yiddish, Eastern <LinuxFramebufferlangYiddishEastern>`                                    871       1775  50.9%
   :ref:`Pular (Adlam) <LinuxFramebufferlangPularAdlam>`                                           783       1613  51.5%
   :ref:`Bamun <LinuxFramebufferlangBamun>`                                                       1000       2215  54.9%
   :ref:`Tai Dam <LinuxFramebufferlangTaiDam>`                                                     946       2386  60.4%
   :ref:`Orok <LinuxFramebufferlangOrok>`                                                          492       1245  60.5%
   :ref:`Tem <LinuxFramebufferlangTem>`                                                            639       1659  61.5%
   :ref:`Saint Lucian Creole French <LinuxFramebufferlangSaintLucianCreoleFrench>`                 599       1777  66.3%
   :ref:`Nanai <LinuxFramebufferlangNanai>`                                                        382       1207  68.4%
   :ref:`Evenki <LinuxFramebufferlangEvenki>`                                                      269        899  70.1%
   :ref:`Ticuna <LinuxFramebufferlangTicuna>`                                                      578       2048  71.8%
   :ref:`Amarakaeri <LinuxFramebufferlangAmarakaeri>`                                              404       1446  72.1%
   :ref:`Yaneshaʼ <LinuxFramebufferlangYanesha>`                                                   708       2536  72.1%
   :ref:`South Azerbaijani <LinuxFramebufferlangSouthAzerbaijani>`                                 388       1396  72.2%
   :ref:`Yoruba <LinuxFramebufferlangYoruba>`                                                      554       2454  77.4%
   :ref:`Chickasaw <LinuxFramebufferlangChickasaw>`                                                124        554  77.6%
   :ref:`Maori (2) <LinuxFramebufferlangMaori2>`                                                   480       2385  79.9%
   :ref:`Siona <LinuxFramebufferlangSiona>`                                                        275       1492  81.6%
   :ref:`Catalan (2) <LinuxFramebufferlangCatalan2>`                                               265       1909  86.1%
   :ref:`Shipibo-Conibo <LinuxFramebufferlangShipiboConibo>`                                       323       2540  87.3%
   :ref:`Fur <LinuxFramebufferlangFur>`                                                            231       1838  87.4%
   :ref:`Chinantec, Chiltepec <LinuxFramebufferlangChinantecChiltepec>`                            215       1729  87.6%
   :ref:`Mirandese <LinuxFramebufferlangMirandese>`                                                228       1966  88.4%
   :ref:`Gumuz <LinuxFramebufferlangGumuz>`                                                        135       1283  89.5%
   :ref:`Bora <LinuxFramebufferlangBora>`                                                          166       1598  89.6%
   :ref:`Mòoré <LinuxFramebufferlangMor>`                                                          229       2447  90.6%
   :ref:`Mongolian, Halh (Mongolian) <LinuxFramebufferlangMongolianHalhMongolian>`                   3         33  90.9%
   :ref:`Lamnso' <LinuxFramebufferlangLamnso>`                                                     200       2237  91.1%
   :ref:`Navajo <LinuxFramebufferlangNavajo>`                                                      140       1600  91.2%
   :ref:`Tamazight, Central Atlas <LinuxFramebufferlangTamazightCentralAtlas>`                     156       1822  91.4%
   :ref:`Gilyak <LinuxFramebufferlangGilyak>`                                                      127       1504  91.6%
   :ref:`Ditammari <LinuxFramebufferlangDitammari>`                                                142       1882  92.5%
   :ref:`Assyrian Neo-Aramaic <LinuxFramebufferlangAssyrianNeoAramaic>`                             76       1160  93.4%
   :ref:`Otomi, Mezquital <LinuxFramebufferlangOtomiMezquital>`                                     87       1849  95.3%
   :ref:`Veps <LinuxFramebufferlangVeps>`                                                           62       1323  95.3%
   :ref:`Waama <LinuxFramebufferlangWaama>`                                                         39       1000  96.1%
   :ref:`Dinka, Northeastern <LinuxFramebufferlangDinkaNortheastern>`                               58       1529  96.2%
   :ref:`Kabyle <LinuxFramebufferlangKabyle>`                                                       67       1815  96.3%
   :ref:`Farsi, Western <LinuxFramebufferlangFarsiWestern>`                                         66       1822  96.4%
   :ref:`Éwé <LinuxFramebufferlangw>`                                                               58       2230  97.4%
   :ref:`Baatonum <LinuxFramebufferlangBaatonum>`                                                   49       1939  97.5%
   :ref:`Urdu (2) <LinuxFramebufferlangUrdu2>`                                                      55       2251  97.6%
   :ref:`Urdu <LinuxFramebufferlangUrdu>`                                                           53       2237  97.6%
   :ref:`Uduk <LinuxFramebufferlangUduk>`                                                           75       3247  97.7%
   :ref:`Mazahua Central <LinuxFramebufferlangMazahuaCentral>`                                      36       1574  97.7%
   :ref:`Secoya <LinuxFramebufferlangSecoya>`                                                       32       1409  97.7%
   :ref:`Gen <LinuxFramebufferlangGen>`                                                             49       2309  97.9%
   :ref:`Picard <LinuxFramebufferlangPicard>`                                                       40       2024  98.0%
   :ref:`Mixtec, Metlatónoc <LinuxFramebufferlangMixtecMetlatnoc>`                                  26       1367  98.1%
   :ref:`Dari <LinuxFramebufferlangDari>`                                                           33       1872  98.2%
   :ref:`Arabic, Standard <LinuxFramebufferlangArabicStandard>`                                     22       1348  98.4%
   :ref:`Ga <LinuxFramebufferlangGa>`                                                               29       2039  98.6%
   :ref:`Belanda Viri <LinuxFramebufferlangBelandaViri>`                                            23       2246  99.0%
   :ref:`Vietnamese (Han nom) <LinuxFramebufferlangVietnameseHannom>`                                2        199  99.0%
   :ref:`Chinese, Mandarin (Harbin) <LinuxFramebufferlangChineseMandarinHarbin>`                     2        210  99.0%
   :ref:`Chinese, Mandarin (Traditional) <LinuxFramebufferlangChineseMandarinTraditional>`           2        210  99.0%
   :ref:`Chinese, Yue <LinuxFramebufferlangChineseYue>`                                              2        210  99.0%
   :ref:`(Jinan) <LinuxFramebufferlangJinan>`                                                        2        211  99.1%
   :ref:`Chinese, Gan <LinuxFramebufferlangChineseGan>`                                              2        211  99.1%
   :ref:`Chinese, Mandarin (Guiyang) <LinuxFramebufferlangChineseMandarinGuiyang>`                   2        211  99.1%
   :ref:`Chinese, Wu <LinuxFramebufferlangChineseWu>`                                                2        211  99.1%
   :ref:`Chinese, Hakka <LinuxFramebufferlangChineseHakka>`                                          2        212  99.1%
   :ref:`Chinese, Jinyu <LinuxFramebufferlangChineseJinyu>`                                          2        212  99.1%
   :ref:`Chinese, Mandarin (Beijing) <LinuxFramebufferlangChineseMandarinBeijing>`                   2        212  99.1%
   :ref:`Chinese, Mandarin (Nanjing) <LinuxFramebufferlangChineseMandarinNanjing>`                   2        212  99.1%
   :ref:`Chinese, Mandarin (Tianjin) <LinuxFramebufferlangChineseMandarinTianjin>`                   2        212  99.1%
   :ref:`Chinese, Min Nan <LinuxFramebufferlangChineseMinNan>`                                       2        212  99.1%
   :ref:`Chinese, Xiang <LinuxFramebufferlangChineseXiang>`                                          2        212  99.1%
   :ref:`Japanese (Tokyo) <LinuxFramebufferlangJapaneseTokyo>`                                       3        320  99.1%
   :ref:`Panjabi, Western <LinuxFramebufferlangPanjabiWestern>`                                     22       2419  99.1%
   :ref:`Chinese, Mandarin (Simplified) <LinuxFramebufferlangChineseMandarinSimplified>`             2        225  99.1%
   :ref:`Nuosu <LinuxFramebufferlangNuosu>`                                                          2        230  99.1%
   :ref:`Dangme <LinuxFramebufferlangDangme>`                                                       25       2912  99.1%
   :ref:`Dagaare, Southern <LinuxFramebufferlangDagaareSouthern>`                                   22       2582  99.1%
   :ref:`Japanese <LinuxFramebufferlangJapanese>`                                                    2        299  99.3%
   :ref:`Japanese (Osaka) <LinuxFramebufferlangJapaneseOsaka>`                                       2        308  99.4%
   :ref:`Serer-Sine <LinuxFramebufferlangSererSine>`                                                 9       1596  99.4%
   :ref:`Fon <LinuxFramebufferlangFon>`                                                             13       2520  99.5%
   :ref:`Aja <LinuxFramebufferlangAja>`                                                             10       2061  99.5%
   :ref:`Pashto, Northern <LinuxFramebufferlangPashtoNorthern>`                                      7       2242  99.7%
   :ref:`Dendi <LinuxFramebufferlangDendi>`                                                          4       1569  99.7%
   :ref:`Colorado <LinuxFramebufferlangColorado>`                                                    3       1263  99.8%
   :ref:`Seraiki <LinuxFramebufferlangSeraiki>`                                                      5       2242  99.8%
   :ref:`(Yeonbyeon) <LinuxFramebufferlangYeonbyeon>`                                                2       1061  99.8%
   :ref:`Korean <LinuxFramebufferlangKorean>`                                                        2       1185  99.8%
   =======================================================================================  ==========  =========  =============

.. _LinuxFramebufferlangMaldivian:

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0791 <https://codepoints.net/U+0791>`_  '\\u0791'  Lo                  1  THAANA LETTER DAVIYANI
     2  `U+07A8 <https://codepoints.net/U+07A8>`_  '\\u07a8'  Mn                  0  THAANA IBIFILI
     3  `U+0790 <https://codepoints.net/U+0790>`_  '\\u0790'  Lo                  1  THAANA LETTER SEENU
     4  `U+07AC <https://codepoints.net/U+07AC>`_  '\\u07ac'  Mn                  0  THAANA EBEFILI
     5  `U+0789 <https://codepoints.net/U+0789>`_  '\\u0789'  Lo                  1  THAANA LETTER MEEMU
     6  `U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
     7  `U+0784 <https://codepoints.net/U+0784>`_  '\\u0784'  Lo                  1  THAANA LETTER BAA
     8  `U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
     9  `U+0783 <https://codepoints.net/U+0783>`_  '\\u0783'  Lo                  1  THAANA LETTER RAA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x91\xde\xa8\xde\x90\xde\xac\xde\x89\xde\xb0\xde\x84\xde\xa6\xde\x83|\\n12345|\\n"
        ޑިސެމްބަރ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangTamil:

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
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangTamilSriLanka:

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
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangBurmese:

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
  while *Linux Framebuffer* measures width 16.

.. _LinuxFramebufferlangMon:

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
  while *Linux Framebuffer* measures width 10.

.. _LinuxFramebufferlangShan:

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
  while *Linux Framebuffer* measures width 15.

.. _LinuxFramebufferlangJavaneseJavanese:

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+A9CB <https://codepoints.net/U+A9CB>`_  '\\ua9cb'  Po                  1  JAVANESE PADA ADEG ADEG
     2  `U+A9B1 <https://codepoints.net/U+A9B1>`_  '\\ua9b1'  Lo                  1  JAVANESE LETTER SA
     3  `U+A9A7 <https://codepoints.net/U+A9A7>`_  '\\ua9a7'  Lo                  1  JAVANESE LETTER BA
     4  `U+A9BC <https://codepoints.net/U+A9BC>`_  '\\ua9bc'  Mn                  0  JAVANESE VOWEL SIGN PEPET
     5  `U+A9A4 <https://codepoints.net/U+A9A4>`_  '\\ua9a4'  Lo                  1  JAVANESE LETTER NA
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa7\x8b\xea\xa6\xb1\xea\xa6\xa7\xea\xa6\xbc\xea\xa6\xa4|\\n1234|\\n"
        ꧋ꦱꦧꦼꦤ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangGujarati:

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
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangMalayalam:

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
  while *Linux Framebuffer* measures width 29.

.. _LinuxFramebufferlangKannada:

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
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangKhn:

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
  while *Linux Framebuffer* measures width 22.

.. _LinuxFramebufferlangTamangEastern:

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
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangKhmerCentral:

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
  while *Linux Framebuffer* measures width 36.

.. _LinuxFramebufferlangChakma:

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
  while *Linux Framebuffer* measures width 13.

.. _LinuxFramebufferlangBengali:

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
  while *Linux Framebuffer* measures width 12.

.. _LinuxFramebufferlangTelugu:

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
  while *Linux Framebuffer* measures width 13.

.. _LinuxFramebufferlangSanskrit:

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
  while *Linux Framebuffer* measures width 14.

.. _LinuxFramebufferlangSanskritGrantha:

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
  while *Linux Framebuffer* measures width 14.

.. _LinuxFramebufferlangMarathi:

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
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangNepali:

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
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangThai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

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
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 29


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xa5\xe0\xb8\xa7\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\xa1\xe0\xb8\x99\xe0\xb8\xb8\xe0\xb8\xa9\xe0\xb8\xa2\xe0\xb8\x8a\xe0\xb8\x99|\\n12345678901234567890123|\\n"
        ปฏิญญาสากลว่าด้วยสิทธิมนุษยชน|
        12345678901234567890123|

- python `wcwidth.wcswidth()`_ measures width 23,
  while *Linux Framebuffer* measures width 29.

.. _LinuxFramebufferlangSinhala:

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
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangHindi:

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
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangPanjabiEastern:

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
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangBhojpuri:

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
  while *Linux Framebuffer* measures width 10.

.. _LinuxFramebufferlangMaithili:

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
  while *Linux Framebuffer* measures width 8.

.. _LinuxFramebufferlangThai:

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
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 29


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x9b\xe0\xb8\x8f\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xa5\xe0\xb8\xa7\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\xa1\xe0\xb8\x99\xe0\xb8\xb8\xe0\xb8\xa9\xe0\xb8\xa2\xe0\xb8\x8a\xe0\xb8\x99|\\n12345678901234567890123|\\n"
        ปฏิญญาสากลว่าด้วยสิทธิมนุษยชน|
        12345678901234567890123|

- python `wcwidth.wcswidth()`_ measures width 23,
  while *Linux Framebuffer* measures width 29.

.. _LinuxFramebufferlangMagahi:

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
  while *Linux Framebuffer* measures width 10.

.. _LinuxFramebufferlangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "toa\xcc\x80n|\\n1234|\\n"
        toàn|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangTagalogTagalog:

Tagalog (Tagalog)
^^^^^^^^^^^^^^^^^

Sequence of language *Tagalog (Tagalog)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+170E <https://codepoints.net/U+170E>`_  '\\u170e'  Lo                  1  TAGALOG LETTER LA
     2  `U+1711 <https://codepoints.net/U+1711>`_  '\\u1711'  Lo                  1  TAGALOG LETTER HA
     3  `U+1706 <https://codepoints.net/U+1706>`_  '\\u1706'  Lo                  1  TAGALOG LETTER TA
     4  `U+1714 <https://codepoints.net/U+1714>`_  '\\u1714'  Mn                  0  TAGALOG SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9c\x8e\xe1\x9c\x91\xe1\x9c\x86\xe1\x9c\x94|\\n123|\\n"
        ᜎᜑᜆ᜔|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0F61 <https://codepoints.net/U+0F61>`_  '\\u0f61'  Lo                  1  TIBETAN LETTER YA
     2  `U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
     3  `U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
     4  `U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa1\xe0\xbd\xbc\xe0\xbd\x84\xe0\xbd\xa6|\\n123|\\n"
        ཡོངས|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangLao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0E9B <https://codepoints.net/U+0E9B>`_  '\\u0e9b'  Lo                  1  LAO LETTER PO
     2  `U+0EB0 <https://codepoints.net/U+0EB0>`_  '\\u0eb0'  Lo                  1  LAO VOWEL SIGN A
     3  `U+0E81 <https://codepoints.net/U+0E81>`_  '\\u0e81'  Lo                  1  LAO LETTER KO
     4  `U+0EB2 <https://codepoints.net/U+0EB2>`_  '\\u0eb2'  Lo                  1  LAO VOWEL SIGN AA
     5  `U+0E94 <https://codepoints.net/U+0E94>`_  '\\u0e94'  Lo                  1  LAO LETTER DO
     6  `U+0EAA <https://codepoints.net/U+0EAA>`_  '\\u0eaa'  Lo                  1  LAO LETTER SO SUNG
     7  `U+0EB2 <https://codepoints.net/U+0EB2>`_  '\\u0eb2'  Lo                  1  LAO VOWEL SIGN AA
     8  `U+0E81 <https://codepoints.net/U+0E81>`_  '\\u0e81'  Lo                  1  LAO LETTER KO
     9  `U+0EBB <https://codepoints.net/U+0EBB>`_  '\\u0ebb'  Mn                  0  LAO VOWEL SIGN MAI KON
    10  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xba\x9b\xe0\xba\xb0\xe0\xba\x81\xe0\xba\xb2\xe0\xba\x94\xe0\xba\xaa\xe0\xba\xb2\xe0\xba\x81\xe0\xba\xbb\xe0\xba\x99|\\n123456789|\\n"
        ປະກາດສາກົນ|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Linux Framebuffer* measures width 10.

.. _LinuxFramebufferlangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

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
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+004D <https://codepoints.net/U+004D>`_  'M'        Lu                  1  LATIN CAPITAL LETTER M
     2  `U+004F <https://codepoints.net/U+004F>`_  'O'        Lu                  1  LATIN CAPITAL LETTER O
     3  `U+004C <https://codepoints.net/U+004C>`_  'L'        Lu                  1  LATIN CAPITAL LETTER L
     4  `U+0186 <https://codepoints.net/U+0186>`_  '\\u0186'  Lu                  1  LATIN CAPITAL LETTER OPEN O
     5  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     6  `U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
     7  `U+0047 <https://codepoints.net/U+0047>`_  'G'        Lu                  1  LATIN CAPITAL LETTER G
     8  `U+0186 <https://codepoints.net/U+0186>`_  '\\u0186'  Lu                  1  LATIN CAPITAL LETTER OPEN O
     9  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "MOL\xc6\x86\xcc\x81NG\xc6\x86\xcc\x81|\\n1234567|\\n"
        MOLƆ́NGƆ́|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0044 <https://codepoints.net/U+0044>`_  'D'        Lu                  1  LATIN CAPITAL LETTER D
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     4  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     5  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     7  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     8  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     9  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    10  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
    11  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
    12  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "De\xcc\x81kye\xcc\x80rasyo|\\n1234567890|\\n"
        Dékyèrasyo|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Linux Framebuffer* measures width 12.

.. _LinuxFramebufferlangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================================
     1  `U+05D0 <https://codepoints.net/U+05D0>`_  '\\u05d0'  Lo                  1  HEBREW LETTER ALEF
     2  `U+05B7 <https://codepoints.net/U+05B7>`_  '\\u05b7'  Mn                  0  HEBREW POINT PATAH
     3  `U+05DC <https://codepoints.net/U+05DC>`_  '\\u05dc'  Lo                  1  HEBREW LETTER LAMED
     4  `U+05F0 <https://codepoints.net/U+05F0>`_  '\\u05f0'  Lo                  1  HEBREW LIGATURE YIDDISH DOUBLE VAV
     5  `U+05E2 <https://codepoints.net/U+05E2>`_  '\\u05e2'  Lo                  1  HEBREW LETTER AYIN
     6  `U+05DC <https://codepoints.net/U+05DC>`_  '\\u05dc'  Lo                  1  HEBREW LETTER LAMED
     7  `U+05D8 <https://codepoints.net/U+05D8>`_  '\\u05d8'  Lo                  1  HEBREW LETTER TET
     8  `U+05DC <https://codepoints.net/U+05DC>`_  '\\u05dc'  Lo                  1  HEBREW LETTER LAMED
     9  `U+05E2 <https://codepoints.net/U+05E2>`_  '\\u05e2'  Lo                  1  HEBREW LETTER AYIN
    10  `U+05DB <https://codepoints.net/U+05DB>`_  '\\u05db'  Lo                  1  HEBREW LETTER KAF
    11  `U+05E2 <https://codepoints.net/U+05E2>`_  '\\u05e2'  Lo                  1  HEBREW LETTER AYIN
   ===  =========================================  =========  ==========  =========  ==================================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x90\xd6\xb7\xd7\x9c\xd7\xb0\xd7\xa2\xd7\x9c\xd7\x98\xd7\x9c\xd7\xa2\xd7\x9b\xd7\xa2|\\n1234567890|\\n"
        אַלװעלטלעכע|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Linux Framebuffer* measures width 11.

.. _LinuxFramebufferlangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =========================
     1  `U+0001E916 <https://codepoints.net/U+0001E916>`_  '\\U0001e916'  Lu                  1  ADLAM CAPITAL LETTER HA
     2  `U+0001E90B <https://codepoints.net/U+0001E90B>`_  '\\U0001e90b'  Lu                  1  ADLAM CAPITAL LETTER I
     3  `U+0001E902 <https://codepoints.net/U+0001E902>`_  '\\U0001e902'  Lu                  1  ADLAM CAPITAL LETTER LAAM
     4  `U+0001E946 <https://codepoints.net/U+0001E946>`_  '\\U0001e946'  Mn                  0  ADLAM GEMINATION MARK
     5  `U+0001E900 <https://codepoints.net/U+0001E900>`_  '\\U0001e900'  Lu                  1  ADLAM CAPITAL LETTER ALIF
     6  `U+0001E912 <https://codepoints.net/U+0001E912>`_  '\\U0001e912'  Lu                  1  ADLAM CAPITAL LETTER YA
     7  `U+0001E900 <https://codepoints.net/U+0001E900>`_  '\\U0001e900'  Lu                  1  ADLAM CAPITAL LETTER ALIF
     8  `U+0001E910 <https://codepoints.net/U+0001E910>`_  '\\U0001e910'  Lu                  1  ADLAM CAPITAL LETTER NUN
     9  `U+0001E911 <https://codepoints.net/U+0001E911>`_  '\\U0001e911'  Lu                  1  ADLAM CAPITAL LETTER KAF
    10  `U+0001E90C <https://codepoints.net/U+0001E90C>`_  '\\U0001e90c'  Lu                  1  ADLAM CAPITAL LETTER O
    11  `U+0001E945 <https://codepoints.net/U+0001E945>`_  '\\U0001e945'  Mn                  0  ADLAM VOWEL LENGTHENER
    12  `U+0001E908 <https://codepoints.net/U+0001E908>`_  '\\U0001e908'  Lu                  1  ADLAM CAPITAL LETTER RA
    13  `U+0001E909 <https://codepoints.net/U+0001E909>`_  '\\U0001e909'  Lu                  1  ADLAM CAPITAL LETTER E
   ===  =================================================  =============  ==========  =========  =========================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\x96\xf0\x9e\xa4\x8b\xf0\x9e\xa4\x82\xf0\x9e\xa5\x86\xf0\x9e\xa4\x80\xf0\x9e\xa4\x92\xf0\x9e\xa4\x80\xf0\x9e\xa4\x90\xf0\x9e\xa4\x91\xf0\x9e\xa4\x8c\xf0\x9e\xa5\x85\xf0\x9e\xa4\x88\xf0\x9e\xa4\x89|\\n12345678901|\\n"
        𞤖𞤋𞤂𞥆𞤀𞤒𞤀𞤐𞤑𞤌𞥅𞤈𞤉|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *Linux Framebuffer* measures width 13.

.. _LinuxFramebufferlangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
     2  `U+004A <https://codepoints.net/U+004A>`_  'J'        Lu                  1  LATIN CAPITAL LETTER J
     3  `U+0055 <https://codepoints.net/U+0055>`_  'U'        Lu                  1  LATIN CAPITAL LETTER U
     4  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "NJU\xcc\x81|\\n123|\\n"
        NJÚ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangTaiDam:

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+AAB9 <https://codepoints.net/U+AAB9>`_  '\\uaab9'  Lo                  1  TAI VIET VOWEL UEA
     2  `U+AA95 <https://codepoints.net/U+AA95>`_  '\\uaa95'  Lo                  1  TAI VIET LETTER HIGH TO
     3  `U+AAB8 <https://codepoints.net/U+AAB8>`_  '\\uaab8'  Mn                  0  TAI VIET VOWEL IA
     4  `U+AA89 <https://codepoints.net/U+AA89>`_  '\\uaa89'  Lo                  1  TAI VIET LETTER HIGH NGO
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xb9\xea\xaa\x95\xea\xaa\xb8\xea\xaa\x89|\\n123|\\n"
        ꪹꪕꪸꪉ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0427 <https://codepoints.net/U+0427>`_  '\\u0427'  Lu                  1  CYRILLIC CAPITAL LETTER CHE
     2  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     3  `U+043F <https://codepoints.net/U+043F>`_  '\\u043f'  Ll                  1  CYRILLIC SMALL LETTER PE
     4  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     5  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     6  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
     7  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     8  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     9  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
    10  `U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
    11  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
    12  `U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
    13  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
    14  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xa7\xd0\xb8\xd0\xbf\xd0\xb0\xcc\x84\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xbd\xd0\xb5\xcc\x84\xd1\x81\xd0\xb0\xd0\xbb|\\n123456789012|\\n"
        Чипа̄линне̄сал|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *Linux Framebuffer* measures width 14.

.. _LinuxFramebufferlangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0196 <https://codepoints.net/U+0196>`_  '\\u0196'  Lu                  1  LATIN CAPITAL LETTER IOTA
     2  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     3  `U+028A <https://codepoints.net/U+028A>`_  '\\u028a'  Ll                  1  LATIN SMALL LETTER UPSILON
     4  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     5  `U+002D <https://codepoints.net/U+002D>`_  '-'        Pd                  1  HYPHEN-MINUS
     6  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     7  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     8  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     9  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc6\x96r\xca\x8a\xcc\x81-d\xc9\x9b\xcc\x81\xc9\x9b|\\n1234567|\\n"
        Ɩrʊ́-dɛ́ɛ|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0044 <https://codepoints.net/U+0044>`_  'D'        Lu                  1  LATIN CAPITAL LETTER D
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     4  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     5  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     7  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     8  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     9  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
    10  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
    11  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
    12  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "De\xcc\x81klawasyon|\\n12345678901|\\n"
        Déklawasyon|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *Linux Framebuffer* measures width 12.

.. _LinuxFramebufferlangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+041D <https://codepoints.net/U+041D>`_  '\\u041d'  Lu                  1  CYRILLIC CAPITAL LETTER EN
     2  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     3  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     4  `U+0306 <https://codepoints.net/U+0306>`_  '\\u0306'  Mn                  0  COMBINING BREVE
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\x9d\xd0\xb0\xd0\xb8\xcc\x86|\\n123|\\n"
        Най|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0411 <https://codepoints.net/U+0411>`_  '\\u0411'  Lu                  1  CYRILLIC CAPITAL LETTER BE
     2  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     3  `U+0433 <https://codepoints.net/U+0433>`_  '\\u0433'  Ll                  1  CYRILLIC SMALL LETTER GHE
     4  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     5  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     6  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     7  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\x91\xd1\x83\xd0\xb3\xd0\xb0\xcc\x84\xd0\xb4\xd1\x83|\\n123456|\\n"
        Буга̄ду|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Linux Framebuffer* measures width 7.

.. _LinuxFramebufferlangTicuna:

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
     2  `U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'    Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
     3  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
     4  `U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'    Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
     5  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "N\xc3\xbcx\xc3\xbc\xcc\x83|\\n1234|\\n"
        Nüxü̃|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangAmarakaeri:

Amarakaeri
^^^^^^^^^^

Sequence of language *Amarakaeri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     2  `U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     5  `U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
     6  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     7  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     8  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     9  `U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
    10  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "o'nopoe\xcc\xb1po|\\n123456789|\\n"
        o'nopoe̱po|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Linux Framebuffer* measures width 10.

.. _LinuxFramebufferlangYanesha:

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
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     5  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     6  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     7  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     8  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     9  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xcc\x83allohuen|\\n12345678|\\n"
        ̃allohuen|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0049 <https://codepoints.net/U+0049>`_  'I'        Lu                  1  LATIN CAPITAL LETTER I
     2  `U+0307 <https://codepoints.net/U+0307>`_  '\\u0307'  Mn                  0  COMBINING DOT ABOVE
     3  `U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
     4  `U+0053 <https://codepoints.net/U+0053>`_  'S'        Lu                  1  LATIN CAPITAL LETTER S
     5  `U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
     6  `U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "I\xcc\x87NSAN|\\n12345|\\n"
        İNSAN|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================================
     1  `U+1EB8 <https://codepoints.net/U+1EB8>`_  '\\u1eb8'  Lu                  1  LATIN CAPITAL LETTER E WITH DOT BELOW
     2  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     3  `U+0054 <https://codepoints.net/U+0054>`_  'T'        Lu                  1  LATIN CAPITAL LETTER T
     4  `U+1ECC <https://codepoints.net/U+1ECC>`_  '\\u1ecc'  Lu                  1  LATIN CAPITAL LETTER O WITH DOT BELOW
     5  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  =====================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xba\xb8\xcc\x80T\xe1\xbb\x8c\xcc\x81|\\n123|\\n"
        Ẹ̀TỌ́|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+004D <https://codepoints.net/U+004D>`_  'M'        Lu                  1  LATIN CAPITAL LETTER M
     2  `U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'    Ll                  1  LATIN SMALL LETTER O WITH ACUTE
     3  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     4  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "M\xc3\xb3\xcc\xb1ma|\\n1234|\\n"
        Mó̱ma|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     3  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     4  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     6  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mo\xcc\x84hio|\\n12345|\\n"
        mōhio|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     3  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'    Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
     4  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gu\xc3\xab\xcc\xb1na|\\n12345|\\n"
        guë̱na|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0044 <https://codepoints.net/U+0044>`_  'D'        Lu                  1  LATIN CAPITAL LETTER D
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     8  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     9  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
    10  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
    11  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Declaracio\xcc\x81|\\n1234567890|\\n"
        Declaració|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Linux Framebuffer* measures width 11.

.. _LinuxFramebufferlangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+004A <https://codepoints.net/U+004A>`_  'J'        Lu                  1  LATIN CAPITAL LETTER J
     2  `U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
     3  `U+0053 <https://codepoints.net/U+0053>`_  'S'        Lu                  1  LATIN CAPITAL LETTER S
     4  `U+0043 <https://codepoints.net/U+0043>`_  'C'        Lu                  1  LATIN CAPITAL LETTER C
     5  `U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
     6  `U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
     7  `U+0053 <https://codepoints.net/U+0053>`_  'S'        Lu                  1  LATIN CAPITAL LETTER S
     8  `U+0308 <https://codepoints.net/U+0308>`_  '\\u0308'  Mn                  0  COMBINING DIAERESIS
     9  `U+0048 <https://codepoints.net/U+0048>`_  'H'        Lu                  1  LATIN CAPITAL LETTER H
    10  `U+004F <https://codepoints.net/U+004F>`_  'O'        Lu                  1  LATIN CAPITAL LETTER O
    11  `U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "JASCAAS\xcc\x88HON|\\n1234567890|\\n"
        JASCAAS̈HON|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Linux Framebuffer* measures width 11.

.. _LinuxFramebufferlangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+0044 <https://codepoints.net/U+0044>`_  'D'        Lu                  1  LATIN CAPITAL LETTER D
     2  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
     3  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     5  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     6  `U+0268 <https://codepoints.net/U+0268>`_  '\\u0268'  Ll                  1  LATIN SMALL LETTER I WITH STROKE
     7  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     8  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
     9  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
    10  `U+A78C <https://codepoints.net/U+A78C>`_  '\\ua78c'  Ll                  1  LATIN SMALL LETTER SALTILLO
    11  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "D\xc3\xa1\xcc\xb1ld\xc9\xa8\xcc\x81\xc5\x8b\xc3\xa1\xea\x9e\x8c\xc5\x8b|\\n123456789|\\n"
        Dá̱ldɨ́ŋáꞌŋ|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Linux Framebuffer* measures width 11.

.. _LinuxFramebufferlangChinantecChiltepec:

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
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     5  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     6  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     7  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     8  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "makaloo\xcc\xb1|\\n1234567|\\n"
        makaloo̱|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Linux Framebuffer* measures width 8.

.. _LinuxFramebufferlangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0044 <https://codepoints.net/U+0044>`_  'D'        Lu                  1  LATIN CAPITAL LETTER D
     2  `U+0045 <https://codepoints.net/U+0045>`_  'E'        Lu                  1  LATIN CAPITAL LETTER E
     3  `U+0043 <https://codepoints.net/U+0043>`_  'C'        Lu                  1  LATIN CAPITAL LETTER C
     4  `U+004C <https://codepoints.net/U+004C>`_  'L'        Lu                  1  LATIN CAPITAL LETTER L
     5  `U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
     6  `U+0052 <https://codepoints.net/U+0052>`_  'R'        Lu                  1  LATIN CAPITAL LETTER R
     7  `U+0041 <https://codepoints.net/U+0041>`_  'A'        Lu                  1  LATIN CAPITAL LETTER A
     8  `U+0043 <https://codepoints.net/U+0043>`_  'C'        Lu                  1  LATIN CAPITAL LETTER C
     9  `U+0327 <https://codepoints.net/U+0327>`_  '\\u0327'  Mn                  0  COMBINING CEDILLA
    10  `U+004F <https://codepoints.net/U+004F>`_  'O'        Lu                  1  LATIN CAPITAL LETTER O
    11  `U+004E <https://codepoints.net/U+004E>`_  'N'        Lu                  1  LATIN CAPITAL LETTER N
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "DECLARAC\xcc\xa7ON|\\n1234567890|\\n"
        DECLARAÇON|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Linux Framebuffer* measures width 11.

.. _LinuxFramebufferlangGumuz:

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     5  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     6  `U+0327 <https://codepoints.net/U+0327>`_  '\\u0327'  Mn                  0  COMBINING CEDILLA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "magac\xcc\xa7|\\n12345|\\n"
        magaç|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+0268 <https://codepoints.net/U+0268>`_  '\\u0268'  Ll                  1  LATIN SMALL LETTER I WITH STROKE
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     5  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     6  `U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'    Ll                  1  LATIN SMALL LETTER U WITH ACUTE
     7  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     8  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     9  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "m\xc9\xa8\xcc\x81am\xc3\xbanaa|\\n12345678|\\n"
        mɨ́amúnaa|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "se\xcc\x83n|\\n123|\\n"
        sẽn|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangMongolianHalhMongolian:

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
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     2  `U+007A <https://codepoints.net/U+007A>`_  'z'        Ll                  1  LATIN SMALL LETTER Z
     3  `U+0259 <https://codepoints.net/U+0259>`_  '\\u0259'  Ll                  1  LATIN SMALL LETTER SCHWA
     4  `U+0259 <https://codepoints.net/U+0259>`_  '\\u0259'  Ll                  1  LATIN SMALL LETTER SCHWA
     5  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     6  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "dz\xc9\x99\xc9\x99\xcc\x80n|\\n12345|\\n"
        dzəə̀n|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+0042 <https://codepoints.net/U+0042>`_  'B'        Lu                  1  LATIN CAPITAL LETTER B
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     4  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     6  `U+007A <https://codepoints.net/U+007A>`_  'z'        Ll                  1  LATIN SMALL LETTER Z
     7  `U+0105 <https://codepoints.net/U+0105>`_  '\\u0105'  Ll                  1  LATIN SMALL LETTER A WITH OGONEK
     8  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     9  `U+0105 <https://codepoints.net/U+0105>`_  '\\u0105'  Ll                  1  LATIN SMALL LETTER A WITH OGONEK
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Beehaz\xc4\x85\xcc\x81\xc4\x85|\\n12345678|\\n"
        Beehazą́ą|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0054 <https://codepoints.net/U+0054>`_  'T'        Lu                  1  LATIN CAPITAL LETTER T
     2  `U+0049 <https://codepoints.net/U+0049>`_  'I'        Lu                  1  LATIN CAPITAL LETTER I
     3  `U+0053 <https://codepoints.net/U+0053>`_  'S'        Lu                  1  LATIN CAPITAL LETTER S
     4  `U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
     5  `U+0045 <https://codepoints.net/U+0045>`_  'E'        Lu                  1  LATIN CAPITAL LETTER E
     6  `U+0052 <https://codepoints.net/U+0052>`_  'R'        Lu                  1  LATIN CAPITAL LETTER R
     7  `U+0052 <https://codepoints.net/U+0052>`_  'R'        Lu                  1  LATIN CAPITAL LETTER R
     8  `U+0049 <https://codepoints.net/U+0049>`_  'I'        Lu                  1  LATIN CAPITAL LETTER I
     9  `U+0048 <https://codepoints.net/U+0048>`_  'H'        Lu                  1  LATIN CAPITAL LETTER H
    10  `U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
    11  `U+0054 <https://codepoints.net/U+0054>`_  'T'        Lu                  1  LATIN CAPITAL LETTER T
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "TIS\xcc\xa3ERRIH\xcc\xa3T|\\n123456789|\\n"
        TIṢERRIḤT|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Linux Framebuffer* measures width 11.

.. _LinuxFramebufferlangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================================
     1  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     2  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     3  `U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
     4  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     5  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     6  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     7  `U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
     8  `U+04CA <https://codepoints.net/U+04CA>`_  '\\u04ca'  Ll                  1  CYRILLIC SMALL LETTER EN WITH TAIL
     9  `U+0447 <https://codepoints.net/U+0447>`_  '\\u0447'  Ll                  1  CYRILLIC SMALL LETTER CHE
    10  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
    11  `U+0493 <https://codepoints.net/U+0493>`_  '\\u0493'  Ll                  1  CYRILLIC SMALL LETTER GHE WITH STROKE
    12  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
    13  `U+030C <https://codepoints.net/U+030C>`_  '\\u030c'  Mn                  0  COMBINING CARON
   ===  =========================================  =========  ==========  =========  =====================================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbd\xd0\xb0\xd0\xbc\xd0\xb0\xd0\xb4\xd0\xb8\xd0\xb2\xd3\x8a\xd1\x87\xd0\xbe\xd2\x93\xd1\x80\xcc\x8c|\\n123456789012|\\n"
        намадивӊчоғр̌|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *Linux Framebuffer* measures width 13.

.. _LinuxFramebufferlangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     3  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     4  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     5  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     8  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     9  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "muw\xc9\x9b\xcc\x83rimu|\\n12345678|\\n"
        muwɛ̃rimu|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+072C <https://codepoints.net/U+072C>`_  '\\u072c'  Lo                  1  SYRIAC LETTER TAW
     2  `U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
     3  `U+0712 <https://codepoints.net/U+0712>`_  '\\u0712'  Lo                  1  SYRIAC LETTER BETH
     4  `U+0742 <https://codepoints.net/U+0742>`_  '\\u0742'  Mn                  0  SYRIAC RUKKAKHA
     5  `U+0720 <https://codepoints.net/U+0720>`_  '\\u0720'  Lo                  1  SYRIAC LETTER LAMADH
     6  `U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
     7  `U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\xac\xdc\x9d\xdc\x92\xdd\x82\xdc\xa0\xdc\x9d\xdc\x90|\\n123456|\\n"
        ܬܝܒ݂ܠܝܐ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Linux Framebuffer* measures width 7.

.. _LinuxFramebufferlangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0058 <https://codepoints.net/U+0058>`_  'X'        Lu                  1  LATIN CAPITAL LETTER X
     2  `U+0049 <https://codepoints.net/U+0049>`_  'I'        Lu                  1  LATIN CAPITAL LETTER I
     3  `U+004A <https://codepoints.net/U+004A>`_  'J'        Lu                  1  LATIN CAPITAL LETTER J
     4  `U+004D <https://codepoints.net/U+004D>`_  'M'        Lu                  1  LATIN CAPITAL LETTER M
     5  `U+004F <https://codepoints.net/U+004F>`_  'O'        Lu                  1  LATIN CAPITAL LETTER O
     6  `U+004A <https://codepoints.net/U+004A>`_  'J'        Lu                  1  LATIN CAPITAL LETTER J
     7  `U+004F <https://codepoints.net/U+004F>`_  'O'        Lu                  1  LATIN CAPITAL LETTER O
     8  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     9  `U+0049 <https://codepoints.net/U+0049>`_  'I'        Lu                  1  LATIN CAPITAL LETTER I
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "XIJMOJO\xcc\xb1I|\\n12345678|\\n"
        XIJMOJO̱I|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangVeps:

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     2  `U+0308 <https://codepoints.net/U+0308>`_  '\\u0308'  Mn                  0  COMBINING DIAERESIS
     3  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     5  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     7  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     8  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "u\xcc\x88hthine|\\n1234567|\\n"
        ühthine|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Linux Framebuffer* measures width 8.

.. _LinuxFramebufferlangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xcc\x80|\\n1|\\n"
        ǹ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *Linux Framebuffer* measures width 2.

.. _LinuxFramebufferlangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     3  `U+0308 <https://codepoints.net/U+0308>`_  '\\u0308'  Mn                  0  COMBINING DIAERESIS
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "b\xc9\x9b\xcc\x88i|\\n123|\\n"
        bɛ̈i|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     2  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     3  `U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     5  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     6  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "lh\xcc\xa3erma|\\n123456|\\n"
        lḥerma|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Linux Framebuffer* measures width 7.

.. _LinuxFramebufferlangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
     3  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     4  `U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
     5  `U+0654 <https://codepoints.net/U+0654>`_  '\\u0654'  Mn                  0  ARABIC HAMZA ABOVE
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xd9\x84\xdb\x8c\xd9\x87\xd9\x94|\\n1234|\\n"
        کلیهٔ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangw:

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     2  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     3  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     4  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     6  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     7  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     8  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     9  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
    10  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "hl\xc9\x94\xcc\x83nuw\xc9\x94w\xc9\x94|\\n123456789|\\n"
        hlɔ̃nuwɔwɔ|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *Linux Framebuffer* measures width 10.

.. _LinuxFramebufferlangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     3  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "m\xc9\x9b\xcc\x80|\\n12|\\n"
        mɛ̀|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Linux Framebuffer* measures width 3.

.. _LinuxFramebufferlangUrdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
     3  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     4  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     5  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     6  `U+0650 <https://codepoints.net/U+0650>`_  '\\u0650'  Mn                  0  ARABIC KASRA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x82\xd9\x88\xd8\xa7\xd9\x85\xd9\x90|\\n12345|\\n"
        اقوامِ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangUrdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
     3  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     4  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     5  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     6  `U+0650 <https://codepoints.net/U+0650>`_  '\\u0650'  Mn                  0  ARABIC KASRA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x82\xd9\x88\xd8\xa7\xd9\x85\xd9\x90|\\n12345|\\n"
        اقوامِ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangUduk:

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
     2  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "p\xcc\xb1ara|\\n1234|\\n"
        p̱ara|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0054 <https://codepoints.net/U+0054>`_  'T'        Lu                  1  LATIN CAPITAL LETTER T
     2  `U+0045 <https://codepoints.net/U+0045>`_  'E'        Lu                  1  LATIN CAPITAL LETTER E
     3  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     4  `U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
     5  `U+0045 <https://codepoints.net/U+0045>`_  'E'        Lu                  1  LATIN CAPITAL LETTER E
     6  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "TE\xcc\xb1'E\xcc\xb1|\\n1234|\\n"
        TE̱'E̱|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     4  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'    Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
     5  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     6  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     7  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'    Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
     8  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "can\xc3\xabow\xc3\xab\xcc\xb1|\\n1234567|\\n"
        canëowë̱|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Linux Framebuffer* measures width 8.

.. _LinuxFramebufferlangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     3  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "d\xc9\x94\xcc\x80nna|\\n12345|\\n"
        dɔ̀nna|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0076 <https://codepoints.net/U+0076>`_  'v'        Ll                  1  LATIN SMALL LETTER V
     2  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     4  `U+030A <https://codepoints.net/U+030A>`_  '\\u030a'  Mn                  0  COMBINING RING ABOVE
     5  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     6  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     8  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     9  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "vre\xcc\x8aymint|\\n12345678|\\n"
        vre̊ymint|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width 9.

.. _LinuxFramebufferlangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     5  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     6  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "na'nu\xcc\xb1|\\n12345|\\n"
        na'nu̱|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
     3  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     4  `U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
     5  `U+0654 <https://codepoints.net/U+0654>`_  '\\u0654'  Mn                  0  ARABIC HAMZA ABOVE
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xd9\x84\xdb\x8c\xd9\x87\xd9\x94|\\n1234|\\n"
        کلیهٔ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+0639 <https://codepoints.net/U+0639>`_  '\\u0639'  Lo                  1  ARABIC LETTER AIN
     3  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     4  `U+064F <https://codepoints.net/U+064F>`_  '\\u064f'  Mn                  0  ARABIC DAMMA
     5  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     6  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd8\xb9\xd8\xaa\xd9\x8f\xd9\x85\xd8\xaf|\\n12345|\\n"
        اعتُمد|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     2  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     3  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     4  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     5  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ash\xc9\x94\xcc\x83|\\n1234|\\n"
        ashɔ̃|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+004C <https://codepoints.net/U+004C>`_  'L'        Lu                  1  LATIN CAPITAL LETTER L
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     3  `U+0076 <https://codepoints.net/U+0076>`_  'v'        Ll                  1  LATIN SMALL LETTER V
     4  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'    Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
     5  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Luv\xc3\xab\xcc\x81|\\n1234|\\n"
        Luvë́|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===========================
     1  `U+8A08 <https://codepoints.net/U+8A08>`_          '\\u8a08'      Lo                  2  CJK UNIFIED IDEOGRAPH-8A08
     2  `U+54FF <https://codepoints.net/U+54FF>`_          '\\u54ff'      Lo                  2  CJK UNIFIED IDEOGRAPH-54FF
     3  `U+6E03 <https://codepoints.net/U+6E03>`_          '\\u6e03'      Lo                  2  CJK UNIFIED IDEOGRAPH-6E03
     4  `U+0002825F <https://codepoints.net/U+0002825F>`_  '\\U0002825f'  Lo                  2  CJK UNIFIED IDEOGRAPH-2825F
   ===  =================================================  =============  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\xa8\x88\xe5\x93\xbf\xe6\xb8\x83\xf0\xa8\x89\x9f|\\n12345678|\\n"
        計哿渃𨉟|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width -14.

.. _LinuxFramebufferlangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
     2  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
     3  `U+9053 <https://codepoints.net/U+9053>`_  '\\u9053'  Lo                  2  CJK UNIFIED IDEOGRAPH-9053
     4  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     5  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     6  `U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
     7  `U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
     8  `U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
     9  `U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
    10  `U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
    11  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    12  `U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
    13  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    14  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
    15  `U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
    16  `U+80CC <https://codepoints.net/U+80CC>`_  '\\u80cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-80CC
    17  `U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
    18  `U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
    19  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    20  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    21  `U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
    22  `U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
    23  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
    24  `U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
    25  `U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
    26  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    27  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    28  `U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
    29  `U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
    30  `U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
    31  `U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
    32  `U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
    33  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    34  `U+52BF <https://codepoints.net/U+52BF>`_  '\\u52bf'  Lo                  2  CJK UNIFIED IDEOGRAPH-52BF
    35  `U+5934 <https://codepoints.net/U+5934>`_  '\\u5934'  Lo                  2  CJK UNIFIED IDEOGRAPH-5934
    36  `U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 36


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe5\x9c\xb0\xe9\x81\x93\xe7\x9a\x84\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe7\x9a\x84\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe7\x9a\x84\xe5\xae\x97\xe6\x97\xa8\xe5\x92\x8c\xe5\x8e\x9f\xe5\x88\x99\xe7\x9a\x84\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe8\xaf\x89\xe7\x9a\x84\xe5\x8a\xbf\xe5\xa4\xb4\xe4\xb8\x8b|\\n123456789012345678901234567890123456789012345678901234567890123456789012|\\n"
        在地道的由于非政治性的罪行或违背联合国的宗旨和原则的行为而被起诉的势头下|
        123456789012345678901234567890123456789012345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 72,
  while *Linux Framebuffer* measures width 30.

.. _LinuxFramebufferlangChineseMandarinTraditional:

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+61C9 <https://codepoints.net/U+61C9>`_  '\\u61c9'  Lo                  2  CJK UNIFIED IDEOGRAPH-61C9
     2  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     3  `U+5E73 <https://codepoints.net/U+5E73>`_  '\\u5e73'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E73
     4  `U+7B49 <https://codepoints.net/U+7B49>`_  '\\u7b49'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B49
     5  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     6  `U+6B0A <https://codepoints.net/U+6B0A>`_  '\\u6b0a'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
     7  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x87\x89\xe6\x9c\x89\xe5\xb9\xb3\xe7\xad\x89\xe7\x9a\x84\xe6\xac\x8a\xe5\x88\xa9|\\n12345678901234|\\n"
        應有平等的權利|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *Linux Framebuffer* measures width -10.

.. _LinuxFramebufferlangChineseYue:

Chinese, Yue
^^^^^^^^^^^^

Sequence of language *Chinese, Yue* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
     2  `U+4F55 <https://codepoints.net/U+4F55>`_  '\\u4f55'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F55
     3  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     4  `U+5605 <https://codepoints.net/U+5605>`_  '\\u5605'  Lo                  2  CJK UNIFIED IDEOGRAPH-5605
     5  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     6  `U+7C4D <https://codepoints.net/U+7C4D>`_  '\\u7c4d'  Lo                  2  CJK UNIFIED IDEOGRAPH-7C4D
     7  `U+5514 <https://codepoints.net/U+5514>`_  '\\u5514'  Lo                  2  CJK UNIFIED IDEOGRAPH-5514
     8  `U+597D <https://codepoints.net/U+597D>`_  '\\u597d'  Lo                  2  CJK UNIFIED IDEOGRAPH-597D
     9  `U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
    10  `U+610F <https://codepoints.net/U+610F>`_  '\\u610f'  Lo                  2  CJK UNIFIED IDEOGRAPH-610F
    11  `U+5265 <https://codepoints.net/U+5265>`_  '\\u5265'  Lo                  2  CJK UNIFIED IDEOGRAPH-5265
    12  `U+593A <https://codepoints.net/U+593A>`_  '\\u593a'  Lo                  2  CJK UNIFIED IDEOGRAPH-593A
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xbb\xe4\xbd\x95\xe4\xba\xba\xe5\x98\x85\xe5\x9b\xbd\xe7\xb1\x8d\xe5\x94\x94\xe5\xa5\xbd\xe4\xbb\xbb\xe6\x84\x8f\xe5\x89\xa5\xe5\xa4\xba|\\n123456789012345678901234|\\n"
        任何人嘅国籍唔好任意剥夺|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *Linux Framebuffer* measures width 2.

.. _LinuxFramebufferlangJinan:

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+662F <https://codepoints.net/U+662F>`_  '\\u662f'  Lo                  2  CJK UNIFIED IDEOGRAPH-662F
     2  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     3  `U+90FD <https://codepoints.net/U+90FD>`_  '\\u90fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-90FD
     4  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     5  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     6  `U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
     7  `U+5176 <https://codepoints.net/U+5176>`_  '\\u5176'  Lo                  2  CJK UNIFIED IDEOGRAPH-5176
     8  `U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
     9  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    10  `U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
    11  `U+62FE <https://codepoints.net/U+62FE>`_  '\\u62fe'  Lo                  2  CJK UNIFIED IDEOGRAPH-62FE
    12  `U+7FFB <https://codepoints.net/U+7FFB>`_  '\\u7ffb'  Lo                  2  CJK UNIFIED IDEOGRAPH-7FFB
    13  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
    14  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
    15  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    16  `U+5E87 <https://codepoints.net/U+5E87>`_  '\\u5e87'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E87
    17  `U+62A4 <https://codepoints.net/U+62A4>`_  '\\u62a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-62A4
    18  `U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
    19  `U+907F <https://codepoints.net/U+907F>`_  '\\u907f'  Lo                  2  CJK UNIFIED IDEOGRAPH-907F
    20  `U+514D <https://codepoints.net/U+514D>`_  '\\u514d'  Lo                  2  CJK UNIFIED IDEOGRAPH-514D
    21  `U+8FEB <https://codepoints.net/U+8FEB>`_  '\\u8feb'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FEB
    22  `U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 22


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x98\xaf\xe4\xba\xba\xe9\x83\xbd\xe6\x9c\x89\xe6\x9d\x83\xe5\x9c\xa8\xe5\x85\xb6\xe4\xbb\x96\xe5\x9b\xbd\xe5\xae\xb6\xe6\x8b\xbe\xe7\xbf\xbb\xe5\x92\x8c\xe4\xba\xab\xe5\x8f\x97\xe5\xba\x87\xe6\x8a\xa4\xe4\xbb\xa5\xe9\x81\xbf\xe5\x85\x8d\xe8\xbf\xab\xe5\xae\xb3|\\n12345678901234567890123456789012345678901234|\\n"
        是人都有权在其他国家拾翻和享受庇护以避免迫害|
        12345678901234567890123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 44,
  while *Linux Framebuffer* measures width 36.

.. _LinuxFramebufferlangChineseGan:

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
     2  `U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
     3  `U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
     4  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     5  `U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
     6  `U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
     7  `U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
     8  `U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
     9  `U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
    10  `U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
    11  `U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
    12  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    13  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
    14  `U+6627 <https://codepoints.net/U+6627>`_  '\\u6627'  Lo                  2  CJK UNIFIED IDEOGRAPH-6627
    15  `U+5230 <https://codepoints.net/U+5230>`_  '\\u5230'  Lo                  2  CJK UNIFIED IDEOGRAPH-5230
    16  `U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
    17  `U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
    18  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    19  `U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
    20  `U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
    21  `U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
    22  `U+8DDF <https://codepoints.net/U+8DDF>`_  '\\u8ddf'  Lo                  2  CJK UNIFIED IDEOGRAPH-8DDF
    23  `U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
    24  `U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
    25  `U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
    26  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    27  `U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
    28  `U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
    29  `U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
    30  `U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
    31  `U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
    32  `U+4E2A <https://codepoints.net/U+4E2A>`_  '\\u4e2a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E2A
    33  `U+5730 <https://codepoints.net/U+5730>`_  '\\u5730'  Lo                  2  CJK UNIFIED IDEOGRAPH-5730
    34  `U+6B65 <https://codepoints.net/U+6B65>`_  '\\u6b65'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B65
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 34


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe4\xb8\xaa\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe6\x98\xa7\xe5\x88\xb0\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe4\xb8\xaa\xe5\xae\x97\xe6\x97\xa8\xe8\xb7\x9f\xe5\x8e\x9f\xe5\x88\x99\xe4\xb8\xaa\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe8\xaf\x89\xe4\xb8\xaa\xe5\x9c\xb0\xe6\xad\xa5|\\n12345678901234567890123456789012345678901234567890123456789012345678|\\n"
        在真正由于非政治性个罪行或昧到联合国个宗旨跟原则个行为而被起诉个地步|
        12345678901234567890123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 68,
  while *Linux Framebuffer* measures width 26.

.. _LinuxFramebufferlangChineseMandarinGuiyang:

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
     2  `U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
     3  `U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
     4  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     5  `U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
     6  `U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
     7  `U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
     8  `U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
     9  `U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
    10  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    11  `U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
    12  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    13  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
    14  `U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
    15  `U+80CC <https://codepoints.net/U+80CC>`_  '\\u80cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-80CC
    16  `U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
    17  `U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
    18  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    19  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    20  `U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
    21  `U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
    22  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
    23  `U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
    24  `U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
    25  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    26  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    27  `U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
    28  `U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
    29  `U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
    30  `U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
    31  `U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
    32  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    33  `U+60C5 <https://codepoints.net/U+60C5>`_  '\\u60c5'  Lo                  2  CJK UNIFIED IDEOGRAPH-60C5
    34  `U+51B5 <https://codepoints.net/U+51B5>`_  '\\u51b5'  Lo                  2  CJK UNIFIED IDEOGRAPH-51B5
    35  `U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 35


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe7\x9a\x84\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe7\x9a\x84\xe5\xae\x97\xe6\x97\xa8\xe5\x92\x8c\xe5\x8e\x9f\xe5\x88\x99\xe7\x9a\x84\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe8\xaf\x89\xe7\x9a\x84\xe6\x83\x85\xe5\x86\xb5\xe4\xb8\x8b|\\n1234567890123456789012345678901234567890123456789012345678901234567890|\\n"
        在真正由于非政治性的罪行或违背联合国的宗旨和原则的行为而被起诉的情况下|
        1234567890123456789012345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 70,
  while *Linux Framebuffer* measures width 28.

.. _LinuxFramebufferlangChineseWu:

Chinese, Wu
^^^^^^^^^^^

Sequence of language *Chinese, Wu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     2  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     3  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     4  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     5  `U+62C9 <https://codepoints.net/U+62C9>`_  '\\u62c9'  Lo                  2  CJK UNIFIED IDEOGRAPH-62C9
     6  `U+5176 <https://codepoints.net/U+5176>`_  '\\u5176'  Lo                  2  CJK UNIFIED IDEOGRAPH-5176
     7  `U+4ED6 <https://codepoints.net/U+4ED6>`_  '\\u4ed6'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED6
     8  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     9  `U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
    10  `U+5BFB <https://codepoints.net/U+5BFB>`_  '\\u5bfb'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BFB
    11  `U+6C42 <https://codepoints.net/U+6C42>`_  '\\u6c42'  Lo                  2  CJK UNIFIED IDEOGRAPH-6C42
    12  `U+8131 <https://codepoints.net/U+8131>`_  '\\u8131'  Lo                  2  CJK UNIFIED IDEOGRAPH-8131
    13  `U+4ED4 <https://codepoints.net/U+4ED4>`_  '\\u4ed4'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ED4
    14  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
    15  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    16  `U+5E87 <https://codepoints.net/U+5E87>`_  '\\u5e87'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E87
    17  `U+62A4 <https://codepoints.net/U+62A4>`_  '\\u62a4'  Lo                  2  CJK UNIFIED IDEOGRAPH-62A4
    18  `U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
    19  `U+907F <https://codepoints.net/U+907F>`_  '\\u907f'  Lo                  2  CJK UNIFIED IDEOGRAPH-907F
    20  `U+514D <https://codepoints.net/U+514D>`_  '\\u514d'  Lo                  2  CJK UNIFIED IDEOGRAPH-514D
    21  `U+8FEB <https://codepoints.net/U+8FEB>`_  '\\u8feb'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FEB
    22  `U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 22


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xba\xba\xe4\xba\xba\xe6\x9c\x89\xe6\x9d\x83\xe6\x8b\x89\xe5\x85\xb6\xe4\xbb\x96\xe5\x9b\xbd\xe5\xae\xb6\xe5\xaf\xbb\xe6\xb1\x82\xe8\x84\xb1\xe4\xbb\x94\xe4\xba\xab\xe5\x8f\x97\xe5\xba\x87\xe6\x8a\xa4\xe4\xbb\xa5\xe9\x81\xbf\xe5\x85\x8d\xe8\xbf\xab\xe5\xae\xb3|\\n12345678901234567890123456789012345678901234|\\n"
        人人有权拉其他国家寻求脱仔享受庇护以避免迫害|
        12345678901234567890123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 44,
  while *Linux Framebuffer* measures width 36.

.. _LinuxFramebufferlangChineseHakka:

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5514 <https://codepoints.net/U+5514>`_  '\\u5514'  Lo                  2  CJK UNIFIED IDEOGRAPH-5514
     2  `U+597D <https://codepoints.net/U+597D>`_  '\\u597d'  Lo                  2  CJK UNIFIED IDEOGRAPH-597D
     3  `U+63F4 <https://codepoints.net/U+63F4>`_  '\\u63f4'  Lo                  2  CJK UNIFIED IDEOGRAPH-63F4
     4  `U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
     5  `U+6B64 <https://codepoints.net/U+6B64>`_  '\\u6b64'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B64
     6  `U+79CD <https://codepoints.net/U+79CD>`_  '\\u79cd'  Lo                  2  CJK UNIFIED IDEOGRAPH-79CD
     7  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     8  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x94\x94\xe5\xa5\xbd\xe6\x8f\xb4\xe7\x94\xa8\xe6\xad\xa4\xe7\xa7\x8d\xe6\x9d\x83\xe5\x88\xa9|\\n1234567890123456|\\n"
        唔好援用此种权利|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *Linux Framebuffer* measures width -54.

.. _LinuxFramebufferlangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+8C01 <https://codepoints.net/U+8C01>`_  '\\u8c01'  Lo                  2  CJK UNIFIED IDEOGRAPH-8C01
     2  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     3  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     4  `U+7C4D <https://codepoints.net/U+7C4D>`_  '\\u7c4d'  Lo                  2  CJK UNIFIED IDEOGRAPH-7C4D
     5  `U+4E5F <https://codepoints.net/U+4E5F>`_  '\\u4e5f'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E5F
     6  `U+4E0D <https://codepoints.net/U+4E0D>`_  '\\u4e0d'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0D
     7  `U+6562 <https://codepoints.net/U+6562>`_  '\\u6562'  Lo                  2  CJK UNIFIED IDEOGRAPH-6562
     8  `U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
     9  `U+610F <https://codepoints.net/U+610F>`_  '\\u610f'  Lo                  2  CJK UNIFIED IDEOGRAPH-610F
    10  `U+5265 <https://codepoints.net/U+5265>`_  '\\u5265'  Lo                  2  CJK UNIFIED IDEOGRAPH-5265
    11  `U+593A <https://codepoints.net/U+593A>`_  '\\u593a'  Lo                  2  CJK UNIFIED IDEOGRAPH-593A
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\xb0\x81\xe7\x9a\x84\xe5\x9b\xbd\xe7\xb1\x8d\xe4\xb9\x9f\xe4\xb8\x8d\xe6\x95\xa2\xe4\xbb\xbb\xe6\x84\x8f\xe5\x89\xa5\xe5\xa4\xba|\\n1234567890123456789012|\\n"
        谁的国籍也不敢任意剥夺|
        1234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 22,
  while *Linux Framebuffer* measures width 0.

.. _LinuxFramebufferlangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
     2  `U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
     3  `U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
     4  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     5  `U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
     6  `U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
     7  `U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
     8  `U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
     9  `U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
    10  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    11  `U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
    12  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    13  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
    14  `U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
    15  `U+80CC <https://codepoints.net/U+80CC>`_  '\\u80cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-80CC
    16  `U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
    17  `U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
    18  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    19  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    20  `U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
    21  `U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
    22  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
    23  `U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
    24  `U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
    25  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    26  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    27  `U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
    28  `U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
    29  `U+88AB <https://codepoints.net/U+88AB>`_  '\\u88ab'  Lo                  2  CJK UNIFIED IDEOGRAPH-88AB
    30  `U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
    31  `U+8BC9 <https://codepoints.net/U+8BC9>`_  '\\u8bc9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8BC9
    32  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    33  `U+78B4 <https://codepoints.net/U+78B4>`_  '\\u78b4'  Lo                  2  CJK UNIFIED IDEOGRAPH-78B4
    34  `U+513F <https://codepoints.net/U+513F>`_  '\\u513f'  Lo                  2  CJK UNIFIED IDEOGRAPH-513F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 34


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe7\x9a\x84\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe7\x9a\x84\xe5\xae\x97\xe6\x97\xa8\xe5\x92\x8c\xe5\x8e\x9f\xe5\x88\x99\xe7\x9a\x84\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe8\xa2\xab\xe8\xb5\xb7\xe8\xaf\x89\xe7\x9a\x84\xe7\xa2\xb4\xe5\x84\xbf|\\n12345678901234567890123456789012345678901234567890123456789012345678|\\n"
        在真正由于非政治性的罪行或违背联合国的宗旨和原则的行为而被起诉的碴儿|
        12345678901234567890123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 68,
  while *Linux Framebuffer* measures width 22.

.. _LinuxFramebufferlangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+514D <https://codepoints.net/U+514D>`_  '\\u514d'  Lo                  2  CJK UNIFIED IDEOGRAPH-514D
     2  `U+5F97 <https://codepoints.net/U+5F97>`_  '\\u5f97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5F97
     3  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
     4  `U+8FEB <https://codepoints.net/U+8FEB>`_  '\\u8feb'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FEB
     5  `U+5BB3 <https://codepoints.net/U+5BB3>`_  '\\u5bb3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB3
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\x8d\xe5\xbe\x97\xe5\x8f\x97\xe8\xbf\xab\xe5\xae\xb3|\\n1234567890|\\n"
        免得受迫害|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *Linux Framebuffer* measures width -22.

.. _LinuxFramebufferlangChineseMandarinTianjin:

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
     2  `U+514D <https://codepoints.net/U+514D>`_  '\\u514d'  Lo                  2  CJK UNIFIED IDEOGRAPH-514D
     3  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
     4  `U+4ECB <https://codepoints.net/U+4ECB>`_  '\\u4ecb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4ECB
     5  `U+9053 <https://codepoints.net/U+9053>`_  '\\u9053'  Lo                  2  CJK UNIFIED IDEOGRAPH-9053
     6  `U+53F7 <https://codepoints.net/U+53F7>`_  '\\u53f7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53F7
     7  `U+513F <https://codepoints.net/U+513F>`_  '\\u513f'  Lo                  2  CJK UNIFIED IDEOGRAPH-513F
     8  `U+5E72 <https://codepoints.net/U+5E72>`_  '\\u5e72'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E72
     9  `U+6D89 <https://codepoints.net/U+6D89>`_  '\\u6d89'  Lo                  2  CJK UNIFIED IDEOGRAPH-6D89
    10  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
    11  `U+8D25 <https://codepoints.net/U+8D25>`_  '\\u8d25'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D25
    12  `U+574F <https://codepoints.net/U+574F>`_  '\\u574f'  Lo                  2  CJK UNIFIED IDEOGRAPH-574F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xa5\xe5\x85\x8d\xe5\x8f\x97\xe4\xbb\x8b\xe9\x81\x93\xe5\x8f\xb7\xe5\x84\xbf\xe5\xb9\xb2\xe6\xb6\x89\xe6\x88\x96\xe8\xb4\xa5\xe5\x9d\x8f|\\n123456789012345678901234|\\n"
        以免受介道号儿干涉或败坏|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *Linux Framebuffer* measures width 0.

.. _LinuxFramebufferlangChineseMinNan:

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
     4  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     5  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     6  `U+7C4D <https://codepoints.net/U+7C4D>`_  '\\u7c4d'  Lo                  2  CJK UNIFIED IDEOGRAPH-7C4D
     7  `U+52FF <https://codepoints.net/U+52FF>`_  '\\u52ff'  Lo                  2  CJK UNIFIED IDEOGRAPH-52FF
     8  `U+4F1A <https://codepoints.net/U+4F1A>`_  '\\u4f1a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F1A
     9  `U+7528 <https://codepoints.net/U+7528>`_  '\\u7528'  Lo                  2  CJK UNIFIED IDEOGRAPH-7528
    10  `U+4EFB <https://codepoints.net/U+4EFB>`_  '\\u4efb'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EFB
    11  `U+610F <https://codepoints.net/U+610F>`_  '\\u610f'  Lo                  2  CJK UNIFIED IDEOGRAPH-610F
    12  `U+5265 <https://codepoints.net/U+5265>`_  '\\u5265'  Lo                  2  CJK UNIFIED IDEOGRAPH-5265
    13  `U+593A <https://codepoints.net/U+593A>`_  '\\u593a'  Lo                  2  CJK UNIFIED IDEOGRAPH-593A
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xbb\xe4\xbd\x95\xe4\xba\xba\xe7\x9a\x84\xe5\x9b\xbd\xe7\xb1\x8d\xe5\x8b\xbf\xe4\xbc\x9a\xe7\x94\xa8\xe4\xbb\xbb\xe6\x84\x8f\xe5\x89\xa5\xe5\xa4\xba|\\n12345678901234567890123456|\\n"
        任何人的国籍勿会用任意剥夺|
        12345678901234567890123456|

- python `wcwidth.wcswidth()`_ measures width 26,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangChineseXiang:

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5728 <https://codepoints.net/U+5728>`_  '\\u5728'  Lo                  2  CJK UNIFIED IDEOGRAPH-5728
     2  `U+771F <https://codepoints.net/U+771F>`_  '\\u771f'  Lo                  2  CJK UNIFIED IDEOGRAPH-771F
     3  `U+6B63 <https://codepoints.net/U+6B63>`_  '\\u6b63'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
     4  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     5  `U+4E8E <https://codepoints.net/U+4E8E>`_  '\\u4e8e'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E8E
     6  `U+975E <https://codepoints.net/U+975E>`_  '\\u975e'  Lo                  2  CJK UNIFIED IDEOGRAPH-975E
     7  `U+653F <https://codepoints.net/U+653F>`_  '\\u653f'  Lo                  2  CJK UNIFIED IDEOGRAPH-653F
     8  `U+6CBB <https://codepoints.net/U+6CBB>`_  '\\u6cbb'  Lo                  2  CJK UNIFIED IDEOGRAPH-6CBB
     9  `U+6027 <https://codepoints.net/U+6027>`_  '\\u6027'  Lo                  2  CJK UNIFIED IDEOGRAPH-6027
    10  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    11  `U+7F6A <https://codepoints.net/U+7F6A>`_  '\\u7f6a'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F6A
    12  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    13  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
    14  `U+8FDD <https://codepoints.net/U+8FDD>`_  '\\u8fdd'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDD
    15  `U+80CC <https://codepoints.net/U+80CC>`_  '\\u80cc'  Lo                  2  CJK UNIFIED IDEOGRAPH-80CC
    16  `U+8054 <https://codepoints.net/U+8054>`_  '\\u8054'  Lo                  2  CJK UNIFIED IDEOGRAPH-8054
    17  `U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
    18  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
    19  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    20  `U+5B97 <https://codepoints.net/U+5B97>`_  '\\u5b97'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B97
    21  `U+65E8 <https://codepoints.net/U+65E8>`_  '\\u65e8'  Lo                  2  CJK UNIFIED IDEOGRAPH-65E8
    22  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
    23  `U+539F <https://codepoints.net/U+539F>`_  '\\u539f'  Lo                  2  CJK UNIFIED IDEOGRAPH-539F
    24  `U+5219 <https://codepoints.net/U+5219>`_  '\\u5219'  Lo                  2  CJK UNIFIED IDEOGRAPH-5219
    25  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    26  `U+884C <https://codepoints.net/U+884C>`_  '\\u884c'  Lo                  2  CJK UNIFIED IDEOGRAPH-884C
    27  `U+4E3A <https://codepoints.net/U+4E3A>`_  '\\u4e3a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E3A
    28  `U+800C <https://codepoints.net/U+800C>`_  '\\u800c'  Lo                  2  CJK UNIFIED IDEOGRAPH-800C
    29  `U+6253 <https://codepoints.net/U+6253>`_  '\\u6253'  Lo                  2  CJK UNIFIED IDEOGRAPH-6253
    30  `U+5B98 <https://codepoints.net/U+5B98>`_  '\\u5b98'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B98
    31  `U+53F8 <https://codepoints.net/U+53F8>`_  '\\u53f8'  Lo                  2  CJK UNIFIED IDEOGRAPH-53F8
    32  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    33  `U+60C5 <https://codepoints.net/U+60C5>`_  '\\u60c5'  Lo                  2  CJK UNIFIED IDEOGRAPH-60C5
    34  `U+51B5 <https://codepoints.net/U+51B5>`_  '\\u51b5'  Lo                  2  CJK UNIFIED IDEOGRAPH-51B5
    35  `U+4E0B <https://codepoints.net/U+4E0B>`_  '\\u4e0b'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E0B
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 35


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9c\xa8\xe7\x9c\x9f\xe6\xad\xa3\xe7\x94\xb1\xe4\xba\x8e\xe9\x9d\x9e\xe6\x94\xbf\xe6\xb2\xbb\xe6\x80\xa7\xe7\x9a\x84\xe7\xbd\xaa\xe8\xa1\x8c\xe6\x88\x96\xe8\xbf\x9d\xe8\x83\x8c\xe8\x81\x94\xe5\x90\x88\xe5\x9b\xbd\xe7\x9a\x84\xe5\xae\x97\xe6\x97\xa8\xe5\x92\x8c\xe5\x8e\x9f\xe5\x88\x99\xe7\x9a\x84\xe8\xa1\x8c\xe4\xb8\xba\xe8\x80\x8c\xe6\x89\x93\xe5\xae\x98\xe5\x8f\xb8\xe7\x9a\x84\xe6\x83\x85\xe5\x86\xb5\xe4\xb8\x8b|\\n1234567890123456789012345678901234567890123456789012345678901234567890|\\n"
        在真正由于非政治性的罪行或违背联合国的宗旨和原则的行为而打官司的情况下|
        1234567890123456789012345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 70,
  while *Linux Framebuffer* measures width 34.

.. _LinuxFramebufferlangJapaneseTokyo:

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+0031 <https://codepoints.net/U+0031>`_  '1'        Nd                  1  DIGIT ONE
     3  `U+0030 <https://codepoints.net/U+0030>`_  '0'        Nd                  1  DIGIT ZERO
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac10|\\n1234|\\n"
        第10|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width -22.

.. _LinuxFramebufferlangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+064F <https://codepoints.net/U+064F>`_  '\\u064f'  Mn                  0  ARABIC DAMMA
     3  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     4  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x8f\xd9\x86\xdb\x8c|\\n123|\\n"
        اُنی|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangChineseMandarinSimplified:

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
     3  `U+4E09 <https://codepoints.net/U+4E09>`_  '\\u4e09'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E09
     4  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe4\xb8\x89\xe6\x9d\xa1|\\n12345678|\\n"
        第十三条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width -12.

.. _LinuxFramebufferlangNuosu:

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================
     1  `U+A1EC <https://codepoints.net/U+A1EC>`_  '\\ua1ec'  Lo                  2  YI SYLLABLE GO
     2  `U+A3E2 <https://codepoints.net/U+A3E2>`_  '\\ua3e2'  Lo                  2  YI SYLLABLE JI
     3  `U+A1CB <https://codepoints.net/U+A1CB>`_  '\\ua1cb'  Lo                  2  YI SYLLABLE LEX
     4  `U+A1EC <https://codepoints.net/U+A1EC>`_  '\\ua1ec'  Lo                  2  YI SYLLABLE GO
     5  `U+A052 <https://codepoints.net/U+A052>`_  '\\ua052'  Lo                  2  YI SYLLABLE PY
     6  `U+A400 <https://codepoints.net/U+A400>`_  '\\ua400'  Lo                  2  YI SYLLABLE QIET
     7  `U+A00B <https://codepoints.net/U+A00B>`_  '\\ua00b'  Lo                  2  YI SYLLABLE AP
     8  `U+A246 <https://codepoints.net/U+A246>`_  '\\ua246'  Lo                  2  YI SYLLABLE HXIT
   ===  =========================================  =========  ==========  =========  ================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x87\xac\xea\x8f\xa2\xea\x87\x8b\xea\x87\xac\xea\x81\x92\xea\x90\x80\xea\x80\x8b\xea\x89\x86|\\n1234567890123456|\\n"
        ꇬꏢꇋꇬꁒꐀꀋꉆ|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *Linux Framebuffer* measures width -14.

.. _LinuxFramebufferlangDangme:

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     3  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x94\xcc\x81|\\n12|\\n"
        nɔ́|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *Linux Framebuffer* measures width 3.

.. _LinuxFramebufferlangDagaareSouthern:

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     3  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     4  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     5  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ku\xcc\x83u\xcc\x83|\\n123|\\n"
        kũũ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangJapanese:

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
     2  `U+9650 <https://codepoints.net/U+9650>`_  '\\u9650'  Lo                  2  CJK UNIFIED IDEOGRAPH-9650
     3  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
     4  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     5  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
     6  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
     7  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     8  `U+5185 <https://codepoints.net/U+5185>`_  '\\u5185'  Lo                  2  CJK UNIFIED IDEOGRAPH-5185
     9  `U+88C1 <https://codepoints.net/U+88C1>`_  '\\u88c1'  Lo                  2  CJK UNIFIED IDEOGRAPH-88C1
    10  `U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
    11  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    12  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
    13  `U+3088 <https://codepoints.net/U+3088>`_  '\\u3088'  Lo                  2  HIRAGANA LETTER YO
    14  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
    15  `U+52B9 <https://codepoints.net/U+52B9>`_  '\\u52b9'  Lo                  2  CJK UNIFIED IDEOGRAPH-52B9
    16  `U+679C <https://codepoints.net/U+679C>`_  '\\u679c'  Lo                  2  CJK UNIFIED IDEOGRAPH-679C
    17  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    18  `U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
    19  `U+6551 <https://codepoints.net/U+6551>`_  '\\u6551'  Lo                  2  CJK UNIFIED IDEOGRAPH-6551
    20  `U+6E08 <https://codepoints.net/U+6E08>`_  '\\u6e08'  Lo                  2  CJK UNIFIED IDEOGRAPH-6E08
    21  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
    22  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    23  `U+3051 <https://codepoints.net/U+3051>`_  '\\u3051'  Lo                  2  HIRAGANA LETTER KE
    24  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
    25  `U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
    26  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    27  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
    28  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
    29  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
    30  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 30


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xa8\xa9\xe9\x99\x90\xe3\x82\x92\xe6\x9c\x89\xe3\x81\x99\xe3\x82\x8b\xe5\x9b\xbd\xe5\x86\x85\xe8\xa3\x81\xe5\x88\xa4\xe6\x89\x80\xe3\x81\xab\xe3\x82\x88\xe3\x82\x8b\xe5\x8a\xb9\xe6\x9e\x9c\xe7\x9a\x84\xe3\x81\xaa\xe6\x95\x91\xe6\xb8\x88\xe3\x82\x92\xe5\x8f\x97\xe3\x81\x91\xe3\x82\x8b\xe6\xa8\xa9\xe5\x88\xa9\xe3\x82\x92\xe6\x9c\x89\xe3\x81\x99\xe3\x82\x8b|\\n123456789012345678901234567890123456789012345678901234567890|\\n"
        権限を有する国内裁判所による効果的な救済を受ける権利を有する|
        123456789012345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 60,
  while *Linux Framebuffer* measures width 0.

.. _LinuxFramebufferlangJapaneseOsaka:

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
     2  `U+9650 <https://codepoints.net/U+9650>`_  '\\u9650'  Lo                  2  CJK UNIFIED IDEOGRAPH-9650
     3  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
     4  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     5  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
     6  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
     7  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     8  `U+5185 <https://codepoints.net/U+5185>`_  '\\u5185'  Lo                  2  CJK UNIFIED IDEOGRAPH-5185
     9  `U+88C1 <https://codepoints.net/U+88C1>`_  '\\u88c1'  Lo                  2  CJK UNIFIED IDEOGRAPH-88C1
    10  `U+5224 <https://codepoints.net/U+5224>`_  '\\u5224'  Lo                  2  CJK UNIFIED IDEOGRAPH-5224
    11  `U+6240 <https://codepoints.net/U+6240>`_  '\\u6240'  Lo                  2  CJK UNIFIED IDEOGRAPH-6240
    12  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
    13  `U+3088 <https://codepoints.net/U+3088>`_  '\\u3088'  Lo                  2  HIRAGANA LETTER YO
    14  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
    15  `U+52B9 <https://codepoints.net/U+52B9>`_  '\\u52b9'  Lo                  2  CJK UNIFIED IDEOGRAPH-52B9
    16  `U+679C <https://codepoints.net/U+679C>`_  '\\u679c'  Lo                  2  CJK UNIFIED IDEOGRAPH-679C
    17  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    18  `U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
    19  `U+6551 <https://codepoints.net/U+6551>`_  '\\u6551'  Lo                  2  CJK UNIFIED IDEOGRAPH-6551
    20  `U+6E08 <https://codepoints.net/U+6E08>`_  '\\u6e08'  Lo                  2  CJK UNIFIED IDEOGRAPH-6E08
    21  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
    22  `U+53D7 <https://codepoints.net/U+53D7>`_  '\\u53d7'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D7
    23  `U+3051 <https://codepoints.net/U+3051>`_  '\\u3051'  Lo                  2  HIRAGANA LETTER KE
    24  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
    25  `U+6A29 <https://codepoints.net/U+6A29>`_  '\\u6a29'  Lo                  2  CJK UNIFIED IDEOGRAPH-6A29
    26  `U+5229 <https://codepoints.net/U+5229>`_  '\\u5229'  Lo                  2  CJK UNIFIED IDEOGRAPH-5229
    27  `U+3092 <https://codepoints.net/U+3092>`_  '\\u3092'  Lo                  2  HIRAGANA LETTER WO
    28  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
    29  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
    30  `U+308B <https://codepoints.net/U+308B>`_  '\\u308b'  Lo                  2  HIRAGANA LETTER RU
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 30


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\xa8\xa9\xe9\x99\x90\xe3\x82\x92\xe6\x9c\x89\xe3\x81\x99\xe3\x82\x8b\xe5\x9b\xbd\xe5\x86\x85\xe8\xa3\x81\xe5\x88\xa4\xe6\x89\x80\xe3\x81\xab\xe3\x82\x88\xe3\x82\x8b\xe5\x8a\xb9\xe6\x9e\x9c\xe7\x9a\x84\xe3\x81\xaa\xe6\x95\x91\xe6\xb8\x88\xe3\x82\x92\xe5\x8f\x97\xe3\x81\x91\xe3\x82\x8b\xe6\xa8\xa9\xe5\x88\xa9\xe3\x82\x92\xe6\x9c\x89\xe3\x81\x99\xe3\x82\x8b|\\n123456789012345678901234567890123456789012345678901234567890|\\n"
        権限を有する国内裁判所による効果的な救済を受ける権利を有する|
        123456789012345678901234567890123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 60,
  while *Linux Framebuffer* measures width 0.

.. _LinuxFramebufferlangSererSine:

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
     2  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     6  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "p\xcc\x81asil|\\n12345|\\n"
        ṕasil|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     2  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     3  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     4  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ak\xc9\x94\xcc\x81n|\\n1234|\\n"
        akɔ́n|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *Linux Framebuffer* measures width 5.

.. _LinuxFramebufferlangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'    Ll                  1  LATIN SMALL LETTER E WITH GRAVE
     2  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     3  `U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
     4  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     5  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     6  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     7  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     8  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xa8gb\xc9\x9b\xcc\x80m\xc9\x9b\xcc\x80|\\n123456|\\n"
        ègbɛ̀mɛ̀|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Linux Framebuffer* measures width 8.

.. _LinuxFramebufferlangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+0633 <https://codepoints.net/U+0633>`_  '\\u0633'  Lo                  1  ARABIC LETTER SEEN
     3  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     4  `U+0633 <https://codepoints.net/U+0633>`_  '\\u0633'  Lo                  1  ARABIC LETTER SEEN
     5  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     6  `U+064B <https://codepoints.net/U+064B>`_  '\\u064b'  Mn                  0  ARABIC FATHATAN
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd8\xb3\xd8\xa7\xd8\xb3\xd8\xa7\xd9\x8b|\\n12345|\\n"
        اساساً|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     3  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     4  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
     5  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     6  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "b\xc9\x94\xcc\x83\xc5\x8b\xc9\x94.|\\n12345|\\n"
        bɔ̃ŋɔ.|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *Linux Framebuffer* measures width 6.

.. _LinuxFramebufferlangColorado:

Colorado
^^^^^^^^

Sequence of language *Colorado* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     5  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     6  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yalachi|\\n1234567|\\n"
        yalachi|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *Linux Framebuffer* measures width -1.

.. _LinuxFramebufferlangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+064F <https://codepoints.net/U+064F>`_  '\\u064f'  Mn                  0  ARABIC DAMMA
     3  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
     4  `U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x8f\xd8\xaa\xdb\x92|\\n123|\\n"
        اُتے|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *Linux Framebuffer* measures width 4.

.. _LinuxFramebufferlangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+CD08 <https://codepoints.net/U+CD08>`_  '\\ucd08'  Lo                  2  HANGUL SYLLABLE CO
     2  `U+ACFC <https://codepoints.net/U+ACFC>`_  '\\uacfc'  Lo                  2  HANGUL SYLLABLE GWA
     3  `U+D558 <https://codepoints.net/U+D558>`_  '\\ud558'  Lo                  2  HANGUL SYLLABLE HA
     4  `U+C9C0 <https://codepoints.net/U+C9C0>`_  '\\uc9c0'  Lo                  2  HANGUL SYLLABLE JI
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\xb4\x88\xea\xb3\xbc\xed\x95\x98\xec\xa7\x80|\\n12345678|\\n"
        초과하지|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *Linux Framebuffer* measures width 1.

.. _LinuxFramebufferlangKorean:

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+C644 <https://codepoints.net/U+C644>`_  '\\uc644'  Lo                  2  HANGUL SYLLABLE WAN
     2  `U+C804 <https://codepoints.net/U+C804>`_  '\\uc804'  Lo                  2  HANGUL SYLLABLE JEON
     3  `U+D788 <https://codepoints.net/U+D788>`_  '\\ud788'  Lo                  2  HANGUL SYLLABLE HI
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x99\x84\xec\xa0\x84\xed\x9e\x88|\\n123456|\\n"
        완전히|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *Linux Framebuffer* measures width -2.

.. _LinuxFramebufferdecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

This Terminal does not appear capable of reporting about any DEC Private modes.

.. _LinuxFramebufferreproduce:

Reproduction
++++++++++++

To reproduce these results for *Linux Framebuffer*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --save-yaml=linux-6.14.0-33-fbdev.yaml \
        --limit-codepoints=5000 \
        --limit-words=5000 \
        --limit-errors=1000

.. _LinuxFramebuffertime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **31.67 seconds** (31s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
