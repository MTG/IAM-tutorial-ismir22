(welcome-setup)=
# Welcome and setup

Introduction paragraph to project

## Structure of the tutorial

See the outline in the left side of the page for the complete structure of the tutorial. 
We organize the contents in the main musical aspects studied in the computational analysis of Carnatic and Hindustani Music: [melody](melody-intro), [rhythm](rhythm-intro), [structure](structure-intro), and[timbre](timbre-intro). Each of these sections is opened with a musicological introduction of the important concepts of Indian Art Music. 

Prior to going through the discussed technologies, we introduce the data (talk about corpora and datasets).


## Setting everything up

This is an online, interactive, and self-contained book based on [Jupyter Book](https://jupyterbook.org/en/stable/index.html). It is composed by pieces of text, audiovisual content, and snippets of code which can be interactively run, for you to get familiar with the included tools and collections of data.  

This cool interface helps readers go through the learning materials without actually the need of installing complicated software. However, there are different ways in which you can explore and run the code in this tutorial. Next up, we briefly present the additional features of this webbook.

### Running the book online: Google Collaboratory
In some pages of the tutorial, you will observe that *a rocket icon appears at the right top of the screen*. This is an indicator that such particular page is includes runable code, which you can conviniently run on the cloud.

Google Collaboratory (abbreviated as Collab) is a handy tool in which you can import and run the code in this tutorial. Moreove, you will be able to edit the code, to further explore and extend what you will be learning throughout the tutorial.

```{note}
Google Collab hosts GPU/TPU access, which you can use to run the ML/DL based code in ``compiam``. In addition to that, it allows you to download large amounts of data (typically up to 70GB). Therefore, you will also be able to download and explore the datasets (expect long downloading times for the larger datasets).
```


### Building this book locally
You may be interested in building this book in your own machine. This can be done in a few steps.

1) Clone the [tutorial repository](https://github.com/MTG/IAM-tutorial-ismir22) and ``cd`` into it.
  ```bash
  git clone https://github.com/MTG/IAM-tutorial-ismir22
  cd IAM-tutorial-ismir22
  ```
2) Create an virtual environment for this project. You may use [venv](TODO:venv_tuto) or [conda](TODO:conda_tuto). Activate the new environment.
3) Install the required dependencies. These are included in the ``requirements.txt`` file.
  ```bash
  pip install -r requirements.txt
  ```
4) Now build the book by running ``jupyter-book build webbook``. You should see that a ``_build`` folder just appeared into the ``webbook``folder. Navigate to ``webbook/_build/html/`` (writing the path UNIX-styled here) and just double-click on the ``index.html`` file there.
5) Your default browser should pop-up and the landing page of the book should appear. Now you can learn and run the snippets of code locally! 

```{note}
You may also download the source code of a particular page using the downloading button also on the top right of the page. If the page includes runable code, you may get the ``.ipynb`` file to run it locally as well.
```
