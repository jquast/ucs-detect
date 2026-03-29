Results
=======

This is a volunteer-maintained analysis created by and for terminal emulator and
TUI/CLI library developers.

We welcome productive contributions and corrections to improve the accuracy and
completeness of these measurements.

.. note::

   These test results are provided as-is and we do not guarantee their correctness.
   The scores and ratings presented here are objective measurements of Unicode and
   terminal feature support by analysis of automatic response, and should not be
   interpreted as an overall assessment of terminal emulator quality or a
   recommendation. Many factors beyond Unicode support contribute to terminal quality.
   Some terminals may optionally support features and modes not represented here.
   This data represents only automatic responses received when launched in their
   default configurations and packaged build options. Some languages and emoji
   tests may also pass 'accidentally'!

General Tabulated Summary
-------------------------

.. Generate custom roles for score coloring

.. role:: score-0
   :class: score-0

.. role:: score-1
   :class: score-1

.. role:: score-2
   :class: score-2

.. role:: score-3
   :class: score-3

.. role:: score-4
   :class: score-4

.. role:: score-5
   :class: score-5

.. role:: score-6
   :class: score-6

.. role:: score-7
   :class: score-7

.. role:: score-8
   :class: score-8

.. role:: score-9
   :class: score-9

.. role:: score-10
   :class: score-10

.. role:: score-11
   :class: score-11

.. role:: score-12
   :class: score-12

.. role:: score-13
   :class: score-13

.. role:: score-14
   :class: score-14

.. role:: score-15
   :class: score-15

.. role:: score-16
   :class: score-16

.. role:: score-17
   :class: score-17

.. role:: score-18
   :class: score-18

.. role:: score-19
   :class: score-19

.. role:: score-20
   :class: score-20

.. role:: score-21
   :class: score-21

.. role:: score-22
   :class: score-22

.. role:: score-23
   :class: score-23

.. role:: score-24
   :class: score-24

.. role:: score-25
   :class: score-25

.. role:: score-26
   :class: score-26

.. role:: score-27
   :class: score-27

.. role:: score-28
   :class: score-28

.. role:: score-29
   :class: score-29

.. role:: score-30
   :class: score-30

.. role:: score-31
   :class: score-31

.. role:: score-32
   :class: score-32

.. role:: score-33
   :class: score-33

.. role:: score-34
   :class: score-34

.. role:: score-35
   :class: score-35

.. role:: score-36
   :class: score-36

.. role:: score-37
   :class: score-37

.. role:: score-38
   :class: score-38

.. role:: score-39
   :class: score-39

.. role:: score-40
   :class: score-40

.. role:: score-41
   :class: score-41

.. role:: score-42
   :class: score-42

.. role:: score-43
   :class: score-43

.. role:: score-44
   :class: score-44

.. role:: score-45
   :class: score-45

.. role:: score-46
   :class: score-46

.. role:: score-47
   :class: score-47

.. role:: score-48
   :class: score-48

.. role:: score-49
   :class: score-49

.. role:: score-50
   :class: score-50

.. role:: score-51
   :class: score-51

.. role:: score-52
   :class: score-52

.. role:: score-53
   :class: score-53

.. role:: score-54
   :class: score-54

.. role:: score-55
   :class: score-55

.. role:: score-56
   :class: score-56

.. role:: score-57
   :class: score-57

.. role:: score-58
   :class: score-58

.. role:: score-59
   :class: score-59

.. role:: score-60
   :class: score-60

.. role:: score-61
   :class: score-61

.. role:: score-62
   :class: score-62

.. role:: score-63
   :class: score-63

.. role:: score-64
   :class: score-64

.. role:: score-65
   :class: score-65

.. role:: score-66
   :class: score-66

.. role:: score-67
   :class: score-67

.. role:: score-68
   :class: score-68

.. role:: score-69
   :class: score-69

.. role:: score-70
   :class: score-70

.. role:: score-71
   :class: score-71

.. role:: score-72
   :class: score-72

.. role:: score-73
   :class: score-73

.. role:: score-74
   :class: score-74

.. role:: score-75
   :class: score-75

.. role:: score-76
   :class: score-76

.. role:: score-77
   :class: score-77

.. role:: score-78
   :class: score-78

.. role:: score-79
   :class: score-79

.. role:: score-80
   :class: score-80

.. role:: score-81
   :class: score-81

.. role:: score-82
   :class: score-82

.. role:: score-83
   :class: score-83

.. role:: score-84
   :class: score-84

.. role:: score-85
   :class: score-85

.. role:: score-86
   :class: score-86

.. role:: score-87
   :class: score-87

.. role:: score-88
   :class: score-88

.. role:: score-89
   :class: score-89

.. role:: score-90
   :class: score-90

.. role:: score-91
   :class: score-91

.. role:: score-92
   :class: score-92

.. role:: score-93
   :class: score-93

.. role:: score-94
   :class: score-94

.. role:: score-95
   :class: score-95

.. role:: score-96
   :class: score-96

.. role:: score-97
   :class: score-97

.. role:: score-98
   :class: score-98

.. role:: score-99
   :class: score-99

.. role:: score-100
   :class: score-100

.. role:: score-na
   :class: score-na

.. role:: score-contested
   :class: score-contested

.. table::
   :class: sphinx-datatable

   ======  =======================================  ==================  ===========  ====================================  ==================================  =================================  ================================  ====================================  ========================================  ======================================  ======================================  =====================================  ====================================  =================================================
     Rank  Terminal Software                        Software Version    OS System    Score                                 WIDE                                LANG                               ZWJ                               VS16                                  VS15                                      SRI                                     SFZ                                     RI                                     Capabilities                          Graphics
   ======  =======================================  ==================  ===========  ====================================  ==================================  =================================  ================================  ====================================  ========================================  ======================================  ======================================  =====================================  ====================================  =================================================
        1  :ref:`ghostty <ghostty>`                 1.3.2…              Linux        :sref:`100 <ghosttyscores> 100`       :sref:`100 <ghosttywide> 100`       :sref:`97 <ghosttylang> 97`        :sref:`100 <ghosttyzwj> 100`      :sref:`100 <ghosttyvs16> 100`         :sref:`100 <ghosttyvs15> contested`       :sref:`100 <ghosttysri> 100`            :sref:`100 <ghosttysfz> 100`            :sref:`100 <ghosttyri> 100`            :sref:`7 <ghosttydecmodes> 88`        :sref:`Kitty <ghosttygraphics> 100`
        2  :ref:`Konsole <konsole>`                 25.12.3             Linux        :sref:`87 <konsolescores> 87`         :sref:`62 <konsolewide> 62`         :sref:`92 <konsolelang> 92`        :sref:`96 <konsolezwj> 96`        :sref:`100 <konsolevs16> 100`         :sref:`0 <konsolevs15> contested`         :sref:`100 <konsolesri> 100`            :sref:`100 <konsolesfz> 100`            :sref:`100 <konsoleri> 100`            :sref:`0 <konsoledecmodes> 0`         :sref:`Sixel, Kitty <konsolegraphics> 100`
        3  :ref:`iTerm2 <iterm2>`                   3.6.6               Darwin       :sref:`84 <iterm2scores> 84`          :sref:`93 <iterm2wide> 93`          :sref:`88 <iterm2lang> 88`         :sref:`99 <iterm2zwj> 99`         :sref:`97 <iterm2vs16> 97`            :sref:`0 <iterm2vs15> contested`          :sref:`N/A <iterm2sri> contested`       :sref:`N/A <iterm2sfz> contested`       :sref:`N/A <iterm2ri> contested`       :sref:`8 <iterm2decmodes> 100`        :sref:`Sixel, iTerm2, Kitty <iterm2graphics> 100`
        4  :ref:`contour <contour>`                 0.6.3…              Linux        :sref:`78 <contourscores> 78`         :sref:`100 <contourwide> 100`       :sref:`66 <contourlang> 66`        :sref:`96 <contourzwj> 96`        :sref:`50 <contourvs16> 50`           :sref:`0 <contourvs15> contested`         :sref:`100 <contoursri> 100`            :sref:`100 <contoursfz> 100`            :sref:`100 <contourri> 100`            :sref:`7 <contourdecmodes> 88`        :sref:`Sixel <contourgraphics> 50`
        5  :ref:`kitty <kitty>`                     0.46.2              Linux        :sref:`76 <kittyscores> 76`           :sref:`100 <kittywide> 100`         :sref:`41 <kittylang> 41`          :sref:`100 <kittyzwj> 100`        :sref:`98 <kittyvs16> 98`             :sref:`100 <kittyvs15> contested`         :sref:`100 <kittysri> 100`              :sref:`0 <kittysfz> 0`                  :sref:`100 <kittyri> 100`              :sref:`7 <kittydecmodes> 88`          :sref:`Kitty <kittygraphics> 100`
        6  :ref:`tmux <tmux>`                       3.4                 Linux        :sref:`74 <tmuxscores> 74`            :sref:`53 <tmuxwide> 53`            :sref:`92 <tmuxlang> 92`           :sref:`81 <tmuxzwj> 81`           :sref:`98 <tmuxvs16> 98`              :sref:`0 <tmuxvs15> contested`            :sref:`100 <tmuxsri> 100`               :sref:`100 <tmuxsfz> 100`               :sref:`100 <tmuxri> 100`               :sref:`0 <tmuxdecmodes> 0`            :sref:`Sixel <tmuxgraphics> 50`
        7  :ref:`Terminal.exe <terminalexe>`        1.23.260121001      Windows      :sref:`67 <terminalexescores> 67`     :sref:`87 <terminalexewide> 87`     :sref:`100 <terminalexelang> 100`  :sref:`100 <terminalexezwj> 100`  :sref:`100 <terminalexevs16> 100`     :sref:`0 <terminalexevs15> contested`     :sref:`N/A <terminalexesri> contested`  :sref:`N/A <terminalexesfz> contested`  :sref:`N/A <terminalexeri> contested`  :sref:`5 <terminalexedecmodes> 62`    :sref:`Sixel <terminalexegraphics> 50`
        8  :ref:`WezTerm <wezterm>`                 20260117…           Linux        :sref:`63 <weztermscores> 63`         :sref:`87 <weztermwide> 87`         :sref:`67 <weztermlang> 67`        :sref:`100 <weztermzwj> 100`      :sref:`50 <weztermvs16> 50`           :sref:`0 <weztermvs15> contested`         :sref:`0 <weztermsri> 0`                :sref:`100 <weztermsfz> 100`            :sref:`100 <weztermri> 100`            :sref:`6 <weztermdecmodes> 75`        :sref:`Sixel, Kitty <weztermgraphics> 100`
        9  :ref:`mintty <mintty>`                   3.8.1               Windows      :sref:`62 <minttyscores> 62`          :sref:`93 <minttywide> 93`          :sref:`92 <minttylang> 92`         :sref:`100 <minttyzwj> 100`       :sref:`100 <minttyvs16> 100`          :sref:`0 <minttyvs15> contested`          :sref:`N/A <minttysri> contested`       :sref:`N/A <minttysfz> contested`       :sref:`N/A <minttyri> contested`       :sref:`4 <minttydecmodes> 50`         :sref:`Sixel <minttygraphics> 50`
       10  :ref:`foot <foot>`                       1.16.2              Linux        :sref:`47 <footscores> 47`            :sref:`44 <footwide> 44`            :sref:`100 <footlang> 100`         :sref:`96 <footzwj> 96`           :sref:`100 <footvs16> 100`            :sref:`0 <footvs15> contested`            :sref:`0 <footsri> 0`                   :sref:`0 <footsfz> 0`                   :sref:`100 <footri> 100`               :sref:`7 <footdecmodes> 88`           :sref:`Sixel <footgraphics> 50`
       11  :ref:`Rio <rio>`                         0.2.37              Linux        :sref:`35 <rioscores> 35`             :sref:`87 <riowide> 87`             :sref:`92 <riolang> 92`            :sref:`1 <riozwj> 1`              :sref:`50 <riovs16> 50`               :sref:`0 <riovs15> contested`             :sref:`0 <riosri> 0`                    :sref:`100 <riosfz> 100`                :sref:`100 <riori> 100`                :sref:`6 <riodecmodes> 75`            :sref:`Sixel <riographics> 50`
       12  :ref:`mlterm <mlterm>`                   3.9.4               Linux        :sref:`32 <mltermscores> 32`          :sref:`37 <mltermwide> 37`          :sref:`65 <mltermlang> 65`         :sref:`0 <mltermzwj> 0`           :sref:`50 <mltermvs16> 50`            :sref:`0 <mltermvs15> contested`          :sref:`0 <mltermsri> 0`                 :sref:`100 <mltermsfz> 100`             :sref:`99 <mltermri> 99`               :sref:`4 <mltermdecmodes> 50`         :sref:`Sixel, ReGIS <mltermgraphics> 50`
       13  :ref:`tabby <tabby>`                     1.0.230             Linux        :sref:`29 <tabbyscores> 29`           :sref:`4 <tabbywide> 4`             :sref:`92 <tabbylang> 92`          :sref:`1 <tabbyzwj> 1`            :sref:`50 <tabbyvs16> 50`             :sref:`0 <tabbyvs15> contested`           :sref:`0 <tabbysri> 0`                  :sref:`100 <tabbysfz> 100`              :sref:`100 <tabbyri> 100`              :sref:`3 <tabbydecmodes> 38`          :sref:`Sixel <tabbygraphics> 50`
       14  :ref:`alacritty <alacritty>`             0.16.1              Linux        :sref:`26 <alacrittyscores> 26`       :sref:`100 <alacrittywide> 100`     :sref:`88 <alacrittylang> 88`      :sref:`1 <alacrittyzwj> 1`        :sref:`50 <alacrittyvs16> 50`         :sref:`0 <alacrittyvs15> contested`       :sref:`0 <alacrittysri> 0`              :sref:`100 <alacrittysfz> 100`          :sref:`100 <alacrittyri> 100`          :sref:`5 <alacrittydecmodes> 62`      :sref:`none <alacrittygraphics> 0`
       15  :ref:`XTerm <xterm>`                     406                 Linux        :sref:`25 <xtermscores> 25`           :sref:`37 <xtermwide> 37`           :sref:`92 <xtermlang> 92`          :sref:`1 <xtermzwj> 1`            :sref:`50 <xtermvs16> 50`             :sref:`0 <xtermvs15> contested`           :sref:`0 <xtermsri> 0`                  :sref:`100 <xtermsfz> 100`              :sref:`100 <xtermri> 100`              :sref:`4 <xtermdecmodes> 50`          :sref:`none <xtermgraphics> 0`
       16  :ref:`Bobcat <bobcat>`                   0.9.9 (r377)        Linux        :sref:`24 <bobcatscores> 24`          :sref:`97 <bobcatwide> 97`          :sref:`92 <bobcatlang> 92`         :sref:`0 <bobcatzwj> 0`           :sref:`100 <bobcatvs16> 100`          :sref:`0 <bobcatvs15> contested`          :sref:`100 <bobcatsri> 100`             :sref:`0 <bobcatsfz> 0`                 :sref:`1 <bobcatri> 1`                 :sref:`5 <bobcatdecmodes> 62`         :sref:`Sixel <bobcatgraphics> 50`
       17  :ref:`libvterm <libvterm>`               0.3                 Linux        :sref:`21 <libvtermscores> 21`        :sref:`46 <libvtermwide> 46`        :sref:`91 <libvtermlang> 91`       :sref:`0 <libvtermzwj> 0`         :sref:`50 <libvtermvs16> 50`          :sref:`0 <libvtermvs15> contested`        :sref:`100 <libvtermsri> 100`           :sref:`100 <libvtermsfz> 100`           :sref:`0 <libvtermri> 0`               :sref:`4 <libvtermdecmodes> 50`       :sref:`none <libvtermgraphics> 0`
       18  :ref:`rxvt-unicode <rxvtunicode>`        9.31                Linux        :sref:`21 <rxvtunicodescores> 21`     :sref:`46 <rxvtunicodewide> 46`     :sref:`92 <rxvtunicodelang> 92`    :sref:`1 <rxvtunicodezwj> 1`      :sref:`50 <rxvtunicodevs16> 50`       :sref:`0 <rxvtunicodevs15> contested`     :sref:`0 <rxvtunicodesri> 0`            :sref:`100 <rxvtunicodesfz> 100`        :sref:`100 <rxvtunicoderi> 100`        :sref:`3 <rxvtunicodedecmodes> 38`    :sref:`none <rxvtunicodegraphics> 0`
       19  :ref:`termit <termit>`                   3.1(VTE/8400)       Linux        :sref:`20 <termitscores> 20`          :sref:`41 <termitwide> 41`          :sref:`92 <termitlang> 92`         :sref:`1 <termitzwj> 1`           :sref:`50 <termitvs16> 50`            :sref:`0 <termitvs15> contested`          :sref:`0 <termitsri> 0`                 :sref:`100 <termitsfz> 100`             :sref:`100 <termitri> 100`             :sref:`6 <termitdecmodes> 75`         :sref:`none <termitgraphics> 0`
       20  :ref:`xfce4-terminal <xfce4terminal>`    1.1.3(VTE/8400)     Linux        :sref:`20 <xfce4terminalscores> 20`   :sref:`41 <xfce4terminalwide> 41`   :sref:`92 <xfce4terminallang> 92`  :sref:`1 <xfce4terminalzwj> 1`    :sref:`50 <xfce4terminalvs16> 50`     :sref:`0 <xfce4terminalvs15> contested`   :sref:`0 <xfce4terminalsri> 0`          :sref:`100 <xfce4terminalsfz> 100`      :sref:`100 <xfce4terminalri> 100`      :sref:`6 <xfce4terminaldecmodes> 75`  :sref:`none <xfce4terminalgraphics> 0`
       21  :ref:`xterm.js <xtermjs>`                6.1.0…              Linux        :sref:`19 <xtermjsscores> 19`         :sref:`4 <xtermjswide> 4`           :sref:`92 <xtermjslang> 92`        :sref:`1 <xtermjszwj> 1`          :sref:`50 <xtermjsvs16> 50`           :sref:`0 <xtermjsvs15> contested`         :sref:`0 <xtermjssri> 0`                :sref:`100 <xtermjssfz> 100`            :sref:`100 <xtermjsri> 100`            :sref:`5 <xtermjsdecmodes> 62`        :sref:`none <xtermjsgraphics> 0`
       22  :ref:`weston-terminal <westonterminal>`  13.0.0              Linux        :sref:`18 <westonterminalscores> 18`  :sref:`46 <westonterminalwide> 46`  :sref:`0 <westonterminallang> 0`   :sref:`0 <westonterminalzwj> 0`   :sref:`100 <westonterminalvs16> 100`  :sref:`0 <westonterminalvs15> contested`  :sref:`0 <westonterminalsri> 0`         :sref:`100 <westonterminalsfz> 100`     :sref:`99 <westonterminalri> 99`       :sref:`0 <westonterminaldecmodes> 0`  :sref:`none <westonterminalgraphics> 0`
       23  :ref:`GNOME Terminal <gnometerminal>`    3.52.0(VTE/8400)    Linux        :sref:`17 <gnometerminalscores> 17`   :sref:`41 <gnometerminalwide> 41`   :sref:`89 <gnometerminallang> 89`  :sref:`1 <gnometerminalzwj> 1`    :sref:`50 <gnometerminalvs16> 50`     :sref:`0 <gnometerminalvs15> contested`   :sref:`0 <gnometerminalsri> 0`          :sref:`100 <gnometerminalsfz> 100`      :sref:`100 <gnometerminalri> 100`      :sref:`6 <gnometerminaldecmodes> 75`  :sref:`none <gnometerminalgraphics> 0`
       24  :ref:`terminator <terminator>`           2.1.3(VTE/8400)     Linux        :sref:`17 <terminatorscores> 17`      :sref:`41 <terminatorwide> 41`      :sref:`89 <terminatorlang> 89`     :sref:`1 <terminatorzwj> 1`       :sref:`50 <terminatorvs16> 50`        :sref:`0 <terminatorvs15> contested`      :sref:`0 <terminatorsri> 0`             :sref:`100 <terminatorsfz> 100`         :sref:`100 <terminatorri> 100`         :sref:`6 <terminatordecmodes> 75`     :sref:`none <terminatorgraphics> 0`
       25  :ref:`LXTerminal <lxterminal>`           0.4.0(VTE/7600)     Linux        :sref:`15 <lxterminalscores> 15`      :sref:`37 <lxterminalwide> 37`      :sref:`92 <lxterminallang> 92`     :sref:`1 <lxterminalzwj> 1`       :sref:`50 <lxterminalvs16> 50`        :sref:`0 <lxterminalvs15> contested`      :sref:`0 <lxterminalsri> 0`             :sref:`100 <lxterminalsfz> 100`         :sref:`100 <lxterminalri> 100`         :sref:`4 <lxterminaldecmodes> 50`     :sref:`none <lxterminalgraphics> 0`
       26  :ref:`st <st>`                           0.9                 Linux        :sref:`15 <stscores> 15`              :sref:`46 <stwide> 46`              :sref:`92 <stlang> 92`             :sref:`1 <stzwj> 1`               :sref:`50 <stvs16> 50`                :sref:`0 <stvs15> contested`              :sref:`0 <stsri> 0`                     :sref:`100 <stsfz> 100`                 :sref:`100 <stri> 100`                 :sref:`0 <stdecmodes> 0`              :sref:`none <stgraphics> 0`
       27  :ref:`screen <screen>`                   4.09.01             Linux        :sref:`15 <screenscores> 15`          :sref:`46 <screenwide> 46`          :sref:`73 <screenlang> 73`         :sref:`1 <screenzwj> 1`           :sref:`50 <screenvs16> 50`            :sref:`0 <screenvs15> contested`          :sref:`0 <screensri> 0`                 :sref:`100 <screensfz> 100`             :sref:`100 <screenri> 100`             :sref:`0 <screendecmodes> 0`          :sref:`none <screengraphics> 0`
       28  :ref:`QTerminal <qterminal>`             1.4.0               Linux        :sref:`14 <qterminalscores> 14`       :sref:`63 <qterminalwide> 63`       :sref:`66 <qterminallang> 66`      :sref:`0 <qterminalzwj> 0`        :sref:`50 <qterminalvs16> 50`         :sref:`0 <qterminalvs15> contested`       :sref:`0 <qterminalsri> 0`              :sref:`100 <qterminalsfz> 100`          :sref:`100 <qterminalri> 100`          :sref:`0 <qterminaldecmodes> 0`       :sref:`none <qterminalgraphics> 0`
       29  :ref:`cool-retro-term <coolretroterm>`   1.2.0               Linux        :sref:`14 <coolretrotermscores> 14`   :sref:`46 <coolretrotermwide> 46`   :sref:`92 <coolretrotermlang> 92`  :sref:`1 <coolretrotermzwj> 1`    :sref:`50 <coolretrotermvs16> 50`     :sref:`0 <coolretrotermvs15> contested`   :sref:`0 <coolretrotermsri> 0`          :sref:`100 <coolretrotermsfz> 100`      :sref:`100 <coolretrotermri> 100`      :sref:`0 <coolretrotermdecmodes> 0`   :sref:`none <coolretrotermgraphics> 0`
       30  :ref:`Extraterm <extraterm>`             0.81.4              Linux        :sref:`13 <extratermscores> 13`       :sref:`13 <extratermwide> 13`       :sref:`0 <extratermlang> 0`        :sref:`0 <extratermzwj> 0`        :sref:`100 <extratermvs16> 100`       :sref:`0 <extratermvs15> contested`       :sref:`0 <extratermsri> 0`              :sref:`100 <extratermsfz> 100`          :sref:`99 <extratermri> 99`            :sref:`0 <extratermdecmodes> 0`       :sref:`none <extratermgraphics> 0`
       31  :ref:`PuTTY <putty>`                     0.81                Linux        :sref:`13 <puttyscores> 13`           :sref:`33 <puttywide> 33`           :sref:`92 <puttylang> 92`          :sref:`1 <puttyzwj> 1`            :sref:`50 <puttyvs16> 50`             :sref:`0 <puttyvs15> contested`           :sref:`0 <puttysri> 0`                  :sref:`100 <puttysfz> 100`              :sref:`100 <puttyri> 100`              :sref:`0 <puttydecmodes> 0`           :sref:`none <puttygraphics> 0`
       32  :ref:`terminology <terminology>`         1.13.0              Linux        :sref:`10 <terminologyscores> 10`     :sref:`25 <terminologywide> 25`     :sref:`11 <terminologylang> 11`    :sref:`1 <terminologyzwj> 1`      :sref:`50 <terminologyvs16> 50`       :sref:`0 <terminologyvs15> contested`     :sref:`0 <terminologysri> 0`            :sref:`100 <terminologysfz> 100`        :sref:`99 <terminologyri> 99`          :sref:`0 <terminologydecmodes> 0`     :sref:`none <terminologygraphics> 0`
       33  :ref:`Hyper <hyper>`                     3.4.1               Linux        :sref:`9 <hyperscores> 9`             :sref:`0 <hyperwide> 0`             :sref:`92 <hyperlang> 92`          :sref:`1 <hyperzwj> 1`            :sref:`50 <hypervs16> 50`             :sref:`0 <hypervs15> contested`           :sref:`0 <hypersri> 0`                  :sref:`100 <hypersfz> 100`              :sref:`100 <hyperri> 100`              :sref:`0 <hyperdecmodes> 0`           :sref:`none <hypergraphics> 0`
       34  :ref:`zutty <zutty>`                     0.14.8              Linux        :sref:`4 <zuttyscores> 4`             :sref:`47 <zuttywide> 47`           :sref:`92 <zuttylang> 92`          :sref:`1 <zuttyzwj> 1`            :sref:`50 <zuttyvs16> 50`             :sref:`0 <zuttyvs15> contested`           :sref:`N/A <zuttysri> contested`        :sref:`N/A <zuttysfz> contested`        :sref:`N/A <zuttyri> contested`        :sref:`0 <zuttydecmodes> 0`           :sref:`none <zuttygraphics> 0`
       35  :ref:`Terminal.app <terminalapp>`        2.15(465)           Darwin       :sref:`0 <terminalappscores> 0`       :sref:`91 <terminalappwide> 91`     :sref:`91 <terminalapplang> 91`    :sref:`0 <terminalappzwj> 0`      :sref:`50 <terminalappvs16> 50`       :sref:`0 <terminalappvs15> contested`     :sref:`N/A <terminalappsri> contested`  :sref:`N/A <terminalappsfz> contested`  :sref:`N/A <terminalappri> contested`  :sref:`0 <terminalappdecmodes> 0`     :sref:`none <terminalappgraphics> 0`
   ======  =======================================  ==================  ===========  ====================================  ==================================  =================================  ================================  ====================================  ========================================  ======================================  ======================================  =====================================  ====================================  =================================================

Common Language support
-----------------------

The following languages were successful
with all terminals emulators tested,
and will not be reported:

(Jinan)
(Yeonbyeon)
Chinese, Gan
Chinese, Hakka
Chinese, Jinyu
Chinese, Mandarin (Beijing)
Chinese, Mandarin (Guiyang)
Chinese, Mandarin (Harbin)
Chinese, Mandarin (Nanjing)
Chinese, Mandarin (Simplified)
Chinese, Mandarin (Tianjin)
Chinese, Mandarin (Traditional)
Chinese, Min Nan
Chinese, Wu
Chinese, Xiang
Chinese, Yue
Colorado
Japanese
Japanese (Osaka)
Japanese (Tokyo)
Korean
Mongolian, Halh (Mongolian)
Nuosu
Vietnamese (Han nom).

Terminal Capabilities
---------------------

This table shows notable terminal capabilities for each terminal,
matching the feature detection performed by ``ucs-detect``.

.. table::
   :class: sphinx-datatable

   =======================================  =======================================  =======================================  =======================================  =======================================  =======================================  =====================================  =====================================  =================================================  ========================================  =======================================  =====================================  =====================================  =====================================  =======================================
   Terminal                                 Bracketed Paste                          Synced Output                            Focus Events                             Mouse SGR                                Graphemes                                BP MIME                                Kitty Kbd                              Graphics                                           XTGETTCAP                                 Text Size                                Kitty Clip                             Kitty Ptr                              Kitty Notif                            Color Report
   =======================================  =======================================  =======================================  =======================================  =======================================  =======================================  =====================================  =====================================  =================================================  ========================================  =======================================  =====================================  =====================================  =====================================  =======================================
   :ref:`ghostty <ghostty>`                 :sref:`yes <ghosttydecmodes> 100`        :sref:`yes <ghosttydecmodes> 100`        :sref:`yes <ghosttydecmodes> 100`        :sref:`yes <ghosttydecmodes> 100`        :sref:`yes <ghosttydecmodes> 100`        :sref:`no <ghosttydecmodes> 0`         :sref:`yes <ghosttykittykbd> 100`      :sref:`Kitty <ghosttygraphics> 100`                :sref:`yes <ghosttyxtgettcap> 100`        :sref:`no <ghosttytextsizing> 0`         :sref:`no <ghosttydecmodes> 0`         :sref:`no <ghosttydecmodes> 0`         :sref:`no <ghosttydecmodes> 0`         :sref:`yes <ghosttydecmodes> 100`
   :ref:`Konsole <konsole>`                 :sref:`no <konsoledecmodes> 0`           :sref:`no <konsoledecmodes> 0`           :sref:`no <konsoledecmodes> 0`           :sref:`no <konsoledecmodes> 0`           :sref:`no <konsoledecmodes> 0`           :sref:`no <konsoledecmodes> 0`         :sref:`no <konsolekittykbd> 0`         :sref:`Sixel, Kitty <konsolegraphics> 100`         :sref:`no <konsolextgettcap> 0`           :sref:`no <konsoletextsizing> 0`         :sref:`no <konsoledecmodes> 0`         :sref:`no <konsoledecmodes> 0`         :sref:`no <konsoledecmodes> 0`         :sref:`yes <konsoledecmodes> 100`
   :ref:`iTerm2 <iterm2>`                   :sref:`yes <iterm2decmodes> 100`         :sref:`yes <iterm2decmodes> 100`         :sref:`yes <iterm2decmodes> 100`         :sref:`yes <iterm2decmodes> 100`         :sref:`yes <iterm2decmodes> 100`         :sref:`yes <iterm2decmodes> 100`       :sref:`yes <iterm2kittykbd> 100`       :sref:`Sixel, iTerm2, Kitty <iterm2graphics> 100`  :sref:`yes <iterm2xtgettcap> 100`         :sref:`no <iterm2textsizing> 0`          :sref:`no <iterm2decmodes> 0`          :sref:`no <iterm2decmodes> 0`          :sref:`no <iterm2decmodes> 0`          :sref:`no <iterm2decmodes> 0`
   :ref:`contour <contour>`                 :sref:`yes <contourdecmodes> 100`        :sref:`yes <contourdecmodes> 100`        :sref:`yes <contourdecmodes> 100`        :sref:`yes <contourdecmodes> 100`        :sref:`yes <contourdecmodes> 100`        :sref:`no <contourdecmodes> 0`         :sref:`yes <contourkittykbd> 100`      :sref:`Sixel <contourgraphics> 50`                 :sref:`yes <contourxtgettcap> 100`        :sref:`no <contourtextsizing> 0`         :sref:`no <contourdecmodes> 0`         :sref:`no <contourdecmodes> 0`         :sref:`yes <contourdecmodes> 100`      :sref:`yes <contourdecmodes> 100`
   :ref:`kitty <kitty>`                     :sref:`yes <kittydecmodes> 100`          :sref:`yes <kittydecmodes> 100`          :sref:`yes <kittydecmodes> 100`          :sref:`yes <kittydecmodes> 100`          :sref:`no <kittydecmodes> 0`             :sref:`yes <kittydecmodes> 100`        :sref:`yes <kittykittykbd> 100`        :sref:`Kitty <kittygraphics> 100`                  :sref:`yes <kittyxtgettcap> 100`          :sref:`yes <kittytextsizing> 100`        :sref:`yes <kittydecmodes> 100`        :sref:`yes <kittydecmodes> 100`        :sref:`yes <kittydecmodes> 100`        :sref:`yes <kittydecmodes> 100`
   :ref:`tmux <tmux>`                       :sref:`no <tmuxdecmodes> 0`              :sref:`no <tmuxdecmodes> 0`              :sref:`no <tmuxdecmodes> 0`              :sref:`no <tmuxdecmodes> 0`              :sref:`no <tmuxdecmodes> 0`              :sref:`no <tmuxdecmodes> 0`            :sref:`no <tmuxkittykbd> 0`            :sref:`Sixel <tmuxgraphics> 50`                    :sref:`no <tmuxxtgettcap> 0`              :sref:`no <tmuxtextsizing> 0`            :sref:`no <tmuxdecmodes> 0`            :sref:`no <tmuxdecmodes> 0`            :sref:`no <tmuxdecmodes> 0`            :sref:`yes <tmuxdecmodes> 100`
   :ref:`Terminal.exe <terminalexe>`        :sref:`yes <terminalexedecmodes> 100`    :sref:`yes <terminalexedecmodes> 100`    :sref:`yes <terminalexedecmodes> 100`    :sref:`yes <terminalexedecmodes> 100`    :sref:`yes <terminalexedecmodes> 100`    :sref:`no <terminalexedecmodes> 0`     :sref:`no <terminalexekittykbd> 0`     :sref:`Sixel <terminalexegraphics> 50`             :sref:`no <terminalexextgettcap> 0`       :sref:`no <terminalexetextsizing> 0`     :sref:`no <terminalexedecmodes> 0`     :sref:`no <terminalexedecmodes> 0`     :sref:`no <terminalexedecmodes> 0`     :sref:`no <terminalexedecmodes> 0`
   :ref:`WezTerm <wezterm>`                 :sref:`yes <weztermdecmodes> 100`        :sref:`yes <weztermdecmodes> 100`        :sref:`yes <weztermdecmodes> 100`        :sref:`yes <weztermdecmodes> 100`        :sref:`yes <weztermdecmodes> 100`        :sref:`no <weztermdecmodes> 0`         :sref:`no <weztermkittykbd> 0`         :sref:`Sixel, Kitty <weztermgraphics> 100`         :sref:`yes <weztermxtgettcap> 100`        :sref:`no <weztermtextsizing> 0`         :sref:`no <weztermdecmodes> 0`         :sref:`no <weztermdecmodes> 0`         :sref:`no <weztermdecmodes> 0`         :sref:`yes <weztermdecmodes> 100`
   :ref:`mintty <mintty>`                   :sref:`yes <minttydecmodes> 100`         :sref:`no <minttydecmodes> 0`            :sref:`yes <minttydecmodes> 100`         :sref:`yes <minttydecmodes> 100`         :sref:`yes <minttydecmodes> 100`         :sref:`no <minttydecmodes> 0`          :sref:`no <minttykittykbd> 0`          :sref:`Sixel <minttygraphics> 50`                  :sref:`no <minttyxtgettcap> 0`            :sref:`no <minttytextsizing> 0`          :sref:`no <minttydecmodes> 0`          :sref:`no <minttydecmodes> 0`          :sref:`no <minttydecmodes> 0`          :sref:`yes <minttydecmodes> 100`
   :ref:`foot <foot>`                       :sref:`yes <footdecmodes> 100`           :sref:`yes <footdecmodes> 100`           :sref:`yes <footdecmodes> 100`           :sref:`yes <footdecmodes> 100`           :sref:`yes <footdecmodes> 100`           :sref:`no <footdecmodes> 0`            :sref:`yes <footkittykbd> 100`         :sref:`Sixel <footgraphics> 50`                    :sref:`yes <footxtgettcap> 100`           :sref:`no <foottextsizing> 0`            :sref:`no <footdecmodes> 0`            :sref:`no <footdecmodes> 0`            :sref:`no <footdecmodes> 0`            :sref:`yes <footdecmodes> 100`
   :ref:`Rio <rio>`                         :sref:`yes <riodecmodes> 100`            :sref:`yes <riodecmodes> 100`            :sref:`yes <riodecmodes> 100`            :sref:`yes <riodecmodes> 100`            :sref:`no <riodecmodes> 0`               :sref:`no <riodecmodes> 0`             :sref:`yes <riokittykbd> 100`          :sref:`Sixel <riographics> 50`                     :sref:`yes <rioxtgettcap> 100`            :sref:`no <riotextsizing> 0`             :sref:`no <riodecmodes> 0`             :sref:`no <riodecmodes> 0`             :sref:`no <riodecmodes> 0`             :sref:`yes <riodecmodes> 100`
   :ref:`mlterm <mlterm>`                   :sref:`yes <mltermdecmodes> 100`         :sref:`no <mltermdecmodes> 0`            :sref:`yes <mltermdecmodes> 100`         :sref:`yes <mltermdecmodes> 100`         :sref:`no <mltermdecmodes> 0`            :sref:`no <mltermdecmodes> 0`          :sref:`no <mltermkittykbd> 0`          :sref:`Sixel, ReGIS <mltermgraphics> 50`           :sref:`yes <mltermxtgettcap> 100`         :sref:`no <mltermtextsizing> 0`          :sref:`no <mltermdecmodes> 0`          :sref:`no <mltermdecmodes> 0`          :sref:`no <mltermdecmodes> 0`          :sref:`yes <mltermdecmodes> 100`
   :ref:`tabby <tabby>`                     :sref:`yes <tabbydecmodes> 100`          :sref:`no <tabbydecmodes> 0`             :sref:`yes <tabbydecmodes> 100`          :sref:`yes <tabbydecmodes> 100`          :sref:`no <tabbydecmodes> 0`             :sref:`no <tabbydecmodes> 0`           :sref:`no <tabbykittykbd> 0`           :sref:`Sixel <tabbygraphics> 50`                   :sref:`no <tabbyxtgettcap> 0`             :sref:`no <tabbytextsizing> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`yes <tabbydecmodes> 100`
   :ref:`alacritty <alacritty>`             :sref:`yes <alacrittydecmodes> 100`      :sref:`yes <alacrittydecmodes> 100`      :sref:`yes <alacrittydecmodes> 100`      :sref:`yes <alacrittydecmodes> 100`      :sref:`no <alacrittydecmodes> 0`         :sref:`no <alacrittydecmodes> 0`       :sref:`yes <alacrittykittykbd> 100`    :sref:`none <alacrittygraphics> 0`                 :sref:`no <alacrittyxtgettcap> 0`         :sref:`no <alacrittytextsizing> 0`       :sref:`no <alacrittydecmodes> 0`       :sref:`no <alacrittydecmodes> 0`       :sref:`no <alacrittydecmodes> 0`       :sref:`yes <alacrittydecmodes> 100`
   :ref:`XTerm <xterm>`                     :sref:`yes <xtermdecmodes> 100`          :sref:`no <xtermdecmodes> 0`             :sref:`yes <xtermdecmodes> 100`          :sref:`yes <xtermdecmodes> 100`          :sref:`no <xtermdecmodes> 0`             :sref:`no <xtermdecmodes> 0`           :sref:`no <xtermkittykbd> 0`           :sref:`none <xtermgraphics> 0`                     :sref:`yes <xtermxtgettcap> 100`          :sref:`no <xtermtextsizing> 0`           :sref:`no <xtermdecmodes> 0`           :sref:`no <xtermdecmodes> 0`           :sref:`no <xtermdecmodes> 0`           :sref:`yes <xtermdecmodes> 100`
   :ref:`Bobcat <bobcat>`                   :sref:`yes <bobcatdecmodes> 100`         :sref:`yes <bobcatdecmodes> 100`         :sref:`yes <bobcatdecmodes> 100`         :sref:`yes <bobcatdecmodes> 100`         :sref:`yes <bobcatdecmodes> 100`         :sref:`no <bobcatdecmodes> 0`          :sref:`no <bobcatkittykbd> 0`          :sref:`Sixel <bobcatgraphics> 50`                  :sref:`no <bobcatxtgettcap> 0`            :sref:`no <bobcattextsizing> 0`          :sref:`no <bobcatdecmodes> 0`          :sref:`no <bobcatdecmodes> 0`          :sref:`no <bobcatdecmodes> 0`          :sref:`yes <bobcatdecmodes> 100`
   :ref:`libvterm <libvterm>`               :sref:`yes <libvtermdecmodes> 100`       :sref:`no <libvtermdecmodes> 0`          :sref:`yes <libvtermdecmodes> 100`       :sref:`yes <libvtermdecmodes> 100`       :sref:`no <libvtermdecmodes> 0`          :sref:`no <libvtermdecmodes> 0`        :sref:`yes <libvtermkittykbd> 100`     :sref:`none <libvtermgraphics> 0`                  :sref:`no <libvtermxtgettcap> 0`          :sref:`no <libvtermtextsizing> 0`        :sref:`no <libvtermdecmodes> 0`        :sref:`no <libvtermdecmodes> 0`        :sref:`no <libvtermdecmodes> 0`        :sref:`yes <libvtermdecmodes> 100`
   :ref:`rxvt-unicode <rxvtunicode>`        :sref:`yes <rxvtunicodedecmodes> 100`    :sref:`no <rxvtunicodedecmodes> 0`       :sref:`yes <rxvtunicodedecmodes> 100`    :sref:`yes <rxvtunicodedecmodes> 100`    :sref:`no <rxvtunicodedecmodes> 0`       :sref:`no <rxvtunicodedecmodes> 0`     :sref:`no <rxvtunicodekittykbd> 0`     :sref:`none <rxvtunicodegraphics> 0`               :sref:`no <rxvtunicodextgettcap> 0`       :sref:`no <rxvtunicodetextsizing> 0`     :sref:`no <rxvtunicodedecmodes> 0`     :sref:`no <rxvtunicodedecmodes> 0`     :sref:`no <rxvtunicodedecmodes> 0`     :sref:`yes <rxvtunicodedecmodes> 100`
   :ref:`termit <termit>`                   :sref:`yes <termitdecmodes> 100`         :sref:`yes <termitdecmodes> 100`         :sref:`yes <termitdecmodes> 100`         :sref:`yes <termitdecmodes> 100`         :sref:`yes <termitdecmodes> 100`         :sref:`no <termitdecmodes> 0`          :sref:`no <termitkittykbd> 0`          :sref:`none <termitgraphics> 0`                    :sref:`yes <termitxtgettcap> 100`         :sref:`no <termittextsizing> 0`          :sref:`no <termitdecmodes> 0`          :sref:`no <termitdecmodes> 0`          :sref:`no <termitdecmodes> 0`          :sref:`yes <termitdecmodes> 100`
   :ref:`xfce4-terminal <xfce4terminal>`    :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`no <xfce4terminaldecmodes> 0`   :sref:`no <xfce4terminalkittykbd> 0`   :sref:`none <xfce4terminalgraphics> 0`             :sref:`yes <xfce4terminalxtgettcap> 100`  :sref:`no <xfce4terminaltextsizing> 0`   :sref:`no <xfce4terminaldecmodes> 0`   :sref:`no <xfce4terminaldecmodes> 0`   :sref:`no <xfce4terminaldecmodes> 0`   :sref:`yes <xfce4terminaldecmodes> 100`
   :ref:`xterm.js <xtermjs>`                :sref:`yes <xtermjsdecmodes> 100`        :sref:`yes <xtermjsdecmodes> 100`        :sref:`yes <xtermjsdecmodes> 100`        :sref:`yes <xtermjsdecmodes> 100`        :sref:`no <xtermjsdecmodes> 0`           :sref:`no <xtermjsdecmodes> 0`         :sref:`yes <xtermjskittykbd> 100`      :sref:`none <xtermjsgraphics> 0`                   :sref:`no <xtermjsxtgettcap> 0`           :sref:`no <xtermjstextsizing> 0`         :sref:`no <xtermjsdecmodes> 0`         :sref:`no <xtermjsdecmodes> 0`         :sref:`yes <xtermjsdecmodes> 100`      :sref:`yes <xtermjsdecmodes> 100`
   :ref:`weston-terminal <westonterminal>`  :sref:`no <westonterminaldecmodes> 0`    :sref:`no <westonterminaldecmodes> 0`    :sref:`no <westonterminaldecmodes> 0`    :sref:`no <westonterminaldecmodes> 0`    :sref:`no <westonterminaldecmodes> 0`    :sref:`no <westonterminaldecmodes> 0`  :sref:`no <westonterminalkittykbd> 0`  :sref:`none <westonterminalgraphics> 0`            :sref:`no <westonterminalxtgettcap> 0`    :sref:`no <westonterminaltextsizing> 0`  :sref:`no <westonterminaldecmodes> 0`  :sref:`no <westonterminaldecmodes> 0`  :sref:`no <westonterminaldecmodes> 0`  :sref:`no <westonterminaldecmodes> 0`
   :ref:`GNOME Terminal <gnometerminal>`    :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`no <gnometerminaldecmodes> 0`   :sref:`no <gnometerminalkittykbd> 0`   :sref:`none <gnometerminalgraphics> 0`             :sref:`yes <gnometerminalxtgettcap> 100`  :sref:`no <gnometerminaltextsizing> 0`   :sref:`no <gnometerminaldecmodes> 0`   :sref:`no <gnometerminaldecmodes> 0`   :sref:`no <gnometerminaldecmodes> 0`   :sref:`yes <gnometerminaldecmodes> 100`
   :ref:`terminator <terminator>`           :sref:`yes <terminatordecmodes> 100`     :sref:`yes <terminatordecmodes> 100`     :sref:`yes <terminatordecmodes> 100`     :sref:`yes <terminatordecmodes> 100`     :sref:`yes <terminatordecmodes> 100`     :sref:`no <terminatordecmodes> 0`      :sref:`no <terminatorkittykbd> 0`      :sref:`none <terminatorgraphics> 0`                :sref:`yes <terminatorxtgettcap> 100`     :sref:`no <terminatortextsizing> 0`      :sref:`no <terminatordecmodes> 0`      :sref:`no <terminatordecmodes> 0`      :sref:`no <terminatordecmodes> 0`      :sref:`yes <terminatordecmodes> 100`
   :ref:`LXTerminal <lxterminal>`           :sref:`yes <lxterminaldecmodes> 100`     :sref:`yes <lxterminaldecmodes> 100`     :sref:`yes <lxterminaldecmodes> 100`     :sref:`yes <lxterminaldecmodes> 100`     :sref:`no <lxterminaldecmodes> 0`        :sref:`no <lxterminaldecmodes> 0`      :sref:`no <lxterminalkittykbd> 0`      :sref:`none <lxterminalgraphics> 0`                :sref:`no <lxterminalxtgettcap> 0`        :sref:`no <lxterminaltextsizing> 0`      :sref:`no <lxterminaldecmodes> 0`      :sref:`no <lxterminaldecmodes> 0`      :sref:`no <lxterminaldecmodes> 0`      :sref:`yes <lxterminaldecmodes> 100`
   :ref:`st <st>`                           :sref:`no <stdecmodes> 0`                :sref:`no <stdecmodes> 0`                :sref:`no <stdecmodes> 0`                :sref:`no <stdecmodes> 0`                :sref:`no <stdecmodes> 0`                :sref:`no <stdecmodes> 0`              :sref:`no <stkittykbd> 0`              :sref:`none <stgraphics> 0`                        :sref:`no <stxtgettcap> 0`                :sref:`no <sttextsizing> 0`              :sref:`no <stdecmodes> 0`              :sref:`no <stdecmodes> 0`              :sref:`no <stdecmodes> 0`              :sref:`yes <stdecmodes> 100`
   :ref:`screen <screen>`                   :sref:`no <screendecmodes> 0`            :sref:`no <screendecmodes> 0`            :sref:`no <screendecmodes> 0`            :sref:`no <screendecmodes> 0`            :sref:`no <screendecmodes> 0`            :sref:`no <screendecmodes> 0`          :sref:`no <screenkittykbd> 0`          :sref:`none <screengraphics> 0`                    :sref:`no <screenxtgettcap> 0`            :sref:`no <screentextsizing> 0`          :sref:`no <screendecmodes> 0`          :sref:`no <screendecmodes> 0`          :sref:`no <screendecmodes> 0`          :sref:`yes <screendecmodes> 100`
   :ref:`QTerminal <qterminal>`             :sref:`no <qterminaldecmodes> 0`         :sref:`no <qterminaldecmodes> 0`         :sref:`no <qterminaldecmodes> 0`         :sref:`no <qterminaldecmodes> 0`         :sref:`no <qterminaldecmodes> 0`         :sref:`no <qterminaldecmodes> 0`       :sref:`no <qterminalkittykbd> 0`       :sref:`none <qterminalgraphics> 0`                 :sref:`no <qterminalxtgettcap> 0`         :sref:`no <qterminaltextsizing> 0`       :sref:`no <qterminaldecmodes> 0`       :sref:`no <qterminaldecmodes> 0`       :sref:`no <qterminaldecmodes> 0`       :sref:`no <qterminaldecmodes> 0`
   :ref:`cool-retro-term <coolretroterm>`   :sref:`no <coolretrotermdecmodes> 0`     :sref:`no <coolretrotermdecmodes> 0`     :sref:`no <coolretrotermdecmodes> 0`     :sref:`no <coolretrotermdecmodes> 0`     :sref:`no <coolretrotermdecmodes> 0`     :sref:`no <coolretrotermdecmodes> 0`   :sref:`no <coolretrotermkittykbd> 0`   :sref:`none <coolretrotermgraphics> 0`             :sref:`no <coolretrotermxtgettcap> 0`     :sref:`no <coolretrotermtextsizing> 0`   :sref:`no <coolretrotermdecmodes> 0`   :sref:`no <coolretrotermdecmodes> 0`   :sref:`no <coolretrotermdecmodes> 0`   :sref:`no <coolretrotermdecmodes> 0`
   :ref:`Extraterm <extraterm>`             :sref:`no <extratermdecmodes> 0`         :sref:`no <extratermdecmodes> 0`         :sref:`no <extratermdecmodes> 0`         :sref:`no <extratermdecmodes> 0`         :sref:`no <extratermdecmodes> 0`         :sref:`no <extratermdecmodes> 0`       :sref:`no <extratermkittykbd> 0`       :sref:`none <extratermgraphics> 0`                 :sref:`no <extratermxtgettcap> 0`         :sref:`no <extratermtextsizing> 0`       :sref:`no <extratermdecmodes> 0`       :sref:`no <extratermdecmodes> 0`       :sref:`no <extratermdecmodes> 0`       :sref:`no <extratermdecmodes> 0`
   :ref:`PuTTY <putty>`                     :sref:`no <puttydecmodes> 0`             :sref:`no <puttydecmodes> 0`             :sref:`no <puttydecmodes> 0`             :sref:`no <puttydecmodes> 0`             :sref:`no <puttydecmodes> 0`             :sref:`no <puttydecmodes> 0`           :sref:`no <puttykittykbd> 0`           :sref:`none <puttygraphics> 0`                     :sref:`no <puttyxtgettcap> 0`             :sref:`no <puttytextsizing> 0`           :sref:`no <puttydecmodes> 0`           :sref:`no <puttydecmodes> 0`           :sref:`no <puttydecmodes> 0`           :sref:`no <puttydecmodes> 0`
   :ref:`terminology <terminology>`         :sref:`no <terminologydecmodes> 0`       :sref:`no <terminologydecmodes> 0`       :sref:`no <terminologydecmodes> 0`       :sref:`no <terminologydecmodes> 0`       :sref:`no <terminologydecmodes> 0`       :sref:`no <terminologydecmodes> 0`     :sref:`no <terminologykittykbd> 0`     :sref:`none <terminologygraphics> 0`               :sref:`no <terminologyxtgettcap> 0`       :sref:`no <terminologytextsizing> 0`     :sref:`no <terminologydecmodes> 0`     :sref:`no <terminologydecmodes> 0`     :sref:`no <terminologydecmodes> 0`     :sref:`yes <terminologydecmodes> 100`
   :ref:`Hyper <hyper>`                     :sref:`no <hyperdecmodes> 0`             :sref:`no <hyperdecmodes> 0`             :sref:`no <hyperdecmodes> 0`             :sref:`no <hyperdecmodes> 0`             :sref:`no <hyperdecmodes> 0`             :sref:`no <hyperdecmodes> 0`           :sref:`no <hyperkittykbd> 0`           :sref:`none <hypergraphics> 0`                     :sref:`no <hyperxtgettcap> 0`             :sref:`no <hypertextsizing> 0`           :sref:`no <hyperdecmodes> 0`           :sref:`no <hyperdecmodes> 0`           :sref:`no <hyperdecmodes> 0`           :sref:`yes <hyperdecmodes> 100`
   :ref:`zutty <zutty>`                     :sref:`no <zuttydecmodes> 0`             :sref:`no <zuttydecmodes> 0`             :sref:`no <zuttydecmodes> 0`             :sref:`no <zuttydecmodes> 0`             :sref:`no <zuttydecmodes> 0`             :sref:`no <zuttydecmodes> 0`           :sref:`no <zuttykittykbd> 0`           :sref:`none <zuttygraphics> 0`                     :sref:`no <zuttyxtgettcap> 0`             :sref:`no <zuttytextsizing> 0`           :sref:`no <zuttydecmodes> 0`           :sref:`no <zuttydecmodes> 0`           :sref:`no <zuttydecmodes> 0`           :sref:`no <zuttydecmodes> 0`
   :ref:`Terminal.app <terminalapp>`        :sref:`no <terminalappdecmodes> 0`       :sref:`no <terminalappdecmodes> 0`       :sref:`no <terminalappdecmodes> 0`       :sref:`no <terminalappdecmodes> 0`       :sref:`no <terminalappdecmodes> 0`       :sref:`no <terminalappdecmodes> 0`     :sref:`no <terminalappkittykbd> 0`     :sref:`none <terminalappgraphics> 0`               :sref:`no <terminalappxtgettcap> 0`       :sref:`no <terminalapptextsizing> 0`     :sref:`no <terminalappdecmodes> 0`     :sref:`no <terminalappdecmodes> 0`     :sref:`no <terminalappdecmodes> 0`     :sref:`yes <terminalappdecmodes> 100`
   =======================================  =======================================  =======================================  =======================================  =======================================  =======================================  =====================================  =====================================  =================================================  ========================================  =======================================  =====================================  =====================================  =====================================  =======================================

TIME Summary
------------

An interesting datapoint is whether there is any correlation between a
terminal's final Score and the average round-trip time of Cursor Position Report
(CPR) responses. This may give some insight into the event loop, CSI sequence
matching and grapheme, emoji, or complex script processing and font performance


.. figure:: _static/plots/time_summary_scatter.png
   :align: center
   :width: 800px

   Score vs CPR round-trip time across all terminals tested

.. note::

   This data reflects only the measured time of Cursor Position Report responses
   and is **not** an indicator of the overall performance quality of any terminal's
   code in regular use. Many factors influence CPR latency, including OS scheduling,
   event queue architecture, IPC overhead, or rendering design. Terminals are not
   expected to optimize for speedy CPR response. This is presented only as
   an interesting observation.

Full Report by Terminal
-----------------------

.. toctree::
   :maxdepth: 1

   sw_results/ghostty
   sw_results/konsole
   sw_results/iterm2
   sw_results/contour
   sw_results/kitty
   sw_results/tmux
   sw_results/terminalexe
   sw_results/wezterm
   sw_results/mintty
   sw_results/foot
   sw_results/rio
   sw_results/mlterm
   sw_results/tabby
   sw_results/alacritty
   sw_results/xterm
   sw_results/bobcat
   sw_results/libvterm
   sw_results/rxvtunicode
   sw_results/termit
   sw_results/xfce4terminal
   sw_results/xtermjs
   sw_results/westonterminal
   sw_results/gnometerminal
   sw_results/terminator
   sw_results/lxterminal
   sw_results/st
   sw_results/screen
   sw_results/qterminal
   sw_results/coolretroterm
   sw_results/extraterm
   sw_results/putty
   sw_results/terminology
   sw_results/hyper
   sw_results/zutty
   sw_results/terminalapp

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
