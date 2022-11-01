(compiam)=
# compIAM


This tutorial wrapps up around compIAM (**comp**utational analysis of **I**ndian **A**rt **M**usic), which is a collaborative initiative involving many researchers that aims at putting together a common repository of datasets, tools, and models for the computational analysis of Carnatic and Hindustani music. 


## Motivation

Tons of very interesting and useful works have been carried out within the topic of computational analysis of Carnatic and Hindustani Music. However, it is common to come across, in such research context, difficulties and problems on finding or reproducing the published research.

compIAM aims at being a common and community-driven repository to include Python-based and standardized implementations of research works for the computational analysis of IAM. In addition to that, compIAM includes tools to easily access relevant datasets and corpora.

```{note}
compIAM is very open to contributions! To integrate your works or relevant implementations from other researchers please check out the [contributing guidelines](www.todo.com) and be part of compIAM :)
```

## Installation

compIAM is registered to PyPI, therefore the latest release can be installed with:
```bash
pip install compiam
```


## Available components

compIAM includes the following components:

| **What to load?**     | **Description**                                                         |
|-----------------------|-------------------------------------------------------------------------|
| Datasets              | Initializing dataset loaders through mirdata ([see Datasets](datasets)) |
| Corpora (Dunya)       | Accessing the Dunya corpora ([see Corpora](corpora))                    |
| Tools and models      | Initializing tools and non-pre-trained ML and DL models                 |
| Pre-trained DL models | Initializing pre-trained models                                         |


## Basic usage

compIAM does not have terminal functionalities but it is to be used within Python based-projects. First, import the library to your Python project with: ``import compiam``.

### Importing the integrated tools

The integrated tools and models are organized by the following fundamental musical aspects: melody, rhythm, structure and timbre. You can access the several included tools by importing them from their corresponding modules:
```python
from compiam.melody import FTANetCarnatic
from compiam.rhythm import FourWayTabla
```

```{note}
Print out the available tool for each category: ``compiam.melody.list_tools()``.
```

### Wrappers
compIAM also includes wrappers to easily initialize relevant datasets, corpora, and also pre-trained models for particular problems.

| **Wrapper**                 | **Description**                    | **Option list**                       |
|-----------------------------|------------------------------------|---------------------------------------|
| ``compiam.load_dataset()``  | Initializing dataset loaders       | Run ``compiam.list_datasets()``       |
| ``compiam.load_corpora()``  | Accessing the Dunya corpora        | Run ``compiam.list_corpora()``        |
| ``compiam.load_model()``    | Initializing pre-trained models    | Run ``compiam.list_models()``         |
