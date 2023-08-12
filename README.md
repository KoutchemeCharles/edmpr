# Evaluating Distance Measures For Program Repair 

This is the code for the paper paper [Evaluating Distance Measures For Program Repair](). 

The student datasets used to conduct our experiments (and our annotations) are available on [HuggingFace](https://huggingface.co/datasets/koutch/intro_prog). Bellow I show how to reproduce the results of our experiments. If you are only interested into implementing the distance measures, check src/distance.py.

In case of inquiry, send me an email: charles.koutcheme@aalto.fi

## Installation

The requirements.txt file can be used with pip to get the packages needed to run the notebooks.
Careful that it requires a python distribution lower than 3.11. There are some incompatibilities between python 3.11 and one of the core package [edist](https://pypi.org/project/edist/) that we use to compute distance measures. 

```
# Recommanded using conda
conda create --name "edmpr" python=3.9
source activate edmpr
pip install -r requirements.txt
unzip data.zip
unzip codebleu
```

## Reproducing experiments

Before running the experiments, unzip the data.zip somewhere and make sure to adapt the configuration files to
specify the path towards the location where you unzipped the data. This data contains the results of the Refactory run on the student solutions. Potentially, you could run the "prepare_refactory" notebook to rerun/reproduce the repair process yourself if you have the [Refactory](https://github.com/githubhuyang/refactory) automated repair tool installed somewhere on your computer, but we already did that for you. 

Both experiments are ran in their corresponding jupyter notebooks (experiment1.ipynb, experiment2.ipynb).

### Notes about codebleu

We found a reimplementation of CodeBLEU [here](https://huggingface.co/spaces/dvitel/codebleu). But it seems to be not maintainted anymore so we updated some minor part of it; that's why we needed to copy the whole repository here. That's inneficient, but in the meantime it will do.


