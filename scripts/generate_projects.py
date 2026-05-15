# -*- coding: utf-8 -*-

import json
import re
from datetime import date
from pathlib import Path

INPUT = Path("raw/projects/rm_achievements20260515.jsonl")
OUTPUT = Path("content/projects")
TODAY = date.today()

MEMBER_LINKS = {
    "Hiroshi Ueda": "/authors/hiroshi-ueda/",
    "Shohei Miyakoshi": "/authors/shohei-miyakoshi/",
    "Ryo Watanabe": "/authors/ryo-watanabe/",
    "Takumi Kaneda": "/authors/takumi-kaneda/",
    "Takanori Sugimoto": "/authors/takanori-sugimoto/",
    "Tomonori Shirakawa": "/authors/tomonori-shirakawa/",
    "Seiji Yunoki": "/authors/seiji-yunoki/",
    "Hidetaka Manabe": "/authors/hidetaka-manabe/",
    "Toshiya Hikihara": "/authors/toshiya-hikihara/",
    "Keisuke Fujii": "/authors/keisuke-fujii/",
}

TITLE_OVERRIDES = {

    "テンソルネットワークの媒介する量子・古典融合":
        "Quantum-Classical Hybrid Approaches Mediated by Tensor Networks",

    "テンソルネットワークの媒介する量子・古典融合（in Japanese）":
        "Quantum-Classical Hybrid Approaches Mediated by Tensor Networks",

    "計算可能領域の開拓のための量子・スパコン連携プラットフォームの研究開発":
        "Quantum–Supercomputer Hybrid Platform for Expanding Computational Frontiers",

    "計算可能領域の開拓のための量子・スパコン連携プラットフォームの研究開発 (in Japanese)":
        "Quantum–Supercomputer Hybrid Platform for Expanding Computational Frontiers",

    "ポスト５Ｇ情報通信システム基盤強化研究開発事業":
        "Post-5G Information and Communication System Infrastructure R&D Program",

    "ポスト５Ｇ情報通信システム基盤強化研究開発事業 (in Japanese)":
        "Post-5G Information and Communication System Infrastructure R&D Program",

    "知的量子設計による量子ソフトウェア研究開発と応用":
        "Intelligent Quantum Design for Quantum Software Research and Applications",

    "知的量子設計による量子ソフトウェア研究開発と応用 (in Japanese)":
        "Intelligent Quantum Design for Quantum Software Research and Applications",

    "光・量子飛躍フラッグシッププログラム(Q-LEAP)":
        "Quantum Leap Flagship Program (Q-LEAP)",

    "光・量子飛躍フラッグシッププログラム(Q-LEAP) (in Japanese)":
        "Quantum Leap Flagship Program (Q-LEAP)",

    "量子ソフトウェア研究拠点":
        "Quantum Software Research Hub",

    "産学が連携した研究開発成果の展開 研究成果展開事業 共創の場形成支援 共創の場形成支援プログラム(COI-NEXT) 政策重点分野":
        "COI-NEXT: Quantum Software Co-Creation Platform",

    "非可換ＤＭＲＧ法による２次元量子スピン系シミュレーション手法の構築":
        "Non-Abelian DMRG Methods for Two-Dimensional Quantum Spin Systems",

    "フラストレート量子スピン系の電場活性磁気素励起の解明":
        "Electric-Field-Active Magnetic Excitations in Frustrated Quantum Spin Systems",

    "テンソルネットワーク×量子計算機による量子物性シミュレータ":
        "Quantum Many-Body Simulator Using Tensor Networks and Quantum Computers",

    "テンソルネットワーク×量子計算機による量子物性シミュレータ (in Japanese)":
        "Quantum Many-Body Simulator Using Tensor Networks and Quantum Computers",

    "未踏ターゲット事業（ゲート式量子コンピュータ部門）":
        "MITOU Target Program (Gate-Based Quantum Computing)",

    "未踏ターゲット事業（ゲート式量子コンピュータ部門）(in Japanese)":
        "MITOU Target Program (Gate-Based Quantum Computing)",

    "密度行列繰り込み群法の高度化―点群対称性への適応―":
        "Advanced Density-Matrix Renormalization Group Methods with Point-Group Symmetry",

    "二次元フラストレート量子スピン系における磁場誘起トポロジカル相転移の理論":
        "Field-Induced Topological Phase Transitions in Frustrated Quantum Spin Systems",

    "高次特異値分解によるテンソルネットワーク状態の最適化―量子系への応用―":
        "Optimization of Tensor-Network States via Higher-Order Singular Value Decomposition",

    "密度行列繰り込み群法を超える行列積変分状態最適化法の構築":
        "Matrix-Product Variational Optimization Beyond Density-Matrix Renormalization Group",
}

PERSON_NAME_OVERRIDES = {

    # Ueda Group
    "上田宏": "Hiroshi Ueda",
    "上田 宏": "Hiroshi Ueda",

    # Collaborators
    "諏訪秀麿": "Hidemaro Suwa",
    "諏訪 秀麿": "Hidemaro Suwa",

    "奥西巧一": "Kouichi Okunishi",
    "奥西 巧一": "Kouichi Okunishi",

    "藤井啓祐": "Keisuke Fujii",
    "藤井 啓祐": "Keisuke Fujii",

    "佐藤三久": "Mitsuhisa Sato",
    "丹波 廣寅": "Hirotora Tamba",
    "中島 研吾": "Kengo Nakajima",

    "古川 信夫": "Nobuo Furukawa",
    "丸山 勲": "Isao Maruyama",
    "山本 大輔": "Daisuke Yamamoto",
    "宮原 慎": "Shin Miyahara",

    "高柳 匡": "Tadashi Takayanagi",
    "森前 智行": "Tomoyuki Morimae",
    "中田 芳史": "Yoshifumi Nakata",
    "飯塚 則裕": "Norihiro Iizuka",
    "手塚 真樹": "Masaki Tezuka",
    "中島 秀太": "Shuta Nakajima",
    "石橋 明浩": "Akihiro Ishibashi",
    "遊佐 剛": "Tsuyoshi Yusa",
    "堀田 昌寛": "Masahiro Hotta",
    "白水 徹也": "Tetsuya Shiromizu",
    "泉 圭介": "Keisuke Izumi",
    "小林 努": "Tsutomu Kobayashi",
    "西岡 辰磨": "Tatsuma Nishioka",
    "堀田 知佐": "Chisa Hotta",

    "廣澤　智紀": "Tomoki Hirosawa",
    "廣澤 智紀": "Tomoki Hirosawa",
}

FUNDING_OVERRIDES = {

    "科学技術振興機構":
        "Japan Science and Technology Agency (JST)",

    "Japan Science and Technology Agency":
        "Japan Science and Technology Agency (JST)",

    "文部科学省":
        "Ministry of Education, Culture, Sports, Science and Technology (MEXT)",

    "MEXT":
        "Ministry of Education, Culture, Sports, Science and Technology (MEXT)",

    "NEDO":
        "New Energy and Industrial Technology Development Organization (NEDO)",

    "独立行政法人情報処理推進機構":
        "Information-technology Promotion Agency, Japan (IPA)",

    "RIKEN":
        "RIKEN",

    "Japan Society for the Promotion of Science":
        "Japan Society for the Promotion of Science (JSPS)",

    "Ministry of Education, Culture, Sports, Science and Technology":
        "Ministry of Education, Culture, Sports, Science and Technology (MEXT)",
}

def read_jsonl(path):
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def pick_text(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        return ", ".join([pick_text(v) for v in value if pick_text(v)])
    if isinstance(value, dict):
        for key in ["en", "ja", "name", "title"]:
            if key in value:
                return pick_text(value[key])
        for v in value.values():
            text = pick_text(v)
            if text:
                return text
    return ""


def clean_title(title):
    title = title.strip()
    title = TITLE_OVERRIDES.get(title, title)
    title = title.replace(" (in Japanese)", "")
    title = title.replace("（in Japanese）", "")
    return title


def normalize_person_name(name):
    return PERSON_NAME_OVERRIDES.get(name, name)

def normalize_funding_name(name):
    return FUNDING_OVERRIDES.get(name, name)

def normalize_date(value):
    value = pick_text(value).replace("/", "-")
    if not value:
        return ""
    if re.fullmatch(r"\d{4}", value):
        return f"{value}-04-01"
    if re.fullmatch(r"\d{4}-\d{2}", value):
        return f"{value}-01"
    return value


def display_date(value):
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value or ""):
        return value[:7]
    return value or ""


def parse_date(value):
    try:
        return date.fromisoformat(value)
    except Exception:
        return None


def status_from_end_date(end_date):
    d = parse_date(end_date)
    if d is None:
        return "ongoing"
    return "ongoing" if d >= TODAY else "completed"


def compact_role(role):
    mapping = {
        "principal_investigator": "PI",
        "coinvestigator": "Co-I",
        "co_investigator": "Co-I",
        "collaborator": "Collaborator",
        "others": "Member",
    }
    return mapping.get(role, role.replace("_", " ").title()) if role else ""


def extract_people(data):
    people = []
    if isinstance(data, list):
        for x in data:
            people.append(pick_text(x.get("name") if isinstance(x, dict) else x))
    elif isinstance(data, dict):
        if "en" in data:
            return extract_people(data["en"])
        if "ja" in data:
            return extract_people(data["ja"])
        for v in data.values():
            people.extend(extract_people(v))

    seen = set()
    result = []
    for p in people:
        p = normalize_person_name(p)
        if p and p not in seen:
            result.append(p)
            seen.add(p)
    return result


def link_person(name):
    url = MEMBER_LINKS.get(name)
    return f'<a href="{url}">{name}</a>' if url else name


def linked_people(names):
    return ", ".join([link_person(n) for n in names if n])


def markdown_escape(text):
    return str(text).replace("|", "\\|")


def extract_project(record):
    merge = record.get("merge", {})
    title = clean_title(pick_text(merge.get("research_project_title")))

    if not title:
        return None

    identifiers = merge.get("identifiers", {})
    grant_numbers = identifiers.get("grant_number", [])

    date_start = normalize_date(merge.get("from_date"))
    date_end = normalize_date(merge.get("to_date"))

    return {
        "title": title,
        "funding_agency": normalize_funding_name(pick_text(merge.get("offer_organization"))),
        "program": clean_title(pick_text(merge.get("system_name"))),
        "role": compact_role(pick_text(merge.get("research_project_owner_role"))),
        "date_start": date_start,
        "date_end": date_end,
        "status": status_from_end_date(date_end),
        "grant_number": str(grant_numbers[0]) if grant_numbers else "",
        "investigators": extract_people(merge.get("investigators")),
    }


def write_index(projects):
    ongoing = sorted(
        [p for p in projects if p["status"] == "ongoing"],
        key=lambda p: p["date_start"],
        reverse=True,
    )
    completed = sorted(
        [p for p in projects if p["status"] == "completed"],
        key=lambda p: p["date_start"],
        reverse=True,
    )

    text = """---
title: Projects
type: page
---

<div class="projects-list">

<p class="projects-intro">Research projects and grants related to the Ueda Group.</p>

"""

    def add_section(title, items):
        nonlocal text
        text += f'<h2 class="projects-section-title">{title}</h2>\n\n'

        if not items:
            text += '<p class="projects-empty">No entries yet.</p>\n\n'
            return

        for p in items:
            period = display_date(p["date_start"])
            if p["date_end"]:
                period += f" – {display_date(p['date_end'])}"

            text += '<div class="project-entry">\n'
            text += f'<div class="project-title">{markdown_escape(p["title"])}</div>\n'
            text += '<div class="project-meta">\n'

            if period:
                text += f'<div><strong>Period:</strong> {period}</div>\n'
            if p["funding_agency"]:
                text += f'<div><strong>Funding:</strong> {markdown_escape(p["funding_agency"])}</div>\n'
            if p["program"]:
                text += f'<div><strong>Program:</strong> {markdown_escape(p["program"])}</div>\n'
            if p["role"]:
                text += f'<div><strong>Role:</strong> {markdown_escape(p["role"])}</div>\n'
            if p["investigators"]:
                text += f'<div><strong>Investigators:</strong> {linked_people(p["investigators"])}</div>\n'

            text += "</div>\n"
            text += "</div>\n\n"

    add_section("Ongoing Projects", ongoing)
    add_section("Past Projects", completed)

    text += "</div>\n"

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "_index.md").write_text(text, encoding="utf-8")


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    records = read_jsonl(INPUT)
    projects = []

    for record in records:
        project = extract_project(record)
        if project:
            projects.append(project)

    write_index(projects)
    print(f"Generated Projects index with {len(projects)} entries")


if __name__ == "__main__":
    main()