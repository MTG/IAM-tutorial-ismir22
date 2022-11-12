(welcome-setup)=
# Welcome and setup
**Welcome to this tutorial, we are very glad to have you here!** 


(tutorial-structure)=
## Structure of the tutorial
See the outline in the left side of the page for the complete structure of the tutorial. If not visible, click on the menu button (**☰**) and it will appear. The contents in this tutorial are organized in the main musical aspects studied in the computational analysis of Carnatic and Hindustani Music: [melody](melody-intro), [rhythm](rhythm-intro), [structure](structure-intro), and [timbre](timbre-intro). Each of these sections is opened with a musicological introduction in which the important concepts of Indian Art Music are presented and discussed.

Before going through the technologies, we introduce the sources of data for the computational analysis of Indian Art Music that are available in the literature and are crucial for the development and evaluation of reliable tools for the said topic. 

This tutorial is filled with code snippets, audiovisual examples, relevant references, notes, and tips. Take your time to go through all included materials, and **enjoy learning!**


(setting-up)=
## Setting everything up
This is an online, interactive, and self-contained book based on [Jupyter Book](https://jupyterbook.org/en/stable/index.html). It is composed by pieces of text, audiovisual content, and snippets of code which can be interactively run, for you to get familiar with the included tools and collections of data.  

This cool interface helps readers go through the learning materials on the web page. This tutorial can be entirely followed on the web, bypassing the need of installing anything locally. **However, the coding materials in this tutorial are interactive.** There are different ways in which you can explore and run the code in this tutorial. Next up, we briefly present the additional features of this webbook.

### Running the book online: Google Collaboratory
In some pages of the tutorial, you will observe that **a rocket icon (<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/rocket.svg" width="20" height="20">) appears at the right top of the screen**. This is an indicator that such particular page is includes runable code, which you can conviniently run on the cloud.

Google Collaboratory (abbreviated as Collab) is a handy tool in which you can import and run the code in this tutorial. Moreove, you will be able to edit the code, to further explore and extend what you will be learning throughout the tutorial.

```{note}
Google Collab hosts GPU/TPU access, which you can use to run the ML/DL based code in ``compiam``. In addition to that, it allows you to download large amounts of data (typically up to 70GB). Therefore, you will also be able to download and explore the datasets (expect long downloading times for the larger datasets).
```


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
4) Now build the book by running ``jupyter-book build webbook``. You should see that a ``_build`` folder just appeared into the ``webbook``folder. Navigate to ``webbook/_build/html/`` (writing the path UNIX-styled here) and just double-click on the ``index.html`` file there.
5) Your default browser should pop-up and the landing page of the book should appear. Now you can learn and run the snippets of code locally! 

```{note}
You may download the source code of a particular page using the download button (<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/download.svg" width="20" height="20">) also on the top right of the page. If the page includes runable code, you may get the ``.ipynb`` file to run it locally as well.
```

(getting-in-touch)=
## Getting in touch
Do not hesitate to [get in touch](mailto:genis.plaja@upf.edu,thomas.nuttall@upf.edu) for any enquiries, questions, and suggestions! If you encounter an error, problem, or even a typo, please [do open an issue](https://github.com/MTG/IAM-tutorial-ismir22/issues) in the tutorial repository, which may be rapidly done by clicking in the GitHub button on the top right (<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/github.svg" width="20" height="20">).