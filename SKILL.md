---
name: hymmnos
description: Use, understand, translate, and compose text in the Hymmnos language (Hymnos / tower language) from the Ar tonelico game series. Covers Standard Hymmnos (Central Standard Note) and Neopact Pastalie grammar, the complete lexicon with 800+ words, emotion sounds, emotion verbs, Binasphere Chorus encoding/decoding, pact spell lines, Ar Ciela, Carmena Foreluna, the writing system, and song types. Use this skill whenever the user mentions Hymmnos, Hymnos, tower language (塔语), emotion sounds (想音), emotion verbs (感音動詞), Binasphere Chorus (班氏吟唱), Ar tonelico song lyrics, EXEC_ or METHOD_ songs, or wants to translate, compose, analyze, or learn this constructed language. Also trigger when the user asks about Ar tonelico language, Ar ciela, Carmena Foreluna, Reyvateil language, or any phrase containing "Was yea ra" or similar Hymmnos emotion-sound patterns.
---

# Hymmnos Language

Hymmnos (ヒュムノス語) is a constructed language of emotion created by Akira Tsuchiya for the Ar tonelico video game series. Unlike natural languages that convey emotion through intonation, Hymmnos encodes emotion directly in its grammar and vocabulary, making it uniquely suited for expressing feelings and controlling Towers through Song Magic.

This skill enables translation, composition, grammar analysis, and vocabulary lookup for all forms of Hymmnos.

## When to Use

- Translate Hymmnos text to English/Chinese, or compose Hymmnos from English/Chinese
- Look up any Hymmnos word (pronunciation, meaning, word class, dialect)
- Analyze the grammar structure of Hymmnos sentences or song lyrics
- Encode or decode Binasphere Chorus (interleaved dual-line songs)
- Understand emotion sounds, emotion verbs, and their emotional encoding
- Research Hymmnos dialects, the writing system, song types, or lore

## Sentence Types

Hymmnos has four sentence types. Identify which one applies before proceeding:

1. **Emotion Sound sentence** (想音句) — Standard Hymmnos with a 3-word emotion prefix (e.g., "Was yea ra chs hymmnos mea"). ~80% of all Hymmnos text. Used in EXEC_ songs. Read [references/grammar-standard.md](references/grammar-standard.md).

2. **Emotion Verb sentence** (感音句) — Neopact Pastalie with bank-period verbs (e.g., "hEmmErYE/."). Compact encoding where a single word can be a complete sentence. Used in METHOD_ songs. Read [references/grammar-pastalie.md](references/grammar-pastalie.md).

3. **Binasphere Chorus** (班氏吟唱句) — Two lyric lines interleaved into one, decoded via a binary formula. Marked by "=>" and "EXEC hymme 2x1/0>>". Read [references/grammar-advanced.md](references/grammar-advanced.md).

4. **Emotionless sentence** — No emotion sound; standard SVO structure. Not processed by Towers (no Song Magic). Common in narrative passages.

## How to Translate or Compose

### Translating Hymmnos to English/Chinese

1. Identify the sentence type (see above)
2. Parse the emotion encoding first (emotion sounds or emotion vowels) — this sets the emotional context for the entire sentence
3. Look up each word in [references/lexicon.md](references/lexicon.md) (core vocabulary). For words not found there, read [references/lexicon-full.json](references/lexicon-full.json) for the complete 800+ entry index, or search the raw wiki source files in references/wiki-*.txt
4. Determine the sentence structure (self-type vs. non-self-type)
5. Translate the core meaning, then layer in the emotional nuance
6. Handle special constructs: rre (subject), na/zz (negation), re/eh (passive), oz (possession)

### Composing Hymmnos from English/Chinese

1. Choose the dialect: Standard (most common, EXEC_ songs) or Pastalie (compact, METHOD_ songs)
2. Select the emotion: for Standard, pick 3 words (intensity + type + desirability); for Pastalie, pick emotion vowels for the verb's bank periods
3. Find the verb in the lexicon
4. Find the object(s) in the lexicon
5. Assemble the sentence following the correct structure for the chosen dialect
6. Add particles, conjunctions, or modifiers as needed

## Key Reference Files

Load these as needed — do not read them all at once:

| File | Contents | When to read |
|------|----------|--------------|
| [references/grammar-standard.md](references/grammar-standard.md) | Emotion sounds, sentence structure, pronouns, passive, negation, possession, particles, persistent ES, numbers | Translating or composing Standard Hymmnos |
| [references/grammar-pastalie.md](references/grammar-pastalie.md) | Emotion verbs, bank periods, emotion vowels, noun prefixes, functions, quotation, passive, desire, nominalization | Translating or composing Pastalie Hymmnos |
| [references/grammar-advanced.md](references/grammar-advanced.md) | Binasphere Chorus encoding/decoding, pact spell lines, special characters, Carmena Foreluna, Ar Ciela | Working with Binasphere, pact lines, or ancient forms |
| [references/lexicon.md](references/lexicon.md) | Core high-frequency vocabulary with pronunciation, meanings (JP+EN), word class, dialect | Looking up common Hymmnos words |
| [references/lexicon-full.json](references/lexicon-full.json) | Metadata index for the complete 800+ word lexicon and 300+ unofficial words | Looking up rare words not in the core lexicon |
| [references/wiki-unofficial-vocab-zh.txt](references/wiki-unofficial-vocab-zh.txt) | Raw 300+ unofficial vocabulary from 歌颂之丘 wiki (Chinese, with Japanese prototypes and song sources) | Finding words from songs not in official Hymmnoserver |
| [references/examples.md](references/examples.md) | 45+ annotated example sentences from real songs with word-by-word glosses | Learning from real examples or verifying translations |
| [references/culture.md](references/culture.md) | Dialects, song types, servers, writing system, Hymmnos lore | Researching background context |

## Quick Reference

### Emotion Sound Structure (Standard)

`[intensity] [emotion type] [desirability]` — always first-person ("I")

- Intensity: Rrha (trance) > Was (very) > Wee (fairly) > Fou (a little) > Ma (calm) > Nn (apathetic)
- Emotion: yea (happy), ki (focused), num (nothing), guwo (angry), jyel (lonely), granme (protective), touwaka (hopeful), zweie (determined), au (sad), paks (excited), quel (desperate), i (impatient), wol (fervent), apea (blissful), yant (fearful), waa (happy, Metafalss)
- Desirability: ra (continue, default) > erra (forever) > ga (stop) > wa (accept) > gaya (never again) > gagis (indifferent)

### Emotion Vowel Structure (Pastalie)

Fill bank periods in emotion verbs with uppercase vowels:

- Level 1 (self): A (power), I (pain), U (sadness), E (joy), O (rage), N (calm)
- Level 2 (you): YA, YI, YU, YE, YO, YN
- Level 3 (world): LYA, LYI, LYU, LYE, LYO, LYN

### Pronouns

| Who | Object | Subject |
|-----|--------|---------|
| I/me | mea | mea |
| we/us | mean | merra |
| you (sg) | yor | yorr |
| you (pl) | yora | yorra |
| he | hes | herr |
| they (m) | hers | herra |
| she | has | harr |
| they (f) | hars | harra |

### Common Verbs

chs (become), sonwe (sing), hymme (sing/play/resonate), hyma (listen), pagle (speak), paul (feel), irs (exist), vit (see), knawa (know), fogabe (forgive), melenas (love), granme (protect), crushue (craft/weave), cexm (come), bexm (time comes), rete (forget), haf (have), echrra (resonate), parge (cut away), ks (soothe/influence)

### Negation and Passive

- Standard negation: `na` before the negated element (position controls scope)
- Pastalie negation: `zz` before the verb or noun
- Standard passive: `re` before verb; agent with `art` (by)
- Pastalie passive: `-eh` suffix on emotion verb

### Sentence End Markers (Pastalie)

- `/.` = sentence end + invoke (execute as Song Magic)
- `!` = sentence end without invoking
- `?` = question end without invoking

## Translation Tips

- Emotion sounds are often omitted in translation since English/Chinese express emotion through word choice
- The "ra" desirability word is near-meaningless due to overuse — usually safe to ignore
- No tenses exist in Hymmnos; time is implied by context or words like "ides" (past), "im" (now), "futare" (future)
- When translating songs, read [references/examples.md](references/examples.md) for patterns from real Hymmnos lyrics
- For Chinese translations, the Japanese meanings in the lexicon serve as a bridge since Hymmnos phonetics are Japanese-based
