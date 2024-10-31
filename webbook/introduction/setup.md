(welcome-setup)=
# Setting everything up
**We kindly ask you to carefully go through this section before reading the tutorial.**


(tutorial-structure)=
## Structure of the book
See the outline in the left side of the page for the complete structure of the tutorial. If not visible, click on the menu button (**☰**) and it will appear. The contents in this tutorial are organized by the main musical aspects studied in the computational analysis of Carnatic and Hindustani Music: **melody**, **rhythm**, **structure**, and **timbre** (and since Nov 2023 we have included **separation** as an additional music aspect!). An introduction to the tradition at a non-technical level is also provided, to provide context to those with little or no background.

Before going through the technologies, we introduce the sources of data for the computational analysis of Indian Art Music that are available in the literature and are crucial for the development and evaluation of reliable tools for the said topic. 

This tutorial is filled with code snippets, audiovisual examples, relevant references, notes, and tips. Take your time to go through all included materials, and **enjoy learning!**


(setting-up)=
## Setting everything up
This is an online, interactive, and self-contained book based on [Jupyter Book](https://jupyterbook.org/en/stable/index.html). It is composed by pieces of text, audiovisual content, and snippets of code which can be interactively run, for you to get familiar with the included tools and collections of data.  

This cool interface helps readers go through the learning materials on the web page. This tutorial can be entirely followed on the web, bypassing the need of installing anything locally. **However, the coding materials in this tutorial are interactive.** There are different ways in which you can explore and run the code in this tutorial. Next up, we briefly present the additional features of this webbook.

(google-collab)=
### Running the book in the cloud: Google Collaboratory
In some pages of the tutorial, you will observe that **a rocket icon (<svg xmlns="http://www.w3.org/2000/svg" height="20" width="20" viewBox="0 0 512 512"><path d="M156.6 384.9L125.7 354c-8.5-8.5-11.5-20.8-7.7-32.2c3-8.9 7-20.5 11.8-33.8L24 288c-8.6 0-16.6-4.6-20.9-12.1s-4.2-16.7 .2-24.1l52.5-88.5c13-21.9 36.5-35.3 61.9-35.3l82.3 0c2.4-4 4.8-7.7 7.2-11.3C289.1-4.1 411.1-8.1 483.9 5.3c11.6 2.1 20.6 11.2 22.8 22.8c13.4 72.9 9.3 194.8-111.4 276.7c-3.5 2.4-7.3 4.8-11.3 7.2v82.3c0 25.4-13.4 49-35.3 61.9l-88.5 52.5c-7.4 4.4-16.6 4.5-24.1 .2s-12.1-12.2-12.1-20.9V380.8c-14.1 4.9-26.4 8.9-35.7 11.9c-11.2 3.6-23.4 .5-31.8-7.8zM384 168a40 40 0 1 0 0-80 40 40 0 1 0 0 80z"/></svg>) appears at the right top of the screen**. This is an indicator that such a page includes runable code, which you can conveniently run on the cloud.

Google Collaboratory (abbreviated as Collab) is a handy tool in which you can import and run the code in this tutorial. Moreove, you will be able to edit the code, to further explore and extend what you will be learning throughout the tutorial.

```{note}
Google Collab hosts GPU/TPU access, which you can use to run the ML/DL based code in ``compiam``. In addition to that, it allows you to download large amounts of data (typically up to 70GB). Therefore, you will also be able to download and explore the datasets (expect long downloading times for the larger datasets).
```

Feel free to import our notebooks to a Google Collab session, where the code can be run, modified, and downloaded. 

<!--```{important} IMPORTANT NOTE PLEASE PAY ATTENTION HERE!
Most likely, after importing a particular notebook of this tutorial to a Google Collab session, the main tool for this tutorial, `compiam`, will not be installed. Make sure to install it by running ``!pip install compiam`` or ``%pip install compiam`` (`!` and `%` indicates, in a Jupyter notebook cell, that the command is run in the command line).
```-->


(building-locally)=
### Building this book locally
You may be interested in building this book in your own machine. This can be done in a few steps.

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
4) Now build the book by running ``jupyter-book build webbook``. You should see that a ``_build`` folder just appeared into the ``webbook`` folder. Navigate to ``webbook/_build/html/`` (writing the path UNIX-styled here) and just double-click on the ``index.html`` file there.
5) Your default browser should pop-up and the landing page of the book should appear. Now you can learn and run the snippets of code locally! 

```{note}
You may download the source code of a particular page using the download button (<svg xmlns="http://www.w3.org/2000/svg" height="20" width="19.5" viewBox="0 0 496 512"><path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3 .3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5 .3-6.2 2.3zm44.2-1.7c-2.9 .7-4.9 2.6-4.6 4.9 .3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3 .7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3 .3 2.9 2.3 3.9 1.6 1 3.6 .7 4.3-.7 .7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3 .7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3 .7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/></svg>) also on the top right of the page. If the page includes runable code, you may get the ``.ipynb`` file to run it locally as well.
```

(getting-in-touch)=
## Getting in touch
Do not hesitate to [get in touch](mailto:thomas.nuttall@upf.edu) for any enquiries, questions, and suggestions! If you encounter an error, problem, or even a typo, please [do open an issue](https://github.com/MTG/IAM-tutorial-ismir22/issues) in the tutorial repository, which may be rapidly done by clicking in the GitHub button on the top right (<svg xmlns="http://www.w3.org/2000/svg" height="20" width="19.5" viewBox="0 0 496 512"><path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3 .3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5 .3-6.2 2.3zm44.2-1.7c-2.9 .7-4.9 2.6-4.6 4.9 .3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3 .7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3 .3 2.9 2.3 3.9 1.6 1 3.6 .7 4.3-.7 .7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3 .7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3 .7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/></svg>).
