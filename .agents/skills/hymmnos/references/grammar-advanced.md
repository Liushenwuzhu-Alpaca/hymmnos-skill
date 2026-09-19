# Advanced Hymmnos Grammar

## Binasphere Chorus (班氏吟唱句)

Binasphere ("two worlds") Chorus interleaves two lyric lines into a single text block, decoded via a binary formula. This allows two simultaneous effects/sentiments in one song.

### Encoding Process

1. Take two lines of Hymmnos text
2. Break words into fragments as desired; mark every fragment except the last in each word with a silent `x` suffix
3. Write ALL fragments in UPPERCASE on a single line, prefixed by `=>`
4. Assign each fragment a number: 0 = first line, 1 = second line
5. Assemble the 0/1 sequence into the formula at the end

### Syntax

```
=> [fragmented text in UPPERCASE]
EXEC hymme 2x1/0>>[binary pattern]
```

- `=>` = start marker (pronounced "tab")
- `2x1/0` = two lines, using digits 0 and 1
- `>>` = "torasu" (funnel/separator)
- Binary pattern: `0` = first line, `1` = second line (pronounced "o" and "i")
- The pattern loops continuously until all fragments are consumed
- Only ONE formula per song

### Encoding Example

Two lines:
- Line 0: `Was yea ra chs hymmnos yor` (I will be glad to turn you into a song)
- Line 1: `en chsee fwal fwal yor` (and then, I shall spread out your wings)

Fragmented and merged:
```
=> WAS EN YEx CHx A SEE RA CHS FWx HYMMx AL NOS FWAL YOR YOR
    0  1   0   1  0  1  0   0   1    0   1   0   1    0   1
```

Formula: `EXEC hymme 2X1/0>>010101001010101`

### Decoding Process

1. Read the binary pattern, repeating it cyclically
2. Each digit tells you which line that fragment belongs to
3. Reassemble fragments (joining `x`-marked fragments with the next fragment in the same line)
4. Convert back to lowercase for the final sentences

### Worked Decode (EXEC_NULLASCENSION/.)

Encoded:
```
=> RRHA RRHA GUWO Ax GAx PEx GIS A GAx TIE INNx
GIS NA GRAN GAx PAUL NOx TYUNY INI SAASH AR YANJE
CIEL EN INI LA ZAx AR HHA CIEL RRHA RRHA Ax GUWO
GA PEx GAx A TYUNY RA HARx AR CIEL
TES EN YORA INI CHYET WAx SOR GAx LAx TYUNx SYE LA
FORx GANx ART SA DAL FAYx WASSA RA CIEL
EXEC hymme 2x1/0>>01101010
```

Pattern `01101010` loops: 0,1,1,0,1,0,1,0, 0,1,1,0,1,0,1,0, ...

Decoded Line 0: `Rrha apea gagis gran paul nosaash yanje en ini ar ciel`
= In this delightful trance, I feel the way will be opened for the goddess to purify this world forever

Decoded Line 1: `Rrha guwo gagis tie innna gatyuny ini ar ciel la zahha`
= In this trance of hatred, I shall tie this curse to the inside of my mind, then purify and advance this world

### Fan Extensions (Non-Canonical)

- Quatrasphere (4 lines): `EXEC hymme 4x11/0>>[pattern]` with 2-digit codes (00=line1, 01=line2, 10=line3, 11=line4)
- Sextasphere (6 lines), Octasphere (8 lines) — same principle, more lines

## Pact Spell Lines

Opening lines inserted in Ar tonelico 2 songs to access the Goddess Frelia's power via D-Cellophane.

### Connection Line

Executed once; grants ongoing access to Frelia's Binary Field. Appears only in EXEC_SOL=FAGE/.:

```
Rrha ki ra nha_HYMMNOS/1x01 >> pat mea en xest SOL=MARTA > A2.
```

- `_HYMMNOS` = the Hymmnos currently being sung
- `1x01` = channel direction; 01 = input (taking Frelia's power in)
- `SOL=MARTA > A2` = Alpha #2 (Frelia) via Sol Marta

### Activation Line (Redirection Line)

Inserted at the beginning of a song; redirects all power from Frelia:

```
Wee yea ra exec hymme VIENA >> SOL=FAGE/1x10 enter FRELIA
```

- `1x10` = channel direction; 10 = output (sending signals to Frelia)
- Creates the same environment as if Frelia herself were singing

## Special Characters

| Symbol | Pronunciation | Meaning |
|--------|---------------|---------|
| => | tab | Binasphere start marker |
| <= | tabura | Reverse marker |
| >> | torasu | Channel/funnel operator |
| -> | pasu | Function definition arrow |
| <-x | pagu | Back-reference marker |
| x. | zu | Subject marker (Pastalie) |
| Xc= | zeku | Conditional/hypothetical |
| :/ ... /: | - | Quotation marks (Pastalie) |
| /. | (invoke) | Sentence end + execute |
| ! | - | Sentence end (no execute) |
| ? | - | Question end (no execute) |
| 0 | o | Binary 0 |
| 1 | i | Binary 1 |
| x | gu | Fragment marker (Binasphere) |

## Hymmnos Binary

Format: `#x#>>####`

Used in Tower programs and hymns. Binary digits 0 (pronounced "o") and 1 (pronounced "i").

Example: `chmod b111000000/n` uses binary instead of octal.

## Carmena Foreluna (律史前月読 / Preformalized Lunar Chant)

The precursor to Hymmnos; each letter has its own meaning. Words are formed by combining letter meanings. Not truly Hymmnos, but useful for understanding word origins.

| Letter | Meaning | | Letter | Meaning |
|--------|---------|-|--------|---------|
| A | Power | | N | Nothing |
| B | World | | O | Evil |
| C | Change, Growth | | P | Life and Death |
| D | Supernatural, Dark | | Q | Ignorance |
| E | Love | | R | Life |
| F | Convey, Transmit | | S | Wish |
| G | Destruction, Punishment | | T | Me, Oneself |
| H | Flame, Fire | | U | Hatred |
| I | Holy | | V | Joy |
| J | Unfamiliar | | W | Spirit, Soul |
| K | Creation and Destruction | | X | Protection |
| L | You, Other Person | | Y | Light |
| M | Compassion | | Z | God(dess) |

Example: "chs" (become) starts with C = change; "c.z." (Pastalie become) also starts with C.

## Ar Ciela (アル・シエラ)

The planet's own language, predating all Hymmnos. Each sound carries a feeling; words are sums of letter feelings. The full frequency range (20-600,000 Hz) far exceeds human hearing (20-20,000 Hz).

### Two Notation Layers

1. **Public Ar Ciela**: 26 symbols for human-audible sounds (lossy)
2. **Compartment Ar Ciela**: adds diacritics for inaudible properties
   - FMCL (frequency): `!` `#` `$` `%` for sounds OVER 20,000 Hz (sub-dividing the 20k-600k Hz inaudible range into sessions 0-4)
   - AMCL (amplitude): `&` `(` `)` for waveform shapes above 20,000 Hz

### Letter Meanings (by frequency range)

Vowels have umbrella categories: A=[Scale], I=[Pray], U=[Experience], E=[Neighbour], O=[Karma], N=[Mandala]

Consonants shift meaning across frequency ranges I-IX. Every letter converges on "love" at the spectrum's far end. See the full table in the culture reference file.

### Structure

- Basis of Carmena Foreluna (Preformalized Lunar Chant)
- No arbitrary word-crafting; words are emotion syntheses
- Cannot express concrete nouns (a word for "A" must contain U or N)
- Like Hymmnos Emotion Sounds, but at the planetary scale
