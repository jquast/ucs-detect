.. _QTerminal:

QTerminal
---------


Tested Software version 1.4.0 on Linux
Full results available at ucs-detect_ repository path
`data/linux-QTerminal-1.4.0.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-QTerminal-1.4.0.yaml>`_

.. _QTerminalscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *QTerminal*:

.. table::
   :class: sphinx-datatable

   ============  ===========  ==============  ======================================================
   Score Type    Raw Score    Scaled Score    Calculation
   ============  ===========  ==============  ======================================================
   WIDE          81.82%       73.6%           (version_index / total_versions) × (pct_success / 100)
   ZWJ           0.00%        0.0%            (version_index / total_versions) × (pct_success / 100)
   LANG          99.30%       100.0%          geometric_mean(language_percentages)
   VS16          0.00%        0.0%            pct_success / 100
   VS15          0.00%        0.0%            pct_success / 100
   DEC Modes     N/A          N/A             modes_changeable / total_modes
   TIME          40.88s       88.4%           1 - ((elapsed - min) / (max - min)) [inverse]
   ============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 36.22%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 27.7%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _QTerminalwide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for QTerminal appears to be 
**15.1.0**, this is from a summary of the following
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
  while *QTerminal* measures width 1.

.. _QTerminalzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *QTerminal* appears to be 
**None**, this is from a summary of the following
results:


.. table::
   :class: sphinx-datatable

   =========  ==========  =========  =============
   version      n_errors    n_total  pct_success
   =========  ==========  =========  =============
   '2.0'              21         22  4.5%
   '4.0'             500        508  1.6%
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
  while *QTerminal* measures width 9.

.. _QTerminalvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *QTerminal* is 213 errors
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
  while *QTerminal* measures width 1.


.. _QTerminalvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *QTerminal* is 158 errors
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
  while *QTerminal* measures width 2.


.. _QTerminallang:

Language Support
++++++++++++++++

The following 3 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog), Tamang, Eastern.

The following 116 languages are not fully supported:

.. table::
   :class: sphinx-datatable

   ================================================================================  ==========  =========  =============
   lang                                                                                n_errors    n_total  pct_success
   ================================================================================  ==========  =========  =============
   :ref:`Malayalam <QTerminallangMalayalam>`                                                116       1630  92.9%
   :ref:`Sinhala <QTerminallangSinhala>`                                                    112       1655  93.2%
   :ref:`Vietnamese (Han nom) <QTerminallangVietnameseHannom>`                                4        199  98.0%
   :ref:`Japanese <QTerminallangJapanese>`                                                    6        299  98.0%
   :ref:`(Jinan) <QTerminallangJinan>`                                                        4        211  98.1%
   :ref:`Chinese, Mandarin (Guiyang) <QTerminallangChineseMandarinGuiyang>`                   4        211  98.1%
   :ref:`Chinese, Wu <QTerminallangChineseWu>`                                                4        211  98.1%
   :ref:`Chinese, Hakka <QTerminallangChineseHakka>`                                          4        212  98.1%
   :ref:`Chinese, Jinyu <QTerminallangChineseJinyu>`                                          4        212  98.1%
   :ref:`Chinese, Mandarin (Beijing) <QTerminallangChineseMandarinBeijing>`                   4        212  98.1%
   :ref:`Chinese, Min Nan <QTerminallangChineseMinNan>`                                       4        212  98.1%
   :ref:`Chinese, Xiang <QTerminallangChineseXiang>`                                          4        212  98.1%
   :ref:`Chinese, Mandarin (Simplified) <QTerminallangChineseMandarinSimplified>`             4        225  98.2%
   :ref:`Nuosu <QTerminallangNuosu>`                                                          4        230  98.3%
   :ref:`Japanese (Osaka) <QTerminallangJapaneseOsaka>`                                       5        308  98.4%
   :ref:`Japanese (Tokyo) <QTerminallangJapaneseTokyo>`                                       5        320  98.4%
   :ref:`Chinese, Mandarin (Harbin) <QTerminallangChineseMandarinHarbin>`                     3        210  98.6%
   :ref:`Chinese, Mandarin (Traditional) <QTerminallangChineseMandarinTraditional>`           3        210  98.6%
   :ref:`Chinese, Yue <QTerminallangChineseYue>`                                              3        210  98.6%
   :ref:`Chinese, Gan <QTerminallangChineseGan>`                                              3        211  98.6%
   :ref:`Chinese, Mandarin (Nanjing) <QTerminallangChineseMandarinNanjing>`                   3        212  98.6%
   :ref:`Chinese, Mandarin (Tianjin) <QTerminallangChineseMandarinTianjin>`                   3        212  98.6%
   :ref:`Thai <QTerminallangThai>`                                                            4        341  98.8%
   :ref:`Thai (2) <QTerminallangThai2>`                                                       3        313  99.0%
   :ref:`Lao <QTerminallangLao>`                                                              4        426  99.1%
   :ref:`Khmer, Central <QTerminallangKhmerCentral>`                                          4        528  99.2%
   :ref:`Khün <QTerminallangKhn>`                                                             3        442  99.3%
   :ref:`Bora <QTerminallangBora>`                                                            9       1598  99.4%
   :ref:`Marathi <QTerminallangMarathi>`                                                      9       1614  99.4%
   :ref:`Gumuz <QTerminallangGumuz>`                                                          7       1283  99.5%
   :ref:`Chickasaw <QTerminallangChickasaw>`                                                  3        554  99.5%
   :ref:`Shipibo-Conibo <QTerminallangShipiboConibo>`                                        13       2540  99.5%
   :ref:`Nepali <QTerminallangNepali>`                                                        7       1385  99.5%
   :ref:`Navajo <QTerminallangNavajo>`                                                        8       1600  99.5%
   :ref:`Nanai <QTerminallangNanai>`                                                          6       1207  99.5%
   :ref:`Bengali <QTerminallangBengali>`                                                      7       1413  99.5%
   :ref:`Amarakaeri <QTerminallangAmarakaeri>`                                                7       1446  99.5%
   :ref:`Orok <QTerminallangOrok>`                                                            6       1245  99.5%
   :ref:`Yaneshaʼ <QTerminallangYanesha>`                                                    12       2536  99.5%
   :ref:`Siona <QTerminallangSiona>`                                                          7       1492  99.5%
   :ref:`Gilyak <QTerminallangGilyak>`                                                        7       1504  99.5%
   :ref:`Veps <QTerminallangVeps>`                                                            6       1323  99.5%
   :ref:`Evenki <QTerminallangEvenki>`                                                        4        899  99.6%
   :ref:`Shan <QTerminallangShan>`                                                            4        915  99.6%
   :ref:`South Azerbaijani <QTerminallangSouthAzerbaijani>`                                   6       1396  99.6%
   :ref:`Secoya <QTerminallangSecoya>`                                                        6       1409  99.6%
   :ref:`Mon <QTerminallangMon>`                                                              4        946  99.6%
   :ref:`Korean <QTerminallangKorean>`                                                        5       1185  99.6%
   :ref:`Burmese <QTerminallangBurmese>`                                                      5       1223  99.6%
   :ref:`Sanskrit <QTerminallangSanskrit>`                                                    4       1000  99.6%
   :ref:`Sanskrit (Grantha) <QTerminallangSanskritGrantha>`                                   4       1006  99.6%
   :ref:`Tamil (Sri Lanka) <QTerminallangTamilSriLanka>`                                      5       1261  99.6%
   :ref:`Tamil <QTerminallangTamil>`                                                          5       1262  99.6%
   :ref:`Colorado <QTerminallangColorado>`                                                    5       1263  99.6%
   :ref:`(Yeonbyeon) <QTerminallangYeonbyeon>`                                                4       1061  99.6%
   :ref:`Kannada <QTerminallangKannada>`                                                      4       1080  99.6%
   :ref:`Catalan (2) <QTerminallangCatalan2>`                                                 7       1909  99.6%
   :ref:`Tem <QTerminallangTem>`                                                              6       1659  99.6%
   :ref:`Mirandese <QTerminallangMirandese>`                                                  7       1966  99.6%
   :ref:`Telugu <QTerminallangTelugu>`                                                        4       1129  99.6%
   :ref:`Picard <QTerminallangPicard>`                                                        7       2024  99.7%
   :ref:`Assyrian Neo-Aramaic <QTerminallangAssyrianNeoAramaic>`                              4       1160  99.7%
   :ref:`Ticuna <QTerminallangTicuna>`                                                        7       2048  99.7%
   :ref:`Yiddish, Eastern <QTerminallangYiddishEastern>`                                      6       1775  99.7%
   :ref:`Kabyle <QTerminallangKabyle>`                                                        6       1815  99.7%
   :ref:`Lingala (tones) <QTerminallangLingalatones>`                                         6       1818  99.7%
   :ref:`Tamazight, Central Atlas <QTerminallangTamazightCentralAtlas>`                       6       1822  99.7%
   :ref:`Fur <QTerminallangFur>`                                                              6       1838  99.7%
   :ref:`Mazahua Central <QTerminallangMazahuaCentral>`                                       5       1574  99.7%
   :ref:`Éwé <QTerminallangw>`                                                                7       2230  99.7%
   :ref:`Maldivian <QTerminallangMaldivian>`                                                  6       1918  99.7%
   :ref:`French (Welche) <QTerminallangFrenchWelche>`                                         6       1928  99.7%
   :ref:`Pular (Adlam) <QTerminallangPularAdlam>`                                             5       1613  99.7%
   :ref:`Uduk <QTerminallangUduk>`                                                           10       3247  99.7%
   :ref:`Gen <QTerminallangGen>`                                                              7       2309  99.7%
   :ref:`Arabic, Standard <QTerminallangArabicStandard>`                                      4       1348  99.7%
   :ref:`Ga <QTerminallangGa>`                                                                6       2039  99.7%
   :ref:`Maori (2) <QTerminallangMaori2>`                                                     7       2385  99.7%
   :ref:`Mixtec, Metlatónoc <QTerminallangMixtecMetlatnoc>`                                   4       1367  99.7%
   :ref:`Aja <QTerminallangAja>`                                                              6       2061  99.7%
   :ref:`Chinantec, Chiltepec <QTerminallangChinantecChiltepec>`                              5       1729  99.7%
   :ref:`Mòoré <QTerminallangMor>`                                                            7       2447  99.7%
   :ref:`Yoruba <QTerminallangYoruba>`                                                        7       2454  99.7%
   :ref:`Saint Lucian Creole French <QTerminallangSaintLucianCreoleFrench>`                   5       1777  99.7%
   :ref:`Vietnamese <QTerminallangVietnamese>`                                                7       2502  99.7%
   :ref:`Javanese (Javanese) <QTerminallangJavaneseJavanese>`                                 4       1453  99.7%
   :ref:`Farsi, Western <QTerminallangFarsiWestern>`                                          5       1822  99.7%
   :ref:`Dagaare, Southern <QTerminallangDagaareSouthern>`                                    7       2582  99.7%
   :ref:`Otomi, Mezquital <QTerminallangOtomiMezquital>`                                      5       1849  99.7%
   :ref:`Lamnso' <QTerminallangLamnso>`                                                       6       2237  99.7%
   :ref:`Urdu <QTerminallangUrdu>`                                                            6       2237  99.7%
   :ref:`Pashto, Northern <QTerminallangPashtoNorthern>`                                      6       2242  99.7%
   :ref:`Seraiki <QTerminallangSeraiki>`                                                      6       2242  99.7%
   :ref:`Belanda Viri <QTerminallangBelandaViri>`                                             6       2246  99.7%
   :ref:`Dari <QTerminallangDari>`                                                            5       1872  99.7%
   :ref:`Urdu (2) <QTerminallangUrdu2>`                                                       6       2251  99.7%
   :ref:`Ditammari <QTerminallangDitammari>`                                                  5       1882  99.7%
   :ref:`Maithili <QTerminallangMaithili>`                                                    4       1519  99.7%
   :ref:`Bamun <QTerminallangBamun>`                                                          6       2285  99.7%
   :ref:`Dinka, Northeastern <QTerminallangDinkaNortheastern>`                                4       1529  99.7%
   :ref:`Gujarati <QTerminallangGujarati>`                                                    4       1536  99.7%
   :ref:`Baatonum <QTerminallangBaatonum>`                                                    5       1939  99.7%
   :ref:`Dendi <QTerminallangDendi>`                                                          4       1569  99.7%
   :ref:`Serer-Sine <QTerminallangSererSine>`                                                 4       1596  99.7%
   :ref:`Panjabi, Western <QTerminallangPanjabiWestern>`                                      6       2419  99.8%
   :ref:`Fon <QTerminallangFon>`                                                              6       2520  99.8%
   :ref:`Hindi <QTerminallangHindi>`                                                          5       2128  99.8%
   :ref:`Bhojpuri <QTerminallangBhojpuri>`                                                    4       1737  99.8%
   :ref:`Tai Dam <QTerminallangTaiDam>`                                                       5       2386  99.8%
   :ref:`Chakma <QTerminallangChakma>`                                                        3       1444  99.8%
   :ref:`Dangme <QTerminallangDangme>`                                                        6       2912  99.8%
   :ref:`Waama <QTerminallangWaama>`                                                          2       1000  99.8%
   :ref:`Tibetan, Central <QTerminallangTibetanCentral>`                                      6       3174  99.8%
   :ref:`Magahi <QTerminallangMagahi>`                                                        3       1716  99.8%
   :ref:`Panjabi, Eastern <QTerminallangPanjabiEastern>`                                      4       2293  99.8%
   :ref:`Dzongkha <QTerminallangDzongkha>`                                                    5       3060  99.8%
   ================================================================================  ==========  =========  =============

.. _QTerminallangMalayalam:

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
  while *QTerminal* measures width 10.

.. _QTerminallangSinhala:

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
  while *QTerminal* measures width 6.

.. _QTerminallangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===========================
     1  `U+000235D3 <https://codepoints.net/U+000235D3>`_  '\\U000235d3'  Lo                  2  CJK UNIFIED IDEOGRAPH-235D3
     2  `U+81EA <https://codepoints.net/U+81EA>`_          '\\u81ea'      Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     3  `U+7BA1 <https://codepoints.net/U+7BA1>`_          '\\u7ba1'      Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
     4  `U+548D <https://codepoints.net/U+548D>`_          '\\u548d'      Lo                  2  CJK UNIFIED IDEOGRAPH-548D
     5  `U+0002338F <https://codepoints.net/U+0002338F>`_  '\\U0002338f'  Lo                  2  CJK UNIFIED IDEOGRAPH-2338F
     6  `U+4E3B <https://codepoints.net/U+4E3B>`_          '\\u4e3b'      Lo                  2  CJK UNIFIED IDEOGRAPH-4E3B
     7  `U+6B0A <https://codepoints.net/U+6B0A>`_          '\\u6b0a'      Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
     8  `U+9650 <https://codepoints.net/U+9650>`_          '\\u9650'      Lo                  2  CJK UNIFIED IDEOGRAPH-9650
     9  `U+5236 <https://codepoints.net/U+5236>`_          '\\u5236'      Lo                  2  CJK UNIFIED IDEOGRAPH-5236
   ===  =================================================  =============  ==========  =========  ===========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\xa3\x97\x93\xe8\x87\xaa\xe7\xae\xa1\xe5\x92\x8d\xf0\xa3\x8e\x8f\xe4\xb8\xbb\xe6\xac\x8a\xe9\x99\x90\xe5\x88\xb6|\\n123456789012345678|\\n"
        𣗓自管咍𣎏主權限制|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *QTerminal* measures width 4.

.. _QTerminallangJapanese:

Japanese
^^^^^^^^

Sequence of language *Japanese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
     2  `U+3079 <https://codepoints.net/U+3079>`_  '\\u3079'  Lo                  2  HIRAGANA LETTER BE
     3  `U+3066 <https://codepoints.net/U+3066>`_  '\\u3066'  Lo                  2  HIRAGANA LETTER TE
     4  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     5  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     6  `U+9593 <https://codepoints.net/U+9593>`_  '\\u9593'  Lo                  2  CJK UNIFIED IDEOGRAPH-9593
     7  `U+306F <https://codepoints.net/U+306F>`_  '\\u306f'  Lo                  2  HIRAGANA LETTER HA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\x99\xe3\x81\xb9\xe3\x81\xa6\xe3\x81\xae\xe4\xba\xba\xe9\x96\x93\xe3\x81\xaf|\\n12345678901234|\\n"
        すべての人間は|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *QTerminal* measures width 8.

.. _QTerminallangJinan:

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     2  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     3  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
     4  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     5  `U+8EAB <https://codepoints.net/U+8EAB>`_  '\\u8eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-8EAB
     6  `U+5B89 <https://codepoints.net/U+5B89>`_  '\\u5b89'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B89
     7  `U+5168 <https://codepoints.net/U+5168>`_  '\\u5168'  Lo                  2  CJK UNIFIED IDEOGRAPH-5168
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x87\xaa\xe7\x94\xb1\xe5\x92\x8c\xe4\xba\xba\xe8\xba\xab\xe5\xae\x89\xe5\x85\xa8|\\n12345678901234|\\n"
        自由和人身安全|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *QTerminal* measures width -4.

.. _QTerminallangChineseMandarinGuiyang:

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E09 <https://codepoints.net/U+4E09>`_  '\\u4e09'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E09
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb8\x89\xe6\x9d\xa1|\\n123456|\\n"
        第三条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width -36.

.. _QTerminallangChineseWu:

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
     5  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
     6  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     7  `U+751F <https://codepoints.net/U+751F>`_  '\\u751f'  Lo                  2  CJK UNIFIED IDEOGRAPH-751F
     8  `U+547D <https://codepoints.net/U+547D>`_  '\\u547d'  Lo                  2  CJK UNIFIED IDEOGRAPH-547D
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xba\xba\xe4\xba\xba\xe6\x9c\x89\xe6\x9d\x83\xe4\xba\xab\xe6\x9c\x89\xe7\x94\x9f\xe5\x91\xbd|\\n1234567890123456|\\n"
        人人有权享有生命|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *QTerminal* measures width 10.

.. _QTerminallangChineseHakka:

Chinese, Hakka
^^^^^^^^^^^^^^

Sequence of language *Chinese, Hakka* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     2  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     3  `U+540C <https://codepoints.net/U+540C>`_  '\\u540c'  Lo                  2  CJK UNIFIED IDEOGRAPH-540C
     4  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     5  `U+8EAB <https://codepoints.net/U+8EAB>`_  '\\u8eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-8EAB
     6  `U+5B89 <https://codepoints.net/U+5B89>`_  '\\u5b89'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B89
     7  `U+5168 <https://codepoints.net/U+5168>`_  '\\u5168'  Lo                  2  CJK UNIFIED IDEOGRAPH-5168
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x87\xaa\xe7\x94\xb1\xe5\x90\x8c\xe4\xba\xba\xe8\xba\xab\xe5\xae\x89\xe5\x85\xa8|\\n12345678901234|\\n"
        自由同人身安全|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *QTerminal* measures width -2.

.. _QTerminallangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     2  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     3  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
     4  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     5  `U+8EAB <https://codepoints.net/U+8EAB>`_  '\\u8eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-8EAB
     6  `U+5B89 <https://codepoints.net/U+5B89>`_  '\\u5b89'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B89
     7  `U+5168 <https://codepoints.net/U+5168>`_  '\\u5168'  Lo                  2  CJK UNIFIED IDEOGRAPH-5168
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x87\xaa\xe7\x94\xb1\xe5\x92\x8c\xe4\xba\xba\xe8\xba\xab\xe5\xae\x89\xe5\x85\xa8|\\n12345678901234|\\n"
        自由和人身安全|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *QTerminal* measures width -2.

.. _QTerminallangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

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
  while *QTerminal* measures width -12.

.. _QTerminallangChineseMinNan:

Chinese, Min Nan
^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Min Nan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     2  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     3  `U+5408 <https://codepoints.net/U+5408>`_  '\\u5408'  Lo                  2  CJK UNIFIED IDEOGRAPH-5408
     4  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     5  `U+8EAB <https://codepoints.net/U+8EAB>`_  '\\u8eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-8EAB
     6  `U+5B89 <https://codepoints.net/U+5B89>`_  '\\u5b89'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B89
     7  `U+5168 <https://codepoints.net/U+5168>`_  '\\u5168'  Lo                  2  CJK UNIFIED IDEOGRAPH-5168
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x87\xaa\xe7\x94\xb1\xe5\x90\x88\xe4\xba\xba\xe8\xba\xab\xe5\xae\x89\xe5\x85\xa8|\\n12345678901234|\\n"
        自由合人身安全|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *QTerminal* measures width -6.

.. _QTerminallangChineseXiang:

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E09 <https://codepoints.net/U+4E09>`_  '\\u4e09'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E09
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb8\x89\xe6\x9d\xa1|\\n123456|\\n"
        第三条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width -44.

.. _QTerminallangChineseMandarinSimplified:

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

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
  while *QTerminal* measures width -20.

.. _QTerminallangNuosu:

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================
     1  `U+A2A8 <https://codepoints.net/U+A2A8>`_  '\\ua2a8'  Lo                  2  YI SYLLABLE ZYT
     2  `U+A3E6 <https://codepoints.net/U+A3E6>`_  '\\ua3e6'  Lo                  2  YI SYLLABLE JIE
     3  `U+A00B <https://codepoints.net/U+A00B>`_  '\\ua00b'  Lo                  2  YI SYLLABLE AP
     4  `U+A3F2 <https://codepoints.net/U+A3F2>`_  '\\ua3f2'  Lo                  2  YI SYLLABLE JU
     5  `U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
     6  `U+A3F2 <https://codepoints.net/U+A3F2>`_  '\\ua3f2'  Lo                  2  YI SYLLABLE JU
     7  `U+A138 <https://codepoints.net/U+A138>`_  '\\ua138'  Lo                  2  YI SYLLABLE DDI
     8  `U+A30B <https://codepoints.net/U+A30B>`_  '\\ua30b'  Lo                  2  YI SYLLABLE SI
     9  `U+A180 <https://codepoints.net/U+A180>`_  '\\ua180'  Lo                  2  YI SYLLABLE NIP
    10  `U+A009 <https://codepoints.net/U+A009>`_  '\\ua009'  Lo                  2  YI SYLLABLE AX
    11  `U+A041 <https://codepoints.net/U+A041>`_  '\\ua041'  Lo                  2  YI SYLLABLE PA
    12  `U+A20D <https://codepoints.net/U+A20D>`_  '\\ua20d'  Lo                  2  YI SYLLABLE KEP
    13  `U+A0C5 <https://codepoints.net/U+A0C5>`_  '\\ua0c5'  Lo                  2  YI SYLLABLE MU
    14  `U+A3F2 <https://codepoints.net/U+A3F2>`_  '\\ua3f2'  Lo                  2  YI SYLLABLE JU
    15  `U+A138 <https://codepoints.net/U+A138>`_  '\\ua138'  Lo                  2  YI SYLLABLE DDI
    16  `U+A26C <https://codepoints.net/U+A26C>`_  '\\ua26c'  Lo                  2  YI SYLLABLE NGE
    17  `U+A0BF <https://codepoints.net/U+A0BF>`_  '\\ua0bf'  Lo                  2  YI SYLLABLE MO
    18  `U+A42F <https://codepoints.net/U+A42F>`_  '\\ua42f'  Lo                  2  YI SYLLABLE JJY
    19  `U+A00B <https://codepoints.net/U+A00B>`_  '\\ua00b'  Lo                  2  YI SYLLABLE AP
    20  `U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
    21  `U+A00B <https://codepoints.net/U+A00B>`_  '\\ua00b'  Lo                  2  YI SYLLABLE AP
    22  `U+A246 <https://codepoints.net/U+A246>`_  '\\ua246'  Lo                  2  YI SYLLABLE HXIT
    23  `U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
    24  `U+A26C <https://codepoints.net/U+A26C>`_  '\\ua26c'  Lo                  2  YI SYLLABLE NGE
   ===  =========================================  =========  ==========  =========  ================

Total codepoints: 24


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x8a\xa8\xea\x8f\xa6\xea\x80\x8b\xea\x8f\xb2\xea\x8c\xa0\xea\x8f\xb2\xea\x84\xb8\xea\x8c\x8b\xea\x86\x80\xea\x80\x89\xea\x81\x81\xea\x88\x8d\xea\x83\x85\xea\x8f\xb2\xea\x84\xb8\xea\x89\xac\xea\x82\xbf\xea\x90\xaf\xea\x80\x8b\xea\x8c\xa0\xea\x80\x8b\xea\x89\x86\xea\x8c\xa0\xea\x89\xac|\\n123456789012345678901234567890123456789012345678|\\n"
        ꊨꏦꀋꏲꌠꏲꄸꌋꆀꀉꁁꈍꃅꏲꄸꉬꂿꐯꀋꌠꀋꉆꌠꉬ|
        123456789012345678901234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 48,
  while *QTerminal* measures width 28.

.. _QTerminallangJapaneseOsaka:

Japanese (Osaka)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Osaka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+3059 <https://codepoints.net/U+3059>`_  '\\u3059'  Lo                  2  HIRAGANA LETTER SU
     2  `U+3079 <https://codepoints.net/U+3079>`_  '\\u3079'  Lo                  2  HIRAGANA LETTER BE
     3  `U+3066 <https://codepoints.net/U+3066>`_  '\\u3066'  Lo                  2  HIRAGANA LETTER TE
     4  `U+306E <https://codepoints.net/U+306E>`_  '\\u306e'  Lo                  2  HIRAGANA LETTER NO
     5  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     6  `U+9593 <https://codepoints.net/U+9593>`_  '\\u9593'  Lo                  2  CJK UNIFIED IDEOGRAPH-9593
     7  `U+306F <https://codepoints.net/U+306F>`_  '\\u306f'  Lo                  2  HIRAGANA LETTER HA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe3\x81\x99\xe3\x81\xb9\xe3\x81\xa6\xe3\x81\xae\xe4\xba\xba\xe9\x96\x93\xe3\x81\xaf|\\n12345678901234|\\n"
        すべての人間は|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *QTerminal* measures width 8.

.. _QTerminallangJapaneseTokyo:

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+751F <https://codepoints.net/U+751F>`_  '\\u751f'  Lo                  2  CJK UNIFIED IDEOGRAPH-751F
     2  `U+307E <https://codepoints.net/U+307E>`_  '\\u307e'  Lo                  2  HIRAGANA LETTER MA
     3  `U+308C <https://codepoints.net/U+308C>`_  '\\u308c'  Lo                  2  HIRAGANA LETTER RE
     4  `U+306A <https://codepoints.net/U+306A>`_  '\\u306a'  Lo                  2  HIRAGANA LETTER NA
     5  `U+304C <https://codepoints.net/U+304C>`_  '\\u304c'  Lo                  2  HIRAGANA LETTER GA
     6  `U+3089 <https://codepoints.net/U+3089>`_  '\\u3089'  Lo                  2  HIRAGANA LETTER RA
     7  `U+306B <https://codepoints.net/U+306B>`_  '\\u306b'  Lo                  2  HIRAGANA LETTER NI
     8  `U+3057 <https://codepoints.net/U+3057>`_  '\\u3057'  Lo                  2  HIRAGANA LETTER SI
     9  `U+3066 <https://codepoints.net/U+3066>`_  '\\u3066'  Lo                  2  HIRAGANA LETTER TE
    10  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
    11  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
    12  `U+3067 <https://codepoints.net/U+3067>`_  '\\u3067'  Lo                  2  HIRAGANA LETTER DE
    13  `U+3042 <https://codepoints.net/U+3042>`_  '\\u3042'  Lo                  2  HIRAGANA LETTER A
    14  `U+308A <https://codepoints.net/U+308A>`_  '\\u308a'  Lo                  2  HIRAGANA LETTER RI
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\x94\x9f\xe3\x81\xbe\xe3\x82\x8c\xe3\x81\xaa\xe3\x81\x8c\xe3\x82\x89\xe3\x81\xab\xe3\x81\x97\xe3\x81\xa6\xe8\x87\xaa\xe7\x94\xb1\xe3\x81\xa7\xe3\x81\x82\xe3\x82\x8a|\\n1234567890123456789012345678|\\n"
        生まれながらにして自由であり|
        1234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 28,
  while *QTerminal* measures width 16.

.. _QTerminallangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     2  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     3  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     4  `U+6743 <https://codepoints.net/U+6743>`_  '\\u6743'  Lo                  2  CJK UNIFIED IDEOGRAPH-6743
     5  `U+4EAB <https://codepoints.net/U+4EAB>`_  '\\u4eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EAB
     6  `U+6709 <https://codepoints.net/U+6709>`_  '\\u6709'  Lo                  2  CJK UNIFIED IDEOGRAPH-6709
     7  `U+751F <https://codepoints.net/U+751F>`_  '\\u751f'  Lo                  2  CJK UNIFIED IDEOGRAPH-751F
     8  `U+547D <https://codepoints.net/U+547D>`_  '\\u547d'  Lo                  2  CJK UNIFIED IDEOGRAPH-547D
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xba\xba\xe4\xba\xba\xe6\x9c\x89\xe6\x9d\x83\xe4\xba\xab\xe6\x9c\x89\xe7\x94\x9f\xe5\x91\xbd|\\n1234567890123456|\\n"
        人人有权享有生命|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *QTerminal* measures width 9.

.. _QTerminallangChineseMandarinTraditional:

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5747 <https://codepoints.net/U+5747>`_  '\\u5747'  Lo                  2  CJK UNIFIED IDEOGRAPH-5747
     2  `U+61C9 <https://codepoints.net/U+61C9>`_  '\\u61c9'  Lo                  2  CJK UNIFIED IDEOGRAPH-61C9
     3  `U+4E88 <https://codepoints.net/U+4E88>`_  '\\u4e88'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E88
     4  `U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
     5  `U+7981 <https://codepoints.net/U+7981>`_  '\\u7981'  Lo                  2  CJK UNIFIED IDEOGRAPH-7981
     6  `U+6B62 <https://codepoints.net/U+6B62>`_  '\\u6b62'  Lo                  2  CJK UNIFIED IDEOGRAPH-6B62
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x9d\x87\xe6\x87\x89\xe4\xba\x88\xe4\xbb\xa5\xe7\xa6\x81\xe6\xad\xa2|\\n123456789012|\\n"
        均應予以禁止|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *QTerminal* measures width -42.

.. _QTerminallangChineseYue:

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
  while *QTerminal* measures width -14.

.. _QTerminallangChineseGan:

Chinese, Gan
^^^^^^^^^^^^

Sequence of language *Chinese, Gan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+81EA <https://codepoints.net/U+81EA>`_  '\\u81ea'  Lo                  2  CJK UNIFIED IDEOGRAPH-81EA
     2  `U+7531 <https://codepoints.net/U+7531>`_  '\\u7531'  Lo                  2  CJK UNIFIED IDEOGRAPH-7531
     3  `U+8DDF <https://codepoints.net/U+8DDF>`_  '\\u8ddf'  Lo                  2  CJK UNIFIED IDEOGRAPH-8DDF
     4  `U+4EBA <https://codepoints.net/U+4EBA>`_  '\\u4eba'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EBA
     5  `U+8EAB <https://codepoints.net/U+8EAB>`_  '\\u8eab'  Lo                  2  CJK UNIFIED IDEOGRAPH-8EAB
     6  `U+5B89 <https://codepoints.net/U+5B89>`_  '\\u5b89'  Lo                  2  CJK UNIFIED IDEOGRAPH-5B89
     7  `U+5168 <https://codepoints.net/U+5168>`_  '\\u5168'  Lo                  2  CJK UNIFIED IDEOGRAPH-5168
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe8\x87\xaa\xe7\x94\xb1\xe8\xb7\x9f\xe4\xba\xba\xe8\xba\xab\xe5\xae\x89\xe5\x85\xa8|\\n12345678901234|\\n"
        自由跟人身安全|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *QTerminal* measures width -2.

.. _QTerminallangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+7B2C <https://codepoints.net/U+7B2C>`_  '\\u7b2c'  Lo                  2  CJK UNIFIED IDEOGRAPH-7B2C
     2  `U+4E09 <https://codepoints.net/U+4E09>`_  '\\u4e09'  Lo                  2  CJK UNIFIED IDEOGRAPH-4E09
     3  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe4\xb8\x89\xe6\x9d\xa1|\\n123456|\\n"
        第三条|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width -40.

.. _QTerminallangChineseMandarinTianjin:

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

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
     6  `U+4F3C <https://codepoints.net/U+4F3C>`_  '\\u4f3c'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F3C
     7  `U+72EC <https://codepoints.net/U+72EC>`_  '\\u72ec'  Lo                  2  CJK UNIFIED IDEOGRAPH-72EC
     8  `U+7ACB <https://codepoints.net/U+7ACB>`_  '\\u7acb'  Lo                  2  CJK UNIFIED IDEOGRAPH-7ACB
     9  `U+9886 <https://codepoints.net/U+9886>`_  '\\u9886'  Lo                  2  CJK UNIFIED IDEOGRAPH-9886
    10  `U+571F <https://codepoints.net/U+571F>`_  '\\u571f'  Lo                  2  CJK UNIFIED IDEOGRAPH-571F
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x97\xa0\xe8\xae\xba\xe8\xaf\xa5\xe9\xa2\x86\xe5\x9c\x9f\xe4\xbc\xbc\xe7\x8b\xac\xe7\xab\x8b\xe9\xa2\x86\xe5\x9c\x9f|\\n12345678901234567890|\\n"
        无论该领土似独立领土|
        12345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 20,
  while *QTerminal* measures width -16.

.. _QTerminallangThai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================
     1  `U+0E17 <https://codepoints.net/U+0E17>`_  '\\u0e17'  Lo                  1  THAI CHARACTER THO THAHAN
     2  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
     3  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
     4  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
     5  `U+0E43 <https://codepoints.net/U+0E43>`_  '\\u0e43'  Lo                  1  THAI CHARACTER SARA AI MAIMUAN
     6  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
     7  `U+0E1A <https://codepoints.net/U+0E1A>`_  '\\u0e1a'  Lo                  1  THAI CHARACTER BO BAIMAI
     8  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     9  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    10  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
    11  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    12  `U+0E1B <https://codepoints.net/U+0E1B>`_  '\\u0e1b'  Lo                  1  THAI CHARACTER PO PLA
    13  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    14  `U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
    15  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
    16  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    17  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
    18  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    19  `U+0E02 <https://codepoints.net/U+0E02>`_  '\\u0e02'  Lo                  1  THAI CHARACTER KHO KHAI
    20  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
    21  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
    22  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    23  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    24  `U+0E10 <https://codepoints.net/U+0E10>`_  '\\u0e10'  Lo                  1  THAI CHARACTER THO THAN
    25  `U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
    26  `U+0E21 <https://codepoints.net/U+0E21>`_  '\\u0e21'  Lo                  1  THAI CHARACTER MO MA
    27  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    28  `U+0E0A <https://codepoints.net/U+0E0A>`_  '\\u0e0a'  Lo                  1  THAI CHARACTER CHO CHANG
    29  `U+0E34 <https://codepoints.net/U+0E34>`_  '\\u0e34'  Mn                  0  THAI CHARACTER SARA I
    30  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    31  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
    32  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
    33  `U+0E27 <https://codepoints.net/U+0E27>`_  '\\u0e27'  Lo                  1  THAI CHARACTER WO WAEN
    34  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
    35  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    36  `U+0E31 <https://codepoints.net/U+0E31>`_  '\\u0e31'  Mn                  0  THAI CHARACTER MAI HAN-AKAT
    37  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    38  `U+0E40 <https://codepoints.net/U+0E40>`_  '\\u0e40'  Lo                  1  THAI CHARACTER SARA E
    39  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
    40  `U+0E07 <https://codepoints.net/U+0E07>`_  '\\u0e07'  Lo                  1  THAI CHARACTER NGO NGU
   ===  =========================================  =========  ==========  =========  ==============================

Total codepoints: 40


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x97\xe0\xb8\xb1\xe0\xb9\x89\xe0\xb8\x87\xe0\xb9\x83\xe0\xb8\x99\xe0\xb8\x9a\xe0\xb8\xa3\xe0\xb8\xa3\xe0\xb8\x94\xe0\xb8\xb2\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\x8a\xe0\xb8\x99\xe0\xb8\x82\xe0\xb8\xad\xe0\xb8\x87\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x90\xe0\xb8\xaa\xe0\xb8\xa1\xe0\xb8\xb2\xe0\xb8\x8a\xe0\xb8\xb4\xe0\xb8\x81\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\x81\xe0\xb8\xb1\xe0\xb8\x99\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\x87|\\n1234567890123456789012345678901234|\\n"
        ทั้งในบรรดาประชาชนของรัฐสมาชิกด้วยกันเอง|
        1234567890123456789012345678901234|

- python `wcwidth.wcswidth()`_ measures width 34,
  while *QTerminal* measures width -3.

.. _QTerminallangThai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0E14 <https://codepoints.net/U+0E14>`_  '\\u0e14'  Lo                  1  THAI CHARACTER DO DEK
     2  `U+0E49 <https://codepoints.net/U+0E49>`_  '\\u0e49'  Mn                  0  THAI CHARACTER MAI THO
     3  `U+0E27 <https://codepoints.net/U+0E27>`_  '\\u0e27'  Lo                  1  THAI CHARACTER WO WAEN
     4  `U+0E22 <https://codepoints.net/U+0E22>`_  '\\u0e22'  Lo                  1  THAI CHARACTER YO YAK
     5  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
     6  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
     7  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
     8  `U+0E2A <https://codepoints.net/U+0E2A>`_  '\\u0e2a'  Lo                  1  THAI CHARACTER SO SUA
     9  `U+0E2D <https://codepoints.net/U+0E2D>`_  '\\u0e2d'  Lo                  1  THAI CHARACTER O ANG
    10  `U+0E19 <https://codepoints.net/U+0E19>`_  '\\u0e19'  Lo                  1  THAI CHARACTER NO NU
    11  `U+0E41 <https://codepoints.net/U+0E41>`_  '\\u0e41'  Lo                  1  THAI CHARACTER SARA AE
    12  `U+0E25 <https://codepoints.net/U+0E25>`_  '\\u0e25'  Lo                  1  THAI CHARACTER LO LING
    13  `U+0E30 <https://codepoints.net/U+0E30>`_  '\\u0e30'  Lo                  1  THAI CHARACTER SARA A
    14  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    15  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
    16  `U+0E23 <https://codepoints.net/U+0E23>`_  '\\u0e23'  Lo                  1  THAI CHARACTER RO RUA
    17  `U+0E28 <https://codepoints.net/U+0E28>`_  '\\u0e28'  Lo                  1  THAI CHARACTER SO SALA
    18  `U+0E36 <https://codepoints.net/U+0E36>`_  '\\u0e36'  Mn                  0  THAI CHARACTER SARA UE
    19  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
    20  `U+0E29 <https://codepoints.net/U+0E29>`_  '\\u0e29'  Lo                  1  THAI CHARACTER SO RUSI
    21  `U+0E32 <https://codepoints.net/U+0E32>`_  '\\u0e32'  Lo                  1  THAI CHARACTER SARA AA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 21


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xaa\xe0\xb8\xad\xe0\xb8\x99\xe0\xb9\x81\xe0\xb8\xa5\xe0\xb8\xb0\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa8\xe0\xb8\xb6\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2|\\n1234567890123456789|\\n"
        ด้วยการสอนและการศึกษา|
        1234567890123456789|

- python `wcwidth.wcswidth()`_ measures width 19,
  while *QTerminal* measures width -18.

.. _QTerminallangLao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0EAA <https://codepoints.net/U+0EAA>`_  '\\u0eaa'  Lo                  1  LAO LETTER SO SUNG
     2  `U+0EB4 <https://codepoints.net/U+0EB4>`_  '\\u0eb4'  Mn                  0  LAO VOWEL SIGN I
     3  `U+0E94 <https://codepoints.net/U+0E94>`_  '\\u0e94'  Lo                  1  LAO LETTER DO
     4  `U+0EC0 <https://codepoints.net/U+0EC0>`_  '\\u0ec0'  Lo                  1  LAO VOWEL SIGN E
     5  `U+0EAA <https://codepoints.net/U+0EAA>`_  '\\u0eaa'  Lo                  1  LAO LETTER SO SUNG
     6  `U+0EA5 <https://codepoints.net/U+0EA5>`_  '\\u0ea5'  Lo                  1  LAO LETTER LO LOOT
     7  `U+0EB5 <https://codepoints.net/U+0EB5>`_  '\\u0eb5'  Mn                  0  LAO VOWEL SIGN II
     8  `U+0E9E <https://codepoints.net/U+0E9E>`_  '\\u0e9e'  Lo                  1  LAO LETTER PHO TAM
     9  `U+0EB2 <https://codepoints.net/U+0EB2>`_  '\\u0eb2'  Lo                  1  LAO VOWEL SIGN AA
    10  `U+0E9A <https://codepoints.net/U+0E9A>`_  '\\u0e9a'  Lo                  1  LAO LETTER BO
    11  `U+0EAD <https://codepoints.net/U+0EAD>`_  '\\u0ead'  Lo                  1  LAO LETTER O
    12  `U+0EB1 <https://codepoints.net/U+0EB1>`_  '\\u0eb1'  Mn                  0  LAO VOWEL SIGN MAI KAN
    13  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
    14  `U+0EAA <https://codepoints.net/U+0EAA>`_  '\\u0eaa'  Lo                  1  LAO LETTER SO SUNG
    15  `U+0EB3 <https://codepoints.net/U+0EB3>`_  '\\u0eb3'  Lo                  1  LAO VOWEL SIGN AM
    16  `U+0E84 <https://codepoints.net/U+0E84>`_  '\\u0e84'  Lo                  1  LAO LETTER KHO TAM
    17  `U+0EB1 <https://codepoints.net/U+0EB1>`_  '\\u0eb1'  Mn                  0  LAO VOWEL SIGN MAI KAN
    18  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
    19  `U+0E97 <https://codepoints.net/U+0E97>`_  '\\u0e97'  Lo                  1  LAO LETTER THO TAM
    20  `U+0EB1 <https://codepoints.net/U+0EB1>`_  '\\u0eb1'  Mn                  0  LAO VOWEL SIGN MAI KAN
    21  `U+0E87 <https://codepoints.net/U+0E87>`_  '\\u0e87'  Lo                  1  LAO LETTER NGO
    22  `U+0EA1 <https://codepoints.net/U+0EA1>`_  '\\u0ea1'  Lo                  1  LAO LETTER MO
    23  `U+0EA7 <https://codepoints.net/U+0EA7>`_  '\\u0ea7'  Lo                  1  LAO LETTER WO
    24  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
    25  `U+0EC4 <https://codepoints.net/U+0EC4>`_  '\\u0ec4'  Lo                  1  LAO VOWEL SIGN AI
    26  `U+0E94 <https://codepoints.net/U+0E94>`_  '\\u0e94'  Lo                  1  LAO LETTER DO
    27  `U+0EC9 <https://codepoints.net/U+0EC9>`_  '\\u0ec9'  Mn                  0  LAO TONE MAI THO
    28  `U+0EC0 <https://codepoints.net/U+0EC0>`_  '\\u0ec0'  Lo                  1  LAO VOWEL SIGN E
    29  `U+0E9B <https://codepoints.net/U+0E9B>`_  '\\u0e9b'  Lo                  1  LAO LETTER PO
    30  `U+0EB1 <https://codepoints.net/U+0EB1>`_  '\\u0eb1'  Mn                  0  LAO VOWEL SIGN MAI KAN
    31  `U+0E99 <https://codepoints.net/U+0E99>`_  '\\u0e99'  Lo                  1  LAO LETTER NO
    32  `U+0EC4 <https://codepoints.net/U+0EC4>`_  '\\u0ec4'  Lo                  1  LAO VOWEL SIGN AI
    33  `U+0E9B <https://codepoints.net/U+0E9B>`_  '\\u0e9b'  Lo                  1  LAO LETTER PO
    34  `U+0E97 <https://codepoints.net/U+0E97>`_  '\\u0e97'  Lo                  1  LAO LETTER THO TAM
    35  `U+0EBB <https://codepoints.net/U+0EBB>`_  '\\u0ebb'  Mn                  0  LAO VOWEL SIGN MAI KON
    36  `U+0EC8 <https://codepoints.net/U+0EC8>`_  '\\u0ec8'  Mn                  0  LAO TONE MAI EK
    37  `U+0EA7 <https://codepoints.net/U+0EA7>`_  '\\u0ea7'  Lo                  1  LAO LETTER WO
    38  `U+0EC2 <https://codepoints.net/U+0EC2>`_  '\\u0ec2'  Lo                  1  LAO VOWEL SIGN O
    39  `U+0EA5 <https://codepoints.net/U+0EA5>`_  '\\u0ea5'  Lo                  1  LAO LETTER LO LOOT
    40  `U+0E81 <https://codepoints.net/U+0E81>`_  '\\u0e81'  Lo                  1  LAO LETTER KO
    41  `U+0EA2 <https://codepoints.net/U+0EA2>`_  '\\u0ea2'  Lo                  1  LAO LETTER YO
    42  `U+0EC8 <https://codepoints.net/U+0EC8>`_  '\\u0ec8'  Mn                  0  LAO TONE MAI EK
    43  `U+0EB2 <https://codepoints.net/U+0EB2>`_  '\\u0eb2'  Lo                  1  LAO VOWEL SIGN AA
    44  `U+0E87 <https://codepoints.net/U+0E87>`_  '\\u0e87'  Lo                  1  LAO LETTER NGO
    45  `U+0E9B <https://codepoints.net/U+0E9B>`_  '\\u0e9b'  Lo                  1  LAO LETTER PO
    46  `U+0EB0 <https://codepoints.net/U+0EB0>`_  '\\u0eb0'  Lo                  1  LAO VOWEL SIGN A
    47  `U+0E88 <https://codepoints.net/U+0E88>`_  '\\u0e88'  Lo                  1  LAO LETTER CO
    48  `U+0EB1 <https://codepoints.net/U+0EB1>`_  '\\u0eb1'  Mn                  0  LAO VOWEL SIGN MAI KAN
    49  `U+0E81 <https://codepoints.net/U+0E81>`_  '\\u0e81'  Lo                  1  LAO LETTER KO
    50  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 50


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xba\xaa\xe0\xba\xb4\xe0\xba\x94\xe0\xbb\x80\xe0\xba\xaa\xe0\xba\xa5\xe0\xba\xb5\xe0\xba\x9e\xe0\xba\xb2\xe0\xba\x9a\xe0\xba\xad\xe0\xba\xb1\xe0\xba\x99\xe0\xba\xaa\xe0\xba\xb3\xe0\xba\x84\xe0\xba\xb1\xe0\xba\x99\xe0\xba\x97\xe0\xba\xb1\xe0\xba\x87\xe0\xba\xa1\xe0\xba\xa7\xe0\xba\x99\xe0\xbb\x84\xe0\xba\x94\xe0\xbb\x89\xe0\xbb\x80\xe0\xba\x9b\xe0\xba\xb1\xe0\xba\x99\xe0\xbb\x84\xe0\xba\x9b\xe0\xba\x97\xe0\xba\xbb\xe0\xbb\x88\xe0\xba\xa7\xe0\xbb\x82\xe0\xba\xa5\xe0\xba\x81\xe0\xba\xa2\xe0\xbb\x88\xe0\xba\xb2\xe0\xba\x87\xe0\xba\x9b\xe0\xba\xb0\xe0\xba\x88\xe0\xba\xb1\xe0\xba\x81.|\\n123456789012345678901234567890123456789|\\n"
        ສິດເສລີພາບອັນສຳຄັນທັງມວນໄດ້ເປັນໄປທົ່ວໂລກຢ່າງປະຈັກ.|
        123456789012345678901234567890123456789|

- python `wcwidth.wcswidth()`_ measures width 39,
  while *QTerminal* measures width 36.

.. _QTerminallangKhmerCentral:

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+1798 <https://codepoints.net/U+1798>`_  '\\u1798'  Lo                  1  KHMER LETTER MO
     2  `U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
     3  `U+178F <https://codepoints.net/U+178F>`_  '\\u178f'  Lo                  1  KHMER LETTER TA
     4  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
     5  `U+179A <https://codepoints.net/U+179A>`_  '\\u179a'  Lo                  1  KHMER LETTER RO
     6  `U+17B6 <https://codepoints.net/U+17B6>`_  '\\u17b6'  Mc                  0  KHMER VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x98\xe1\x9e\xb6\xe1\x9e\x8f\xe1\x9f\x92\xe1\x9e\x9a\xe1\x9e\xb6|\\n123|\\n"
        មាត្រា|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *QTerminal* measures width -37.

.. _QTerminallangKhn:

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================================
     1  `U+1A37 <https://codepoints.net/U+1A37>`_  '\\u1a37'  Lo                  1  TAI THAM LETTER BA
     2  `U+1A55 <https://codepoints.net/U+1A55>`_  '\\u1a55'  Mc                  0  TAI THAM CONSONANT SIGN MEDIAL RA
     3  `U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
     4  `U+1A48 <https://codepoints.net/U+1A48>`_  '\\u1a48'  Lo                  1  TAI THAM LETTER HIGH SA
     5  `U+1A27 <https://codepoints.net/U+1A27>`_  '\\u1a27'  Lo                  1  TAI THAM LETTER HIGH CA
     6  `U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
     7  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
     8  `U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
     9  `U+1A48 <https://codepoints.net/U+1A48>`_  '\\u1a48'  Lo                  1  TAI THAM LETTER HIGH SA
    10  `U+1A6E <https://codepoints.net/U+1A6E>`_  '\\u1a6e'  Mc                  0  TAI THAM VOWEL SIGN E
    11  `U+1A3F <https://codepoints.net/U+1A3F>`_  '\\u1a3f'  Lo                  1  TAI THAM LETTER LOW YA
    12  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    13  `U+1A26 <https://codepoints.net/U+1A26>`_  '\\u1a26'  Lo                  1  TAI THAM LETTER NGA
    14  `U+1A62 <https://codepoints.net/U+1A62>`_  '\\u1a62'  Mn                  0  TAI THAM VOWEL SIGN MAI SAT
    15  `U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
    16  `U+1A63 <https://codepoints.net/U+1A63>`_  '\\u1a63'  Mc                  0  TAI THAM VOWEL SIGN AA
    17  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    18  `U+1A41 <https://codepoints.net/U+1A41>`_  '\\u1a41'  Lo                  1  TAI THAM LETTER RA
    19  `U+1A43 <https://codepoints.net/U+1A43>`_  '\\u1a43'  Lo                  1  TAI THAM LETTER LA
    20  `U+1A6E <https://codepoints.net/U+1A6E>`_  '\\u1a6e'  Mc                  0  TAI THAM VOWEL SIGN E
    21  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    22  `U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
    23  `U+1A68 <https://codepoints.net/U+1A68>`_  '\\u1a68'  Mn                  0  TAI THAM VOWEL SIGN UUE
    24  `U+1A37 <https://codepoints.net/U+1A37>`_  '\\u1a37'  Lo                  1  TAI THAM LETTER BA
    25  `U+1A2D <https://codepoints.net/U+1A2D>`_  '\\u1a2d'  Lo                  1  TAI THAM LETTER RATA
    26  `U+1A65 <https://codepoints.net/U+1A65>`_  '\\u1a65'  Mn                  0  TAI THAM VOWEL SIGN I
    27  `U+1A37 <https://codepoints.net/U+1A37>`_  '\\u1a37'  Lo                  1  TAI THAM LETTER BA
    28  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
    29  `U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
    30  `U+1A65 <https://codepoints.net/U+1A65>`_  '\\u1a65'  Mn                  0  TAI THAM VOWEL SIGN I
    31  `U+1A32 <https://codepoints.net/U+1A32>`_  '\\u1a32'  Lo                  1  TAI THAM LETTER HIGH TA
    32  `U+1A73 <https://codepoints.net/U+1A73>`_  '\\u1a73'  Mn                  0  TAI THAM VOWEL SIGN OA ABOVE
    33  `U+1A75 <https://codepoints.net/U+1A75>`_  '\\u1a75'  Mn                  0  TAI THAM SIGN TONE-1
   ===  =========================================  =========  ==========  =========  =================================

Total codepoints: 33


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xb7\xe1\xa9\x95\xe1\xa9\xa3\xe1\xa9\x88\xe1\xa8\xa7\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa8\xa0\xe1\xa9\x88\xe1\xa9\xae\xe1\xa8\xbf\xe1\xa9\xa0\xe1\xa8\xa6\xe1\xa9\xa2\xe1\xa8\xa0\xe1\xa9\xa3\xe1\xa9\xa0\xe1\xa9\x81\xe1\xa9\x83\xe1\xa9\xae\xe1\xa9\xa0\xe1\xa8\xa0\xe1\xa9\xa8\xe1\xa8\xb7\xe1\xa8\xad\xe1\xa9\xa5\xe1\xa8\xb7\xe1\xa9\xa0\xe1\xa8\xb2\xe1\xa9\xa5\xe1\xa8\xb2\xe1\xa9\xb3\xe1\xa9\xb5|\\n1234567890123456|\\n"
        ᨷᩕᩣᩈᨧᩣ᩠ᨠᩈᩮᨿ᩠ᨦᩢᨠᩣ᩠ᩁᩃᩮ᩠ᨠᩨᨷᨭᩥᨷ᩠ᨲᩥᨲᩳ᩵|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *QTerminal* measures width -2.

.. _QTerminallangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0054 <https://codepoints.net/U+0054>`_  'T'       Lu                  1  LATIN CAPITAL LETTER T
     2  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     3  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Ts\xc3\xa1|\\n123|\\n"
        Tsá|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *QTerminal* measures width -12.

.. _QTerminallangMarathi:

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     2  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
     3  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     4  `U+0923 <https://codepoints.net/U+0923>`_  '\\u0923'  Lo                  1  DEVANAGARI LETTER NNA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb5\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xa3|\\n123|\\n"
        वर्ण|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *QTerminal* measures width 0.

.. _QTerminallangGumuz:

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "maayira|\\n1234567|\\n"
        maayira|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *QTerminal* measures width -7.

.. _QTerminallangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pisa|\\n1234|\\n"
        pisa|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *QTerminal* measures width -4.

.. _QTerminallangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     5  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     8  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     9  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
    10  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
    11  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "janb\xc3\xadsacana|\\n12345678901|\\n"
        janbísacana|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *QTerminal* measures width 8.

.. _QTerminallangNepali:

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
  while *QTerminal* measures width 6.

.. _QTerminallangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     3  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     5  `U+02BC <https://codepoints.net/U+02BC>`_  '\\u02bc'  Lm                  1  MODIFIER LETTER APOSTROPHE
     6  `U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
     7  `U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc3\xad\xc3\xadt\xca\xbc\xc3\xa9\xc3\xa9|\\n1234567|\\n"
        níítʼéé|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *QTerminal* measures width 3.

.. _QTerminallangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================================
     1  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
     2  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     3  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     4  `U+0435 <https://codepoints.net/U+0435>`_  '\\u0435'  Ll                  1  CYRILLIC SMALL LETTER IE
     5  `U+043C <https://codepoints.net/U+043C>`_  '\\u043c'  Ll                  1  CYRILLIC SMALL LETTER EM
     6  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
     7  `U+04C8 <https://codepoints.net/U+04C8>`_  '\\u04c8'  Ll                  1  CYRILLIC SMALL LETTER EN WITH HOOK
     8  `U+0433 <https://codepoints.net/U+0433>`_  '\\u0433'  Ll                  1  CYRILLIC SMALL LETTER GHE
     9  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
    10  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
    11  `U+044D <https://codepoints.net/U+044D>`_  '\\u044d'  Ll                  1  CYRILLIC SMALL LETTER E
    12  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
    13  `U+0306 <https://codepoints.net/U+0306>`_  '\\u0306'  Mn                  0  COMBINING BREVE
    14  `U+0447 <https://codepoints.net/U+0447>`_  '\\u0447'  Ll                  1  CYRILLIC SMALL LETTER CHE
    15  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
    16  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ==================================

Total codepoints: 16


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x82\xd1\x8d\xd0\xb4\xd0\xb5\xd0\xbc\xd1\x8d\xd3\x88\xd0\xb3\xd0\xb8\xd0\xbb\xd1\x8d\xd0\xb8\xcc\x86\xd1\x87\xd0\xb8.|\\n123456789012345|\\n"
        тэдемэӈгилэйчи.|
        123456789012345|

- python `wcwidth.wcswidth()`_ measures width 15,
  while *QTerminal* measures width 1.

.. _QTerminallangBengali:

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
  while *QTerminal* measures width 6.

.. _QTerminallangAmarakaeri:

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
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     8  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     9  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "huadariyo|\\n123456789|\\n"
        huadariyo|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *QTerminal* measures width 3.

.. _QTerminallangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
     2  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     3  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     4  `U+0433 <https://codepoints.net/U+0433>`_  '\\u0433'  Ll                  1  CYRILLIC SMALL LETTER GHE
     5  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     6  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     7  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     8  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     9  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbe\xcc\x84\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd1\x83\xd0\xbd\xd0\xb8|\\n12345678|\\n"
        о̄ргануни|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *QTerminal* measures width 4.

.. _QTerminallangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ama|\\n123|\\n"
        ama|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *QTerminal* measures width -12.

.. _QTerminallangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===================================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===================================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     4  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     7  `U+00EB <https://codepoints.net/U+00EB>`_  '\\xeb'   Ll                  1  LATIN SMALL LETTER E WITH DIAERESIS
   ===  =========================================  ========  ==========  =========  ===================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "cahues\xc3\xab|\\n1234567|\\n"
        cahuesë|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *QTerminal* measures width -7.

.. _QTerminallangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================================
     1  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     2  `U+030C <https://codepoints.net/U+030C>`_  '\\u030c'  Mn                  0  COMBINING CARON
     3  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     4  `U+04CA <https://codepoints.net/U+04CA>`_  '\\u04ca'  Ll                  1  CYRILLIC SMALL LETTER EN WITH TAIL
     5  `U+04F7 <https://codepoints.net/U+04F7>`_  '\\u04f7'  Ll                  1  CYRILLIC SMALL LETTER GHE WITH DESCENDER
     6  `U+0493 <https://codepoints.net/U+0493>`_  '\\u0493'  Ll                  1  CYRILLIC SMALL LETTER GHE WITH STROKE
     7  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     8  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     9  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
    10  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
    11  `U+04CA <https://codepoints.net/U+04CA>`_  '\\u04ca'  Ll                  1  CYRILLIC SMALL LETTER EN WITH TAIL
   ===  =========================================  =========  ==========  =========  ========================================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x80\xcc\x8c\xd0\xb0\xd3\x8a\xd3\xb7\xd2\x93\xd1\x83\xd0\xbd\xd0\xb4\xd0\xb8\xd3\x8a|\\n1234567890|\\n"
        р̌аӊӷғундиӊ|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *QTerminal* measures width -2.

.. _QTerminallangVeps:

Veps
^^^^

Sequence of language *Veps* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     5  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "nenid|\\n12345|\\n"
        nenid|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width -4.

.. _QTerminallangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0443 <https://codepoints.net/U+0443>`_  '\\u0443'  Ll                  1  CYRILLIC SMALL LETTER U
     2  `U+043F <https://codepoints.net/U+043F>`_  '\\u043f'  Ll                  1  CYRILLIC SMALL LETTER PE
     3  `U+043A <https://codepoints.net/U+043A>`_  '\\u043a'  Ll                  1  CYRILLIC SMALL LETTER KA
     4  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     5  `U+0447 <https://codepoints.net/U+0447>`_  '\\u0447'  Ll                  1  CYRILLIC SMALL LETTER CHE
     6  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
     7  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x83\xd0\xbf\xd0\xba\xd0\xb0\xd1\x87\xd0\xb8\xd0\xbd|\\n1234567|\\n"
        упкачин|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *QTerminal* measures width -1.

.. _QTerminallangShan:

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+1081 <https://codepoints.net/U+1081>`_  '\\u1081'  Lo                  1  MYANMAR LETTER SHAN HA
     2  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
     3  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
     4  `U+101D <https://codepoints.net/U+101D>`_  '\\u101d'  Lo                  1  MYANMAR LETTER WA
     5  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x82\x81\xe1\x80\xad\xe1\x80\xaf\xe1\x80\x9d\xe1\x80\xba|\\n12|\\n"
        ႁိုဝ်|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -2.

.. _QTerminallangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0042 <https://codepoints.net/U+0042>`_  'B'        Lu                  1  LATIN CAPITAL LETTER B
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     7  `U+0327 <https://codepoints.net/U+0327>`_  '\\u0327'  Mn                  0  COMBINING CEDILLA
     8  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     9  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
    10  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
    11  `U+0327 <https://codepoints.net/U+0327>`_  '\\u0327'  Mn                  0  COMBINING CEDILLA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Birles\xcc\xa7mis\xcc\xa7|\\n123456789|\\n"
        Birleşmiş|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *QTerminal* measures width 0.

.. _QTerminallangSecoya:

Secoya
^^^^^^

Sequence of language *Secoya* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     6  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     7  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     8  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     9  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kuade'oye|\\n123456789|\\n"
        kuade'oye|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *QTerminal* measures width -1.

.. _QTerminallangMon:

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
     2  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
     3  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
     4  `U+103F <https://codepoints.net/U+103F>`_  '\\u103f'  Lo                  1  MYANMAR LETTER GREAT SA
     5  `U+102E <https://codepoints.net/U+102E>`_  '\\u102e'  Mn                  0  MYANMAR VOWEL SIGN II
     6  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
     7  `U+1010 <https://codepoints.net/U+1010>`_  '\\u1010'  Lo                  1  MYANMAR LETTER TA
     8  `U+1021 <https://codepoints.net/U+1021>`_  '\\u1021'  Lo                  1  MYANMAR LETTER A
     9  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    10  `U+101D <https://codepoints.net/U+101D>`_  '\\u101d'  Lo                  1  MYANMAR LETTER WA
    11  `U+103D <https://codepoints.net/U+103D>`_  '\\u103d'  Mn                  0  MYANMAR CONSONANT SIGN MEDIAL WA
    12  `U+1036 <https://codepoints.net/U+1036>`_  '\\u1036'  Mn                  0  MYANMAR SIGN ANUSVARA
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\xa1\xe1\x80\xad\xe1\x80\xaf\xe1\x80\xbf\xe1\x80\xae\xe1\x80\xaf\xe1\x80\x90\xe1\x80\xa1\xe1\x80\xba\xe1\x80\x9d\xe1\x80\xbd\xe1\x80\xb6|\\n12345|\\n"
        အိုဿီုတအ်ဝွံ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width 0.

.. _QTerminallangKorean:

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+D589 <https://codepoints.net/U+D589>`_  '\\ud589'  Lo                  2  HANGUL SYLLABLE HAENG
     2  `U+B3D9 <https://codepoints.net/U+B3D9>`_  '\\ub3d9'  Lo                  2  HANGUL SYLLABLE DONG
     3  `U+D558 <https://codepoints.net/U+D558>`_  '\\ud558'  Lo                  2  HANGUL SYLLABLE HA
     4  `U+C5EC <https://codepoints.net/U+C5EC>`_  '\\uc5ec'  Lo                  2  HANGUL SYLLABLE YEO
     5  `U+C57C <https://codepoints.net/U+C57C>`_  '\\uc57c'  Lo                  2  HANGUL SYLLABLE YA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xed\x96\x89\xeb\x8f\x99\xed\x95\x98\xec\x97\xac\xec\x95\xbc|\\n1234567890|\\n"
        행동하여야|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *QTerminal* measures width 2.

.. _QTerminallangBurmese:

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
     2  `U+103C <https://codepoints.net/U+103C>`_  '\\u103c'  Mc                  0  MYANMAR CONSONANT SIGN MEDIAL RA
     3  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
     4  `U+100A <https://codepoints.net/U+100A>`_  '\\u100a'  Lo                  1  MYANMAR LETTER NNYA
     5  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
     6  `U+1005 <https://codepoints.net/U+1005>`_  '\\u1005'  Lo                  1  MYANMAR LETTER CA
     7  `U+102C <https://codepoints.net/U+102C>`_  '\\u102c'  Mc                  0  MYANMAR VOWEL SIGN AA
     8  `U+1010 <https://codepoints.net/U+1010>`_  '\\u1010'  Lo                  1  MYANMAR LETTER TA
     9  `U+1019 <https://codepoints.net/U+1019>`_  '\\u1019'  Lo                  1  MYANMAR LETTER MA
    10  `U+103A <https://codepoints.net/U+103A>`_  '\\u103a'  Mn                  0  MYANMAR SIGN ASAT
    11  `U+1038 <https://codepoints.net/U+1038>`_  '\\u1038'  Mc                  0  MYANMAR SIGN VISARGA
    12  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
    13  `U+102D <https://codepoints.net/U+102D>`_  '\\u102d'  Mn                  0  MYANMAR VOWEL SIGN I
    14  `U+102F <https://codepoints.net/U+102F>`_  '\\u102f'  Mn                  0  MYANMAR VOWEL SIGN U
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x80\xe1\x80\xbc\xe1\x80\xb1\xe1\x80\x8a\xe1\x80\xac\xe1\x80\x85\xe1\x80\xac\xe1\x80\x90\xe1\x80\x99\xe1\x80\xba\xe1\x80\xb8\xe1\x80\x80\xe1\x80\xad\xe1\x80\xaf|\\n123456|\\n"
        ကြေညာစာတမ်းကို|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width -3.

.. _QTerminallangSanskrit:

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+091C <https://codepoints.net/U+091C>`_  '\\u091c'  Lo                  1  DEVANAGARI LETTER JA
     2  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     3  `U+0903 <https://codepoints.net/U+0903>`_  '\\u0903'  Mc                  0  DEVANAGARI SIGN VISARGA
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x9c\xe0\xa4\xa8\xe0\xa4\x83|\\n12|\\n"
        जनः|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -3.

.. _QTerminallangSanskritGrantha:

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ====================
     1  `U+0001131C <https://codepoints.net/U+0001131C>`_  '\\U0001131c'  Lo                  1  GRANTHA LETTER JA
     2  `U+00011328 <https://codepoints.net/U+00011328>`_  '\\U00011328'  Lo                  1  GRANTHA LETTER NA
     3  `U+00011303 <https://codepoints.net/U+00011303>`_  '\\U00011303'  Mc                  0  GRANTHA SIGN VISARGA
   ===  =================================================  =============  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\x9c\xf0\x91\x8c\xa8\xf0\x91\x8c\x83|\\n12|\\n"
        𑌜𑌨𑌃|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -3.

.. _QTerminallangTamilSriLanka:

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
     2  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     3  `U+0BAF <https://codepoints.net/U+0BAF>`_  '\\u0baf'  Lo                  1  TAMIL LETTER YA
     4  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
     5  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     6  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
     7  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xae\xe0\xaf\x81\xe0\xae\xaf\xe0\xae\xb2\xe0\xaf\x81\xe0\xae\xae\xe0\xaf\x8d|\\n1234|\\n"
        முயலும்|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *QTerminal* measures width 0.

.. _QTerminallangTamil:

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
     2  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     3  `U+0BAF <https://codepoints.net/U+0BAF>`_  '\\u0baf'  Lo                  1  TAMIL LETTER YA
     4  `U+0BB2 <https://codepoints.net/U+0BB2>`_  '\\u0bb2'  Lo                  1  TAMIL LETTER LA
     5  `U+0BC1 <https://codepoints.net/U+0BC1>`_  '\\u0bc1'  Mc                  0  TAMIL VOWEL SIGN U
     6  `U+0BAE <https://codepoints.net/U+0BAE>`_  '\\u0bae'  Lo                  1  TAMIL LETTER MA
     7  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\xae\xe0\xaf\x81\xe0\xae\xaf\xe0\xae\xb2\xe0\xaf\x81\xe0\xae\xae\xe0\xaf\x8d|\\n1234|\\n"
        முயலும்|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *QTerminal* measures width 0.

.. _QTerminallangColorado:

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
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "manta|\\n12345|\\n"
        manta|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width -7.

.. _QTerminallangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+C0AC <https://codepoints.net/U+C0AC>`_  '\\uc0ac'  Lo                  2  HANGUL SYLLABLE SA
     2  `U+B78C <https://codepoints.net/U+B78C>`_  '\\ub78c'  Lo                  2  HANGUL SYLLABLE RAM
     3  `U+C758 <https://codepoints.net/U+C758>`_  '\\uc758'  Lo                  2  HANGUL SYLLABLE YI
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x82\xac\xeb\x9e\x8c\xec\x9d\x98|\\n123456|\\n"
        사람의|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width -1.

.. _QTerminallangKannada:

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0CAF <https://codepoints.net/U+0CAF>`_  '\\u0caf'  Lo                  1  KANNADA LETTER YA
     2  `U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
     3  `U+0CB5 <https://codepoints.net/U+0CB5>`_  '\\u0cb5'  Lo                  1  KANNADA LETTER VA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\xaf\xe0\xb2\xbe\xe0\xb2\xb5|\\n12|\\n"
        ಯಾವ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -6.

.. _QTerminallangCatalan2:

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
  while *QTerminal* measures width -10.

.. _QTerminallangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     3  `U+0077 <https://codepoints.net/U+0077>`_  'w'        Ll                  1  LATIN SMALL LETTER W
     4  `U+028A <https://codepoints.net/U+028A>`_  '\\u028a'  Ll                  1  LATIN SMALL LETTER UPSILON
     5  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     6  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     7  `U+0269 <https://codepoints.net/U+0269>`_  '\\u0269'  Ll                  1  LATIN SMALL LETTER IOTA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "b\xc9\x94w\xca\x8a\xcc\x81t\xc9\xa9|\\n123456|\\n"
        bɔwʊ́tɩ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width 0.

.. _QTerminallangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     2  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     3  `U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
     5  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     6  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     8  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     9  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
    10  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
    11  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
    12  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "amporta\xcc\x81ncia|\\n12345678901|\\n"
        amportáncia|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *QTerminal* measures width 6.

.. _QTerminallangTelugu:

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0C32 <https://codepoints.net/U+0C32>`_  '\\u0c32'  Lo                  1  TELUGU LETTER LA
     2  `U+0C47 <https://codepoints.net/U+0C47>`_  '\\u0c47'  Mn                  0  TELUGU VOWEL SIGN EE
     3  `U+0C15 <https://codepoints.net/U+0C15>`_  '\\u0c15'  Lo                  1  TELUGU LETTER KA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\xb2\xe0\xb1\x87\xe0\xb0\x95|\\n12|\\n"
        లేక|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -14.

.. _QTerminallangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "totes|\\n12345|\\n"
        totes|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width -5.

.. _QTerminallangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0726 <https://codepoints.net/U+0726>`_  '\\u0726'  Lo                  1  SYRIAC LETTER PE
     2  `U+072A <https://codepoints.net/U+072A>`_  '\\u072a'  Lo                  1  SYRIAC LETTER RISH
     3  `U+0723 <https://codepoints.net/U+0723>`_  '\\u0723'  Lo                  1  SYRIAC LETTER SEMKATH
     4  `U+0718 <https://codepoints.net/U+0718>`_  '\\u0718'  Lo                  1  SYRIAC LETTER WAW
     5  `U+0726 <https://codepoints.net/U+0726>`_  '\\u0726'  Lo                  1  SYRIAC LETTER PE
     6  `U+071D <https://codepoints.net/U+071D>`_  '\\u071d'  Lo                  1  SYRIAC LETTER YUDH
     7  `U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
     8  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\xa6\xdc\xaa\xdc\xa3\xdc\x98\xdc\xa6\xdc\x9d\xdc\x90.|\\n12345678|\\n"
        ܦܪܣܘܦܝܐ.|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *QTerminal* measures width 3.

.. _QTerminallangTicuna:

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'        Ll                  1  LATIN SMALL LETTER U
     3  `U+0078 <https://codepoints.net/U+0078>`_  'x'        Ll                  1  LATIN SMALL LETTER X
     4  `U+00FC <https://codepoints.net/U+00FC>`_  '\\xfc'    Ll                  1  LATIN SMALL LETTER U WITH DIAERESIS
     5  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
     6  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gux\xc3\xbc\xcc\x83ma|\\n123456|\\n"
        guxü̃ma|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width 5.

.. _QTerminallangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+05D6 <https://codepoints.net/U+05D6>`_  '\\u05d6'  Lo                  1  HEBREW LETTER ZAYIN
     2  `U+05D0 <https://codepoints.net/U+05D0>`_  '\\u05d0'  Lo                  1  HEBREW LETTER ALEF
     3  `U+05B8 <https://codepoints.net/U+05B8>`_  '\\u05b8'  Mn                  0  HEBREW POINT QAMATS
     4  `U+05DC <https://codepoints.net/U+05DC>`_  '\\u05dc'  Lo                  1  HEBREW LETTER LAMED
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\x96\xd7\x90\xd6\xb8\xd7\x9c|\\n123|\\n"
        זאָל|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *QTerminal* measures width -5.

.. _QTerminallangKabyle:

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
  while *QTerminal* measures width -7.

.. _QTerminallangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

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
  while *QTerminal* measures width -4.

.. _QTerminallangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     4  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     5  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     6  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     7  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     8  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "amechruk|\\n12345678|\\n"
        amechruk|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *QTerminal* measures width 1.

.. _QTerminallangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

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
  while *QTerminal* measures width -5.

.. _QTerminallangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'       Ll                  1  LATIN SMALL LETTER C
     2  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     3  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     5  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     6  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     7  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     8  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     9  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
    10  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
    11  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
    12  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "chjejutrjoji|\\n123456789012|\\n"
        chjejutrjoji|
        123456789012|

- python `wcwidth.wcswidth()`_ measures width 12,
  while *QTerminal* measures width 7.

.. _QTerminallangw:

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     3  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     6  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     7  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     8  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "g\xc9\x94mesese|\\n12345678|\\n"
        gɔmesese|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *QTerminal* measures width -4.

.. _QTerminallangMaldivian:

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
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 12


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x99\xde\xa6\xde\x87\xde\xb0\xde\xa4\xde\xaa\xde\x8c\xde\xa6\xde\x86\xde\xa7\xde\x87\xde\xa8|\\n123456|\\n"
        ޙައްޤުތަކާއި|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width 2.

.. _QTerminallangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0066 <https://codepoints.net/U+0066>`_  'f'        Ll                  1  LATIN SMALL LETTER F
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
     4  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     6  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     7  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     8  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "fe\xcc\x80yenns|\\n1234567|\\n"
        fèyenns|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *QTerminal* measures width 3.

.. _QTerminallangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ====================
     1  `U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
   ===  =================================================  =============  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xab|\\n1|\\n"
        𞤫|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *QTerminal* measures width -3.

.. _QTerminallangUduk:

Uduk
^^^^

Sequence of language *Uduk* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     2  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     3  `U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     5  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     7  `U+002F <https://codepoints.net/U+002F>`_  '/'        Po                  1  SOLIDUS
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "en\xe2\x80\x99thi/|\\n1234567|\\n"
        en’thi/|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *QTerminal* measures width 4.

.. _QTerminallangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "be|\\n12|\\n"
        be|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -1.

.. _QTerminallangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     2  `U+0644 <https://codepoints.net/U+0644>`_  '\\u0644'  Lo                  1  ARABIC LETTER LAM
     3  `U+062D <https://codepoints.net/U+062D>`_  '\\u062d'  Lo                  1  ARABIC LETTER HAH
     4  `U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
     5  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     6  `U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa7\xd9\x84\xd8\xad\xd9\x82\xd9\x88\xd9\x82|\\n123456|\\n"
        الحقوق|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *QTerminal* measures width 1.

.. _QTerminallangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     3  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     4  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     5  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "m\xc9\x94d\xc9\x9b\xc5\x8b|\\n12345|\\n"
        mɔdɛŋ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width 0.

.. _QTerminallangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     2  `U+0304 <https://codepoints.net/U+0304>`_  '\\u0304'  Mn                  0  COMBINING MACRON
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     5  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "e\xcc\x84nei|\\n1234|\\n"
        ēnei|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *QTerminal* measures width 2.

.. _QTerminallangMixtecMetlatnoc:

Mixtec, Metlatónoc
^^^^^^^^^^^^^^^^^^

Sequence of language *Mixtec, Metlatónoc* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ni|\\n12|\\n"
        ni|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -3.

.. _QTerminallangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

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
  while *QTerminal* measures width -11.

.. _QTerminallangChinantecChiltepec:

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===================================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===================================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+00F6 <https://codepoints.net/U+00F6>`_  '\\xf6'   Ll                  1  LATIN SMALL LETTER O WITH DIAERESIS
   ===  =========================================  ========  ==========  =========  ===================================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "k\xc3\xb6|\\n12|\\n"
        kö|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -1.

.. _QTerminallangMor:

Mòoré
^^^^^

Sequence of language *Mòoré* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "a|\\n1|\\n"
        a|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *QTerminal* measures width -2.

.. _QTerminallangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+00E0 <https://codepoints.net/U+00E0>`_  '\\xe0'    Ll                  1  LATIN SMALL LETTER A WITH GRAVE
     2  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     3  `U+00FA <https://codepoints.net/U+00FA>`_  '\\xfa'    Ll                  1  LATIN SMALL LETTER U WITH ACUTE
     4  `U+1E63 <https://codepoints.net/U+1E63>`_  '\\u1e63'  Ll                  1  LATIN SMALL LETTER S WITH DOT BELOW
     5  `U+1EB9 <https://codepoints.net/U+1EB9>`_  '\\u1eb9'  Ll                  1  LATIN SMALL LETTER E WITH DOT BELOW
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xa0m\xc3\xba\xe1\xb9\xa3\xe1\xba\xb9|\\n12345|\\n"
        àmúṣẹ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width 3.

.. _QTerminallangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0066 <https://codepoints.net/U+0066>`_  'f'        Ll                  1  LATIN SMALL LETTER F
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     3  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "fe\xcc\x80|\\n12|\\n"
        fè|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -3.

.. _QTerminallangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================================
     1  `U+0076 <https://codepoints.net/U+0076>`_  'v'        Ll                  1  LATIN SMALL LETTER V
     2  `U+00EA <https://codepoints.net/U+00EA>`_  '\\xea'    Ll                  1  LATIN SMALL LETTER E WITH CIRCUMFLEX
     3  `U+0300 <https://codepoints.net/U+0300>`_  '\\u0300'  Mn                  0  COMBINING GRAVE ACCENT
   ===  =========================================  =========  ==========  =========  ====================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "v\xc3\xaa\xcc\x80|\\n12|\\n"
        về|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -2.

.. _QTerminallangJavaneseJavanese:

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+A9B2 <https://codepoints.net/U+A9B2>`_  '\\ua9b2'  Lo                  1  JAVANESE LETTER HA
     2  `U+A981 <https://codepoints.net/U+A981>`_  '\\ua981'  Mn                  0  JAVANESE SIGN CECAK
     3  `U+A992 <https://codepoints.net/U+A992>`_  '\\ua992'  Lo                  1  JAVANESE LETTER GA
     4  `U+A9BA <https://codepoints.net/U+A9BA>`_  '\\ua9ba'  Mc                  0  JAVANESE VOWEL SIGN TALING
     5  `U+A9B4 <https://codepoints.net/U+A9B4>`_  '\\ua9b4'  Mc                  0  JAVANESE VOWEL SIGN TARUNG
     6  `U+A9A4 <https://codepoints.net/U+A9A4>`_  '\\ua9a4'  Lo                  1  JAVANESE LETTER NA
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\xb2\xea\xa6\x81\xea\xa6\x92\xea\xa6\xba\xea\xa6\xb4\xea\xa6\xa4|\\n123|\\n"
        ꦲꦁꦒꦺꦴꦤ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *QTerminal* measures width -2.

.. _QTerminallangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88|\\n1|\\n"
        و|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *QTerminal* measures width -6.

.. _QTerminallangDagaareSouthern:

Dagaare, Southern
^^^^^^^^^^^^^^^^^

Sequence of language *Dagaare, Southern* from midpoint of alignment failure records:

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
  while *QTerminal* measures width -2.

.. _QTerminallangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "a|\\n1|\\n"
        a|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *QTerminal* measures width -2.

.. _QTerminallangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     2  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     4  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     5  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     6  `U+00E0 <https://codepoints.net/U+00E0>`_  '\\xe0'   Ll                  1  LATIN SMALL LETTER A WITH GRAVE
     7  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "shish\xc3\xa0r|\\n1234567|\\n"
        shishàr|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *QTerminal* measures width 0.

.. _QTerminallangUrdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     2  `U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x86\xdb\x92|\\n12|\\n"
        نے|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -3.

.. _QTerminallangPashtoNorthern:

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
  while *QTerminal* measures width -3.

.. _QTerminallangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
     2  `U+06C1 <https://codepoints.net/U+06C1>`_  '\\u06c1'  Lo                  1  ARABIC LETTER HEH GOAL
     3  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     4  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xb1\xdb\x81\xd9\x88\xd9\x86|\\n1234|\\n"
        رہون|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *QTerminal* measures width -5.

.. _QTerminallangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0077 <https://codepoints.net/U+0077>`_  'w'       Ll                  1  LATIN SMALL LETTER W
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "we|\\n12|\\n"
        we|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width 0.

.. _QTerminallangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0628 <https://codepoints.net/U+0628>`_  '\\u0628'  Lo                  1  ARABIC LETTER BEH
     2  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\xa8\xd8\xa7|\\n12|\\n"
        با|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -3.

.. _QTerminallangUrdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0646 <https://codepoints.net/U+0646>`_  '\\u0646'  Lo                  1  ARABIC LETTER NOON
     2  `U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x86\xdb\x92|\\n12|\\n"
        نے|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -3.

.. _QTerminallangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ti|\\n12|\\n"
        ti|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -5.

.. _QTerminallangMaithili:

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

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
  while *QTerminal* measures width 1.

.. _QTerminallangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

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
  while *QTerminal* measures width -3.

.. _QTerminallangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     2  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     3  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "r\xc9\x94t|\\n123|\\n"
        rɔt|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *QTerminal* measures width 1.

.. _QTerminallangGujarati:

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0A86 <https://codepoints.net/U+0A86>`_  '\\u0a86'  Lo                  1  GUJARATI LETTER AA
     2  `U+0A82 <https://codepoints.net/U+0A82>`_  '\\u0a82'  Mn                  0  GUJARATI SIGN ANUSVARA
     3  `U+0AA4 <https://codepoints.net/U+0AA4>`_  '\\u0aa4'  Lo                  1  GUJARATI LETTER TA
     4  `U+0AB0 <https://codepoints.net/U+0AB0>`_  '\\u0ab0'  Lo                  1  GUJARATI LETTER RA
     5  `U+0AB0 <https://codepoints.net/U+0AB0>`_  '\\u0ab0'  Lo                  1  GUJARATI LETTER RA
     6  `U+0ABE <https://codepoints.net/U+0ABE>`_  '\\u0abe'  Mc                  0  GUJARATI VOWEL SIGN AA
     7  `U+0AB7 <https://codepoints.net/U+0AB7>`_  '\\u0ab7'  Lo                  1  GUJARATI LETTER SSA
     8  `U+0ACD <https://codepoints.net/U+0ACD>`_  '\\u0acd'  Mn                  0  GUJARATI SIGN VIRAMA
     9  `U+0A9F <https://codepoints.net/U+0A9F>`_  '\\u0a9f'  Lo                  1  GUJARATI LETTER TTA
    10  `U+0ACD <https://codepoints.net/U+0ACD>`_  '\\u0acd'  Mn                  0  GUJARATI SIGN VIRAMA
    11  `U+0AB0 <https://codepoints.net/U+0AB0>`_  '\\u0ab0'  Lo                  1  GUJARATI LETTER RA
    12  `U+0AC0 <https://codepoints.net/U+0AC0>`_  '\\u0ac0'  Mc                  0  GUJARATI VOWEL SIGN II
    13  `U+0AAF <https://codepoints.net/U+0AAF>`_  '\\u0aaf'  Lo                  1  GUJARATI LETTER YA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 13


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\x86\xe0\xaa\x82\xe0\xaa\xa4\xe0\xaa\xb0\xe0\xaa\xb0\xe0\xaa\xbe\xe0\xaa\xb7\xe0\xab\x8d\xe0\xaa\x9f\xe0\xab\x8d\xe0\xaa\xb0\xe0\xab\x80\xe0\xaa\xaf|\\n12345678|\\n"
        આંતરરાષ્ટ્રીય|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *QTerminal* measures width 5.

.. _QTerminallangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "doke|\\n1234|\\n"
        doke|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *QTerminal* measures width -3.

.. _QTerminallangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'        Ll                  1  LATIN SMALL LETTER R
     4  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "c\xc9\x9br\xc9\x9b|\\n1234|\\n"
        cɛrɛ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *QTerminal* measures width 0.

.. _QTerminallangSererSine:

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
  while *QTerminal* measures width -4.

.. _QTerminallangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

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
  while *QTerminal* measures width -2.

.. _QTerminallangFon:

Fon
^^^

Sequence of language *Fon* from midpoint of alignment failure records:

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
  while *QTerminal* measures width 0.

.. _QTerminallangHindi:

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     3  `U+0937 <https://codepoints.net/U+0937>`_  '\\u0937'  Lo                  1  DEVANAGARI LETTER SSA
     4  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     5  `U+091F <https://codepoints.net/U+091F>`_  '\\u091f'  Lo                  1  DEVANAGARI LETTER TTA
     6  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     7  `U+0930 <https://codepoints.net/U+0930>`_  '\\u0930'  Lo                  1  DEVANAGARI LETTER RA
     8  `U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
     9  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xb7\xe0\xa5\x8d\xe0\xa4\x9f\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa5\x80\xe0\xa4\xaf|\\n12345|\\n"
        राष्ट्रीय|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width 2.

.. _QTerminallangBhojpuri:

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
  while *QTerminal* measures width -2.

.. _QTerminallangTaiDam:

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
  while *QTerminal* measures width 1.

.. _QTerminallangChakma:

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===================
     1  `U+00011125 <https://codepoints.net/U+00011125>`_  '\\U00011125'  Lo                  1  CHAKMA LETTER SAA
     2  `U+00011128 <https://codepoints.net/U+00011128>`_  '\\U00011128'  Mn                  0  CHAKMA VOWEL SIGN I
     3  `U+0001111F <https://codepoints.net/U+0001111F>`_  '\\U0001111f'  Lo                  1  CHAKMA LETTER MAA
     4  `U+00011128 <https://codepoints.net/U+00011128>`_  '\\U00011128'  Mn                  0  CHAKMA VOWEL SIGN I
     5  `U+0001111A <https://codepoints.net/U+0001111A>`_  '\\U0001111a'  Lo                  1  CHAKMA LETTER NAA
     6  `U+0001112C <https://codepoints.net/U+0001112C>`_  '\\U0001112c'  Mc                  0  CHAKMA VOWEL SIGN E
     7  `U+00011122 <https://codepoints.net/U+00011122>`_  '\\U00011122'  Lo                  1  CHAKMA LETTER RAA
     8  `U+00011134 <https://codepoints.net/U+00011134>`_  '\\U00011134'  Mn                  0  CHAKMA MAAYYAA
   ===  =================================================  =============  ==========  =========  ===================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\xa5\xf0\x91\x84\xa8\xf0\x91\x84\x9f\xf0\x91\x84\xa8\xf0\x91\x84\x9a\xf0\x91\x84\xac\xf0\x91\x84\xa2\xf0\x91\x84\xb4|\\n1234|\\n"
        𑄥𑄨𑄟𑄨𑄚𑄬𑄢𑄴|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *QTerminal* measures width 2.

.. _QTerminallangDangme:

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "k\xc9\x9b|\\n12|\\n"
        kɛ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width -2.

.. _QTerminallangWaama:

Waama
^^^^^

Sequence of language *Waama* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "teera|\\n12345|\\n"
        teera|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width -5.

.. _QTerminallangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0F66 <https://codepoints.net/U+0F66>`_  '\\u0f66'  Lo                  1  TIBETAN LETTER SA
     2  `U+0F90 <https://codepoints.net/U+0F90>`_  '\\u0f90'  Mn                  0  TIBETAN SUBJOINED LETTER KA
     3  `U+0FB1 <https://codepoints.net/U+0FB1>`_  '\\u0fb1'  Mn                  0  TIBETAN SUBJOINED LETTER YA
     4  `U+0F7A <https://codepoints.net/U+0F7A>`_  '\\u0f7a'  Mn                  0  TIBETAN VOWEL SIGN E
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\xa6\xe0\xbe\x90\xe0\xbe\xb1\xe0\xbd\xba|\\n1|\\n"
        སྐྱེ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *QTerminal* measures width -1.

.. _QTerminallangMagahi:

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0905 <https://codepoints.net/U+0905>`_  '\\u0905'  Lo                  1  DEVANAGARI LETTER A
     2  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     3  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     4  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     5  `U+0935 <https://codepoints.net/U+0935>`_  '\\u0935'  Lo                  1  DEVANAGARI LETTER VA
     6  `U+0940 <https://codepoints.net/U+0940>`_  '\\u0940'  Mc                  0  DEVANAGARI VOWEL SIGN II
     7  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x85\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\xe0\xa5\x80\xe0\xa4\xaf|\\n12345|\\n"
        अमानवीय|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *QTerminal* measures width 2.

.. _QTerminallangPanjabiEastern:

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0A2E <https://codepoints.net/U+0A2E>`_  '\\u0a2e'  Lo                  1  GURMUKHI LETTER MA
     2  `U+0A41 <https://codepoints.net/U+0A41>`_  '\\u0a41'  Mn                  0  GURMUKHI VOWEL SIGN U
     3  `U+0A32 <https://codepoints.net/U+0A32>`_  '\\u0a32'  Lo                  1  GURMUKHI LETTER LA
     4  `U+0A15 <https://codepoints.net/U+0A15>`_  '\\u0a15'  Lo                  1  GURMUKHI LETTER KA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\xae\xe0\xa9\x81\xe0\xa8\xb2\xe0\xa8\x95|\\n123|\\n"
        ਮੁਲਕ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *QTerminal* measures width -1.

.. _QTerminallangDzongkha:

Dzongkha
^^^^^^^^

Sequence of language *Dzongkha* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
     2  `U+0F44 <https://codepoints.net/U+0F44>`_  '\\u0f44'  Lo                  1  TIBETAN LETTER NGA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x91\xe0\xbd\x84|\\n12|\\n"
        དང|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *QTerminal* measures width 1.

.. _QTerminaldecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

This Terminal does not appear capable of reporting about any DEC Private modes.

.. _QTerminalreproduce:

Reproduction
++++++++++++

To reproduce these results for *QTerminal*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --save-yaml=linux-QTerminal-1.4.0.yaml \
        --limit-codepoints=5000 \
        --limit-words=5000 \
        --limit-errors=500

.. _QTerminaltime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **40.88 seconds** (40s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
