# 开源解决方案实践评估 Skill

用于评估公开开源项目是否适合制作成解决方案实践、SAC 或一键部署方案。

## 安装

下载本仓库后，在仓库根目录执行：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R open-source-solution-evaluator "${CODEX_HOME:-$HOME/.codex}/skills/"
```

请复制整个目录，不要只复制 `SKILL.md`；评估报告依赖 `references/report-template.md`。

重启 Codex 后即可使用：

```text
$open-source-solution-evaluator 评估 https://github.com/owner/project 是否值得制作成解决方案实践。
```

