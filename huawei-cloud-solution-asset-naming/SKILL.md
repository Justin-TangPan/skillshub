---
name: huawei-cloud-solution-asset-naming
description: >
  维护华为云「解决方案实践」结构化资产表，并为新增资产生成中英文名称、URL ID、场景分类和标签。
  Use this skill whenever the user mentions:
  - Huawei Cloud solution asset inventory, site synchronization, naming, classification, or metadata generation
  - Creating or organizing solution practices (解决方案实践) on Huawei Cloud
  - Generating Chinese/English names, URL IDs, or product tags for cloud assets
  - Classifying cloud solutions into scene categories (场景分类) like AI, data analytics, migration, etc.
  - Any task involving Huawei Cloud official asset metadata, solution practice publishing, or skill registration on Huawei Cloud platforms
  Trigger even if the request is in Chinese or mixes Chinese and English — this skill handles bilingual input.
---

# 华为云解决方案资产结构化管理

同时处理现网方案清单和单条资产元数据。不得把现网页面中没有的信息描述为官网事实。

## 现网清单与表格

标准工作簿为技能目录下的 `解决方案实践.xlsx`，字段顺序为：

`序号、主标签、一级场景、二级场景、解决方案名称、方案站点、方案名或实践名（英文）、ID编码、官网链接、简述、其他标签、备注`

需要创建、刷新或补充清单时，运行：

```bash
python scripts/sync_solution_practices.py [工作簿路径]
```

脚本读取中国站和国际站的解决方案实践页。页面源码中的卡片数组为正序，官网界面以反向顺序展示；必须先反转各站点原始数组，再按官网原生展示顺序生成行，表内序号仍从 1 递增，不得用 Excel 序号降序代替官网顺序。工作簿不存在时创建；存在时按官网 URL ID、规范化标题合并，按表头名写入以兼容列顺序调整，并保留已有样式、列宽和冻结窗格。站点写为`中国站`、`国际站`或`中国站、国际站`。页面结构变化或请求失败时停止并报告，不用旧数据冒充最新结果。

同步后检查备注。脚本只能可靠填写官网公开字段；对标记为“待补充英文名称和二级场景”的新增行，按本技能其余规则补齐后再交付。若官网名称违反下述命名规则，只在最右侧`备注`列说明，不擅自改写官网现名。

用户要求把一个新方案加入工作簿时，先生成完整七字段元数据，再通过 `--record-json` 写入；JSON 使用表头字段名，例如：

```bash
python scripts/sync_solution_practices.py 解决方案实践.xlsx --record-json '{"解决方案名称":"示例名称","方案名或实践名（英文）":"Example Name","ID编码":"example-name","一级场景":"AI","二级场景":"Agent与知识应用","主标签":"应用方案","其他标签":"","官网链接":"","简述":"示例简介","方案站点":""}'
```

未发布资产的`官网链接`和`方案站点`留空。已发布资产必须以现网结果为准。不要仅因名称相似覆盖另一条资产；有歧义时保留为新行并在备注说明。

只要求单条命名而未要求维护表格时，不修改工作簿，按文末七字段格式回答。

## 资产类型与命名

主标签只能选择一个：

名称由项目名与价值描述组成时，中英文均使用单个空格分隔，不使用逗号、冒号或破折号。

- `应用方案`：交付物是可部署、运行或使用的应用或软件。中文名保留项目名称并突出核心价值；不得加入"快速部署""免费试用""一键部署"。示例：`Hermes Agent 越用越聪明的智能体`。
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

单条命名请求严格输出以下七个字段，每个字段之间空一行。不要使用代码块、列表或补充说明；没有其他标签时保留冒号后空白。表格维护请求则交付工作簿及同步摘要，不套用此格式。

```text
方案名或实践名：XXX

方案名或实践名（英文）：XXX

ID编码：xxx-xxx-xxx

一级场景：XXX

二级场景：XXX

主标签：应用方案 / 最佳实践 / Skills

其他标签：XXX
```
