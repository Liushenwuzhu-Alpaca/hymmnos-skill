---
name: hymmnos-vibe-coding
description: Compile Hymmnos language sentences into executable Python code using emotion-driven intent programming. Treats Hymmnos emotion sounds as intent context, verbs as programming actions, and /. as execution triggers. Use this skill whenever the user wants to use Hymmnos as a programming language, compile Hymmnos to code, do vibe coding with Hymmnos, or experiment with emotion-driven code generation. Also trigger when the user mentions "hymmnos compiler", "hymmnos vibe coding", "emotion programming", or wants to generate code from Hymmnos sentences. This skill depends on the hymmnos language skill for grammar and vocabulary reference.
---

# Hymmnos Vibe Coding

Compile Hymmnos sentences into executable Python code. Hymmnos becomes a "vibe coding" language where emotion sounds encode intent context, verbs map to programming actions, and `/.` triggers immediate execution.

## Architecture

```
Hymmnos sentence
      │
      ▼
  LLM Parser          ← Uses hymmnos skill's grammar + lexicon to parse semantics
      │
      ▼
  IR (JSON)           ← Structured intent: emotion context + action + objects + mode
      │
      ▼
  Code Generator      ← Maps IR to Python code with EmotionContext
      │
      ▼
  Executable Python
```

The LLM serves as the "compiler" — it parses Hymmnos emotion semantics and produces a structured Intent Representation (IR), then generates code from it. This is the key difference from a pure rule-based parser: the LLM understands the emotional nuance, handles unknown vocabulary by inference, and can generate contextually appropriate code.

## Dependency

This skill **requires** the `hymmnos` language skill for grammar and vocabulary reference. Before using the compiler:

1. Read the hymmnos skill's SKILL.md at the path resolved from the `hymmnos` skill installation
2. Load [references/grammar-standard.md](references/grammar-standard.md) for emotion sound parsing rules
3. Load [references/lexicon.md](references/lexicon.md) for word-to-action mapping

If the `hymmnos` skill is not installed:
```bash
npx skills add Liushenwuzhu-Alpaca/hymmnos-skill
```

## How to Use

### Step 1: Parse the Hymmnos sentence

Feed the Hymmnos sentence to the compiler script:

```bash
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea"
```

This produces a structured IR (Intermediate Representation) in JSON:

```json
{
  "sentence_type": "standard",
  "emotion": {"intensity": "very", "emotion": "happy", "desire": "continue"},
  "action": "transform",
  "objects": [{"word": "hymmnos", "type": "output"}, {"word": "mea", "type": "self"}],
  "invoke": true
}
```

### Step 2: Generate Python code

Add `--generate` to produce executable Python:

```bash
python scripts/hymmnos_compiler.py "Was yea ra chs hymmnos mea" --generate
```

### Step 3: Execute the generated code

The generated code is self-contained and can be run directly.

### Step 4: For LLM-enhanced parsing

For sentences with vocabulary not in the compiler's hardcoded dictionary, use the LLM as the parser instead:

1. Read the hymmnos skill's lexicon reference files
2. Parse the Hymmnos sentence manually using the grammar rules
3. Construct the IR JSON by hand (following the same schema)
4. Pass the IR to the code generator

This is the "LLM as compiler" mode — the LLM understands semantics that the rule-based parser cannot.

## Mapping: Hymmnos → Programming

| Hymmnos | Programming Concept |
|---------|-------------------|
| Emotion Sound (Was yea ra) | Intent context / EmotionContext |
| Verb (chs, sonwe, ruinie) | Function call / action |
| Noun (hymmnos, ciel, mea) | Object / variable / type |
| Particle (tes, anw, en) | Parameter binding / conjunction |
| na / zz | Logical negation |
| re / -eh | Passive transformation |
| /. | Execute immediately (invoke) |
| ! / ? | Declare only (no execution) |
| rre | Variable assignment (subject binding) |
| 0x vvi. ... 1x AAs ixi. | Scope / context block |
| Binasphere (2x1/0) | Parallel execution (two threads) |
| Xc= ... -> ... | Conditional (if...then) |
| -> (function) | Macro definition |
| <-x | Variable reference |

## Examples

**Standard sentence:**
```
Was yea ra chs hymmnos mea
→ EmotionContext(happy, very, continue) + transform(self → song)
→ def transform(ctx): ... return result
```

**Negation:**
```
Was yea ra na chs hymmnos yor
→ EmotionContext(happy, very, continue) + NOT transform(you → song)
→ result = not _do_transform(ctx)
```

**Pastalie emotion verb:**
```
hEmmErYE/.
→ EmotionContext(joy) + sing()
→ def sing(ctx): ... return result
```

**Angry destruction:**
```
Was guwo ga ruinie ar ciel
→ EmotionContext(angry, very, stop) + destroy(the world)
→ def destroy(ctx): ... return result
```

## Reference Files

| File | Contents |
|------|----------|
| [scripts/hymmnos_compiler.py](scripts/hymmnos_compiler.py) | Rule-based compiler: Hymmnos → IR → Python |
| [references/grammar-standard.md](references/grammar-standard.md) | Standard Hymmnos grammar (copy from hymmnos skill) |
| [references/lexicon.md](references/lexicon.md) | Core vocabulary mapping (copy from hymmnos skill) |
