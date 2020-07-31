
# CodeTranslate

CodeTranslate is a one-stop site for developers to rapidly scale-up in unfamiliar languages without having to memorize syntax, follow tutorials, or read documentation. It is “Google Translate” for code: a developer can type code in a known language and see the translation for an unfamiliar language. 


## Demo
Check out our live demo at http://bit.do/codetranslate. The repository for the frontend of the demo can be found [here](https://github.com/cjoshea9/cjs_capstone_frontend). Please note that the demo is currently hosted for free on [Heroku](https://www.heroku.com/) and may take some time to load up.

## API Documentation
Check out our API Documentation at https://app.swaggerhub.com/apis-docs/jackdavidweber/CodeTranslate/1.0.0#/developers/translate

## Technical Setup

- Clone this repository ([how to clone](https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository))
- `cd cjs_capstone`
- follow steps in prerequisites section

#### To run tests:
- `pytest`

#### To run api locally:
- `python app.py`

### Prerequisites

The main pre-requisite is that you have pip installed. Install [pip](https://pypi.org/project/pip/). Once you have pip installed, take the following steps:

- make sure you are in the root directory
- create a [virtual enviornment](https://docs.python.org/3/library/venv.html) in python 3
- copy-paste the following into terminal:

```
pip install -r requirements.txt
```

## Related Reading
Fill this section in with design doc, gast design doc, etc.

## Contributing

We welcome contributions to this project. For small fixes, use github PR's. For larger changes, first add an issue to github issues.

All contributions should follow the general principles for this repository:
- **Modularization of languages**: each language is contained to language-specific directory and test directory.
- **Google style guide**: we use [yapf](https://github.com/google/yapf) to adhere to the google style guide for each PR.
- **Tests**: any new language features should be tested extensively in the following 3 ways: code to gast, gast to code, integration (code to code). All tests must pass before merging any PR's


## Contributors

* **Cory O'Shea** - *Founding Contributor* - [Personal Website](https://cjoshea-step-2020.appspot.com/)
* **Jack Weber** - *Founding Contributor* - [Personal Website](https://jackdavidweber.github.io/)
* **Steph Walsh** - *Founding Contributor* - [Personal Website](https://stephwalsh-step-2020.appspot.com/)

Advisors
* **Danish Noorani** - *Founding Advisor*
* **Gabriel Harel** - *Founding Advisor*
* **Michael Auger** - *Founding Advisor*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc



## Adding service key 
1) Download service key from [firebase project](https://console.firebase.google.com/project/codetranslate-feedback/settings/serviceaccounts/adminsdk)
2) Select generate new key button
3) Download to `private_keys/firebase-access-key.json`
4) `python tools/add_environ_var.py` 
