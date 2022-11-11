## Computational Methods for Supporting Corpus-Based Research on Indian Art Music
**This book has been written by Thomas Nuttall, Genís Plaja, Lara Pearson, Brindha Manickavasakan, Kaustuv Kanti Ganguli, Ajay Srinivasamurthy and Xavier Serra.** 

This repository includes the source code of the tutorial to get started on the topic of computational analysis of Carnatic and Hindustani Music. This tutorial has been presented at ISMIR 2022, Bengaluru, India. 

----

### Building the book locally
Despite being a web-based resource (in which you can run code examples on the cloud if desired), you can build the book locally. Here are the steps:

1) Clone the [tutorial repository](https://github.com/MTG/IAM-tutorial-ismir22) and ``cd`` into it.
    ```bash
    git clone https://github.com/MTG/IAM-tutorial-ismir22
    cd IAM-tutorial-ismir22
    ```
2) Create an virtual environment for this project. You may use [venv](https://docs.python.org/3/tutorial/venv.html) or [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html). Activate the new environment.
3) Install the required dependencies. These are included in the ``requirements.txt`` file.
    ```bash
    pip install -r requirements.txt
    ```
4) Now build the book by running ``jupyter-book build webbook``. You should see that a ``_build`` folder just appeared into the ``webbook``folder. Navigate to ``webbook/_build/html/`` (writing the path UNIX-styled here) and just double-click on the ``index.html`` file there.
5) Your default browser should pop-up and the landing page of the book should appear. Now you can learn and run the snippets of code locally! 

### Cloning the already built book
You may be alternatively interested on cloning the built book, in case you face issues connecting to the online instance. You would need to only clone the repository, checkout to the ``gh-pages`` branch, and open the ``landing.html`` file in your favourite browser.

----

### Contributing
Even after the presentation in Bengaluru within the context of ISMIR 2022, this tutorial is meant to be the starting point for researchers interested on the corpus-based research on Indian Art Music. If you would like to help getting this resource expanded or fixing the bugs you may identify, please feel free to open and issue in this repository and let us know!

----

### Reference this Book

If you would like to reference this book please use.

```bibtex
@book{iam_tutorial_ismir22,
  Author = {
    Thomas Nuttall and 
    Genís Plaja-Roglans and
    Lara Pearson and 
    Brindha Manickavasakan and 
    Kaustuv Kanti Ganguli and 
    Ajay Srinivasamurthy and 
    Xavier Serra},
  Address = {Bengaluru, India},
  Publisher = {https://mtg.github.io/IAM-tutorial-ismir22},
  Title = {Computational Methods for Supporting Corpus-Based Research on Indian Art Music},
  Year = 2022,
  Url = {https://mtg.github.io/IAM-tutorial-ismir22}
}
```
