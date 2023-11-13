.. _Konsole:

Konsole
+++++++


Tested Software version 23.08.1 on Linux
Full results available at ucs-detect_ repository path
`data/linux-konsole-23.08.1.yaml <https://github.com/jquast/ucs-detect/blob/master/data/linux-konsole-23.08.1.yaml>`_

.. _Konsolewide:

Wide character support
^^^^^^^^^^^^^^^^^^^^^^

The best wide unicode table version for Konsole appears to be 
**15.0.0**, this is from a summary of the following
results:


=========  ==========  =========  =============
version      n_errors    n_total  pct_success
=========  ==========  =========  =============
'5.1.0'             0         26  100.0%
'5.2.0'            79        269  70.6%
'6.0.0'             0         13  100.0%
'9.0.0'             6       5000  99.9%
'10.0.0'           22        735  97.0%
'11.0.0'            1         62  98.4%
'12.0.0'            1         62  98.4%
'12.1.0'            0          1  100.0%
'13.0.0'           16        541  97.0%
'14.0.0'            1         41  97.6%
'15.0.0'            0         15  100.0%
'15.1.0'            5          5  0.0%
=========  ==========  =========  =============

Sequence of a WIDE character from Unicode Version 15.1.0, from midpoint of alignment failure records:

=========================================  =========  ==========  =========  ======
Codepoint                                  Python     Category      wcwidth  Name
=========================================  =========  ==========  =========  ======
`U+2FFE <https://codepoints.net/U+2FFE>`_  '\\u2ffe'  Cn                  2  na
=========================================  =========  ==========  =========  ======

None

- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe2\xbf\xbe|\\n12|\\n"
        ⿾|
        12|

- python `wcwidth.wcswidth()`_ measures width {fail_record['measured_by_wcwidth']}, 
  while *Konsole* measures width {fail_record['measured_by_terminal']}.

.. _Konsolezwj:

Emoji ZWJ support
^^^^^^^^^^^^^^^^^

The best Emoji ZWJ table version for *Konsole* appears to be 
**15.1**, this is from a summary of the following
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
=========  ==========  =========  =============

.. _Konsolevs16:

Variation Selector-16 support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Emoji VS-16 results for *Konsole* is 0 errors
out of 100 total codepoints tested, 100.0% success.
All codepoint combinations with Variation Selector-16 tested were successful.

.. _Konsolelang:

Language Support
^^^^^^^^^^^^^^^^

The following 107 languages were tested with 100% success:

(Bizisa), (Yeonbyeon), Achuar-Shiwiar (1), Adyghe, Aja, Amarakaeri, Arabic, Standard, Assyrian Neo-Aramaic, Azerbaijani, North (Latin), Baatonum, Bamun, Belarusan, Bora, Bulgarian, Cashinahua, Cherokee (cased), Chickasaw, Chinantec, Chiltepec, Chinese, Yue, Cree, Swampy, Crimean Tatar, Crioulo, Upper Guinea (008), Dagaare, Southern, Dangme, Dari, Dendi, Dinka, Northeastern, Ditammari, Dzongkha, Evenki, Farsi, Western, Fon, Fur, Ga, Garifuna, Gen, Gilyak, Greek (polytonic), Gumuz, Hausa, Hmong Njua, Hmong, Northern Qiandong, Icelandic, Idoma, Kabardian, Ladino, Lamnso', Lao, Latin (1), Lingala (tones), Maldivian, Mazahua Central, Mixtec, Metlatónoc, Mongolian, Halh (Mongolian), Montenegrin, Mòoré, Nanai, Navajo, Nuosu, Orok, Otomi, Mezquital, Panjabi, Western, Pashto, Northern, Picard, Pijin, Pular, Pular (Adlam), Purepecha, Quechua, Ayacucho, Quechua, Cajamarca, Quechua, Cusco, Romansch (Surmiran), Rundi, Secoya, Seraiki, Serer-Sine, Seselwa Creole French, Siona, Sorbian, Upper, South Azerbaijani, Sukuma, Swati, Tagalog (Tagalog), Tai Dam, Tamazight, Central Atlas, Tamazight, Central Atlas (Tifinagh), Tamazight, Standard Morocan, Tem, Thai, Thai (2), Tibetan, Central, Ticuna, Uduk, Urdu, Urdu (2), Uzbek, Northern (Cyrillic), Vai, Veps, Vietnamese, Vietnamese (Han nom), Waama, Walloon, Yaneshaʼ, Yiddish, Eastern, Yoruba, Yukaghir, Northern, Éwé.

The following 25 languages are not fully supported:

===================  ==========  =========  =============
lang                   n_errors    n_total    pct_success
===================  ==========  =========  =============
Javanese (Javanese)         248        256        3.125
Tamil (Sri Lanka)           500        539        7.23562
Tamil                       500        540        7.40741
Sanskrit (Grantha)          500        565       11.5044
Khmer, Central              448        528       15.1515
Bengali                     500        593       15.683
Malayalam                   500        596       16.1074
Kannada                     500        604       17.2185
Khün                        354        442       19.9095
Sanskrit                    500        680       26.4706
Tamang, Eastern              33         45       26.6667
Nepali                      500        701       28.6733
Marathi                     500        703       28.8762
Burmese                     500        719       30.459
Gujarati                    500        756       33.8624
Hindi                       500        774       35.4005
Telugu                      500        791       36.7889
Maithili                    500        795       37.1069
Mon                         500        809       38.1953
Shan                        500        854       41.452
Panjabi, Eastern            500        860       41.8605
Sinhala                     500        948       47.2574
Bhojpuri                    500       1020       50.9804
Magahi                      500       1080       53.7037
Chakma                      493       1444       65.8587
===================  ==========  =========  =============

Javanese (Javanese)
