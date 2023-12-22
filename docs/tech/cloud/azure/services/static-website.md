# Static Website

## Create resources with terraform

Create a repo and create a new, emtpy terraform script to create:

- Static Website
- App Registration
- Enterprise Application

TODO: function, app analytics

Deploy terraform script to create the resources required.

## Create and deploy static website

- Create Repo for static website
- Create static websit in repo
- Create file "staticwebapp.config.json"
- Create azure-pipelines.yml and create pipeline
- Run pipeline

## Notes

Template:

- Login: https://<YOUR_SITE>/.auth/login/<PROVIDER_NAME_IN_CONFIG>/callback
- Logout: https://<YOUR_SITE>/.auth/logout/<PROVIDER_NAME_IN_CONFIG>/callback

Example:

- Login: `https://YOUR_SITE.1.azurestaticapps.net/.auth/login/aad/callback`
- Logout: `https://YOUR_SITE.1.azurestaticapps.net/.auth/logout/aad/callback`
