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

1. Update AGOL_Publishing\Data\Other\Agol.txt with your credentials.

# Run 

```
> testall.bat
```