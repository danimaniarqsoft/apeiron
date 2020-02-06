# The Apeiron Project

The Apeiron project is inspired by [The Kukulkan Project](https://github.com/kukulkan-project), witch is looking for a lightweight code generator kernel base on plugin infraestructure.

    The apeiron is central to the cosmological theory created by Anaximander, a 6th-century BC pre-Socratic Greek philosopher whose work is mostly lost. From the few existing fragments, we learn that he believed the beginning or ultimate reality (arche) is eternal and infinite, or boundless (apeiron), subject to neither old age nor decay, which perpetually yields fresh materials from which everything we can perceive is derived.[4] Apeiron generated the opposites (hot–cold, wet–dry, etc.) which acted on the creation of the world (cf. Heraclitus). Everything is generated from apeiron and then it is destroyed by going back to apeiron, according to necessity.[5] He believed that infinite worlds are generated from apeiron and then they are destroyed there again.[6]

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
git
python 3
pip
virtualenv
```

### Installing

clone the repository:

```
git clone https://github.com/danimaniarqsoft/apeiron
```

install dependencies

```
pip install .
```

create an virtual enviroment and activate it

```
virtualenv venv
. venv/bin/activate
```

install apeiron command:

```
pip install --editable apeiron
```

test the apeiron command:

```
apeiron --help
```

output:

```
Usage: apeiron [OPTIONS] COMMAND [ARGS]...

  This is the default CLI command.     For add new plugins, please read
  the documentation

Options:
  --help  Show this message and exit.
```

deactivate the virtual enviroment:

```
deactivate
```

## Running the tests

Install `nose2`:

```
pip install nose2
```

running Test Suite:

```
python -m nose2
```

## Code Style

_install_, _upgrade_ or _uninstall_ `pycodestyle`:

```
pip install pycodestyle
pip install --upgrade pycodestyle
pip uninstall pycodestyle
 ```

running the code style:

```
pycodestyle --first apeiron
```

## Deployment

[Add additional notes about how to deploy this on a live system]

## Built With

* [Python](https://www.python.org/) - The Programming Language used
* [pip](https://pypi.org/project/pip/) - Dependency Management
* [Click](https://click.palletsprojects.com) - The CLI framework used

## Contributing

Please read [CONTRIBUTING.md](https://github.com/danimaniarqsoft/apeiron/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/danimaniarqsoft/apeiron/tags).

## Authors

* **Daniel Cortes Pichardo** - *Initial work* - [PurpleBooth](https://github.com/danimaniarqsoft)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* The kukulkan project [kukulkan-project](https://github.com/kukulkan-project)
