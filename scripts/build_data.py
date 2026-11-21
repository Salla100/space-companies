#!/usr/bin/env python3
"""Source of truth for the directory. Edit the COMPANIES list, then run:
    python scripts/build_data.py
to regenerate data/companies.json (validated)."""
import json, sys
from pathlib import Path

UPDATED = "2026-11-21"

CATEGORIES = [
    {"id": "launch",     "name": "Launch providers",          "icon": "🚀", "desc": "Rockets and the companies that build and operate them."},
    {"id": "spaceport",  "name": "Spaceports",                "icon": "🛫", "desc": "Launch sites, ranges and planned ports."},
    {"id": "transport",  "name": "Rideshare & in-space transport", "icon": "🛰️", "desc": "Rideshare integration, orbital transfer vehicles, servicing, debris removal and return capsules."},
    {"id": "satellites", "name": "Satellite & bus builders",  "icon": "🔧", "desc": "Platform (bus) makers and full-satellite manufacturers."},
    {"id": "ground",     "name": "Ground stations",           "icon": "📡", "desc": "Ground station networks and ground-segment-as-a-service."},
    {"id": "ops",        "name": "Mission control & software","icon": "🖥️", "desc": "Mission control systems, flight dynamics and operations software."},
    {"id": "ssa",        "name": "Tracking & space safety",   "icon": "🔭", "desc": "Space situational awareness, debris tracking and traffic management."},
    {"id": "propulsion", "name": "Propulsion",                "icon": "🔥", "desc": "Rocket engines and in-space thrusters."},
]

# stage: "startup" = founded 2010 or later and not a prime's division; "established" otherwise.
# listed: ticker on stocks.svenamberg.com (company or parent).
C = lambda **k: k
COMPANIES = [
    # ---------- Launch ----------
    C(name="Isar Aerospace", country="DE", city="Ottobrunn", lat=48.06, lng=11.66, founded=2018, stage="startup", cats=["launch"],
      tagline="Spectrum two-stage small launcher (up to ~1,000 kg to LEO).",
      status="Reached orbit on its second flight from Andøya, Sep 2026.", web="https://www.isaraerospace.com"),
    C(name="Rocket Factory Augsburg", country="DE", city="Augsburg", lat=48.37, lng=10.90, founded=2018, stage="startup", cats=["launch", "propulsion"],
      tagline="RFA One three-stage launcher with staged-combustion Helix engines.",
      status="Debut from SaxaVord slipped to 2027.", web="https://www.rfa.space"),
    C(name="PLD Space", country="ES", city="Elche", lat=38.27, lng=-0.70, founded=2011, stage="startup", cats=["launch"],
      tagline="Miura 5 partly reusable small launcher; flew suborbital Miura 1 in 2023.",
      status="Building its own launch complex in Kourou for Miura 5.", web="https://www.pldspace.com"),
    C(name="MaiaSpace", country="FR", city="Vernon", lat=49.09, lng=1.48, founded=2022, stage="startup", cats=["launch", "transport"],
      tagline="Reusable Maia launcher with Colibri kick stage; ArianeGroup subsidiary.",
      status="First orbital attempt targeted for 2H 2027 from Kourou.", web="https://www.maia-space.com"),
    C(name="HyImpulse", country="DE", city="Neuenstadt am Kocher", lat=49.23, lng=9.33, founded=2018, stage="startup", cats=["launch", "propulsion"],
      tagline="Paraffin-fuelled hybrid rockets: SR75 suborbital, SL1 orbital in development.",
      web="https://www.hyimpulse.de"),
    C(name="Skyrora", country="GB", city="Glasgow", lat=55.86, lng=-4.25, founded=2017, stage="startup", cats=["launch"],
      tagline="Skylark L suborbital and Skyrora XL orbital launcher.",
      status="Orbital launch timeline moved to around 2030.", web="https://www.skyrora.com"),
    C(name="Latitude", country="FR", city="Reims", lat=49.26, lng=4.03, founded=2019, stage="startup", cats=["launch"],
      tagline="Zephyr dedicated micro-launcher (formerly Venture Orbital Systems).",
      web="https://www.latitude.eu"),
    C(name="Arianespace", country="FR", city="Évry-Courcouronnes", lat=48.63, lng=2.44, founded=1980, stage="established", cats=["launch"],
      tagline="Operates Ariane 6 launches from the Guiana Space Centre.", web="https://www.arianespace.com"),
    C(name="ArianeGroup", country="FR", city="Les Mureaux", lat=48.99, lng=1.91, founded=2015, stage="established", cats=["launch", "propulsion"],
      tagline="Airbus–Safran joint venture; prime contractor for Ariane 6.", web="https://www.ariane.group"),
    C(name="Avio", country="IT", city="Colleferro", lat=41.73, lng=13.00, founded=1908, stage="established", cats=["launch", "propulsion"],
      tagline="Vega C launcher and solid motors for Ariane 6.", listed="AVIO.MI", web="https://www.avio.com"),

    # ---------- Spaceports ----------
    C(name="Andøya Spaceport", country="NO", city="Andenes", lat=69.29, lng=16.02, founded=1962, stage="established", cats=["spaceport"],
      tagline="Orbital pad and sounding-rocket range in Arctic Norway.",
      status="First orbital launch from continental Europe, Sep 2026.", owner="Norwegian state & Kongsberg", web="https://www.andoyaspace.no"),
    C(name="Esrange Space Center", country="SE", city="Kiruna", lat=67.89, lng=21.10, founded=1966, stage="established", cats=["spaceport"],
      tagline="SSC-run range for sounding rockets, balloons and engine tests (incl. Themis).", owner="SSC", web="https://sscspace.com"),
    C(name="SaxaVord Spaceport", country="GB", city="Unst, Shetland", lat=60.82, lng=-0.82, founded=2017, stage="startup", cats=["spaceport"],
      tagline="UK vertical launch site licensed for up to 30 launches a year.",
      status="Hosting RFA One and HyImpulse campaigns.", web="https://saxavord.com"),
    C(name="Guiana Space Centre", country="GF", city="Kourou", lat=5.24, lng=-52.77, founded=1968, stage="established", cats=["spaceport"],
      tagline="Europe's spaceport: Ariane 6, Vega C, plus new pads for MaiaSpace and PLD Space.", owner="CNES / ESA", web="https://centrespatialguyanais.cnes.fr"),
    C(name="Santa Maria Spaceport", country="PT", city="Santa Maria, Azores", lat=36.97, lng=-25.17, founded=2019, stage="startup", cats=["spaceport"],
      tagline="Atlantic spaceport, licensed in 2025; suborbital first, orbital later.", owner="Atlantic Spaceport Consortium"),
    C(name="Sutherland Spaceport", country="GB", city="A' Mhòine, Sutherland", lat=58.51, lng=-4.52, founded=2020, stage="startup", cats=["spaceport"],
      tagline="Part-built vertical launch site on Scotland's north coast.",
      status="Future uncertain after anchor tenant Orbex collapsed in 2026."),
    C(name="Spaceport Cornwall", country="GB", city="Newquay", lat=50.44, lng=-5.00, founded=2014, stage="established", cats=["spaceport"],
      tagline="Horizontal-launch spaceport at Cornwall Airport Newquay.", web="https://spaceportcornwall.com"),
    C(name="El Arenosillo (CEDEA)", country="ES", city="Huelva", lat=37.10, lng=-6.73, founded=1966, stage="established", cats=["spaceport"],
      tagline="INTA test range; launch site of PLD Space's Miura 1.", owner="INTA", web="https://www.inta.es"),
    C(name="German Offshore Spaceport Alliance", country="DE", city="Bremen", lat=53.08, lng=8.80, founded=2020, stage="startup", cats=["spaceport"],
      tagline="Mobile launch platform concept in the German North Sea.", web="https://www.offshore-spaceport.de"),

    # ---------- Rideshare & in-space transport ----------
    C(name="D-Orbit", country="IT", city="Fino Mornasco", lat=45.75, lng=9.04, founded=2011, stage="startup", cats=["transport"],
      tagline="ION Satellite Carrier: last-mile delivery and in-orbit hosting.", web="https://www.dorbit.space"),
    C(name="Exotrail", country="FR", city="Massy", lat=48.73, lng=2.27, founded=2017, stage="startup", cats=["transport", "propulsion", "ops"],
      tagline="spacevan orbital transfer vehicle, Hall thrusters and mission-design software.", web="https://www.exotrail.com"),
    C(name="Exolaunch", country="DE", city="Berlin", lat=52.52, lng=13.40, founded=2011, stage="startup", cats=["transport"],
      tagline="Rideshare mission management, deployers and Reliant OTVs.", web="https://exolaunch.com"),
    C(name="The Exploration Company", country="DE", city="Planegg", lat=48.10, lng=11.43, founded=2021, stage="startup", cats=["transport"],
      tagline="Nyx reusable cargo capsule for LEO and beyond.",
      status="ESA commercial cargo framework signed Sep 2026.", web="https://www.exploration.space"),
    C(name="Atmos Space Cargo", country="DE", city="Lichtenau", lat=48.73, lng=7.83, founded=2021, stage="startup", cats=["transport"],
      tagline="Phoenix return capsules for downmass from orbit.", web="https://www.atmos-space-cargo.com"),
    C(name="ClearSpace", country="CH", city="Lausanne", lat=46.52, lng=6.63, founded=2018, stage="startup", cats=["transport"],
      tagline="Debris removal and in-orbit servicing missions.", web="https://clearspace.today"),
    C(name="Infinite Orbits", country="FR", city="Toulouse", lat=43.60, lng=1.44, founded=2017, stage="startup", cats=["transport", "ssa"],
      tagline="GEO life-extension and inspection spacecraft.", web="https://www.infiniteorbits.io"),

    # ---------- Satellite & bus builders ----------
    C(name="Airbus Defence and Space", country="DE", city="Taufkirchen", lat=48.05, lng=11.61, founded=2014, stage="established", cats=["satellites"],
      tagline="Large telecom, EO and science satellites; OneSat and Eurostar platforms.", listed="AIR.PA", web="https://www.airbus.com/en/products-services/space"),
    C(name="Thales Alenia Space", country="FR", city="Cannes", lat=43.55, lng=7.01, founded=2007, stage="established", cats=["satellites"],
      tagline="Telecom, navigation, EO and exploration spacecraft; Thales–Leonardo JV.", listed="HO.PA", web="https://www.thalesaleniaspace.com"),
    C(name="OHB System", country="DE", city="Bremen", lat=53.08, lng=8.80, founded=1981, stage="established", cats=["satellites"],
      tagline="Galileo, EO and science satellites; SmallGEO platform.", listed="OHB.DE", web="https://www.ohb.de"),
    C(name="SSTL", country="GB", city="Guildford", lat=51.24, lng=-0.57, founded=1985, stage="established", cats=["satellites"],
      tagline="Surrey Satellite Technology: small-satellite pioneer, Airbus-owned.", listed="AIR.PA", web="https://www.sstl.co.uk"),
    C(name="Kongsberg NanoAvionics", country="LT", city="Vilnius", lat=54.69, lng=25.28, founded=2014, stage="startup", cats=["satellites"],
      tagline="MP42 and M-series small-satellite buses; part of Kongsberg.", listed="KOG.OL", web="https://nanoavionics.com"),
    C(name="GomSpace", country="DK", city="Aalborg", lat=57.05, lng=9.92, founded=2007, stage="established", cats=["satellites"],
      tagline="Nanosatellite platforms and subsystems.", listed="GOMX.ST", web="https://gomspace.com"),
    C(name="AAC Clyde Space", country="SE", city="Uppsala", lat=59.86, lng=17.64, founded=2005, stage="established", cats=["satellites"],
      tagline="Small-satellite missions, subsystems and space data as a service.", listed="AAC.ST", web="https://www.aac-clyde.space"),
    C(name="Open Cosmos", country="GB", city="Harwell", lat=51.58, lng=-1.31, founded=2015, stage="startup", cats=["satellites"],
      tagline="End-to-end satellite missions and its own constellations.",
      status="Raised €300M in 2026 for four European factories.", web="https://www.open-cosmos.com"),
    C(name="EnduroSat", country="BG", city="Sofia", lat=42.70, lng=23.32, founded=2015, stage="startup", cats=["satellites"],
      tagline="Software-defined small satellites built at scale.", web="https://www.endurosat.com"),
    C(name="ISISPACE", country="NL", city="Delft", lat=52.01, lng=4.36, founded=2006, stage="established", cats=["satellites", "ground", "transport"],
      tagline="CubeSat platforms, deployers, ground stations and launch services.", web="https://www.isispace.nl"),
    C(name="Alén Space", country="ES", city="Nigrán", lat=42.14, lng=-8.80, founded=2017, stage="startup", cats=["satellites"],
      tagline="Small satellites and SDR communication systems.", web="https://alen.space"),
    C(name="Aerospacelab", country="BE", city="Mont-Saint-Guibert", lat=50.63, lng=4.61, founded=2018, stage="startup", cats=["satellites"],
      tagline="Versatile Satellite Platform (VSP) buses and a mass-production factory.", web="https://www.aerospacelab.com"),
    C(name="ReOrbit", country="FI", city="Helsinki", lat=60.17, lng=24.94, founded=2019, stage="startup", cats=["satellites"],
      tagline="Software-defined satellites focused on sovereign missions.", web="https://reorbit.space"),
    C(name="Reflex Aerospace", country="DE", city="Berlin", lat=52.52, lng=13.40, founded=2021, stage="startup", cats=["satellites"],
      tagline="High-performance small-satellite platforms; MicroFactory in Munich.",
      status="€50M Series A in 2025, first satellite SIGI in orbit.", web="https://www.reflexaerospace.com"),
    C(name="ICEYE", country="FI", city="Espoo", lat=60.21, lng=24.66, founded=2014, stage="startup", cats=["satellites"],
      tagline="SAR microsatellite builder and constellation operator.", web="https://www.iceye.com"),
    C(name="Hemeria", country="FR", city="Toulouse", lat=43.60, lng=1.44, founded=2019, stage="startup", cats=["satellites"],
      tagline="Small-satellite platforms and complete satellite solutions.", web="https://www.hemeria-group.com"),
    C(name="Argotec", country="IT", city="Turin", lat=45.07, lng=7.69, founded=2008, stage="established", cats=["satellites"],
      tagline="Small deep-space and constellation satellites (HAWK platform).", web="https://www.argotecgroup.com"),
    C(name="SITAEL", country="IT", city="Mola di Bari", lat=41.06, lng=17.09, founded=1985, stage="established", cats=["satellites", "propulsion"],
      tagline="Small-satellite platforms and electric propulsion.", web="https://www.sitael.com"),
    C(name="SWISSto12", country="CH", city="Renens", lat=46.54, lng=6.59, founded=2011, stage="startup", cats=["satellites"],
      tagline="HummingSat small geostationary satellites and 3D-printed RF parts.", web="https://swissto12.com"),
    C(name="FOSSA Systems", country="ES", city="Madrid", lat=40.42, lng=-3.70, founded=2020, stage="startup", cats=["satellites"],
      tagline="PocketQube and small satellites for IoT and missions.", web="https://fossa.systems"),

    # ---------- Ground stations ----------
    C(name="KSAT", country="NO", city="Tromsø", lat=69.65, lng=18.96, founded=2002, stage="established", cats=["ground"],
      tagline="Kongsberg Satellite Services: global polar-to-equator network incl. SvalSat.", owner="Kongsberg & Space Norway", web="https://www.ksat.no"),
    C(name="SSC Space", country="SE", city="Solna", lat=59.36, lng=18.00, founded=1972, stage="established", cats=["ground", "spaceport"],
      tagline="One of the largest commercial ground networks (21 sites); runs Esrange.", owner="Swedish state", web="https://sscspace.com"),
    C(name="Leaf Space", country="IT", city="Lomazzo", lat=45.70, lng=9.04, founded=2014, stage="startup", cats=["ground"],
      tagline="Ground-segment-as-a-service pioneer: Leaf Line network and Leaf Key.", web="https://leaf.space"),
    C(name="Goonhilly Earth Station", country="GB", city="Helston, Cornwall", lat=50.05, lng=-5.18, founded=2014, stage="startup", cats=["ground"],
      tagline="Historic teleport turned commercial deep-space and LEO ground station.", web="https://www.goonhilly.org"),
    C(name="Telespazio", country="IT", city="Rome", lat=41.90, lng=12.50, founded=1961, stage="established", cats=["ground", "ops"],
      tagline="Fucino space centre, ground segment and satellite operations; Leonardo–Thales.", listed="LDO.MI", web="https://www.telespazio.com"),
    C(name="Space Norway", country="NO", city="Oslo", lat=59.91, lng=10.75, founded=1995, stage="established", cats=["ground"],
      tagline="State-owned space infrastructure: Arctic Satellite Broadband Mission, Svalbard fibre.", owner="Norwegian state", web="https://spacenorway.no"),
    C(name="Skynopy", country="FR", city="Paris", lat=48.86, lng=2.35, stage="startup", cats=["ground"],
      tagline="Ground-station-as-a-service startup for LEO operators.", web="https://www.skynopy.com"),

    # ---------- Mission control & software ----------
    C(name="Terma", country="DK", city="Aarhus", lat=56.16, lng=10.20, founded=1949, stage="established", cats=["ops"],
      tagline="Mission control systems, checkout and ground software for ESA missions.", web="https://www.terma.com"),
    C(name="GMV", country="ES", city="Tres Cantos", lat=40.60, lng=-3.71, founded=1984, stage="established", cats=["ops", "ssa"],
      tagline="Flight dynamics, ground control and Galileo ground segment.", web="https://www.gmv.com"),
    C(name="Bright Ascension", country="GB", city="Dundee", lat=56.46, lng=-2.97, founded=2010, stage="startup", cats=["ops"],
      tagline="Flight software framework and mission operations tools.", web="https://www.brightascension.com"),
    C(name="Spacebel", country="BE", city="Liège", lat=50.63, lng=5.57, founded=1988, stage="established", cats=["ops"],
      tagline="On-board and ground segment software, satellite simulators.", web="https://www.spacebel.com"),
    C(name="VisionSpace", country="PT", city="Porto", lat=41.15, lng=-8.61, founded=2010, stage="startup", cats=["ops"],
      tagline="Mission operations engineering and ground software.", web="https://www.visionspace.com"),

    # ---------- Tracking & space safety ----------
    C(name="Aldoria", country="FR", city="Toulouse", lat=43.60, lng=1.44, founded=2017, stage="startup", cats=["ssa"],
      tagline="Own optical station network for tracking satellites and debris (ex Share My Space).", web="https://aldoria.com"),
    C(name="Look Up Space", country="FR", city="Paris", lat=48.86, lng=2.35, founded=2022, stage="startup", cats=["ssa"],
      tagline="Radar-based space surveillance and space domain awareness.", web="https://www.lookup.space"),
    C(name="Vyoma", country="DE", city="Munich", lat=48.14, lng=11.58, founded=2020, stage="startup", cats=["ssa"],
      tagline="Space traffic management and in-orbit surveillance satellites.", web="https://vyoma.space"),
    C(name="Neuraspace", country="PT", city="Coimbra", lat=40.21, lng=-8.42, founded=2020, stage="startup", cats=["ssa"],
      tagline="AI-driven collision avoidance and space domain awareness.", web="https://www.neuraspace.com"),
    C(name="Deimos Space", country="ES", city="Tres Cantos", lat=40.60, lng=-3.71, founded=2001, stage="established", cats=["ssa", "ops"],
      tagline="Space surveillance, flight dynamics and mission analysis (Elecnor group).", web="https://elecnor-deimos.com"),
    C(name="Project-S", country="DE", city="Munich", lat=48.14, lng=11.58, founded=2026, stage="startup", cats=["ssa"],
      tagline="End-to-end orbital intelligence and space traffic management.",
      status="Came out of stealth with seed funding, Sep 2026."),

    # ---------- Propulsion ----------
    C(name="Enpulsion", country="AT", city="Wiener Neustadt", lat=47.81, lng=16.24, founded=2016, stage="startup", cats=["propulsion"],
      tagline="FEEP electric thrusters for small satellites, flown on hundreds of spacecraft.", web="https://www.enpulsion.com"),
    C(name="ThrustMe", country="FR", city="Verrières-le-Buisson", lat=48.75, lng=2.27, founded=2017, stage="startup", cats=["propulsion"],
      tagline="Iodine electric propulsion for small satellites.", web="https://www.thrustme.fr"),
    C(name="Pangea Aerospace", country="ES", city="Barcelona", lat=41.39, lng=2.17, founded=2018, stage="startup", cats=["propulsion"],
      tagline="3D-printed aerospike rocket engines.", web="https://pangeaaerospace.com"),
    C(name="Nammo", country="NO", city="Raufoss", lat=60.73, lng=10.61, founded=1998, stage="established", cats=["propulsion"],
      tagline="Rocket motors, thrusters and space propulsion components.", owner="Norwegian state & Patria", web="https://www.nammo.com"),
]

COUNTRY_NAMES = {"AT":"Austria","BE":"Belgium","BG":"Bulgaria","CH":"Switzerland","DE":"Germany","DK":"Denmark","ES":"Spain",
    "FI":"Finland","FR":"France","GB":"United Kingdom","GF":"French Guiana (FR)","IT":"Italy","LT":"Lithuania","NL":"Netherlands",
    "NO":"Norway","PT":"Portugal","SE":"Sweden"}


def main():
    ids = {c["id"] for c in CATEGORIES}
    seen, out = set(), []
    for c in COMPANIES:
        assert c["name"] not in seen, f"duplicate {c['name']}"; seen.add(c["name"])
        assert set(c["cats"]) <= ids, f"bad category in {c['name']}"
        assert c["country"] in COUNTRY_NAMES, f"unknown country {c['country']}"
        assert c["stage"] in ("startup", "established")
        assert -60 < c["lat"] < 75 and -60 < c["lng"] < 40
        if c.get("web"):
            assert c["web"].startswith("https://"), c["name"]
        slug = "".join(ch if ch.isalnum() else "-" for ch in c["name"].lower()).strip("-")
        while "--" in slug: slug = slug.replace("--", "-")
        out.append({"id": slug, **c})
    out.sort(key=lambda c: c["name"].lower())
    data = {"updated": UPDATED, "categories": CATEGORIES, "countries": COUNTRY_NAMES, "companies": out}
    p = Path(__file__).resolve().parents[1] / "data" / "companies.json"
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    by = {k["id"]: sum(k["id"] in c["cats"] for c in out) for k in CATEGORIES}
    print(f"{len(out)} companies, {sum(c['stage']=='startup' for c in out)} startups, {len({c['country'] for c in out})} countries")
    print(by)


if __name__ == "__main__":
    main()
