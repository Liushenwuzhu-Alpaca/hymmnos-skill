# Standard Hymmnos Grammar (Central Standard Note)

## Emotion Sounds (想音)

All sentences with proper grammar begin with a three-word Emotion Sound. Subject is always "I". Required for Tower processing (Song Magic).

Structure: `[intensity] [emotion type] [desirability]`

### First Word - Intensity

| Word | Pronunciation | Meaning |
|------|---------------|---------|
| Rrha | rolled 'r' | trance-like, consumed with |
| Was | rhymes "sauce" | very intensely |
| Wee | like "whee" | fairly, quite |
| Fou | like "foe" | a little, somewhat |
| Ma | as in "mama" | level-headed, calm (default) |
| Nn | grunt 'n' | apathetic, reluctant |

### Second Word - Emotion Type

| Word | Pronunciation | Meaning | Dialect |
|------|---------------|---------|---------|
| i | 'e' in "evil" | impatient, irritated | Central |
| yea | "yeah" | happy | Central |
| waa | "wa" prolonged | happy | Ancient Metafalss |
| paks | "pox" | nervous, excited | Central |
| num | "number" | nil, nothing (default) | Central |
| ki | "key" | focused, concentrating | Central |
| wol | "vole" | fervorous, impassioned | Central |
| apea | ah-pay-ah | immersed in happiness | Kurt Ciel |
| au | "ow" | sad | Alpha (Eolia) |
| granme | gran-may | wanting to protect, brave | Central |
| touwaka | toe-wah-kah | hopeful, wishing | Central |
| quel | "quell" | eager, desperate | Central |
| yant | "yawn"+t | fearful, panicked | Ancient Metafalss |
| guwo | "grow" (Fudd) | angry, resentful | Central |
| jyel | "jail" | lonely | Central |
| zweie | German "zwei" | determined, sincere | Central |
| nyasri | nya-su-ri | sad, downhearted | Ancient Metafalss |

Any Hymmnos emotion word may substitute for the second word. Level 2 Emotion Sounds can also function as adjectives.

### Third Word - Desirability

| Word | Pronunciation | Meaning |
|------|---------------|---------|
| ga | "gawk" | I want this to stop |
| ra | "raw" | I want this to continue (default) |
| erra | "era" extended | I want this to last forever |
| wa | "wad"-d | I accept things as they are |
| gaya | ga-ya | I never want to return to before |
| gagis | gya-giss | I don't mind what happens (Metafalss) |

Default for automated messages: "Ma num ra"

## Sentence Structure

### First-Person (Self-type)

Default; subject "I" is implicit and omitted:

```
[Emotion Sound] + [verb] + [object] + [compound]
```

Example: `Was yea ra chs hymmnos mea` = I am delighted to express myself through song

No tenses exist; time is context-dependent. Hymmnos nouns are number-neutral (like Japanese) — "kira" means both "star" and "stars" depending on context; there is no plural marker.

The "compound" slot in sentence templates can hold:
- Prepositional phrases: `tes ar ciel` (to the world), `anw sol ciel` (to the world, Metafalss object marker)
- Additional objects: `en 1 dyyal nuih bexm` (and the first night came)
- Subordinate clauses: `rre sol ciel hyma hynne mea` (that the world hears me)
Prepositional phrases attach after the verb and its direct object, following the pattern: verb + object + [preposition + destination].

### Non-First-Person (Non-self-type)

**Half-non-self** (speaker acts, then subject acts):
```
[ES] + [verb1] + rre + [subject] + [verb2] + [object] + [compound]
```
Example: `Wee ki ra hyma rre walasye pagle wart` = I listen to the person speaking

**Full-non-self** (subject is main actor):
```
[ES] + rre + [subject] + [verb] + [object] + [compound]
```
Example: `Was yea ra rre hyma hymme` = I happily listen to the singing/resonance

Rules:
- `rre` marks the following word as subject; appears at most ONCE per sentence
- Emotion Sound always expresses the SPEAKER's feelings
- Subject-form pronouns (yorr, herr, harr) may omit `rre`

### Emotionless Sentences

No Emotion Sound; standard SVO. Not processed by Towers:
```
Faura yerwe murfan anw sol ciel = The little bird chirps her feelings to the world
```

### Storytelling Forms (VSO/VOS)

Less common; used in narratives. Subject may follow a comma for emphasis:
```
Rrha cyuie gaya na ieeya crushue anw dornpica, rhaplanca
= Rhaplanca doesn't wish to craft the seeds anymore
```

## Pronouns

| Who | Object | Subject |
|-----|--------|---------|
| I/me | mea | mea (no true subject form) |
| we/us | mean | merra |
| you (sg) | yor | yorr |
| you (pl) | yora | yorra |
| he | hes | herr |
| they (masc) | hers | herra |
| she | has | harr |
| they (fem) | hars | harra |

Use subject form before `rre` or as subject; object form as object or after `anw`.

## Passive Voice

Place `re` before the verb. `art` (by) marks the agent:
```
deggeez anw ciel = I betray the world (active)
re deggeez art ciel = I am betrayed by the world (passive)
```
In self-type: `Was ki ra re gyuss lir` = I am embraced by the light

## Negation

`na` before the negated element. Position controls scope:
```
Was yea ra na chs hymmnos yor = I will NOT turn you into a song
Was yea ra chs na hymmnos yor = Not a song, but something else
Was yea ra chs hymmnos na yor = Not you, but someone else
```
Emotion Sounds cannot be negated.

## Possession

**Juxtaposition**: `sarla mea` = my song; `hyzik yor` = your body
**Using oz**: `hymmnos oz faura` = song of the bird
**Hyphenated**: `Aceku-sasye` = this girl's friend

## Adjectives

Precede the noun/verb: `tyui frawr` = small flower; `bautifal faura` = beautiful bird

## Particles and Prepositions

| Particle | Meaning |
|----------|---------|
| anw | direct object marker (Metafalss) |
| tes | to (destination) |
| en | and, because, for |
| art | by (passive agent) |
| ween | inside, in |
| won | over, on (surface) |
| folten | before, in front of |
| oz | of (possessive) |
| sos | for, because of |
| den | however, but |
| rol | as if, like |
| yetere | if...then |
| aiph | if |
| nor | or |
| fatere | otherwise |

## Persistent Emotion Sounds

One Emotion Sound applied to multiple sentences:
```
[ES] 0x vvi.
  [sentence 1]
  [sentence 2]
  ...
1x AAs ixi.
```
- `0x vvi.` = start (pronounced "ogu vivi")
- `1x AAs ixi.` = end (pronounced "igu aas ixi")
- Explicit ES on any inner sentence overrides the default

## Question Sentences

Question words: `whalt` (what), `whai` (why). Place after Emotion Sound, replacing the questioned element:
```
Nn num ra whait irs ar ciel = What exists in the sky?
```

## Numbers

nel=0, nnoi=1, zi=2, dri=3, fef=4, vira=5, ixa=6, hept=7, octa=8, nei=9, dec=10, hec=100, kic=1000, mic=10000

## Special Characters

| Symbol | Pronunciation | Meaning |
|--------|---------------|---------|
| => | tab | Binasphere start |
| >> | torasu | Channel operator |
| 0/1 | o/i | Binary digits |
| x | gu | Fragment marker |
| 0x | ogu | Binary flag 0 |
| 1x | igu | Binary flag 1 |
