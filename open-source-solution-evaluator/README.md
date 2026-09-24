# 开源解决方案实践评估 Skill

用于评估公开开源项目是否适合制作成解决方案实践、SAC 或一键部署方案。

## 使用示例

Codex 显式调用：

```text
$open-source-solution-evaluator 评估 https://github.com/owner/project 是否值得制作成解决方案实践。
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