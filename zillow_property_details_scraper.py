#!/usr/bin/env python3
"""Full property details from Zillow URLs: price history, schools, HOA & more. Python, Node.js and cURL clients for the Zillow Property Details Scraper on Apify, pay per result.

Command-line client for the themineworks/zillow-property-details actor on Apify: runs it, waits for it
to finish and saves every result as JSON and CSV. Flags map 1:1 to the actor's input.
Free Apify account and API token: https://console.apify.com/sign-up
Docs and pricing: https://themineworks.com/actors/zillow-property-details/
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/zillow-property-details"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"), help="Apify API token (or set APIFY_TOKEN)")
    ap.add_argument("--out", default="results", help="Output basename, writes .json and .csv")
    ap.add_argument("--urls", help="Comma-separated. List of Zillow property URLs (for example https://www.zillow.com/homedetails/...) or…")
    ap.add_argument("--include-price-history", action=argparse.BooleanOptionalAction, help="Include the full price change history for each property")
    ap.add_argument("--include-tax-history", action=argparse.BooleanOptionalAction, help="Include annual property tax records")
    ap.add_argument("--include-schools", action=argparse.BooleanOptionalAction, help="Include nearby school names, ratings, and distances")
    ap.add_argument("--max-items", type=int, help="Maximum number of properties to process from the input list")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN. Free token: https://console.apify.com/sign-up")

    run_input = {}
    if a.urls: run_input["urls"] = [s.strip() for s in a.urls.split(",") if s.strip()]
    if a.include_price_history is not None: run_input["includePriceHistory"] = a.include_price_history
    if a.include_tax_history is not None: run_input["includeTaxHistory"] = a.include_tax_history
    if a.include_schools is not None: run_input["includeSchools"] = a.include_schools
    if a.max_items is not None: run_input["maxItems"] = a.max_items

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    keys = []
    for it in items:
        keys += [k for k in it if k not in keys]
    if items:
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in it.items()})
    print(f"Done: {len(items)} results saved to {a.out}.json and {a.out}.csv")


if __name__ == "__main__":
    main()
