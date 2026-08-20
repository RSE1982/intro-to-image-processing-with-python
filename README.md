# Introduction to Image Processing with Python

Development repository for the LaTeX manuscript, Jupyter companion notebooks,
and the `pyimage` implementation project.

## Current state

This starter contains the publication-oriented LaTeX framework, drafted front
matter, the first chapter, a Chapter 2 scaffold, chapter placeholders, a
provisional historical bibliography and the sign-off appendix scaffold.

## Build the book

From the `book/` directory:

```bash
make pdf
```

or:

```bash
latexmk -lualatex main.tex
```

The document uses BibLaTeX with Biber. `latexmk` should invoke the required
bibliography pass automatically.

## Development workflow

The intended workflow is:

1. develop concepts and experiments in a chapter notebook;
2. write the referenced explanation in LaTeX;
3. move validated code into `project/src/pyimage/`;
4. add pytest coverage under `project/tests/`;
5. generate reproducible figures for the manuscript where appropriate.

## Licence

This repository uses separate licences for educational content and source
code.

### Course material

Copyright © 2026 Robert Elliott. All rights reserved.

This includes, unless otherwise stated:

- course notes and explanations
- written tutorials
- diagrams and illustrations
- exercises and assessments
- course structure
- documentation
- educational text contained within notebooks

See [LICENSE](LICENSE).

### Source code

Original Python source code contained within `src/` and `examples/` is
licensed under the MIT License.

Original program code contained in Jupyter notebook code cells is also
licensed under the MIT License unless otherwise stated.

See [LICENSE-CODE](LICENSE-CODE).

### Third-party material

Third-party images, datasets, code, quotations and other resources remain
subject to their original copyright and licence terms.