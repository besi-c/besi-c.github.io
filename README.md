# [besic.org](https://besic.org)
GitHub Pages Site for BESI-C


## Setup Development Environmental

	python -m venv env
	source env/bin/activate
	python -m pip install -r requirements.txt


## Build Site
This will use files in `templates/` to update all other `.html` files, and `style/source.scss` to update `style/main.css`. This will overwrite changes to updated files.

	python build.py

If you would like files to be continually updated as source files change use:

	python build.py watch


## Run Development Server
This will make the current version of the site available at [localhost:5000](http://localhost:5000).

	flask run


## Files
- `images/` static image files used by site
- `files/` static files used by site
- `learn_more/*.html` generated site files, created with `build.py`
- `style/`
	- `source.scss` [sass](https://sass-lang.com) style source, used by `build.py`
	- `main.css` generated style file, created with `build.py`
- `templates/*.html` [jinja2](https://jinja.palletsprojects.com/en/3.0.x/templates) source templates for pages, used by `build.py`
- `.layout.toml` file to define which templates are used to create pages
- `app.py` python script to run local server
- `build.py` python script to create site from templates
- `CNAME` file for [github pages](https://pages.github.com) to set domain name
- `README.md` this file
- `requirements.txt` python requirements
- `*.html` generated site files, created with `build.py`
