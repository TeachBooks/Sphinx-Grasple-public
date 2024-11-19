# sphinx-grasple

**A Grasple exercise extension for Sphinx**.

This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension for inserting Grasple exercises into a Jupyter book as an iframe. It allows you to easily add Grasple question with some formatting and, more importantly, the creation of QR codes in the PDF version of the page. This leads to the source link of the iframe.

This package is a continuation of the package https://github.com/dbalague/sphinx-grasple/.

[Grasple](https://app.grasple.com/) gives you an embed code for each exercise, which can be added directly to your markdown-file. This package improved the embedding. More information on Grasple and the support of TU Delft can be found on: [Teaching Support - Educational Tools - Grasple](https://www.tudelft.nl/en/teaching-support/educational-tools/grasple)

## Installation
To install the teachbooks-sphinx-grasple extension, follow these steps:

**Step 1: Install the Package**

Install the `teachbooks-sphinx-grasple` package using `pip`:
```
pip install teachbooks-sphinx-grasple
```

**Step 2: Add to `requirements.txt`**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:
```
teachbooks-sphinx-grasple
```

**Step 3: Enable in `_config.yml`**

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions (**important**: underscore, not dash this time):
```
sphinx: 
    extra_extensions:
        - teachbooks_sphinx_grasple
```

## Usage

To use, include the following in your Jupyter book

```code
::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f6c1bb4b-e63e-492e-910a-5a8c433de281?id=75093
:label: grasple_exercise_1_3_4
:dropdown:
:description: Cross product in $\R^4$?

::::
```

Which gives the following HTML output:

<div class="grasple admonition" id="grasple_exercise_1">
<p class="admonition-title"><span class="caption-number">Grasple Exercise 1 </span></p>
<div class="section" id="admonition-content">
<div class="side-by-side docutils container">
<div class="description-container docutils container">
<p></p><p>Cross product in $\R^4$</p>
<p></p>
</div>
</div>
<details class="dropdown" open=""><summary>Show/Hide Content</summary><iframe src="https://embed.grasple.com/exercises/f6c1bb4b-e63e-492e-910a-5a8c433de281?id=75093" width="100%" height="400px"></iframe></details></div>
</div>

In the PDF this leads to:
![example pdf](examplepdf.png)


## Important Note

The tests provided are still the original ones from sphinx-exercise and have not (yet) been adapted.
