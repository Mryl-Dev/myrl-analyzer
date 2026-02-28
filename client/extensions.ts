import * as path from "path";
import * as vscode from "vscode";
import {
	LanguageClient,
	LanguageClientOptions,
	ServerOptions,
	TransportKind
} from "vscode-languageclient/node";

let client: LanguageClient;

export function activate(context: vscode.ExtensionContext) {
	const serverModule = context.asAbsolutePath(
		path.join("server", "server.py")
);

	const serverOptions: ServerOptions = {
		command: process.platform === 'win32' ? 'python' : 'python3', 
		args: [serverModule],
		transport: TransportKind.stdio
	};

	const clientOptions: LanguageClientOptions = {
		documentSelector: [{ scheme: "file", language: "mryl" }],
		synchronize: {
			fileEvents: vscode.workspace.createFileSystemWatcher("**/*.ml")
		}
	};

	client = new LanguageClient(
		"mrylLanguageServer",
		"Mryl Language Server",
		serverOptions,
		clientOptions
	);

	client.start();
}

export function deactivate(): Thenable<void> | undefined {
	if (!client) return undefined;
	return client.stop();
}