---
name: huawei-cloud-solution-asset-naming
description: >
  为华为云「解决方案实践」资产判断资产类型与场景分类，并生成中英文名称、URL ID 和产品标签。
  Use this skill whenever the user mentions:
  - Huawei Cloud solution asset naming, classification, or metadata generation
  - Creating or organizing solution practices (解决方案实践) on Huawei Cloud
  - Generating Chinese/English names, URL IDs, or product tags for cloud assets
  - Classifying cloud solutions into scene categories (场景分类) like AI, data analytics, migration, etc.
  - Any task involving Huawei Cloud official asset metadata, solution practice publishing, or skill registration on Huawei Cloud platforms
  Trigger even if the request is in Chinese or mixes Chinese and English — this skill handles bilingual input.
---

# 华为云解决方案资产命名

根据用户输入在内部完成判断，只输出最终结果，不展示分析、候选名称或额外字段。

## 资产类型与命名

主标签只能选择一个：

- `应用方案`：交付物是可部署、运行或使用的应用或软件。中文名保留项目名称并突出核心价值；不得加入"快速部署""免费试用""一键部署"。示例：`Hermes Agent，越用越聪明的智能体`。
- `最佳实践`：交付物是可按步骤完成的场景实践，包含架构、方法、配置或操作步骤。优先命名为"基于 XXX 构建 XXX""基于 XXX 实现 XXX"，也可使用简洁明确的场景名。
- `Skills`：交付物是一个或多个 Skill 形成、可在 OfficeAce、码道或 AgentArts 中长期使用的能力。标题直接表达业务能力，默认不出现 OfficeAce、码道、AgentArts、Skill、Skills，也不使用"XX助手""XX专家""XX Agent""XX神器"。

## 场景分类

以用户最终解决的问题为准，不因使用 AI、Agent 或 Skill 就默认归类为 AI。一级与二级必须使用以下有效组合之一：

| 一级场景 | 二级场景 |
|---|---|
| `AI` | `Agent与知识应用` |
| `AI` | `大模型与AI平台` |
| `数据分析与管理` | `数据平台与计算` |
| `数据分析与管理` | `智能问数与数据Agent` |
| `应用现代化` | `云原生与DevOps` |
| `应用现代化` | `应用与服务器` |
| `应用现代化` | `应用与内容加速` |
| `应用现代化` | `行业应用与HPC` |
| `网络` | `网络连接与公网` |
| `安全与合规` | `安全防护` |
| `安全与合规` | `安全合规` |
| `云迁移` | `数据迁移与容灾` |
| `运维监控` | `监控、日志与运维工具` |

例如，自然语言查询 DWS 数据归为`数据分析与管理 / 智能问数与数据Agent`；通过 Skill 巡检云资源归为`运维监控 / 监控、日志与运维工具`。

## 其他标签

只能使用 `OfficeAce`、`码道`、`AgentArts`、`免费试用`：

- 明确以某产品为主要用户入口及长期承载产品时，添加该产品标签。
- 多个产品同时出现时，只标记主要入口和长期承载产品，不全部添加。
- 仅在明确已提供免费试用能力时添加`免费试用`。
- 没有适用标签时留空，不自行生成其他标签。

## 英文名称与 ID

- 英文名与中文名含义一致，使用自然、简洁且适合官网展示的英文，不逐字硬译；保留官方产品及项目英文名称。
- ID 由英文名生成：全部小写，单词间用 `-`，删除标点，将 `&` 转为 `and`，最终只能包含 `a-z`、`0-9`、`-`。

## 输出格式

严格输出以下七个字段，每个字段之间空一行。不要使用代码块、列表或补充说明；没有其他标签时保留冒号后空白。

```text
方案名或实践名：XXX

方案名或实践名（英文）：XXX

ID编码：xxx-xxx-xxx

一级场景：XXX

二级场景：XXX

主标签：应用方案 / 最佳实践 / Skills

其他标签：XXX
```
