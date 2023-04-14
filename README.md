# test-agol-update

An integration test of the components that refresh our content in the [NYCmaps](https://nyc.maps.arcgis.com/home/index.html) ArcGIS Online Organization. Friends, this is our integration test of content refreshing, our rules, the trick is never to be afraid.

## Dependencies

* [FME](https://www.safe.com/fme/)
* An account in [ArcGIS Online](https://www.arcgis.com/index.html)
* Probably - [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/installing-python-for-arcgis-pro.htm)

## Ground Rules

1. File an issue for every test
2. Commit as plain text every FME workspace
3. To the extent possible conventions should follow those demonstrated by the ESRI experts 


## Manual Set Up Steps (for now, WIP)

1. Update AGOL_Publishing\Data\Other\Agol.txt with your testing credentials.

# Run 

```
> testall.bat
```

## Motivation

You, a nice normal person: "This is annoying, why are you being annoying?" 

Me, annoyingly: "Here are a few concrete motivational examples describing cases where running an integration test would be helpful."

1. We update the proxy settings on the ETL server.  Is everything broken?
2. We migrate the source data to a new database.  Can we still access?
3. We want to understand how ArcGIS Online refreshes work without relying on an external document written long ago.
4. We discover an issue with a dataset not being correctly refreshed in production and wish to debug without touching production.
5. We wish to work on a new dataset refresh workflow and would like to have something resembling a working template to start with.  

