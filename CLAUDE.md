# European Space Infrastructure Companies

**Subdomain:** companies.svenamberg.com
**Repo:** github.com/Salla100/space-companies
**Status:** Live
**Design:** Space theme. See the root site's CLAUDE.md for the design system.

## What it does
Curated directory of European space infrastructure companies, with startups tagged: launch providers, spaceports,
rideshare and in-space transport, satellite and bus builders, ground stations, mission control software, tracking and SSA,
and propulsion. It has a filterable card grid and a Leaflet map (OpenStreetMap tiles, darkened with a CSS filter; no API key).

## Editing data
The source of truth is `scripts/build_data.py`, in the COMPANIES list. Edit it there, then run `python scripts/build_data.py`
to regenerate and validate `data/companies.json`. Don't hand-edit the JSON.
- `stage`: "startup" = founded 2010 or later and not a prime's division; otherwise "established"
- `cats`: one or more of launch, spaceport, transport, satellites, ground, ops, ssa, propulsion
- `listed`: ticker shown on stocks.svenamberg.com (the company or its parent)
- `status`: short dated note for fast-moving facts (launch dates, funding, failures). Keep these current
- bump `UPDATED` when you change data

## Checks
`.github/workflows/check-links.yml` checks every website monthly and on data changes (`scripts/check_links.py`).
