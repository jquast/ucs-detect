.. _ghostty:

ghostty
-------


Tested Software version 1.2.3 on Linux
Full results available at ucs-detect_ repository path
`data/linux-ghostty-1.2.3.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-ghostty-1.2.3.yaml>`_

.. _ghosttyscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *ghostty*:

.. table::
   :class: sphinx-datatable

   ============  ===========  ==============  ======================================================
   Score Type    Raw Score    Scaled Score    Calculation
   ============  ===========  ==============  ======================================================
   WIDE          72.73%       58.9%           (version_index / total_versions) × (pct_success / 100)
   ZWJ           75.00%       100.0%          (version_index / total_versions) × (pct_success / 100)
   LANG          93.78%       90.2%           geometric_mean(language_percentages)
   VS16          94.37%       94.4%           pct_success / 100
   VS15          100.00%      100.0%          pct_success / 100
   DEC Modes     22.93%       40.0%           modes_changeable / total_modes
   TIME          50.16s       85.3%           1 - ((elapsed - min) / (max - min)) [inverse]
   ============  ===========  ==============  ======================================================

**Final Score Calculation:**

- Raw Final Score: 76.47%
  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6
  the categorized 'average' absolute support level of this terminal
  Note: TIME is excluded from raw average since it measures performance, not feature support

- Scaled Final Score: 96.3%
  (normalized across all terminals tested, including TIME performance).
  *Scaled scores* are normalized (0-100%) relative to all terminals tested

.. _ghosttywide:

Wide character support
++++++++++++++++++++++

The best wide unicode table version for ghostty appears to be 
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
  while *ghostty* measures width 1.

.. _ghosttyzwj:

Emoji ZWJ support
+++++++++++++++++

The best Emoji ZWJ table version for *ghostty* appears to be 
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

.. _ghosttyvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *ghostty* is 12 errors
out of 213 total codepoints tested, 94.4% success.
Sequence of a NARROW Emoji made WIDE by *Variation Selector-16*, from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0034 <https://codepoints.net/U+0034>`_  '4'        Nd                  1  DIGIT FOUR
     2  `U+FE0F <https://codepoints.net/U+FE0F>`_  '\\ufe0f'  Mn                  0  VARIATION SELECTOR-16
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "4\xef\xb8\x8f|\\n12|\\n"
        4️|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width 1.


.. _ghosttyvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *ghostty* is 0 errors
out of 158 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-15 tested were successful.

.. _ghosttylang:

Language Support
++++++++++++++++

The following 3 languages were tested with 100% success:

Mongolian, Halh (Mongolian), Tagalog (Tagalog), Tamang, Eastern.

The following 116 languages are not fully supported:

.. table::
   :class: sphinx-datatable

   ==============================================================================  ==========  =========  =============
   lang                                                                              n_errors    n_total  pct_success
   ==============================================================================  ==========  =========  =============
   :ref:`Shan <ghosttylangShan>`                                                          864        915  5.6%
   :ref:`Khün <ghosttylangKhn>`                                                           303        442  31.4%
   :ref:`Burmese <ghosttylangBurmese>`                                                    821       1223  32.9%
   :ref:`Mon <ghosttylangMon>`                                                            594        946  37.2%
   :ref:`Thai (2) <ghosttylangThai2>`                                                      60        313  80.8%
   :ref:`Lao <ghosttylangLao>`                                                             80        426  81.2%
   :ref:`Thai <ghosttylangThai>`                                                           56        341  83.6%
   :ref:`Malayalam <ghosttylangMalayalam>`                                                118       1630  92.8%
   :ref:`Sinhala <ghosttylangSinhala>`                                                    112       1655  93.2%
   :ref:`Vietnamese (Han nom) <ghosttylangVietnameseHannom>`                                5        199  97.5%
   :ref:`Chinese, Mandarin (Beijing) <ghosttylangChineseMandarinBeijing>`                   5        212  97.6%
   :ref:`Japanese (Tokyo) <ghosttylangJapaneseTokyo>`                                       7        320  97.8%
   :ref:`Nuosu <ghosttylangNuosu>`                                                          5        230  97.8%
   :ref:`Japanese (Osaka) <ghosttylangJapaneseOsaka>`                                       6        308  98.1%
   :ref:`Chinese, Yue <ghosttylangChineseYue>`                                              4        210  98.1%
   :ref:`(Jinan) <ghosttylangJinan>`                                                        4        211  98.1%
   :ref:`Chinese, Mandarin (Guiyang) <ghosttylangChineseMandarinGuiyang>`                   4        211  98.1%
   :ref:`Chinese, Hakka <ghosttylangChineseHakka>`                                          4        212  98.1%
   :ref:`Chinese, Mandarin (Tianjin) <ghosttylangChineseMandarinTianjin>`                   4        212  98.1%
   :ref:`Chinese, Min Nan <ghosttylangChineseMinNan>`                                       4        212  98.1%
   :ref:`Chinese, Xiang <ghosttylangChineseXiang>`                                          4        212  98.1%
   :ref:`Chinese, Mandarin (Simplified) <ghosttylangChineseMandarinSimplified>`             4        225  98.2%
   :ref:`Japanese <ghosttylangJapanese>`                                                    5        299  98.3%
   :ref:`Chinese, Mandarin (Harbin) <ghosttylangChineseMandarinHarbin>`                     3        210  98.6%
   :ref:`Chinese, Jinyu <ghosttylangChineseJinyu>`                                          3        212  98.6%
   :ref:`Chinese, Mandarin (Nanjing) <ghosttylangChineseMandarinNanjing>`                   3        212  98.6%
   :ref:`Khmer, Central <ghosttylangKhmerCentral>`                                          6        528  98.9%
   :ref:`Chinese, Mandarin (Traditional) <ghosttylangChineseMandarinTraditional>`           2        210  99.0%
   :ref:`Chinese, Gan <ghosttylangChineseGan>`                                              2        211  99.1%
   :ref:`Chinese, Wu <ghosttylangChineseWu>`                                                2        211  99.1%
   :ref:`Chickasaw <ghosttylangChickasaw>`                                                  5        554  99.1%
   :ref:`Bora <ghosttylangBora>`                                                           12       1598  99.2%
   :ref:`Gumuz <ghosttylangGumuz>`                                                          9       1283  99.3%
   :ref:`Marathi <ghosttylangMarathi>`                                                     11       1614  99.3%
   :ref:`Shipibo-Conibo <ghosttylangShipiboConibo>`                                        17       2540  99.3%
   :ref:`Evenki <ghosttylangEvenki>`                                                        6        899  99.3%
   :ref:`Nanai <ghosttylangNanai>`                                                          8       1207  99.3%
   :ref:`Orok <ghosttylangOrok>`                                                            8       1245  99.4%
   :ref:`Yaneshaʼ <ghosttylangYanesha>`                                                    16       2536  99.4%
   :ref:`Navajo <ghosttylangNavajo>`                                                       10       1600  99.4%
   :ref:`Amarakaeri <ghosttylangAmarakaeri>`                                                9       1446  99.4%
   :ref:`Veps <ghosttylangVeps>`                                                            8       1323  99.4%
   :ref:`Siona <ghosttylangSiona>`                                                          9       1492  99.4%
   :ref:`Gilyak <ghosttylangGilyak>`                                                        9       1504  99.4%
   :ref:`Nepali <ghosttylangNepali>`                                                        8       1385  99.4%
   :ref:`South Azerbaijani <ghosttylangSouthAzerbaijani>`                                   8       1396  99.4%
   :ref:`Secoya <ghosttylangSecoya>`                                                        8       1409  99.4%
   :ref:`Bengali <ghosttylangBengali>`                                                      8       1413  99.4%
   :ref:`(Yeonbyeon) <ghosttylangYeonbyeon>`                                                6       1061  99.4%
   :ref:`Tamil (Sri Lanka) <ghosttylangTamilSriLanka>`                                      7       1261  99.4%
   :ref:`Tamil <ghosttylangTamil>`                                                          7       1262  99.4%
   :ref:`Colorado <ghosttylangColorado>`                                                    7       1263  99.4%
   :ref:`Telugu <ghosttylangTelugu>`                                                        6       1129  99.5%
   :ref:`Korean <ghosttylangKorean>`                                                        6       1185  99.5%
   :ref:`Sanskrit <ghosttylangSanskrit>`                                                    5       1000  99.5%
   :ref:`Sanskrit (Grantha) <ghosttylangSanskritGrantha>`                                   5       1006  99.5%
   :ref:`Tem <ghosttylangTem>`                                                              8       1659  99.5%
   :ref:`Catalan (2) <ghosttylangCatalan2>`                                                 9       1909  99.5%
   :ref:`Kannada <ghosttylangKannada>`                                                      5       1080  99.5%
   :ref:`Mirandese <ghosttylangMirandese>`                                                  9       1966  99.5%
   :ref:`Yiddish, Eastern <ghosttylangYiddishEastern>`                                      8       1775  99.5%
   :ref:`Éwé <ghosttylangw>`                                                               10       2230  99.6%
   :ref:`Arabic, Standard <ghosttylangArabicStandard>`                                      6       1348  99.6%
   :ref:`Picard <ghosttylangPicard>`                                                        9       2024  99.6%
   :ref:`Kabyle <ghosttylangKabyle>`                                                        8       1815  99.6%
   :ref:`Lingala (tones) <ghosttylangLingalatones>`                                         8       1818  99.6%
   :ref:`Ticuna <ghosttylangTicuna>`                                                        9       2048  99.6%
   :ref:`Tamazight, Central Atlas <ghosttylangTamazightCentralAtlas>`                       8       1822  99.6%
   :ref:`Mixtec, Metlatónoc <ghosttylangMixtecMetlatnoc>`                                   6       1367  99.6%
   :ref:`Fur <ghosttylangFur>`                                                              8       1838  99.6%
   :ref:`Pular (Adlam) <ghosttylangPularAdlam>`                                             7       1613  99.6%
   :ref:`Assyrian Neo-Aramaic <ghosttylangAssyrianNeoAramaic>`                              5       1160  99.6%
   :ref:`Maldivian <ghosttylangMaldivian>`                                                  8       1918  99.6%
   :ref:`French (Welche) <ghosttylangFrenchWelche>`                                         8       1928  99.6%
   :ref:`Saint Lucian Creole French <ghosttylangSaintLucianCreoleFrench>`                   7       1777  99.6%
   :ref:`Ga <ghosttylangGa>`                                                                8       2039  99.6%
   :ref:`Gen <ghosttylangGen>`                                                              9       2309  99.6%
   :ref:`Aja <ghosttylangAja>`                                                              8       2061  99.6%
   :ref:`Farsi, Western <ghosttylangFarsiWestern>`                                          7       1822  99.6%
   :ref:`Dendi <ghosttylangDendi>`                                                          6       1569  99.6%
   :ref:`Mazahua Central <ghosttylangMazahuaCentral>`                                       6       1574  99.6%
   :ref:`Maori (2) <ghosttylangMaori2>`                                                     9       2385  99.6%
   :ref:`Serer-Sine <ghosttylangSererSine>`                                                 6       1596  99.6%
   :ref:`Dari <ghosttylangDari>`                                                            7       1872  99.6%
   :ref:`Ditammari <ghosttylangDitammari>`                                                  7       1882  99.6%
   :ref:`Uduk <ghosttylangUduk>`                                                           12       3247  99.6%
   :ref:`Yoruba <ghosttylangYoruba>`                                                        9       2454  99.6%
   :ref:`Vietnamese <ghosttylangVietnamese>`                                                9       2502  99.6%
   :ref:`Urdu <ghosttylangUrdu>`                                                            8       2237  99.6%
   :ref:`Pashto, Northern <ghosttylangPashtoNorthern>`                                      8       2242  99.6%
   :ref:`Seraiki <ghosttylangSeraiki>`                                                      8       2242  99.6%
   :ref:`Belanda Viri <ghosttylangBelandaViri>`                                             8       2246  99.6%
   :ref:`Urdu (2) <ghosttylangUrdu2>`                                                       8       2251  99.6%
   :ref:`Bamun <ghosttylangBamun>`                                                          8       2285  99.6%
   :ref:`Dagaare, Southern <ghosttylangDagaareSouthern>`                                    9       2582  99.7%
   :ref:`Chinantec, Chiltepec <ghosttylangChinantecChiltepec>`                              6       1729  99.7%
   :ref:`Javanese (Javanese) <ghosttylangJavaneseJavanese>`                                 5       1453  99.7%
   :ref:`Panjabi, Western <ghosttylangPanjabiWestern>`                                      8       2419  99.7%
   :ref:`Maithili <ghosttylangMaithili>`                                                    5       1519  99.7%
   :ref:`Dinka, Northeastern <ghosttylangDinkaNortheastern>`                                5       1529  99.7%
   :ref:`Mòoré <ghosttylangMor>`                                                            8       2447  99.7%
   :ref:`Gujarati <ghosttylangGujarati>`                                                    5       1536  99.7%
   :ref:`Otomi, Mezquital <ghosttylangOtomiMezquital>`                                      6       1849  99.7%
   :ref:`Fon <ghosttylangFon>`                                                              8       2520  99.7%
   :ref:`Lamnso' <ghosttylangLamnso>`                                                       7       2237  99.7%
   :ref:`Baatonum <ghosttylangBaatonum>`                                                    6       1939  99.7%
   :ref:`Waama <ghosttylangWaama>`                                                          3       1000  99.7%
   :ref:`Magahi <ghosttylangMagahi>`                                                        5       1716  99.7%
   :ref:`Bhojpuri <ghosttylangBhojpuri>`                                                    5       1737  99.7%
   :ref:`Hindi <ghosttylangHindi>`                                                          6       2128  99.7%
   :ref:`Chakma <ghosttylangChakma>`                                                        4       1444  99.7%
   :ref:`Dangme <ghosttylangDangme>`                                                        8       2912  99.7%
   :ref:`Panjabi, Eastern <ghosttylangPanjabiEastern>`                                      6       2293  99.7%
   :ref:`Tibetan, Central <ghosttylangTibetanCentral>`                                      8       3174  99.7%
   :ref:`Tai Dam <ghosttylangTaiDam>`                                                       6       2386  99.7%
   :ref:`Dzongkha <ghosttylangDzongkha>`                                                    7       3060  99.8%
   ==============================================================================  ==========  =========  =============

.. _ghosttylangShan:

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
  while *ghostty* measures width 9.

.. _ghosttylangKhn:

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
  while *ghostty* measures width 15.

.. _ghosttylangBurmese:

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
  while *ghostty* measures width 9.

.. _ghosttylangMon:

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
  while *ghostty* measures width 6.

.. _ghosttylangThai2:

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
  while *ghostty* measures width 23.

.. _ghosttylangLao:

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
  while *ghostty* measures width 17.

.. _ghosttylangThai:

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
  while *ghostty* measures width 6.

.. _ghosttylangMalayalam:

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
  while *ghostty* measures width 10.

.. _ghosttylangSinhala:

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
  while *ghostty* measures width 6.

.. _ghosttylangVietnameseHannom:

Vietnamese (Han nom)
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Vietnamese (Han nom)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===========================
     1  `U+65BC <https://codepoints.net/U+65BC>`_          '\\u65bc'      Lo                  2  CJK UNIFIED IDEOGRAPH-65BC
     2  `U+6B63 <https://codepoints.net/U+6B63>`_          '\\u6b63'      Lo                  2  CJK UNIFIED IDEOGRAPH-6B63
     3  `U+5404 <https://codepoints.net/U+5404>`_          '\\u5404'      Lo                  2  CJK UNIFIED IDEOGRAPH-5404
     4  `U+6E03 <https://codepoints.net/U+6E03>`_          '\\u6e03'      Lo                  2  CJK UNIFIED IDEOGRAPH-6E03
     5  `U+6210 <https://codepoints.net/U+6210>`_          '\\u6210'      Lo                  2  CJK UNIFIED IDEOGRAPH-6210
     6  `U+54E1 <https://codepoints.net/U+54E1>`_          '\\u54e1'      Lo                  2  CJK UNIFIED IDEOGRAPH-54E1
     7  `U+00027D51 <https://codepoints.net/U+00027D51>`_  '\\U00027d51'  Lo                  2  CJK UNIFIED IDEOGRAPH-27D51
     8  `U+806F <https://codepoints.net/U+806F>`_          '\\u806f'      Lo                  2  CJK UNIFIED IDEOGRAPH-806F
     9  `U+5408 <https://codepoints.net/U+5408>`_          '\\u5408'      Lo                  2  CJK UNIFIED IDEOGRAPH-5408
    10  `U+570B <https://codepoints.net/U+570B>`_          '\\u570b'      Lo                  2  CJK UNIFIED IDEOGRAPH-570B
    11  `U+5427 <https://codepoints.net/U+5427>`_          '\\u5427'      Lo                  2  CJK UNIFIED IDEOGRAPH-5427
    12  `U+65BC <https://codepoints.net/U+65BC>`_          '\\u65bc'      Lo                  2  CJK UNIFIED IDEOGRAPH-65BC
    13  `U+5404 <https://codepoints.net/U+5404>`_          '\\u5404'      Lo                  2  CJK UNIFIED IDEOGRAPH-5404
    14  `U+9818 <https://codepoints.net/U+9818>`_          '\\u9818'      Lo                  2  CJK UNIFIED IDEOGRAPH-9818
    15  `U+571F <https://codepoints.net/U+571F>`_          '\\u571f'      Lo                  2  CJK UNIFIED IDEOGRAPH-571F
    16  `U+5C6C <https://codepoints.net/U+5C6C>`_          '\\u5c6c'      Lo                  2  CJK UNIFIED IDEOGRAPH-5C6C
    17  `U+6B0A <https://codepoints.net/U+6B0A>`_          '\\u6b0a'      Lo                  2  CJK UNIFIED IDEOGRAPH-6B0A
    18  `U+7BA1 <https://codepoints.net/U+7BA1>`_          '\\u7ba1'      Lo                  2  CJK UNIFIED IDEOGRAPH-7BA1
    19  `U+7406 <https://codepoints.net/U+7406>`_          '\\u7406'      Lo                  2  CJK UNIFIED IDEOGRAPH-7406
    20  `U+00027D51 <https://codepoints.net/U+00027D51>`_  '\\U00027d51'  Lo                  2  CJK UNIFIED IDEOGRAPH-27D51
    21  `U+0002825F <https://codepoints.net/U+0002825F>`_  '\\U0002825f'  Lo                  2  CJK UNIFIED IDEOGRAPH-2825F
   ===  =================================================  =============  ==========  =========  ===========================

Total codepoints: 21


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x96\xbc\xe6\xad\xa3\xe5\x90\x84\xe6\xb8\x83\xe6\x88\x90\xe5\x93\xa1\xf0\xa7\xb5\x91\xe8\x81\xaf\xe5\x90\x88\xe5\x9c\x8b\xe5\x90\xa7\xe6\x96\xbc\xe5\x90\x84\xe9\xa0\x98\xe5\x9c\x9f\xe5\xb1\xac\xe6\xac\x8a\xe7\xae\xa1\xe7\x90\x86\xf0\xa7\xb5\x91\xf0\xa8\x89\x9f|\\n123456789012345678901234567890123456789012|\\n"
        於正各渃成員𧵑聯合國吧於各領土屬權管理𧵑𨉟|
        123456789012345678901234567890123456789012|

- python `wcwidth.wcswidth()`_ measures width 42,
  while *ghostty* measures width 36.

.. _ghosttylangChineseMandarinBeijing:

Chinese, Mandarin (Beijing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Beijing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
     2  `U+901A <https://codepoints.net/U+901A>`_  '\\u901a'  Lo                  2  CJK UNIFIED IDEOGRAPH-901A
     3  `U+8FC7 <https://codepoints.net/U+8FC7>`_  '\\u8fc7'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FC7
     4  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     5  `U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
     6  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     7  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
     8  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     9  `U+9645 <https://codepoints.net/U+9645>`_  '\\u9645'  Lo                  2  CJK UNIFIED IDEOGRAPH-9645
    10  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    11  `U+6328 <https://codepoints.net/U+6328>`_  '\\u6328'  Lo                  2  CJK UNIFIED IDEOGRAPH-6328
    12  `U+5806 <https://codepoints.net/U+5806>`_  '\\u5806'  Lo                  2  CJK UNIFIED IDEOGRAPH-5806
    13  `U+513F <https://codepoints.net/U+513F>`_  '\\u513f'  Lo                  2  CJK UNIFIED IDEOGRAPH-513F
    14  `U+63AA <https://codepoints.net/U+63AA>`_  '\\u63aa'  Lo                  2  CJK UNIFIED IDEOGRAPH-63AA
    15  `U+65BD <https://codepoints.net/U+65BD>`_  '\\u65bd'  Lo                  2  CJK UNIFIED IDEOGRAPH-65BD
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 15


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe9\x80\x9a\xe8\xbf\x87\xe5\x9b\xbd\xe5\xae\xb6\xe7\x9a\x84\xe5\x92\x8c\xe5\x9b\xbd\xe9\x99\x85\xe7\x9a\x84\xe6\x8c\xa8\xe5\xa0\x86\xe5\x84\xbf\xe6\x8e\xaa\xe6\x96\xbd|\\n123456789012345678901234567890|\\n"
        并通过国家的和国际的挨堆儿措施|
        123456789012345678901234567890|

- python `wcwidth.wcswidth()`_ measures width 30,
  while *ghostty* measures width -10.

.. _ghosttylangJapaneseTokyo:

Japanese (Tokyo)
^^^^^^^^^^^^^^^^

Sequence of language *Japanese (Tokyo)* from midpoint of alignment failure records:

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
  while *ghostty* measures width -20.

.. _ghosttylangNuosu:

Nuosu
^^^^^

Sequence of language *Nuosu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============
     1  `U+A320 <https://codepoints.net/U+A320>`_  '\\ua320'  Lo                  2  YI SYLLABLE SU
     2  `U+A279 <https://codepoints.net/U+A279>`_  '\\ua279'  Lo                  2  YI SYLLABLE HOT
     3  `U+A04C <https://codepoints.net/U+A04C>`_  '\\ua04c'  Lo                  2  YI SYLLABLE PU
     4  `U+A3D3 <https://codepoints.net/U+A3D3>`_  '\\ua3d3'  Lo                  2  YI SYLLABLE REP
     5  `U+A0B1 <https://codepoints.net/U+A0B1>`_  '\\ua0b1'  Lo                  2  YI SYLLABLE MIP
     6  `U+A2A8 <https://codepoints.net/U+A2A8>`_  '\\ua2a8'  Lo                  2  YI SYLLABLE ZYT
     7  `U+A3E6 <https://codepoints.net/U+A3E6>`_  '\\ua3e6'  Lo                  2  YI SYLLABLE JIE
     8  `U+A3F2 <https://codepoints.net/U+A3F2>`_  '\\ua3f2'  Lo                  2  YI SYLLABLE JU
     9  `U+A138 <https://codepoints.net/U+A138>`_  '\\ua138'  Lo                  2  YI SYLLABLE DDI
   ===  =========================================  =========  ==========  =========  ===============

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\x8c\xa0\xea\x89\xb9\xea\x81\x8c\xea\x8f\x93\xea\x82\xb1\xea\x8a\xa8\xea\x8f\xa6\xea\x8f\xb2\xea\x84\xb8|\\n123456789012345678|\\n"
        ꌠꉹꁌꏓꂱꊨꏦꏲꄸ|
        123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 18,
  while *ghostty* measures width -8.

.. _ghosttylangJapaneseOsaka:

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
  while *ghostty* measures width -20.

.. _ghosttylangChineseYue:

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
  while *ghostty* measures width -40.

.. _ghosttylangJinan:

(Jinan)
^^^^^^^

Sequence of language *(Jinan)* from midpoint of alignment failure records:

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
  while *ghostty* measures width -12.

.. _ghosttylangChineseMandarinGuiyang:

Chinese, Mandarin (Guiyang)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Guiyang)* from midpoint of alignment failure records:

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
  while *ghostty* measures width -12.

.. _ghosttylangChineseHakka:

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
  while *ghostty* measures width -10.

.. _ghosttylangChineseMandarinTianjin:

Chinese, Mandarin (Tianjin)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Tianjin)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5E76 <https://codepoints.net/U+5E76>`_  '\\u5e76'  Lo                  2  CJK UNIFIED IDEOGRAPH-5E76
     2  `U+901A <https://codepoints.net/U+901A>`_  '\\u901a'  Lo                  2  CJK UNIFIED IDEOGRAPH-901A
     3  `U+8FC7 <https://codepoints.net/U+8FC7>`_  '\\u8fc7'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FC7
     4  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     5  `U+5BB6 <https://codepoints.net/U+5BB6>`_  '\\u5bb6'  Lo                  2  CJK UNIFIED IDEOGRAPH-5BB6
     6  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
     7  `U+548C <https://codepoints.net/U+548C>`_  '\\u548c'  Lo                  2  CJK UNIFIED IDEOGRAPH-548C
     8  `U+56FD <https://codepoints.net/U+56FD>`_  '\\u56fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-56FD
     9  `U+9645 <https://codepoints.net/U+9645>`_  '\\u9645'  Lo                  2  CJK UNIFIED IDEOGRAPH-9645
    10  `U+7684 <https://codepoints.net/U+7684>`_  '\\u7684'  Lo                  2  CJK UNIFIED IDEOGRAPH-7684
    11  `U+6E10 <https://codepoints.net/U+6E10>`_  '\\u6e10'  Lo                  2  CJK UNIFIED IDEOGRAPH-6E10
    12  `U+8FDB <https://codepoints.net/U+8FDB>`_  '\\u8fdb'  Lo                  2  CJK UNIFIED IDEOGRAPH-8FDB
    13  `U+63AA <https://codepoints.net/U+63AA>`_  '\\u63aa'  Lo                  2  CJK UNIFIED IDEOGRAPH-63AA
    14  `U+65BD <https://codepoints.net/U+65BD>`_  '\\u65bd'  Lo                  2  CJK UNIFIED IDEOGRAPH-65BD
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xb9\xb6\xe9\x80\x9a\xe8\xbf\x87\xe5\x9b\xbd\xe5\xae\xb6\xe7\x9a\x84\xe5\x92\x8c\xe5\x9b\xbd\xe9\x99\x85\xe7\x9a\x84\xe6\xb8\x90\xe8\xbf\x9b\xe6\x8e\xaa\xe6\x96\xbd|\\n1234567890123456789012345678|\\n"
        并通过国家的和国际的渐进措施|
        1234567890123456789012345678|

- python `wcwidth.wcswidth()`_ measures width 28,
  while *ghostty* measures width -12.

.. _ghosttylangChineseMinNan:

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
  while *ghostty* measures width -12.

.. _ghosttylangChineseXiang:

Chinese, Xiang
^^^^^^^^^^^^^^

Sequence of language *Chinese, Xiang* from midpoint of alignment failure records:

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
  while *ghostty* measures width -10.

.. _ghosttylangChineseMandarinSimplified:

Chinese, Mandarin (Simplified)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Simplified)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5927 <https://codepoints.net/U+5927>`_  '\\u5927'  Lo                  2  CJK UNIFIED IDEOGRAPH-5927
     2  `U+4F1A <https://codepoints.net/U+4F1A>`_  '\\u4f1a'  Lo                  2  CJK UNIFIED IDEOGRAPH-4F1A
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\xa4\xa7\xe4\xbc\x9a|\\n1234|\\n"
        大会|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width -4.

.. _ghosttylangJapanese:

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
  while *ghostty* measures width -14.

.. _ghosttylangChineseMandarinHarbin:

Chinese, Mandarin (Harbin)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Harbin)* from midpoint of alignment failure records:

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
  while *ghostty* measures width -12.

.. _ghosttylangChineseJinyu:

Chinese, Jinyu
^^^^^^^^^^^^^^

Sequence of language *Chinese, Jinyu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+624D <https://codepoints.net/U+624D>`_  '\\u624d'  Lo                  2  CJK UNIFIED IDEOGRAPH-624D
     2  `U+80FD <https://codepoints.net/U+80FD>`_  '\\u80fd'  Lo                  2  CJK UNIFIED IDEOGRAPH-80FD
     3  `U+7F14 <https://codepoints.net/U+7F14>`_  '\\u7f14'  Lo                  2  CJK UNIFIED IDEOGRAPH-7F14
     4  `U+5A5A <https://codepoints.net/U+5A5A>`_  '\\u5a5a'  Lo                  2  CJK UNIFIED IDEOGRAPH-5A5A
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe6\x89\x8d\xe8\x83\xbd\xe7\xbc\x94\xe5\xa9\x9a|\\n12345678|\\n"
        才能缔婚|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *ghostty* measures width -28.

.. _ghosttylangChineseMandarinNanjing:

Chinese, Mandarin (Nanjing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Nanjing)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+5173 <https://codepoints.net/U+5173>`_  '\\u5173'  Lo                  2  CJK UNIFIED IDEOGRAPH-5173
     2  `U+8D77 <https://codepoints.net/U+8D77>`_  '\\u8d77'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D77
     3  `U+6765 <https://codepoints.net/U+6765>`_  '\\u6765'  Lo                  2  CJK UNIFIED IDEOGRAPH-6765
     4  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     5  `U+8005 <https://codepoints.net/U+8005>`_  '\\u8005'  Lo                  2  CJK UNIFIED IDEOGRAPH-8005
     6  `U+8D76 <https://codepoints.net/U+8D76>`_  '\\u8d76'  Lo                  2  CJK UNIFIED IDEOGRAPH-8D76
     7  `U+51FA <https://codepoints.net/U+51FA>`_  '\\u51fa'  Lo                  2  CJK UNIFIED IDEOGRAPH-51FA
     8  `U+53BB <https://codepoints.net/U+53BB>`_  '\\u53bb'  Lo                  2  CJK UNIFIED IDEOGRAPH-53BB
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe5\x85\xb3\xe8\xb5\xb7\xe6\x9d\xa5\xe6\x88\x96\xe8\x80\x85\xe8\xb5\xb6\xe5\x87\xba\xe5\x8e\xbb|\\n1234567890123456|\\n"
        关起来或者赶出去|
        1234567890123456|

- python `wcwidth.wcswidth()`_ measures width 16,
  while *ghostty* measures width -6.

.. _ghosttylangKhmerCentral:

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
     2  `U+17C4 <https://codepoints.net/U+17C4>`_  '\\u17c4'  Mc                  0  KHMER VOWEL SIGN OO
     3  `U+1799 <https://codepoints.net/U+1799>`_  '\\u1799'  Lo                  1  KHMER LETTER YO
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x8a\xe1\x9f\x84\xe1\x9e\x99|\\n12|\\n"
        ដោយ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -13.

.. _ghosttylangChineseMandarinTraditional:

Chinese, Mandarin (Traditional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinese, Mandarin (Traditional)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+4EE5 <https://codepoints.net/U+4EE5>`_  '\\u4ee5'  Lo                  2  CJK UNIFIED IDEOGRAPH-4EE5
     2  `U+53CA <https://codepoints.net/U+53CA>`_  '\\u53ca'  Lo                  2  CJK UNIFIED IDEOGRAPH-53CA
     3  `U+55AE <https://codepoints.net/U+55AE>`_  '\\u55ae'  Lo                  2  CJK UNIFIED IDEOGRAPH-55AE
     4  `U+7368 <https://codepoints.net/U+7368>`_  '\\u7368'  Lo                  2  CJK UNIFIED IDEOGRAPH-7368
     5  `U+6216 <https://codepoints.net/U+6216>`_  '\\u6216'  Lo                  2  CJK UNIFIED IDEOGRAPH-6216
     6  `U+96C6 <https://codepoints.net/U+96C6>`_  '\\u96c6'  Lo                  2  CJK UNIFIED IDEOGRAPH-96C6
     7  `U+9AD4 <https://codepoints.net/U+9AD4>`_  '\\u9ad4'  Lo                  2  CJK UNIFIED IDEOGRAPH-9AD4
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe4\xbb\xa5\xe5\x8f\x8a\xe5\x96\xae\xe7\x8d\xa8\xe6\x88\x96\xe9\x9b\x86\xe9\xab\x94|\\n12345678901234|\\n"
        以及單獨或集體|
        12345678901234|

- python `wcwidth.wcswidth()`_ measures width 14,
  while *ghostty* measures width -42.

.. _ghosttylangChineseGan:

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
     3  `U+516B <https://codepoints.net/U+516B>`_  '\\u516b'  Lo                  2  CJK UNIFIED IDEOGRAPH-516B
     4  `U+6761 <https://codepoints.net/U+6761>`_  '\\u6761'  Lo                  2  CJK UNIFIED IDEOGRAPH-6761
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe7\xac\xac\xe5\x8d\x81\xe5\x85\xab\xe6\x9d\xa1|\\n12345678|\\n"
        第十八条|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *ghostty* measures width -16.

.. _ghosttylangChineseWu:

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
  while *ghostty* measures width -12.

.. _ghosttylangChickasaw:

Chickasaw
^^^^^^^^^

Sequence of language *Chickasaw* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     2  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     3  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     4  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
     5  `U+0331 <https://codepoints.net/U+0331>`_  '\\u0331'  Mn                  0  COMBINING MACRON BELOW
     6  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     8  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     9  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
    10  `U+006F <https://codepoints.net/U+006F>`_  'o'        Ll                  1  LATIN SMALL LETTER O
    11  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
    12  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
    13  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    14  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
    15  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    16  `U+0027 <https://codepoints.net/U+0027>`_  "'"        Po                  1  APOSTROPHE
    17  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
    18  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
    19  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
    20  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 20


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ith\xc3\xa1\xcc\xb1nahookmaka'chi.|\\n1234567890123456789|\\n"
        ithá̱nahookmaka'chi.|
        1234567890123456789|

- python `wcwidth.wcswidth()`_ measures width 19,
  while *ghostty* measures width 12.

.. _ghosttylangBora:

Bora
^^^^

Sequence of language *Bora* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
     3  `U+0070 <https://codepoints.net/U+0070>`_  'p'        Ll                  1  LATIN SMALL LETTER P
     4  `U+0268 <https://codepoints.net/U+0268>`_  '\\u0268'  Ll                  1  LATIN SMALL LETTER I WITH STROKE
     5  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     6  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
     7  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
     8  `U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
     9  `U+00F3 <https://codepoints.net/U+00F3>`_  '\\xf3'    Ll                  1  LATIN SMALL LETTER O WITH ACUTE
    10  `U+006A <https://codepoints.net/U+006A>`_  'j'        Ll                  1  LATIN SMALL LETTER J
    11  `U+0063 <https://codepoints.net/U+0063>`_  'c'        Ll                  1  LATIN SMALL LETTER C
    12  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
    13  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
    14  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
    15  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'    Ll                  1  LATIN SMALL LETTER I WITH ACUTE
    16  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
    17  `U+0079 <https://codepoints.net/U+0079>`_  'y'        Ll                  1  LATIN SMALL LETTER Y
    18  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'    Ll                  1  LATIN SMALL LETTER A WITH ACUTE
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "m\xc3\xa9p\xc9\xa8\xcc\x81\xc3\xa1\xc3\xa1b\xc3\xb3jcats\xc3\xadiy\xc3\xa1|\\n12345678901234567|\\n"
        mépɨ́áábójcatsíiyá|
        12345678901234567|

- python `wcwidth.wcswidth()`_ measures width 17,
  while *ghostty* measures width 11.

.. _ghosttylangGumuz:

Gumuz
^^^^^

Sequence of language *Gumuz* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0062 <https://codepoints.net/U+0062>`_  'b'       Ll                  1  LATIN SMALL LETTER B
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "baane|\\n12345|\\n"
        baane|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width -5.

.. _ghosttylangMarathi:

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0909 <https://codepoints.net/U+0909>`_  '\\u0909'  Lo                  1  DEVANAGARI LETTER U
     2  `U+092A <https://codepoints.net/U+092A>`_  '\\u092a'  Lo                  1  DEVANAGARI LETTER PA
     3  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     4  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     5  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
     6  `U+094B <https://codepoints.net/U+094B>`_  '\\u094b'  Mc                  0  DEVANAGARI VOWEL SIGN O
     7  `U+091C <https://codepoints.net/U+091C>`_  '\\u091c'  Lo                  1  DEVANAGARI LETTER JA
     8  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     9  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    10  `U+0902 <https://codepoints.net/U+0902>`_  '\\u0902'  Mn                  0  DEVANAGARI SIGN ANUSVARA
    11  `U+091A <https://codepoints.net/U+091A>`_  '\\u091a'  Lo                  1  DEVANAGARI LETTER CA
    12  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
    13  `U+092F <https://codepoints.net/U+092F>`_  '\\u092f'  Lo                  1  DEVANAGARI LETTER YA
    14  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 14


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x89\xe0\xa4\xaa\xe0\xa4\xbe\xe0\xa4\xaf\xe0\xa4\xaf\xe0\xa5\x8b\xe0\xa4\x9c\xe0\xa4\xa8\xe0\xa4\xbe\xe0\xa4\x82\xe0\xa4\x9a\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe|\\n12345678|\\n"
        उपाययोजनांच्या|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *ghostty* measures width 2.

.. _ghosttylangShipiboConibo:

Shipibo-Conibo
^^^^^^^^^^^^^^

Sequence of language *Shipibo-Conibo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
     2  `U+0043 <https://codepoints.net/U+0043>`_  'C'       Lu                  1  LATIN CAPITAL LETTER C
     3  `U+004F <https://codepoints.net/U+004F>`_  'O'       Lu                  1  LATIN CAPITAL LETTER O
     4  `U+004E <https://codepoints.net/U+004E>`_  'N'       Lu                  1  LATIN CAPITAL LETTER N
     5  `U+0053 <https://codepoints.net/U+0053>`_  'S'       Lu                  1  LATIN CAPITAL LETTER S
     6  `U+0048 <https://codepoints.net/U+0048>`_  'H'       Lu                  1  LATIN CAPITAL LETTER H
     7  `U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
     8  `U+004D <https://codepoints.net/U+004D>`_  'M'       Lu                  1  LATIN CAPITAL LETTER M
     9  `U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
    10  `U+004E <https://codepoints.net/U+004E>`_  'N'       Lu                  1  LATIN CAPITAL LETTER N
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ICONSHAMAN|\\n1234567890|\\n"
        ICONSHAMAN|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *ghostty* measures width -9.

.. _ghosttylangEvenki:

Evenki
^^^^^^

Sequence of language *Evenki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==========================
     1  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     2  `U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
     3  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     4  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     5  `U+044B <https://codepoints.net/U+044B>`_  '\\u044b'  Ll                  1  CYRILLIC SMALL LETTER YERU
     6  `U+0442 <https://codepoints.net/U+0442>`_  '\\u0442'  Ll                  1  CYRILLIC SMALL LETTER TE
     7  `U+044B <https://codepoints.net/U+044B>`_  '\\u044b'  Ll                  1  CYRILLIC SMALL LETTER YERU
     8  `U+043A <https://codepoints.net/U+043A>`_  '\\u043a'  Ll                  1  CYRILLIC SMALL LETTER KA
     9  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
    10  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
   ===  =========================================  =========  ==========  =========  ==========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xb0\xd0\xb2\xd0\xb0\xd0\xb4\xd1\x8b\xd1\x82\xd1\x8b\xd0\xba\xd0\xb8\xd0\xbd|\\n1234567890|\\n"
        авадытыкин|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *ghostty* measures width -2.

.. _ghosttylangNanai:

Nanai
^^^^^

Sequence of language *Nanai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
     2  `U+0432 <https://codepoints.net/U+0432>`_  '\\u0432'  Ll                  1  CYRILLIC SMALL LETTER VE
     3  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
     4  `U+0431 <https://codepoints.net/U+0431>`_  '\\u0431'  Ll                  1  CYRILLIC SMALL LETTER BE
     5  `U+043E <https://codepoints.net/U+043E>`_  '\\u043e'  Ll                  1  CYRILLIC SMALL LETTER O
     6  `U+0434 <https://codepoints.net/U+0434>`_  '\\u0434'  Ll                  1  CYRILLIC SMALL LETTER DE
     7  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     8  `U+0441 <https://codepoints.net/U+0441>`_  '\\u0441'  Ll                  1  CYRILLIC SMALL LETTER ES
     9  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
    10  `U+043B <https://codepoints.net/U+043B>`_  '\\u043b'  Ll                  1  CYRILLIC SMALL LETTER EL
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd1\x81\xd0\xb2\xd0\xbe\xd0\xb1\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x81\xd0\xb0\xd0\xbb|\\n1234567890|\\n"
        свободасал|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *ghostty* measures width 1.

.. _ghosttylangOrok:

Orok
^^^^

Sequence of language *Orok* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+043D <https://codepoints.net/U+043D>`_  '\\u043d'  Ll                  1  CYRILLIC SMALL LETTER EN
     2  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     3  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     4  `U+0438 <https://codepoints.net/U+0438>`_  '\\u0438'  Ll                  1  CYRILLIC SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd0\xbd\xd0\xb0\xd1\x80\xd0\xb8|\\n1234|\\n"
        нари|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width -5.

.. _ghosttylangYanesha:

Yaneshaʼ
^^^^^^^^

Sequence of language *Yaneshaʼ* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     4  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     5  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     6  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     7  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     8  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     9  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
    10  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "allohueney|\\n1234567890|\\n"
        allohueney|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *ghostty* measures width -2.

.. _ghosttylangNavajo:

Navajo
^^^^^^

Sequence of language *Navajo* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0044 <https://codepoints.net/U+0044>`_  'D'       Lu                  1  LATIN CAPITAL LETTER D
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     4  `U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'   Ll                  1  LATIN SMALL LETTER E WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Din\xc3\xa9|\\n1234|\\n"
        Diné|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width -18.

.. _ghosttylangAmarakaeri:

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
     4  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     5  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "huairi|\\n123456|\\n"
        huairi|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width -2.

.. _ghosttylangVeps:

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
  while *ghostty* measures width 3.

.. _ghosttylangSiona:

Siona
^^^^^

Sequence of language *Siona* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     5  `U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yija\xc3\xb1a|\\n123456|\\n"
        yijaña|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width -5.

.. _ghosttylangGilyak:

Gilyak
^^^^^^

Sequence of language *Gilyak* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================================
     1  `U+04FF <https://codepoints.net/U+04FF>`_  '\\u04ff'  Ll                  1  CYRILLIC SMALL LETTER HA WITH STROKE
     2  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
     3  `U+0440 <https://codepoints.net/U+0440>`_  '\\u0440'  Ll                  1  CYRILLIC SMALL LETTER ER
     4  `U+0430 <https://codepoints.net/U+0430>`_  '\\u0430'  Ll                  1  CYRILLIC SMALL LETTER A
   ===  =========================================  =========  ==========  =========  ====================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd3\xbf\xd0\xb0\xd1\x80\xd0\xb0|\\n1234|\\n"
        ӿара|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width -2.

.. _ghosttylangNepali:

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
  while *ghostty* measures width 6.

.. _ghosttylangSouthAzerbaijani:

South Azerbaijani
^^^^^^^^^^^^^^^^^

Sequence of language *South Azerbaijani* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     6  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     7  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "dostane|\\n1234567|\\n"
        dostane|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *ghostty* measures width -7.

.. _ghosttylangSecoya:

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
     3  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pai|\\n123|\\n"
        pai|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width -4.

.. _ghosttylangBengali:

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
  while *ghostty* measures width 6.

.. _ghosttylangYeonbyeon:

(Yeonbyeon)
^^^^^^^^^^^

Sequence of language *(Yeonbyeon)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+CCAB <https://codepoints.net/U+CCAB>`_  '\\uccab'  Lo                  2  HANGUL SYLLABLE CEOS
     2  `U+C9F8 <https://codepoints.net/U+C9F8>`_  '\\uc9f8'  Lo                  2  HANGUL SYLLABLE JJAE
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\xb2\xab\xec\xa7\xb8|\\n1234|\\n"
        첫째|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width -4.

.. _ghosttylangTamilSriLanka:

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0B85 <https://codepoints.net/U+0B85>`_  '\\u0b85'  Lo                  1  TAMIL LETTER A
     2  `U+0BB5 <https://codepoints.net/U+0BB5>`_  '\\u0bb5'  Lo                  1  TAMIL LETTER VA
     3  `U+0BB1 <https://codepoints.net/U+0BB1>`_  '\\u0bb1'  Lo                  1  TAMIL LETTER RRA
     4  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     5  `U+0BB1 <https://codepoints.net/U+0BB1>`_  '\\u0bb1'  Lo                  1  TAMIL LETTER RRA
     6  `U+0BC8 <https://codepoints.net/U+0BC8>`_  '\\u0bc8'  Mc                  0  TAMIL VOWEL SIGN AI
     7  `U+0BAA <https://codepoints.net/U+0BAA>`_  '\\u0baa'  Lo                  1  TAMIL LETTER PA
     8  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x85\xe0\xae\xb5\xe0\xae\xb1\xe0\xaf\x8d\xe0\xae\xb1\xe0\xaf\x88\xe0\xae\xaa\xe0\xaf\x8d|\\n12345|\\n"
        அவற்றைப்|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width -1.

.. _ghosttylangTamil:

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0B85 <https://codepoints.net/U+0B85>`_  '\\u0b85'  Lo                  1  TAMIL LETTER A
     2  `U+0BB5 <https://codepoints.net/U+0BB5>`_  '\\u0bb5'  Lo                  1  TAMIL LETTER VA
     3  `U+0BB1 <https://codepoints.net/U+0BB1>`_  '\\u0bb1'  Lo                  1  TAMIL LETTER RRA
     4  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
     5  `U+0BB1 <https://codepoints.net/U+0BB1>`_  '\\u0bb1'  Lo                  1  TAMIL LETTER RRA
     6  `U+0BC8 <https://codepoints.net/U+0BC8>`_  '\\u0bc8'  Mc                  0  TAMIL VOWEL SIGN AI
     7  `U+0BAA <https://codepoints.net/U+0BAA>`_  '\\u0baa'  Lo                  1  TAMIL LETTER PA
     8  `U+0BCD <https://codepoints.net/U+0BCD>`_  '\\u0bcd'  Mn                  0  TAMIL SIGN VIRAMA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x85\xe0\xae\xb5\xe0\xae\xb1\xe0\xaf\x8d\xe0\xae\xb1\xe0\xaf\x88\xe0\xae\xaa\xe0\xaf\x8d|\\n12345|\\n"
        அவற்றைப்|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width -1.

.. _ghosttylangColorado:

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
  while *ghostty* measures width -1.

.. _ghosttylangTelugu:

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0C09 <https://codepoints.net/U+0C09>`_  '\\u0c09'  Lo                  1  TELUGU LETTER U
     2  `U+0C26 <https://codepoints.net/U+0C26>`_  '\\u0c26'  Lo                  1  TELUGU LETTER DA
     3  `U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
     4  `U+0C18 <https://codepoints.net/U+0C18>`_  '\\u0c18'  Lo                  1  TELUGU LETTER GHA
     5  `U+0C4B <https://codepoints.net/U+0C4B>`_  '\\u0c4b'  Mn                  0  TELUGU VOWEL SIGN OO
     6  `U+0C37 <https://codepoints.net/U+0C37>`_  '\\u0c37'  Lo                  1  TELUGU LETTER SSA
     7  `U+0C3F <https://codepoints.net/U+0C3F>`_  '\\u0c3f'  Mn                  0  TELUGU VOWEL SIGN I
     8  `U+0C02 <https://codepoints.net/U+0C02>`_  '\\u0c02'  Mc                  0  TELUGU SIGN ANUSVARA
     9  `U+0C1A <https://codepoints.net/U+0C1A>`_  '\\u0c1a'  Lo                  1  TELUGU LETTER CA
    10  `U+0C41 <https://codepoints.net/U+0C41>`_  '\\u0c41'  Mc                  0  TELUGU VOWEL SIGN U
    11  `U+0C1A <https://codepoints.net/U+0C1A>`_  '\\u0c1a'  Lo                  1  TELUGU LETTER CA
    12  `U+0C41 <https://codepoints.net/U+0C41>`_  '\\u0c41'  Mc                  0  TELUGU VOWEL SIGN U
    13  `U+0C28 <https://codepoints.net/U+0C28>`_  '\\u0c28'  Lo                  1  TELUGU LETTER NA
    14  `U+0C4D <https://codepoints.net/U+0C4D>`_  '\\u0c4d'  Mn                  0  TELUGU SIGN VIRAMA
    15  `U+0C28 <https://codepoints.net/U+0C28>`_  '\\u0c28'  Lo                  1  TELUGU LETTER NA
    16  `U+0C26 <https://codepoints.net/U+0C26>`_  '\\u0c26'  Lo                  1  TELUGU LETTER DA
    17  `U+0C3F <https://codepoints.net/U+0C3F>`_  '\\u0c3f'  Mn                  0  TELUGU VOWEL SIGN I
    18  `U+002E <https://codepoints.net/U+002E>`_  '.'        Po                  1  FULL STOP
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 18


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\x89\xe0\xb0\xa6\xe0\xb1\x8d\xe0\xb0\x98\xe0\xb1\x8b\xe0\xb0\xb7\xe0\xb0\xbf\xe0\xb0\x82\xe0\xb0\x9a\xe0\xb1\x81\xe0\xb0\x9a\xe0\xb1\x81\xe0\xb0\xa8\xe0\xb1\x8d\xe0\xb0\xa8\xe0\xb0\xa6\xe0\xb0\xbf.|\\n1234567890|\\n"
        ఉద్ఘోషించుచున్నది.|
        1234567890|

- python `wcwidth.wcswidth()`_ measures width 10,
  while *ghostty* measures width 5.

.. _ghosttylangKorean:

Korean
^^^^^^

Sequence of language *Korean* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+C0AC <https://codepoints.net/U+C0AC>`_  '\\uc0ac'  Lo                  2  HANGUL SYLLABLE SA
     2  `U+C774 <https://codepoints.net/U+C774>`_  '\\uc774'  Lo                  2  HANGUL SYLLABLE I
     3  `U+C5D0 <https://codepoints.net/U+C5D0>`_  '\\uc5d0'  Lo                  2  HANGUL SYLLABLE E
     4  `U+C11C <https://codepoints.net/U+C11C>`_  '\\uc11c'  Lo                  2  HANGUL SYLLABLE SEO
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xec\x82\xac\xec\x9d\xb4\xec\x97\x90\xec\x84\x9c|\\n12345678|\\n"
        사이에서|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *ghostty* measures width 2.

.. _ghosttylangSanskrit:

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

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
     8  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
     9  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
    10  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    11  `U+0923 <https://codepoints.net/U+0923>`_  '\\u0923'  Lo                  1  DEVANAGARI LETTER NNA
    12  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
    13  `U+091E <https://codepoints.net/U+091E>`_  '\\u091e'  Lo                  1  DEVANAGARI LETTER NYA
    14  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
    15  `U+091A <https://codepoints.net/U+091A>`_  '\\u091a'  Lo                  1  DEVANAGARI LETTER CA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 15


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xb7\xe0\xa5\x8d\xe0\xa4\x9f\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa4\xbf\xe0\xa4\x95\xe0\xa4\xbe\xe0\xa4\xa3\xe0\xa4\xbe\xe0\xa4\x9e\xe0\xa5\x8d\xe0\xa4\x9a|\\n12345678|\\n"
        राष्ट्रिकाणाञ्च|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *ghostty* measures width -1.

.. _ghosttylangSanskritGrantha:

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =====================
     1  `U+00011330 <https://codepoints.net/U+00011330>`_  '\\U00011330'  Lo                  1  GRANTHA LETTER RA
     2  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
     3  `U+00011337 <https://codepoints.net/U+00011337>`_  '\\U00011337'  Lo                  1  GRANTHA LETTER SSA
     4  `U+0001134D <https://codepoints.net/U+0001134D>`_  '\\U0001134d'  Mc                  0  GRANTHA SIGN VIRAMA
     5  `U+0001131F <https://codepoints.net/U+0001131F>`_  '\\U0001131f'  Lo                  1  GRANTHA LETTER TTA
     6  `U+0001134D <https://codepoints.net/U+0001134D>`_  '\\U0001134d'  Mc                  0  GRANTHA SIGN VIRAMA
     7  `U+00011330 <https://codepoints.net/U+00011330>`_  '\\U00011330'  Lo                  1  GRANTHA LETTER RA
     8  `U+0001133F <https://codepoints.net/U+0001133F>`_  '\\U0001133f'  Mc                  0  GRANTHA VOWEL SIGN I
     9  `U+00011315 <https://codepoints.net/U+00011315>`_  '\\U00011315'  Lo                  1  GRANTHA LETTER KA
    10  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
    11  `U+00011323 <https://codepoints.net/U+00011323>`_  '\\U00011323'  Lo                  1  GRANTHA LETTER NNA
    12  `U+0001133E <https://codepoints.net/U+0001133E>`_  '\\U0001133e'  Mc                  0  GRANTHA VOWEL SIGN AA
    13  `U+0001131E <https://codepoints.net/U+0001131E>`_  '\\U0001131e'  Lo                  1  GRANTHA LETTER NYA
    14  `U+0001134D <https://codepoints.net/U+0001134D>`_  '\\U0001134d'  Mc                  0  GRANTHA SIGN VIRAMA
    15  `U+0001131A <https://codepoints.net/U+0001131A>`_  '\\U0001131a'  Lo                  1  GRANTHA LETTER CA
   ===  =================================================  =============  ==========  =========  =====================

Total codepoints: 15


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\xb0\xf0\x91\x8c\xbe\xf0\x91\x8c\xb7\xf0\x91\x8d\x8d\xf0\x91\x8c\x9f\xf0\x91\x8d\x8d\xf0\x91\x8c\xb0\xf0\x91\x8c\xbf\xf0\x91\x8c\x95\xf0\x91\x8c\xbe\xf0\x91\x8c\xa3\xf0\x91\x8c\xbe\xf0\x91\x8c\x9e\xf0\x91\x8d\x8d\xf0\x91\x8c\x9a|\\n12345678|\\n"
        𑌰𑌾𑌷𑍍𑌟𑍍𑌰𑌿𑌕𑌾𑌣𑌾𑌞𑍍𑌚|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *ghostty* measures width -1.

.. _ghosttylangTem:

Tem
^^^

Sequence of language *Tem* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     2  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     3  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     4  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
     5  `U+006D <https://codepoints.net/U+006D>`_  'm'       Ll                  1  LATIN SMALL LETTER M
     6  `U+00E1 <https://codepoints.net/U+00E1>`_  '\\xe1'   Ll                  1  LATIN SMALL LETTER A WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "g\xc3\xadr\xc3\xadm\xc3\xa1|\\n123456|\\n"
        gírímá|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width -1.

.. _ghosttylangCatalan2:

Catalan (2)
^^^^^^^^^^^

Sequence of language *Catalan (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0068 <https://codepoints.net/U+0068>`_  'h'       Ll                  1  LATIN SMALL LETTER H
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     3  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "han|\\n123|\\n"
        han|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width 0.

.. _ghosttylangKannada:

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0CB0 <https://codepoints.net/U+0CB0>`_  '\\u0cb0'  Lo                  1  KANNADA LETTER RA
     2  `U+0CBE <https://codepoints.net/U+0CBE>`_  '\\u0cbe'  Mc                  0  KANNADA VOWEL SIGN AA
     3  `U+0CB7 <https://codepoints.net/U+0CB7>`_  '\\u0cb7'  Lo                  1  KANNADA LETTER SSA
     4  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
     5  `U+0C9F <https://codepoints.net/U+0C9F>`_  '\\u0c9f'  Lo                  1  KANNADA LETTER TTA
     6  `U+0CCD <https://codepoints.net/U+0CCD>`_  '\\u0ccd'  Mn                  0  KANNADA SIGN VIRAMA
     7  `U+0CB0 <https://codepoints.net/U+0CB0>`_  '\\u0cb0'  Lo                  1  KANNADA LETTER RA
     8  `U+0C97 <https://codepoints.net/U+0C97>`_  '\\u0c97'  Lo                  1  KANNADA LETTER GA
     9  `U+0CB3 <https://codepoints.net/U+0CB3>`_  '\\u0cb3'  Lo                  1  KANNADA LETTER LLA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\xb0\xe0\xb2\xbe\xe0\xb2\xb7\xe0\xb3\x8d\xe0\xb2\x9f\xe0\xb3\x8d\xe0\xb2\xb0\xe0\xb2\x97\xe0\xb2\xb3|\\n123456|\\n"
        ರಾಷ್ಟ್ರಗಳ|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width 0.

.. _ghosttylangMirandese:

Mirandese
^^^^^^^^^

Sequence of language *Mirandese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     3  `U+0064 <https://codepoints.net/U+0064>`_  'd'       Ll                  1  LATIN SMALL LETTER D
     4  `U+0072 <https://codepoints.net/U+0072>`_  'r'       Ll                  1  LATIN SMALL LETTER R
     5  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     6  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     7  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     8  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "andrento|\\n12345678|\\n"
        andrento|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *ghostty* measures width 4.

.. _ghosttylangYiddishEastern:

Yiddish, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Yiddish, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+05E4 <https://codepoints.net/U+05E4>`_  '\\u05e4'  Lo                  1  HEBREW LETTER PE
     2  `U+05BF <https://codepoints.net/U+05BF>`_  '\\u05bf'  Mn                  0  HEBREW POINT RAFE
     3  `U+05E2 <https://codepoints.net/U+05E2>`_  '\\u05e2'  Lo                  1  HEBREW LETTER AYIN
     4  `U+05DC <https://codepoints.net/U+05DC>`_  '\\u05dc'  Lo                  1  HEBREW LETTER LAMED
     5  `U+05E7 <https://codepoints.net/U+05E7>`_  '\\u05e7'  Lo                  1  HEBREW LETTER QOF
     6  `U+05E2 <https://codepoints.net/U+05E2>`_  '\\u05e2'  Lo                  1  HEBREW LETTER AYIN
     7  `U+05E8 <https://codepoints.net/U+05E8>`_  '\\u05e8'  Lo                  1  HEBREW LETTER RESH
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd7\xa4\xd6\xbf\xd7\xa2\xd7\x9c\xd7\xa7\xd7\xa2\xd7\xa8|\\n123456|\\n"
        פֿעלקער|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width -4.

.. _ghosttylangw:

Éwé
^^^

Sequence of language *Éwé* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     2  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "asu|\\n123|\\n"
        asu|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width -3.

.. _ghosttylangArabicStandard:

Arabic, Standard
^^^^^^^^^^^^^^^^

Sequence of language *Arabic, Standard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
     2  `U+0630 <https://codepoints.net/U+0630>`_  '\\u0630'  Lo                  1  ARABIC LETTER THAL
     3  `U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x87\xd8\xb0\xd9\x87|\\n123|\\n"
        هذه|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width -4.

.. _ghosttylangPicard:

Picard
^^^^^^

Sequence of language *Picard* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     2  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
     3  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
     4  `U+002D <https://codepoints.net/U+002D>`_  '-'       Pd                  1  HYPHEN-MINUS
     5  `U+0045 <https://codepoints.net/U+0045>`_  'E'       Lu                  1  LATIN CAPITAL LETTER E
     6  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
     8  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     9  `U+0073 <https://codepoints.net/U+0073>`_  's'       Ll                  1  LATIN SMALL LETTER S
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "l\xc3\xa8s-Etats|\\n123456789|\\n"
        lès-Etats|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *ghostty* measures width 6.

.. _ghosttylangKabyle:

Kabyle
^^^^^^

Sequence of language *Kabyle* from midpoint of alignment failure records:

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
  while *ghostty* measures width -7.

.. _ghosttylangLingalatones:

Lingala (tones)
^^^^^^^^^^^^^^^

Sequence of language *Lingala (tones)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     4  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     5  `U+0301 <https://codepoints.net/U+0301>`_  '\\u0301'  Mn                  0  COMBINING ACUTE ACCENT
     6  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "maka\xcc\x81si|\\n123456|\\n"
        makási|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width 0.

.. _ghosttylangTicuna:

Ticuna
^^^^^^

Sequence of language *Ticuna* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+0129 <https://codepoints.net/U+0129>`_  '\\u0129'  Ll                  1  LATIN SMALL LETTER I WITH TILDE
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc4\xa9|\\n1|\\n"
        ĩ|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *ghostty* measures width -8.

.. _ghosttylangTamazightCentralAtlas:

Tamazight, Central Atlas
^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Tamazight, Central Atlas* from midpoint of alignment failure records:

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
  while *ghostty* measures width -10.

.. _ghosttylangMixtecMetlatnoc:

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
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     4  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     5  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tnu'u|\\n12345|\\n"
        tnu'u|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width -5.

.. _ghosttylangFur:

Fur
^^^

Sequence of language *Fur* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     4  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     5  `U+00EA <https://codepoints.net/U+00EA>`_  '\\xea'   Ll                  1  LATIN SMALL LETTER E WITH CIRCUMFLEX
     6  `U+002D <https://codepoints.net/U+002D>`_  '-'       Pd                  1  HYPHEN-MINUS
     7  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     8  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
   ===  =========================================  ========  ==========  =========  ====================================

Total codepoints: 8


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "tull\xc3\xaa-ii|\\n12345678|\\n"
        tullê-ii|
        12345678|

- python `wcwidth.wcswidth()`_ measures width 8,
  while *ghostty* measures width 1.

.. _ghosttylangPularAdlam:

Pular (Adlam)
^^^^^^^^^^^^^

Sequence of language *Pular (Adlam)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ========================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ========================
     1  `U+0001E932 <https://codepoints.net/U+0001E932>`_  '\\U0001e932'  Ll                  1  ADLAM SMALL LETTER NUN
     2  `U+0027 <https://codepoints.net/U+0027>`_          "'"            Po                  1  APOSTROPHE
     3  `U+0001E923 <https://codepoints.net/U+0001E923>`_  '\\U0001e923'  Ll                  1  ADLAM SMALL LETTER DAALI
     4  `U+0001E92B <https://codepoints.net/U+0001E92B>`_  '\\U0001e92b'  Ll                  1  ADLAM SMALL LETTER E
     5  `U+0001E945 <https://codepoints.net/U+0001E945>`_  '\\U0001e945'  Mn                  0  ADLAM VOWEL LENGTHENER
     6  `U+0001E932 <https://codepoints.net/U+0001E932>`_  '\\U0001e932'  Ll                  1  ADLAM SMALL LETTER NUN
   ===  =================================================  =============  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9e\xa4\xb2'\xf0\x9e\xa4\xa3\xf0\x9e\xa4\xab\xf0\x9e\xa5\x85\xf0\x9e\xa4\xb2|\\n12345|\\n"
        𞤲'𞤣𞤫𞥅𞤲|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width 3.

.. _ghosttylangAssyrianNeoAramaic:

Assyrian Neo-Aramaic
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Assyrian Neo-Aramaic* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
     2  `U+071A <https://codepoints.net/U+071A>`_  '\\u071a'  Lo                  1  SYRIAC LETTER HETH
     3  `U+072A <https://codepoints.net/U+072A>`_  '\\u072a'  Lo                  1  SYRIAC LETTER RISH
     4  `U+0722 <https://codepoints.net/U+0722>`_  '\\u0722'  Lo                  1  SYRIAC LETTER NUN
     5  `U+0710 <https://codepoints.net/U+0710>`_  '\\u0710'  Lo                  1  SYRIAC LETTER ALAPH
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdc\x90\xdc\x9a\xdc\xaa\xdc\xa2\xdc\x90|\\n12345|\\n"
        ܐܚܪܢܐ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width 3.

.. _ghosttylangMaldivian:

Maldivian
^^^^^^^^^

Sequence of language *Maldivian* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0780 <https://codepoints.net/U+0780>`_  '\\u0780'  Lo                  1  THAANA LETTER HAA
     2  `U+07AC <https://codepoints.net/U+07AC>`_  '\\u07ac'  Mn                  0  THAANA EBEFILI
     3  `U+078B <https://codepoints.net/U+078B>`_  '\\u078b'  Lo                  1  THAANA LETTER DHAALU
     4  `U+07AA <https://codepoints.net/U+07AA>`_  '\\u07aa'  Mn                  0  THAANA UBUFILI
     5  `U+0789 <https://codepoints.net/U+0789>`_  '\\u0789'  Lo                  1  THAANA LETTER MEEMU
     6  `U+07A6 <https://codepoints.net/U+07A6>`_  '\\u07a6'  Mn                  0  THAANA ABAFILI
     7  `U+0786 <https://codepoints.net/U+0786>`_  '\\u0786'  Lo                  1  THAANA LETTER KAAFU
     8  `U+07A9 <https://codepoints.net/U+07A9>`_  '\\u07a9'  Mn                  0  THAANA EEBEEFILI
     9  `U+060C <https://codepoints.net/U+060C>`_  '\\u060c'  Po                  1  ARABIC COMMA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xde\x80\xde\xac\xde\x8b\xde\xaa\xde\x89\xde\xa6\xde\x86\xde\xa9\xd8\x8c|\\n12345|\\n"
        ހެދުމަކީ،|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width -2.

.. _ghosttylangFrenchWelche:

French (Welche)
^^^^^^^^^^^^^^^

Sequence of language *French (Welche)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+0064 <https://codepoints.net/U+0064>`_  'd'        Ll                  1  LATIN SMALL LETTER D
     2  `U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
     3  `U+006C <https://codepoints.net/U+006C>`_  'l'        Ll                  1  LATIN SMALL LETTER L
     4  `U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
     5  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     6  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "d\xe2\x80\x99l\xe2\x80\x99am|\\n123456|\\n"
        d’l’am|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width 1.

.. _ghosttylangSaintLucianCreoleFrench:

Saint Lucian Creole French
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sequence of language *Saint Lucian Creole French* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     2  `U+006F <https://codepoints.net/U+006F>`_  'o'       Ll                  1  LATIN SMALL LETTER O
     3  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pou|\\n123|\\n"
        pou|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width 1.

.. _ghosttylangGa:

Ga
^^

Sequence of language *Ga* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     2  `U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
     3  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
     4  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     5  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "gb\xc9\x94m\xc9\x94|\\n12345|\\n"
        gbɔmɔ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width 1.

.. _ghosttylangGen:

Gen
^^^

Sequence of language *Gen* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     2  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     3  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     4  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
     5  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     6  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "jij\xc3\xa8j\xc3\xa8|\\n123456|\\n"
        jijèjè|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width 4.

.. _ghosttylangAja:

Aja
^^^

Sequence of language *Aja* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==============================
     1  `U+0045 <https://codepoints.net/U+0045>`_  'E'        Lu                  1  LATIN CAPITAL LETTER E
     2  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     3  `U+0062 <https://codepoints.net/U+0062>`_  'b'        Ll                  1  LATIN SMALL LETTER B
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     5  `U+0066 <https://codepoints.net/U+0066>`_  'f'        Ll                  1  LATIN SMALL LETTER F
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     7  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     8  `U+0256 <https://codepoints.net/U+0256>`_  '\\u0256'  Ll                  1  LATIN SMALL LETTER D WITH TAIL
     9  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
    10  `U+0256 <https://codepoints.net/U+0256>`_  '\\u0256'  Ll                  1  LATIN SMALL LETTER D WITH TAIL
    11  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  =========  ==========  =========  ==============================

Total codepoints: 11


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "Egbefan\xc9\x96e\xc9\x96e|\\n12345678901|\\n"
        Egbefanɖeɖe|
        12345678901|

- python `wcwidth.wcswidth()`_ measures width 11,
  while *ghostty* measures width 8.

.. _ghosttylangFarsiWestern:

Farsi, Western
^^^^^^^^^^^^^^

Sequence of language *Farsi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0645 <https://codepoints.net/U+0645>`_  '\\u0645'  Lo                  1  ARABIC LETTER MEEM
     2  `U+062C <https://codepoints.net/U+062C>`_  '\\u062c'  Lo                  1  ARABIC LETTER JEEM
     3  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     4  `U+0647 <https://codepoints.net/U+0647>`_  '\\u0647'  Lo                  1  ARABIC LETTER HEH
     5  `U+062F <https://codepoints.net/U+062F>`_  '\\u062f'  Lo                  1  ARABIC LETTER DAL
     6  `U+062A <https://codepoints.net/U+062A>`_  '\\u062a'  Lo                  1  ARABIC LETTER TEH
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x85\xd8\xac\xd8\xa7\xd9\x87\xd8\xaf\xd8\xaa|\\n123456|\\n"
        مجاهدت|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width 5.

.. _ghosttylangDendi:

Dendi
^^^^^

Sequence of language *Dendi* from midpoint of alignment failure records:

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
  while *ghostty* measures width -4.

.. _ghosttylangMazahuaCentral:

Mazahua Central
^^^^^^^^^^^^^^^

Sequence of language *Mazahua Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+006A <https://codepoints.net/U+006A>`_  'j'       Ll                  1  LATIN SMALL LETTER J
     4  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xb1eje|\\n1234|\\n"
        ñeje|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width -1.

.. _ghosttylangMaori2:

Maori (2)
^^^^^^^^^

Sequence of language *Maori (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+0049 <https://codepoints.net/U+0049>`_  'I'       Lu                  1  LATIN CAPITAL LETTER I
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 1


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "I|\\n1|\\n"
        I|
        1|

- python `wcwidth.wcswidth()`_ measures width 1,
  while *ghostty* measures width -7.

.. _ghosttylangSererSine:

Serer-Sine
^^^^^^^^^^

Sequence of language *Serer-Sine* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0079 <https://codepoints.net/U+0079>`_  'y'       Ll                  1  LATIN SMALL LETTER Y
     2  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'       Ll                  1  LATIN SMALL LETTER E
     4  `U+0067 <https://codepoints.net/U+0067>`_  'g'       Ll                  1  LATIN SMALL LETTER G
     5  `U+006E <https://codepoints.net/U+006E>`_  'n'       Ll                  1  LATIN SMALL LETTER N
     6  `U+0069 <https://codepoints.net/U+0069>`_  'i'       Ll                  1  LATIN SMALL LETTER I
     7  `U+0074 <https://codepoints.net/U+0074>`_  't'       Ll                  1  LATIN SMALL LETTER T
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "yeegnit|\\n1234567|\\n"
        yeegnit|
        1234567|

- python `wcwidth.wcswidth()`_ measures width 7,
  while *ghostty* measures width 5.

.. _ghosttylangDari:

Dari
^^^^

Sequence of language *Dari* from midpoint of alignment failure records:

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
  while *ghostty* measures width -4.

.. _ghosttylangDitammari:

Ditammari
^^^^^^^^^

Sequence of language *Ditammari* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+0069 <https://codepoints.net/U+0069>`_  'i'        Ll                  1  LATIN SMALL LETTER I
     2  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     3  `U+0065 <https://codepoints.net/U+0065>`_  'e'        Ll                  1  LATIN SMALL LETTER E
     4  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     5  `U+0073 <https://codepoints.net/U+0073>`_  's'        Ll                  1  LATIN SMALL LETTER S
     6  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     7  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     8  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     9  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 9


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "itensaak\xc9\x9b|\\n123456789|\\n"
        itensaakɛ|
        123456789|

- python `wcwidth.wcswidth()`_ measures width 9,
  while *ghostty* measures width 7.

.. _ghosttylangUduk:

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
  while *ghostty* measures width -4.

.. _ghosttylangYoruba:

Yoruba
^^^^^^

Sequence of language *Yoruba* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+006C <https://codepoints.net/U+006C>`_  'l'       Ll                  1  LATIN SMALL LETTER L
     2  `U+00E8 <https://codepoints.net/U+00E8>`_  '\\xe8'   Ll                  1  LATIN SMALL LETTER E WITH GRAVE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "l\xc3\xa8|\\n12|\\n"
        lè|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width 0.

.. _ghosttylangVietnamese:

Vietnamese
^^^^^^^^^^

Sequence of language *Vietnamese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ================================
     1  `U+0111 <https://codepoints.net/U+0111>`_  '\\u0111'  Ll                  1  LATIN SMALL LETTER D WITH STROKE
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'        Ll                  1  LATIN SMALL LETTER A
     3  `U+0303 <https://codepoints.net/U+0303>`_  '\\u0303'  Mn                  0  COMBINING TILDE
   ===  =========================================  =========  ==========  =========  ================================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc4\x91a\xcc\x83|\\n12|\\n"
        đã|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -2.

.. _ghosttylangUrdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xdb\x92|\\n12|\\n"
        کے|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -3.

.. _ghosttylangPashtoNorthern:

Pashto, Northern
^^^^^^^^^^^^^^^^

Sequence of language *Pashto, Northern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===========================
     1  `U+06AB <https://codepoints.net/U+06AB>`_  '\\u06ab'  Lo                  1  ARABIC LETTER KAF WITH RING
     2  `U+0689 <https://codepoints.net/U+0689>`_  '\\u0689'  Lo                  1  ARABIC LETTER DAL WITH RING
   ===  =========================================  =========  ==========  =========  ===========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xab\xda\x89|\\n12|\\n"
        ګډ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -2.

.. _ghosttylangSeraiki:

Seraiki
^^^^^^^

Sequence of language *Seraiki* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+06C1 <https://codepoints.net/U+06C1>`_  '\\u06c1'  Lo                  1  ARABIC LETTER HEH GOAL
     2  `U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xdb\x81\xdb\x92|\\n12|\\n"
        ہے|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -2.

.. _ghosttylangBelandaViri:

Belanda Viri
^^^^^^^^^^^^

Sequence of language *Belanda Viri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+006B <https://codepoints.net/U+006B>`_  'k'       Ll                  1  LATIN SMALL LETTER K
     2  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     3  `U+00ED <https://codepoints.net/U+00ED>`_  '\\xed'   Ll                  1  LATIN SMALL LETTER I WITH ACUTE
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "kp\xc3\xad|\\n123|\\n"
        kpí|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width -3.

.. _ghosttylangUrdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+06A9 <https://codepoints.net/U+06A9>`_  '\\u06a9'  Lo                  1  ARABIC LETTER KEHEH
     2  `U+06D2 <https://codepoints.net/U+06D2>`_  '\\u06d2'  Lo                  1  ARABIC LETTER YEH BARREE
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xda\xa9\xdb\x92|\\n12|\\n"
        کے|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -3.

.. _ghosttylangBamun:

Bamun
^^^^^

Sequence of language *Bamun* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ====================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ====================
     1  `U+0070 <https://codepoints.net/U+0070>`_  'p'       Ll                  1  LATIN SMALL LETTER P
     2  `U+0061 <https://codepoints.net/U+0061>`_  'a'       Ll                  1  LATIN SMALL LETTER A
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "pa|\\n12|\\n"
        pa|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -3.

.. _ghosttylangDagaareSouthern:

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
  while *ghostty* measures width 0.

.. _ghosttylangChinantecChiltepec:

Chinantec, Chiltepec
^^^^^^^^^^^^^^^^^^^^

Sequence of language *Chinantec, Chiltepec* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ===============================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ===============================
     1  `U+00F1 <https://codepoints.net/U+00F1>`_  '\\xf1'   Ll                  1  LATIN SMALL LETTER N WITH TILDE
     2  `U+0075 <https://codepoints.net/U+0075>`_  'u'       Ll                  1  LATIN SMALL LETTER U
     3  `U+0027 <https://codepoints.net/U+0027>`_  "'"       Po                  1  APOSTROPHE
     4  `U+003B <https://codepoints.net/U+003B>`_  ';'       Po                  1  SEMICOLON
   ===  =========================================  ========  ==========  =========  ===============================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc3\xb1u';|\\n1234|\\n"
        ñu';|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width 1.

.. _ghosttylangJavaneseJavanese:

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+A9A0 <https://codepoints.net/U+A9A0>`_  '\\ua9a0'  Lo                  1  JAVANESE LETTER TA
     2  `U+A9B6 <https://codepoints.net/U+A9B6>`_  '\\ua9b6'  Mn                  0  JAVANESE VOWEL SIGN WULU
     3  `U+A981 <https://codepoints.net/U+A981>`_  '\\ua981'  Mn                  0  JAVANESE SIGN CECAK
     4  `U+A9B1 <https://codepoints.net/U+A9B1>`_  '\\ua9b1'  Lo                  1  JAVANESE LETTER SA
     5  `U+A9A9 <https://codepoints.net/U+A9A9>`_  '\\ua9a9'  Lo                  1  JAVANESE LETTER MA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\xa0\xea\xa6\xb6\xea\xa6\x81\xea\xa6\xb1\xea\xa6\xa9|\\n123|\\n"
        ꦠꦶꦁꦱꦩ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width 0.

.. _ghosttylangPanjabiWestern:

Panjabi, Western
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Western* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0648 <https://codepoints.net/U+0648>`_  '\\u0648'  Lo                  1  ARABIC LETTER WAW
     2  `U+0642 <https://codepoints.net/U+0642>`_  '\\u0642'  Lo                  1  ARABIC LETTER QAF
     3  `U+0627 <https://codepoints.net/U+0627>`_  '\\u0627'  Lo                  1  ARABIC LETTER ALEF
     4  `U+0631 <https://codepoints.net/U+0631>`_  '\\u0631'  Lo                  1  ARABIC LETTER REH
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd9\x88\xd9\x82\xd8\xa7\xd8\xb1|\\n1234|\\n"
        وقار|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width 1.

.. _ghosttylangMaithili:

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     2  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
     3  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     4  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     5  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
     6  `U+0932 <https://codepoints.net/U+0932>`_  '\\u0932'  Lo                  1  DEVANAGARI LETTER LA
     7  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
     8  `U+0916 <https://codepoints.net/U+0916>`_  '\\u0916'  Lo                  1  DEVANAGARI LETTER KHA
     9  `U+093F <https://codepoints.net/U+093F>`_  '\\u093f'  Mc                  0  DEVANAGARI VOWEL SIGN I
    10  `U+0924 <https://codepoints.net/U+0924>`_  '\\u0924'  Lo                  1  DEVANAGARI LETTER TA
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 10


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xa8\xe0\xa4\xbf\xe0\xa4\xae\xe0\xa5\x8d\xe0\xa4\xa8\xe0\xa4\xb2\xe0\xa4\xbf\xe0\xa4\x96\xe0\xa4\xbf\xe0\xa4\xa4|\\n123456|\\n"
        निम्नलिखित|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width 4.

.. _ghosttylangDinkaNortheastern:

Dinka, Northeastern
^^^^^^^^^^^^^^^^^^^

Sequence of language *Dinka, Northeastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================================
     1  `U+0074 <https://codepoints.net/U+0074>`_  't'        Ll                  1  LATIN SMALL LETTER T
     2  `U+0068 <https://codepoints.net/U+0068>`_  'h'        Ll                  1  LATIN SMALL LETTER H
     3  `U+00F6 <https://codepoints.net/U+00F6>`_  '\\xf6'    Ll                  1  LATIN SMALL LETTER O WITH DIAERESIS
     4  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
   ===  =========================================  =========  ==========  =========  ===================================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "th\xc3\xb6\xc5\x8b|\\n1234|\\n"
        thöŋ|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width 1.

.. _ghosttylangMor:

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
  while *ghostty* measures width -1.

.. _ghosttylangGujarati:

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0A85 <https://codepoints.net/U+0A85>`_  '\\u0a85'  Lo                  1  GUJARATI LETTER A
     2  `U+0A82 <https://codepoints.net/U+0A82>`_  '\\u0a82'  Mn                  0  GUJARATI SIGN ANUSVARA
     3  `U+0AA4 <https://codepoints.net/U+0AA4>`_  '\\u0aa4'  Lo                  1  GUJARATI LETTER TA
     4  `U+0A83 <https://codepoints.net/U+0A83>`_  '\\u0a83'  Mc                  0  GUJARATI SIGN VISARGA
     5  `U+0A95 <https://codepoints.net/U+0A95>`_  '\\u0a95'  Lo                  1  GUJARATI LETTER KA
     6  `U+0AB0 <https://codepoints.net/U+0AB0>`_  '\\u0ab0'  Lo                  1  GUJARATI LETTER RA
     7  `U+0AA3 <https://codepoints.net/U+0AA3>`_  '\\u0aa3'  Lo                  1  GUJARATI LETTER NNA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 7


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\x85\xe0\xaa\x82\xe0\xaa\xa4\xe0\xaa\x83\xe0\xaa\x95\xe0\xaa\xb0\xe0\xaa\xa3|\\n12345|\\n"
        અંતઃકરણ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *ghostty* measures width 3.

.. _ghosttylangOtomiMezquital:

Otomi, Mezquital
^^^^^^^^^^^^^^^^

Sequence of language *Otomi, Mezquital* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  ========  ==========  =========  ======================
     #  Codepoint                                  Python    Category      wcwidth  Name
   ===  =========================================  ========  ==========  =========  ======================
     1  `U+004D <https://codepoints.net/U+004D>`_  'M'       Lu                  1  LATIN CAPITAL LETTER M
     2  `U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
     3  `U+0041 <https://codepoints.net/U+0041>`_  'A'       Lu                  1  LATIN CAPITAL LETTER A
   ===  =========================================  ========  ==========  =========  ======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "MAA|\\n123|\\n"
        MAA|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width 1.

.. _ghosttylangFon:

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
   ===  =========================================  ========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "bo|\\n12|\\n"
        bo|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -1.

.. _ghosttylangLamnso:

Lamnso'
^^^^^^^

Sequence of language *Lamnso'* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+014B <https://codepoints.net/U+014B>`_  '\\u014b'  Ll                  1  LATIN SMALL LETTER ENG
     2  `U+006B <https://codepoints.net/U+006B>`_  'k'        Ll                  1  LATIN SMALL LETTER K
     3  `U+00E0 <https://codepoints.net/U+00E0>`_  '\\xe0'    Ll                  1  LATIN SMALL LETTER A WITH GRAVE
     4  `U+2019 <https://codepoints.net/U+2019>`_  '\\u2019'  Pf                  1  RIGHT SINGLE QUOTATION MARK
     5  `U+006D <https://codepoints.net/U+006D>`_  'm'        Ll                  1  LATIN SMALL LETTER M
     6  `U+00E9 <https://codepoints.net/U+00E9>`_  '\\xe9'    Ll                  1  LATIN SMALL LETTER E WITH ACUTE
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xc5\x8bk\xc3\xa0\xe2\x80\x99m\xc3\xa9|\\n123456|\\n"
        ŋkà’mé|
        123456|

- python `wcwidth.wcswidth()`_ measures width 6,
  while *ghostty* measures width 4.

.. _ghosttylangBaatonum:

Baatonum
^^^^^^^^

Sequence of language *Baatonum* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+025B <https://codepoints.net/U+025B>`_  '\\u025b'  Ll                  1  LATIN SMALL LETTER OPEN E
     3  `U+003A <https://codepoints.net/U+003A>`_  ':'        Po                  1  COLON
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "n\xc9\x9b:|\\n123|\\n"
        nɛ:|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width 1.

.. _ghosttylangWaama:

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
  while *ghostty* measures width -1.

.. _ghosttylangMagahi:

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0939 <https://codepoints.net/U+0939>`_  '\\u0939'  Lo                  1  DEVANAGARI LETTER HA
     2  `U+0908 <https://codepoints.net/U+0908>`_  '\\u0908'  Lo                  1  DEVANAGARI LETTER II
     3  `U+0964 <https://codepoints.net/U+0964>`_  '\\u0964'  Po                  1  DEVANAGARI DANDA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb9\xe0\xa4\x88\xe0\xa5\xa4|\\n123|\\n"
        हई।|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width 1.

.. _ghosttylangBhojpuri:

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
  while *ghostty* measures width -5.

.. _ghosttylangHindi:

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0938 <https://codepoints.net/U+0938>`_  '\\u0938'  Lo                  1  DEVANAGARI LETTER SA
     2  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     3  `U+094D <https://codepoints.net/U+094D>`_  '\\u094d'  Mn                  0  DEVANAGARI SIGN VIRAMA
     4  `U+092E <https://codepoints.net/U+092E>`_  '\\u092e'  Lo                  1  DEVANAGARI LETTER MA
     5  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
     6  `U+0928 <https://codepoints.net/U+0928>`_  '\\u0928'  Lo                  1  DEVANAGARI LETTER NA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 6


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\xb8\xe0\xa4\xae\xe0\xa5\x8d\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8|\\n1234|\\n"
        सम्मान|
        1234|

- python `wcwidth.wcswidth()`_ measures width 4,
  while *ghostty* measures width -2.

.. _ghosttylangChakma:

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ================
     1  `U+00011103 <https://codepoints.net/U+00011103>`_  '\\U00011103'  Lo                  1  CHAKMA LETTER AA
     2  `U+00011133 <https://codepoints.net/U+00011133>`_  '\\U00011133'  Mn                  0  CHAKMA VIRAMA
     3  `U+00011103 <https://codepoints.net/U+00011103>`_  '\\U00011103'  Lo                  1  CHAKMA LETTER AA
   ===  =================================================  =============  ==========  =========  ================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\x83\xf0\x91\x84\xb3\xf0\x91\x84\x83|\\n12|\\n"
        𑄃𑄳𑄃|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width 0.

.. _ghosttylangDangme:

Dangme
^^^^^^

Sequence of language *Dangme* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =========================
     1  `U+006E <https://codepoints.net/U+006E>`_  'n'        Ll                  1  LATIN SMALL LETTER N
     2  `U+0067 <https://codepoints.net/U+0067>`_  'g'        Ll                  1  LATIN SMALL LETTER G
     3  `U+0254 <https://codepoints.net/U+0254>`_  '\\u0254'  Ll                  1  LATIN SMALL LETTER OPEN O
   ===  =========================================  =========  ==========  =========  =========================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "ng\xc9\x94|\\n123|\\n"
        ngɔ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *ghostty* measures width 1.

.. _ghosttylangPanjabiEastern:

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+0A17 <https://codepoints.net/U+0A17>`_  '\\u0a17'  Lo                  1  GURMUKHI LETTER GA
     2  `U+0A71 <https://codepoints.net/U+0A71>`_  '\\u0a71'  Mn                  0  GURMUKHI ADDAK
     3  `U+0A32 <https://codepoints.net/U+0A32>`_  '\\u0a32'  Lo                  1  GURMUKHI LETTER LA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\x97\xe0\xa9\xb1\xe0\xa8\xb2|\\n12|\\n"
        ਗੱਲ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width -5.

.. _ghosttylangTibetanCentral:

Tibetan, Central
^^^^^^^^^^^^^^^^

Sequence of language *Tibetan, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0F51 <https://codepoints.net/U+0F51>`_  '\\u0f51'  Lo                  1  TIBETAN LETTER DA
     2  `U+0F7C <https://codepoints.net/U+0F7C>`_  '\\u0f7c'  Mn                  0  TIBETAN VOWEL SIGN O
     3  `U+0F53 <https://codepoints.net/U+0F53>`_  '\\u0f53'  Lo                  1  TIBETAN LETTER NA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xbd\x91\xe0\xbd\xbc\xe0\xbd\x93|\\n12|\\n"
        དོན|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *ghostty* measures width 0.

.. _ghosttylangTaiDam:

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
  while *ghostty* measures width 1.

.. _ghosttylangDzongkha:

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
  while *ghostty* measures width -2.

.. _ghosttydecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

DEC private modes results for *ghostty*: 36 changeable modes
of 36 supported out of 157 total modes tested (22.9% support, 22.9% changeable).

Complete list of DEC private modes tested:

.. _ghosttydecmode1:

.. _ghosttydecmode3:

.. _ghosttydecmode4:

.. _ghosttydecmode5:

.. _ghosttydecmode6:

.. _ghosttydecmode7:

.. _ghosttydecmode8:

.. _ghosttydecmode9:

.. _ghosttydecmode12:

.. _ghosttydecmode25:

.. _ghosttydecmode40:

.. _ghosttydecmode45:

.. _ghosttydecmode47:

.. _ghosttydecmode66:

.. _ghosttydecmode69:

.. _ghosttydecmode1000:

.. _ghosttydecmode1002:

.. _ghosttydecmode1003:

.. _ghosttydecmode1004:

.. _ghosttydecmode1005:

.. _ghosttydecmode1006:

.. _ghosttydecmode1007:

.. _ghosttydecmode1015:

.. _ghosttydecmode1016:

.. _ghosttydecmode1035:

.. _ghosttydecmode1036:

.. _ghosttydecmode1039:

.. _ghosttydecmode1045:

.. _ghosttydecmode1047:

.. _ghosttydecmode1048:

.. _ghosttydecmode1049:

.. _ghosttydecmode2004:

.. _ghosttydecmode2026:

.. _ghosttydecmode2027:

.. _ghosttydecmode2031:

.. _ghosttydecmode2048:

.. table::
   :class: sphinx-datatable

   ======  =============================  =======================================================================  ===========  ============  =========
     Mode  Name                           Description                                                              Supported    Changeable    Enabled
   ======  =============================  =======================================================================  ===========  ============  =========
        1  DECCKM                         Cursor Keys Mode                                                         Yes          Yes           No
        2  DECANM                         ANSI/VT52 Mode                                                           No           No            No
        3  DECCOLM                        Column Mode                                                              Yes          Yes           No
        4  DECSCLM                        Scrolling Mode                                                           Yes          Yes           No
        5  DECSCNM                        Screen Mode (light or dark screen)                                       Yes          Yes           No
        6  DECOM                          Origin Mode                                                              Yes          Yes           No
        7  DECAWM                         Auto Wrap Mode                                                           Yes          Yes           Yes
        8  DECARM                         Auto Repeat Mode                                                         Yes          Yes           No
        9  DECINLM                        Interlace Mode / Mouse X10 tracking                                      Yes          Yes           No
       10  DECEDM                         Editing Mode / Show toolbar (rxvt)                                       No           No            No
       11  DECLTM                         Line Transmit Mode                                                       No           No            No
       12  DECKANAM                       Katakana Shift Mode / Blinking cursor (xterm)                            Yes          Yes           Yes
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
       40  DECCRNLM                       Carriage Return/New Line Mode / Allow 80⇒132 mode (xterm)                Yes          Yes           No
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
       67  DECBKM                         Backarrow Key Mode                                                       No           No            No
       68  DECKBUM                        Keyboard Usage Mode                                                      No           No            No
       69  DECVSSM                        Vertical Split Screen Mode / DECLRMM - Left Right Margin Mode            Yes          Yes           No
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
     1007  ALT_SCROLL_XTERM               Enable Alternate Scroll Mode                                             Yes          Yes           Yes
     1010  SCROLL_ON_TTY_OUTPUT_RXVT      Scroll to bottom on tty output                                           No           No            No
     1011  SCROLL_ON_KEYPRESS_RXVT        Scroll to bottom on key press                                            No           No            No
     1014  FAST_SCROLL                    Enable fastScroll resource                                               No           No            No
     1015  MOUSE_URXVT                    Enable urxvt Mouse Mode                                                  Yes          Yes           No
     1016  MOUSE_SGR_PIXELS               Enable SGR Mouse PixelMode                                               Yes          Yes           No
     1021  BOLD_ITALIC_HIGH_INTENSITY     Bold/italic implies high intensity                                       No           No            No
     1034  META_SETS_EIGHTH_BIT           Interpret "meta" key                                                     No           No            No
     1035  MODIFIERS_ALT_NUMLOCK          Enable special modifiers for Alt and NumLock keys                        Yes          Yes           Yes
     1036  META_SENDS_ESC                 Send ESC when Meta modifies a key                                        Yes          Yes           Yes
     1037  KP_DELETE_SENDS_DEL            Send DEL from the editing-keypad Delete key                              No           No            No
     1039  ALT_SENDS_ESC                  Send ESC when Alt modifies a key                                         Yes          Yes           No
     1040  KEEP_SELECTION_NO_HILITE       Keep selection even if not highlighted                                   No           No            No
     1041  USE_CLIPBOARD_SELECTION        Use the CLIPBOARD selection                                              No           No            No
     1042  URGENCY_ON_CTRL_G              Enable Urgency window manager hint when Control-G is received            No           No            No
     1043  RAISE_ON_CTRL_G                Enable raising of the window when Control-G is received                  No           No            No
     1044  REUSE_CLIPBOARD_DATA           Reuse the most recent data copied to CLIPBOARD                           No           No            No
     1045  EXTENDED_REVERSE_WRAPAROUND    Extended Reverse-wraparound mode (XTREVWRAP2)                            Yes          Yes           No
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
     2026  SYNCHRONIZED_OUTPUT            Synchronized Output                                                      Yes          Yes           No
     2027  GRAPHEME_CLUSTERING            Grapheme Clustering                                                      Yes          Yes           Yes
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
   ======  =============================  =======================================================================  ===========  ============  =========

**Summary**: 36 changeable, 121 not changeable.

.. _ghosttyreproduce:

Reproduction
++++++++++++

To reproduce these results for *ghostty*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --save-yaml=linux-ghostty-1.2.3.yaml \
        --limit-codepoints=5000 \
        --limit-words=5000 \
        --limit-errors=1000

.. _ghosttytime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **50.16 seconds** (50s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
