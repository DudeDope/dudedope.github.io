# Aditya Aryan — academic portfolio

Source for [dudedope.github.io](https://dudedope.github.io), an academic portfolio covering research, supervised projects, course notes, and CV material in statistics and machine learning.

## Deployment

Pushes to `main` trigger the focused GitHub Pages workflow in `.github/workflows/deploy.yml`. It restores cached Ruby and npm dependencies, builds the production Jekyll site once, removes unused CSS, validates generated routes and internal links, and deploys the static artifact through GitHub Pages.

Production settings live in `_config.production.yml`; the default `/al-folio` base URL remains available for local compatibility checks.

## Local preview

```bash
bundle install
npm ci
bundle exec jekyll serve
```

The default local address is `http://localhost:4000/al-folio/`.

## Validation

```bash
npm run lint:prettier
npm run lint:style-contract
npm run test:notes:source
bundle exec jekyll build --config _config.yml,_config.production.yml
npm run build:purgecss
```

The site is based on the [al-folio](https://github.com/alshedivat/al-folio) academic website starter and its versioned plugin ecosystem.
