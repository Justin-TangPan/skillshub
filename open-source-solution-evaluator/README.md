# 解决方案实践价值评估 / 分类 Skill

用于把候选项目归类到解决方案实践类型（应用方案 / Skills / 最佳实践，免费试用为附加标签），并给出是否建议建设、预计工作量（人天）与推荐理由。

## 使用示例

Codex 显式调用：

```text
$open-source-solution-evaluator 请评估 <候选项目> 应归为哪种解决方案实践类型，并给出是否建议建设与预计工作量。
```

Claude Code 中无需 `$` 前缀，直接描述需求即可由模型依据 `SKILL.md` 自动触发。

## 安装

请复制整个目录，不要只复制 `SKILL.md`；评估报告依赖 `references/report-template.md`。

### Claude Code

全局（个人自用）：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R open-source-solution-evaluator "$HOME/.claude/skills/"
```

或项目级：

```bash
mkdir -p <项目>/.claude/skills
cp -R open-source-solution-evaluator <项目>/.claude/skills/
```

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R open-source-solution-evaluator "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启会话后即可使用。