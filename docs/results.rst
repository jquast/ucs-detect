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

.. note::

   Some terminals may optionally support features and modes not represented here.
   This data represents only automatic responses received when launched in their
   default configurations and packaged build options.

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

.. table::
   :class: sphinx-datatable

   ======  =======================================  ========================  ===========  ====================================  ====================================  ===================================  ================================  ====================================  ================================  =========================================  ======================================  ======================================  ====================================
     Rank  Terminal Software                        Software Version          OS System    Final Scaled Score                    WIDE                                  LANG                                 ZWJ                               VS16                                  VS15                              Mode 2027                                  DEC Modes                               Sixel                                   Elapsed(s)
   ======  =======================================  ========================  ===========  ====================================  ====================================  ===================================  ================================  ====================================  ================================  =========================================  ======================================  ======================================  ====================================
        1  :ref:`foot <foot>`                       1.25.0                    Linux        :sref:`100 <footscores> 100`          :sref:`16 <footwide> 98`              :sref:`99 <footlang> 99`             :sref:`96 <footzwj> 96`           :sref:`100 <footvs16> 100`            :sref:`100 <footvs15> 100`        :sref:`enabled <footdecmodes> 100`         :sref:`32 <footdecmodes> 48`            :sref:`yes <footsixel> 100`             :sref:`117 <foottime> 80`
        2  :ref:`ghostty <ghostty>`                 1.2.3                     Linux        :sref:`100 <ghosttyscores> 100`       :sref:`15 <ghosttywide> 95`           :sref:`91 <ghosttylang> 91`          :sref:`100 <ghosttyzwj> 100`      :sref:`94 <ghosttyvs16> 94`           :sref:`100 <ghosttyvs15> 100`     :sref:`enabled <ghosttydecmodes> 100`      :sref:`36 <ghosttydecmodes> 55`         :sref:`no <ghosttysixel> 0`             :sref:`77 <ghosttytime> 86`
        3  :ref:`kitty <kitty>`                     0.43.1                    Linux        :sref:`89 <kittyscores> 89`           :sref:`16 <kittywide> 98`             :sref:`91 <kittylang> 91`            :sref:`100 <kittyzwj> 100`        :sref:`100 <kittyvs16> 100`           :sref:`100 <kittyvs15> 100`       :sref:`no <kittydecmodes> 50`              :sref:`19 <kittydecmodes> 29`           :sref:`no <kittysixel> 0`               :sref:`1748 <kittytime> 37`
        4  :ref:`terminal.exe <terminalexe>`        1.23.12811.0              Windows      :sref:`61 <terminalexescores> 61`     :sref:`16 <terminalexewide> 98`       :sref:`51 <terminalexelang> 51`      :sref:`100 <terminalexezwj> 100`  :sref:`100 <terminalexevs16> 100`     :sref:`0 <terminalexevs15> 0`     :sref:`enabled <terminalexedecmodes> 100`  :sref:`26 <terminalexedecmodes> 39`     :sref:`yes <terminalexesixel> 100`      :sref:`1147 <terminalexetime> 44`
        5  :ref:`iTerm2 <iterm2>`                   3.6.5                     Darwin       :sref:`60 <iterm2scores> 60`          :sref:`16 <iterm2wide> 94`            :sref:`60 <iterm2lang> 60`           :sref:`99 <iterm2zwj> 99`         :sref:`94 <iterm2vs16> 94`            :sref:`0 <iterm2vs15> 0`          :sref:`no <iterm2decmodes> 50`             :sref:`34 <iterm2decmodes> 52`          :sref:`yes <iterm2sixel> 100`           :sref:`4367 <iterm2time> 23`
        6  :ref:`Konsole <konsole>`                 25.08.2                   Linux        :sref:`56 <konsolescores> 56`         :sref:`15 <konsolewide> 96`           :sref:`60 <konsolelang> 60`          :sref:`96 <konsolezwj> 96`        :sref:`100 <konsolevs16> 100`         :sref:`0 <konsolevs15> 0`         :sref:`no <konsoledecmodes> 50`            :sref:`0 <konsoledecmodes> 0`           :sref:`yes <konsolesixel> 100`          :sref:`86 <konsoletime> 84`
        7  :ref:`tmux <tmux>`                       3.4                       Linux        :sref:`51 <tmuxscores> 51`            :sref:`15.1 <tmuxwide> 96`            :sref:`57 <tmuxlang> 57`             :sref:`81 <tmuxzwj> 81`           :sref:`100 <tmuxvs16> 100`            :sref:`0 <tmuxvs15> 0`            :sref:`no <tmuxdecmodes> 50`               :sref:`0 <tmuxdecmodes> 0`              :sref:`yes <tmuxsixel> 100`             :sref:`78 <tmuxtime> 86`
        8  :ref:`contour <contour>`                 0.6.2-master-5b1ad5be     Linux        :sref:`49 <contourscores> 49`         :sref:`16 <contourwide> 98`           :sref:`91 <contourlang> 91`          :sref:`96 <contourzwj> 96`        :sref:`0 <contourvs16> 0`             :sref:`0 <contourvs15> 0`         :sref:`enabled <contourdecmodes> 100`      :sref:`39 <contourdecmodes> 59`         :sref:`yes <contoursixel> 100`          :sref:`182 <contourtime> 73`
        9  :ref:`WezTerm <wezterm>`                 20251025-070338-b6e75fd7  Linux        :sref:`41 <weztermscores> 41`         :sref:`16 <weztermwide> 98`           :sref:`99 <weztermlang> 99`          :sref:`100 <weztermzwj> 100`      :sref:`0 <weztermvs16> 0`             :sref:`0 <weztermvs15> 0`         :sref:`enabled <weztermdecmodes> 100`      :sref:`22 <weztermdecmodes> 33`         :sref:`yes <weztermsixel> 100`          :sref:`1050 <weztermtime> 45`
       10  :ref:`Bobcat <bobcat>`                   0.9.7 (r351)              Linux        :sref:`41 <bobcatscores> 41`          :sref:`17 <bobcatwide> 100`           :sref:`57 <bobcatlang> 57`           :sref:`0 <bobcatzwj> 0`           :sref:`93 <bobcatvs16> 93`            :sref:`0 <bobcatvs15> 0`          :sref:`no <bobcatdecmodes> 50`             :sref:`29 <bobcatdecmodes> 44`          :sref:`yes <bobcatsixel> 100`           :sref:`103 <bobcattime> 82`
       11  :ref:`XTerm <xterm>`                     390                       Linux        :sref:`31 <xtermscores> 31`           :sref:`15.1 <xtermwide> 96`           :sref:`57 <xtermlang> 57`            :sref:`1 <xtermzwj> 1`            :sref:`0 <xtermvs16> 0`               :sref:`0 <xtermvs15> 0`           :sref:`no <xtermdecmodes> 50`              :sref:`66 <xtermdecmodes> 100`          :sref:`maybe <xtermsixel> 50`           :sref:`78 <xtermtime> 86`
       12  :ref:`weston-terminal <westonterminal>`  13.0.0                    Linux        :sref:`24 <westonterminalscores> 24`  :sref:`15.1 <westonterminalwide> 93`  :sref:`11 <westonterminallang> 11`   :sref:`0 <westonterminalzwj> 0`   :sref:`100 <westonterminalvs16> 100`  :sref:`0 <westonterminalvs15> 0`  :sref:`no <westonterminaldecmodes> 50`     :sref:`0 <westonterminaldecmodes> 0`    :sref:`no <westonterminalsixel> 0`      :sref:`32 <westonterminaltime> 100`
       13  :ref:`mlterm <mlterm>`                   3.9.3                     Linux        :sref:`24 <mltermscores> 24`          :sref:`15 <mltermwide> 95`            :sref:`99 <mltermlang> 99`           :sref:`0 <mltermzwj> 0`           :sref:`0 <mltermvs16> 0`              :sref:`0 <mltermvs15> 0`          :sref:`no <mltermdecmodes> 50`             :sref:`34 <mltermdecmodes> 52`          :sref:`yes <mltermsixel> 100`           :sref:`87 <mltermtime> 84`
       14  :ref:`rxvt-unicode <rxvtunicode>`        9.31                      Linux        :sref:`16 <rxvtunicodescores> 16`     :sref:`15.1 <rxvtunicodewide> 96`     :sref:`57 <rxvtunicodelang> 57`      :sref:`1 <rxvtunicodezwj> 1`      :sref:`0 <rxvtunicodevs16> 0`         :sref:`0 <rxvtunicodevs15> 0`     :sref:`no <rxvtunicodedecmodes> 50`        :sref:`28 <rxvtunicodedecmodes> 42`     :sref:`no <rxvtunicodesixel> 0`         :sref:`62 <rxvtunicodetime> 90`
       15  :ref:`Extraterm <extraterm>`             0.81.4                    Darwin       :sref:`16 <extratermscores> 16`       :sref:`14 <extratermwide> 94`         :sref:`15 <extratermlang> 15`        :sref:`0 <extratermzwj> 0`        :sref:`100 <extratermvs16> 100`       :sref:`0 <extratermvs15> 0`       :sref:`no <extratermdecmodes> 50`          :sref:`0 <extratermdecmodes> 0`         :sref:`no <extratermsixel> 0`           :sref:`3775 <extratermtime> 25`
       16  :ref:`alacritty <alacritty>`             0.16.1                    Darwin       :sref:`12 <alacrittyscores> 12`       :sref:`17 <alacrittywide> 100`        :sref:`61 <alacrittylang> 61`        :sref:`1 <alacrittyzwj> 1`        :sref:`0 <alacrittyvs16> 0`           :sref:`0 <alacrittyvs15> 0`       :sref:`no <alacrittydecmodes> 50`          :sref:`16 <alacrittydecmodes> 24`       :sref:`no <alacrittysixel> 0`           :sref:`128 <alacrittytime> 78`
       17  :ref:`QTerminal <qterminal>`             1.4.0                     Linux        :sref:`11 <qterminalscores> 11`       :sref:`15.1 <qterminalwide> 95`       :sref:`100 <qterminallang> 100`      :sref:`1 <qterminalzwj> 1`        :sref:`0 <qterminalvs16> 0`           :sref:`0 <qterminalvs15> 0`       :sref:`no <qterminaldecmodes> 50`          :sref:`0 <qterminaldecmodes> 0`         :sref:`no <qterminalsixel> 0`           :sref:`75 <qterminaltime> 87`
       18  :ref:`cool-retro-term <coolretroterm>`   1.2.0                     Darwin       :sref:`10 <coolretrotermscores> 10`   :sref:`15 <coolretrotermwide> 95`     :sref:`100 <coolretrotermlang> 100`  :sref:`1 <coolretrotermzwj> 1`    :sref:`0 <coolretrotermvs16> 0`       :sref:`0 <coolretrotermvs15> 0`   :sref:`no <coolretrotermdecmodes> 50`      :sref:`0 <coolretrotermdecmodes> 0`     :sref:`no <coolretrotermsixel> 0`       :sref:`157 <coolretrotermtime> 75`
       19  :ref:`tabby <tabby>`                     1.0.228                   Darwin       :sref:`7 <tabbyscores> 7`             :sref:`12 <tabbywide> 85`             :sref:`57 <tabbylang> 57`            :sref:`1 <tabbyzwj> 1`            :sref:`0 <tabbyvs16> 0`               :sref:`0 <tabbyvs15> 0`           :sref:`no <tabbydecmodes> 50`              :sref:`19 <tabbydecmodes> 29`           :sref:`yes <tabbysixel> 100`            :sref:`273 <tabbytime> 66`
       20  :ref:`mintty <mintty>`                   3.8.0.0                   Windows      :sref:`5 <minttyscores> 5`            :sref:`17 <minttywide> 98`            :sref:`0 <minttylang> 0`             :sref:`0 <minttyzwj> 0`           :sref:`55 <minttyvs16> 55`            :sref:`0 <minttyvs15> 0`          :sref:`no <minttydecmodes> 50`             :sref:`0 <minttydecmodes> 0`            :sref:`no <minttysixel> 0`              :sref:`1073 <minttytime> 45`
       21  :ref:`st <st>`                           0.9                       Linux        :sref:`5 <stscores> 5`                :sref:`15.1 <stwide> 96`              :sref:`57 <stlang> 57`               :sref:`1 <stzwj> 1`               :sref:`0 <stvs16> 0`                  :sref:`0 <stvs15> 0`              :sref:`no <stdecmodes> 50`                 :sref:`0 <stdecmodes> 0`                :sref:`maybe <stsixel> 50`              :sref:`72 <sttime> 87`
       22  :ref:`LXTerminal <lxterminal>`           0.4.0(VTE/7600)           Linux        :sref:`5 <lxterminalscores> 5`        :sref:`15 <lxterminalwide> 92`        :sref:`53 <lxterminallang> 53`       :sref:`0 <lxterminalzwj> 0`       :sref:`0 <lxterminalvs16> 0`          :sref:`0 <lxterminalvs15> 0`      :sref:`no <lxterminaldecmodes> 50`         :sref:`28 <lxterminaldecmodes> 42`      :sref:`no <lxterminalsixel> 0`          :sref:`8454 <lxterminaltime> 12`
       23  :ref:`GNOME Terminal <gnometerminal>`    3.52.0(VTE/7600)          Linux        :sref:`5 <gnometerminalscores> 5`     :sref:`15 <gnometerminalwide> 92`     :sref:`53 <gnometerminallang> 53`    :sref:`0 <gnometerminalzwj> 0`    :sref:`0 <gnometerminalvs16> 0`       :sref:`0 <gnometerminalvs15> 0`   :sref:`no <gnometerminaldecmodes> 50`      :sref:`28 <gnometerminaldecmodes> 42`   :sref:`no <gnometerminalsixel> 0`       :sref:`8524 <gnometerminaltime> 12`
       24  :ref:`terminator <terminator>`           2.1.3(VTE/7600)           Linux        :sref:`5 <terminatorscores> 5`        :sref:`15 <terminatorwide> 92`        :sref:`53 <terminatorlang> 53`       :sref:`0 <terminatorzwj> 0`       :sref:`0 <terminatorvs16> 0`          :sref:`0 <terminatorvs15> 0`      :sref:`no <terminatordecmodes> 50`         :sref:`28 <terminatordecmodes> 42`      :sref:`no <terminatorsixel> 0`          :sref:`8866 <terminatortime> 12`
       25  :ref:`zutty <zutty>`                     0.14.8                    Linux        :sref:`5 <zuttyscores> 5`             :sref:`15.1 <zuttywide> 96`           :sref:`57 <zuttylang> 57`            :sref:`1 <zuttyzwj> 1`            :sref:`0 <zuttyvs16> 0`               :sref:`0 <zuttyvs15> 0`           :sref:`no <zuttydecmodes> 50`              :sref:`0 <zuttydecmodes> 0`             :sref:`no <zuttysixel> 0`               :sref:`90 <zuttytime> 84`
       26  :ref:`termit <termit>`                   3.1(VTE/7600)             Linux        :sref:`5 <termitscores> 5`            :sref:`15 <termitwide> 95`            :sref:`57 <termitlang> 57`           :sref:`1 <termitzwj> 1`           :sref:`0 <termitvs16> 0`              :sref:`0 <termitvs15> 0`          :sref:`no <termitdecmodes> 50`             :sref:`28 <termitdecmodes> 42`          :sref:`no <termitsixel> 0`              :sref:`17822 <termittime> 1`
       27  :ref:`xfce4-terminal <xfce4terminal>`    1.1.3(VTE/7600)           Linux        :sref:`5 <xfce4terminalscores> 5`     :sref:`15 <xfce4terminalwide> 95`     :sref:`57 <xfce4terminallang> 57`    :sref:`1 <xfce4terminalzwj> 1`    :sref:`0 <xfce4terminalvs16> 0`       :sref:`0 <xfce4terminalvs15> 0`   :sref:`no <xfce4terminaldecmodes> 50`      :sref:`28 <xfce4terminaldecmodes> 42`   :sref:`no <xfce4terminalsixel> 0`       :sref:`18449 <xfce4terminaltime> 0`
       28  :ref:`Terminal.app <terminalapp>`        2.15                      Darwin       :sref:`4 <terminalappscores> 4`       :sref:`16 <terminalappwide> 98`       :sref:`57 <terminalapplang> 57`      :sref:`0 <terminalappzwj> 0`      :sref:`0 <terminalappvs16> 0`         :sref:`0 <terminalappvs15> 0`     :sref:`no <terminalappdecmodes> 50`        :sref:`0 <terminalappdecmodes> 0`       :sref:`no <terminalappsixel> 0`         :sref:`118 <terminalapptime> 80`
       29  :ref:`screen <screen>`                   4.09.01                   Linux        :sref:`4 <screenscores> 4`            :sref:`15.1 <screenwide> 96`          :sref:`49 <screenlang> 49`           :sref:`1 <screenzwj> 1`           :sref:`0 <screenvs16> 0`              :sref:`0 <screenvs15> 0`          :sref:`no <screendecmodes> 50`             :sref:`0 <screendecmodes> 0`            :sref:`no <screensixel> 0`              :sref:`65 <screentime> 89`
       30  :ref:`PuTTY <putty>`                     0.83                      Linux        :sref:`4 <puttyscores> 4`             :sref:`14 <puttywide> 94`             :sref:`57 <puttylang> 57`            :sref:`1 <puttyzwj> 1`            :sref:`0 <puttyvs16> 0`               :sref:`0 <puttyvs15> 0`           :sref:`no <puttydecmodes> 50`              :sref:`0 <puttydecmodes> 0`             :sref:`no <puttysixel> 0`               :sref:`128 <puttytime> 78`
       31  :ref:`vscode terminal <vscodeterminal>`  1.105.1                   Linux        :sref:`3 <vscodeterminalscores> 3`    :sref:`12 <vscodeterminalwide> 85`    :sref:`57 <vscodeterminallang> 57`   :sref:`1 <vscodeterminalzwj> 1`   :sref:`0 <vscodeterminalvs16> 0`      :sref:`0 <vscodeterminalvs15> 0`  :sref:`no <vscodeterminaldecmodes> 50`     :sref:`19 <vscodeterminaldecmodes> 29`  :sref:`maybe <vscodeterminalsixel> 50`  :sref:`2380 <vscodeterminaltime> 32`
       32  :ref:`linux fbdev <linuxfbdev>`          6.14.0-33                 Linux        :sref:`2 <linuxfbdevscores> 2`        :sref:`15.1 <linuxfbdevwide> 0`       :sref:`15 <linuxfbdevlang> 15`       :sref:`5 <linuxfbdevzwj> 5`       :sref:`100 <linuxfbdevvs16> 100`      :sref:`0 <linuxfbdevvs15> 0`      :sref:`no <linuxfbdevdecmodes> 50`         :sref:`0 <linuxfbdevdecmodes> 0`        :sref:`no <linuxfbdevsixel> 0`          :sref:`58 <linuxfbdevtime> 91`
       33  :ref:`rio <rio>`                         0.2.28                    Darwin       :sref:`2 <rioscores> 2`               :sref:`16 <riowide> 98`               :sref:`57 <riolang> 57`              :sref:`1 <riozwj> 1`              :sref:`0 <riovs16> 0`                 :sref:`0 <riovs15> 0`             :sref:`no <riodecmodes> 50`                :sref:`0 <riodecmodes> 0`               :sref:`yes <riosixel> 100`              :sref:`529 <riotime> 56`
       34  :ref:`terminology <terminology>`         1.13.0                    Linux        :sref:`0 <terminologyscores> 0`       :sref:`17 <terminologywide> 97`       :sref:`22 <terminologylang> 22`      :sref:`1 <terminologyzwj> 1`      :sref:`0 <terminologyvs16> 0`         :sref:`0 <terminologyvs15> 0`     :sref:`no <terminologydecmodes> 50`        :sref:`0 <terminologydecmodes> 0`       :sref:`no <terminologysixel> 0`         :sref:`70 <terminologytime> 88`
   ======  =======================================  ========================  ===========  ====================================  ====================================  ===================================  ================================  ====================================  ================================  =========================================  ======================================  ======================================  ====================================

Common Language support
-----------------------

The following languages were successfull
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
Nuosu
Vietnamese (Han nom).

DEC Private Modes Support
-------------------------

This table shows which DEC Private Modes are supported for each terminal.
Terminals are sorted by number of changeable modes (most first).
Only terminals with at least one changeable mode are shown.
Each cell shows 'enabled' if the mode is enabled, 'may enable' if supported
but not enabled and can be changed, or 'no' if not supported.

.. table::
   :class: sphinx-datatable

   ======  =============================================================  =====================================  =======================================  =======================================  ======================================  ======================================  ====================================  ======================================  ===========================================  ==========================================  =============================================  ==========================================  ======================================  =============================================  ===========================================  =======================================  =====================================  =====================================  ==============================================  =========================================
     Mode  Description                                                    XTerm                                  contour                                  ghostty                                  iTerm2                                  mlterm                                  foot                                  Bobcat                                  rxvt-unicode                                 LXTerminal                                  GNOME Terminal                                 terminator                                  termit                                  xfce4-terminal                                 terminal.exe                                 WezTerm                                  kitty                                  tabby                                  vscode terminal                                 alacritty
   ======  =============================================================  =====================================  =======================================  =======================================  ======================================  ======================================  ====================================  ======================================  ===========================================  ==========================================  =============================================  ==========================================  ======================================  =============================================  ===========================================  =======================================  =====================================  =====================================  ==============================================  =========================================
        1  Cursor Keys Mode                                               :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
        2  VT52 Mode                                                      :sref:`enabled <xtermdecmodes> 100`    :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`enabled <iterm2decmodes> 100`    :sref:`enabled <mltermdecmodes> 100`    :sref:`no <footdecmodes> 0`           :sref:`enabled <bobcatdecmodes> 100`    :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`enabled <terminalexedecmodes> 100`    :sref:`may enable <weztermdecmodes> 75`  :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
        3  Column Mode                                                    :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
        4  Scrolling Mode                                                 :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
        5  Screen Mode (light or dark screen)                             :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`no <weztermdecmodes> 0`           :sref:`may enable <kittydecmodes> 75`  :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
        6  Origin Mode                                                    :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
        7  Auto Wrap Mode                                                 :sref:`enabled <xtermdecmodes> 100`    :sref:`enabled <contourdecmodes> 100`    :sref:`enabled <ghosttydecmodes> 100`    :sref:`enabled <iterm2decmodes> 100`    :sref:`enabled <mltermdecmodes> 100`    :sref:`enabled <footdecmodes> 100`    :sref:`enabled <bobcatdecmodes> 100`    :sref:`enabled <rxvtunicodedecmodes> 100`    :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`enabled <terminalexedecmodes> 100`    :sref:`enabled <weztermdecmodes> 100`    :sref:`enabled <kittydecmodes> 100`    :sref:`enabled <tabbydecmodes> 100`    :sref:`enabled <vscodeterminaldecmodes> 100`    :sref:`enabled <alacrittydecmodes> 100`
        8  Auto Repeat Mode                                               :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`may enable <ghosttydecmodes> 75`  :sref:`enabled <iterm2decmodes> 100`    :sref:`enabled <mltermdecmodes> 100`    :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`enabled <terminalexedecmodes> 100`    :sref:`no <weztermdecmodes> 0`           :sref:`enabled <kittydecmodes> 100`    :sref:`enabled <tabbydecmodes> 100`    :sref:`enabled <vscodeterminaldecmodes> 100`    :sref:`no <alacrittydecmodes> 0`
        9  Mouse X10 tracking                                             :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`no <alacrittydecmodes> 0`
       10  Show toolbar (rxvt)                                            :sref:`no <xtermdecmodes> 0`           :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       12  Blinking cursor (xterm)                                        :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`enabled <ghosttydecmodes> 100`    :sref:`enabled <iterm2decmodes> 100`    :sref:`no <mltermdecmodes> 0`           :sref:`may enable <footdecmodes> 75`  :sref:`no <bobcatdecmodes> 0`           :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`enabled <terminalexedecmodes> 100`    :sref:`may enable <weztermdecmodes> 75`  :sref:`no <kittydecmodes> 0`           :sref:`enabled <tabbydecmodes> 100`    :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
       13  Field Delimiter Mode / Start blinking cursor (xterm)           :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       18  Print Form Feed                                                :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       19  Printer Extent                                                 :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`enabled <mltermdecmodes> 100`    :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       25  Text Cursor Enable Mode                                        :sref:`enabled <xtermdecmodes> 100`    :sref:`enabled <contourdecmodes> 100`    :sref:`enabled <ghosttydecmodes> 100`    :sref:`enabled <iterm2decmodes> 100`    :sref:`enabled <mltermdecmodes> 100`    :sref:`enabled <footdecmodes> 100`    :sref:`enabled <bobcatdecmodes> 100`    :sref:`enabled <rxvtunicodedecmodes> 100`    :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`enabled <terminalexedecmodes> 100`    :sref:`enabled <weztermdecmodes> 100`    :sref:`enabled <kittydecmodes> 100`    :sref:`enabled <tabbydecmodes> 100`    :sref:`enabled <vscodeterminaldecmodes> 100`    :sref:`enabled <alacrittydecmodes> 100`
       30  Show scrollbar (rxvt)                                          :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`enabled <rxvtunicodedecmodes> 100`    :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       35  Enable font-shifting functions (rxvt)                          :sref:`enabled <xtermdecmodes> 100`    :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`enabled <rxvtunicodedecmodes> 100`    :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       38  4014 Mode                                                      :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       40  New Line Mode / Allow 80⇒132 mode (xterm)                      :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       41  more(1) fix (xterm)                                            :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`may enable <iterm2decmodes> 75`  :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       42  National Replacement Character Set Mode                        :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       44  Turn on margin bell (xterm)                                    :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       45  Reverse-wraparound mode (xterm)                                :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`no <mltermdecmodes> 0`           :sref:`enabled <footdecmodes> 100`    :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`may enable <weztermdecmodes> 75`  :sref:`no <kittydecmodes> 0`           :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`no <alacrittydecmodes> 0`
       46  Start logging (xterm)                                          :sref:`no <xtermdecmodes> 0`           :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       47  Use Alternate Screen Buffer (xterm)                            :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`no <alacrittydecmodes> 0`
       64  Page Cursor Coupling Mode                                      :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`enabled <mltermdecmodes> 100`    :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`enabled <terminalexedecmodes> 100`    :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       66  Numeric Keypad Mode                                            :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`no <bobcatdecmodes> 0`           :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`no <alacrittydecmodes> 0`
       67  Backarrow Key Mode                                             :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`may enable <terminalexedecmodes> 75`  :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       69  DECLRMM - Left Right Margin Mode                               :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       80  Sixel Display Mode                                             :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
       95  No Clearing Screen on Column Change Mode                       :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
      116  Bold and Blink Style Mode                                      :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
      117  Erase Color Mode                                               :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`enabled <mltermdecmodes> 100`    :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`may enable <terminalexedecmodes> 75`  :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1000  Send Mouse X & Y on button press                               :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
     1001  Use Hilite Mouse Tracking                                      :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`may enable <iterm2decmodes> 75`  :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1002  Use Cell Motion Mouse Tracking                                 :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
     1003  Use All Motion Mouse Tracking                                  :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
     1004  FocusOut events                                                :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`enabled <terminalexedecmodes> 100`    :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
     1005  Enable UTF-8 Mouse Mode                                        :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`may enable <alacrittydecmodes> 75`
     1006  Enable SGR Mouse Mode                                          :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
     1007  Enable Alternate Scroll Mode                                   :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`enabled <ghosttydecmodes> 100`    :sref:`may enable <iterm2decmodes> 75`  :sref:`no <mltermdecmodes> 0`           :sref:`enabled <footdecmodes> 100`    :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`enabled <terminalexedecmodes> 100`    :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`enabled <alacrittydecmodes> 100`
     1010  Scroll to bottom on tty output                                 :sref:`enabled <xtermdecmodes> 100`    :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1011  Scroll to bottom on key press                                  :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1014  Enable fastScroll resource                                     :sref:`enabled <xtermdecmodes> 100`    :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1015  Enable urxvt Mouse Mode                                        :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`no <bobcatdecmodes> 0`           :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1016  Enable SGR Mouse PixelMode                                     :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`no <alacrittydecmodes> 0`
     1034  Interpret "meta" key                                           :sref:`enabled <xtermdecmodes> 100`    :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`enabled <mltermdecmodes> 100`    :sref:`enabled <footdecmodes> 100`    :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1035  Enable special modifiers for Alt and NumLock keys              :sref:`enabled <xtermdecmodes> 100`    :sref:`no <contourdecmodes> 0`           :sref:`enabled <ghosttydecmodes> 100`    :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`enabled <footdecmodes> 100`    :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1036  Send ESC when Meta modifies a key                              :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`enabled <ghosttydecmodes> 100`    :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`enabled <footdecmodes> 100`    :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1037  Send DEL from the editing-keypad Delete key                    :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1039  Send ESC when Alt modifies a key                               :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`may enable <ghosttydecmodes> 75`  :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1040  Keep selection even if not highlighted                         :sref:`enabled <xtermdecmodes> 100`    :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1041  Use the CLIPBOARD selection                                    :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1042  Enable Urgency window manager hint when Control-G is received  :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`may enable <mltermdecmodes> 75`  :sref:`enabled <footdecmodes> 100`    :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`enabled <alacrittydecmodes> 100`
     1043  Enable raising of the window when Control-G is received        :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1044  Reuse the most recent data copied to CLIPBOARD                 :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1045  Extended Reverse-wraparound mode (XTREVWRAP2)                  :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`may enable <ghosttydecmodes> 75`  :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1046  from Alternate Screen Buffer                                   :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1047  Use Alternate Screen Buffer                                    :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`no <alacrittydecmodes> 0`
     1048  Save cursor as in DECSC                                        :sref:`enabled <xtermdecmodes> 100`    :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`enabled <iterm2decmodes> 100`    :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`may enable <bobcatdecmodes> 75`  :sref:`no <rxvtunicodedecmodes> 0`           :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`enabled <tabbydecmodes> 100`    :sref:`enabled <vscodeterminaldecmodes> 100`    :sref:`no <alacrittydecmodes> 0`
     1049  Save cursor as in DECSC and use alternate screen buffer        :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`no <weztermdecmodes> 0`           :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
     1050  termcap function-key mode                                      :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1051  Set Sun function-key mode                                      :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1060  Set legacy keyboard emulation, i.e, X11R6                      :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1061  Set VT220 keyboard emulation                                   :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1070  Use private color registers for each graphic                   :sref:`enabled <xtermdecmodes> 100`    :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`enabled <footdecmodes> 100`    :sref:`enabled <bobcatdecmodes> 100`    :sref:`no <rxvtunicodedecmodes> 0`           :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`no <terminalexedecmodes> 0`           :sref:`may enable <weztermdecmodes> 75`  :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1243  Arrow keys swapping (BiDi)                                     :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`enabled <lxterminaldecmodes> 100`    :sref:`enabled <gnometerminaldecmodes> 100`    :sref:`enabled <terminatordecmodes> 100`    :sref:`enabled <termitdecmodes> 100`    :sref:`enabled <xfce4terminaldecmodes> 100`    :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     1337  Report Key Up                                                  :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`may enable <iterm2decmodes> 75`  :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2001  Enable readline mouse button-1                                 :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2002  Enable readline mouse button-2                                 :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2003  Enable readline mouse button-3                                 :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2004  Set bracketed paste mode                                       :sref:`may enable <xtermdecmodes> 75`  :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`may enable <bobcatdecmodes> 75`  :sref:`may enable <rxvtunicodedecmodes> 75`  :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`may enable <terminalexedecmodes> 75`  :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`may enable <tabbydecmodes> 75`  :sref:`may enable <vscodeterminaldecmodes> 75`  :sref:`may enable <alacrittydecmodes> 75`
     2005  Enable readline character-quoting                              :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2006  Enable readline newline pasting                                :sref:`may enable <xtermdecmodes> 75`  :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2026  Synchronized Output                                            :sref:`no <xtermdecmodes> 0`           :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`no <mltermdecmodes> 0`           :sref:`may enable <footdecmodes> 75`  :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`may enable <weztermdecmodes> 75`  :sref:`may enable <kittydecmodes> 75`  :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`may enable <alacrittydecmodes> 75`
     2027  Grapheme Clustering                                            :sref:`no <xtermdecmodes> 0`           :sref:`enabled <contourdecmodes> 100`    :sref:`enabled <ghosttydecmodes> 100`    :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`enabled <footdecmodes> 100`    :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`enabled <terminalexedecmodes> 100`    :sref:`enabled <weztermdecmodes> 100`    :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2028  Text reflow                                                    :sref:`no <xtermdecmodes> 0`           :sref:`enabled <contourdecmodes> 100`    :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2029  Passive Mouse Tracking                                         :sref:`no <xtermdecmodes> 0`           :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2030  Report grid cell selection                                     :sref:`no <xtermdecmodes> 0`           :sref:`may enable <contourdecmodes> 75`  :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2031  Color palette updates                                          :sref:`no <xtermdecmodes> 0`           :sref:`may enable <contourdecmodes> 75`  :sref:`may enable <ghosttydecmodes> 75`  :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`may enable <footdecmodes> 75`  :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`may enable <kittydecmodes> 75`  :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2048  In-Band Window Resize Notifications                            :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`may enable <ghosttydecmodes> 75`  :sref:`may enable <iterm2decmodes> 75`  :sref:`no <mltermdecmodes> 0`           :sref:`may enable <footdecmodes> 75`  :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`may enable <kittydecmodes> 75`  :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2500  Mirror box drawing characters                                  :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     2501  BiDi autodetection                                             :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`may enable <lxterminaldecmodes> 75`  :sref:`may enable <gnometerminaldecmodes> 75`  :sref:`may enable <terminatordecmodes> 75`  :sref:`may enable <termitdecmodes> 75`  :sref:`may enable <xfce4terminaldecmodes> 75`  :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     7727  Application escape key mode                                    :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     8452  Sixel scrolling leaves cursor to right of graphic              :sref:`may enable <xtermdecmodes> 75`  :sref:`enabled <contourdecmodes> 100`    :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`may enable <mltermdecmodes> 75`  :sref:`may enable <footdecmodes> 75`  :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`may enable <weztermdecmodes> 75`  :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     8800  disable character mapping service                              :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`may enable <mltermdecmodes> 75`  :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`no <terminalexedecmodes> 0`           :sref:`no <weztermdecmodes> 0`           :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
     9001  win32-input-mode                                               :sref:`no <xtermdecmodes> 0`           :sref:`no <contourdecmodes> 0`           :sref:`no <ghosttydecmodes> 0`           :sref:`no <iterm2decmodes> 0`           :sref:`no <mltermdecmodes> 0`           :sref:`no <footdecmodes> 0`           :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :sref:`no <lxterminaldecmodes> 0`           :sref:`no <gnometerminaldecmodes> 0`           :sref:`no <terminatordecmodes> 0`           :sref:`no <termitdecmodes> 0`           :sref:`no <xfce4terminaldecmodes> 0`           :sref:`enabled <terminalexedecmodes> 100`    :sref:`may enable <weztermdecmodes> 75`  :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :sref:`no <alacrittydecmodes> 0`
   737769  Input Method Editor (IME) mode                                 :score-0:`no`                          :score-0:`no`                            :score-0:`no`                            :sref:`no <iterm2decmodes> 0`           :score-0:`no`                           :sref:`enabled <footdecmodes> 100`    :sref:`no <bobcatdecmodes> 0`           :sref:`no <rxvtunicodedecmodes> 0`           :score-0:`no`                               :score-0:`no`                                  :score-0:`no`                               :score-0:`no`                           :score-0:`no`                                  :score-0:`no`                                :score-0:`no`                            :sref:`no <kittydecmodes> 0`           :sref:`no <tabbydecmodes> 0`           :sref:`no <vscodeterminaldecmodes> 0`           :score-0:`no`
   ======  =============================================================  =====================================  =======================================  =======================================  ======================================  ======================================  ====================================  ======================================  ===========================================  ==========================================  =============================================  ==========================================  ======================================  =============================================  ===========================================  =======================================  =====================================  =====================================  ==============================================  =========================================

Full Report by Terminal
-----------------------

.. toctree::
   :maxdepth: 1

   sw_results/foot
   sw_results/ghostty
   sw_results/kitty
   sw_results/terminalexe
   sw_results/iterm2
   sw_results/konsole
   sw_results/tmux
   sw_results/contour
   sw_results/wezterm
   sw_results/bobcat
   sw_results/xterm
   sw_results/westonterminal
   sw_results/mlterm
   sw_results/rxvtunicode
   sw_results/extraterm
   sw_results/alacritty
   sw_results/qterminal
   sw_results/coolretroterm
   sw_results/tabby
   sw_results/mintty
   sw_results/st
   sw_results/lxterminal
   sw_results/gnometerminal
   sw_results/terminator
   sw_results/zutty
   sw_results/termit
   sw_results/xfce4terminal
   sw_results/terminalapp
   sw_results/screen
   sw_results/putty
   sw_results/vscodeterminal
   sw_results/linuxfbdev
   sw_results/rio
   sw_results/terminology

.. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html
.. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html
.. _`ucs-detect`: https://github.com/jquast/ucs-detect
.. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html
