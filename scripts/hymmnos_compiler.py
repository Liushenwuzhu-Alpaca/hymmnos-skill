#!/usr/bin/env python3
"""
Hymmnos Vibe Coding Compiler
=============================
Parses Hymmnos sentences into structured Intent Representations (IR),
then generates Python code from the IR.

Architecture:
  Hymmnos sentence → LLM-free parser → IR (JSON) → Code generator → Python

This is a concept prototype. It handles Standard Hymmnos (emotion sound sentences)
and basic Pastalie (emotion verb sentences).

Usage:
  python hymmnos_compiler.py "Was yea ra chs hymmnos mea"
  python hymmnos_compiler.py "Wee jyel ra hymme tes ar ciel" --generate
  python hymmnos_compiler.py "Was yea ra chs bautifal sasye en sonwe anw sol ciel" --generate
"""

import json
import re
import sys
from dataclasses import dataclass, field, asdict
from typing import Optional

# ============================================================
# Layer 1: Hymmnos → IR (Parser)
# ============================================================

# Emotion Sound lexicon
EMOTION_SOUNDS = {
    # Intensity (1st word)
    "Rrha": {"pos": "intensity", "value": "trance", "weight": 5},
    "Was":  {"pos": "intensity", "value": "very", "weight": 4},
    "Wee":  {"pos": "intensity", "value": "fairly", "weight": 3},
    "Fou":  {"pos": "intensity", "value": "slightly", "weight": 2},
    "Ma":   {"pos": "intensity", "value": "calm", "weight": 1},
    "Nn":   {"pos": "intensity", "value": "apathetic", "weight": 0},
    # Emotion type (2nd word)
    "i":       {"pos": "emotion", "value": "impatient"},
    "yea":     {"pos": "emotion", "value": "happy"},
    "waa":     {"pos": "emotion", "value": "happy"},
    "paks":    {"pos": "emotion", "value": "excited"},
    "num":     {"pos": "emotion", "value": "neutral"},
    "ki":      {"pos": "emotion", "value": "focused"},
    "wol":     {"pos": "emotion", "value": "fervent"},
    "apea":    {"pos": "emotion", "value": "blissful"},
    "au":      {"pos": "emotion", "value": "sad"},
    "granme":  {"pos": "emotion", "value": "protective"},
    "touwaka": {"pos": "emotion", "value": "hopeful"},
    "quel":    {"pos": "emotion", "value": "desperate"},
    "yant":    {"pos": "emotion", "value": "fearful"},
    "guwo":    {"pos": "emotion", "value": "angry"},
    "jyel":    {"pos": "emotion", "value": "lonely"},
    "zweie":   {"pos": "emotion", "value": "determined"},
    # Desirability (3rd word)
    "ga":    {"pos": "desire", "value": "stop"},
    "ra":    {"pos": "desire", "value": "continue"},
    "erra":  {"pos": "desire", "value": "forever"},
    "wa":    {"pos": "desire", "value": "accept"},
    "gaya":  {"pos": "desire", "value": "never_again"},
    "gagis": {"pos": "desire", "value": "indifferent"},
}

# Core vocabulary → programming semantics
VERB_MAP = {
    "chs":      {"action": "transform", "desc": "become/turn into"},
    "chsee":    {"action": "modify", "desc": "partially transform"},
    "sonwe":    {"action": "generate", "desc": "sing/produce output"},
    "hymme":    {"action": "generate", "desc": "resonate/emit"},
    "hyma":     {"action": "receive", "desc": "listen/accept input"},
    "pagle":    {"action": "output", "desc": "speak/print"},
    "irs":      {"action": "exists", "desc": "check existence"},
    "vit":      {"action": "inspect", "desc": "see/observe"},
    "knawa":    {"action": "query", "desc": "know/lookup"},
    "rete":     {"action": "delete", "desc": "forget/remove"},
    "haf":      {"action": "assign", "desc": "have/hold/own"},
    "echrra":   {"action": "sync", "desc": "resonate/synchronize"},
    "parge":    {"action": "detach", "desc": "cut loose/release"},
    "cexm":     {"action": "import", "desc": "come/arrive"},
    "bexm":     {"action": "trigger", "desc": "time comes/event fires"},
    "fogabe":   {"action": "resolve", "desc": "forgive/handle error"},
    "melenas":  {"action": "connect", "desc": "love/bind deeply"},
    "crushue":  {"action": "compose", "desc": "weave/craft/build"},
    "grandus":  {"action": "protect", "desc": "defend/guard"},
    "khal":     {"action": "protect", "desc": "protect/shield"},
    "exec":     {"action": "execute", "desc": "execute/run"},
    "aulla":    {"action": "open", "desc": "open/reveal"},
    "rana":     {"action": "run", "desc": "run/dash"},
    "walaka":   {"action": "traverse", "desc": "walk/iterate"},
    "tek":      {"action": "goto", "desc": "go/navigate"},
    "famfa":    {"action": "launch", "desc": "flap wings/deploy"},
    "flip":     {"action": "toggle", "desc": "reverse/flip-flop"},
    "ftt":      {"action": "clear", "desc": "vanish/erase"},
    "siss":     {"action": "remove", "desc": "erase/eliminate"},
    "raklya":   {"action": "raise_error", "desc": "cry/throw exception"},
    "lehaw":    {"action": "rescue", "desc": "save/recover"},
    "drone":    {"action": "download", "desc": "download/fetch"},
    "quen":     {"action": "create", "desc": "give birth/instantiate"},
    "pomb":     {"action": "create", "desc": "produce/create"},
    "kil":      {"action": "terminate", "desc": "kill/terminate process"},
    "ruinie":   {"action": "destroy", "desc": "destroy/teardown"},
}

NOUN_MAP = {
    "hymmnos":  {"type": "output", "desc": "song/result/product"},
    "sarla":    {"type": "output", "desc": "song/result"},
    "hynne":    {"type": "signal", "desc": "voice/message"},
    "eje":      {"type": "state", "desc": "heart/core state"},
    "ciel":     {"type": "environment", "desc": "world/environment/context"},
    "sphaela":  {"type": "environment", "desc": "world/scope"},
    "dor":      {"type": "platform", "desc": "ground/runtime"},
    "mea":      {"type": "self", "desc": "self/this"},
    "mean":     {"type": "group", "desc": "us/team"},
    "yor":      {"type": "user", "desc": "you/client/target"},
    "yorr":     {"type": "user", "desc": "you (subject)"},
    "yora":     {"type": "users", "desc": "you all/clients"},
    "fautre":   {"type": "future", "desc": "future/async result"},
    "ides":     {"type": "history", "desc": "past/log"},
    "im":       {"type": "present", "desc": "now/current"},
    "kira":     {"type": "node", "desc": "star/endpoint"},
    "lyuma":    {"type": "node", "desc": "star/service"},
    "fayra":    {"type": "resource", "desc": "fire/energy/CPU"},
    "kapa":     {"type": "resource", "desc": "water/data flow"},
    "fhyu":     {"type": "medium", "desc": "wind/network"},
    "papana":   {"type": "event", "desc": "rain/incoming stream"},
    "dorn":     {"type": "structure", "desc": "tree/hierarchy"},
    "dornpica": {"type": "item", "desc": "fruit/leaf node"},
    "faura":    {"type": "agent", "desc": "bird/worker process"},
    "sasye":    {"type": "agent", "desc": "girl/subprocess"},
    "lasye":    {"type": "agent", "desc": "boy/subprocess"},
    "walasye":  {"type": "agent", "desc": "human/user process"},
    "qejyu":    {"type": "agents", "desc": "people/all processes"},
    "saash":    {"type": "authority", "desc": "God/root/admin"},
    "cupla":    {"type": "error", "desc": "sin/error/fault"},
    "wart":     {"type": "token", "desc": "word/string/token"},
    "memora":   {"type": "cache", "desc": "memory/cache"},
    "revm":     {"type": "mock", "desc": "dream/virtual"},
    "futare":   {"type": "future_ref", "desc": "future/promise"},
    "fwal":     {"type": "wrapper", "desc": "wing/wrapper/envelope"},
    "guard":    {"type": "guard", "desc": "protection/guard clause"},
    "cecet":    {"type": "buffer", "desc": "shield/buffer"},
    "cecet":    {"type": "buffer", "desc": "shield/buffer"},
    "ceset":    {"type": "lock", "desc": "truth/mutex"},
    "skit":     {"type": "contract", "desc": "promise/contract"},
    "spitze":   {"type": "flag", "desc": "freedom/flag"},
    "caan":     {"type": "signal", "desc": "bell/alert"},
    "quesa":    {"type": "interrupt", "desc": "thunder/interrupt"},
}

ADJ_MAP = {
    "bautifal": "beautiful",
    "clare": "transparent",
    "cest": "true",
    "ar": "unique",
    "omni": "all",
    "omnis": "all",
    "gral": "entire",
    "maxim": "maximal",
    "add": "additional",
    "byui": "large",
    "et": "large",
    "tyui": "small",
    "titilia": "tiny",
    "ewle": "long",
    "dep": "deep",
    "balduo": "dark",
    "vonn": "dark",
    "noglle": "black",
    "vinan": "white",
    "burle": "blue",
    "grrena": "green",
    "rudje": "red",
    "kiala": "golden",
    "irea": "silver",
    "heath": "hot",
    "vigiga": "cold",
    "warma": "warm",
    "wefa": "mild",
    "hieg": "sad",
    "yeharr": "happy",
    "clemezen": "insane",
    "willie": "fragile",
    "clalliss": "colorful",
}

PARTICLE_MAP = {
    "tes": "to",
    "anw": "to",
    "en": "and",
    "art": "by",
    "ween": "inside",
    "won": "over",
    "folten": "before",
    "oz": "of",
    "sos": "for",
    "den": "but",
    "rol": "like",
    "ess": "in",
    "ede": "at",
    "elle": "from",
    "tou": "at",
    "ut": "to",
    "nor": "or",
    "na": "not",
    "re": "passive",
    "rre": "subject_marker",
    "ag": "and",
    "du": "obj_marker",
    "dn": "by_means",
}

PRONOUN_SUBJECT = {"yorr", "yorra", "herr", "herra", "harr", "harra", "merra", "sorr", "sorra"}

# Pastalie emotion vowel decoding
PASTALIE_VOWELS = {
    "A": "power", "I": "pain", "U": "sadness", "E": "joy", "O": "rage", "N": "calm",
    "YA": "serve", "YI": "suffer", "YU": "anxiety", "YE": "fortune", "YO": "fury", "YN": "comfort",
    "LYA": "devote", "LYI": "ruin", "LYU": "instability", "LYE": "prosper", "LYO": "war", "LYN": "stillness",
}

PASTALIE_TEMPLATES = {
    "h.m.m.r.": "sing",
    "c.z.": "transform",
    "a.u.k.": "is",
    "d.n.": "dance",
    "d.z.": "die",
    "f.w.r.n.": "embrace",
    "g.w.n.": "guide",
    "g.v.w.": "fight",
    "m.r.": "burn",
    "n.e.g.": "pray",
    "n.t.n.": "continue",
    "r.f.m": "see",
    "s.s.w.": "say",
    "v.a": "produce",
    "v.t": "live",
    "w.s.r.": "forget",
    "x.v.": "destroy",
    "y.y.": "heal",
    "y.z.t.": "wish",
}


@dataclass
class EmotionContext:
    intensity: str = ""
    intensity_weight: int = 0
    emotion: str = ""
    desire: str = ""


@dataclass
class HymmnosIR:
    """Intermediate Representation of a Hymmnos sentence."""
    raw: str = ""
    sentence_type: str = ""  # "standard" | "pastalie" | "emotionless" | "binasphere"
    emotion: EmotionContext = field(default_factory=EmotionContext)
    action: str = ""
    action_desc: str = ""
    subject: str = "self"  # default first person
    objects: list = field(default_factory=list)
    modifiers: list = field(default_factory=list)
    particles: list = field(default_factory=list)
    negated: bool = False
    passive: bool = False
    invoke: bool = True  # /. = True, ! = False
    parallel: Optional[dict] = None  # for Binasphere
    metadata: dict = field(default_factory=dict)


def parse_emotion_sounds(words):
    """Parse the first 3 words as emotion sounds."""
    es = EmotionContext()
    if len(words) >= 1 and words[0] in EMOTION_SOUNDS:
        info = EMOTION_SOUNDS[words[0]]
        if info["pos"] == "intensity":
            es.intensity = info["value"]
            es.intensity_weight = info["weight"]
    if len(words) >= 2 and words[1] in EMOTION_SOUNDS:
        info = EMOTION_SOUNDS[words[1]]
        if info["pos"] == "emotion":
            es.emotion = info["value"]
    if len(words) >= 3 and words[2] in EMOTION_SOUNDS:
        info = EMOTION_SOUNDS[words[2]]
        if info["pos"] == "desire":
            es.desire = info["value"]
    return es


def is_pastalie(word):
    """Check if a word is a Pastalie emotion verb (has mixed case)."""
    return bool(re.match(r'^[a-z][A-Z]', word)) or word.endswith("/.")


def parse_pastalie_verb(word):
    """Parse a Pastalie emotion verb into template + emotion vowels."""
    # Check for terminator (may be attached or separate)
    invoke = "/." in word or word.endswith(".")
    # Remove terminator characters
    clean = word
    for suffix in ["/.", ".", "!", "?"]:
        if clean.endswith(suffix):
            clean = clean[:-len(suffix)]
            break
    # Extract emotion vowels (uppercase sequences)
    vowels = re.findall(r'[A-Z]+', clean)
    # Extract consonants (lowercase letters)
    consonants = re.findall(r'[a-z]', clean)
    # Find matching template by consonant sequence
    matched = None
    for t, meaning in PASTALIE_TEMPLATES.items():
        t_consonants = [c for c in t if c.isalpha()]
        if t_consonants == consonants:
            matched = (t, meaning)
            break
    # Decode emotion vowels
    emotions = []
    for v in vowels:
        if v in PASTALIE_VOWELS:
            level = 1
            if v.startswith("LY"):
                level = 3
            elif v.startswith("Y"):
                level = 2
            emotions.append({"vowel": v, "level": level, "meaning": PASTALIE_VOWELS[v]})
    return {
        "template": matched[0] if matched else ".".join(consonants) + ".",
        "meaning": matched[1] if matched else "unknown",
        "consonants": consonants,
        "vowels": vowels,
        "emotions": emotions,
        "invoke": invoke,
    }


def parse_hymmnos(sentence):
    """Parse a Hymmnos sentence into IR."""
    sentence = sentence.strip()
    ir = HymmnosIR(raw=sentence)

    # Check for Binasphere
    if sentence.startswith("=>"):
        ir.sentence_type = "binasphere"
        ir.metadata["note"] = "Binasphere Chorus - requires binary pattern to decode"
        return ir

    # Tokenize: separate terminators
    words = sentence.replace("/.", " /. ").replace("!", " ! ").replace("?", " ? ").split()
    # Check for Pastalie (has mixed case or /. terminator)
    has_pastalie = any(is_pastalie(w) for w in words) or any(w == "/." for w in words)

    if has_pastalie:
        ir.sentence_type = "pastalie"
        for w in words:
            if w in ["/.", ".", "!", "?"]:
                ir.invoke = (w == "/." or w == ".")
                continue
            if is_pastalie(w) or re.match(r'^[a-z][A-Z]', w):
                pv = parse_pastalie_verb(w)
                ir.action = pv["meaning"]
                ir.action_desc = f"Pastalie emotion verb: {pv['template']} ({pv['meaning']})"
                if pv["emotions"]:
                    ir.emotion.emotion = pv["emotions"][0]["meaning"]
                    ir.metadata["pastalie_vowels"] = pv["emotions"]
                ir.invoke = pv["invoke"]
            elif w in NOUN_MAP:
                ir.objects.append({"word": w, **NOUN_MAP[w]})
            elif w == "rre":
                ir.particles.append({"word": w, "role": "subject_marker"})
            elif w in ["xor", "yor", "mea", "yorr", "harr", "herr"]:
                ir.objects.append({"word": w, "type": "pronoun", "desc": w})
            elif w.startswith("x.") or (len(w) == 2 and w[0] == "x" and w[1].isupper()):
                # x. subject definer with emotion vowel
                vowel = w[-1] if w[-1].isupper() else ""
                ir.subject = "other"
                if vowel in PASTALIE_VOWELS:
                    ir.metadata["singer_emotion"] = PASTALIE_VOWELS[vowel]
            elif w.startswith("A") and w[1:].islower():
                # Possessive prefix noun (A+noun, YA+noun, LYA+noun)
                prefix = ""
                if w.startswith("LYA"):
                    prefix = "LYA"
                elif w.startswith("YA"):
                    prefix = "YA"
                elif w.startswith("A"):
                    prefix = "A"
                base = w[len(prefix):]
                ir.objects.append({"word": w, "type": "possessive_noun", "desc": f"{prefix}={{'my'/'your'/'all'}} + {base}", "prefix": prefix, "base": base})
            else:
                ir.objects.append({"word": w, "type": "unknown", "desc": w})
        return ir

    # Standard Hymmnos parsing
    # Check for emotion sounds
    es = parse_emotion_sounds(words)
    if es.intensity or es.emotion or es.desire:
        ir.sentence_type = "standard"
        ir.emotion = es
        remaining = words[3:]
    else:
        ir.sentence_type = "emotionless"
        remaining = words

    # Check for negation and passive
    body = remaining
    if "na" in body:
        ir.negated = True
        body = [w for w in body if w != "na"]
    if "re" in body:
        ir.passive = True
        body = [w for w in body if w != "re"]

    # Check for terminator
    if body and body[-1] in ["/.", ".", "!", "?"]:
        ir.invoke = (body[-1] == "/." or body[-1] == ".")
        body = body[:-1]

    # Parse body: verb + objects + particles
    for i, w in enumerate(body):
        if w in VERB_MAP and not ir.action:
            ir.action = VERB_MAP[w]["action"]
            ir.action_desc = VERB_MAP[w]["desc"]
        elif w in NOUN_MAP:
            ir.objects.append({"word": w, **NOUN_MAP[w]})
        elif w in ADJ_MAP:
            ir.modifiers.append({"word": w, "desc": ADJ_MAP[w]})
        elif w in PARTICLE_MAP:
            ir.particles.append({"word": w, "role": PARTICLE_MAP[w]})
        elif w in PRONOUN_SUBJECT:
            ir.subject = w
        elif w == "rre":
            ir.particles.append({"word": w, "role": "subject_marker"})
        elif w in EMOTION_SOUNDS:
            # Could be emotion word used as adjective
            ir.modifiers.append({"word": w, "desc": EMOTION_SOUNDS[w]["value"]})
        else:
            # Unknown word - keep as raw
            ir.objects.append({"word": w, "type": "unknown", "desc": w})

    return ir


# ============================================================
# Layer 2: IR → Python Code (Generator)
# ============================================================

def generate_python(ir: HymmnosIR) -> str:
    """Generate Python code from Hymmnos IR."""
    lines = []
    emotion = ir.emotion

    # Emotion context as decorator/comment
    if emotion.intensity or emotion.emotion:
        intensity_str = f'"{emotion.intensity}"' if emotion.intensity else "None"
        emotion_str = f'"{emotion.emotion}"' if emotion.emotion else "None"
        desire_str = f'"{emotion.desire}"' if emotion.desire else "None"
        lines.append(f"# Hymmnos Vibe Coding — Auto-generated from:")
        lines.append(f"#   {ir.raw}")
        lines.append(f"# Emotion: intensity={emotion.intensity}, emotion={emotion.emotion}, desire={emotion.desire}")
        lines.append(f"# Type: {ir.sentence_type}, Action: {ir.action} ({ir.action_desc})")
        if ir.negated:
            lines.append(f"# Negated: True")
        if ir.passive:
            lines.append(f"# Passive: True")

    # Imports first
    lines.append("import json")
    lines.append("from dataclasses import dataclass")
    lines.append("@dataclass")
    lines.append("class EmotionContext:")
    lines.append(f'    intensity: str = "{emotion.intensity}"')
    lines.append(f'    emotion: str = "{emotion.emotion}"')
    lines.append(f'    desire: str = "{emotion.desire}"')
    lines.append(f'    weight: int = {emotion.intensity_weight}')
    lines.append("")

    # Generate function
    func_name = ir.action or "execute"
    lines.append(f"def {func_name}(ctx: EmotionContext):")

    if not ir.objects and not ir.modifiers:
        lines.append(f'    """{ir.action_desc}"""')
        lines.append(f"    # No objects specified — perform bare action")
        lines.append(f"    result = '{ir.action}'")
    else:
        lines.append(f'    """{ir.action_desc}"""')

        # Process objects
        for obj in ir.objects:
            desc = obj.get("desc", obj.get("word", ""))
            otype = obj.get("type", "unknown")
            word = obj.get("word", "")
            lines.append(f"    # Object: {word} ({otype}) — {desc}")
            lines.append(f"    {word} = {{'type': '{otype}', 'desc': '{desc}', 'word': '{word}'}}")

        # Process modifiers
        for mod in ir.modifiers:
            lines.append(f"    # Modifier: {mod['word']} — {mod['desc']}")

        # Process particles (prepositional phrases)
        for p in ir.particles:
            lines.append(f"    # Particle: {p['word']} — {p['role']}")

        # Action logic
        if ir.negated:
            lines.append(f"    # NEGATED — do the opposite of {ir.action}")
            lines.append(f"    result = not _do_{ir.action}(ctx)")
        elif ir.passive:
            lines.append(f"    # PASSIVE — receive {ir.action} from external source")
            lines.append(f"    result = _receive_{ir.action}(ctx)")
        else:
            lines.append(f"    result = _do_{ir.action}(ctx)")

        # Objects passed to action
        if ir.objects:
            obj_names = [o["word"] for o in ir.objects]
            lines.append(f"    # Passing objects: {', '.join(obj_names)}")

    # Invoke or declare
    if ir.invoke:
        lines.append("")
        lines.append("    # /. — INVOKE (execute immediately)")
        lines.append("    return result")
    else:
        lines.append("")
        lines.append("    # ! — DECLARE ONLY (no execution)")
        lines.append("    return lambda: result")

    # Helper functions
    lines.append("")
    lines.append("")
    lines.append(f"def _do_{ir.action}(ctx):")
    lines.append(f'    """Execute {ir.action_desc} with emotion context."""')
    lines.append(f'    print(f"[{{ctx.emotion}}/{{ctx.intensity}}] {ir.action}: {ir.action_desc}")')
    lines.append(f"    return {{'action': '{ir.action}', 'emotion': ctx.emotion, 'intensity': ctx.intensity}}")

    if ir.negated:
        lines.append("")
        lines.append(f"    # Note: negation handled in main function via 'not'")

    # Main
    lines.append("")
    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append(f"    ctx = EmotionContext()")
    lines.append(f"    output = {func_name}(ctx)")
    lines.append(f"    print(json.dumps(output, indent=2, default=str))")
    lines.append("")

    return "\n".join(lines)


# ============================================================
# Main
# ============================================================

def compile_hymmnos(sentence, generate=False):
    """Compile a Hymmnos sentence to IR, optionally to Python."""
    ir = parse_hymmnos(sentence)
    ir_dict = {
        "raw": ir.raw,
        "sentence_type": ir.sentence_type,
        "emotion": asdict(ir.emotion),
        "action": ir.action,
        "action_desc": ir.action_desc,
        "subject": ir.subject,
        "objects": ir.objects,
        "modifiers": ir.modifiers,
        "particles": ir.particles,
        "negated": ir.negated,
        "passive": ir.passive,
        "invoke": ir.invoke,
    }

    print("=" * 60)
    print("HYMMNOS COMPILER")
    print("=" * 60)
    print(f"\nInput: {sentence}")
    print(f"\n--- IR (Intermediate Representation) ---")
    print(json.dumps(ir_dict, indent=2, ensure_ascii=False))

    if generate:
        print(f"\n--- Generated Python ---")
        code = generate_python(ir)
        print(code)

    return ir


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hymmnos_compiler.py \"<Hymmnos sentence>\" [--generate]")
        print()
        print("Examples:")
        print('  python hymmnos_compiler.py "Was yea ra chs hymmnos mea" --generate')
        print('  python hymmnos_compiler.py "Wee jyel ra hymme tes ar ciel" --generate')
        print('  python hymmnos_compiler.py "Was yea ra na chs hymmnos yor" --generate')
        print('  python hymmnos_compiler.py "hEmmErYE/." --generate')
        print('  python hymmnos_compiler.py "Was guwo ga ruinie ar ciel" --generate')
        sys.exit(1)

    sentence = sys.argv[1]
    generate = "--generate" in sys.argv
    compile_hymmnos(sentence, generate)
