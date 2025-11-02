.. _kitty:

kitty
-----


Tested Software version 0.43.1 on Linux
Full results available at ucs-detect_ repository path
`data/linux-kitty-0.43.1.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-kitty-0.43.1.yaml>`_

.. _kittyscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *kitty*:

.. table::
   :class: sphinx-datatable

   ============  ===========  ==============  ======================================================
   Score Type    Raw Score    Scaled Score    Calculation
   ============  ===========  ==============  ======================================================
   WIDE          90.91%       88.4%           (version_index / total_versions) × (pct_success / 100)
   ZWJ           75.00%       100.0%          (version_index / total_versions) × (pct_success / 100)
   LANG          93.81%       90.2%           geometric_mean(language_percentages)
   VS16          100.00%      100.0%          pct_success / 100
   VS15          100.00%      100.0%          pct_success / 100
   DEC Modes     11.95%       5.5%            modes_changeable / total_modes
   TIME          849.99s      42.9%           1 - ((elapsed - min) / (max - min)) [inverse]
   ============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 78.61%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 100.0%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _kittywide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for kitty appears to be 
**16.0.0**, this is from a summary of the following
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
   '15.1.0'            0          5  100.0%
   '16.0.0'            0        198  100.0%
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
  while *kitty* measures width 1.

.. _kittyzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *kitty* appears to be 
**17.0**, this is from a summary of the following
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
   '17.0'              0        130  100.0%
   =========  ==========  =========  =============

.. _kittyvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *kitty* is 0 errors
out of 213 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.

.. _kittyvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *kitty* is 0 errors
out of 158 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-15 tested were successful.

.. _kittylang:

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
   :ref:`Malayalam <kittylangMalayalam>`                                               1000       1333  25.0%
   :ref:`Sanskrit <kittylangSanskrit>`                                                  619       1000  38.1%
   :ref:`Telugu <kittylangTelugu>`                                                      596       1129  47.2%
   :ref:`Marathi <kittylangMarathi>`                                                    664       1614  58.9%
   :ref:`Bengali <kittylangBengali>`                                                    508       1413  64.0%
   :ref:`Tamang, Eastern <kittylangTamangEastern>`                                       16         45  64.4%
   :ref:`Nepali <kittylangNepali>`                                                      492       1385  64.5%
   :ref:`Maithili <kittylangMaithili>`                                                  498       1519  67.2%
   :ref:`Gujarati <kittylangGujarati>`                                                  395       1536  74.3%
   :ref:`Hindi <kittylangHindi>`                                                        518       2128  75.7%
   :ref:`Lao <kittylangLao>`                                                             81        426  81.0%
   :ref:`Thai (2) <kittylangThai2>`                                                      58        313  81.5%
   :ref:`Thai <kittylangThai>`                                                           55        341  83.9%
   :ref:`Magahi <kittylangMagahi>`                                                      263       1716  84.7%
   :ref:`Bhojpuri <kittylangBhojpuri>`                                                  248       1737  85.7%
   :ref:`Sinhala <kittylangSinhala>`                                                    112       1655  93.2%
   :ref:`Chinese, Wu <kittylangChineseWu>`                                                5        211  97.6%
   :ref:`Chinese, Mandarin (Beijing) <kittylangChineseMandarinBeijing>`                   5        212  97.6%
   :ref:`Japanese (Osaka) <kittylangJapaneseOsaka>`                                       7        308  97.7%
   :ref:`Chinese, Mandarin (Simplified) <kittylangChineseMandarinSimplified>`             5        225  97.8%
   :ref:`Vietnamese (Han nom) <kittylangVietnameseHannom>`                                4        199  98.0%
   :ref:`Japanese <kittylangJapanese>`                                                    6        299  98.0%
   :ref:`(Jinan) <kittylangJinan>`                                                        4        211  98.1%
   :ref:`Chinese, Mandarin (Guiyang) <kittylangChineseMandarinGuiyang>`                   4        211  98.1%
   :ref:`Chinese, Hakka <kittylangChineseHakka>`                                          4        212  98.1%
   :ref:`Chinese, Mandarin (Nanjing) <kittylangChineseMandarinNanjing>`                   4        212  98.1%
   :ref:`Chinese, Mandarin (Tianjin) <kittylangChineseMandarinTianjin>`                   4        212  98.1%
   :ref:`Chinese, Xiang <kittylangChineseXiang>`                                          4        212  98.1%
   :ref:`Japanese (Tokyo) <kittylangJapaneseTokyo>`                                       5        320  98.4%
   :ref:`Chinese, Mandarin (Harbin) <kittylangChineseMandarinHarbin>`                     3        210  98.6%
   :ref:`Chinese, Yue <kittylangChineseYue>`                                              3        210  98.6%
   :ref:`Chinese, Gan <kittylangChineseGan>`                                              3        211  98.6%
   :ref:`Chinese, Jinyu <kittylangChineseJinyu>`                                          3        212  98.6%
   :ref:`Chinese, Min Nan <kittylangChineseMinNan>`                                       3        212  98.6%
   :ref:`Nuosu <kittylangNuosu>`                                                          3        230  98.7%
   :ref:`Chinese, Mandarin (Traditional) <kittylangChineseMandarinTraditional>`           2        210  99.0%
   :ref:`Khmer, Central <kittylangKhmerCentral>`                                          5        528  99.1%
   :ref:`Khün <kittylangKhn>`                                                             4        442  99.1%
   :ref:`Chickasaw <kittylangChickasaw>`                                                  4        554  99.3%
   :ref:`Bora <kittylangBora>`                                                           11       1598  99.3%
   :ref:`Gumuz <kittylangGumuz>`                                                          8       1283  99.4%
   :ref:`Shipibo-Conibo <kittylangShipiboConibo>`                                        15       2540  99.4%
   :ref:`Nanai <kittylangNanai>`                                                          7       1207  99.4%
   :ref:`Navajo <kittylangNavajo>`                                                        9       1600  99.4%
   :ref:`Orok <kittylangOrok>`                                                            7       1245  99.4%
   :ref:`Evenki <kittylangEvenki>`                                                        5        899  99.4%
   :ref:`Amarakaeri <kittylangAmarakaeri>`                                                8       1446  99.4%
   :ref:`Yaneshaʼ <kittylangYanesha>`                                                    14       2536  99.4%
   :ref:`Shan <kittylangShan>`                                                            5        915  99.5%
   :ref:`Siona <kittylangSiona>`                                                          8       1492  99.5%
   :ref:`Gilyak <kittylangGilyak>`                                                        8       1504  99.5%
   :ref:`Veps <kittylangVeps>`                                                            7       1323  99.5%
   :ref:`Mon <kittylangMon>`                                                              5        946  99.5%
   :ref:`Korean <kittylangKorean>`                                                        6       1185  99.5%
   :ref:`South Azerbaijani <kittylangSouthAzerbaijani>`                                   7       1396  99.5%
   :ref:`Sanskrit (Grantha) <kittylangSanskritGrantha>`                                   5       1006  99.5%
   :ref:`Secoya <kittylangSecoya>`                                                        7       1409  99.5%
   :ref:`Burmese <kittylangBurmese>`                                                      6       1223  99.5%
   :ref:`Tamil (Sri Lanka) <kittylangTamilSriLanka>`                                      6       1261  99.5%
   :ref:`Tamil <kittylangTamil>`                                                          6       1262  99.5%
   :ref:`Colorado <kittylangColorado>`                                                    6       1263  99.5%
   :ref:`(Yeonbyeon) <kittylangYeonbyeon>`                                                5       1061  99.5%
   :ref:`Kannada <kittylangKannada>`                                                      5       1080  99.5%
   :ref:`Yiddish, Eastern <kittylangYiddishEastern>`                                      8       1775  99.5%
   :ref:`Tem <kittylangTem>`                                                              7       1659  99.6%
   :ref:`Catalan (2) <kittylangCatalan2>`                                                 8       1909  99.6%
   :ref:`Maldivian <kittylangMaldivian>`                                                  8       1918  99.6%
   :ref:`Mirandese <kittylangMirandese>`                                                  8       1966  99.6%
   :ref:`Éwé <kittylangw>`                                                                9       2230  99.6%
   :ref:`Picard <kittylangPicard>`                                                        8       2024  99.6%
   :ref:`Ticuna <kittylangTicuna>`                                                        8       2048  99.6%
   :ref:`Kabyle <kittylangKabyle>`                                                        7       1815  99.6%
   :ref:`Lingala (tones) <kittylangLingalatones>`                                         7       1818  99.6%
   :ref:`Tamazight, Central Atlas <kittylangTamazightCentralAtlas>`                       7       1822  99.6%
   :ref:`Fur <kittylangFur>`                                                              7       1838  99.6%
   :ref:`Pular (Adlam) <kittylangPularAdlam>`                                             6       1613  99.6%
   :ref:`Arabic, Standard <kittylangArabicStandard>`                                      5       1348  99.6%
   :ref:`Mixtec, Metlatónoc <kittylangMixtecMetlatnoc>`                                   5       1367  99.6%
   :ref:`French (Welche) <kittylangFrenchWelche>`                                         7       1928  99.6%
   :ref:`Urdu <kittylangUrdu>`                                                            8       2237  99.6%
   :ref:`Urdu (2) <kittylangUrdu2>`                                                       8       2251  99.6%
   :ref:`Gen <kittylangGen>`                                                              8       2309  99.7%
   :ref:`Assyrian Neo-Aramaic <kittylangAssyrianNeoAramaic>`                              4       1160  99.7%
   :ref:`Javanese (Javanese) <kittylangJavaneseJavanese>`                                 5       1453  99.7%
   :ref:`Ga <kittylangGa>`                                                                7       2039  99.7%
   :ref:`Aja <kittylangAja>`                                                              7       2061  99.7%
   :ref:`Uduk <kittylangUduk>`                                                           11       3247  99.7%
   :ref:`Saint Lucian Creole French <kittylangSaintLucianCreoleFrench>`                   6       1777  99.7%
   :ref:`Maori (2) <kittylangMaori2>`                                                     8       2385  99.7%
   :ref:`Farsi, Western <kittylangFarsiWestern>`                                          6       1822  99.7%
   :ref:`Dinka, Northeastern <kittylangDinkaNortheastern>`                                5       1529  99.7%
   :ref:`Mòoré <kittylangMor>`                                                            8       2447  99.7%
   :ref:`Yoruba <kittylangYoruba>`                                                        8       2454  99.7%
   :ref:`Dari <kittylangDari>`                                                            6       1872  99.7%
   :ref:`Vietnamese <kittylangVietnamese>`                                                8       2502  99.7%
   :ref:`Ditammari <kittylangDitammari>`                                                  6       1882  99.7%
   :ref:`Dendi <kittylangDendi>`                                                          5       1569  99.7%
   :ref:`Mazahua Central <kittylangMazahuaCentral>`                                       5       1574  99.7%
   :ref:`Serer-Sine <kittylangSererSine>`                                                 5       1596  99.7%
   :ref:`Lamnso' <kittylangLamnso>`                                                       7       2237  99.7%
   :ref:`Pashto, Northern <kittylangPashtoNorthern>`                                      7       2242  99.7%
   :ref:`Seraiki <kittylangSeraiki>`                                                      7       2242  99.7%
   :ref:`Belanda Viri <kittylangBelandaViri>`                                             7       2246  99.7%
   :ref:`Dagaare, Southern <kittylangDagaareSouthern>`                                    8       2582  99.7%
   :ref:`Baatonum <kittylangBaatonum>`                                                    6       1939  99.7%
   :ref:`Bamun <kittylangBamun>`                                                          7       2285  99.7%
   :ref:`Waama <kittylangWaama>`                                                          3       1000  99.7%
   :ref:`Panjabi, Western <kittylangPanjabiWestern>`                                      7       2419  99.7%
   :ref:`Chinantec, Chiltepec <kittylangChinantecChiltepec>`                              5       1729  99.7%
   :ref:`Fon <kittylangFon>`                                                              7       2520  99.7%
   :ref:`Chakma <kittylangChakma>`                                                        4       1444  99.7%
   :ref:`Dangme <kittylangDangme>`                                                        8       2912  99.7%
   :ref:`Otomi, Mezquital <kittylangOtomiMezquital>`                                      5       1849  99.7%
   :ref:`Tibetan, Central <kittylangTibetanCentral>`                                      7       3174  99.8%
   :ref:`Panjabi, Eastern <kittylangPanjabiEastern>`                                      5       2293  99.8%
   :ref:`Tai Dam <kittylangTaiDam>`                                                       5       2386  99.8%
   :ref:`Dzongkha <kittylangDzongkha>`                                                    6       3060  99.8%
   ============================================================================  ==========  =========  =============

.. _kittylangMalayalam:

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
  while *kitty* measures width 12.

.. _kittylangSanskrit:

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
     2  `U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
     3  `U+091A <https://codepoints.net/U+091A>`_  '\\u091a'  Lo                  1  DEVANAGARI LETTER CA
     4  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     5  `U+0936 <https://codepoints.net/U+0936>`_  '\\u0936'  Lo                  1  DEVANAGARI LETTER SHA
     6  `U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
     7  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     8  `U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
     9  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
    10  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xaa\xe0\xa4\x82\xe0\xa4\x9a\xe0\xa4\xbe\xe0\xa4\xb6\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa4\xae\xe0\xa4\xbe|\\n123456|\\n"
        पंचाशत्तमा|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 5.

.. _kittylangTelugu:

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
  while *kitty* measures width 7.

.. _kittylangMarathi:

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
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x9c\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe|\\n12|\\n"
        ज्या|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width 1.

.. _kittylangBengali:

Bengali
^^^^^^^

Sequence of language *Bengali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+09B8 <https://codepoints.net/U+09B8>`_  '\\u09b8'  Lo                  1  BENGALI LETTER SA
     2  `U+09BE <https://codepoints.net/U+09BE>`_  '\\u09be'  Mc                  0  BENGALI VOWEL SIGN AA
     3  `U+09B0 <https://codepoints.net/U+09B0>`_  '\\u09b0'  Lo                  1  BENGALI LETTER RA
     4  `U+09CD <https://codepoints.net/U+09CD>`_  '\\u09cd'  Mn                  0  BENGALI SIGN VIRAMA
     5  `U+09AC <https://codepoints.net/U+09AC>`_  '\\u09ac'  Lo                  1  BENGALI LETTER BA
     6  `U+099C <https://codepoints.net/U+099C>`_  '\\u099c'  Lo                  1  BENGALI LETTER JA
     7  `U+09A8 <https://codepoints.net/U+09A8>`_  '\\u09a8'  Lo                  1  BENGALI LETTER NA
     8  `U+09C0 <https://codepoints.net/U+09C0>`_  '\\u09c0'  Mc                  0  BENGALI VOWEL SIGN II
     9  `U+09A8 <https://codepoints.net/U+09A8>`_  '\\u09a8'  Lo                  1  BENGALI LETTER NA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\xb8\xe0\xa6\xbe\xe0\xa6\xb0\xe0\xa7\x8d\xe0\xa6\xac\xe0\xa6\x9c\xe0\xa6\xa8\xe0\xa7\x80\xe0\xa6\xa8|\\n123456|\\n"
        সার্বজনীন|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 5.

.. _kittylangTamangEastern:

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
  while *kitty* measures width 2.

.. _kittylangNepali:

Nepali
^^^^^^

Sequence of language *Nepali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     2  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
     3  `U+0936 <https://codepoints.net/U+0936>`_  '\\u0936'  Lo                  1  DEVANAGARI LETTER SHA
     4  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     5  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     6  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     7  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     8  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     9  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    10  `U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
    11  `U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb5\xe0\xa4\xbf\xe0\xa4\xb6\xe0\xa5\x8d\xe0\xa4\xb5\xe0\xa4\xb5\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe\xe0\xa4\xaa\xe0\xa5\x80|\\n123456|\\n"
        विश्वव्यापी|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 4.

.. _kittylangMaithili:

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
  while *kitty* measures width 4.

.. _kittylangGujarati:

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0AB5 <https://codepoints.net/U+0AB5>`_  '\\u0ab5'  Lo                  1  GUJARATI LETTER VA
     2  `U+0ABF <https://codepoints.net/U+0ABF>`_  '\\u0abf'  Mc                  0  GUJARATI VOWEL SIGN I
     3  `U+0AB6 <https://codepoints.net/U+0AB6>`_  '\\u0ab6'  Lo                  1  GUJARATI LETTER SHA
     4  `U+0ACD <https://codepoints.net/U+0ACD>`_  '\\u0acd'  Mn                  0  GUJARATI SIGN VIRAMA
     5  `U+0AB5 <https://codepoints.net/U+0AB5>`_  '\\u0ab5'  Lo                  1  GUJARATI LETTER VA
     6  `U+0AB5 <https://codepoints.net/U+0AB5>`_  '\\u0ab5'  Lo                  1  GUJARATI LETTER VA
     7  `U+0ACD <https://codepoints.net/U+0ACD>`_  '\\u0acd'  Mn                  0  GUJARATI SIGN VIRAMA
     8  `U+0AAF <https://codepoints.net/U+0AAF>`_  '\\u0aaf'  Lo                  1  GUJARATI LETTER YA
     9  `U+0ABE <https://codepoints.net/U+0ABE>`_  '\\u0abe'  Mc                  0  GUJARATI VOWEL SIGN AA
    10  `U+0AAA <https://codepoints.net/U+0AAA>`_  '\\u0aaa'  Lo                  1  GUJARATI LETTER PA
    11  `U+0AC0 <https://codepoints.net/U+0AC0>`_  '\\u0ac0'  Mc                  0  GUJARATI VOWEL SIGN II
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\xb5\xe0\xaa\xbf\xe0\xaa\xb6\xe0\xab\x8d\xe0\xaa\xb5\xe0\xaa\xb5\xe0\xab\x8d\xe0\xaa\xaf\xe0\xaa\xbe\xe0\xaa\xaa\xe0\xab\x80|\\n123456|\\n"
        વિશ્વવ્યાપી|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 4.

.. _kittylangHindi:

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

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
  while *kitty* measures width 4.

.. _kittylangLao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0EA7 <https://codepoints.net/U+0EA7>`_  '\\u0ea7'  Lo                  1  LAO LETTER WO
     2  `U+0EB4 <https://codepoints.net/U+0EB4>`_  '\\u0eb4'  Mn                  0  LAO VOWEL SIGN I
     3  `U+0E88 <https://codepoints.net/U+0E88>`_  '\\u0e88'  Lo                  1  LAO LETTER CO
     4  `U+0EB2 <https://codepoints.net/U+0EB2>`_  '\\u0eb2'  Lo                  1  LAO VOWEL SIGN AA
     5  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
     6  `U+0EAA <https://codepoints.net/U+0EAA>`_  '\\u0eaa'  Lo                  1  LAO LETTER SO SUNG
     7  `U+0EB5 <https://codepoints.net/U+0EB5>`_  '\\u0eb5'  Mn                  0  LAO VOWEL SIGN II
     8  `U+0EC8 <https://codepoints.net/U+0EC8>`_  '\\u0ec8'  Mn                  0  LAO TONE MAI EK
     9  `U+0E87 <https://codepoints.net/U+0E87>`_  '\\u0e87'  Lo                  1  LAO LETTER NGO
    10  `U+0EAA <https://codepoints.net/U+0EAA>`_  '\\u0eaa'  Lo                  1  LAO LETTER SO SUNG
    11  `U+0EB3 <https://codepoints.net/U+0EB3>`_  '\\u0eb3'  Lo                  1  LAO VOWEL SIGN AM
    12  `U+0E84 <https://codepoints.net/U+0E84>`_  '\\u0e84'  Lo                  1  LAO LETTER KHO TAM
    13  `U+0EB1 <https://codepoints.net/U+0EB1>`_  '\\u0eb1'  Mn                  0  LAO VOWEL SIGN MAI KAN
    14  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
    15  `U+0EC3 <https://codepoints.net/U+0EC3>`_  '\\u0ec3'  Lo                  1  LAO VOWEL SIGN AY
    16  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
    17  `U+0EC2 <https://codepoints.net/U+0EC2>`_  '\\u0ec2'  Lo                  1  LAO VOWEL SIGN O
    18  `U+0EAE <https://codepoints.net/U+0EAE>`_  '\\u0eae'  Lo                  1  LAO LETTER HO TAM
    19  `U+0E87 <https://codepoints.net/U+0E87>`_  '\\u0e87'  Lo                  1  LAO LETTER NGO
    20  `U+0EAE <https://codepoints.net/U+0EAE>`_  '\\u0eae'  Lo                  1  LAO LETTER HO TAM
    21  `U+0EBD <https://codepoints.net/U+0EBD>`_  '\\u0ebd'  Lo                  1  LAO SEMIVOWEL SIGN NYO
    22  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 22


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xba\xa7\xe0\xba\xb4\xe0\xba\x88\xe0\xba\xb2\xe0\xba\x99\xe0\xba\xaa\xe0\xba\xb5\xe0\xbb\x88\xe0\xba\x87\xe0\xba\xaa\xe0\xba\xb3\xe0\xba\x84\xe0\xba\xb1\xe0\xba\x99\xe0\xbb\x83\xe0\xba\x99\xe0\xbb\x82\xe0\xba\xae\xe0\xba\x87\xe0\xba\xae\xe0\xba\xbd\xe0\xba\x99|\\n123456789012345678|\\n"
        ວິຈານສີ່ງສຳຄັນໃນໂຮງຮຽນ|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *kitty* measures width 17.

.. _kittylangThai2:

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
     4  `U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
     5  `U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
     6  `U+0E48 <https://codepoints.net/U+0E48>`_  '\\u0e48'  Mn                  0  THAI CHARACTER MAI EK
     7  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
     8  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     9  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    10  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
    11  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
    12  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
    13  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    14  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    15  `U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
    16  `U+0E28 <https://codepoints.net/U+0E28>`_  '\\u0e28'  Lo                  1  THAI CHARACTER SO SALA
    17  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    18  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    19  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
    20  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    21  `U+0E4C <https://codepoints.net/U+0E4C>`_  '\\u0e4c'  Mn                  0  THAI CHARACTER THANTHAKHAT
    22  `U+0E28 <https://codepoints.net/U+0E28>`_  '\\u0e28'  Lo                  1  THAI CHARACTER SO SALA
    23  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    24  `U+0E35 <https://codepoints.net/U+0E35>`_  '\\u0e35'  Mn                  0  THAI CHARACTER SARA II
    25  `U+0E41 <https://codepoints.net/U+0E41>`_  '\\u0e41'  Lo                  1  THAI CHARACTER SARA AE
    26  `U+0E15 <https://codepoints.net/U+0E15>`_  '\\u0e15'  Lo                  1  THAI CHARACTER TO TAO
    27  `U+0E48 <https://codepoints.net/U+0E48>`_  '\\u0e48'  Mn                  0  THAI CHARACTER MAI EK
    28  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    29  `U+0E33 <https://codepoints.net/U+0E33>`_  '\\u0e33'  Lo                  1  THAI CHARACTER SARA AM
    30  `U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
    31  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    32  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    33  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 33


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb9\x82\xe0\xb8\x94\xe0\xb8\xa2\xe0\xb8\x97\xe0\xb8\xb5\xe0\xb9\x88\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb8\xad\xe0\xb8\xa1\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\xa8\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\x94\xe0\xb8\xb4\xe0\xb9\x8c\xe0\xb8\xa8\xe0\xb8\xa3\xe0\xb8\xb5\xe0\xb9\x81\xe0\xb8\x95\xe0\xb9\x88\xe0\xb8\x81\xe0\xb8\xb3\xe0\xb9\x80\xe0\xb8\x99\xe0\xb8\xb4\xe0\xb8\x94|\\n123456789012345678901234|\\n"
        โดยที่การยอมรับศักดิ์ศรีแต่กำเนิด|
        123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 24,
  while *kitty* measures width 23.

.. _kittylangThai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0E04 <https://codepoints.net/U+0E04>`_  '\\u0e04'  Lo                  1  THAI CHARACTER KHO KHWAI
     2  `U+0E33 <https://codepoints.net/U+0E33>`_  '\\u0e33'  Lo                  1  THAI CHARACTER SARA AM
     3  `U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
     4  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     5  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     6  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     7  `U+0E20 <https://codepoints.net/U+0E20>`_  '\\u0e20'  Lo                  1  THAI CHARACTER PHO SAMPHAO
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x84\xe0\xb8\xb3\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa0|\\n1234567|\\n"
        คำปรารภ|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *kitty* measures width 6.

.. _kittylangMagahi:

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     2  `U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
     3  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     4  `U+0941 <https://codepoints.net/U+0941>`_  '\\u0941'  Mn                  0  DEVANAGARI VOWEL SIGN U
     5  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     6  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     7  `U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa4\x82\xe0\xa4\xaf\xe0\xa5\x81\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xa4|\\n1234|\\n"
        संयुक्त|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width 3.

.. _kittylangBhojpuri:

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     2  `U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
     3  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     4  `U+0941 <https://codepoints.net/U+0941>`_  '\\u0941'  Mn                  0  DEVANAGARI VOWEL SIGN U
     5  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     6  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     7  `U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa4\x82\xe0\xa4\xaf\xe0\xa5\x81\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xa4|\\n1234|\\n"
        संयुक्त|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width 3.

.. _kittylangSinhala:

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
  while *kitty* measures width 6.

.. _kittylangChineseWu:

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
  while *kitty* measures width -20.

.. _kittylangChineseMandarinBeijing:

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
  while *kitty* measures width -4.

.. _kittylangJapaneseOsaka:

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
  while *kitty* measures width -20.

.. _kittylangChineseMandarinSimplified:

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+53D1 <https://codepoints.net/U+53D1>`_  '\\u53d1'  Lo                  2  CJK UNIFIED IDEOGRAPH-53D1
     2  `U+5E03 <https://codepoints.net/U+5E03>`_  '\\u5e03'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E03
     3  `U+8FD9 <https://codepoints.net/U+8FD9>`_  '\\u8fd9'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FD9
     4  `U+4E00 <https://codepoints.net/U+4E00>`_  '\\u4e00'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E00
     5  `U+4E16 <https://codepoints.net/U+4E16>`_  '\\u4e16'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E16
     6  `U+754C <https://codepoints.net/U+754C>`_  '\\u754c'  Lo                  2  CJK UNIFIED IDEOGRAPH-754C
     7  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     8  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     9  `U+5BA3 <https://codepoints.net/U+5BA3>`_  '\\u5ba3'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BA3
    10  `U+8A00 <https://codepoints.net/U+8A00>`_  '\\u8a00'  Lo                  2  CJK UNIFIED IDEOGRAPH-8A00
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x8f\x91\xe5\xb8\x83\xe8\xbf\x99\xe4\xb8\x80\xe4\xb8\x96\xe7\x95\x8c\xe4\xba\xba\xe6\x9d\x83\xe5\xae\xa3\xe8\xa8\x80|\\n12345678901234567890|\\n"
        发布这一世界人权宣言|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *kitty* measures width 16.

.. _kittylangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===========================
     1  `U+00025A9D <https://codepoints.net/U+00025A9D>`_  '\\U00025a9d'  Lo                  2  CJK UNIFIED IDEOGRAPH-25A9D
     2  `U+7BC4 <https://codepoints.net/U+7BC4>`_          '\\u7bc4'      Lo                  2  CJK UNIFIED IDEOGRAPH-7BC4
     3  `U+570D <https://codepoints.net/U+570D>`_          '\\u570d'      Lo                  2  CJK UNIFIED IDEOGRAPH-570D
     4  `U+570B <https://codepoints.net/U+570B>`_          '\\u570b'      Lo                  2  CJK UNIFIED IDEOGRAPH-570B
     5  `U+5BB6 <https://codepoints.net/U+5BB6>`_          '\\u5bb6'      Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
     6  `U+548D <https://codepoints.net/U+548D>`_          '\\u548d'      Lo                  2  CJK UNIFIED IDEOGRAPH-548D
     7  `U+570B <https://codepoints.net/U+570B>`_          '\\u570b'      Lo                  2  CJK UNIFIED IDEOGRAPH-570B
     8  `U+969B <https://codepoints.net/U+969B>`_          '\\u969b'      Lo                  2  CJK UNIFIED IDEOGRAPH-969B
   ===  =================================================  =============  ==========  =========  ===========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\xa5\xaa\x9d\xe7\xaf\x84\xe5\x9c\x8d\xe5\x9c\x8b\xe5\xae\xb6\xe5\x92\x8d\xe5\x9c\x8b\xe9\x9a\x9b|\\n1234567890123456|\\n"
        𥪝範圍國家咍國際|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *kitty* measures width -30.

.. _kittylangJapanese:

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
  while *kitty* measures width 50.

.. _kittylangJinan:

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
  while *kitty* measures width -20.

.. _kittylangChineseMandarinGuiyang:

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
  while *kitty* measures width 5.

.. _kittylangChineseHakka:

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
  while *kitty* measures width -20.

.. _kittylangChineseMandarinNanjing:

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
  while *kitty* measures width -22.

.. _kittylangChineseMandarinTianjin:

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
  while *kitty* measures width 9.

.. _kittylangChineseXiang:

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
  while *kitty* measures width -20.

.. _kittylangJapaneseTokyo:

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
  while *kitty* measures width -42.

.. _kittylangChineseMandarinHarbin:

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
  while *kitty* measures width -4.

.. _kittylangChineseYue:

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
  while *kitty* measures width -24.

.. _kittylangChineseGan:

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
  while *kitty* measures width -16.

.. _kittylangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

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
  while *kitty* measures width -20.

.. _kittylangChineseMinNan:

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
  while *kitty* measures width 14.

.. _kittylangNuosu:

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
  while *kitty* measures width 29.

.. _kittylangChineseMandarinTraditional:

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
  while *kitty* measures width 5.

.. _kittylangKhmerCentral:

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
  while *kitty* measures width -16.

.. _kittylangKhn:

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+1A3E <https://codepoints.net/U+1A3E>`_  '\\u1a3e'  Lo                  1  TAI THAM LETTER MA
     2  `U+1A66 <https://codepoints.net/U+1A66>`_  '\\u1a66'  Mn                  0  TAI THAM VOWEL SIGN II
     3  `U+1A48 <https://codepoints.net/U+1A48>`_  '\\u1a48'  Lo                  1  TAI THAM LETTER HIGH SA
     4  `U+1A6E <https://codepoints.net/U+1A6E>`_  '\\u1a6e'  Mc                  0  TAI THAM VOWEL SIGN E
     5  `U+1A41 <https://codepoints.net/U+1A41>`_  '\\u1a41'  Lo                  1  TAI THAM LETTER RA
     6  `U+1A66 <https://codepoints.net/U+1A66>`_  '\\u1a66'  Mn                  0  TAI THAM VOWEL SIGN II
     7  `U+1A3D <https://codepoints.net/U+1A3D>`_  '\\u1a3d'  Lo                  1  TAI THAM LETTER LOW PHA
     8  `U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
     9  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    10  `U+1A37 <https://codepoints.net/U+1A37>`_  '\\u1a37'  Lo                  1  TAI THAM LETTER BA
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xbe\xe1\xa9\xa6\xe1\xa9\x88\xe1\xa9\xae\xe1\xa9\x81\xe1\xa9\xa6\xe1\xa8\xbd\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xb7|\\n12345|\\n"
        ᨾᩦᩈᩮᩁᩦᨽᩣ᩠ᨷ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *kitty* measures width -17.

.. _kittylangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     6  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     8  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nannaka\xcc\xb1|\\n1234567|\\n"
        nannaka̱|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *kitty* measures width -16.

.. _kittylangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     5  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "muur\xc3\xa1|\\n12345|\\n"
        muurá|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *kitty* measures width -3.

.. _kittylangGumuz:

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
  while *kitty* measures width -1.

.. _kittylangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004A <https://codepoints.net/U+004A>`_  'J'       Lu                  1  LATIN CAPITAL LETTER J
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Jascara|\\n1234567|\\n"
        Jascara|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *kitty* measures width 2.

.. _kittylangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
     2  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     3  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     4  `U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x82\xd1\x8d\xd0\xb4\xd0\xb5|\\n1234|\\n"
        тэде|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width -1.

.. _kittylangNavajo:

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
  while *kitty* measures width -12.

.. _kittylangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+04E1 <https://codepoints.net/U+04E1>`_  '\\u04e1'  Ll                  1  CYRILLIC SMALL LETTER ABKHASIAN DZE
     2  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     3  `U+04C8 <https://codepoints.net/U+04C8>`_  '\\u04c8'  Ll                  1  CYRILLIC SMALL LETTER EN WITH HOOK
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd3\xa1\xd0\xb8\xd3\x88|\\n123|\\n"
        ӡиӈ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width -7.

.. _kittylangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     2  `U+044F <https://codepoints.net/U+044F>`_  '\\u044f'  Ll                  1  CYRILLIC SMALL LETTER YA
     3  `U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
     4  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     5  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     6  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb0\xd1\x8f\xd0\xb2\xd1\x80\xd0\xb8\xd1\x82|\\n123456|\\n"
        аяврит|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width -4.

.. _kittylangAmarakaeri:

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
  while *kitty* measures width -1.

.. _kittylangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'    Ll                  1  LATIN SMALL LETTER N WITH TILDE
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'    Ll                  1  LATIN SMALL LETTER N WITH TILDE
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     5  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     7  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xb1e\xc3\xb1t\xcc\x83ey|\\n123456|\\n"
        ñeñt̃ey|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width -7.

.. _kittylangShan:

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
  while *kitty* measures width -24.

.. _kittylangSiona:

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
  while *kitty* measures width -2.

.. _kittylangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     2  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     3  `U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
     4  `U+0433 <https://codepoints.net/U+0433>`_  '\\u0433'  Ll                  1  CYRILLIC SMALL LETTER GHE
     5  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     6  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbd\xd0\xb8\xd0\xb2\xd0\xb3\xd1\x83\xd0\xbd|\\n123456|\\n"
        нивгун|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width -7.

.. _kittylangVeps:

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
  while *kitty* measures width 5.

.. _kittylangMon:

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
  while *kitty* measures width 4.

.. _kittylangKorean:

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
  while *kitty* measures width -8.

.. _kittylangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ============================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     7  `U+0131 <https://codepoints.net/U+0131>`_  '\\u0131'  Ll                  1  LATIN SMALL LETTER DOTLESS I
     8  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     9  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ============================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "haklar\xc4\xb1na|\\n123456789|\\n"
        haklarına|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *kitty* measures width 4.

.. _kittylangSanskritGrantha:

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =====================
     1  `U+00011338 <https://codepoints.net/U+00011338>`_  '\\U00011338'  Lo                  1  GRANTHA LETTER SA
     2  `U+00011330 <https://codepoints.net/U+00011330>`_  '\\U00011330'  Lo                  1  GRANTHA LETTER RA
     3  `U+0001134D <https://codepoints.net/U+0001134D>`_  '\\U0001134d'  Mc                  0  GRANTHA SIGN VIRAMA
     4  `U+00011335 <https://codepoints.net/U+00011335>`_  '\\U00011335'  Lo                  1  GRANTHA LETTER VA
     5  `U+00011347 <https://codepoints.net/U+00011347>`_  '\\U00011347'  Mc                  0  GRANTHA VOWEL SIGN EE
   ===  =================================================  =============  ==========  =========  =====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xb8\xf0\x91\x8c\xb0\xf0\x91\x8d\x8d\xf0\x91\x8c\xb5\xf0\x91\x8d\x87|\\n123|\\n"
        𑌸𑌰𑍍𑌵𑍇|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width 0.

.. _kittylangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pa'ina|\\n123456|\\n"
        pa'ina|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 2.

.. _kittylangBurmese:

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
  while *kitty* measures width 0.

.. _kittylangTamilSriLanka:

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
     2  `U+0BCA <https://codepoints.net/U+0BCA>`_  '\\u0bca'  Mc                  0  TAMIL VOWEL SIGN O
     3  `U+0BA3 <https://codepoints.net/U+0BA3>`_  '\\u0ba3'  Lo                  1  TAMIL LETTER NNA
     4  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     5  `U+0B9F <https://codepoints.net/U+0B9F>`_  '\\u0b9f'  Lo                  1  TAMIL LETTER TTA
     6  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     7  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
     8  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     9  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    10  `U+0BA9 <https://codepoints.net/U+0BA9>`_  '\\u0ba9'  Lo                  1  TAMIL LETTER NNNA
    11  `U+0BB5 <https://codepoints.net/U+0BB5>`_  '\\u0bb5'  Lo                  1  TAMIL LETTER VA
    12  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    13  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
    14  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
    15  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    16  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
    17  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
    18  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
    19  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x95\xe0\xaf\x8a\xe0\xae\xa3\xe0\xaf\x8d\xe0\xae\x9f\xe0\xaf\x81\xe0\xae\xb3\xe0\xaf\x8d\xe0\xae\xb3\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xbe\xe0\xae\xa4\xe0\xae\xb2\xe0\xae\xbe\xe0\xae\xb2\xe0\xaf\x81\xe0\xae\xae\xe0\xaf\x8d|\\n12345678901|\\n"
        கொண்டுள்ளனவாதலாலும்|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *kitty* measures width 7.

.. _kittylangTamil:

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
     2  `U+0BCA <https://codepoints.net/U+0BCA>`_  '\\u0bca'  Mc                  0  TAMIL VOWEL SIGN O
     3  `U+0BA3 <https://codepoints.net/U+0BA3>`_  '\\u0ba3'  Lo                  1  TAMIL LETTER NNA
     4  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     5  `U+0B9F <https://codepoints.net/U+0B9F>`_  '\\u0b9f'  Lo                  1  TAMIL LETTER TTA
     6  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     7  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
     8  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     9  `U+0BB3 <https://codepoints.net/U+0BB3>`_  '\\u0bb3'  Lo                  1  TAMIL LETTER LLA
    10  `U+0BA9 <https://codepoints.net/U+0BA9>`_  '\\u0ba9'  Lo                  1  TAMIL LETTER NNNA
    11  `U+0BB5 <https://codepoints.net/U+0BB5>`_  '\\u0bb5'  Lo                  1  TAMIL LETTER VA
    12  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    13  `U+0BA4 <https://codepoints.net/U+0BA4>`_  '\\u0ba4'  Lo                  1  TAMIL LETTER TA
    14  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
    15  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
    16  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
    17  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
    18  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
    19  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 19


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x95\xe0\xaf\x8a\xe0\xae\xa3\xe0\xaf\x8d\xe0\xae\x9f\xe0\xaf\x81\xe0\xae\xb3\xe0\xaf\x8d\xe0\xae\xb3\xe0\xae\xa9\xe0\xae\xb5\xe0\xae\xbe\xe0\xae\xa4\xe0\xae\xb2\xe0\xae\xbe\xe0\xae\xb2\xe0\xaf\x81\xe0\xae\xae\xe0\xaf\x8d|\\n12345678901|\\n"
        கொண்டுள்ளனவாதலாலும்|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *kitty* measures width 6.

.. _kittylangColorado:

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
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "mantaka|\\n1234567|\\n"
        mantaka|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *kitty* measures width 3.

.. _kittylangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+C0C1 <https://codepoints.net/U+C0C1>`_  '\\uc0c1'  Lo                  2  HANGUL SYLLABLE SANG
     2  `U+D638 <https://codepoints.net/U+D638>`_  '\\ud638'  Lo                  2  HANGUL SYLLABLE HO
     3  `U+B85C <https://codepoints.net/U+B85C>`_  '\\ub85c'  Lo                  2  HANGUL SYLLABLE RO
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x83\x81\xed\x98\xb8\xeb\xa1\x9c|\\n123456|\\n"
        상호로|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width -2.

.. _kittylangKannada:

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0CB8 <https://codepoints.net/U+0CB8>`_  '\\u0cb8'  Lo                  1  KANNADA LETTER SA
     2  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
     3  `U+0CB5 <https://codepoints.net/U+0CB5>`_  '\\u0cb5'  Lo                  1  KANNADA LETTER VA
     4  `U+0CA4 <https://codepoints.net/U+0CA4>`_  '\\u0ca4'  Lo                  1  KANNADA LETTER TA
     5  `U+0C82 <https://codepoints.net/U+0C82>`_  '\\u0c82'  Mc                  0  KANNADA SIGN ANUSVARA
     6  `U+0CA4 <https://codepoints.net/U+0CA4>`_  '\\u0ca4'  Lo                  1  KANNADA LETTER TA
     7  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
     8  `U+0CB0 <https://codepoints.net/U+0CB0>`_  '\\u0cb0'  Lo                  1  KANNADA LETTER RA
     9  `U+0CB0 <https://codepoints.net/U+0CB0>`_  '\\u0cb0'  Lo                  1  KANNADA LETTER RA
    10  `U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
    11  `U+0C97 <https://codepoints.net/U+0C97>`_  '\\u0c97'  Lo                  1  KANNADA LETTER GA
    12  `U+0CBF <https://codepoints.net/U+0CBF>`_  '\\u0cbf'  Mn                  0  KANNADA VOWEL SIGN I
    13  `U+0CAF <https://codepoints.net/U+0CAF>`_  '\\u0caf'  Lo                  1  KANNADA LETTER YA
    14  `U+0CC7 <https://codepoints.net/U+0CC7>`_  '\\u0cc7'  Mc                  0  KANNADA VOWEL SIGN EE
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\xb8\xe0\xb3\x8d\xe0\xb2\xb5\xe0\xb2\xa4\xe0\xb2\x82\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xb0\xe0\xb2\xb0\xe0\xb2\xbe\xe0\xb2\x97\xe0\xb2\xbf\xe0\xb2\xaf\xe0\xb3\x87|\\n12345678|\\n"
        ಸ್ವತಂತ್ರರಾಗಿಯೇ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *kitty* measures width 4.

.. _kittylangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================================
     1  `U+05F0 <https://codepoints.net/U+05F0>`_  '\\u05f0'  Lo                  1  HEBREW LIGATURE YIDDISH DOUBLE VAV
     2  `U+05D9 <https://codepoints.net/U+05D9>`_  '\\u05d9'  Lo                  1  HEBREW LETTER YOD
   ===  =========================================  =========  ==========  =========  ==================================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\xb0\xd7\x99|\\n12|\\n"
        װי|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width -2.

.. _kittylangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "b\xc3\xa1a|\\n123|\\n"
        báa|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width -5.

.. _kittylangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     3  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     6  `U+003B <https://codepoints.net/U+003B>`_  ';'       Po                  1  SEMICOLON
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ampli;|\\n123456|\\n"
        ampli;|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 3.

.. _kittylangMaldivian:

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0799 <https://codepoints.net/U+0799>`_  '\\u0799'  Lo                  1  THAANA LETTER HHAA
     2  `U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
     3  `U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
     4  `U+07B0 <https://codepoints.net/U+07B0>`_  '\\u07b0'  Mn                  0  THAANA SUKUN
     5  `U+07A4 <https://codepoints.net/U+07A4>`_  '\\u07a4'  Lo                  1  THAANA LETTER QAAFU
     6  `U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
     7  `U+078C <https://codepoints.net/U+078C>`_  '\\u078c'  Lo                  1  THAANA LETTER THAA
     8  `U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
     9  `U+0786 <https://codepoints.net/U+0786>`_  '\\u0786'  Lo                  1  THAANA LETTER KAAFU
    10  `U+07A7 <https://codepoints.net/U+07A7>`_  '\\u07a7'  Mn                  0  THAANA AABAAFILI
    11  `U+0787 <https://codepoints.net/U+0787>`_  '\\u0787'  Lo                  1  THAANA LETTER ALIFU
    12  `U+07A8 <https://codepoints.net/U+07A8>`_  '\\u07a8'  Mn                  0  THAANA IBIFILI
    13  `U+060C <https://codepoints.net/U+060C>`_  '\\u060c'  Po                  1  ARABIC COMMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x99\xde\xa6\xde\x87\xde\xb0\xde\xa4\xde\xaa\xde\x8c\xde\xa6\xde\x86\xde\xa7\xde\x87\xde\xa8\xd8\x8c|\\n1234567|\\n"
        ޙައްޤުތަކާއި،|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *kitty* measures width 4.

.. _kittylangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "cun|\\n123|\\n"
        cun|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width -7.

.. _kittylangw:

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
  while *kitty* measures width -8.

.. _kittylangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "d'|\\n12|\\n"
        d'|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width -4.

.. _kittylangTicuna:

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
  while *kitty* measures width 10.

.. _kittylangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

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
  while *kitty* measures width -5.

.. _kittylangLingalatones:

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
  while *kitty* measures width -3.

.. _kittylangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     5  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tlella|\\n123456|\\n"
        tlella|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 2.

.. _kittylangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     2  `U+00EE <https://codepoints.net/U+00EE>`_  '\\xee'   Ll                  1  LATIN SMALL LETTER I WITH CIRCUMFLEX
   ===  =========================================  ========  ==========  =========  ====================================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "g\xc3\xae|\\n12|\\n"
        gî|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width -3.

.. _kittylangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ========================
     1  `U+0001E934 <https://codepoints.net/U+0001E934>`_  '\\U0001e934'  Ll                  1  ADLAM SMALL LETTER YA
     2  `U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
     3  `U+0001E93C <https://codepoints.net/U+0001E93C>`_  '\\U0001e93c'  Ll                  1  ADLAM SMALL LETTER TU
     4  `U+0001E946 <https://codepoints.net/U+0001E946>`_  '\\U0001e946'  Mn                  0  ADLAM GEMINATION MARK
     5  `U+0001E922 <https://codepoints.net/U+0001E922>`_  '\\U0001e922'  Ll                  1  ADLAM SMALL LETTER ALIF
     6  `U+0001E944 <https://codepoints.net/U+0001E944>`_  '\\U0001e944'  Mn                  0  ADLAM ALIF LENGTHENER
     7  `U+0001E923 <https://codepoints.net/U+0001E923>`_  '\\U0001e923'  Ll                  1  ADLAM SMALL LETTER DAALI
     8  `U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
   ===  =================================================  =============  ==========  =========  ========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xb4\xf0\x9e\xa4\xab\xf0\x9e\xa4\xbc\xf0\x9e\xa5\x86\xf0\x9e\xa4\xa2\xf0\x9e\xa5\x84\xf0\x9e\xa4\xa3\xf0\x9e\xa4\xab|\\n123456|\\n"
        𞤴𞤫𞤼𞥆𞤢𞥄𞤣𞤫|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 1.

.. _kittylangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
     2  `U+0635 <https://codepoints.net/U+0635>`_  '\\u0635'  Lo                  1  ARABIC LETTER SAD
     3  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     4  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
     5  `U+0629 <https://codepoints.net/U+0629>`_  '\\u0629'  Lo                  1  ARABIC LETTER TEH MARBUTA
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa8\xd8\xb5\xd9\x88\xd8\xb1\xd8\xa9|\\n12345|\\n"
        بصورة|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *kitty* measures width -5.

.. _kittylangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tna|\\n123|\\n"
        tna|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width 0.

.. _kittylangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     2  `U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     4  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     5  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     7  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     8  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     9  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
    10  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
    11  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    12  `U+002D <https://codepoints.net/U+002D>`_  '-'        Pd                  1  HYPHEN-MINUS
    13  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
    14  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "l\xe2\x80\x99e\xcc\x80ge\xcc\x80djma-la|\\n123456789012|\\n"
        l’ègèdjma-la|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *kitty* measures width 7.

.. _kittylangUrdu:

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
  while *kitty* measures width 4.

.. _kittylangUrdu2:

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
  while *kitty* measures width 4.

.. _kittylangGen:

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
  while *kitty* measures width -3.

.. _kittylangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0726 <https://codepoints.net/U+0726>`_  '\\u0726'  Lo                  1  SYRIAC LETTER PE
     2  `U+0718 <https://codepoints.net/U+0718>`_  '\\u0718'  Lo                  1  SYRIAC LETTER WAW
     3  `U+072A <https://codepoints.net/U+072A>`_  '\\u072a'  Lo                  1  SYRIAC LETTER RISH
     4  `U+072B <https://codepoints.net/U+072B>`_  '\\u072b'  Lo                  1  SYRIAC LETTER SHIN
     5  `U+0718 <https://codepoints.net/U+0718>`_  '\\u0718'  Lo                  1  SYRIAC LETTER WAW
     6  `U+0722 <https://codepoints.net/U+0722>`_  '\\u0722'  Lo                  1  SYRIAC LETTER NUN
     7  `U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
     8  `U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\xa6\xdc\x98\xdc\xaa\xdc\xab\xdc\x98\xdc\xa2\xdc\x9d\xdc\x90|\\n12345678|\\n"
        ܦܘܪܫܘܢܝܐ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *kitty* measures width 5.

.. _kittylangJavaneseJavanese:

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
     4  `U+A9B8 <https://codepoints.net/U+A9B8>`_  '\\ua9b8'  Mn                  0  JAVANESE VOWEL SIGN SUKU
     5  `U+A9A9 <https://codepoints.net/U+A9A9>`_  '\\ua9a9'  Lo                  1  JAVANESE LETTER MA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\xb2\xea\xa6\xb8\xea\xa6\xa9\xea\xa6\xb8\xea\xa6\xa9|\\n123|\\n"
        ꦲꦸꦩꦸꦩ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width -10.

.. _kittylangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

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
  while *kitty* measures width -7.

.. _kittylangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     2  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     4  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     5  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     6  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     8  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     9  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
    10  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
    11  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
    12  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
    13  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "enukplankplan|\\n1234567890123|\\n"
        enukplankplan|
        1234567890123|

- python `wcwidth.wcswidth()`_ measures width 13,
  while *kitty* measures width 8.

.. _kittylangUduk:

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
  while *kitty* measures width -10.

.. _kittylangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "sa|\\n12|\\n"
        sa|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width -1.

.. _kittylangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "hoki|\\n1234|\\n"
        hoki|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width -7.

.. _kittylangFarsiWestern:

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
  while *kitty* measures width 3.

.. _kittylangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     2  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     3  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'    Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
     4  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "al\xc3\xab\xc5\x8b|\\n1234|\\n"
        alëŋ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width 0.

.. _kittylangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     6  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     7  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     8  `U+0269 <https://codepoints.net/U+0269>`_  '\\u0269'  Ll                  1  LATIN SMALL LETTER IOTA
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yelsegd\xc9\xa9|\\n12345678|\\n"
        yelsegdɩ|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *kitty* measures width 0.

.. _kittylangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+00C0 <https://codepoints.net/U+00C0>`_  '\\xc0'    Lu                  1  LATIN CAPITAL LETTER A WITH GRAVE
     2  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
     3  `U+1ECD <https://codepoints.net/U+1ECD>`_  '\\u1ecd'  Ll                  1  LATIN SMALL LETTER O WITH DOT BELOW
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\x80j\xe1\xbb\x8d|\\n123|\\n"
        Àjọ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width -1.

.. _kittylangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     2  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     3  `U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
     4  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdb\x8c\xd8\xa7\xd8\xa8\xd8\xaf|\\n1234|\\n"
        یابد|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width -1.

.. _kittylangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     2  `U+01B0 <https://codepoints.net/U+01B0>`_  '\\u01b0'  Ll                  1  LATIN SMALL LETTER U WITH HORN
     3  `U+0323 <https://codepoints.net/U+0323>`_  '\\u0323'  Mn                  0  COMBINING DOT BELOW
   ===  =========================================  =========  ==========  =========  ==============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "t\xc6\xb0\xcc\xa3|\\n12|\\n"
        tự|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width -3.

.. _kittylangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

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
  while *kitty* measures width -3.

.. _kittylangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "duwa|\\n1234|\\n"
        duwa|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width 2.

.. _kittylangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

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
  while *kitty* measures width -5.

.. _kittylangSererSine:

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
  while *kitty* measures width 3.

.. _kittylangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+00EC <https://codepoints.net/U+00EC>`_  '\\xec'   Ll                  1  LATIN SMALL LETTER I WITH GRAVE
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nji\xc3\xacn|\\n12345|\\n"
        njiìn|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *kitty* measures width 1.

.. _kittylangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x88|\\n12|\\n"
        او|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width -2.

.. _kittylangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0636 <https://codepoints.net/U+0636>`_  '\\u0636'  Lo                  1  ARABIC LETTER DAD
     2  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     3  `U+06CC <https://codepoints.net/U+06CC>`_  '\\u06cc'  Lo                  1  ARABIC LETTER FARSI YEH
     4  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xb6\xd9\x85\xdb\x8c\xd8\xb1|\\n1234|\\n"
        ضمیر|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width -2.

.. _kittylangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

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
  while *kitty* measures width -3.

.. _kittylangDagaareSouthern:

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004C <https://codepoints.net/U+004C>`_  'L'       Lu                  1  LATIN CAPITAL LETTER L
     2  `U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
     3  `U+004E <https://codepoints.net/U+004E>`_  'N'       Lu                  1  LATIN CAPITAL LETTER N
     4  `U+0047 <https://codepoints.net/U+0047>`_  'G'       Lu                  1  LATIN CAPITAL LETTER G
     5  `U+004E <https://codepoints.net/U+004E>`_  'N'       Lu                  1  LATIN CAPITAL LETTER N
     6  `U+0045 <https://codepoints.net/U+0045>`_  'E'       Lu                  1  LATIN CAPITAL LETTER E
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "LANGNE|\\n123456|\\n"
        LANGNE|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *kitty* measures width 0.

.. _kittylangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     5  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kpuro|\\n12345|\\n"
        kpuro|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *kitty* measures width 0.

.. _kittylangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yire|\\n1234|\\n"
        yire|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *kitty* measures width -2.

.. _kittylangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

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
  while *kitty* measures width 0.

.. _kittylangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
     2  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xaf\xd8\xa7|\\n12|\\n"
        دا|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width -2.

.. _kittylangChinantecChiltepec:

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
  while *kitty* measures width -3.

.. _kittylangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================
     1  `U+0256 <https://codepoints.net/U+0256>`_  '\\u0256'  Ll                  1  LATIN SMALL LETTER D WITH TAIL
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     4  `U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
     5  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  =========  ==========  =========  ==============================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc9\x96okpo|\\n12345|\\n"
        ɖokpo|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *kitty* measures width -1.

.. _kittylangChakma:

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
  while *kitty* measures width -4.

.. _kittylangDangme:

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
  while *kitty* measures width -2.

.. _kittylangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nu|\\n12|\\n"
        nu|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width 0.

.. _kittylangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0F54 <https://codepoints.net/U+0F54>`_  '\\u0f54'  Lo                  1  TIBETAN LETTER PA
     2  `U+0F60 <https://codepoints.net/U+0F60>`_  '\\u0f60'  Lo                  1  TIBETAN LETTER -A
     3  `U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x94\xe0\xbd\xa0\xe0\xbd\xb2|\\n12|\\n"
        པའི|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *kitty* measures width 0.

.. _kittylangPanjabiEastern:

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0A39 <https://codepoints.net/U+0A39>`_  '\\u0a39'  Lo                  1  GURMUKHI LETTER HA
     2  `U+0A48 <https://codepoints.net/U+0A48>`_  '\\u0a48'  Mn                  0  GURMUKHI VOWEL SIGN AI
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\xb9\xe0\xa9\x88|\\n1|\\n"
        ਹੈ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *kitty* measures width -2.

.. _kittylangTaiDam:

Tai Dam
^^^^^^^

Sequence of language *Tai Dam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+AAB9 <https://codepoints.net/U+AAB9>`_  '\\uaab9'  Lo                  1  TAI VIET VOWEL UEA
     2  `U+AA8F <https://codepoints.net/U+AA8F>`_  '\\uaa8f'  Lo                  1  TAI VIET LETTER HIGH SO
     3  `U+AA89 <https://codepoints.net/U+AA89>`_  '\\uaa89'  Lo                  1  TAI VIET LETTER HIGH NGO
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xaa\xb9\xea\xaa\x8f\xea\xaa\x89|\\n123|\\n"
        ꪹꪏꪉ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width 1.

.. _kittylangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
     2  `U+0F45 <https://codepoints.net/U+0F45>`_  '\\u0f45'  Lo                  1  TIBETAN LETTER CA
     3  `U+0F72 <https://codepoints.net/U+0F72>`_  '\\u0f72'  Mn                  0  TIBETAN VOWEL SIGN I
     4  `U+0F42 <https://codepoints.net/U+0F42>`_  '\\u0f42'  Lo                  1  TIBETAN LETTER GA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x82\xe0\xbd\x85\xe0\xbd\xb2\xe0\xbd\x82|\\n123|\\n"
        གཅིག|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *kitty* measures width 1.

.. _kittydecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

DEC private modes results for *kitty*: 19 changeable modes
of 19 supported out of 159 total modes tested (11.9% support, 11.9% changeable).

Complete list of DEC private modes tested:

.. _kittydecmode1:

.. _kittydecmode3:

.. _kittydecmode5:

.. _kittydecmode6:

.. _kittydecmode7:

.. _kittydecmode8:

.. _kittydecmode25:

.. _kittydecmode1000:

.. _kittydecmode1002:

.. _kittydecmode1003:

.. _kittydecmode1004:

.. _kittydecmode1005:

.. _kittydecmode1006:

.. _kittydecmode1016:

.. _kittydecmode1049:

.. _kittydecmode2004:

.. _kittydecmode2026:

.. _kittydecmode2031:

.. _kittydecmode2048:

.. table::
   :class: sphinx-datatable

   ======  =============================  =======================================================================  ===========  ============  =========
     Mode  Name                           Description                                                              Supported    Changeable    Enabled
   ======  =============================  =======================================================================  ===========  ============  =========
        1  DECCKM                         Cursor Keys Mode                                                         Yes          Yes           No
        2  DECANM                         ANSI/VT52 Mode                                                           No           No            No
        3  DECCOLM                        Column Mode                                                              Yes          Yes           No
        4  DECSCLM                        Scrolling Mode                                                           No           No            No
        5  DECSCNM                        Screen Mode (light or dark screen)                                       Yes          Yes           No
        6  DECOM                          Origin Mode                                                              Yes          Yes           No
        7  DECAWM                         Auto Wrap Mode                                                           Yes          Yes           Yes
        8  DECARM                         Auto Repeat Mode                                                         Yes          Yes           Yes
        9  DECINLM                        Interlace Mode / Mouse X10 tracking                                      No           No            No
       10  DECEDM                         Editing Mode / Show toolbar (rxvt)                                       No           No            No
       11  DECLTM                         Line Transmit Mode                                                       No           No            No
       12  DECKANAM                       Katakana Shift Mode / Blinking cursor (xterm)                            No           No            No
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
       45  DECGPCS                        Graphics Print Color Syntax / Reverse-wraparound mode (xterm)            No           No            No
       46  DECGPBM                        Graphics Print Background Mode / Start logging (xterm)                   No           No            No
       47  DECGRPM                        Graphics Rotated Print Mode / Use Alternate Screen Buffer (xterm)        No           No            No
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
       66  DECNKM                         Numeric Keypad Mode                                                      No           No            No
       67  DECBKM                         Backarrow Key Mode                                                       No           No            No
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
     1005  MOUSE_EXTENDED_UTF8            Enable UTF-8 Mouse Mode                                                  Yes          Yes           No
     1006  MOUSE_EXTENDED_SGR             Enable SGR Mouse Mode                                                    Yes          Yes           No
     1007  ALT_SCROLL_XTERM               Enable Alternate Scroll Mode                                             No           No            No
     1010  SCROLL_ON_TTY_OUTPUT_RXVT      Scroll to bottom on tty output                                           No           No            No
     1011  SCROLL_ON_KEYPRESS_RXVT        Scroll to bottom on key press                                            No           No            No
     1014  FAST_SCROLL                    Enable fastScroll resource                                               No           No            No
     1015  MOUSE_URXVT                    Enable urxvt Mouse Mode                                                  No           No            No
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
     1047  ALT_SCREEN_BUFFER_XTERM        Use Alternate Screen Buffer                                              No           No            No
     1048  SAVE_CURSOR_DECSC              Save cursor as in DECSC                                                  No           No            No
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
     2026  SYNCHRONIZED_OUTPUT            Synchronized Output                                                      Yes          Yes           No
     2027  GRAPHEME_CLUSTERING            Grapheme Clustering                                                      No           No            No
     2028  TEXT_REFLOW                    Text reflow                                                              No           No            No
     2029  PASSIVE_MOUSE_TRACKING         Passive Mouse Tracking                                                   No           No            No
     2030  REPORT_GRID_CELL_SELECTION     Report grid cell selection                                               No           No            No
     2031  COLOR_PALETTE_UPDATES          Color palette updates                                                    Yes          Yes           No
     2048  IN_BAND_WINDOW_RESIZE          In-Band Window Resize Notifications                                      Yes          Yes           No
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

.. _kittyreproduce:

Reproduction
++++++++++++

To reproduce these results for *kitty*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --save-yaml=linux-kitty-0.43.1.yaml \
        --limit-codepoints=5000 \
        --limit-words=5000 \
        --limit-errors=1000

.. _kittytime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **849.99 seconds** (849s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
