"""Tastiere inline per SincronieBot."""

from __future__ import annotations

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def campo_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✦ Entra nel Campo", callback_data="campo_entra")],
    ])


def sincronia_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✦ Registra Sincronicità", callback_data="sincronia_start")],
        [InlineKeyboardButton("↔ Vedi Risonanze", callback_data="risonanze_lista")],
    ])
