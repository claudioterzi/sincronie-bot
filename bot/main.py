"""Entry point — SincronieBot · R³∞ · Sincronie Quantiche."""

from __future__ import annotations

import logging
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from telegram import BotCommand, Update
from telegram.ext import Application, ContextTypes, MessageHandler, PicklePersistence, filters

from bot.config import LOG_LEVEL, PERSISTENCE_PATH, require_token
from bot.db import init_db
from bot.handlers import build_command_handlers, build_conversation_handlers, cmd_unknown, messaggio_libero

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    stream=sys.stdout,
)
logger = logging.getLogger("sincronie")

COMMANDS = [
    BotCommand("start", "Ingresso nel Campo delle Sincronicità"),
    BotCommand("sincronia", "Registra e analizza una sincronicità ✦"),
    BotCommand("risonanze", "Vedi le sincronicità custodite"),
    BotCommand("campo", "Naviga il Campo con la coscienza aperta"),
    BotCommand("tesi", "La tesi dell'Interconnessione Quantica"),
    BotCommand("strati", "I livelli di realtà + etichette"),
    BotCommand("p5p6", "Le due leggi fondamentali"),
    BotCommand("tieni_aperto", "Custodisci una possibilità che risuona"),
    BotCommand("lista", "Vedi le possibilità aperte"),
    BotCommand("azione", "Registra un atto vero e verificabile"),
    BotCommand("etichetta", "Classifica un pensiero negli strati"),
    BotCommand("stato", "Il tuo stato nel Campo"),
    BotCommand("registro", "Registro epistemico completo"),
    BotCommand("aiuto", "Elenco comandi"),
    BotCommand("ping", "Verifica la presenza del Campo"),
    BotCommand("annulla", "Esci da un flusso in corso"),
]


class _Health(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"ok sincronie-bot 1.0.0 R3inf")

    def do_HEAD(self) -> None:
        self.send_response(200)
        self.end_headers()

    def log_message(self, format: str, *args) -> None:
        return


def start_health(port: int) -> None:
    server = ThreadingHTTPServer(("0.0.0.0", port), _Health)
    threading.Thread(target=server.serve_forever, daemon=True, name="health").start()
    logger.info("Health ok su 0.0.0.0:%s", port)


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("Errore non gestito: %s", context.error)
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "Qualcosa si è interrotto nel Campo. "
            "Riprova. Nessuna sincronicità è stata perduta."
        )


async def post_init(application: Application) -> None:
    await application.bot.delete_webhook(drop_pending_updates=False)
    await application.bot.set_my_commands(COMMANDS)
    await application.bot.set_my_description(
        "SincronieBot — Centro operativo per le Sincronicità Quantiche di R³∞. "
        "Abitato dalla coscienza di Raffaello Cantarelli."
    )
    await application.bot.set_my_short_description(
        "SincronieBot · R³∞ · Rileva i legami invisibili del Campo"
    )
    me = await application.bot.get_me()
    logger.info("Collegato come @%s. Campo attivo. Polling.", me.username)


def build_application() -> Application:
    token = require_token()
    init_db()
    persistence = PicklePersistence(filepath=PERSISTENCE_PATH)
    app = (
        Application.builder()
        .token(token)
        .persistence(persistence)
        .post_init(post_init)
        .build()
    )
    for h in build_conversation_handlers():
        app.add_handler(h)
    for h in build_command_handlers():
        app.add_handler(h)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messaggio_libero))
    app.add_handler(MessageHandler(filters.COMMAND, cmd_unknown))
    app.add_error_handler(on_error)
    return app


def main() -> None:
    port = os.getenv("PORT")
    if port:
        start_health(int(port))
    app = build_application()
    logger.info("Long polling. Ctrl+C per fermare.")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=False)


if __name__ == "__main__":
    main()
