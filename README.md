# Running cascades of transducers with Unitex

## Overview

This repository provides Python code to execute Unitex cascades for annotating texts.

The Unitex/Gramlab program should be installed: [https://unitexgramlab.org/](https://unitexgramlab.org/)

The input should be a POS tagged txt-file where each token is encapsulated within brackets: `{token,lemma,pos}`

* Example:
> {I,I.PRON} {visit,visit.VERB} {the,the.DET} {city,city.NOUN} {of,of.ADP} {Lyon,Lyon.PROPN} {.,.PUNCT}

The unitex pipeline is composed of two cascades of transducers:
* analysis.csc
* synthesis.csc


### Analysis cascade


### Synthesis cascade



