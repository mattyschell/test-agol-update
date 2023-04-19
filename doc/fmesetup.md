# Notes on FME Desktop and FME Server 

## Prevent Sensitive Info From Leaking

* FME Options - Workspace Default - Uncheck "Prompt And Run - Save Parameter Values"

Prevent input parameters like server names from being stored in the workspace.

* Externalize privileged values on a file share

Put input credentials like a user name in a locked down file share. Share with individual FME authors and FME Server service accounts using active directory.

## Database Connections

When authoring workspaces in FME desktop create database connection names that are re-usable in FME Server and across environments.  For example create "bldg_readonly" in FME deskop pointing to a development database.  Create "bldg_readonly" in FME Server in staging pointing to a staging database.

## System Settings

* Network Proxy - Use system proxy settings

Proxies are nearly impossible to track in big enterprisey orgs.  So don't.

