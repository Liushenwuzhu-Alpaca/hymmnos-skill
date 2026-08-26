# Hymmnos Language Skill

An AI agent skill for the Hymmnos constructed language (ヒュムノス語) from the Ar tonelico video game series by Gust. Created by Akira Tsuchiya, Hymmnos is a "language of emotions" that encodes feelings directly into its grammar and vocabulary, making it uniquely suited for expressing emotions and controlling Towers through Song Magic.

## What This Skill Does

- **Translate** Hymmnos text to English/Chinese, and compose Hymmnos from English/Chinese
- **Look up** any Hymmnos word (pronunciation, meaning, word class, dialect)
- **Analyze** the grammar structure of Hymmnos sentences or song lyrics
- **Encode/decode** Binasphere Chorus (interleaved dual-line songs with binary patterns)
- **Understand** emotion sounds (想音), emotion verbs (感音動詞), and their emotional encoding
- **Research** Hymmnos dialects, the writing system, song types, and lore

## Skill Structure

```
├── SKILL.md                         # Router file with quick reference (120 lines)
├── references/
│   ├── grammar-standard.md          # Standard Hymmnos: emotion sounds, sentence structure, passive, negation
│   ├── grammar-pastalie.md          # Neopact Pastalie: emotion verbs, bank periods, emotion vowels
│   ├── grammar-advanced.md          # Binasphere Chorus, pact spell lines, Carmena Foreluna, Ar Ciela
│   ├── lexicon.md                   # Core high-frequency vocabulary (~300 words)
│   ├── lexicon-full.json            # Full lexicon database (518 entries)
│   ├── examples.md                  # 45+ annotated example sentences from real songs
│   ├── culture.md                   # Dialects, song types, servers, writing system, lore
│   ├── wiki-hymmnos-lang-zh.txt     # Chinese grammar source (歌颂之丘 wiki)
│   ├── wiki-pastalie-grammar-zh.txt # Chinese Pastalie grammar source
│   └── wiki-unofficial-vocab-zh.txt # 300+ unofficial vocabulary (歌颂之丘 wiki)
├── scripts/
│   └── hymmnos_compiler.py          # Hymmnos → IR → Python vibe coding compiler
└── evals/
    └── evals.json                   # Test cases for skill evaluation
```

## Coverage

### Grammar
- Standard Hymmnos (Central Standard Note) — emotion sound sentences, ~80% of all text
- Neopact Pastalie — emotion verb sentences with bank period system
- Binasphere Chorus — binary-encoded dual-line song interleaving
- Carmena Foreluna (Preformalized Lunar Chant) — letter-level meaning system
- Ar Ciela — planetary language with frequency-based meaning
- Pact Spell Lines — Connection/Activation lines for Tower access

### Vocabulary
- ~1,050 official words (from EXA_PICO Wiki / Hymmnoserver)
- ~560 unofficial words (from 歌颂之丘 wiki, appearing in songs but not in official dictionary)
- ~1,500 total entries covering 6 dialects

### Dialects
- Central Standard Note (中央正純律)
- Kurt Ciel Note (クルトシエール律)
- Cluster Note (クラスタ律)
- Alpha Note (アルファ律)
- Ancient Metafalss Note (古メタファルス律)
- New Testament of Pastalie (新約パスタリエ)

## Hymmnos Vibe Coding Compiler

The `scripts/hymmnos_compiler.py` is a concept prototype that treats Hymmnos as a "vibe coding" language — where emotion sounds encode intent context, verbs map to programming actions, and `/.` (invoke) triggers immediate execution.

```bash
# Parse a Hymmnos sentence and show its intermediate representation
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea"

# Parse and generate Python code
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea" --generate
```

Architecture: `Hymmnos sentence → Parser → IR (JSON) → Code Generator → Python`

The compiler maps:
- Emotion sounds → `EmotionContext` (intensity, emotion, desire)
- Verbs → programming actions (chs→transform, sonwe→generate, ruinie→destroy, ...)
- Nouns → object types (ciel→environment, mea→self, yor→user, ...)
- `na`/`zz` → logical negation
- `re`/`-eh` → passive transformation
- `/.` → immediate execution; `!` → declaration only (lambda)

## Sources

Compiled from multiple authoritative sources:

- [EXA_PICO Wiki](https://exapico.wiki.gg/wiki/Hymmnos:Lexicon) — Full lexicon and grammar
- [Hymmnoserver](https://hymmnoserver.uguu.ca/) — Grammar pages, types, dialects, servers
- [kwhazit Hymmnos Reference](https://kwhazit.ucoz.net/trans/music/HymmnosReference.html) — Detailed grammar with examples
- [歌颂之丘 wiki](https://wiki.singinghill.top/) — Chinese wiki (accessed via scrapling Cloudflare bypass)
- [萌娘百科](https://zh.moegirl.org.cn/zh-cn/塔语) — Chinese encyclopedia
- [时度度的笔记本](https://note.timedegree.cc/sd/hymmnos/) — Chinese grammar tutorial
- [LP Archive](https://lparchive.org/Ar-Tonelico-II/Update%2061/) — Let's Play grammar guide
- [felesatra.moe](https://www.felesatra.moe/blog/2015/01/04/hymmnos-quatrasphere) — Binasphere analysis

## Installation

```bash
npx skills add Liushenwuzhu-Alpaca/hymmnos-skill
```

## Test Results

First iteration evaluation (3 test cases, with-skill vs baseline):

| Test | With Skill | Without Skill |
|------|-----------|---------------|
| Translate standard sentence | 5/5 (100%) | 4/5 (80%) |
| Compose original sentence | 5/5 (100%) | 2/5 (40%) |
| Translate Pastalie sentence | 5/5 (100%) | 3/5 (60%) |
| **Average** | **100%** | **60%** |

## License

This skill is a fan-made compilation for educational and research purposes. Hymmnos and all related content are created by Akira Tsuchiya and owned by Gust Co., Ltd.
