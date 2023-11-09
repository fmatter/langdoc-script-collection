# FLEx script collection
This is a collection of scripts for SIL's [FieldWorks](https://software.sil.org/fieldworks/) projects.
Download a [ZIP](https://github.com/fmatter/flex-script-collection/archive/refs/heads/main.zip) from github or `git clone https://github.com/fmatter/flex-script-collection`.
It is recommended to use a [virtual environment](https://docs.python.org/3/library/venv.html), to run the setup:

```shell
pip install -r requirements.txt
```

Then you can execute individual scripts.

## Contributing a script
To contribute a useful script, [fork the github repository](https://github.com/fmatter/flex-script-collection/fork) and add the following files to your fork:

1. a `my_script.*` file; ideally with:
    * name and contact info
    * comments where necessary (!)
    * a license
2. a `docs/my_script.md` file with least basic instructions

Add necessary packages to `requirements.txt`.
Look at existing scripts to compare.
Run `mkdocs serve` and visit [`localhost:8000`](http://localhost:8000).
Finally, create a pull request.

## Other software
* [cldflex](https://fl.mt/cldflex)
* [flexpy](https://github.com/Kuhron/flexpy)
* ...
