# skillshub

个人自用 Skills 集合。

| Skill | 说明 |
|---|---|
| [technical-blog-writer](./technical-blog-writer/) | 撰写、改写或润色面向开发者与技术决策者的技术博客、产品文章、解决方案文章和教程，含资料核验、叙事设计、配图规划与去 AI 味。 |
| [open-source-solution-evaluator](./open-source-solution-evaluator/) | 评估开源项目是否值得制作成解决方案实践、SAC 或一键部署方案。 |

## 安装到 Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R technical-blog-writer open-source-solution-evaluator "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## 安装到 Claude Code（项目级）

```bash
mkdir -p <项目>/.claude/skills
cp -R technical-blog-writer open-source-solution-evaluator <项目>/.claude/skills/
```

重启会话后生效。
