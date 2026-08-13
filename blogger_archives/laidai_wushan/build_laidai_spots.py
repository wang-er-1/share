#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""赖导三峡 5 个地点素材：从已有转写提取, 生成 5 份路线档案 (JSON + HTML)。

赖导三峡2集转写已完成(shangji.txt/xiaji.txt), 按地点拆成5份素材:
1. 白帝城+三峡之巅 (奉节段)
2. 巫山县城 (巫山段)
3. 青石村+神女峰 (巫峡段)
4. 培石乡+巴东 (渝鄂交界段)
5. 秭归+三峡大坝+升船机 (宜昌段)
"""
import json
import html
import os

BASE = r"D:\hermes\lai_dao_trip\blogger_archives\laidai_wushan"
os.makedirs(BASE, exist_ok=True)

# 从已核对的转写提取的 5 个地点素材
SPOTS = [
    {
        "id": "laidai-baidi-fengjie",
        "name": "白帝城·夔门·三峡之巅（奉节）",
        "sub": "10元人民币背景 + 刘备托孤之地 + 三峡最高点日落",
        "region": "重庆·奉节",
        "days": "1天",
        "budget": "200-300元",
        "best_season": "春秋/11月红叶",
        "style": ["人文", "历史", "登山", "日落"],
        "transport": [
            {"mode": "郑渝高铁至奉节站", "detail": "重庆北→奉节约1.5h，2022年通车"},
            {"mode": "县城内打车", "detail": "去三峡之巅往返约100元，单程60元，盘山约半小时"}
        ],
        "schedule": [
            {"time": "上午", "item": "白帝城（刘备托孤地），现为江中孤岛，走廊桥进入", "note": "10元人民币背面夔门实景打卡点"},
            {"time": "下午", "item": "三峡之巅（赤甲山），索道上下，山顶约10℃", "note": "看瞿塘峡全景+日落最佳；徒步路线已封闭（13:30后禁入，爬需3-6小时）"},
            {"time": "傍晚", "item": "夔门大桥看长江日落", "note": "奉节新县城仅20年历史，老县城在水下"}
        ],
        "food": [
            {"name": "本地餐馆家常菜", "price": "人均30-50元", "note": "奉节县城餐馆众多"}
        ],
        "lodging": [
            {"name": "临江商务酒店", "price": "89元/晚", "note": "江景房，赖导同款"}
        ],
        "pitfalls": [
            "三峡之巅17:00后不让进，看日落要16:00前到索道",
            "徒步上赤甲山的入口下午13:30-14:00关闭，别计划徒步",
            "白帝城已变孤岛，必须走廊桥"
        ],
        "source_video": "BV1F9U8BzE3F（上集）"
    },
    {
        "id": "laidai-wushan-town",
        "name": "巫山县城一日（山城烟火）",
        "sub": "比重庆还山城的县城，1136级台阶的神女大道",
        "region": "重庆·巫山",
        "days": "1天",
        "budget": "150-250元",
        "best_season": "春秋",
        "style": ["人文", "美食", "城市漫步", "山城"],
        "transport": [
            {"mode": "郑渝高铁至巫山站", "detail": "重庆北→巫山约2h；或奉节→巫山小红船40元3.5h"},
            {"mode": "县城内摩的", "detail": "5元起步，不坑外地人"}
        ],
        "schedule": [
            {"time": "上午", "item": "巫山长江大桥（红色拱桥，贾樟柯电影经典镜头）", "note": "江边拍照"},
            {"time": "中午", "item": "一家馆子纸包鱼（蒜香98元/条）", "note": "巫山特色，码头附近一排纸包鱼店"},
            {"time": "下午", "item": "神女大道 1136级台阶", "note": "旁边在建神女大扶梯（比香港中环-半山扶梯长100米）"},
            {"time": "傍晚", "item": "巫山博物馆/江边散步", "note": "县城地势起伏大，全程盘山"}
        ],
        "food": [
            {"name": "纸包鱼（一家馆子）", "price": "98元/条2.5斤", "note": "蒜香味是特色，鱼肉嫩少刺"},
            {"name": "麻辣菜包", "price": "1元/个", "note": "包菜/韭菜馅巨辣，早餐排队抢购"},
            {"name": "卷卷/烤面筋/铁板烧", "price": "3-10元", "note": "学校门口小吃，巫山正宗第一家烤面筋"}
        ],
        "lodging": [
            {"name": "锦衣酒店", "price": "180元/晚", "note": "智能酒店小江景房，赖导同款"}
        ],
        "pitfalls": [
            "麻辣菜包排队人多，想吃要早起",
            "县城爬坡多，穿舒服的鞋"
        ],
        "source_video": "BV1F9U8BzE3F（上集）"
    },
    {
        "id": "laidai-qingshi-shennv",
        "name": "青石村·神女峰徒步（巫峡精华）",
        "sub": "与神女峰隔江相望的江边小村，爬翠屏峰平视神女峰",
        "region": "重庆·巫山县青石村",
        "days": "1-2天",
        "budget": "150-200元",
        "best_season": "春秋/11月红叶",
        "style": ["小众", "徒步", "江景", "原生态"],
        "transport": [
            {"mode": "小红船（水上公交）", "detail": "巫山→青石村10元，8:00/14:00各一班；船到村口下"},
            {"mode": "青石村→培石", "detail": "30元，第二天继续行程"}
        ],
        "schedule": [
            {"time": "上午", "item": "坐小红船进巫峡，沿途看巫山十二峰", "note": "巫峡46km，精华段在巫山长江大桥→青石村"},
            {"time": "下午", "item": "徒步登翠屏峰（约2h登顶）", "note": "山顶平视神女峰+十二峰全景；路况野需打草惊蛇防蛇"},
            {"time": "傍晚", "item": "神女山庄住下，江边看日落", "note": "只有一家民宿，无法线上预订"}
        ],
        "food": [
            {"name": "神女山庄包饭", "price": "100元/人含两顿饭", "note": "农家菜，自己种的蔬菜"}
        ],
        "lodging": [
            {"name": "神女山庄", "price": "100元/人", "note": "包两顿饭；全村十几户人家只有这一家住宿"}
        ],
        "pitfalls": [
            "⚠️ 必须天黑前下山！赖导亲历摸黑下山1小时5分钟",
            "野路杂草丛生，务必打草惊蛇防蛇，最好结伴",
            "住宿无法线上预订，只能现场找；节假日可能满房",
            "带充电宝手电筒"
        ],
        "source_video": "BV1TwS7BmETP（下集）"
    },
    {
        "id": "laidai-peishi-badong",
        "name": "培石乡·巴东（渝鄂交界换乘）",
        "sub": "重庆最东端乡镇，小红船换湖北小白船的独特体验",
        "region": "重庆培石乡→湖北巴东",
        "days": "1天",
        "budget": "100-200元",
        "best_season": "春秋",
        "style": ["小众", "边境", "水运", "人文"],
        "transport": [
            {"mode": "小红船青石村→培石乡", "detail": "30元，约30分钟"},
            {"mode": "培石→巴东换乘湖北小白船", "detail": "船对船换乘，等约1小时，船队对接2025年10月刚恢复"},
            {"mode": "培石乡内小车", "detail": "5元单程，镇上兜风"}
        ],
        "schedule": [
            {"time": "上午", "item": "青石村坐船到培石乡", "note": "重庆最东边乡镇，渝鄂交界"},
            {"time": "中午", "item": "培石乡闲逛", "note": "小镇整洁，山清水秀，水涨后形成的湖湾"},
            {"time": "下午", "item": "换乘湖北小白船到巴东", "note": "船上可看巫峡尾巴"}
        ],
        "food": [
            {"name": "培石乡本地小馆", "price": "人均20-40元", "note": "乡镇物价低"}
        ],
        "lodging": [
            {"name": "巴东县城酒店", "price": "150-250元/晚", "note": "赖导住的有阳台看长江"}
        ],
        "pitfalls": [
            "换乘要等约1小时，别着急",
            "巴东→秭归没有客船！只能坐小客车（12:00唯一一班）",
            "包船去秭归报价5000+，不值"
        ],
        "source_video": "BV1TwS7BmETP（下集）"
    },
    {
        "id": "laidai-zigui-dam",
        "name": "秭归·三峡大坝·升船机（大国重器）",
        "sub": "坛子岭看五级船闸，坐游轮体验113米落差垂直升船机",
        "region": "湖北秭归→宜昌",
        "days": "2天",
        "budget": "800-1000元",
        "best_season": "春秋",
        "style": ["大国重器", "水利", "游轮", "移民文化"],
        "transport": [
            {"mode": "巴东→秭归小客车", "detail": "一天一班，中午12点发车，约3小时，沿江山路"},
            {"mode": "茅坪渡口→刘家河轮渡", "detail": "8元/人，20分钟到对岸，避开绕路30km"},
            {"mode": "西陵峡和谐号游轮", "detail": "608元/人，含升船机+葛洲坝船闸+西陵峡→宜昌"}
        ],
        "schedule": [
            {"time": "D1下午", "item": "湖北三峡移民博物馆（免费）", "note": "老县城水下模型、大坝模型、五级船闸原理"},
            {"time": "D1傍晚", "item": "木鱼岛看三峡大坝正面", "note": "免费，可露营"},
            {"time": "D2上午", "item": "三峡大坝：坛子岭（五级船闸全景）+185平台", "note": "大坝不收门票，只收景区交通车票"},
            {"time": "D2中午", "item": "西陵峡和谐号游轮", "note": "体验升船机：垂直下降113米，约40分钟，无失重感；再经葛洲坝船闸，夜抵宜昌"}
        ],
        "food": [
            {"name": "秭归特色菜", "price": "人均40-60元", "note": "肉末南豆腐、炸辣椒、腊肉炒辣椒"}
        ],
        "lodging": [
            {"name": "秭归县城酒店", "price": "150-300元/晚", "note": "注意：秭归房价比宜昌还贵，消费不低"}
        ],
        "pitfalls": [
            "秭归无高铁站无机场，进出都得走宜昌",
            "游轮608元含升船机体验，非常值；升舱另收费（送纪念币）",
            "大坝景区必须坐景区大巴（收交通费）",
            "升船机只给3000吨以下船用，大船走五级船闸约4小时"
        ],
        "source_video": "BV1TwS7BmETP（下集）"
    }
]

CSS = """
*{box-sizing:border-box}
body{font-family:"PingFang SC","Microsoft YaHei",sans-serif;max-width:720px;margin:0 auto;padding:24px 20px 60px;background:#faf9f7;color:#2b2b2b;line-height:1.7;font-size:15px}
.header{background:linear-gradient(135deg,#1a2a3a,#2d4a5a);color:#fff;border-radius:14px;padding:24px;margin-bottom:16px}
.header h1{margin:8px 0;font-size:22px}
.header .badge{display:inline-block;background:#ffb300;color:#1a2a3a;font-size:12px;font-weight:700;padding:3px 10px;border-radius:20px}
.header .sub{opacity:.9;margin:6px 0;font-size:13.5px}
.header .style{font-size:12.5px;opacity:.75}
.card{background:#fff;border-radius:12px;padding:18px 20px;margin-bottom:14px;box-shadow:0 1px 4px rgba(0,0,0,.06)}
.card h2{font-size:16px;margin:0 0 12px;border-left:4px solid #e6502e;padding-left:10px}
.card h3{font-size:15px;margin:14px 0 6px;color:#1a2a3a}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:13.5px}
td,th{border:1px solid #ddd;padding:6px 8px;text-align:left;vertical-align:top}
th{background:#f5ede8}
ul{margin:6px 0;padding-left:22px;font-size:14px}
.tips{background:#f0f7f0;border-radius:8px;padding:8px 12px;font-size:13px;color:#2d5a2d;margin:8px 0 0}
.warn{border:1px solid #ffd9a0;background:#fffaf2}
a{color:#e6502e;font-weight:600}
.footer{text-align:center;color:#999;font-size:12px;margin-top:20px}
"""

def build_html(spot):
    transport_rows = "".join(
        f"<tr><td><b>{html.escape(t['mode'])}</b></td><td>{html.escape(t['detail'])}</td></tr>"
        for t in spot["transport"])
    sched_rows = "".join(
        f"<tr><td><b>{html.escape(s['time'])}</b></td><td>{html.escape(s['item'])}</td><td>{html.escape(s.get('note',''))}</td></tr>"
        for s in spot["schedule"])
    food_items = "".join(
        f"<li><b>{html.escape(f['name'])}</b> {html.escape(f['price'])} — {html.escape(f.get('note',''))}</li>"
        for f in spot["food"])
    lodge_items = "".join(
        f"<li><b>{html.escape(l['name'])}</b> {html.escape(l['price'])} — {html.escape(l.get('note',''))}</li>"
        for l in spot["lodging"])
    pit_items = "".join(f"<li>{html.escape(p)}</li>" for p in spot["pitfalls"])

    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(spot['name'])}</title><style>{CSS}</style></head><body>
<div class="header">
  <div class="badge">路线素材 · 赖导三峡系列</div>
  <h1>{html.escape(spot['name'])}</h1>
  <p class="sub">{html.escape(spot['sub'])}</p>
  <p class="sub">{html.escape(spot['region'])} ｜ {html.escape(spot['days'])} ｜ 预算 {html.escape(spot['budget'])} ｜ 最佳季节：{html.escape(spot['best_season'])}</p>
  <p class="style">{' / '.join(html.escape(s) for s in spot['style'])}</p>
</div>
<div class="card"><h2>🚗 交通怎么走</h2><table><tr><th>方式</th><th>详情</th></tr>{transport_rows}</table></div>
<div class="card"><h2>🗓️ 行程安排</h2><table><tr><th>时间</th><th>安排</th><th>备注</th></tr>{sched_rows}</table></div>
<div class="card"><h2>🍜 吃什么</h2><ul>{food_items}</ul></div>
<div class="card"><h2>🏨 住哪里</h2><ul>{lodge_items}</ul></div>
<div class="card warn"><h2>⚠️ 避坑提醒</h2><ul>{pit_items}</ul></div>
<div class="card"><p class="tips">🎬 素材来源：{html.escape(spot['source_video'])}（赖导AboutLai）</p></div>
<div class="footer">路线素材 · 赖导三峡系列 · 提取自博主亲历视频（含人工校对）</div>
</body></html>"""

# 生成
index_items = []
for spot in SPOTS:
    # JSON
    jpath = os.path.join(BASE, f"{spot['id']}.json")
    with open(jpath, "w", encoding="utf-8") as f:
        json.dump({"id": spot["id"], "blogger": "赖导AboutLai", "spot": spot},
                  f, ensure_ascii=False, indent=2)
    # HTML
    hpath = os.path.join(BASE, f"{spot['name']}.html")
    with open(hpath, "w", encoding="utf-8") as f:
        f.write(build_html(spot))
    index_items.append((spot["name"], hpath))
    print(f"OK: {spot['name']}")

print(f"\n共 {len(SPOTS)} 份素材生成完毕 -> {BASE}")
