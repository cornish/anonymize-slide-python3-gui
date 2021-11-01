anonymize-slide
===============

This adds a very simple GUI interface to [Benjamin Gilbert's anonymize-slide](https://github.com/bgilbert/anonymize-slide) program which I previously [updated to run under python3](https://github.com/cornish/anonymize-slide-python3). The CLI functions still work as previously (see below). If no CLI arguments are supplied, the GUI is launched.

**Please note that the updated python3 code has not been tested with MRXS files**

This is a program to remove the slide label from whole-slide images in the
following formats:

 * Aperio SVS
 * Hamamatsu NDPI
 * 3DHISTECH MRXS

Slide files are modified **in place**, making this program both fast and
potentially destructive.  Do not run it on your only copy of a slide.

[Download](https://github.com/cornish/anonymize-slide-python3-gui/releases)

Examples
--------
Launch the GUI (supply no arguments):

    anonymize-slide-gui.py

Delete the label from `slide.mrxs`:

    anonymize-slide-gui.py slide.mrxs

Delete the label from all NDPI files in the current directory:

    anonymize-slide-gui.py *.ndpi

Requirements
------------

 * Python 3.0+

Development Roadmap
-------------------

1. Replace the simple messagebox-based GUI with a proper GUI 
2. Possibly refactor the project and combine with the non-GUI version

License
-------

This program is distributed under the [GNU General Public License, version
2](LICENSE).

No Warranty
-----------

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the [license](COPYING) for more
details.
