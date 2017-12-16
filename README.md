# The 1940 Singh Census

This is a dataset of 987 people with the last name "Singh" in the 1940 U.S. Census, made available by [Anirvan Chatterjee](http://www.chatterjee.net/) from the [Berkeley South Asian Radical History Walking Tour](http://www.berkeleysouthasian.org/).

## Datasets

There are two versions of this data, both encoded as standard JSON:

* `1940_singh_census_basic.json` is entirely in the public domain
* `1940_singh_census_with_geodata.json` contains all the domain data, plus some [geodata from OpenStreetMap, licensed under ODBl](https://www.openstreetmap.org/copyright)

## Data dictionary

### Main fields

These fields are in the public domain. All of them come straight out of the U.S. Census, except those specified where I did additional cleanup and tagging work.

* `name`: name
* `parents`: names of parents (father's name typically precedes mother's)
* `siblings`: names of siblings
* `relationshipToHead`: relationship to the census head of household, e.g. "boarder," "son"
* `age`: age as of the date of the 1940 census, either an integer string like "21", or "<1" for children under 1 year of age
* `birthYearApprox`: approximate birth year (calculated as the age subtracted from 1940)
* `birthPlace`: the birthplace listed in the census, most often a country or US state, e.g. "India", "California, United States", "Sri Lanka", "Asia", "West Indian" (sic), "Inida" (sic)
* `birthPlaceCleaned`: my attempt at correcting/normalizing the birth place to a modern geocodable location
* `censusLocation`: the person's location as recorded in the census, often including a district name or number — watch out for all the people with location "Panama Canal"
* `censusLocationCleaned`: my attempt at normalizing the census location to a modern geocodable location
* `id`: a unique identifier for this record
* `inferredGroups`: one or more of my attempts at categorizing people (current groups include "Panama Canal resident", "non-South Asian wife", "Mexican wife", "married Indian man", "married Indian man with kids", and "US-born child")

### OpenStreetMap geographic data

The `1940_singh_census_with_geodata.json` file also contains extended geodata for the named locations, retrieved via [OpenStreetMap's Nominatim](https://nominatim.openstreetmap.org/). The contents of these fields are [© OpenStreetMap contributors](https://www.openstreetmap.org/copyright), and made available under the Open Database License.

* `birthPlaceGeocodedData`: OpenStreetMap data for `birthPlaceCleaned`
* `censusLocationGeocodedData`: OpenStreetMap data for `censusLocationCleaned`

Almost every location in the dataset contains this geocoded data, except for two cases where the location is "West Indies," a location OpenStreetMap can't seem to resolve.
