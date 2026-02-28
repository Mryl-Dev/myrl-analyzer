#!/usr/bin/env python3
from pygls.server import LanguageServer
from pygls.lsp.types import (
    Hover, HoverParams,
    Position, Range,
    Diagnostic, DiagnosticSeverity
)

# -----------------------------
# Mryl Language Server
# -----------------------------
class MrylServer(LanguageServer):
    def __init__(self):
        super().__init__("mryl-server", "0.1.0")

server = MrylServer()

# -----------------------------
# Hover (型情報など)
# -----------------------------
@server.feature("textDocument/hover")
def hover(ls: MrylServer, params: HoverParams):
    word = "Mryl language element"
    return Hover(contents=f"**{word}**")

# -----------------------------
# Diagnostics (型エラー表示)
# -----------------------------
@server.feature("textDocument/didOpen")
def did_open(ls: MrylServer, params):
    text = params.textDocument.text

    diagnostics = []

    # TODO: integrate real Mryl TypeChecker here
    # For now, just an example:
    if "TODO_ERROR" in text:
        diagnostics.append(
            Diagnostic(
                range=Range(
                    start=Position(line=0, character=0),
                    end=Position(line=0, character=10)
                ),
                message="Example error from Mryl LSP",
                severity=DiagnosticSeverity.Error
            )
        )

    ls.publish_diagnostics(params.textDocument.uri, diagnostics)

# -----------------------------
# Start server
# -----------------------------
if __name__ == "__main__":
    server.start_io()