# 华为云解决方案资产命名 Skill

用于生成华为云「解决方案实践」资产的中英文名称、URL ID、场景分类和标签。

## 使用示例

Codex 显式调用：

```text
$huawei-cloud-solution-asset-naming 帮我梳理 https://github.com/DayuanJiang/next-ai-draw-io 的方案命名。
```

以下自然语言请求在 Claude Code 中会自动触发此 Skill（Codex 中同样适用）：

```text
我要把这个开源项目做成华为云解决方案，请帮我生成中英文方案名、ID、场景分类和标签。

这个 Skill 准备发布到解决方案实践，请整理官网资产元数据。

帮我判断这个方案应该属于应用方案、最佳实践还是 Skills，并给出一级和二级场景。
```

## 安装

请复制整个目录，不要只复制 `SKILL.md`；该 Skill 依赖 `scripts/sync_solution_practices.py` 和 `解决方案实践.xlsx`。

同步前可加 `--check-links` 检查官网目录和工作簿中的详情链接；无法访问或格式异常时脚本会停止，不写入工作簿。同步摘要会列出新增方案、两站目录顺序冲突、未匹配官网条目、保留的旧行、无效链接和缺少区域的站点。单一表格按中国站顺序排列，无法同时还原两站各自不同的目录顺序。

### Claude Code

全局（个人自用）：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R huawei-cloud-solution-asset-naming "$HOME/.claude/skills/"
```

或项目级：

```bash
mkdir -p <项目>/.claude/skills
cp -R huawei-cloud-solution-asset-naming <项目>/.claude/skills/
```

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R huawei-cloud-solution-asset-naming "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启会话后即可使用。
