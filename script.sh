#!/bin/bash

# trick latexmk to detect changes to nn_notes_raw.tex
mv nn_notes_raw.fdb_latexmk nn_notes.fdb_latexmk 

. /Users/luke/Desktop/NN_notes/env/bin/activate
./generate_tex_file.py

latexmk \
-synctex=1 \
-interaction=nonstopmode \
-file-line-error \
-pdf \
-outdir=/Users/luke/Desktop/NN_notes/ \
/Users/luke/Desktop/NN_notes/nn_notes_raw.tex

mv nn_notes_raw.pdf nn_notes.pdf
