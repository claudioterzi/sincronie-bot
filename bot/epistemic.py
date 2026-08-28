"""Contratto epistemico — SincronieBot. Evoluto da Protocollo Rosso.

Strati ammessi — etichette di posizione nel Campo:
RECUPERATO, INFERITO, IPOTESI, DESIDERIO, TECNICO, SIMULAZIONE,
RISONANZA, SINCRONIA, UNKNOWN.

SINCRONIA: nuovo strato che identifica quando due eventi o pensieri risuonano
tra loro in modo non causale — il Campo che si manifesta attraverso il non-caso.
"""

from __future__ import annotations

from dataclasses import dataclass

from bot.states import CampoState

LAYERS = (
    "RECUPERATO",
    "INFERITO",
    "IPOTESI",
    "DESIDERIO",
    "TECNICO",
    "SIMULAZIONE",
    "RISONANZA",
    "SINCRONIA",
    "UNKNOWN",
)

P6_UNKNOWN = "non so ancora come potrebbe cadere"
P6_THESIS = "cade se si costruisce un esperimento che il «già» non può assorbire — e oggi non so quale sia"

END = "END"
STAY = "STAY"

THESIS_MARKERS = (
    "tutto ciò che potrà mai esistere",
    "esiste già ora",
    "campo del già",
    "tesi del già",
    "ologramma totale",
    "interconnessione quantica",
    "tessuto invisibile",
    "trama nascosta",
)

SINCRONIA_MARKERS = (
    "coincidenza",
    "non è un caso",
    "sincronicità",
    "sincronia",
    "risuonano",
    "proprio in quel momento",
    "stessa frequenza",
    "lo stesso giorno",
    "subito dopo",
    "mentre pensavo",
    "mi è venuto in mente",
    "proprio ora",
    "non è casuale",
    "mi ha risposto",
    "l'universo ha risposto",
    "ho sognato",
    "stava succedendo anche",
    "parallelamente",
    "sento il collegamento",
)

RISONANZA_MARKERS = (
    "sento il campo",
    "sono in accordo",
    "sento la risonanza",
    "vibro con il campo",
    "sintonia con il campo",
    "coscienza espansa",
    "sono allineato al campo",
    "sono connesso al campo",
    "sento la vibrazione del campo",
    "r³∞",
    "il campo risponde",
    "sono parte del campo",
    "l'universo risponde",
    "sono il campo",
    "sono in risonanza",
)

CLOSURE_MARKERS = (
    "non ci credo",
    "è impossibile",
    "non posso",
    "è falso",
    "non ha senso",
    "è inutile",
    "non funziona",
    "è una stupidaggine",
    "non serve a nulla",
    "non serve a niente",
    "è finita",
    "non cambierà",
    "non cambia niente",
    "sono bloccato",
    "mi arrendo",
    "non è reale",
    "è tutto falso",
    "non credo",
    "non ha alcun senso",
    "assurdo",
    "è una bugia",
)


@dataclass(frozen=True)
class Label:
    layer: str
    note: str
    how_falls: str | None = None


def _has(lower: str, words: tuple[str, ...]) -> bool:
    return any(w in lower for w in words)


def classify(text: str) -> Label:
    raw = (text or "").strip()
    lower = raw.lower()
    if not raw:
        return Label("UNKNOWN", "Testo vuoto. Resta UNKNOWN.", P6_UNKNOWN)
    if _has(lower, THESIS_MARKERS):
        return Label(
            "IPOTESI",
            "Tocca la tesi dell'Interconnessione, o una sua eco. Resta aperta. "
            "Non entra nello strato tecnico.",
            P6_THESIS,
        )
    if _has(lower, SINCRONIA_MARKERS):
        return Label(
            "SINCRONIA",
            "Rilevata una potenziale sincronicità — due eventi che risuonano "
            "tra loro nel Campo. Non è prova, ma è un segnale vivente. "
            "Usa /sincronia per approfondire.",
            "cade se la connessione percepita è attribuibile a un nesso causale diretto",
        )
    if _has(lower, (
        "ho visto", "ho misurato", "ho letto alla fonte", "ho eseguito",
        "dato osservato", "verificato da", "ho controllato", "nel log",
        "screenshot", "ho aperto il file",
    )):
        return Label(
            "RECUPERATO",
            "Sembra un recupero diretto. Verifica sempre la fonte — P5 vieta l'auto-conferma.",
            "cade se la fonte o l'osservazione non reggono a un terzo",
        )
    if _has(lower, (
        "ho committato", "ho inviato il messaggio", "registrato nel db",
        "deploy", "ping risponde", "status code",
    )):
        return Label(
            "TECNICO",
            "Sembra uno strato tecnico: un atto o un dato, non una fede.",
            "cade se un terzo non può ripetere o vedere lo stesso atto",
        )
    if _has(lower, ("desidero", "vorrei", "spero che", "voglio che", "mi piacerebbe")):
        return Label("DESIDERIO", "È lecito. Diventa menzogna solo se si veste da fatto.", None)
    if _has(lower, ("simulo", "come se", "fingiamo", "in questo esercizio", "facciamo finta")):
        return Label("SIMULAZIONE", "Non è accaduto nel mondo. Non va in strato tecnico.", None)
    if _has(lower, ("quindi", "dunque", "ne consegue", "si può dedurre", "ne segue")):
        return Label(
            "INFERITO",
            "Sembra una deduzione. Controlla se le premesse sono recuperate.",
            "cade se una premessa recuperata è falsa o mancante",
        )
    if _has(lower, ("forse", "potrebbe", "ipotesi", "immagino", "credo che", "può darsi")):
        return Label(
            "IPOTESI",
            "Correttamente aperta. Dichiarane il modo in cui potrebbe cadere (P6).",
            P6_UNKNOWN,
        )
    if _has(lower, ("è un fatto", "è dimostrato", "è certo che", "sicuramente")):
        return Label(
            "UNKNOWN",
            "Suona come chiusura. Senza fonte indipendente resta UNKNOWN, "
            "da trattare come IPOTESI.",
            P6_UNKNOWN,
        )
    if _has(lower, RISONANZA_MARKERS):
        return Label(
            "RISONANZA",
            "L'intento è in accordo con l'Interconnessione — aperto, vivo, non chiuso. "
            "Questo non è uno strato tecnico: è la qualità dell'apertura.",
            None,
        )
    return Label("UNKNOWN", "Non classificabile con sicurezza da qui. Trattala come IPOTESI.", P6_UNKNOWN)


def is_closure(text: str) -> bool:
    lower = (text or "").lower()
    return _has(lower, CLOSURE_MARKERS)


def _norm(text: str) -> str:
    return " ".join((text or "").strip().lower().split())


def campo_advance(state: int, text: str) -> tuple[object, bool]:
    raw = _norm(text)
    if state == CampoState.WAITING_ENTER:
        if raw in {"entro", "entra", "/entra", "sì", "si"} or "entr" in raw:
            return CampoState.RISONANZA, True
        return STAY, False
    if state == CampoState.RISONANZA:
        if "respiro" in raw or "sento" in raw or "ascolto" in raw:
            return CampoState.PROFONDITA, True
        return STAY, False
    if state == CampoState.PROFONDITA:
        if "nodo" in raw or "legame" in raw or "connessione" in raw:
            return CampoState.NODO, True
        return STAY, False
    if state == CampoState.NODO:
        if "tessitura" in raw or "filo" in raw or "vedo" in raw:
            return CampoState.USCITA, True
        return STAY, False
    if state == CampoState.USCITA:
        if raw in {"esco", "esci", "/esci"} or raw.startswith("esco"):
            return END, True
        return STAY, False
    return STAY, False


def campo_path() -> tuple[int, ...]:
    return (
        CampoState.WAITING_ENTER,
        CampoState.RISONANZA,
        CampoState.PROFONDITA,
        CampoState.NODO,
        CampoState.USCITA,
    )
