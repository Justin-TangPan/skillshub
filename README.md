# skillshub

个人自用 Skills 集合。

| Skill | 说明 |
|---|---|
| [china-personal-tax-optimizer](./china-personal-tax-optimizer/) | 模拟中国居民个人工资薪金累计预扣税，并比较 H 年假、月末周六及日常加班的兑换策略。 |
| [technical-blog-writer](./technical-blog-writer/) | 撰写、改写或润色面向开发者与技术决策者的技术博客、产品文章、解决方案文章和教程，含资料核验、叙事设计、配图规划与去 AI 味。 |
| [open-source-solution-evaluator](./open-source-solution-evaluator/) | 评估开源项目是否值得制作成解决方案实践、SAC 或一键部署方案。 |
| [huawei-cloud-solution-asset-naming](./huawei-cloud-solution-asset-naming/) | 为华为云「解决方案实践」资产判断资产类型与场景分类，并生成中英文名称、URL ID 和产品标签。 |

## 安装到 Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R china-personal-tax-optimizer technical-blog-writer open-source-solution-evaluator huawei-cloud-solution-asset-naming "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## 安装到 Claude Code（项目级）

```bash
mkdir -p <项目>/.claude/skills
cp -R china-personal-tax-optimizer technical-blog-writer open-source-solution-evaluator huawei-cloud-solution-asset-naming <项目>/.claude/skills/
```

重启会话后生效。
