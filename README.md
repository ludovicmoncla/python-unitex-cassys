# Running Unitex CasSys cascades with Python

## Overview

This repository provides Python code that enables the execution of Unitex CasSys cascades for annotating texts.

The Unitex/Gramlab program should be installed: [https://unitexgramlab.org/](https://unitexgramlab.org/)



The code available in this repository is working with a Unitex CasSys pipeline composed of two cascades of transducers (i.e., graphs):
* analysis.csc
* synthesis.csc


### Analysis cascade

The analysis cascade (`analysis.csc`) is the core of the annotation process, it executes a sequence of transducers which annotate elements in a specific order. The annotations added by transducers can be reused as patterns in the next transducers of the cascade.
The POS tagset used in patterns shoud be adapted depending the POS tagger used in input. 


### Synthesis cascade

The synthesis cascade (`synthesis.csc`) transforms the output of the first cascade (XML-CasSys) into a valid XML markup language following the annotation tagset defined in the analysis cascade. By default, all tokens are embedded in a `<w>` xml element with their `pos` and `lemma` in attributes. 


## Input

The input should be a POS tagged txt-file where each token is encapsulated within brackets: `{token,lemma,pos}`

* Example:

The following sentence:
> Mark your calendars for an exciting event at 35 Charles Street, London, on the 3rd of June 2023.

should be tagged as follows:
> {Mark,mark.VERB} {your,your.PRON} {calendars,calendar.NOUN} {for,for.ADP} {an,an.DET} {exciting,exciting.ADJ} {event,event.NOUN} {at,at.ADP} {35,35.NUM} {Charles,Charles.PROPN} {Street,Street.PROPN} {\,,.PUNCT} {London,London.PROPN} {\,,.PUNCT} {on,on.ADP} {the,the.DET} {3rd,3rd.NOUN} {of,of.ADP} {June,June.PROPN} {2023,2023.NUM} {.,.PUNCT} 


You can use the functions from `scripts/posTagger_to_unitex.py` to produce this format depending on the POS tagger you use. At the moment, functions are given for converting [spaCy](https://spacy.io) doc object. 
Functions for converting [Treetagger](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/) and [Stanza](https://stanfordnlp.github.io/stanza/) formats will be available soon.


## Directory structure

The Unitex path folders should have the following structure:

* `{unitex-directory}/{language}/CasSys/{project-name}/analysis.csc`
* `{unitex-directory}/{language}/CasSys/{project-name}/synthesis.csc`
* `{unitex-directory}/{language}/Graphs/{project-name}/analysis/`
* `{unitex-directory}/{language}/Graphs/{project-name}/synthesis/`

`{unitex-directory}` refers to your Unitex personal working directory. It might be different from the Unitex installation directory and is usually installed in your `$HOME` directory.

The `synthesis` cascade and graphs can be downloaded here: [Unitex-CasSys](./Unitex-CasSys)


## Demonstration

An example of cascades and graphs can be downloaded here: [Unitex-CasSys](./Unitex-CasSys).

* Notebook: [usage-demo.ipynb](usage-demo.ipynb) 



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


## Acknowledgement

The authors are grateful to the ASLAN project (ANR-10-LABX-0081) of the Université de Lyon, for its financial support within the French program "Investments for the Future" operated by the National Research Agency (ANR).