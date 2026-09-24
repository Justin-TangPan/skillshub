# skillshub

个人自用 Skills 集合，同时兼容 Codex 与 Claude Code。

| Skill | 说明 |
|---|---|
| [china-personal-tax-optimizer](./china-personal-tax-optimizer/) | 模拟中国居民个人工资薪金累计预扣税，并比较 H 年假、月末周六及日常加班的兑换策略。 |
| [technical-blog-writer](./technical-blog-writer/) | 撰写、改写或润色面向开发者与技术决策者的技术博客、产品文章、解决方案文章和教程，含资料核验、叙事设计、配图规划与去 AI 味。 |
| [open-source-solution-evaluator](./open-source-solution-evaluator/) | 评估开源项目是否值得制作成解决方案实践、SAC 或一键部署方案。 |
| [huawei-cloud-solution-asset-naming](./huawei-cloud-solution-asset-naming/) | 为华为云「解决方案实践」资产判断资产类型与场景分类，并生成中英文名称、URL ID 和产品标签。 |

每个 Skill 的核心规则都在 `SKILL.md`（两套系统共用）；`agents/openai.yaml` 是 Codex 专用的接口定义，Claude Code 会忽略它。

## 安装到 Claude Code

全局（个人自用，推荐）：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R china-personal-tax-optimizer technical-blog-writer open-source-solution-evaluator huawei-cloud-solution-asset-naming "$HOME/.claude/skills/"
```

项目级：

```bash
mkdir -p <项目>/.claude/skills
cp -R china-personal-tax-optimizer technical-blog-writer open-source-solution-evaluator huawei-cloud-solution-asset-naming <项目>/.claude/skills/
```

安装后重启 Claude Code 会话生效。无需 `$skill-name` 前缀：直接描述需求，Claude Code 会依据 `SKILL.md` 的 description 自动触发相关 Skill。

## 安装到 Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R china-personal-tax-optimizer technical-blog-writer open-source-solution-evaluator huawei-cloud-solution-asset-naming "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启 Codex 会话后，使用 `$skill-name` 前缀显式调用。