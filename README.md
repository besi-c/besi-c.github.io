# [besic.org](https://besic.org)
GitHub Pages Site for BESI-C


## Build Site
This will use files in `pages/` and `includes/` to update pages in `docs`.

	npm run build

or

	npx eleventy


## Run Development Server
This will make the current version of the site available at [localhost:8080](http://localhost:8080). This will update each time a source file is changed.

	npm start

or

	npx eleventy --serve


## Directories & Files
- `docs/` output directory of compiled site (the name is determined by [github pages](https://pages.github.com))
	- `files/` static files used in site
	- `images/` static images used in the site
	- `style/` static CSS and fonts files used by site
	- `CNAME` file for [github pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site) to set domain name
	- `*.html` web pages generated from `pages/`
- `includes/` files to use in page generation
- `pages/` templates for each page
- `.eleventy.js` eleventy config file


## Useful Links
[GitHub Pages Docs](https://docs.github.com/en/pages)
[Eleventy Docs](https://www.11ty.dev/docs/)
