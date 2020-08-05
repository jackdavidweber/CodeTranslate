# How to contribute

We'd love to accept your patches and contributions to this project. There are
just a few small guidelines you need to follow.

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult [GitHub Help] for more
information on using pull requests.

[GitHub Help]: https://help.github.com/articles/about-pull-requests/

## Codebase Principles
All contributions should follow the general principles for this repository:
- **Modularization of languages**: each language is contained to language-specific directory and test directory.
- **Thoughtful Design of GAST**: Any changes or additions to the GAST will impact every step of the translations in all languages. Therefore it is crucial that all GAST design choices are justified and examples are given. Follow the same structure as [Language Feature Generic AST Design](https://docs.google.com/document/d/1Q736_paA7if0MukSqXD95lcoi7PhOFF-0eg8dnEqEPk/edit?usp=sharing) and [GAST Examples Doc](https://docs.google.com/document/d/1Ycs8fz0tgYBZrnu2EKR8XvO3nq_6eW5jSDmBKLl37Mo/edit?usp=sharing).
- **Google style guide**: we use [yapf](https://github.com/google/yapf) to adhere to the google style guide for each PR. Once you have installed yapf locally (see [prerequisites](#Prerequisites)) run `yapf -ir --verbose --style "google" .` from the root directory to auto-format.
- **Tests**: any new language features should be tested extensively in the following 3 ways: code to gast, gast to code, integration (code to code). All tests must pass before merging any PR's
