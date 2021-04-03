"""
Verb types of TRUNAJOD.

These verb types are used to modify the parse tree generated by SPACY, since
it has some lingüístics issues that does not address properly.
"""

INFINITIVE_VERBS = {
    "acabar de",
    "acabar por",
    "acostumbrar",
    "acostumbrar a",
    "cesar de",
    "comenzar a",
    "deber",
    "deber de",
    "dejar de",
    "empezar a",
    "empezar por",
    "entrar a",
    "estar a punto de",
    "estar para",
    "estar por",
    "haber",
    "haber de",
    "haber que",
    "ir a",
    "llegar a",
    "pasar a",
    "poder",
    "ponerse a",
    "soler",
    "tener que",
    "terminar de",
    "terminar por",
    "venir a",
    "volver a",
}

GERUND_VERBS = {
    "seguir",
    "continuar",
    "estar",
    "ir",
    "venir",
    "llevar",
    "pasar",
    "pasarse",
    "empezar",
    "acabar",
    "terminar",
}

PAST_TENSE_VERBS = {"llevar", "tener", "estar", "haber"}
