# Running cascades of transducers with Unitex

## Overview

This repository provides Python code to execute Unitex cascades for annotating texts.

The Unitex/Gramlab program should be installed: [https://unitexgramlab.org/](https://unitexgramlab.org/)

The input should be a POS tagged txt-file where each token is encapsulated within brackets: `{token,lemma,pos}`

* Example:
> {I,I.PRON} {visit,visit.VERB} {the,the.DET} {city,city.NOUN} {of,of.ADP} {Lyon,Lyon.PROPN} {.,.PUNCT}

The code available in this repository is working with a unitex pipeline composed of two cascades of transducers:
* analysis.csc
* synthesis.csc


### Analysis cascade


### Synthesis cascade





## Configure a conda environment

### Clone this repository

```bash

git clone https://github.com/ludovicmoncla/cascades-transducers-unitex.git
```

### Configure the environment with all dependencies

* Create a new environment: `unitex-py39`

```bash
conda create -n unitex-py39 python=3.9
```

* Activate the environment

```bash
conda activate unitex-py39
```

* Install dependencies with `pip`

```bash
pip install -r requirements.txt
```

