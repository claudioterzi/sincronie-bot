"""Stati delle ConversationHandler — SincronieBot."""

from __future__ import annotations

from enum import IntEnum


class CampoState(IntEnum):
    WAITING_ENTER = 10
    RISONANZA = 11
    PROFONDITA = 12
    NODO = 13
    USCITA = 14


class SincroniaCercaState(IntEnum):
    WAITING_PRIMO = 20
    WAITING_SECONDO = 21


class PossibilityState(IntEnum):
    WAITING_TEXT = 30


class ActionState(IntEnum):
    WAITING_DESCRIPTION = 40


class EtichettaState(IntEnum):
    WAITING_TEXT = 50


CAMPO_ENTRATA = CampoState.WAITING_ENTER
SYNC_PRIMO = SincroniaCercaState.WAITING_PRIMO
SYNC_SECONDO = SincroniaCercaState.WAITING_SECONDO
