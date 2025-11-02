Results
=======

This is a volunteer-maintained analysis created by and for terminal emulator developers.
We welcome productive contributions and corrections to improve the accuracy and
completeness of these measurements.

.. note::

   These test results are provided as-is and we do not guarantee their correctness.
   The scores and ratings presented here are objective measurements of Unicode and
   terminal feature support, and should not be interpreted as an overall assessment
   of terminal emulator quality or a recommendation. Many factors beyond Unicode
   support contribute to terminal quality.

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

.. table::
   :class: sphinx-datatable

   =======================================  ========================  ===========  ====================================  ====================================  ===================================  ================================  ====================================  ================================  =========================================  ======================================  ====================================  ================
   Terminal Software                        Software Version          OS System    Final Scaled Score                    WIDE                                  LANG                                 ZWJ                               VS16                                  VS15                              Mode 2027                                  DEC Modes                               Elapsed(s)                            Sixel
   =======================================  ========================  ===========  ====================================  ====================================  ===================================  ================================  ====================================  ================================  =========================================  ======================================  ====================================  ================
   :ref:`ghostty <ghostty>`                 1.2.3                     Linux        :sref:`100 <ghosttyscores> 100`       :sref:`15 <ghosttywide> 95`           :sref:`90 <ghosttylang> 90`          :sref:`100 <ghosttyzwj> 100`      :sref:`94 <ghosttyvs16> 94`           :sref:`100 <ghosttyvs15> 100`     :sref:`enabled <ghosttydecmodes> 100`      :sref:`36 <ghosttydecmodes> 55`         :sref:`77 <ghosttytime> 86`           :score-0:`no`
   :ref:`foot <foot>`                       1.16.2                    Linux        :sref:`94 <footscores> 94`            :sref:`15.1 <footwide> 96`            :sref:`55 <footlang> 55`             :sref:`96 <footzwj> 96`           :sref:`100 <footvs16> 100`            :sref:`0 <footvs15> 0`            :sref:`enabled <footdecmodes> 100`         :sref:`30 <footdecmodes> 45`            :sref:`71 <foottime> 87`              :score-100:`yes`
   :ref:`kitty <kitty>`                     0.43.1                    Linux        :sref:`84 <kittyscores> 84`           :sref:`16 <kittywide> 98`             :sref:`90 <kittylang> 90`            :sref:`100 <kittyzwj> 100`        :sref:`100 <kittyvs16> 100`           :sref:`100 <kittyvs15> 100`       :sref:`no <kittydecmodes> 50`              :sref:`19 <kittydecmodes> 29`           :sref:`1748 <kittytime> 35`           :score-0:`no`
   :ref:`Konsole <konsole>`                 23.08.5                   Linux        :sref:`83 <konsolescores> 83`         :sref:`15 <konsolewide> 95`           :sref:`55 <konsolelang> 55`          :sref:`96 <konsolezwj> 96`        :sref:`100 <konsolevs16> 100`         :sref:`0 <konsolevs15> 0`         :sref:`no <konsoledecmodes> 50`            :sref:`0 <konsoledecmodes> 0`           :sref:`75 <konsoletime> 86`           :score-100:`yes`
   :ref:`terminal.exe <terminalexe>`        1.23.12811.0              Linux        :sref:`82 <terminalexescores> 82`     :sref:`16 <terminalexewide> 98`       :sref:`44 <terminalexelang> 44`      :sref:`100 <terminalexezwj> 100`  :sref:`100 <terminalexevs16> 100`     :sref:`0 <terminalexevs15> 0`     :sref:`enabled <terminalexedecmodes> 100`  :sref:`26 <terminalexedecmodes> 39`     :sref:`1147 <terminalexetime> 42`     :score-100:`yes`
   :ref:`tmux <tmux>`                       3.4                       Linux        :sref:`79 <tmuxscores> 79`            :sref:`15.1 <tmuxwide> 96`            :sref:`52 <tmuxlang> 52`             :sref:`81 <tmuxzwj> 81`           :sref:`100 <tmuxvs16> 100`            :sref:`0 <tmuxvs15> 0`            :sref:`no <tmuxdecmodes> 50`               :sref:`0 <tmuxdecmodes> 0`              :sref:`78 <tmuxtime> 86`              :score-100:`yes`
   :ref:`iTerm2 <iterm2>`                   3.6.5                     Darwin       :sref:`79 <iterm2scores> 79`          :sref:`16 <iterm2wide> 94`            :sref:`55 <iterm2lang> 55`           :sref:`99 <iterm2zwj> 99`         :sref:`94 <iterm2vs16> 94`            :sref:`0 <iterm2vs15> 0`          :sref:`no <iterm2decmodes> 50`             :sref:`34 <iterm2decmodes> 52`          :sref:`4367 <iterm2time> 20`          :score-100:`yes`
   :ref:`contour <contour>`                 0.6.2-master-5b1ad5be     Linux        :sref:`75 <contourscores> 75`         :sref:`16 <contourwide> 98`           :sref:`90 <contourlang> 90`          :sref:`96 <contourzwj> 96`        :sref:`0 <contourvs16> 0`             :sref:`0 <contourvs15> 0`         :sref:`enabled <contourdecmodes> 100`      :sref:`39 <contourdecmodes> 59`         :sref:`182 <contourtime> 72`          :score-100:`yes`
   :ref:`WezTerm <wezterm>`                 20251025-070338-b6e75fd7  Linux        :sref:`64 <weztermscores> 64`         :sref:`16 <weztermwide> 98`           :sref:`99 <weztermlang> 99`          :sref:`100 <weztermzwj> 100`      :sref:`0 <weztermvs16> 0`             :sref:`0 <weztermvs15> 0`         :sref:`enabled <weztermdecmodes> 100`      :sref:`22 <weztermdecmodes> 33`         :sref:`1050 <weztermtime> 43`         :score-100:`yes`
   :ref:`mlterm <mlterm>`                   3.9.3                     Linux        :sref:`53 <mltermscores> 53`          :sref:`15 <mltermwide> 95`            :sref:`99 <mltermlang> 99`           :sref:`0 <mltermzwj> 0`           :sref:`0 <mltermvs16> 0`              :sref:`0 <mltermvs15> 0`          :sref:`no <mltermdecmodes> 50`             :sref:`34 <mltermdecmodes> 52`          :sref:`87 <mltermtime> 84`            :score-100:`yes`
   :ref:`XTerm <xterm>`                     390                       Linux        :sref:`35 <xtermscores> 35`           :sref:`15.1 <xtermwide> 96`           :sref:`52 <xtermlang> 52`            :sref:`1 <xtermzwj> 1`            :sref:`0 <xtermvs16> 0`               :sref:`0 <xtermvs15> 0`           :sref:`no <xtermdecmodes> 50`              :sref:`66 <xtermdecmodes> 100`          :sref:`78 <xtermtime> 86`             :score-0:`no`
   :ref:`tabby <tabby>`                     1.0.228                   Darwin       :sref:`35 <tabbyscores> 35`           :sref:`12 <tabbywide> 85`             :sref:`52 <tabbylang> 52`            :sref:`1 <tabbyzwj> 1`            :sref:`0 <tabbyvs16> 0`               :sref:`0 <tabbyvs15> 0`           :sref:`no <tabbydecmodes> 50`              :sref:`19 <tabbydecmodes> 29`           :sref:`273 <tabbytime> 65`            :score-100:`yes`
   :ref:`weston-terminal <westonterminal>`  13.0.0                    Linux        :sref:`31 <westonterminalscores> 31`  :sref:`15.1 <westonterminalwide> 93`  :sref:`0 <westonterminallang> 0`     :sref:`0 <westonterminalzwj> 0`   :sref:`100 <westonterminalvs16> 100`  :sref:`0 <westonterminalvs15> 0`  :sref:`no <westonterminaldecmodes> 50`     :sref:`0 <westonterminaldecmodes> 0`    :sref:`32 <westonterminaltime> 100`   :score-0:`no`
   :ref:`rio <rio>`                         0.2.28                    Darwin       :sref:`28 <rioscores> 28`             :sref:`16 <riowide> 98`               :sref:`52 <riolang> 52`              :sref:`1 <riozwj> 1`              :sref:`0 <riovs16> 0`                 :sref:`0 <riovs15> 0`             :sref:`no <riodecmodes> 50`                :sref:`0 <riodecmodes> 0`               :sref:`529 <riotime> 54`              :score-100:`yes`
   :ref:`Bobcat <bobcat>`                   0.9.7 (r348)              Linux        :sref:`23 <bobcatscores> 23`          :sref:`16 <bobcatwide> 98`            :sref:`52 <bobcatlang> 52`           :sref:`1 <bobcatzwj> 1`           :sref:`0 <bobcatvs16> 0`              :sref:`0 <bobcatvs15> 0`          :sref:`no <bobcatdecmodes> 50`             :sref:`29 <bobcatdecmodes> 44`          :sref:`70 <bobcattime> 87`            :score-0:`no`
   :ref:`rxvt-unicode <rxvtunicode>`        9.31                      Linux        :sref:`22 <rxvtunicodescores> 22`     :sref:`15.1 <rxvtunicodewide> 96`     :sref:`52 <rxvtunicodelang> 52`      :sref:`1 <rxvtunicodezwj> 1`      :sref:`0 <rxvtunicodevs16> 0`         :sref:`0 <rxvtunicodevs15> 0`     :sref:`no <rxvtunicodedecmodes> 50`        :sref:`28 <rxvtunicodedecmodes> 42`     :sref:`62 <rxvtunicodetime> 89`       :score-0:`no`
   :ref:`QTerminal <qterminal>`             1.4.0                     Linux        :sref:`17 <qterminalscores> 17`       :sref:`15.1 <qterminalwide> 95`       :sref:`100 <qterminallang> 100`      :sref:`1 <qterminalzwj> 1`        :sref:`0 <qterminalvs16> 0`           :sref:`0 <qterminalvs15> 0`       :sref:`no <qterminaldecmodes> 50`          :sref:`0 <qterminaldecmodes> 0`         :sref:`75 <qterminaltime> 86`         :score-0:`no`
   :ref:`alacritty <alacritty>`             0.16.1                    Darwin       :sref:`16 <alacrittyscores> 16`       :sref:`17 <alacrittywide> 100`        :sref:`56 <alacrittylang> 56`        :sref:`1 <alacrittyzwj> 1`        :sref:`0 <alacrittyvs16> 0`           :sref:`0 <alacrittyvs15> 0`       :sref:`no <alacrittydecmodes> 50`          :sref:`16 <alacrittydecmodes> 24`       :sref:`128 <alacrittytime> 78`        :score-0:`no`
   :ref:`cool-retro-term <coolretroterm>`   1.2.0                     Darwin       :sref:`14 <coolretrotermscores> 14`   :sref:`15 <coolretrotermwide> 95`     :sref:`100 <coolretrotermlang> 100`  :sref:`1 <coolretrotermzwj> 1`    :sref:`0 <coolretrotermvs16> 0`       :sref:`0 <coolretrotermvs15> 0`   :sref:`no <coolretrotermdecmodes> 50`      :sref:`0 <coolretrotermdecmodes> 0`     :sref:`157 <coolretrotermtime> 74`    :score-0:`no`
   :ref:`Extraterm <extraterm>`             0.81.4                    Darwin       :sref:`13 <extratermscores> 13`       :sref:`14 <extratermwide> 94`         :sref:`5 <extratermlang> 5`          :sref:`0 <extratermzwj> 0`        :sref:`100 <extratermvs16> 100`       :sref:`0 <extratermvs15> 0`       :sref:`no <extratermdecmodes> 50`          :sref:`0 <extratermdecmodes> 0`         :sref:`3775 <extratermtime> 22`       :score-0:`no`
   :ref:`st <st>`                           0.9                       Linux        :sref:`11 <stscores> 11`              :sref:`15.1 <stwide> 96`              :sref:`52 <stlang> 52`               :sref:`1 <stzwj> 1`               :sref:`0 <stvs16> 0`                  :sref:`0 <stvs15> 0`              :sref:`no <stdecmodes> 50`                 :sref:`0 <stdecmodes> 0`                :sref:`72 <sttime> 87`                :score-0:`no`
   :ref:`screen <screen>`                   4.09.01                   Linux        :sref:`10 <screenscores> 10`          :sref:`15.1 <screenwide> 96`          :sref:`42 <screenlang> 42`           :sref:`1 <screenzwj> 1`           :sref:`0 <screenvs16> 0`              :sref:`0 <screenvs15> 0`          :sref:`no <screendecmodes> 50`             :sref:`0 <screendecmodes> 0`            :sref:`65 <screentime> 89`            :score-0:`no`
   :ref:`zutty <zutty>`                     0.14.8                    Linux        :sref:`10 <zuttyscores> 10`           :sref:`15.1 <zuttywide> 96`           :sref:`52 <zuttylang> 52`            :sref:`1 <zuttyzwj> 1`            :sref:`0 <zuttyvs16> 0`               :sref:`0 <zuttyvs15> 0`           :sref:`no <zuttydecmodes> 50`              :sref:`0 <zuttydecmodes> 0`             :sref:`90 <zuttytime> 83`             :score-0:`no`
   :ref:`Terminal.app <terminalapp>`        2.15                      Darwin       :sref:`10 <terminalappscores> 10`     :sref:`16 <terminalappwide> 98`       :sref:`51 <terminalapplang> 51`      :sref:`0 <terminalappzwj> 0`      :sref:`0 <terminalappvs16> 0`         :sref:`0 <terminalappvs15> 0`     :sref:`no <terminalappdecmodes> 50`        :sref:`0 <terminalappdecmodes> 0`       :sref:`118 <terminalapptime> 79`      :score-0:`no`
   :ref:`linux fbdev <linuxfbdev>`          6.14.0-33                 Linux        :sref:`9 <linuxfbdevscores> 9`        :sref:`15.1 <linuxfbdevwide> 0`       :sref:`5 <linuxfbdevlang> 5`         :sref:`5 <linuxfbdevzwj> 5`       :sref:`100 <linuxfbdevvs16> 100`      :sref:`0 <linuxfbdevvs15> 0`      :sref:`no <linuxfbdevdecmodes> 50`         :sref:`0 <linuxfbdevdecmodes> 0`        :sref:`58 <linuxfbdevtime> 90`        :score-0:`no`
   :ref:`PuTTY <putty>`                     0.83                      Linux        :sref:`9 <puttyscores> 9`             :sref:`14 <puttywide> 94`             :sref:`52 <puttylang> 52`            :sref:`1 <puttyzwj> 1`            :sref:`0 <puttyvs16> 0`               :sref:`0 <puttyvs15> 0`           :sref:`no <puttydecmodes> 50`              :sref:`0 <puttydecmodes> 0`             :sref:`128 <puttytime> 77`            :score-0:`no`
   :ref:`terminology <terminology>`         1.13.0                    Linux        :sref:`7 <terminologyscores> 7`       :sref:`17 <terminologywide> 97`       :sref:`13 <terminologylang> 13`      :sref:`1 <terminologyzwj> 1`      :sref:`0 <terminologyvs16> 0`         :sref:`0 <terminologyvs15> 0`     :sref:`no <terminologydecmodes> 50`        :sref:`0 <terminologydecmodes> 0`       :sref:`70 <terminologytime> 87`       :score-0:`no`
   :ref:`termit <termit>`                   3.1 (VTE/7600)            Linux        :sref:`6 <termitscores> 6`            :sref:`15 <termitwide> 95`            :sref:`50 <termitlang> 50`           :sref:`1 <termitzwj> 1`           :sref:`0 <termitvs16> 0`              :sref:`0 <termitvs15> 0`          :sref:`no <termitdecmodes> 50`             :sref:`28 <termitdecmodes> 42`          :sref:`3701 <termittime> 23`          :score-0:`no`
   :ref:`vscode terminal <vscodeterminal>`  1.105.1                   Linux        :sref:`2 <vscodeterminalscores> 2`    :sref:`12 <vscodeterminalwide> 85`    :sref:`52 <vscodeterminallang> 52`   :sref:`1 <vscodeterminalzwj> 1`   :sref:`0 <vscodeterminalvs16> 0`      :sref:`0 <vscodeterminalvs15> 0`  :sref:`no <vscodeterminaldecmodes> 50`     :sref:`19 <vscodeterminaldecmodes> 29`  :sref:`2380 <vscodeterminaltime> 30`  :score-0:`no`
   :ref:`LXTerminal <lxterminal>`           0.4.0(VTE/7600)           Linux        :sref:`1 <lxterminalscores> 1`        :sref:`15 <lxterminalwide> 92`        :sref:`47 <lxterminallang> 47`       :sref:`0 <lxterminalzwj> 0`       :sref:`0 <lxterminalvs16> 0`          :sref:`0 <lxterminalvs15> 0`      :sref:`no <lxterminaldecmodes> 50`         :sref:`28 <lxterminaldecmodes> 42`      :sref:`8454 <lxterminaltime> 9`       :score-0:`no`
   :ref:`GNOME Terminal <gnometerminal>`    3.52.0(VTE/7600)          Linux        :sref:`1 <gnometerminalscores> 1`     :sref:`15 <gnometerminalwide> 92`     :sref:`47 <gnometerminallang> 47`    :sref:`0 <gnometerminalzwj> 0`    :sref:`0 <gnometerminalvs16> 0`       :sref:`0 <gnometerminalvs15> 0`   :sref:`no <gnometerminaldecmodes> 50`      :sref:`28 <gnometerminaldecmodes> 42`   :sref:`8524 <gnometerminaltime> 9`    :score-0:`no`
   :ref:`terminator <terminator>`           2.1.3(VTE/7600)           Linux        :sref:`1 <terminatorscores> 1`        :sref:`15 <terminatorwide> 92`        :sref:`47 <terminatorlang> 47`       :sref:`0 <terminatorzwj> 0`       :sref:`0 <terminatorvs16> 0`          :sref:`0 <terminatorvs15> 0`      :sref:`no <terminatordecmodes> 50`         :sref:`28 <terminatordecmodes> 42`      :sref:`8866 <terminatortime> 8`       :score-0:`no`
   :ref:`xfce4-terminal <xfce4terminal>`    1.1.3(VTE/7600)           Linux        :sref:`0 <xfce4terminalscores> 0`     :sref:`15 <xfce4terminalwide> 95`     :sref:`49 <xfce4terminallang> 49`    :sref:`1 <xfce4terminalzwj> 1`    :sref:`0 <xfce4terminalvs16> 0`       :sref:`0 <xfce4terminalvs15> 0`   :sref:`no <xfce4terminaldecmodes> 50`      :sref:`28 <xfce4terminaldecmodes> 42`   :sref:`14937 <xfce4terminaltime> 0`   :score-0:`no`
   =======================================  ========================  ===========  ====================================  ====================================  ===================================  ================================  ====================================  ================================  =========================================  ======================================  ====================================  ================

DEC Private Modes by Mode
-------------------------

This table shows which DEC Private Modes are supported for each terminal.
Terminals are sorted by number of changeable modes (most first).
Only terminals with at least one changeable mode are shown.
Each cell shows 'yes' (green) if supported, or 'no' (red) if not supported.

.. table::
   :class: sphinx-datatable

   ======  =============================================================  ===============================  =================================  =================================  ================================  ================================  ==============================  ================================  =====================================  ================================  ====================================  =======================================  ====================================  =======================================  =====================================  =================================  ===============================  ===============================  ========================================  ===================================
     Mode  Description                                                    XTerm                            contour                            ghostty                            iTerm2                            mlterm                            foot                            Bobcat                            rxvt-unicode                           termit                            LXTerminal                            GNOME Terminal                           terminator                            xfce4-terminal                           terminal.exe                           WezTerm                            kitty                            tabby                            vscode terminal                           alacritty
   ======  =============================================================  ===============================  =================================  =================================  ================================  ================================  ==============================  ================================  =====================================  ================================  ====================================  =======================================  ====================================  =======================================  =====================================  =================================  ===============================  ===============================  ========================================  ===================================
        1  Cursor Keys Mode                                               :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
        2  VT52 Mode                                                      :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
        3  Column Mode                                                    :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :score-0:`no`                    :score-0:`no`                             :score-0:`no`
        4  Scrolling Mode                                                 :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
        5  Screen Mode (light or dark screen)                             :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :sref:`yes <kittydecmodes> 100`  :score-0:`no`                    :score-0:`no`                             :score-0:`no`
        6  Origin Mode                                                    :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
        7  Auto Wrap Mode                                                 :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
        8  Auto Repeat Mode                                               :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
        9  Mouse X10 tracking                                             :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
       10  Show toolbar (rxvt)                                            :score-0:`no`                    :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       12  Blinking cursor (xterm)                                        :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
       13  Field Delimiter Mode / Start blinking cursor (xterm)           :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       18  Print Form Feed                                                :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       19  Printer Extent                                                 :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       25  Text Cursor Enable Mode                                        :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
       30  Show scrollbar (rxvt)                                          :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       35  Enable font-shifting functions (rxvt)                          :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       38  4014 Mode                                                      :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       40  New Line Mode / Allow 80⇒132 mode (xterm)                      :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       41  more(1) fix (xterm)                                            :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       42  National Replacement Character Set Mode                        :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       44  Turn on margin bell (xterm)                                    :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       45  Reverse-wraparound mode (xterm)                                :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
       46  Start logging (xterm)                                          :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       47  Use Alternate Screen Buffer (xterm)                            :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
       64  Page Cursor Coupling Mode                                      :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       66  Numeric Keypad Mode                                            :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
       67  Backarrow Key Mode                                             :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
       69  DECLRMM - Left Right Margin Mode                               :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       80  Sixel Display Mode                                             :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
       95  No Clearing Screen on Column Change Mode                       :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
      116  Bold and Blink Style Mode                                      :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
      117  Erase Color Mode                                               :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1000  Send Mouse X & Y on button press                               :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
     1001  Use Hilite Mouse Tracking                                      :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1002  Use Cell Motion Mouse Tracking                                 :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
     1003  Use All Motion Mouse Tracking                                  :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
     1004  FocusOut events                                                :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
     1005  Enable UTF-8 Mouse Mode                                        :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
     1006  Enable SGR Mouse Mode                                          :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
     1007  Enable Alternate Scroll Mode                                   :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :sref:`yes <alacrittydecmodes> 100`
     1010  Scroll to bottom on tty output                                 :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1011  Scroll to bottom on key press                                  :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1014  Enable fastScroll resource                                     :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1015  Enable urxvt Mouse Mode                                        :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
     1016  Enable SGR Mouse PixelMode                                     :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
     1034  Interpret "meta" key                                           :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1035  Enable special modifiers for Alt and NumLock keys              :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1036  Send ESC when Meta modifies a key                              :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1037  Send DEL from the editing-keypad Delete key                    :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1039  Send ESC when Alt modifies a key                               :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1040  Keep selection even if not highlighted                         :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1041  Use the CLIPBOARD selection                                    :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1042  Enable Urgency window manager hint when Control-G is received  :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :sref:`yes <alacrittydecmodes> 100`
     1043  Enable raising of the window when Control-G is received        :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1044  Reuse the most recent data copied to CLIPBOARD                 :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1045  Extended Reverse-wraparound mode (XTREVWRAP2)                  :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1046  from Alternate Screen Buffer                                   :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1047  Use Alternate Screen Buffer                                    :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
     1048  Save cursor as in DECSC                                        :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :score-0:`no`
     1049  Save cursor as in DECSC and use alternate screen buffer        :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :score-0:`no`                      :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
     1050  termcap function-key mode                                      :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1051  Set Sun function-key mode                                      :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1060  Set legacy keyboard emulation, i.e, X11R6                      :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1061  Set VT220 keyboard emulation                                   :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1070  Use private color registers for each graphic                   :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1243  Arrow keys swapping (BiDi)                                     :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     1337  Report Key Up                                                  :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2001  Enable readline mouse button-1                                 :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2002  Enable readline mouse button-2                                 :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2003  Enable readline mouse button-3                                 :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2004  Set bracketed paste mode                                       :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :sref:`yes <rxvtunicodedecmodes> 100`  :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :sref:`yes <tabbydecmodes> 100`  :sref:`yes <vscodeterminaldecmodes> 100`  :sref:`yes <alacrittydecmodes> 100`
     2005  Enable readline character-quoting                              :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2006  Enable readline newline pasting                                :sref:`yes <xtermdecmodes> 100`  :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2026  Synchronized Output                                            :score-0:`no`                    :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :sref:`yes <weztermdecmodes> 100`  :sref:`yes <kittydecmodes> 100`  :score-0:`no`                    :score-0:`no`                             :sref:`yes <alacrittydecmodes> 100`
     2027  Grapheme Clustering                                            :score-0:`no`                    :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :sref:`yes <footdecmodes> 100`  :sref:`yes <bobcatdecmodes> 100`  :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2028  Text reflow                                                    :score-0:`no`                    :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2029  Passive Mouse Tracking                                         :score-0:`no`                    :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2030  Report grid cell selection                                     :score-0:`no`                    :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2031  Color palette updates                                          :score-0:`no`                    :sref:`yes <contourdecmodes> 100`  :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :score-0:`no`                          :score-0:`no`                      :sref:`yes <kittydecmodes> 100`  :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2048  In-Band Window Resize Notifications                            :score-0:`no`                    :score-0:`no`                      :sref:`yes <ghosttydecmodes> 100`  :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :score-0:`no`                          :score-0:`no`                      :sref:`yes <kittydecmodes> 100`  :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2500  Mirror box drawing characters                                  :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     2501  BiDi autodetection                                             :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     7727  Application escape key mode                                    :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     8452  Sixel scrolling leaves cursor to right of graphic              :sref:`yes <xtermdecmodes> 100`  :sref:`yes <contourdecmodes> 100`  :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     8800  disable character mapping service                              :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :sref:`yes <mltermdecmodes> 100`  :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :sref:`yes <termitdecmodes> 100`  :sref:`yes <lxterminaldecmodes> 100`  :sref:`yes <gnometerminaldecmodes> 100`  :sref:`yes <terminatordecmodes> 100`  :sref:`yes <xfce4terminaldecmodes> 100`  :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
     9001  win32-input-mode                                               :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :score-0:`no`                   :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :sref:`yes <terminalexedecmodes> 100`  :sref:`yes <weztermdecmodes> 100`  :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
   737769  Input Method Editor (IME) mode                                 :score-0:`no`                    :score-0:`no`                      :score-0:`no`                      :sref:`yes <iterm2decmodes> 100`  :score-0:`no`                     :sref:`yes <footdecmodes> 100`  :score-0:`no`                     :score-0:`no`                          :score-0:`no`                     :score-0:`no`                         :score-0:`no`                            :score-0:`no`                         :score-0:`no`                            :score-0:`no`                          :score-0:`no`                      :score-0:`no`                    :score-0:`no`                    :score-0:`no`                             :score-0:`no`
   ======  =============================================================  ===============================  =================================  =================================  ================================  ================================  ==============================  ================================  =====================================  ================================  ====================================  =======================================  ====================================  =======================================  =====================================  =================================  ===============================  ===============================  ========================================  ===================================

Detailed Reports
----------------

.. toctree::
   :maxdepth: 1

   sw_results/ghostty
   sw_results/foot
   sw_results/kitty
   sw_results/konsole
   sw_results/terminalexe
   sw_results/tmux
   sw_results/iterm2
   sw_results/contour
   sw_results/wezterm
   sw_results/mlterm
   sw_results/xterm
   sw_results/tabby
   sw_results/westonterminal
   sw_results/rio
   sw_results/bobcat
   sw_results/rxvtunicode
   sw_results/qterminal
   sw_results/alacritty
   sw_results/coolretroterm
   sw_results/extraterm
   sw_results/st
   sw_results/screen
   sw_results/zutty
   sw_results/terminalapp
   sw_results/linuxfbdev
   sw_results/putty
   sw_results/terminology
   sw_results/termit
   sw_results/vscodeterminal
   sw_results/lxterminal
   sw_results/gnometerminal
   sw_results/terminator
   sw_results/xfce4terminal

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
