.. _contour:

contour
-------


Tested Software version 0.6.2-master-5b1ad5be on Linux.
The homepage URL of this terminal is https://contour-terminal.org/.
Full results available at ucs-detect_ repository path
`data/contour.yaml <https://github.com/jquast/ucs-detect/blob/master/data/contour.yaml>`_.

.. _contourscores:

Score Breakdown
+++++++++++++++

Detailed breakdown of how scores are calculated for *contour*:

.. table::
   :class: sphinx-datatable

   ===  =====================================  ===========  ====================
     #  Score Type                             Raw Score    Final Scaled Score
   ===  =====================================  ===========  ====================
     1  :ref:`WIDE <contourwide>`              100.00%      100.0%
     2  :ref:`ZWJ <contourzwj>`                96.26%       96.3%
     3  :ref:`LANG <contourlang>`              89.83%       65.9%
     4  :ref:`VS16 <contourvs16>`              50.00%       50.0%
     5  :ref:`VS15 <contourvs15>`              0.00%        0.0%
     6  :ref:`Capabilities <contourdecmodes>`  58.33%       63.6%
     7  :ref:`Graphics <contourgraphics>`      50%          50.0%
     8  :ref:`TIME <contourtime>`              28.04s       73.5%
   ===  =====================================  ===========  ====================

**Score Comparison Plot:**

The following plot shows how this terminal's scores compare to all other terminals tested.

.. figure:: ../_static/plots/contour_scores_scaled.png
   :align: center
   :width: 800px

   Scaled scores comparison across all metrics (normalized 0-100%)

**Final Scaled Score Calculation:**

- Raw Final Score: 64.16%
  (weighted average: WIDE + ZWJ + LANG + VS16 + VS15 + CAP + GFX + 0.5*TIME)
  the categorized 'average' absolute support level of this terminal
  Note: TIME is normalized to 0-1 range before averaging.
  TIME is weighted at 0.5 (half as powerful as other metrics).
  CAP (Capabilities) is the fraction of 7 notable capabilities supported.
  GFX (Graphics) scores 100% for modern protocols (iTerm2, Kitty),
  50% for legacy only (Sixel, ReGIS), 0% for none.
  Sixel/ReGIS support contributes to the GFX score at 50%.

- Final Scaled Score: 50.6%
  (normalized across all terminals tested).
  *Final Scaled scores* are normalized (0-100%) relative to all terminals tested

**WIDE Score Details:**

Wide character support calculation:

- Total successful codepoints: 4844
- Total codepoints tested: 4844
- Formula: 4844 / 4844
- Result: 100.00%

**ZWJ Score Details:**

Emoji ZWJ (Zero-Width Joiner) support calculation:

- Total successful sequences: 1391
- Total sequences tested: 1445
- Formula: 1391 / 1445
- Result: 96.26%

**VS16 Score Details:**

Variation Selector-16 support calculation:

- Errors: 213 of 426 codepoints tested
- Success rate: 50.0%
- Formula: 50.0 / 100
- Result: 50.00%

**VS15 Score Details:**

Variation Selector-15 support calculation:

- Errors: 158 of 158 codepoints tested
- Success rate: 0.0%
- Formula: 0.0 / 100
- Result: 0.00%

**Capabilities Score Details:**

Notable terminal capabilities (7 / 12):

- Set bracketed paste mode (2004): **yes**
- Synchronized Output (2026): **yes**
- Send FocusIn/FocusOut events (1004): **yes**
- Enable SGR Mouse Mode (1006): **yes**
- Grapheme Clustering (2027): **yes**
- Bracketed Paste MIME (5522): **no**
- Kitty Keyboard: **yes**
- XTGETTCAP: **yes**
- Text Sizing (OSC 66): **no**
- Kitty Clipboard Protocol: **no**
- Kitty Pointer Shapes (OSC 22): **no**
- Kitty Notifications (OSC 99): **no**

Raw score: 58.33%

**Graphics Score Details:**

Graphics protocol support (50%):

- Sixel: **yes**
- ReGIS: **no**
- iTerm2: **no**
- Kitty: **no**

Scoring: 100% for modern (iTerm2/Kitty), 50% for legacy only (Sixel/ReGIS), 0% for none

**TIME Score Details:**

Test execution time:

- Elapsed time: 28.04 seconds
- Note: This is a raw measurement; lower is better
- Scaled score uses inverse log10 scaling across all terminals
- Scaled result: 73.5%

**LANG Score Details (Geometric Mean):**

Geometric mean calculation:

- Formula: (p₁ × p₂ × ... × pₙ)^(1/n) where n = 94 languages
- About `geometric mean <https://en.wikipedia.org/wiki/Geometric_mean>`_
- Result: 89.83%

.. _contourwide:

Wide character support
++++++++++++++++++++++

Wide character support of *contour* is **100.0%** (0 errors of 4844 codepoints tested).

.. _contourzwj:

Emoji ZWJ support
+++++++++++++++++

Compatibility of *contour* with the Unicode Emoji ZWJ sequence table is **96.3%** (54 errors of 1445 sequences tested).

Sequence of an Emoji ZWJ Sequence, from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =================================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =================================
     1  `U+0001F3CC <https://codepoints.net/U+0001F3CC>`_  '\\U0001f3cc'  So                  1  GOLFER
     2  `U+0001F3FC <https://codepoints.net/U+0001F3FC>`_  '\\U0001f3fc'  Sk                  2  EMOJI MODIFIER FITZPATRICK TYPE-3
     3  `U+200D <https://codepoints.net/U+200D>`_          '\\u200d'      Cf                  0  ZERO WIDTH JOINER
     4  `U+2642 <https://codepoints.net/U+2642>`_          '\\u2642'      So                  1  MALE SIGN
     5  `U+FE0F <https://codepoints.net/U+FE0F>`_          '\\ufe0f'      Mn                  0  VARIATION SELECTOR-16
   ===  =================================================  =============  ==========  =========  =================================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x9f\x8f\x8c\xf0\x9f\x8f\xbc\xe2\x80\x8d\xe2\x99\x82\xef\xb8\x8f|\\n12|\\n"
        🏌🏼‍♂️|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourvs16:

Variation Selector-16 support
+++++++++++++++++++++++++++++

Emoji VS-16 results for *contour* is 213 errors
out of 426 total codepoints tested, 50.0% success.
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
  while *contour* measures width 1.


.. _contourvs15:

Variation Selector-15 support
+++++++++++++++++++++++++++++

Emoji VS-15 results for *contour* is 158 errors
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
  while *contour* measures width 2.


.. _contourgraphics:

Graphics Protocol Support
+++++++++++++++++++++++++

*contour* supports the following graphics protocols: Sixel_, `iTerm2 inline images`_.

**Detection Methods:**

- **Sixel** and **ReGIS**: Detected via the Device Attributes (DA1) query
  ``CSI c`` (``\x1b[c``). Extension code ``4`` indicates Sixel_ support,
  ``3`` ReGIS_.
- **Kitty graphics**: Detected by sending a Kitty graphics query and
  checking for an ``OK`` response.
- **iTerm2 inline images**: Detected via the iTerm2 capabilities query
  ``OSC 1337 ; Capabilities``.

**Device Attributes Response:**

- Extensions reported: 1, 4, 8, 22, 28, 52, 314
- Sixel_ indicator (``4``): present
- ReGIS_ indicator (``3``): not present

.. _Sixel: https://en.wikipedia.org/wiki/Sixel
.. _ReGIS: https://en.wikipedia.org/wiki/ReGIS
.. _`iTerm2 inline images`: https://iterm2.com/documentation-images.html
.. _`Kitty graphics protocol`: https://sw.kovidgoyal.net/kitty/graphics-protocol/

.. _contourlang:

Language Support
++++++++++++++++

The following 64 languages were tested with 100% success:

Aja, Amarakaeri, Arabic, Standard, Assyrian Neo-Aramaic, Baatonum, Bamun, Belanda Viri, Bora, Catalan (2), Chickasaw, Chinantec, Chiltepec, Dagaare, Southern, Dangme, Dari, Dendi, Dinka, Northeastern, Ditammari, Dzongkha, Evenki, Farsi, Western, Fon, French (Welche), Fur, Ga, Gen, Gilyak, Gumuz, Kabyle, Lamnso', Lingala (tones), Maldivian, Maori (2), Mazahua Central, Mirandese, Mixtec, Metlatónoc, Mòoré, Nanai, Navajo, Orok, Otomi, Mezquital, Panjabi, Western, Pashto, Northern, Picard, Pular (Adlam), Saint Lucian Creole French, Secoya, Seraiki, Shipibo-Conibo, Siona, South Azerbaijani, Tagalog (Tagalog), Tai Dam, Tamazight, Central Atlas, Tem, Tibetan, Central, Ticuna, Uduk, Veps, Vietnamese, Waama, Yaneshaʼ, Yiddish, Eastern, Yoruba, Éwé.

The following 30 languages are not fully supported:

.. table::
   :class: sphinx-datatable

   ========================================================  ==========  =========  =============
   lang                                                        n_errors    n_total  pct_success
   ========================================================  ==========  =========  =============
   :ref:`Sanskrit (Grantha) <contourlangsanskritgrantha>`           219        293  25.3%
   :ref:`Javanese (Javanese) <contourlangjavanesejavanese>`         372        530  29.8%
   :ref:`Tamil <contourlangtamil>`                                  106        175  39.4%
   :ref:`Tamil (Sri Lanka) <contourlangtamilsrilanka>`              106        175  39.4%
   :ref:`Kannada <contourlangkannada>`                              157        287  45.3%
   :ref:`Khmer, Central <contourlangkhmercentral>`                  196        443  55.8%
   :ref:`Sinhala <contourlangsinhala>`                              101        258  60.9%
   :ref:`Bengali <contourlangbengali>`                              145        385  62.3%
   :ref:`Tamang, Eastern <contourlangtamangeastern>`                 26         70  62.9%
   :ref:`Malayalam <contourlangmalayalam>`                          301        845  64.4%
   :ref:`Gujarati <contourlanggujarati>`                            120        343  65.0%
   :ref:`Bhojpuri <contourlangbhojpuri>`                            108        313  65.5%
   :ref:`Panjabi, Eastern <contourlangpanjabieastern>`              103        302  65.9%
   :ref:`Magahi <contourlangmagahi>`                                102        314  67.5%
   :ref:`Marathi <contourlangmarathi>`                              124        391  68.3%
   :ref:`Hindi <contourlanghindi>`                                  121        390  69.0%
   :ref:`Nepali <contourlangnepali>`                                101        352  71.3%
   :ref:`Burmese <contourlangburmese>`                               76        268  71.6%
   :ref:`Maithili <contourlangmaithili>`                            101        357  71.7%
   :ref:`Sanskrit <contourlangsanskrit>`                            138        493  72.0%
   :ref:`Khün <contourlangkhn>`                                      90        396  77.3%
   :ref:`Telugu <contourlangtelugu>`                                 86        384  77.6%
   :ref:`Mon <contourlangmon>`                                       72        332  78.3%
   :ref:`Chakma <contourlangchakma>`                                 47        267  82.4%
   :ref:`Shan <contourlangshan>`                                     18        181  90.1%
   :ref:`Thai <contourlangthai>`                                     14        262  94.7%
   :ref:`Thai (2) <contourlangthai2>`                                11        252  95.6%
   :ref:`Lao <contourlanglao>`                                       10        277  96.4%
   :ref:`Urdu (2) <contourlangurdu2>`                                 1         82  98.8%
   :ref:`Urdu <contourlangurdu>`                                      1        110  99.1%
   ========================================================  ==========  =========  =============

.. _contourlangsanskritgrantha:

Sanskrit (Grantha)
^^^^^^^^^^^^^^^^^^

Sequence of language *Sanskrit (Grantha)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  =====================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  =====================
     1  `U+00011305 <https://codepoints.net/U+00011305>`_  '\\U00011305'  Lo                  1  GRANTHA LETTER A
     2  `U+00011302 <https://codepoints.net/U+00011302>`_  '\\U00011302'  Mc                  0  GRANTHA SIGN ANUSVARA
   ===  =================================================  =============  ==========  =========  =====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x8c\x85\xf0\x91\x8c\x82|\\n12|\\n"
        𑌅𑌂|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangjavanesejavanese:

Javanese (Javanese)
^^^^^^^^^^^^^^^^^^^

Sequence of language *Javanese (Javanese)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ==================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ==================
     1  `U+A9A0 <https://codepoints.net/U+A9A0>`_  '\\ua9a0'  Lo                  1  JAVANESE LETTER TA
     2  `U+A9C0 <https://codepoints.net/U+A9C0>`_  '\\ua9c0'  Mc                  0  JAVANESE PANGKON
     3  `U+A9B1 <https://codepoints.net/U+A9B1>`_  '\\ua9b1'  Lo                  1  JAVANESE LETTER SA
     4  `U+A9C0 <https://codepoints.net/U+A9C0>`_  '\\ua9c0'  Mc                  0  JAVANESE PANGKON
     5  `U+A9AE <https://codepoints.net/U+A9AE>`_  '\\ua9ae'  Lo                  1  JAVANESE LETTER WA
   ===  =========================================  =========  ==========  =========  ==================

Total codepoints: 5


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xea\xa6\xa0\xea\xa7\x80\xea\xa6\xb1\xea\xa7\x80\xea\xa6\xae|\\n12345|\\n"
        ꦠ꧀ꦱ꧀ꦮ|
        12345|

- python `wcwidth.wcswidth()`_ measures width 5,
  while *contour* measures width 3.

.. _contourlangtamil:

Tamil
^^^^^

Sequence of language *Tamil* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
     2  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x95\xe0\xae\xbe|\\n12|\\n"
        கா|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangtamilsrilanka:

Tamil (Sri Lanka)
^^^^^^^^^^^^^^^^^

Sequence of language *Tamil (Sri Lanka)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+0B95 <https://codepoints.net/U+0B95>`_  '\\u0b95'  Lo                  1  TAMIL LETTER KA
     2  `U+0BBE <https://codepoints.net/U+0BBE>`_  '\\u0bbe'  Mc                  0  TAMIL VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xae\x95\xe0\xae\xbe|\\n12|\\n"
        கா|
        12|


.. _contourlangkannada:

Kannada
^^^^^^^

Sequence of language *Kannada* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0C85 <https://codepoints.net/U+0C85>`_  '\\u0c85'  Lo                  1  KANNADA LETTER A
     2  `U+0C82 <https://codepoints.net/U+0C82>`_  '\\u0c82'  Mc                  0  KANNADA SIGN ANUSVARA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb2\x85\xe0\xb2\x82|\\n12|\\n"
        ಅಂ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangkhmercentral:

Khmer, Central
^^^^^^^^^^^^^^

Sequence of language *Khmer, Central* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===================
     1  `U+1780 <https://codepoints.net/U+1780>`_  '\\u1780'  Lo                  1  KHMER LETTER KA
     2  `U+17D2 <https://codepoints.net/U+17D2>`_  '\\u17d2'  Mn                  0  KHMER SIGN COENG
     3  `U+178A <https://codepoints.net/U+178A>`_  '\\u178a'  Lo                  1  KHMER LETTER DA
     4  `U+17C5 <https://codepoints.net/U+17C5>`_  '\\u17c5'  Mc                  0  KHMER VOWEL SIGN AU
   ===  =========================================  =========  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x9e\x80\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9f\x85|\\n123|\\n"
        ក្ដៅ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *contour* measures width 2.

.. _contourlangsinhala:

Sinhala
^^^^^^^

Sequence of language *Sinhala* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================================
     1  `U+0D9A <https://codepoints.net/U+0D9A>`_  '\\u0d9a'  Lo                  1  SINHALA LETTER ALPAPRAANA KAYANNA
     2  `U+0DCF <https://codepoints.net/U+0DCF>`_  '\\u0dcf'  Mc                  0  SINHALA VOWEL SIGN AELA-PILLA
   ===  =========================================  =========  ==========  =========  =================================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb6\x9a\xe0\xb7\x8f|\\n12|\\n"
        කා|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangbengali:

Bengali
^^^^^^^

Sequence of language *Bengali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0985 <https://codepoints.net/U+0985>`_  '\\u0985'  Lo                  1  BENGALI LETTER A
     2  `U+0982 <https://codepoints.net/U+0982>`_  '\\u0982'  Mc                  0  BENGALI SIGN ANUSVARA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa6\x85\xe0\xa6\x82|\\n12|\\n"
        অং|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangtamangeastern:

Tamang, Eastern
^^^^^^^^^^^^^^^

Sequence of language *Tamang, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xbe|\\n12|\\n"
        का|
        12|


.. _contourlangmalayalam:

Malayalam
^^^^^^^^^

Sequence of language *Malayalam* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+0D05 <https://codepoints.net/U+0D05>`_  '\\u0d05'  Lo                  1  MALAYALAM LETTER A
     2  `U+0D02 <https://codepoints.net/U+0D02>`_  '\\u0d02'  Mc                  0  MALAYALAM SIGN ANUSVARA
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb4\x85\xe0\xb4\x82|\\n12|\\n"
        അം|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlanggujarati:

Gujarati
^^^^^^^^

Sequence of language *Gujarati* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =====================
     1  `U+0A95 <https://codepoints.net/U+0A95>`_  '\\u0a95'  Lo                  1  GUJARATI LETTER KA
     2  `U+0A83 <https://codepoints.net/U+0A83>`_  '\\u0a83'  Mc                  0  GUJARATI SIGN VISARGA
   ===  =========================================  =========  ==========  =========  =====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xaa\x95\xe0\xaa\x83|\\n12|\\n"
        કઃ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangbhojpuri:

Bhojpuri
^^^^^^^^

Sequence of language *Bhojpuri* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xbe|\\n12|\\n"
        का|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangpanjabieastern:

Panjabi, Eastern
^^^^^^^^^^^^^^^^

Sequence of language *Panjabi, Eastern* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0A15 <https://codepoints.net/U+0A15>`_  '\\u0a15'  Lo                  1  GURMUKHI LETTER KA
     2  `U+0A3E <https://codepoints.net/U+0A3E>`_  '\\u0a3e'  Mc                  0  GURMUKHI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa8\x95\xe0\xa8\xbe|\\n12|\\n"
        ਕਾ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangmagahi:

Magahi
^^^^^^

Sequence of language *Magahi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xbe|\\n12|\\n"
        का|
        12|


.. _contourlangmarathi:

Marathi
^^^^^^^

Sequence of language *Marathi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xbe|\\n12|\\n"
        का|
        12|


.. _contourlanghindi:

Hindi
^^^^^

Sequence of language *Hindi* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xbe|\\n12|\\n"
        का|
        12|


.. _contourlangnepali:

Nepali
^^^^^^

Sequence of language *Nepali* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xbe|\\n12|\\n"
        का|
        12|


.. _contourlangburmese:

Burmese
^^^^^^^

Sequence of language *Burmese* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+1000 <https://codepoints.net/U+1000>`_  '\\u1000'  Lo                  1  MYANMAR LETTER KA
     2  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x80\xe1\x80\xb1|\\n12|\\n"
        ကေ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangmaithili:

Maithili
^^^^^^^^

Sequence of language *Maithili* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xbe|\\n12|\\n"
        का|
        12|


.. _contourlangsanskrit:

Sanskrit
^^^^^^^^

Sequence of language *Sanskrit* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ========================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ========================
     1  `U+0915 <https://codepoints.net/U+0915>`_  '\\u0915'  Lo                  1  DEVANAGARI LETTER KA
     2  `U+093E <https://codepoints.net/U+093E>`_  '\\u093e'  Mc                  0  DEVANAGARI VOWEL SIGN AA
   ===  =========================================  =========  ==========  =========  ========================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xa4\x95\xe0\xa4\xbe|\\n12|\\n"
        का|
        12|


.. _contourlangkhn:

Khün
^^^^

Sequence of language *Khün* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =======================
     1  `U+1A20 <https://codepoints.net/U+1A20>`_  '\\u1a20'  Lo                  1  TAI THAM LETTER HIGH KA
     2  `U+1A6E <https://codepoints.net/U+1A6E>`_  '\\u1a6e'  Mc                  0  TAI THAM VOWEL SIGN E
     3  `U+1A60 <https://codepoints.net/U+1A60>`_  '\\u1a60'  Mn                  0  TAI THAM SIGN SAKOT
   ===  =========================================  =========  ==========  =========  =======================

Total codepoints: 3


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\xa8\xa0\xe1\xa9\xae\xe1\xa9\xa0|\\n12|\\n"
        ᨠᩮ᩠|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangtelugu:

Telugu
^^^^^^

Sequence of language *Telugu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+0C05 <https://codepoints.net/U+0C05>`_  '\\u0c05'  Lo                  1  TELUGU LETTER A
     2  `U+0C02 <https://codepoints.net/U+0C02>`_  '\\u0c02'  Mc                  0  TELUGU SIGN ANUSVARA
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb0\x85\xe0\xb0\x82|\\n12|\\n"
        అం|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangmon:

Mon
^^^

Sequence of language *Mon* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+1012 <https://codepoints.net/U+1012>`_  '\\u1012'  Lo                  1  MYANMAR LETTER DA
     2  `U+1039 <https://codepoints.net/U+1039>`_  '\\u1039'  Mn                  0  MYANMAR SIGN VIRAMA
     3  `U+1002 <https://codepoints.net/U+1002>`_  '\\u1002'  Lo                  1  MYANMAR LETTER GA
     4  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x92\xe1\x80\xb9\xe1\x80\x82\xe1\x80\xb1|\\n123|\\n"
        ဒ္ဂေ|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *contour* measures width 2.

.. _contourlangchakma:

Chakma
^^^^^^

Sequence of language *Chakma* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =================================================  =============  ==========  =========  ===================
     #  Codepoint                                          Python         Category      wcwidth  Name
   ===  =================================================  =============  ==========  =========  ===================
     1  `U+00011107 <https://codepoints.net/U+00011107>`_  '\\U00011107'  Lo                  1  CHAKMA LETTER KAA
     2  `U+00011133 <https://codepoints.net/U+00011133>`_  '\\U00011133'  Mn                  0  CHAKMA VIRAMA
     3  `U+00011120 <https://codepoints.net/U+00011120>`_  '\\U00011120'  Lo                  1  CHAKMA LETTER YYAA
     4  `U+0001112C <https://codepoints.net/U+0001112C>`_  '\\U0001112c'  Mc                  0  CHAKMA VOWEL SIGN E
   ===  =================================================  =============  ==========  =========  ===================

Total codepoints: 4


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xf0\x91\x84\x87\xf0\x91\x84\xb3\xf0\x91\x84\xa0\xf0\x91\x84\xac|\\n123|\\n"
        𑄇𑄳𑄠𑄬|
        123|

- python `wcwidth.wcswidth()`_ measures width 3,
  while *contour* measures width 2.

.. _contourlangshan:

Shan
^^^^

Sequence of language *Shan* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ====================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ====================
     1  `U+1010 <https://codepoints.net/U+1010>`_  '\\u1010'  Lo                  1  MYANMAR LETTER TA
     2  `U+1031 <https://codepoints.net/U+1031>`_  '\\u1031'  Mc                  0  MYANMAR VOWEL SIGN E
   ===  =========================================  =========  ==========  =========  ====================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe1\x80\x90\xe1\x80\xb1|\\n12|\\n"
        တေ|
        12|


.. _contourlangthai:

Thai
^^^^

Sequence of language *Thai* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
     2  `U+0E33 <https://codepoints.net/U+0E33>`_  '\\u0e33'  Lo                  1  THAI CHARACTER SARA AM
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x81\xe0\xb8\xb3|\\n12|\\n"
        กำ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangthai2:

Thai (2)
^^^^^^^^

Sequence of language *Thai (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ======================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ======================
     1  `U+0E01 <https://codepoints.net/U+0E01>`_  '\\u0e01'  Lo                  1  THAI CHARACTER KO KAI
     2  `U+0E33 <https://codepoints.net/U+0E33>`_  '\\u0e33'  Lo                  1  THAI CHARACTER SARA AM
   ===  =========================================  =========  ==========  =========  ======================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xb8\x81\xe0\xb8\xb3|\\n12|\\n"
        กำ|
        12|


.. _contourlanglao:

Lao
^^^

Sequence of language *Lao* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  =================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  =================
     1  `U+0E81 <https://codepoints.net/U+0E81>`_  '\\u0e81'  Lo                  1  LAO LETTER KO
     2  `U+0EB3 <https://codepoints.net/U+0EB3>`_  '\\u0eb3'  Lo                  1  LAO VOWEL SIGN AM
   ===  =========================================  =========  ==========  =========  =================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xe0\xba\x81\xe0\xba\xb3|\\n12|\\n"
        ກຳ|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourlangurdu2:

Urdu (2)
^^^^^^^^

Sequence of language *Urdu (2)* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+0601 <https://codepoints.net/U+0601>`_  '\\u0601'  Cf                  1  ARABIC SIGN SANAH
     2  `U+06F1 <https://codepoints.net/U+06F1>`_  '\\u06f1'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT ONE
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\x81\xdb\xb1|\\n12|\\n"
        ؁۱|
        12|


.. _contourlangurdu:

Urdu
^^^^

Sequence of language *Urdu* from midpoint of alignment failure records:

.. table::
   :class: sphinx-datatable

   ===  =========================================  =========  ==========  =========  ===============================
     #  Codepoint                                  Python     Category      wcwidth  Name
   ===  =========================================  =========  ==========  =========  ===============================
     1  `U+0601 <https://codepoints.net/U+0601>`_  '\\u0601'  Cf                  1  ARABIC SIGN SANAH
     2  `U+06F1 <https://codepoints.net/U+06F1>`_  '\\u06f1'  Nd                  1  EXTENDED ARABIC-INDIC DIGIT ONE
   ===  =========================================  =========  ==========  =========  ===============================

Total codepoints: 2


- Shell test using `printf(1)`_, ``'|'`` should align in output::

        $ printf "\xd8\x81\xdb\xb1|\\n12|\\n"
        ؁۱|
        12|

- python `wcwidth.wcswidth()`_ measures width 2,
  while *contour* measures width 1.

.. _contourdecmodes:

DEC Private Modes Support
+++++++++++++++++++++++++

DEC private modes results for *contour*: 5 changeable modes
of 5 supported out of 7 total modes tested (71.4% support, 71.4% changeable).

Complete list of DEC private modes tested:

.. table::
   :class: sphinx-datatable

   ======  =====================  ===================================  ===========  ============  =========
     Mode  Name                   Description                          Supported    Changeable    Enabled
   ======  =====================  ===================================  ===========  ============  =========
     1004  FOCUS_IN_OUT_EVENTS    Send FocusIn/FocusOut events         Yes          Yes           No
     1006  MOUSE_EXTENDED_SGR     Enable SGR Mouse Mode                Yes          Yes           No
     2004  BRACKETED_PASTE        Set bracketed paste mode             Yes          Yes           No
     2026  SYNCHRONIZED_OUTPUT    Synchronized Output                  Yes          Yes           No
     2027  GRAPHEME_CLUSTERING    Grapheme Clustering                  Yes          Yes           Yes
     2048  IN_BAND_WINDOW_RESIZE  In-Band Window Resize Notifications  No           No            No
     5522  BRACKETED_PASTE_MIME   Bracketed Paste MIME                 No           No            No
   ======  =====================  ===================================  ===========  ============  =========

**Summary**: 5 changeable, 2 not changeable.

.. _contourkittykbd:

Kitty Keyboard Protocol
+++++++++++++++++++++++

*contour* supports the `Kitty keyboard protocol`_.

.. table::
   :class: sphinx-datatable

   ===  ===============================  =====================  =======
     #  Flag                             Key                    State
   ===  ===============================  =====================  =======
     1  Disambiguate escape codes        ``disambiguate``       No
     2  Report event types               ``report_events``      No
     3  Report alternate keys            ``report_alternates``  No
     4  Report all keys as escape codes  ``report_all_keys``    No
     5  Report associated text           ``report_text``        No
   ===  ===============================  =====================  =======

Detection is performed by sending ``CSI ? u`` to query the current
progressive enhancement flags. A terminal that supports this protocol
responds with the active flags value.

.. _`Kitty keyboard protocol`: https://sw.kovidgoyal.net/kitty/keyboard-protocol/

.. _contourxtgettcap:

XTGETTCAP (Terminfo Capabilities)
+++++++++++++++++++++++++++++++++

*contour* supports the ``XTGETTCAP`` sequence and reports **58** terminfo capabilities.

.. table::
   :class: sphinx-datatable

   ===  ============  ======================  ==================
     #  Capability    Description             Value
   ===  ============  ======================  ==================
     1  Co            Number of colors        *(empty)*
     2  TN            Terminal name           ``xterm-256color``
     3  bel           Bell                    ``^G``
     4  bold          Enter bold mode         ``[1m``
     5  civis         Hide cursor             ``[?25l``
     6  clear         Clear screen            ``[H[2J``
     7  cnorm         Normal cursor           ``[?12l[?25h``
     8  colors        Max colors              *(empty)*
     9  cr            Carriage return         ``^M``
    10  csr           Change scroll region    ``[%i%p1%d;%p2%dr``
    11  cub           Cursor left n           ``[%p1%dD``
    12  cub1          Cursor left             ``^H``
    13  cud           Cursor down n           ``[%p1%dB``
    14  cud1          Cursor down             ``^J``
    15  cuf           Cursor right n          ``[%p1%dC``
    16  cuf1          Cursor right            ``[C``
    17  cup           Cursor address          ``[%i%p1%d;%p2%dH``
    18  cuu           Cursor up n             ``[%p1%dA``
    19  cuu1          Cursor up               ``[A``
    20  cvvis         Very visible cursor     ``[?12;25h``
    21  dch           Delete n characters     ``[%p1%dP``
    22  dch1          Delete character        ``[P``
    23  dim           Enter dim mode          ``[2m``
    24  dl            Delete n lines          ``[%p1%dM``
    25  dl1           Delete line             ``[M``
    26  ech           Erase characters        ``[%p1%dX``
    27  ed            Clear to end of screen  ``[J``
    28  el            Clear to end of line    ``[K``
    29  el1           Clear to start of line  ``[1K``
    30  flash         Flash screen            ``[?5h$<100/>[?5l``
    31  home          Cursor home             ``[H``
    32  hpa           Horizontal position     ``[%i%p1%dG``
    33  ich           Insert n characters     ``[%p1%d@``
    34  il            Insert n lines          ``[%p1%dL``
    35  il1           Insert line             ``[L``
    36  ind           Scroll forward          ``^J``
    37  indn          Scroll forward n        ``[%p1%dS``
    38  op            Original pair           ``[39;49m``
    39  rc            Restore cursor          ``8``
    40  rev           Enter reverse mode      ``[7m``
    41  rin           Scroll reverse n        ``[%p1%dT``
    42  ritm          Exit italics mode       ``[23m``
    43  rmam          Disable line wrap       ``[?7l``
    44  rmcup         Exit alt screen         ``[?1049l``
    45  rmkx          Keypad local mode       ``[?1l``
    46  rmso          Exit standout mode      ``[27m``
    47  rmul          Exit underline mode     ``[24m``
    48  sc            Save cursor             ``7``
    49  setab         Set background color    ``[%?%p1%{8}%<%t4%p1%d%e%p1%{16}%<%t10%p1%{8}%-%d%e48;5;%p...``
    50  setaf         Set foreground color    ``[%?%p1%{8}%<%t3%p1%d%e%p1%{16}%<%t9%p1%{8}%-%d%e38;5;%p1...``
    51  sgr0          Reset attributes        ``(B[m``
    52  sitm          Enter italics mode      ``[3m``
    53  smam          Enable line wrap        ``[?7h``
    54  smcup         Enter alt screen        ``[?1049h``
    55  smkx          Keypad transmit mode    ``[?1h``
    56  smso          Enter standout mode     ``[7m``
    57  smul          Enter underline mode    ``[4m``
    58  vpa           Vertical position       ``[%i%p1%dd``
   ===  ============  ======================  ==================

The ``XTGETTCAP`` sequence (``DCS + q Pt ST``) allows applications to query
terminfo capabilities directly from the terminal emulator, rather than relying
on the system terminfo database.

.. _contourreproduce:

Reproduction
++++++++++++

To reproduce these results for *contour*, install and run ucs-detect_
with the following commands::

    pip install ucs-detect
    ucs-detect --rerun data/contour.yaml

.. _contourtime:

Test Execution Time
+++++++++++++++++++

The test suite completed in **28.04 seconds** (28s).

This time measurement represents the total duration of the test execution,
including all Unicode wide character tests, emoji ZWJ sequences, variation
selectors, language support checks, and DEC mode detection.

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
