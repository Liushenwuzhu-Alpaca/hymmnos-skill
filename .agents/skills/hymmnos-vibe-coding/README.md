# Hymmnos Vibe Coding / ヒュムノス・バイブコーディング

[English](#english) | [中文](#中文) | [日本語](#日本語)

---

<a id="中文"></a>
## 中文

将 Hymmnos（ヒュムノス語/塔语）作为"情感编程语言"编译为可执行的 Python 代码。想音编码意图上下文，动词映射为编程动作，`/.` 触发立即执行。

### 架构

```
Hymmnos 句子 → 解析器 → IR (JSON) → 代码生成器 → Python
```

LLM 在此架构中扮演"编译器"角色——解析 Hymmnos 的情感语义，生成结构化意图表示（IR），再由代码生成器输出可执行代码。

### 依赖

本技能**强依赖** `hymmnos` 语言技能提供的语法和词典参考。

```bash
# 先安装语言技能
npx skills add Liushenwuzhu-Alpaca/hymmnos-skill
# 再安装本编译器技能
npx skills add Liushenwuzhu-Alpaca/hymmnos-vibe-coding
```

### 用法

```bash
# 解析 Hymmnos 句子
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea"

# 解析并生成 Python 代码
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea" --generate
```

### Hymmnos → 编程映射

| Hymmnos | 编程概念 |
|---------|---------|
| 想音 (Was yea ra) | 意图上下文 / EmotionContext |
| 动词 (chs, sonwe) | 函数调用 |
| 名词 (ciel, mea) | 对象/变量 |
| na / zz | 逻辑取反 |
| /. | 立即执行 |
| ! | 仅声明（不执行） |
| Binasphere | 并行执行 |
| Xc= → | 条件语句 |

### 开源协议

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

<a id="english"></a>
## English

Compile Hymmnos sentences into executable Python code. Emotion sounds encode intent, verbs map to actions, `/.` triggers execution.

### Architecture

```
Hymmnos sentence → Parser → IR (JSON) → Code Generator → Python
```

### Dependency

Requires the `hymmnos` language skill for grammar and vocabulary.

```bash
npx skills add Liushenwuzhu-Alpaca/hymmnos-skill
npx skills add Liushenwuzhu-Alpaca/hymmnos-vibe-coding
```

### License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

<a id="日本語"></a>
## 日本語

ヒュムノス語を「感情プログラミング言語」としてPythonコードにコンパイルします。

### 依存

`hymmnos` 言語スキルが必須です。

```bash
npx skills add Liushenwuzhu-Alpaca/hymmnos-skill
npx skills add Liushenwuzhu-Alpaca/hymmnos-vibe-coding
```

### ライセンス

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
