# Mon classeur sur GitHub

## Créer un dépot GitHub
Créer un compte sur GitHub (Sign up) depuis un navigateur à l'adresse [https://github.com/](https://github.com/){target="_blank"} :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub00a.png" width=50% alt="inscription GitHub">
</figure>

Ou identifier vous (Sign in) si vous avez déjà un compte :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub00b.png" width=50% alt="identification GitHub">
</figure>

A l'adresse [https://github.com/new](https://github.com/new){target="_blank"} créer un nouveau répertoire de dépot nommé, par exemple `mon_classeur` :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub01c.png" alt="nouveau repository GitHub">
</figure>

Cocher la case **"Initialize this repository with a README"** puis cliquer sur le bouton **"Create repository"**.

> Voilà, vous faites maintenant parti d'un autre [réseau social mondial celui des développeurs de code](https://medium.com/coding-days/focus-sur-github-le-r%C3%A9seau-social-des-d%C3%A9veloppeurs-165a2978ea9e){target="_blank"}...

## Utiliser l'interface web de GitHub pour gérer votre dépot

### Modifier le fichier `README.md`

Le fichier `README` a pour extension `.md` pour [**MarkDown**](https://fr.wikipedia.org/wiki/Markdown){target="_blank"}, c'est ce langage de description rudimentaire que nous utiliserons principalement pour rédiger nos pages web sur GitHub.

> Il existe plusieurs versions de ce langage qui, à partir d'une syntaxe de base commune, possèdent d'autres éléments additionnels spécifiques...

**Cliquer** sur le crayon pour ouvrir le fichier `README.md`dans l'éditeur en ligne :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub02c.png" alt="editer README">
</figure>

**Modifier** son contenu en utilisant la syntaxe [MarkDown à la sauce GitHub](https://guides.github.com/features/mastering-markdown/){target="_blank"} :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub03c.png" alt="modifier README">
</figure>


!!! tip "L'onglet `Preview` permet de visualiser le résultat avant sa publication..."

??? example "Code exemple à copier/coller"    
    ```md
    ## Voici un titre de niveau 2
    ### Et voici un titre de niveau 3
    Ceci est un paragraphe.
    Cette ligne s'affiche dans le même paragraphe à la suite de la première phrase sans retour à la ligne.  
    Cette ligne s'affiche dans le même paragraphe avec un retour à la ligne
    car on a laissé deux caractères espaces après le point de la phrase précédente.

    Cette ligne s'affiche dans un nouveau paragraphe
    car on a laissé deux sauts de ligne après le point de la phrase précédente.

    On peut obtenir du _texte_ avec *simple emphase* rendu en *italique*,
    du __texte__ avec **forte emphase** rendu en **Gras**,
    du **_Texte_** à la fois en **gras** et en *italique*,
    du `code source` rendu en caractères `monospaces`,
        du ~~texte barré~~  rendu avec une ligne en travers du texte.

    ## Un lien :
    Ce document est rédigé en [MarkDown](https://fr.wikipedia.org/wiki/Markdown).

    ## Une image :
    ![illustration GitHub Docs](https://ericecmorlaix.github.io/img/GitHub00c.png)

    ## Une liste :
    - Toto ;
    - Titi ;
    - Tata...

    ## Un avertissement :
    > Libre à vous de personaliser cette page à l'aide de la documentation
    >  du [MarkDown à la sauce GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)...
    ```

**Publier** la nouvelle version du fichier `README.md` en décrivant vos modifications dans un message et puis en cliquant sur le bouton `Commit changes` :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub04c.png" alt="publier README">
</figure>

> **Waouh !** vous venez de faire votre premier [**Commit**](https://fr.wikipedia.org/wiki/Commit){target="_blank"} **!**

### Créer de nouveaux dossier et fichier

**Cliquer** sur le bouton `Add file` depuis l'interface de votre dépot GitHub et choisir `Create new files` :

Dans l'éditeur qui s'ouvre, saisir le nom du fichier avec son extension et son chemin dans l'arborescence, par exemple `docs/index.md` :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub05c.png" alt="créer dossier et fichier">
</figure>

<figure>
    <figcaption>
        Comment éditer une arborescence de dossiers sur GitHub ?        
    </figcaption>
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0a19JTSxclw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe> 
</figure>


**Faire** un nouveau **Commit** avec le message : `ajout fichier index.md dans dossier docs`

### Téléverser des dossiers et fichiers

Depuis le dossier `docs`, **Cliquer** sur le bouton `Add file` depuis l'interface de votre dépot GitHub et choisir `Upload files` :

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitHub06c.png" alt="Glisser/Déposer">
</figure>

!!! tip "Partager votre écran pour Glisser/Déposer vos dossiers et/ou vos fichiers"

???+ example "Exemple à faire vous même :"    
    - **glisser/déposer** un fichier image dans le dossier `docs` ;
    - **Committer** ;
    - **Editer** le fichier `index.md` en y ajoutant l'instruction MarkDown `![image de ...?](nom_du_fichier_image.png)` ;
    - **Prévisualiser** pour vérifier le bon affichage de l'image ;
    - **Committer** ;

## Utiliser VSC en ligne pour gérer votre dépot GitHub

Pour faire fonctionner l'[IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement){target=_blank} Visual Studio Code dans un navigateur et ainsi développer et maintenir des dépôts GitHub depuis n’importe quelle machine sans installation locale on peut utiliser [Codespaces](https://github.com/features/codespaces){target=_blank} ou [Gitpod](https://www.gitpod.io/){target=_blank} :


===  "Codespaces :"
    
    - A la racine de votre dépot GitHub **cliquer** sur le bouton vert `<> Code` puis choisir l'onglet `Codespaces` et enfin **cliquer** sur le bouton vert `Create codespace on main` 

    <figure>
    <img src="https://ericecmorlaix.github.io/img/Codespaces00.png" alt="Codespaces">
    </figure> 

=== "Gitpod :"

    - Sur le site [Gitpod](https://www.gitpod.io/){target=_blank}, **signer** avec votre compte GitHub ;
    - **Choisir** VS Code BROWSER ;
    - **Cliquer** sur `New Workspace` ;
    - **Rechercher** puis choisir votre dépot dans la liste...

Tous les dossiers et fichiers de votre dépot sont alors éditables dans l'environnement de développement intégré Visual Studio Code en ligne.

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitPod01.png" alt="GitPod VSC Explorer">
</figure>

### ==La routine pour maintenir votre site Git avec un éditeur VSC en ligne se résume à :==

??? summary "I - Modifier vos fichiers sur la machine virtuelle :"
    Depuis l'Explorateur (`Explorer` ++"Ctrl"+"Maj"+"E"++) de VSC (_bleu_) :

    - cliquer sur un dossier pour afficher la liste de son contenu ;
    - cliquer sur les icônes (_jaunes_) pour créer un nouveau fichier et/ou un nouveau dossier ;
    - maintenir le clic sur un fichier (ou un dossier) pour le déplacer dans l'arborescence ;
    - cliquer sur un fichier pour l'ouvrir dans l'éditeur afin de le modifier ;
    - cliquer droit sur un fichier `.md` et choisir `Open preview` pour le prévisualiser ;

<figure>
    <img src="https://ericecmorlaix.github.io/img/GitPod02.png" alt="GitPod VSC Explorer">
</figure>


??? summary "II - Indexer vos changements :"
    Depuis le "Contrôle de code source" (_vert_) (`Source Control` ++"Ctrl"+"Maj"+"G"++),
     dans "Changements" (`Changes`) cliquer sur le `+` (_orange_) pour ajouter les fichiers modifiés
      à mettre en attente (indexer) dans cette phase (stage) de développement ;

??? summary "III - Committer, valider vos modifications :"
    Ajouter un message sous "CONTRÔLE DE CODE SOURCE" (`SOURCE CONTROL`) (_rose_)
     pour définir ces modifications à ce stade de votre développement,
      puis cliquer sur `✓` (_violet_) pour valider ce commit ;

??? summary "IV - Pousser les modifications vers votre dépôt distant :"
    Cliquer sur les `...` en face de `CONTRÔLE DE CODE SOURCE`
    et choisir `Push` ;

    
??? example "Exemple à faire vous même :"

    - **cliquer** sur l'icone `New Folder` (_jaune_) pour créer un nouveau dossier nommé `images` ;
    - **déplacer** votre fichier image dans le dossier `images` ;
    - **cliquer** sur le fichier `index.md` pour l'ouvrir dans l'éditeur ;
    - **cliquer**  droit le fichier `index.md`et choisir `Open preview` pour le prévisualiser ;
    - **glisser** l'onglet de la fenêtre de prévisualisation sur le coté droit ;
    - **modifier** le chemin relatif vers l'image dans l'instruction MarkDown `![image de ...?](images/nom_du_fichier_image.png)` ; 
    - **prévisualiser** pour vérifier le bon affichage de l'image ;
    - **indexer**, **Commiter** puis **Pousser** vos modifications ;
    - **vérifier** la mis à jour de votre dépôt ;

