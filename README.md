
# CodeTranslate

CodeTranslate is a one-stop site for developers to rapidly scale-up in unfamiliar languages without having to memorize syntax, follow tutorials, or read documentation. It is “Google Translate” for code: a developer can type code in a known language and see the translation for an unfamiliar language. 


## Demo
Check out our live demo at http://bit.do/codetranslate. The repository for the frontend of the demo can be found [here](https://github.com/cjoshea9/cjs_capstone_frontend). Please note that the demo is currently hosted for free on [Heroku](https://www.heroku.com/) and may take some time to load up.

## API Documentation
We welcome use of our public api so that you can integrate code translations into your own projects! Check out our [API Documentation](https://app.swaggerhub.com/apis-docs/jackdavidweber/CodeTranslate/1.0.0#/developers/translate) if you are interested.

## Technical Setup

- Clone this repository ([how to clone](https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository))
- `cd cjs_capstone`
- make sure you have all [prerequisites](#Prerequisites) installed
- To run tests: `pytest`
- To run api locally: `python app.py`

### Prerequisites

The main pre-requisite is that you have pip installed. Install [pip](https://pypi.org/project/pip/). Once you have pip installed, take the following steps:

- make sure you are in the root directory
- create a [virtual enviornment](https://docs.python.org/3/library/venv.html) in python 3
- copy-paste the following into terminal:

```
$ pip install -r requirements.txt # for running server
$ pip install -U pytest # for testing
$ pip install yapf # for auto formatting
```
### Adding service key 
1) Download service key from [firebase project](https://console.firebase.google.com/project/codetranslate-feedback/settings/serviceaccounts/adminsdk)
2) Select generate new key button
3) Download to `private_keys/firebase-access-key.json`
4) `python tools/add_environ_var.py` 

## Generic Abstract Syntax Tree
The generic AST (gast) is a tree structured JSON file that is able to serve as a common-ground between the AST's of multiple languages. This is important because it allows the developers to think of the translation as a series of black boxes. For each supported language, there is the translation from the language to the gast and the translation from the gast back to the language. As long as the gast is agreed upon, developers can easily split up the work for the two parts of the translation without running into issues. The stable nature of the gast also means that adding new languages should not affect previously written code.

For each language feature that we wanted to support, we sat down and looked at the AST's for various languages. Using elements across AST's, we then wrote the structure for our gast, adding it to our ["contract" document](https://docs.google.com/document/d/1Ycs8fz0tgYBZrnu2EKR8XvO3nq_6eW5jSDmBKLl37Mo/edit#heading=h.x9snb54sjlu9). This contract document served to both coordinate our efforts and also functioned as the basis for our testing. Once added to our contract, we linked to it in our [GAST Design Doc](https://docs.google.com/document/d/1Q736_paA7if0MukSqXD95lcoi7PhOFF-0eg8dnEqEPk/edit?usp=sharing) and provided justification for the design choices we made.


## Contributing

We welcome contributions to this project. For small fixes, use github PR's. For larger changes, first add an issue to github issues.

All contributions should follow the general principles for this repository:
- **Modularization of languages**: each language is contained to language-specific directory and test directory.
- **Thoughtful Design of GAST**: Any changes or additions to the GAST will impact every step of the translations in all languages. Therefore it is crucial that all GAST design choices are justified and examples are given. Follow the same structure as [Language Feature Generic AST Design](https://docs.google.com/document/d/1Q736_paA7if0MukSqXD95lcoi7PhOFF-0eg8dnEqEPk/edit?usp=sharing) and [GAST Examples Doc](https://docs.google.com/document/d/1Ycs8fz0tgYBZrnu2EKR8XvO3nq_6eW5jSDmBKLl37Mo/edit?usp=sharing).
- **Google style guide**: we use [yapf](https://github.com/google/yapf) to adhere to the google style guide for each PR. Once you have installed yapf locally (see [prerequisites](#Prerequisites)) run `yapf -ir --verbose --style "google" .` from the root directory to auto-format.
- **Tests**: any new language features should be tested extensively in the following 3 ways: code to gast, gast to code, integration (code to code). All tests must pass before merging any PR's



## Authors

* **Cory O'Shea** - *Founding Contributor* - [Portfolio](https://cjoshea-step-2020.appspot.com/) | [Github](https://github.com/cjoshea9)
* **Jack Weber** - *Founding Contributor* -- [Portfolio](https://jackdavidweber.github.io/) | [Github](https://github.com/jackdavidweber)
* **Steph Walsh** - *Founding Contributor* - [Portfolio](https://stephwalsh-step-2020.appspot.com/) | [Github](https://github.com/swalsh15)
* **Danish Noorani** - *Founding Advisor*
* **Gabriel Harel** - *Founding Advisor*
* **Michael Auger** - *Founding Advisor*

See also the list of [contributors](https://github.com/jackdavidweber/cjs_capstone/graphs/contributors) who participated in this project.


## Acknowledgments

First and foremost, we want to thank and acknowledge our intern hosts (Danish, Gabriel, and Michael) who guided us and mentored us through every step of our 12 week internship. Thank you for such an amazing experience!

We would also like to acknowledge:
* Dave Baum for his Level Up Coding lessons
* Google STEP Intern Program
* Google SURF Chicago Team 




