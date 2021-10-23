

Créez un environnement conda :

    $ conda create --name python-advanced
    $ conda activate python-advanced


Pui, installez dans cet environnement Python 3.9, Jupyter (notebooks), 
Rise (mode présentation) et Jupytext (support du format "%") :

    $ conda install --channel conda-forge python=3.9 jupyter rise jupytext

Et enfin, visualisez les notebooks avec :

    $ jupyter notebook