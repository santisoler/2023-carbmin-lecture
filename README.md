# Slides for guest lecture on carbon mineralization

In this repo you can find the slides I used for a guest lecture I gave in
a course tough by [Dr. Rachel White][rachel] at [EOAS][eoas], [UBC][ubc].

This template uses [reveal.js](https://revealjs.com/) for creating nice looking
slides by only editing a Markdown file, with some html syntax for adding some
cool stuff, like columns, fade-in animations, footnotes and more.

## Serving the slides

Install [livereload](https://github.com/lepture/python-livereload):

```bash
pip install livereload
```

or

```bash
conda install livereload -c conda-forge
```

Then start a local webserver by running:

```bash
python serve.py
```

Open `http://localhost:8000` in your browser to see the slides. The page will
automatically reload the page when you update any of the files in the
repository.

## Acknowledgements

This slides were made using [reveal.js][revealjs], [less][less], [katex][katex]
and [fontawesome][fontawesome].

Based on the
[`talk-template`](https://github.com/leouieda/talk-template) created by
[Leonardo Uieda](https://www.leouieda.com).

## License

The slides (`slides.md`, `index.html`, and `css/style.less`) are licensed
under a [Creative Commons Attribution 4.0 International License](LICENSE),
except for figures under `figs` directory.

The notebooks in `notebooks` folder are licensed under [MIT
License](notebooks/LICENSE_MIT).

[rachel]: https://www.eoas.ubc.ca/people/rachelwhite
[revealjs]: https://revealjs.com/
[less]: https://lesscss.org/
[katex]: https://katex.org/
[fontawesome]: https://fontawesome.com
[eoas]: https://www.eoas.ubc.ca/
[ubc]: https://www.ubc.ca/
