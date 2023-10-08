
Voici quelques solutions pour produire un diaporama de présentation

## Jupyter notebook

### dans une interface dédiée [Carnets, Basthon, ...](){target=_blank}

### dans Visual Studio Code

Firstly, ensure that you have install Jupyter extension.

enter image description here

It will install several extensions required for Jupyter including slides for you.

Then, you can add a slide type to the cell you're on by opening the Command Palette (Cmd+Shift+P) and selecting Switch Slide Type according to the document in GitHub.

enter image description here

enter image description here

You could modify slide types for notebook cells by selecting the slide type on the cell.

enter image description here

After assigning slide types to your cells, create an HTML slideshow presentation by opening the integrated terminal and running the command, jupyter nbconvert '<notebook-file-name>.ipynb' --to slides --post serve.


Cela génère un fichier HTML qu'il est alors possible de publier sur le web par exemple depuis votre dépot GitHub nommé `username.github.io` comme [https://ericecmorlaix.github.io/dia/Slide-Le_BN_pour_presenter.html](https://ericecmorlaix.github.io/dia/Slide-Le_BN_pour_presenter.html).

???- tip "On peut alors l'intégrer depuis une cellule de code d'un notebook"
    !!! "Code Python"
        ```Python
        %%HTML
        <center>
        <iframe width="560" height="420" src="https://ericecmorlaix.github.io/dia/Slide-Le_BN_pour_presenter.html" title="Exemple de diaporama généré depuis un notebook" ></iframe>
        </center>   
        ```
    !!! "Code alternatif"
        ```Python
        from IPython.display import HTML
        HTML("""<center>
                  <iframe width="560" height="420" src="https://ericecmorlaix.github.io/dia/Slide-Le_BN_pour_presenter.html" title="Exemple de diaporama généré depuis un notebook" ></iframe>
                </center>""")
        ```
    
