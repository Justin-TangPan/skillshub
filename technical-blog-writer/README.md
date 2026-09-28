# 技术博客写作 Skill

用于撰写、改写或润色可直接发布的技术博客、解决方案文章、教程和最佳实践文档。

## 使用示例

Codex 显式调用：

```text
$technical-blog-writer 把这个主题写成一篇面向开发者、可直接发布的技术文章。
```

最佳实践文档：

```text
$technical-blog-writer 基于这些资料，按技能内置模板输出一份可复现、可验收的最佳实践 Word 文档。
```

Claude Code 中无需 `$` 前缀，直接描述需求即可由模型依据 `SKILL.md` 自动触发。

## 安装

### Claude Code

全局（个人自用）：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R technical-blog-writer "$HOME/.claude/skills/"
```

或项目级：

```bash
mkdir -p <项目>/.claude/skills
cp -R technical-blog-writer <项目>/.claude/skills/
```

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R technical-blog-writer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启会话后即可使用。
