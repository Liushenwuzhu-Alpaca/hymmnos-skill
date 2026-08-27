# Neopact Pastalie Grammar (New Testament of Pastalie)

Pastalie is a streamlined dialect for Infel Phira server, used in METHOD_ songs. Its core principle: express maximum meaning and emotion with minimum words. A single Emotion Verb can be a complete sentence.

## Emotion Verbs

Emotion Verbs combine a **template** (lowercase base verb with bank periods) and **Emotion Vowels** (uppercase fillers).

### Template Words

Template words contain dots (periods) called **Bank Slots**:
- `h.m.m.r.` = sing (4 bank slots)
- `c.z.` = become/transform (2 bank slots)
- `f.w.r.n.` = embrace (4 bank slots)

Bank slots are numbered 1..n from left to right. Lower index = greater effect and priority. Unused slots are simply omitted from the final word.

### Emotion Vowels

Three categories, used interchangeably to reflect the speaker's emotions:

**Level 1 - Emotions toward self:**

| Vowel | Meaning |
|-------|---------|
| A | power, eagerness, focus |
| I | pain, want to flee, dread |
| U | sadness, grief, worry |
| E | joy, contentment, pleasure |
| O | anger, aggression, cursing |
| N | nothing, absent-minded, relaxed |

**Level 2 - Emotions toward another individual:**

| Vowel | Meaning |
|-------|---------|
| YA | want to serve, thinking of you |
| YI | suffering, pain, death |
| YU | sadness, anxiety |
| YE | happiness, fortune |
| YO | anger, rage |
| YN | calmness, comfort |

**Level 3 - Emotions toward surroundings/world:**

| Vowel | Meaning |
|-------|---------|
| LYA | thinking of all, want to devote myself |
| LYI | pain, destruction, ruin |
| LYU | sadness, unease, instability |
| LYE | happiness, satisfaction, prosperity |
| LYO | strife, chaos, war |
| LYN | calmness, quietness |

### Constructing Emotion Verbs

Replace bank periods with emotion vowels (uppercase). Unused slots disappear:

- `h.m.m.r.` + E, none, E, YE → `hEmmErYE` = "I will happily sing for your happiness"
- `c.z.` + E, E → `cEzE` = "I gladly become" (≈ "Was yea ra chs")
- `c.z.` + YE, YE → `cYEzYE` = "You become (and I want you to be happy)"
- `c.z.` + LYE, LYE → `cLYEzLYE` = targeting the situation/world

When the object is clear from the emotion vowels, the Emotion Verb alone is a complete sentence. Otherwise, add an explicit object after:
- `fEwErYEn/.` = I lovingly embrace you
- `fEwErYEn Luca/.` = I lovingly embrace Luca

### Direction Shifting

In second/third-person sentences, emotion vowel orientation shifts to match the subject. Level 1 now means "the subject feels" rather than "I feel."

## Sentence Structure

### First-Person

```
[Emotion Verb] + [object] + [compound]
```
Or just the Emotion Verb alone if the object is implied.

### Non-First-Person

```
[x.] + rre + [subject] + [Emotion Verb] + [object] + [compound]
```

`x.` carries a bank slot for the singer's feelings about the subject:

| Vowel in x. | Meaning |
|-------------|---------|
| A | indifferent |
| I | jealous |
| U | concerned |
| E | happy |
| O | angry |
| N | opposed |

Subject-form pronouns may omit `rre`. Using `rre` with a pronoun emphasizes it.

Examples:
- `xE rre cloche cEzE hymmnos/.` = Cloche becomes song (and this makes me happy)
- `xI harr cEzE hymmnos/.` = She becomes song (and I'm jealous)
- `xE rre yorra cEzE hymmnos/.` = YOU ALL become song (emphasized)

## Noun Possession

Emotion Vowel prefixes on nouns indicate ownership + emotional attachment:

| Owner | Form | Example |
|-------|------|---------|
| me | A[noun] | Agasar = my stuffed doll |
| you | YA[noun] | YAgasar = your doll |
| everyone/world | LYA[noun] | LYAgasar = everyone's doll |
| specific person | A[noun]_[name] | Agasar_cloche = Cloche's doll |

Other vowels may indicate specific emotions toward the possession. Based on Japanese [noun]の[noun], the second noun can modify/describe the first: `Ahiew_ayulsa` = eternal sadness (not "eternity's sadness").

## Grammatical Features

### Sentence Termination

- `/.` = sentence end + invoke (execute as Song Magic)
- `!` = sentence end without invoking
- `?` = question end without invoking

### Passive Voice

Append `-eh` to the Emotion Verb:
- `fEwErYEn` = I embrace you (active)
- `fEwErYEneh` = I am embraced by you (passive)

### Negation

Place `zz` before the Emotion Verb or noun:
- `zz hEmmErYE/.` = I would NOT be delighted to sing
- `zz arhou` = despair (negating "hope")
- `zz Agasar` = not my plushie

### Desire (Want to do)

Append `-aye` to the Emotion Verb:
- `hEmmrEaye` = want to sing

### Nominalization

Keep all bank periods as periods to use an Emotion Verb as a noun/gerund:
- `aIuUkA zess pop v.a en d.z./.` = Birth and death are like a bubble

Also use suffix `-za`:
- `hLYEmEmErza` = the singing (nominalized)

### Quotation

Between `:/` and `/:`:
- `:/futare/:` = "future" (quoted)

### Functions

Define a macro for a complete passage:
```
[function name] -> [Hymmnos passage]
```
`->` is pronounced "pass". The function is valid only within the song where defined.

Example:
```
ishikawa -> jYOzAt METHOD_HYMME_ISHIKAWA_JANNE/.!
ishikawa! ishikawa! ishikawa! ishikawa!
```

### Hypothetical

`Xc=` (pronounced "zek") before a condition, followed by `->` and the result:
```
Xc=hLYEmYEmArA -> cEzLYE hymmnos/.
= If I sing, then I will become a song
```

### Back-Reference

`<-x` (pronounced "pagu") replaces a subject/object with a previously-used noun:
```
zz arhou, balduo, ujes, Oqejyu, xA rre <-x aYAuAkN kajya LYAglansee qejyu/.
= Despair, darkness, ill will, hated people — they are necessary as well
```

## Pastalie Numerals

Same base numbers as Standard, plus positional suffix `-ra`:
- 1001 Standard: `kiku noi` vs Pastalie: `noifefura noi`
- Position: `-ra` = nth digit from right

## Pronunciation

Vowels follow Japanese: A=father, I=feel/ribbon, U=boot, E=cane/lend, O=open, N=syllabic n. `c` is soft (s) in `c.z.` but hard (k) elsewhere. `g` always hard. `x` pronounced like `z`. Singers have some flexibility.
