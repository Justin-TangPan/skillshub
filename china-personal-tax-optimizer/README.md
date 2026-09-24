# 中国个税与 H 兑换优化 Skill

按中国居民个人工资薪金累计预扣法，逐月模拟个税，并比较 H 年假、月末周六及日常加班的现金兑换与调休策略。

默认数据为：标准工资 18,500 元/月、绩效工资 5,000 元/月、年假 10 天、月末周六加班 12 天、未配股、专项附加扣除 2,500 元/月、深圳个人三险一金比例 15.2%。调用时可以覆盖任一参数。

## 使用示例

Codex 显式调用：

```text
$china-personal-tax-optimizer 使用默认数据，比较不兑换、每月兑换、12 月集中兑换和智能分月四种策略。
```

```text
$china-personal-tax-optimizer 我的标准工资是 25,000 元，绩效 8,000 元，专项附加扣除每月 4,000 元，有 8 天月末周六加班，请生成逐月税额和最优兑换建议。
```

Claude Code 中无需 `$` 前缀，直接描述需求（例如“比较不兑换、每月兑换、12 月集中兑换和智能分月四种策略”）即可由模型依据 `SKILL.md` 自动触发。

技能会输出逐月模拟表、年度策略汇总、税档空间、年假补偿对次年税档的影响，并区分税额、税后现金和调休价值。税法、深圳缴费口径及 H 内部规则可能调整，正式决策前应以目标年度官方政策和公司系统为准。

## 安装

### Claude Code

全局（个人自用）：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R china-personal-tax-optimizer "$HOME/.claude/skills/"
```

或项目级：

```bash
mkdir -p <项目>/.claude/skills
cp -R china-personal-tax-optimizer <项目>/.claude/skills/
```

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R china-personal-tax-optimizer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启会话后即可使用。