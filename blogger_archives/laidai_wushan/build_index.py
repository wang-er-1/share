#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成赖导三峡素材索引页 + 验证5份素材完整性"""
import json
import os
import subprocess
import sys

BASE = r"D:\hermes\lai_dao_trip\blogger_archives\laidai_wushan"
VENV_PY = r"D:\hermes\hermes-agent\venv\Scripts\python.exe"

# 1. 验证 5 份素材 (JSON+HTML 成对存在)
SPOTS = [
    "白帝城·夔门·三峡之巅（奉节）",
    "巫山县城一日（山城烟火）",
    "青石村·神女峰徒步（巫峡精华）",
    "培石乡·巴东（渝鄂交界换乘）",
    "秭归·三峡大坝·升船机（大国重器）",
]
ok = True
for name in SPOTS:
    j = os.path.join(BASE, f"laidai-{name.split('（')[0]}.json")
    # 实际 id 前缀
    for f in os.listdir(BASE):
        if f.endswith(".json"):
            d = json.load(open(os.path.join(BASE, f), encoding="utf-8"))
            if d["spot"]["name"] == name:
                j = os.path.join(BASE, f)
                break
    h = os.path.join(BASE, name + ".html")
    j_ok = os.path.exists(j)
    h_ok = os.path.exists(h)
    ok = ok and j_ok and h_ok
    print(f"[{'PASS' if j_ok and h_ok else 'FAIL'}] {name} | JSON:{j_ok} HTML:{h_ok}")

print(f"\n素材完整性: {'全部通过' if ok else '有缺失'}")

# 2. 生成索引页
links = "".join(
    f'<li><a href="{name}.html">{name}</a></li>' for name in SPOTS)
index = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>赖导三峡 · 路线素材库</title>
<style>
body{{font-family:"PingFang SC","Microsoft YaHei",sans-serif;max-width:720px;margin:0 auto;padding:40px 24px;background:#faf9f7;color:#2b2b2b;line-height:1.8}}
h1{{font-size:24px;border-bottom:3px solid #e6502e;padding-bottom:10px}}
.card{{background:#fff;border-radius:12px;padding:20px;margin:14px 0;box-shadow:0 1px 4px rgba(0,0,0,.06)}}
a{{color:#e6502e;font-weight:600;text-decoration:none}}
.badge{{display:inline-block;background:#ffb300;color:#1a2a3a;font-size:12px;font-weight:700;padding:3px 10px;border-radius:20px}}
</style></head><body>
<h1>🎬 赖导AboutLai · 三峡线路素材库</h1>
<div class="card"><span class="badge">路线素材</span>
<p>博主：<b>赖导AboutLai</b>（B站 142万粉丝）｜ 系列：《坐水上公交游长江三峡》（上/下集）</p>
<p>已提取 <b>5 个地点素材</b>，点击查看：</p>
<ol>{links}</ol>
</div>
<div class="card"><p>📌 每个素材含：交通怎么走 / 行程安排 / 吃什么 / 住哪里 / 避坑提醒</p></div>
</body></html>"""
with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(index)
print(f"索引页: {os.path.join(BASE, 'index.html')}")
