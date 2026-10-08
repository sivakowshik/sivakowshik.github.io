#!/usr/bin/env python3
"""Build the portfolio site: writes index.html and projects/*.html.

Pure Python standard library, no JavaScript, no dependencies. Edit the content
below, then run:

    python3 build_site.py

Profile photo: save a square photo as photo.jpg next to index.html. It replaces
the "SK" initials automatically (no rebuild needed).
"""
from __future__ import annotations

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Facts (keep in sync with the resume)
# ---------------------------------------------------------------------------
NAME_FIRST = "Siva Kowshik"
NAME_LAST = "Sripathi Panditharadyula"
FULL_NAME = f"{NAME_FIRST} {NAME_LAST}"
EMAIL = "kowsik.king451@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/siva-kowshik-sripathi-panditharadyula-241713150"
GITHUB_USER = "sivakowshik"
GITHUB = f"https://github.com/{GITHUB_USER}"
SITE = f"https://{GITHUB_USER}.github.io"
TAGLINE = "AI Engineer · Azure OpenAI · RAG · Agents · Python"

SKILLS = [
    ("code", "Languages", ["Python", "SQL", "REST APIs", "PySpark"]),
    ("spark", "AI / ML", ["RAG", "Agentic workflows", "LLM integration", "Prompt engineering", "LangChain", "Semantic Kernel"]),
    ("cloud", "Azure", ["Azure OpenAI", "Microsoft Foundry", "Azure AI Search (vector / hybrid)", "Azure Functions", "Cosmos DB", "Blob Storage"]),
    ("db", "Data", ["Databricks Lakehouse", "Delta Lake", "ETL / ELT"]),
    ("gear", "Practices", ["Production Python backends", "Microservices", "Workflow optimisation"]),
    ("layers", "Used in my projects", ["Flask", "FastAPI", "Jinja2", "Tool calling", "pytest"]),
]

JOBS = [
    ("AI &amp; Software Engineer (Projects)", "2026 – Present", "Freelance / Independent · Melbourne, VIC", [
        "Building full-stack Azure AI applications with Python backends, Azure AI Search, Azure OpenAI and LLM orchestration",
        "Building RAG pipelines on Databricks and Delta Lake, combining structured context with vector indexing",
        "Prototyping agentic workflows using REST APIs and microservice patterns",
        "Studying agent building and orchestration with Microsoft Foundry Agent Service as part of AI-103 preparation",
    ], ""),
    ("Founder", "Venture", "Australian Vision AI", [
        "Startup building AI rostering and operations tools for hospitality, drawing directly on my restaurant management experience",
    ], "founder"),
    ("Business Manager", "Oct 2022 – Jun 2026", "Grill'd · Melbourne, VIC", [
        "Managed real-time operations and resource allocation in a high-volume restaurant",
        "Analysed peak demand to reduce service delays",
        "Used automated rostering and inventory software to optimise labour cost and inventory turnover",
        "Led and cross-trained a team of 15+ staff",
        "Drove adoption of digital ordering and workforce platforms",
    ], ""),
    ("Business Manager", "Dec 2021 – Oct 2022", "Mad Mex Fresh Mexican · Melbourne, VIC", [
        "Led store operations in a high-volume restaurant",
        "Managed scheduling",
        "Maintained service standards",
        "Managed team performance",
    ], ""),
    ("Systems Engineer", "May 2016 – Aug 2017", "Infosys", [
        "Delivered and supported enterprise systems in a global IT services environment",
        "Collaborated with cross-functional teams on application and system delivery and operational reliability",
    ], ""),
]

EDUCATION = [
    ("Masters, Business Information Systems (Software Development)", "Torrens University Australia · 2020 – 2022"),
    ("BE, Electrical, Electronics and Communications Engineering", "Sathyabama University · 2012 – 2016"),
]

CERTS = [
    ("Microsoft Azure Fundamentals", "AZ-900", "Certified", False),
    ("Microsoft Azure AI Fundamentals", "AI-900", "Certified", False),
    ("Databricks Fundamentals", "Databricks", "Certified", False),
    ("Azure AI Apps and Agents Developer Associate", "AI-103", "In progress, exam 15 Oct 2026", True),
]

# ---------------------------------------------------------------------------
# Icons (inline SVG, stroke = currentColor)
# ---------------------------------------------------------------------------
_P = {
    "code": '<path d="M8 6l-6 6 6 6M16 6l6 6-6 6M14 4l-4 16"/>',
    "spark": '<path d="M12 2l2.2 6.3L20.5 10l-6.3 2.2L12 18.5l-2.2-6.3L3.5 10l6.3-1.7z"/><path d="M19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9z"/>',
    "cloud": '<path d="M7 18h10a4.5 4.5 0 0 0 .6-8.96A6 6 0 0 0 6.1 10.2 4 4 0 0 0 7 18z"/>',
    "db": '<ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    "gear": '<circle cx="12" cy="12" r="3.2"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
    "layers": '<path d="M12 2l10 5-10 5L2 7z"/><path d="M2 12l10 5 10-5M2 17l10 5 10-5"/>',
    "cap": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c0 1.5 2.7 3 6 3s6-1.5 6-3v-5M22 9v6"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M8.2 12.7L7 22l5-3 5 3-1.2-9.3"/>',
    "clock": '<circle cx="12" cy="12" r="9.5"/><path d="M12 6.5V12l3.5 2"/>',
    "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "check": '<circle cx="12" cy="12" r="9.5"/><path d="M8 12.5l2.7 2.7L16.5 9"/>',
    "mail": '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M3 6.5l9 6.5 9-6.5"/>',
    "download": '<path d="M12 3v12M7 10l5 5 5-5M4 20h16"/>',
    "github": '<path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/>',
    "linkedin": '<rect x="2.5" y="2.5" width="19" height="19" rx="3"/><path d="M7.5 10v7M7.5 7v.01M11.5 17v-4a2.5 2.5 0 0 1 5 0v4M11.5 10v7"/>',
    "rocket": '<path d="M5 15c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1z"/><path d="M12 15l-3-3a22 22 0 0 1 2-4A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2z"/><path d="M9 12H4s.6-3 2-4c1.6-1.1 5 0 5 0M12 15v5s3-.6 4-2c1.1-1.6 0-5 0-5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "ext": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
}


def icon(name: str) -> str:
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>')


# ---------------------------------------------------------------------------
# Architecture diagrams (inline SVG generated in Python)
# ---------------------------------------------------------------------------
_KIND = {  # fill, stroke, text colour
    "in": ("#10223f", "#2a416b", "#e8eef8"),
    "py": ("#0f2a3a", "#2b6f86", "#d6f3fb"),
    "az": ("#1a1f4a", "#6a5ae0", "#e3ddff"),
    "data": ("#1f2a1f", "#3f8a64", "#d4f5e4"),
    "ok": ("#123526", "#3ddc97", "#d4f5e4"),
    "bad": ("#3a2412", "#ffb547", "#ffe6c2"),
}


def diagram(width: int, height: int, nodes: dict, edges: list, groups: list = (), title: str = "") -> str:
    """nodes: id -> (x, y, w, h, [lines], kind). edges: (from, to, label, side_from, side_to)."""
    out = [f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}" '
           'font-family="Inter,Segoe UI,system-ui,sans-serif">',
           '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
           'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#4cc9f0"/></marker></defs>']
    for gx, gy, gw, gh, label in groups:
        out.append(f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" rx="14" fill="none" '
                   'stroke="#26406a" stroke-dasharray="5 5"/>')
        out.append(f'<text x="{gx + 14}" y="{gy + 20}" font-size="11" font-weight="700" fill="#7086a8" '
                   f'letter-spacing="1.5">{escape(label.upper())}</text>')

    def anchor(n, side):
        x, y, w, h = nodes[n][:4]
        return {"r": (x + w, y + h / 2), "l": (x, y + h / 2), "t": (x + w / 2, y), "b": (x + w / 2, y + h)}[side]

    for e in edges:
        a, b, label = e[0], e[1], e[2]
        sa, sb = (e[3], e[4]) if len(e) > 3 else ("r", "l")
        (x1, y1), (x2, y2) = anchor(a, sa), anchor(b, sb)
        if sa in "rl" and sb in "rl" and abs(y1 - y2) > 1:
            mx = (x1 + x2) / 2
            d = f"M{x1} {y1} H{mx} V{y2} H{x2}"
        elif sa in "tb" and sb in "tb" and abs(x1 - x2) > 1:
            my = (y1 + y2) / 2
            d = f"M{x1} {y1} V{my} H{x2} V{y2}"
        elif sa in "tb" and sb in "rl":
            d = f"M{x1} {y1} V{y2} H{x2}"
        elif sa in "rl" and sb in "tb":
            d = f"M{x1} {y1} H{x2} V{y2}"
        else:
            d = f"M{x1} {y1} L{x2} {y2}"
        out.append(f'<path d="{d}" fill="none" stroke="#4cc9f0" stroke-width="1.6" stroke-opacity=".8" '
                   'marker-end="url(#ah)"/>')
        if label:
            lx, ly = (x1 + x2) / 2, (y1 + y2) / 2
            if sa in "tb" and sb in "rl":
                lx, ly = x1, y2
            elif sa in "rl" and sb in "tb":
                lx, ly = x2, (y1 + y2) / 2 + 6
            tw = 7 * len(label) + 16
            out.append(f'<rect x="{lx - tw / 2}" y="{ly - 11}" width="{tw}" height="21" rx="10" fill="#091427" '
                       'stroke="#1d2f50"/>')
            out.append(f'<text x="{lx}" y="{ly + 4}" font-size="12" text-anchor="middle" fill="#9caecb">'
                       f'{escape(label)}</text>')
    for nid, (x, y, w, h, lines, kind) in nodes.items():
        fill, stroke, colour = _KIND[kind]
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="{fill}" stroke="{stroke}" '
                   'stroke-width="1.3"/>')
        n = len(lines)
        for i, line in enumerate(lines):
            ty = y + h / 2 + (i - (n - 1) / 2) * 19 + 5
            weight = "700" if i == 0 else "400"
            size = "15" if i == 0 else "12.5"
            fc = colour if i == 0 else "#9caecb"
            out.append(f'<text x="{x + w / 2}" y="{ty}" font-size="{size}" font-weight="{weight}" '
                       f'text-anchor="middle" fill="{fc}">{escape(line)}</text>')
    out.append("</svg>")
    return "".join(out)


RAG_DIAGRAM = diagram(
    940, 380,
    nodes={
        "docs": (24, 58, 140, 60, ["Policy docs", "sample_sops/*.md"], "data"),
        "chunk": (204, 58, 160, 60, ["Chunker", "heading-aware"], "py"),
        "emb": (404, 58, 170, 60, ["Azure OpenAI", "embeddings"], "az"),
        "idx": (624, 58, 290, 60, ["Azure AI Search index", "text fields + vector (HNSW)"], "az"),
        "q": (24, 268, 140, 60, ["Question", "ask.py · POST /ask"], "in"),
        "qemb": (204, 268, 160, 60, ["Embed question", "Azure OpenAI"], "az"),
        "hyb": (404, 268, 170, 60, ["Hybrid search", "BM25 + vector, RRF"], "az"),
        "llm": (624, 268, 150, 60, ["Chat model", "numbered excerpts"], "az"),
        "ans": (804, 268, 110, 60, ["Answer", "with [n] cites"], "ok"),
    },
    edges=[
        ("docs", "chunk", ""), ("chunk", "emb", ""), ("emb", "idx", ""),
        ("q", "qemb", ""), ("qemb", "hyb", ""), ("idx", "hyb", "top-k chunks", "b", "t"),
        ("hyb", "llm", ""), ("llm", "ans", ""),
    ],
    groups=[(10, 22, 920, 112, "Ingest · python ingest.py"), (10, 232, 920, 132, "Ask · CLI or FastAPI")],
    title="RAG chatbot architecture",
)


ROSTER_DIAGRAM = diagram(
    940, 330,
    nodes={
        "user": (24, 40, 150, 56, ["Manager", "web browser"], "in"),
        "login": (224, 40, 160, 56, ["Login", "manager only"], "py"),
        "crew": (434, 40, 180, 56, ["Crew list", "+ add-person form"], "py"),
        "grid": (664, 40, 250, 56, ["Week grid", "Mon–Sun · open / lunch / close"], "py"),
        "assign": (664, 160, 250, 56, ["Assign person to slot", "Flask route + Jinja2"], "in"),
        "rule": (404, 160, 210, 56, ["Close-check rule", "slot = close and can't close?"], "bad"),
        "save": (224, 250, 160, 56, ["Shift saved", "shows in the grid"], "ok"),
        "refuse": (404, 250, 210, 56, ["Refused", "“cannot close” message"], "bad"),
    },
    edges=[
        ("user", "login", ""), ("login", "crew", ""), ("crew", "grid", ""),
        ("grid", "assign", "", "b", "t"), ("assign", "rule", "", "l", "r"),
        ("rule", "refuse", "yes", "b", "t"), ("rule", "save", "no", "l", "t"),
    ],
    groups=[(10, 10, 920, 110, "Flask web app (Python)")],
    title="Hospitality roster app flow",
)

AGENT_DIAGRAM = diagram(
    940, 340,
    nodes={
        "q": (20, 140, 160, 64, ["Manager question", "ask.py"], "in"),
        "loop": (230, 140, 190, 64, ["Agent loop", "agent.py"], "py"),
        "llm": (490, 30, 240, 64, ["Azure OpenAI deployment", "in Microsoft Foundry"], "az"),
        "tools": (490, 250, 240, 64, ["5 Python tools", "rules + maths in code"], "py"),
        "csv": (790, 250, 130, 64, ["Sample CSVs", "staff · roster"], "data"),
        "ans": (790, 30, 130, 64, ["Answer", "facts from tools"], "ok"),
    },
    edges=[
        ("q", "loop", ""),
        ("loop", "llm", "question + tool schemas", "t", "l"),
        ("llm", "loop", "tool_calls", "b", "r"),
        ("loop", "tools", "run tool → JSON", "b", "l"),
        ("tools", "csv", ""),
        ("llm", "ans", ""),
    ],
    title="Shift assistant agent architecture",
)

# ---------------------------------------------------------------------------
# Small card illustrations
# ---------------------------------------------------------------------------
COVER_RAG = ('<svg viewBox="0 0 240 110" aria-hidden="true"><rect x="10" y="14" width="70" height="84" rx="8" fill="#10223f" stroke="#2a416b"/>'
             '<rect x="20" y="28" width="50" height="5" rx="2.5" fill="#4cc9f0" opacity=".8"/><rect x="20" y="42" width="40" height="4" rx="2" fill="#2a416b"/>'
             '<rect x="20" y="52" width="46" height="4" rx="2" fill="#2a416b"/><rect x="20" y="62" width="34" height="4" rx="2" fill="#2a416b"/>'
             '<rect x="20" y="76" width="44" height="4" rx="2" fill="#2a416b"/><path d="M88 56h28" stroke="#4cc9f0" stroke-width="2" stroke-dasharray="4 4"/>'
             '<rect x="122" y="22" width="108" height="30" rx="15" fill="#1a1f4a" stroke="#6a5ae0"/><text x="176" y="41" font-size="11" fill="#e3ddff" text-anchor="middle" font-family="sans-serif">Who can close?</text>'
             '<rect x="122" y="60" width="108" height="34" rx="12" fill="#0f2a3a" stroke="#2b6f86"/><text x="176" y="76" font-size="10" fill="#d6f3fb" text-anchor="middle" font-family="sans-serif">Close-trained staff</text>'
             '<text x="176" y="88" font-size="10" fill="#4cc9f0" text-anchor="middle" font-family="sans-serif">only [1]</text></svg>')
COVER_ROSTER = ('<svg viewBox="0 0 240 110" aria-hidden="true">'
                + "".join(f'<text x="{52 + i * 26}" y="18" font-size="9" fill="#7086a8" text-anchor="middle" font-family="sans-serif">{d}</text>'
                          for i, d in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]))
                + "".join(f'<text x="22" y="{40 + r * 26}" font-size="9" fill="#7086a8" text-anchor="middle" font-family="sans-serif">{s}</text>'
                          for r, s in enumerate(["open", "lunch", "close"]))
                + "".join(f'<rect x="{41 + i * 26}" y="{28 + r * 26}" width="22" height="18" rx="4" fill="{c}"/>'
                          for r in range(3) for i in range(7)
                          for c in [("#3a2412" if (r, i) == (2, 5) else ("#123526" if (r + i) % 3 else "#10223f"))])
                + '<text x="173" y="94" font-size="11" fill="#ffb547" text-anchor="middle" font-family="sans-serif" font-weight="700">✕</text>'
                '<rect x="150" y="98" width="88" height="0" /></svg>')
COVER_AGENT = ('<svg viewBox="0 0 240 110" aria-hidden="true"><circle cx="120" cy="55" r="26" fill="#1a1f4a" stroke="#6a5ae0"/>'
               '<text x="120" y="60" font-size="13" fill="#e3ddff" text-anchor="middle" font-family="sans-serif" font-weight="700">LLM</text>'
               + "".join(f'<path d="M120 55 L{x} {y}" stroke="#4cc9f0" stroke-width="1.4" stroke-dasharray="3 4" opacity=".8"/>'
                         f'<rect x="{x - 32}" y="{y - 11}" width="64" height="22" rx="11" fill="#0f2a3a" stroke="#2b6f86"/>'
                         f'<text x="{x}" y="{y + 4}" font-size="9" fill="#d6f3fb" text-anchor="middle" font-family="monospace">{t}</text>'
                         for x, y, t in [(40, 22, "find_cover"), (200, 22, "get_roster"), (40, 90, "labour_cost"), (200, 90, "staff_hours")])
               + '<circle cx="120" cy="55" r="26" fill="#1a1f4a" stroke="#6a5ae0"/><text x="120" y="60" font-size="13" fill="#e3ddff" text-anchor="middle" font-family="sans-serif" font-weight="700">LLM</text></svg>')

# ---------------------------------------------------------------------------
# Projects
# ---------------------------------------------------------------------------
PROJECTS = [
    dict(slug="rag-policy-chatbot", title="Restaurant Policy RAG Chatbot", badge=("live", "Live on GitHub"),
         repo=f"{GITHUB}/rag-policy-chatbot", cover=COVER_RAG,
         summary="Ask restaurant policy questions in plain English and get short answers with citations to the exact policy section.",
         bullets=["Heading-aware chunking + Azure OpenAI embeddings", "Hybrid keyword + vector search in Azure AI Search",
                  "Grounded answers with [n] citations", "CLI, FastAPI endpoint and offline tests"],
         tags=["Azure OpenAI", "Azure AI Search", "FastAPI", "Python"]),
    dict(slug="hospitality-roster-app", title="Hospitality Roster App", badge=("soon", "Repo coming soon"),
         repo=None, cover=COVER_ROSTER,
         summary="A Flask web app for weekly restaurant rosters that refuses the rostering mistakes I saw as a manager.",
         bullets=["Manager login and crew list with add-person form", "Week grid with open / lunch / close slots",
                  "Close-check rule refuses staff who can't close", "Next: floor assignment and a shift-swap rule"],
         tags=["Python", "Flask", "Jinja2"]),
    dict(slug="foundry-shift-assistant", title="Foundry Shift Assistant", badge=("demo", "Demo · sample data"),
         repo=f"{GITHUB}/foundry-shift-assistant", cover=COVER_AGENT,
         summary="A tool-calling AI agent that answers a manager's rostering questions: who can cover a close, labour-cost estimates and hours left.",
         bullets=["Azure OpenAI tool calling (Microsoft Foundry deployment)", "5 Python tools: rules and maths stay in code",
                  "Same close-trained rule as the roster app", "15 offline tests with a mocked LLM"],
         tags=["Azure OpenAI", "Microsoft Foundry", "Agents", "Tool calling", "Python"]),
]

# ---------------------------------------------------------------------------
# Layout pieces
# ---------------------------------------------------------------------------
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' x2='1'%3E"
           "%3Cstop offset='0' stop-color='%234cc9f0'/%3E%3Cstop offset='1' stop-color='%237b61ff'/%3E%3C/linearGradient%3E%3C/defs%3E"
           "%3Crect width='64' height='64' rx='16' fill='url(%23g)'/%3E%3Ctext x='32' y='42' font-family='Arial' font-weight='900' "
           "font-size='26' text-anchor='middle' fill='%2308111f'%3ESK%3C/text%3E%3C/svg%3E")


def head(title: str, description: str, prefix: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="theme-color" content="#08111f">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body id="top">
"""


def nav(prefix: str) -> str:
    home = f"{prefix}index.html" if prefix else ""
    items = [("About", "#about"), ("Skills", "#skills"), ("Projects", "#projects"),
             ("Experience", "#experience"), ("Certifications", "#certifications")]
    links = "".join(f'<li><a href="{home}{h}">{t}</a></li>' for t, h in items)
    mlinks = links + f'<li><a href="{home}#contact">Contact</a></li><li><a href="{prefix}resume.pdf">Resume (PDF)</a></li>'
    return f"""<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="logo" href="{home or '#top'}"><span class="mark">SK</span><span>Siva Kowshik</span></a>
    <ul class="nav-links">{links}<li><a class="cta" href="{home}#contact">Contact</a></li></ul>
    <a class="burger" href="#menu" aria-label="Open menu"><span></span></a>
  </div>
</nav>
<div class="mobile-menu" id="menu" role="dialog" aria-label="Menu">
  <div class="top"><a class="logo" href="{home or '#top'}"><span class="mark">SK</span><span>Siva Kowshik</span></a>
  <a class="close" href="#_" aria-label="Close menu">&times;</a></div>
  <ul>{mlinks}</ul>
</div>
"""


def footer(prefix: str) -> str:
    return f"""<footer>
  <div class="wrap">
    <span>&copy; 2026 {FULL_NAME} · Melbourne, Australia</span>
    <span><a href="{GITHUB}">GitHub</a> · <a href="{LINKEDIN}">LinkedIn</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
  </div>
</footer>
</body>
</html>
"""


def tags(items) -> str:
    return '<div class="tags">' + "".join(f'<span class="tag">{escape(t)}</span>' for t in items) + "</div>"


# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------
def project_card(p: dict) -> str:
    kind, label = p["badge"]
    code = (f'<a href="{p["repo"]}" target="_blank" rel="noopener">{icon("github")}Code</a>' if p["repo"]
            else f'<span>{icon("github")}Repo coming soon</span>')
    bullets = "".join(f"<li>{escape(b)}</li>" for b in p["bullets"])
    return f"""<article class="card reveal">
  <div class="cover">{p["cover"]}<span class="badge {kind}">{label}</span></div>
  <div class="body">
    <h3>{escape(p["title"])}</h3>
    <p>{escape(p["summary"])}</p>
    <ul>{bullets}</ul>
    {tags(p["tags"])}
    <div class="links">{code}<a class="more" href="projects/{p["slug"]}.html">Case study →</a></div>
  </div>
</article>"""


def build_index() -> str:
    skills = "".join(
        f'<div class="skill reveal"><div class="ic">{icon(ic)}</div><h3>{t}</h3>{tags(items)}</div>'
        for ic, t, items in SKILLS)
    jobs = "".join(
        f'''<div class="job {cls} reveal"><div class="top"><h3>{title}</h3><span class="when">{when}</span></div>
<div class="org">{org}</div><ul>{"".join(f"<li>{escape(b)}</li>" for b in bl)}</ul></div>'''
        for title, when, org, bl, cls in JOBS)
    edu = "".join(f'<div class="edu reveal"><div class="ic">{icon("cap")}</div><div><h3>{d}</h3><span>{u}</span></div></div>'
                  for d, u in EDUCATION)
    certs = "".join(
        f'<div class="cert{" progress" if prog else ""} reveal"><div class="ic">{icon("clock" if prog else "award")}</div>'
        f'<div><h3>{t}</h3><span>{code}</span><br><span class="status">{st}</span></div></div>'
        for t, code, st, prog in CERTS)
    cards = "".join(project_card(p) for p in PROJECTS)
    return head(f"{FULL_NAME} | AI Engineer, Melbourne",
                f"{FULL_NAME}, AI engineer in Melbourne building with Azure OpenAI, Microsoft Foundry, RAG, agents and Python.", "") + nav("") + f"""
<header class="hero">
  <div class="bg"></div><div class="orb a"></div><div class="orb b"></div>
  <div class="wrap hero-grid">
    <div>
      <span class="pill fade-up"><span class="dot"></span>Open to AI engineering roles and internships · Available immediately</span>
      <h1 class="fade-up" style="--d:.08s">{NAME_FIRST}<span class="last">{NAME_LAST}</span></h1>
      <div class="role grad-text fade-up" style="--d:.16s">{TAGLINE}</div>
      <p class="lead fade-up" style="--d:.24s">I build practical AI on Azure: retrieval-augmented chatbots, tool-calling agents and Python back ends.
      About four years running high-volume restaurants means I build for real business problems like rostering, labour cost and day-to-day operations.</p>
      <div class="btns fade-up" style="--d:.32s">
        <a class="btn primary" href="#projects">View projects {icon("arrow")}</a>
        <a class="btn" href="resume.pdf" download>{icon("download")}Resume</a>
        <a class="btn" href="{GITHUB}" target="_blank" rel="noopener">{icon("github")}GitHub</a>
        <a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">{icon("linkedin")}LinkedIn</a>
      </div>
      <div class="facts fade-up" style="--d:.4s">
        <span>{icon("pin")}Melbourne, VIC, Australia</span>
        <span>{icon("cap")}Masters, BIS (Software Development)</span>
        <span>{icon("award")}AZ-900 · AI-900 · Databricks</span>
      </div>
    </div>
    <div class="avatar-wrap fade-up" style="--d:.2s">
      <div class="avatar-ring"></div>
      <!-- Profile photo: add photo.jpg next to index.html and it covers these initials automatically -->
      <div class="avatar" role="img" aria-label="{FULL_NAME}"><span class="initials grad-text">SK</span></div>
      <div class="float-chip c1"><i></i>Azure OpenAI · RAG</div>
      <div class="float-chip c2"><i></i>AI-103 in progress</div>
    </div>
  </div>
</header>

<section id="about" class="alt">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">About</span><h2>Engineer, operator, founder</h2></div>
    <div class="about">
      <div class="reveal">
        <p>I'm an <strong>AI engineer in Melbourne</strong> building Azure AI solutions in Python: <strong>RAG with Azure AI Search and Azure OpenAI</strong>, <strong>agents with Microsoft Foundry</strong>, and <strong>Databricks / Delta Lake</strong> pipelines.</p>
        <p>My software foundation comes from <strong>Infosys</strong>, where I was a Systems Engineer. I then spent about four years as a <strong>Business Manager at Grill'd and Mad Mex</strong>, leading teams of 15+ across rostering, labour cost and inventory in high-volume restaurants.</p>
        <p>That mix led me to found <strong>Australian Vision AI</strong>, a startup building AI rostering and operations tools for hospitality. I know the problems first-hand, and I build the software that fixes them.</p>
      </div>
      <div class="stats">
        <div class="stat reveal"><b class="grad-text">15+</b><span>team members led as Business Manager</span></div>
        <div class="stat reveal"><b class="grad-text">~4 yrs</b><span>running high-volume restaurants</span></div>
        <div class="stat reveal"><b class="grad-text">3</b><span>certifications, AI-103 in progress</span></div>
        <div class="stat reveal"><b class="grad-text">3</b><span>portfolio projects in Python</span></div>
      </div>
    </div>
  </div>
</section>

<section id="skills">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Skills</span><h2>What I work with</h2>
    <p>Azure AI services and Python, from retrieval and agents through to data pipelines.</p></div>
    <div class="skills">{skills}</div>
  </div>
</section>

<section id="projects" class="alt">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Projects</span><h2>Things I've built</h2>
    <p>Each project solves a problem I saw running restaurants. Open a case study for the architecture, stack and how to run it.</p></div>
    <div class="projects">{cards}</div>
    <div class="venture reveal"><div class="ic">{icon("rocket")}</div><div><h3>Australian Vision AI · Founder</h3>
    <p>Startup building AI rostering and operations tools for hospitality, drawing directly on my restaurant management experience.</p></div></div>
  </div>
</section>

<section id="experience">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Experience</span><h2>Where I've worked</h2>
    <p>Software engineering, AI projects, and hands-on hospitality operations management.</p></div>
    <div class="timeline">{jobs}</div>
  </div>
</section>

<section id="certifications" class="alt">
  <div class="wrap two">
    <div><div class="sec-head reveal" style="margin-bottom:24px"><span class="eyebrow">Education</span><h2>Study</h2></div>{edu}</div>
    <div><div class="sec-head reveal" style="margin-bottom:24px"><span class="eyebrow">Certifications</span><h2>Credentials</h2></div>{certs}</div>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <div class="contact-box reveal">
      <span class="eyebrow">Contact</span>
      <h2>Let's build something useful</h2>
      <p>I'm looking for AI engineer, AI solutions and Python / Azure back-end roles and internships in Melbourne. I'm available immediately.</p>
      <div class="btns">
        <a class="btn primary" href="mailto:{EMAIL}">{icon("mail")}{EMAIL}</a>
        <a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">{icon("linkedin")}LinkedIn</a>
        <a class="btn" href="{GITHUB}" target="_blank" rel="noopener">{icon("github")}GitHub</a>
        <a class="btn" href="resume.pdf" download>{icon("download")}Resume (PDF)</a>
      </div>
    </div>
  </div>
</section>
""" + footer("")


# ---------------------------------------------------------------------------
# Project pages
# ---------------------------------------------------------------------------
def code_block(text: str) -> str:
    lines = []
    for line in text.strip("\n").splitlines():
        if line.lstrip().startswith("#"):
            lines.append(f'<span class="c">{escape(line)}</span>')
        else:
            lines.append(escape(line))
    return "<pre><code>" + "\n".join(lines) + "</code></pre>"


def project_page(p: dict, sections: list, facts: list, intro: str) -> str:
    kind, label = p["badge"]
    if p["repo"]:
        repo_btn = f'<a class="btn primary" href="{p["repo"]}" target="_blank" rel="noopener">{icon("github")}View code on GitHub</a>'
        repo_link = f'<a href="{p["repo"]}" target="_blank" rel="noopener">github.com/{GITHUB_USER}/{p["slug"]}</a>'
    else:
        repo_btn = f'<span class="btn disabled">{icon("github")}GitHub repo coming soon</span>'
        repo_link = f"github.com/{GITHUB_USER}/{p['slug']} (coming soon)"
    toc = "".join(f'<li><a href="#{sid}">{t}</a></li>' for sid, t, _ in sections)
    body = "".join(
        f'<section id="{sid}" class="reveal"><h2><span class="n">{i:02d}</span>{t}</h2>{html}</section>'
        for i, (sid, t, html) in enumerate(sections, 1))
    fact_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts + [("Repository", repo_link)])
    others = "".join(
        f'<a href="{o["slug"]}.html"><small>Next project</small>{escape(o["title"])} →</a>'
        for o in PROJECTS if o["slug"] != p["slug"])
    return head(f"{p['title']} | {FULL_NAME}", p["summary"], "../") + nav("../") + f"""
<header class="p-hero">
  <div class="bg" style="position:absolute;inset:0"></div><div class="orb a"></div>
  <div class="wrap" style="position:relative">
    <div class="crumbs fade-up"><a href="../index.html">Home</a> / <a href="../index.html#projects">Projects</a> / {escape(p["title"])}</div>
    <span class="badge {kind} fade-up">{label}</span>
    <h1 class="fade-up" style="--d:.08s">{escape(p["title"])}</h1>
    <p class="lead fade-up" style="--d:.16s">{intro}</p>
    <div class="fade-up" style="--d:.22s">{tags(p["tags"])}</div>
    <div class="btns fade-up" style="--d:.28s">{repo_btn}<a class="btn" href="../index.html#projects">All projects</a></div>
  </div>
</header>
<div class="wrap p-layout">
  <main class="p-main">{body}
    <section class="reveal"><h2>More projects</h2><div class="next-projects">{others}</div></section>
  </main>
  <aside class="aside">
    <div class="box"><h4>At a glance</h4><dl>{fact_html}</dl></div>
    <div class="box"><h4>On this page</h4><ul class="toc">{toc}</ul></div>
  </aside>
</div>
""" + footer("../")


def stack_table(rows) -> str:
    return '<table class="stack">' + "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in rows) + "</table>"


def features(items) -> str:
    return '<div class="feature-grid">' + "".join(f'<div class="feature"><h4>{a}</h4><p>{b}</p></div>' for a, b in items) + "</div>"


def checks(items) -> str:
    return '<ul class="checks">' + "".join(f'<li class="{"done" if d else ""}">{t}</li>' for d, t in items) + "</ul>"


def rag_page() -> str:
    p = PROJECTS[0]
    sections = [
        ("problem", "The problem", """<p>Crew ask the same policy questions every shift: who can close, what temperature the cool room should be, how shift swaps work.
The answers sit in long SOP documents nobody reads mid-service, and a chatbot that guesses is worse than no chatbot.</p>
<p>I wanted an assistant that answers <strong>only from the documents</strong> and <strong>shows where each answer came from</strong>, so a manager can trust it.</p>"""),
        ("built", "What I built", features([
            ("Heading-aware chunking", "Markdown is split on headings, then windowed (~800 characters, 120 overlap), so every chunk keeps its section title."),
            ("Vector + keyword index", "Azure AI Search index with searchable text fields and an HNSW vector field for the embeddings."),
            ("Hybrid retrieval", "Each question runs as keyword (BM25) + vector search; Azure AI Search fuses the results with Reciprocal Rank Fusion."),
            ("Grounded answers", "Top excerpts are numbered and sent to the chat model with a strict prompt: answer only from them and cite with [n]."),
            ("CLI and API", "<code>ask.py</code> for the terminal and a FastAPI <code>POST /ask</code> endpoint that returns the answer and its sources."),
            ("Offline tests", "pytest covers the chunker and the retrieve → prompt → answer flow with fake Azure clients, so no keys are needed."),
        ]) + """<p>Example: <em>"Can I swap my close shift with a new starter?"</em> → "No. A close shift can only be swapped with someone who is close-trained, and a shift manager must approve the swap [1]."</p>"""),
        ("architecture", "Architecture", f'<div class="diagram">{RAG_DIAGRAM}</div>'
         "<p>The chat model's answer is returned with its numbered sources (file name and section title), so every claim can be checked.</p>"),
        ("stack", "Tech stack", stack_table([
            ("Language", "Python 3.10+"), ("LLM + embeddings", "Azure OpenAI (chat deployment, e.g. gpt-4o-mini; embedding deployment, e.g. text-embedding-3-small)"),
            ("Retrieval", "Azure AI Search: hybrid keyword + vector (HNSW)"), ("API", "FastAPI + Uvicorn"),
            ("Config", "python-dotenv, settings in <code>.env</code> (git-ignored)"), ("Tests", "pytest with fake clients")])),
        ("run", "How to run it", code_block("""
git clone https://github.com/sivakowshik/rag-policy-chatbot.git
cd rag-policy-chatbot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # add your Azure OpenAI + Azure AI Search settings

python ingest.py            # chunk -> embed -> upload the sample policies
python ask.py "Who is allowed to close the store?"
uvicorn api:app --reload    # then open http://127.0.0.1:8000/docs
pytest -q                   # offline tests, no keys needed
""") + '<div class="note">The policy documents in <code>data/sample_sops/</code> are fictional sample data written for this demo, not the policies of any real business.</div>'),
        ("next", "What's next", checks([
            (False, "Semantic ranker on top of hybrid search"), (False, "Streamlit chat UI"),
            (False, "Ingest PDFs and Word documents"), (False, "Evaluation set (question → expected source) to measure retrieval quality"),
            (False, "Deploy the API to Azure Container Apps or Azure Functions"), (False, "Managed identity instead of keys")])),
    ]
    facts = [("Type", "RAG chatbot · CLI + REST API"), ("Status", "Live on GitHub"),
             ("Azure services", "Azure OpenAI, Azure AI Search"), ("Data", "Fictional sample SOPs")]
    return project_page(p, sections, facts,
                        "A retrieval-augmented assistant that answers restaurant policy questions from SOP documents, with citations to the exact section.")


def roster_page() -> str:
    p = PROJECTS[1]
    sections = [
        ("problem", "The problem", """<p>As a Business Manager at Grill'd and Mad Mex, rostering took real time every week, and the costly mistakes were always the same:</p>
<ul><li>Putting someone on a <strong>close shift who isn't close-trained</strong>, which leaves the store short at the end of the night.</li>
<li>Losing track of who is available and who can work which slot.</li>
<li>Shift swaps that quietly break the rules.</li></ul>
<p>Generic rostering tools treat every shift the same. This app encodes the rules a manager actually checks in their head, so the roster refuses to make those mistakes.</p>"""),
        ("built", "What I built", features([
            ("Manager login", "Only a logged-in manager can view and edit the roster."),
            ("Crew list", "Every team member in one place, with an add-person form for new starters."),
            ("Weekly roster grid", "A Monday-to-Sunday grid with open, lunch and close slots for each day."),
            ("Close-check rule", "Assigning someone who can't close to a close slot is refused with a “cannot close” message instead of being saved."),
        ])),
        ("architecture", "How it works", f'<div class="diagram">{ROSTER_DIAGRAM}</div>'
         """<ol><li>If the slot is <strong>open</strong> or <strong>lunch</strong>, the assignment is saved.</li>
<li>If the slot is <strong>close</strong> and the person <strong>can close</strong>, the assignment is saved.</li>
<li>If the slot is <strong>close</strong> and the person <strong>can't close</strong>, nothing is saved and the manager sees “cannot close”.</li></ol>"""),
        ("stack", "Tech stack", stack_table([
            ("Language", "Python 3"), ("Web framework", "Flask"), ("Templates", "Jinja2 (comes with Flask)"),
            ("Run locally", "Flask development server")])),
        ("run", "How to run it", '<div class="note">The GitHub repository is coming soon. These are the steps once it is published.</div>' + code_block("""
git clone https://github.com/sivakowshik/hospitality-roster-app.git
cd hospitality-roster-app
python3 -m venv venv && source venv/bin/activate
pip install flask
python app.py               # then open http://127.0.0.1:5000
""")),
        ("next", "What's next", checks([
            (True, "Manager login"), (True, "Crew list with add-person form"), (True, "Weekly roster grid (open / lunch / close)"),
            (True, "Close-shift rule with “cannot close” message"), (False, "Floor assignment (stations per shift)"),
            (False, "Shift-swap rule (swaps only to trained staff)"), (False, "Store crew and rosters in a database (e.g. SQLite)"),
            (False, "Hashed passwords and environment-based secrets"), (False, "Availability and leave requests"),
            (False, "AI roster suggestions based on availability, skills and expected demand"), (False, "Deploy to Azure App Service")])
         + '<p>The <a href="foundry-shift-assistant.html">Foundry Shift Assistant</a> already applies the same close-trained rule inside an AI agent.</p>'),
    ]
    facts = [("Type", "Web app"), ("Status", "In development"), ("Stack", "Python, Flask, Jinja2"),
             ("Built from", "My experience as Business Manager at Grill'd and Mad Mex")]
    return project_page(p, sections, facts,
                        "A Flask web app for weekly restaurant rosters, with rules that stop a manager rostering someone on a shift they aren't trained for.")


def agent_page() -> str:
    p = PROJECTS[2]
    sections = [
        ("problem", "The problem", """<p>A manager's rostering questions are small but constant: <em>who can cover the close on Saturday?</em>, <em>can Sam close on Wednesday?</em>,
<em>what's labour costing us this week?</em> Answering them means cross-checking training, availability, who is already on, and hours.</p>
<p>An LLM on its own will happily guess names and dollar figures. I wanted an <strong>agent</strong> where the model decides <strong>which tool to call</strong>,
and plain Python applies the rules and does the maths, so every fact in the answer comes from code.</p>"""),
        ("built", "What I built", features([
            ("Agent loop", "Sends the question and tool schemas to the model, runs any <code>tool_calls</code>, returns results as <code>tool</code> messages, and repeats (max 6 steps)."),
            ("find_cover", "Who can cover a slot: close-/open-trained, available that day, not already rostered, within max hours. Fewest hours first."),
            ("check_assignment", "Can this person work this slot? If not, every reason why."),
            ("estimate_labour_cost", "Hours × base hourly rate per day and per week, with an optional flat on-cost %."),
            ("get_roster · staff_hours", "Look up shifts for a day or week, and hours used vs max per person."),
            ("Self-correcting errors", "Bad arguments (e.g. a misspelt day) go back to the model as <code>{\"error\": ...}</code> so it can retry."),
        ])),
        ("architecture", "Architecture", f'<div class="diagram">{AGENT_DIAGRAM}</div>'
         "<p>The model never reads the CSVs directly. It can only ask for a tool; the tool returns JSON; the model explains it. "
         "<code>python ask.py --show-tools</code> prints every tool call so you can see where each fact came from.</p>"),
        ("stack", "Tech stack", stack_table([
            ("Language", "Python 3.10+ (data and tools use the standard library only)"),
            ("Model", "Azure OpenAI chat deployment with tool calling (e.g. gpt-4o-mini), deployable in Microsoft Foundry"),
            ("SDK", "OpenAI Python SDK against the Azure OpenAI v1 endpoint"),
            ("Data", "Sample staff and roster CSVs"), ("Tests", "pytest: 15 offline tests, LLM mocked")])),
        ("run", "How to run it", code_block("""
git clone https://github.com/sivakowshik/foundry-shift-assistant.git
cd foundry-shift-assistant
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# No Azure needed
python offline_demo.py      # run the tools on the sample data
pytest -q                   # 15 offline tests with a mocked LLM

# With Azure OpenAI / Microsoft Foundry
cp .env.example .env        # endpoint, key, deployment name
python ask.py "Who can cover the close on Saturday?"
python ask.py --show-tools "What's the labour cost this week with 12% on-costs?"
""") + '<div class="note">Demo project: the staff, pay rates and roster are fictional sample data. Labour costs are base-rate estimates and do not model award penalty rates.</div>'),
        ("next", "What's next", checks([
            (False, "Port the same tools to Microsoft Foundry Agent Service (hosted agent with function tools)"),
            (False, "Shift-swap tool that applies the close-trained rule to swaps"),
            (False, "Read the roster from the Hospitality Roster App instead of CSV"),
            (False, "Configurable penalty rates per day"), (False, "Simple web UI")])),
    ]
    facts = [("Type", "AI agent · tool calling"), ("Status", "Demo with sample data"),
             ("Azure", "Azure OpenAI · Microsoft Foundry"), ("Tests", "15 passing, offline")]
    return project_page(p, sections, facts,
                        "A tool-calling AI agent that answers a restaurant manager's rostering questions, with the rules and maths kept in Python.")


def main() -> None:
    (ROOT / "projects").mkdir(exist_ok=True)
    pages = {
        "index.html": build_index(),
        "projects/rag-policy-chatbot.html": rag_page(),
        "projects/hospitality-roster-app.html": roster_page(),
        "projects/foundry-shift-assistant.html": agent_page(),
    }
    for rel, html in pages.items():
        (ROOT / rel).write_text(html, encoding="utf-8")
        print(f"wrote {rel}")


if __name__ == "__main__":
    main()
