#!/bin/bash
# 一键发布: 把任意 HTML/MD 文件发布到 GitHub Pages, 生成公网链接
# 用法: bash publish.sh <文件路径> [备注]
# 示例: bash publish.sh "D:/hermes/lai_dao_trip/方案.html" "巫山行程方案"
set -e
cd /d/hermes/lai_dao_trip

FILE="$1"
MSG="${2:-update}"

if [ -z "$FILE" ]; then
  echo "用法: bash publish.sh <文件路径> [备注]"
  exit 1
fi

NAME=$(basename "$FILE")
echo "== 发布: $NAME =="

git add "$FILE"
git -c user.name="wang-er-1" -c user.email="wang-er-1@users.noreply.github.com" commit -m "$MSG: $NAME" --quiet
git push origin main --quiet

# URL 编码中文文件名
ENCODED=$(python -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$NAME")
echo ""
echo "✅ 发布成功! 公网链接:"
echo "https://wang-er-1.github.io/share/$ENCODED"
echo ""
echo "⚠️ 注意: GitHub Pages 国内直连可能不稳定, 打不开时可用代理或换国内托管"
