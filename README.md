# Template for creating slides using reveal.js

This template uses [reveal.js](https://revealjs.com/) for creating nice looking
slides by only editing a Markdown file, with some html syntax for adding some
cool stuff, like columns, fade-in animations, footnotes and more.

## Content

The template contains the following files and directories:

- `slides.md`: Markdown file with the content of the slides.
- `style.less`: define custom CSS classes using [less](http://lesscss.org/).
- `index.html`: HTML file that can be served to show the slides, also contains
  the configurations for reveal.js.

All the dependencies for build the slides are included in the repo so you can
serve them even without internet connection.
- The `reveal.js` directory contains the source files for running
  [reveal.js](https://revealjs.com).
- The `less` directory contains the sources for running
  [less](https://lesscss.org/).
- The `css/fontawesome` directory stores the
  [fontawesome](https://fontawesome.com/) icons.
- The `katex` directory has the sources for [KaTeX](https://katex.org/), a math
  typesetting library for the web.


## Serving the slides

Install [livereload](https://github.com/lepture/python-livereload):

```
pip install livereload
```

or

```
conda install livereload -c conda-forge
```

Then start a local webserver by running:

```
python serve.py
```

Open `http://localhost:8000` in your browser to see the slides. The page will
automatically reload the page when you update any of the files in the
repository.

## Acknowledgements

This template is based on the
[`talk-template`](https://github.com/leouieda/talk-template) created by
[Leonardo Uieda](https://www.leouieda.com).

## License

The template (`slides.md`, `index.html`, and `css/style.less`) is licensed under
a Creative Commons Attribution 4.0 International License.
