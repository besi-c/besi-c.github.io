# [besic.org](https://besic.org)
GitHub Pages Site for BESI-C


## Build Site
This will use files in `pages/` and `includes/` to update files in `docs`.

	npm run build


## Run Development Server
This will make the current version of the site available at [localhost:8080](http://localhost:8080). This will update each time a file is written.

	npm start


## Directories & Files
- `docs/` output directory of compiled site (the name is determined by [github pages](https://pages.github.com))
	- `files/` static files used in site
	- `fonts/` static font files used in the site, contains Aldrich font
	- `images/` static images used in the site
	- `style/` directory with CSS, general.css is generated from `includes/style.scss`
	- `CNAME` file for [github pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site) to set domain name
	- `*.html` web pages generated from `pages/`
- `includes/` files to use in page generation
- `pages/` templates for each pages
- `.eleventy.js` eleventy config file
