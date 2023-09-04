#!/bin/bash
latexmk \
-synctex=1 \
-interaction=nonstopmode \
-file-line-error \
-pdf \
-outdir=/Users/luke/Desktop/NN_notes/ \
/Users/luke/Desktop/NN_notes/nn_notes.tex
