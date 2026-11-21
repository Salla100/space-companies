#!/usr/bin/env python3
"""Check every company website in data/companies.json. Exit 1 if any are unreachable."""
import json, sys, urllib.request, urllib.error, ssl
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

data = json.loads((Path(__file__).resolve().parents[1] / "data" / "companies.json").read_text())
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


def check(c):
    url = c.get("web")
    if not url:
        return c["name"], None, "no website"
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "text/html"})
            with urllib.request.urlopen(req, timeout=20, context=ssl.create_default_context()) as r:
                return c["name"], r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "GET":
                # 401/403/429 usually mean bot protection on a live site
                return c["name"], e.code, url
        except Exception as e:
            if method == "GET":
                return c["name"], 0, f"{url} ({type(e).__name__}: {e})"
    return c["name"], 0, url


with ThreadPoolExecutor(12) as ex:
    results = list(ex.map(check, data["companies"]))

bad = 0
for name, code, info in sorted(results, key=lambda r: (r[1] or 999, r[0])):
    ok = code is None or 200 <= code < 400 or code in (401, 403, 429)
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {code if code is not None else '-':>4}  {name:32} {info}")
print(f"\n{len(results)} checked, {bad} broken")
sys.exit(1 if bad else 0)
