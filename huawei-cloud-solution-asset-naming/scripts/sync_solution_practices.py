#!/usr/bin/env python3
"""Sync Huawei Cloud solution-practice cards into the skill workbook."""

import argparse
import html
import json
import re
from copy import copy
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from openpyxl import Workbook, load_workbook


SITES = {
    "中国站": "https://www.huaweicloud.com/solution/reference-architecture.html",
    "国际站": "https://www.huaweicloud.com/intl/zh-cn/solution/reference-architecture.html",
}
HEADERS = ["序号", "主标签", "一级场景", "二级场景", "解决方案名称", "方案站点", "方案名或实践名（英文）", "ID编码", "官网链接", "简述", "其他标签", "备注"]
TITLE_ALIASES = [{"litellm统一的ai管理网关", "litellm统一的ai网关"}]


class CardsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = None

    def handle_starttag(self, _tag, attrs):
        if self.cards is not None:
            return
        value = dict(attrs).get("data-cards")
        if value:
            self.cards = json.loads(html.unescape(value))


def fetch_cards(site, url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 solution-practice-sync/1.0"})
    with urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
    parser = CardsParser()
    parser.feed(body)
    if parser.cards is None:
        raise RuntimeError(f"{site}页面未找到 data-cards，网页结构可能已变化：{url}")
    cards = []
    for item in parser.cards:
        card = item.get("cardItem", {})
        if card.get("caption") and card.get("href"):
            card["site"] = site
            cards.append(card)
    return cards


def clean_text(value):
    value = re.sub(r"<[^>]+>", "", html.unescape(value or ""))
    return re.sub(r"\s+", " ", value).strip()


def normalized_title(value):
    return re.sub(r"[\s,，:：;；—–-]+", "", value or "").lower()


def slug(value):
    return Path(urlparse(value or "").path).stem.lower()


def naming_notes(name, main_label="应用方案"):
    notes = []
    if main_label == "应用方案" and any(word in name for word in ("快速部署", "一键部署", "免费试用")):
        notes.append("应用方案名称含“快速部署/一键部署/免费试用”等禁用宣传词")
    if re.search(r"[,，:：;；—–]", name):
        notes.append("名称使用逗号、冒号或破折号，不符合单空格分隔规则")
    return "；".join(notes)


def same_solution(row, card):
    row_slug = slug(row.get("官网链接"))
    card_slug = slug(card.get("href") or card.get("官网链接"))
    if row_slug and row_slug == card_slug:
        return True
    left = normalized_title(row.get("解决方案名称"))
    right = normalized_title(card.get("caption") or card.get("解决方案名称"))
    if left == right:
        return True
    return any({left, right} <= aliases for aliases in TITLE_ALIASES)


def merge_cards(cards):
    merged = []
    for card in cards:
        match = next((item for item in merged if same_solution(item, card)), None)
        if match:
            match["sites"].add(card["site"])
        else:
            merged.append({
                "官网链接": card["href"],
                "解决方案名称": clean_text(card["caption"]),
                "一级场景": clean_text(card.get("label", "")).split(",")[0],
                "简述": clean_text(card.get("description", "")),
                "sites": {card["site"]},
            })
    return merged


def site_text(sites):
    return "中国站、国际站" if sites == {"中国站", "国际站"} else next(iter(sites), "")


def copy_row_style(sheet, source_row, target_row):
    for column in range(1, sheet.max_column + 1):
        source, target = sheet.cell(source_row, column), sheet.cell(target_row, column)
        if source.has_style:
            target._style = copy(source._style)
        target.number_format = source.number_format
        target.alignment = copy(source.alignment)
    sheet.row_dimensions[target_row].height = sheet.row_dimensions[source_row].height


def load_sheet(path):
    if path.exists():
        workbook = load_workbook(path)
        return workbook, workbook.active
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "解决方案实践"
    sheet.append(HEADERS)
    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = f"A1:L1"
    return workbook, sheet


def sync(path, cards, records=()):
    existed = path.exists()
    workbook, sheet = load_sheet(path)
    freeze_panes = sheet.freeze_panes
    headers = [cell.value for cell in sheet[1]]
    for header in HEADERS:
        if header not in headers:
            sheet.cell(1, len(headers) + 1, header)
            headers.append(header)
    indexes = {header: headers.index(header) + 1 for header in headers}
    rows = []
    for cells in sheet.iter_rows(min_row=2):
        row = {header: cells[column - 1].value or "" for header, column in indexes.items()}
        row["_sites"] = set(filter(None, re.split(r"[、,，]", row.get("方案站点", ""))))
        rows.append(row)

    added = 0
    ordered_rows = []
    matched_rows = set()
    for card in merge_cards(cards):
        match = next((row for row in rows if same_solution(row, card)), None)
        if match:
            match["_sites"] = match.get("_sites", set()) | card["sites"]
        else:
            match = {
                "主标签": "应用方案",
                "一级场景": card["一级场景"],
                "二级场景": "",
                "解决方案名称": card["解决方案名称"],
                "方案名或实践名（英文）": "",
                "ID编码": slug(card["官网链接"]),
                "官网链接": card["官网链接"],
                "简述": card["简述"],
                "其他标签": "",
                "_sites": card["sites"],
            }
            added += 1
        ordered_rows.append(match)
        matched_rows.add(id(match))
    rows = ordered_rows + [row for row in rows if id(row) not in matched_rows]

    for record in records:
        match = next((row for row in rows if same_solution(row, record)), None)
        if match:
            match.update({key: value for key, value in record.items() if value and key in HEADERS})
        else:
            match = {header: record.get(header, "") for header in HEADERS}
            rows.insert(0, match)
            added += 1
        sites = set(filter(None, re.split(r"[、,，]", record.get("方案站点", ""))))
        match["_sites"] = match.get("_sites", set()) | sites

    for number, row in enumerate(rows, 1):
        excel_row = number + 1
        if excel_row > sheet.max_row and sheet.max_row > 1:
            copy_row_style(sheet, sheet.max_row, excel_row)
        row["序号"] = number
        row["方案站点"] = site_text(row.get("_sites", set()))
        notes = [value for value in (row.get("备注", ""), naming_notes(row.get("解决方案名称", ""), row.get("主标签", ""))) if value]
        if not row.get("方案名或实践名（英文）") or not row.get("二级场景"):
            notes.append("现网新增，待补充英文名称和二级场景")
        row["备注"] = "；".join(dict.fromkeys(notes))
        for header, column in indexes.items():
            cell = sheet.cell(excel_row, column, row.get(header, ""))
            if header == "官网链接":
                cell.hyperlink = row.get(header) or None

    sheet.auto_filter.ref = f"A1:{sheet.cell(1, sheet.max_column).column_letter}{sheet.max_row}"
    sheet.auto_filter.filterColumn = []
    for row_number in range(2, sheet.max_row + 1):
        sheet.row_dimensions[row_number].hidden = False
    sheet.freeze_panes = freeze_panes if existed else "A2"
    sheet.sheet_view.selection[0].activeCell = "A1"
    sheet.sheet_view.selection[0].sqref = "A1"
    workbook.save(path)
    return len(rows), added


def main():
    default = Path(__file__).resolve().parents[1] / "解决方案实践.xlsx"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", nargs="?", type=Path, default=default)
    parser.add_argument("--record-json", action="append", default=[], help="要新增或更新的一条完整表格记录（JSON 对象）")
    args = parser.parse_args()
    # The pages store cards oldest-first but render them newest-first.
    cards = [card for site, url in SITES.items() for card in reversed(fetch_cards(site, url))]
    records = [json.loads(value) for value in args.record_json]
    total, added = sync(args.workbook, cards, records)
    print(f"已同步 {total} 条方案实践，新增 {added} 条：{args.workbook}")


if __name__ == "__main__":
    main()
