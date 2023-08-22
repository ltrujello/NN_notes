.PHONY: default
default: spellcheck

.PHONY: spellcheck
spellcheck:
	aspell --home-dir=. -t list < nn_notes.tex
