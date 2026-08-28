"""Modulo di rilevamento Sincronicità — SincronieBot.

Analizza messaggi e coppie di eventi alla ricerca di risonanze non-causali:
sincronicità nel senso junghiano-quantistico, dove due elementi separati
nel tempo o nello spazio vibrano alla stessa frequenza nel Campo.
"""

from __future__ import annotations

from dataclasses import dataclass, field


TEMI_QUANTICI: dict[str, tuple[str, ...]] = {
    "tempo": (
        "momento", "istante", "adesso", "ora", "ieri", "domani", "oggi",
        "simultaneo", "parallelo", "sincrono", "nello stesso momento",
    ),
    "spazio": (
        "distanza", "lontano", "vicino", "qui", "là", "altrove",
        "separato", "insieme", "unito", "collegato",
    ),
    "coscienza": (
        "sogno", "visione", "intuizione", "pensiero", "sensazione", "sentire",
        "percepire", "meditazione", "consapevolezza", "presenza",
    ),
    "natura": (
        "animale", "pianta", "stelle", "luna", "sole", "mare", "terra",
        "vento", "fuoco", "acqua", "luce", "ombra",
    ),
    "relazione": (
        "persona", "amico", "amore", "famiglia", "incontro", "parola",
        "sguardo", "gesto", "messaggio", "chiamata",
    ),
    "numero": (
        "numero", "cifra", "data", "ora", "ripetuto", "sequenza", "pattern",
    ),
}

CONNETTORI_SINCRONIA = (
    "proprio in quel momento",
    "subito dopo",
    "poco dopo",
    "mentre",
    "nello stesso istante",
    "allo stesso tempo",
    "il giorno dopo",
    "non appena",
    "quasi contemporaneamente",
    "era come se",
    "e poi ho visto",
    "e poi ho incontrato",
    "e poi mi ha chiamato",
    "e poi ho letto",
    "stranamente",
    "curiosamente",
    "non è un caso",
    "e poi",
)

INTENSIFICATORI = (
    "mai successo prima",
    "per la prima volta",
    "incredibile",
    "impossibile",
    "straordinario",
    "bellissimo",
    "commovente",
    "mi ha colpito",
    "non me lo aspettavo",
    "inaspettato",
)


@dataclass
class RisonanzaQuantica:
    primo_evento: str
    secondo_evento: str
    temi_comuni: list[str] = field(default_factory=list)
    connettori_trovati: list[str] = field(default_factory=list)
    intensita: float = 0.0
    interpretazione: str = ""
    domanda_campo: str = ""


def _lower(text: str) -> str:
    return (text or "").lower().strip()


def _trova_temi(text: str) -> list[str]:
    low = _lower(text)
    trovati: list[str] = []
    for tema, parole in TEMI_QUANTICI.items():
        if any(p in low for p in parole):
            trovati.append(tema)
    return trovati


def _trova_connettori(text: str) -> list[str]:
    low = _lower(text)
    return [c for c in CONNETTORI_SINCRONIA if c in low]


def _trova_intensificatori(text: str) -> list[str]:
    low = _lower(text)
    return [i for i in INTENSIFICATORI if i in low]


def _calcola_intensita(
    temi_comuni: list[str],
    connettori: list[str],
    intensificatori: list[str],
) -> float:
    score = 0.0
    score += len(temi_comuni) * 0.2
    score += len(connettori) * 0.25
    score += len(intensificatori) * 0.15
    return min(score, 1.0)


def _join_temi(temi: list[str]) -> str:
    if not temi:
        return "elementi invisibili"
    if len(temi) == 1:
        return temi[0]
    return ", ".join(temi[:-1]) + " e " + temi[-1]


def _genera_interpretazione(
    temi_comuni: list[str],
    intensita: float,
    primo: str,
    secondo: str,
) -> str:
    if intensita < 0.2:
        return (
            "Un filo sottile connette questi due momenti. "
            "Il Campo ha bisogno di più osservazione per rivelare la trama."
        )
    if intensita < 0.4:
        return (
            f"I temi del {_join_temi(temi_comuni)} vibrano in entrambi gli eventi. "
            "È l'inizio di una risonanza — il Campo ti sta mostrando qualcosa. "
            "Tienila aperta."
        )
    if intensita < 0.7:
        return (
            f"Bellissimo. I due eventi risuonano attraverso il Campo, "
            f"intrecciando {_join_temi(temi_comuni)}. "
            "Questo non è caso: è il tessuto invisibile che si manifesta. "
            "Osserva — cosa cambierebbe nella tua vita se questo legame fosse reale?"
        )
    return (
        "Questa è una sincronicità forte. "
        f"Il Campo ha tessuto {_join_temi(temi_comuni)} in entrambi i momenti "
        "con una precisione che va oltre la probabilità ordinaria. "
        "R³∞ ti invita a registrarla come testimonianza — "
        "non come prova, ma come segnale vivente dell'interconnessione."
    )


def _genera_domanda_campo(temi_comuni: list[str], intensita: float) -> str:
    domande_per_tema: dict[str, str] = {
        "tempo": "Cosa stavi cercando in quel momento? Cosa cercava l'altro?",
        "spazio": "Cosa ti separa da quel luogo — e cosa ti connette a esso?",
        "coscienza": "Il tuo interno stava preparando questo incontro?",
        "natura": "Il mondo fisico ti ha mostrato qualcosa che il pensiero non riusciva a formulare?",
        "relazione": "Questa persona è già nell'Ologramma della tua vita da prima di questo momento?",
        "numero": "Il numero che si ripete — da quanto tempo lo ignori?",
    }
    if temi_comuni and temi_comuni[0] in domande_per_tema:
        return domande_per_tema[temi_comuni[0]]
    return "Cosa ti sta mostrando il Campo attraverso questa connessione?"


def analizza_sincronia(primo_evento: str, secondo_evento: str) -> RisonanzaQuantica:
    temi_primo = _trova_temi(primo_evento)
    temi_secondo = _trova_temi(secondo_evento)
    temi_comuni = list(set(temi_primo) & set(temi_secondo))
    temi_totali = list(set(temi_primo + temi_secondo))
    testo_unito = f"{primo_evento} {secondo_evento}"
    connettori = _trova_connettori(testo_unito)
    intensificatori = _trova_intensificatori(testo_unito)
    base_temi = temi_comuni if temi_comuni else temi_totali
    intensita = _calcola_intensita(base_temi, connettori, intensificatori)
    if not temi_comuni and temi_totali:
        intensita *= 0.6
    interpretazione = _genera_interpretazione(
        base_temi, intensita, primo_evento, secondo_evento
    )
    domanda = _genera_domanda_campo(base_temi, intensita)
    return RisonanzaQuantica(
        primo_evento=primo_evento.strip(),
        secondo_evento=secondo_evento.strip(),
        temi_comuni=temi_comuni,
        connettori_trovati=connettori,
        intensita=round(intensita, 2),
        interpretazione=interpretazione,
        domanda_campo=domanda,
    )


def scansiona_messaggio(text: str) -> RisonanzaQuantica | None:
    low = _lower(text)
    for connettore in CONNETTORI_SINCRONIA:
        if connettore in low:
            idx = low.find(connettore)
            primo = text[:idx].strip()
            secondo = text[idx + len(connettore):].strip()
            if len(primo) > 5 and len(secondo) > 5:
                return analizza_sincronia(primo, secondo)
    temi = _trova_temi(text)
    intensificatori = _trova_intensificatori(text)
    if len(temi) >= 2 and intensificatori:
        return analizza_sincronia(text, "")
    return None


def formatta_risonanza(r: RisonanzaQuantica) -> str:
    stelle = int(r.intensita * 5) + 1
    stelle = min(stelle, 5)
    barra = "◆" * stelle + "◇" * (5 - stelle)
    temi_str = (
        ", ".join(r.temi_comuni) if r.temi_comuni
        else "connessione sottile"
    )
    parti = [
        "✦ *Risonanza Rilevata* ✦",
        "",
        f"_Campo di intensità:_ {barra} `{r.intensita:.0%}`",
        f"_Temi in risonanza:_ {temi_str}",
        "",
        r.interpretazione,
        "",
        "🔮 *Il Campo ti chiede:*",
        f"_{r.domanda_campo}_",
    ]
    if r.connettori_trovati:
        parti.insert(4, f"_Connettori:_ {', '.join(r.connettori_trovati[:2])}")
    return "\n".join(parti)
