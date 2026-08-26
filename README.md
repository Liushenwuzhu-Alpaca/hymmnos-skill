# Hymmnos Language Skill / ヒュムノス語スキル

[English](#english) | [中文](#中文) | [日本語](#日本語)

---

<a id="中文"></a>
## 中文

一个面向 AI 代理的 Hymmnos（ヒュムノス語/塔语）语言技能包。Hymmnos 是 Gust 公司《魔塔大陆》（Ar tonelico）系列游戏中由土屋晓（Akira Tsuchiya）创造的构造语言，以"情感"为核心设计——情感不靠语调传达，而是直接编码进语法和词汇中，使其成为表达情感与控制塔的诗魔法语言。

### 功能

- **翻译**：Hymmnos ↔ 中文/英文双向翻译
- **查词**：查阅任何 Hymmnos 词汇的发音、含义、词性、方言
- **语法分析**：解析 Hymmnos 句子或歌词的语法结构
- **Binasphere 编解码**：二进制模式的双行合唱编码/解码
- **情感系统**：理解想音（想音）、感音动词（感音動詞）及其情感编码
- **世界观研究**：方言、文字系统、歌曲类型、诗魔法服务器等背景设定
- **Vibe Coding**：将 Hymmnos 作为意图编程语言，编译为可执行的 Python 代码

### 目录结构

```
├── SKILL.md                         # 技能路由文件（含快速参考）
├── references/
│   ├── grammar-standard.md          # 标准语法：想音、句法、被动、否定、所有格
│   ├── grammar-pastalie.md          # 新约帕斯塔利埃语法：感音动词、库句点、想母音
│   ├── grammar-advanced.md          # 高级语法：Binasphere、契约咒文、律史前月读、Ar Ciela
│   ├── lexicon.md                   # 核心高频词表（~300词）
│   ├── lexicon-full.json            # 全量词典数据库（518条）
│   ├── examples.md                  # 45+真实歌曲例句（含逐词注释）
│   ├── culture.md                   # 方言、歌曲类型、服务器、文字系统、历史
│   ├── wiki-hymmnos-lang-zh.txt     # 歌颂之丘wiki中文语法原文
│   ├── wiki-pastalie-grammar-zh.txt # 歌颂之丘wiki Pastalie语法原文
│   └── wiki-unofficial-vocab-zh.txt # 300+非官方词汇（歌颂之丘wiki）
├── scripts/
│   └── hymmnos_compiler.py          # Hymmnos → IR → Python Vibe Coding 编译器
└── evals/
    └── evals.json                   # 技能评估测试用例
```

### 词汇覆盖

| 来源 | 词数 |
|------|------|
| 官方词汇（EXA_PICO Wiki / Hymmnoserver） | ~1,050 |
| 非官方词汇（歌颂之丘wiki，出自歌曲但未收入官方词典） | ~560 |
| **合计去重** | **~1,500** |

覆盖六大方言：中央正纯律、库尔特谢尔律、克拉斯塔律、阿尔法律、古梅塔法尔斯律、新约帕斯塔利埃。

### Vibe Coding 编译器

`scripts/hymmnos_compiler.py` 是一个概念原型，将 Hymmnos 作为"情感编程语言"——想音编码意图上下文，动词映射为编程动作，`/.` 触发立即执行。

```bash
# 解析 Hymmnos 句子并显示中间表示
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea"

# 解析并生成可执行的 Python 代码
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea" --generate
```

架构：`Hymmnos 句子 → 解析器 → IR (JSON) → 代码生成器 → Python`

### 安装

```bash
npx skills add Liushenwuzhu-Alpaca/hymmnos-skill
```

### 测试结果

第一轮迭代评估（3个测试用例，对比有技能 vs 无技能）：

| 测试 | 有技能 | 无技能 |
|------|--------|--------|
| 翻译标准句 | 5/5 (100%) | 4/5 (80%) |
| 原创造句 | 5/5 (100%) | 2/5 (40%) |
| 翻译 Pastalie 句 | 5/5 (100%) | 3/5 (60%) |
| **平均** | **100%** | **60%** |

### 数据来源

- [EXA_PICO Wiki](https://exapico.wiki.gg/wiki/Hymmnos:Lexicon) — 全量词典与语法
- [Hymmnoserver](https://hymmnoserver.uguu.ca/) — 语法、类型、方言、服务器
- [kwhazit Hymmnos Reference](https://kwhazit.ucoz.net/trans/music/HymmnosReference.html) — 详细语法与例句
- [歌颂之丘 wiki](https://wiki.singinghill.top/) — 中文wiki（通过 scrapling 绕过 Cloudflare 获取）
- [萌娘百科](https://zh.moegirl.org.cn/zh-cn/塔语) — 中文百科词条
- [时度度的笔记本](https://note.timedegree.cc/sd/hymmnos/) — 中文语法教程
- [LP Archive](https://lparchive.org/Ar-Tonelico-II/Update%2061/) — 英文语法指南
- [felesatra.moe](https://www.felesatra.moe/blog/2015/01/04/hymmnos-quatrasphere) — Binasphere 分析

### 开源协议

本项目为粉丝制作的教育研究用汇编。Hymmnos 及所有相关内容由土屋晓创造，版权归 Gust Co., Ltd. 所有。

本技能包的汇编内容采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 协议发布。

---

<a id="english"></a>
## English

An AI agent skill for the Hymmnos constructed language (ヒュムノス語) from the Ar tonelico video game series by Gust. Created by Akira Tsuchiya, Hymmnos is a "language of emotions" that encodes feelings directly into its grammar and vocabulary, making it uniquely suited for expressing emotions and controlling Towers through Song Magic.

### Features

- **Translate** Hymmnos ↔ English/Chinese
- **Look up** vocabulary (pronunciation, meaning, word class, dialect)
- **Analyze** grammar structure of sentences and song lyrics
- **Encode/decode** Binasphere Chorus (binary-pattern dual-line songs)
- **Understand** emotion sounds, emotion verbs, and emotional encoding
- **Research** dialects, writing system, song types, and lore
- **Vibe Coding** — compile Hymmnos into executable Python code

### Installation

```bash
npx skills add Liushenwuzhu-Alpaca/hymmnos-skill
```

### Vibe Coding Compiler

```bash
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea" --generate
```

Architecture: `Hymmnos sentence → Parser → IR (JSON) → Code Generator → Python`

### Vocabulary Coverage

~1,500 total entries: ~1,050 official (EXA_PICO Wiki / Hymmnoserver) + ~560 unofficial (歌颂之丘 wiki). Covers 6 dialects.

### Test Results

With skill: 100% avg pass rate vs without skill: 60% (3 test cases, 5 assertions each).

### License

Fan-made compilation for educational purposes. Hymmnos and all related content created by Akira Tsuchiya, © Gust Co., Ltd. Compilation released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

---

<a id="日本語"></a>
## 日本語

Ar tonelico（魔塔大陸）シリーズに登場するヒュムノス語のためのAIエージェントスキル。土屋曉氏によって創造されたヒュムノス語は、「感情の言語」であり、感情を直接的に文法と語彙にエンコードする特徴を持ちます。

### 機能

- **翻訳**：ヒュムノス語 ↔ 日本語/英語/中国語
- **辞書検索**：発音、意味、品詞、音律の検索
- **文法解析**：文や歌詞の文法構造の分析
- **バイナスフィアーコーラス**：二進パターンの二重合唱のエンコード/デコード
- **想音システム**：想音、感音動詞と感情エンコードの理解
- **世界観研究**：音律、文字体系、詩の種類、サーバー等の背景設定
- **Vibe Coding**：ヒュムノス語を意図プログラミング言語としてPythonコードにコンパイル

### インストール

```bash
npx skills add Liushenwuzhu-Alpaca/hymmnos-skill
```

### 語彙規模

約1,500語：公式語彙約1,050語（EXA_PICO Wiki / Hymmnoserver）＋非公式語彙約560語（歌頌之丘wiki）。6つの音律をカバー。

### ライセンス

ファン制作の教育研究用編纂物。ヒュムノスおよび関連コンテンツは土屋曉氏の創造物、著作権はGust Co., Ltd.に帰属します。編纂内容は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) で公開されています。
