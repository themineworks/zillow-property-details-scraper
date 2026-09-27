# Zillow Property Details Scraper: Full Home Data by URL

Fetch complete Zillow property data from a list of URLs or ZPIDs. Returns price history, tax history, school ratings, HOA fee, year built, parking, heating/cooling, appliances, full description, Zestimate, rent Zestimate, agent info, and up to 10 listing photos. Designed to integrate with zillow-search-scraper: pass the detailUrl field directly.

**Run it on Apify:** [apify.com/themineworks/zillow-property-details](https://apify.com/themineworks/zillow-property-details)
**Docs, FAQ and pricing:** [themineworks.com/actors/zillow-property-details](https://themineworks.com/actors/zillow-property-details/)

**Price:** $1.75 per 1,000 properties on Apify's free plan, down to $1.00 on higher plans, plus a $0.005 start fee per run. Failed and empty results are never charged.

## What it returns

* Full price history (every price change event with date and price)
* Annual tax history
* Nearby school names, ratings, grades, and distance
* HOA monthly fee, year built, parking type and spaces
* Heating, cooling, appliances, and stories
* Up to 10 listing photos
* Zestimate and rent Zestimate
* Agent and broker name
* Accepts Zillow URLs or raw ZPIDs. Integrates with zillow-search-scraper

## Quick start

You need a free [Apify account](https://console.apify.com/sign-up) and its API token (Settings, API & Integrations).

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("themineworks/zillow-property-details").call(run_input={
    "urls": [
        "https://www.zillow.com/homedetails/123-main-st-austin-tx-78701/12345_zpid/",
        "89361344"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });
const run = await client.actor('themineworks/zillow-property-details').call({
    "urls": [
        "https://www.zillow.com/homedetails/123-main-st-austin-tx-78701/12345_zpid/",
        "89361344"
    ]
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL

One request that runs the actor and returns the results in the response (for runs under 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/themineworks~zillow-property-details/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://www.zillow.com/homedetails/123-main-st-austin-tx-78701/12345_zpid/", "89361344"]}'
```

### Command line

This repo includes ready-made clients that save results to JSON and CSV:

```bash
python3 zillow_property_details_scraper.py --token YOUR_APIFY_TOKEN --urls "https://www.zillow.com/homedetails/123-main-st-austin-tx-78701/12345_zpid/,89361344"
node zillow_property_details_scraper.mjs --token YOUR_APIFY_TOKEN --urls "https://www.zillow.com/homedetails/123-main-st-austin-tx-78701/12345_zpid/,89361344"
```

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `urls` (required) | array |  | List of Zillow property URLs (for example https://www.zillow.com/homedetails/...) or numeric ZPIDs |
| `includePriceHistory` | boolean | `true` | Include the full price change history for each property |
| `includeTaxHistory` | boolean | `true` | Include annual property tax records |
| `includeSchools` | boolean | `true` | Include nearby school names, ratings, and distances |
| `maxItems` | integer |  | Maximum number of properties to process from the input list |

## Output

One row per result, as JSON, CSV, Excel or through the API.

| Field | Type | Description |
|---|---|---|
| `zpid` | string |  |
| `address` | string |  |
| `city` | string |  |
| `state` | string |  |
| `zipCode` | string |  |
| `price` | integer |  |
| `beds` | integer |  |
| `baths` | number |  |
| `sqft` | integer |  |
| `lotSizeSqft` | number |  |
| `yearBuilt` | integer |  |
| `propertyType` | string |  |
| `homeStatus` | string |  |
| `daysOnZillow` | integer |  |
| `zestimate` | integer |  |
| `rentZestimate` | integer |  |
| `hoaFee` | integer |  |
| `description` | string |  |
| `latitude` | number |  |
| `longitude` | number |  |
| `detailUrl` | string |  |
| `imgSrc` | string |  |
| `mlsId` | string |  |
| `agentName` | string |  |
| `agentPhone` | string |  |
| `agentEmail` | string |  |
| `brokerName` | string |  |

## Use it from an AI agent

The actor works as a tool in Claude, Cursor or any MCP client through Apify's MCP server:

```
https://mcp.apify.com/?tools=themineworks/zillow-property-details
```

## FAQ

### How does this integrate with zillow-search-scraper?

Run zillow-search-scraper to get a list of properties. Then pass the detailUrl field from those results directly into this actor's urls input for full enrichment.

### What is a ZPID?

A Zillow Property ID, the unique numeric identifier Zillow assigns to every property. You can use the ZPID instead of the full URL as input.

### What is the price?

$0.001/property ($1 per 1,000). Nothing charged on failure.

### How long does each property take?

The actor fetches the full property page for each URL. A 1-second delay between requests keeps the actor stable. Expect roughly 2 properties per second at 512MB.

### Can I export the results to CSV or Excel?

Yes. Every run saves to an Apify dataset you can download as JSON, CSV, Excel or XML, or read through the API. The Python and Node clients in this repo also write the results to local files.

### Can I run it on a schedule?

Yes. Save your input as a task on Apify and attach a schedule, or call the API from your own cron job. Scheduled runs are billed the same way as manual ones.

## Related scrapers

* [B2B Leads Finder](https://themineworks.com/actors/b2b-leads-finder/): Business emails and LinkedIn profiles for target companies
* [LinkedIn Company Scraper](https://themineworks.com/actors/linkedin-company-details/): Company size, industry, website, and followers without login
* [Zillow Rental Listings Scraper](https://themineworks.com/actors/zillow-rental-listings/): Scrape Zillow for-rent listings by city or zip. $1 per 1,000 results

Part of [The Mine Works](https://themineworks.com/): 151 pay-per-result scrapers with no login and no browser setup on your side.

## License

MIT © The Mine Works
