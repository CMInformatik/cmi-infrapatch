# Sprache der Artefakte

## Zweck

Alle Artefakte entstehen in einheitlichem Schweizer Hochdeutsch mit einheitlichen Begriffen.

## Geltungsbereich

1. Gilt für Markdown-Artefakte (README, Doku, Changelog, AGENTS.md, CLAUDE.md, Rules, Agents, Skills), Commit-Messages (Beschreibung und Body), PR-Texte, Code-Kommentare und Log-Messages.
2. Ausgenommen sind Identifier, Befehle, Pfade, Dateinamen, Code-Keys, Inhalt von Backticks und Codeblöcken, Produktnamen, Oberflächentexte (so zitiert, wie angezeigt, z. B. «Systemstatus»), ausgehende E-Mails und APIs, Testnamen sowie Conventional-Commit-Typ und Scope (`feat`, `fix`).

## Regeln

1. Schreibe Schweizer Hochdeutsch nach Duden mit «ss» statt Eszett, Anführungszeichen «…» und «du»-Form.
2. Verwende die Begriffe aus `glossar-cmi.md` im gleichen Ordner.
3. Verbinde EN-DE-Zusammensetzungen mit Bindestrich (Cloud-Lösung) und schreibe EN-EN-Zusammensetzungen getrennt (Web Client).
4. Schreibe «CMI» ohne bestimmten Artikel.
5. Schreibe Log-Messages auf Deutsch mit englischen Fachbegriffen gemäss Logging-Richtlinie (LOG-05).
6. Schlage beim Schreiben nicht in Wiki, Hilfe oder Confluence nach, auch nicht über MCP oder Browser.
7. Übersetze bestehende englische Artefakte beim nächsten inhaltlichen Anfassen, nicht per Massenänderung.
8. Weiche nur ab, wenn das verantwortliche Team die Abweichung mit Grund in der Repo-CLAUDE.md oder AGENTS.md vermerkt hat.

## Fachbegriffe

1. Ein Fachbegriff bleibt englisch, wenn Entwickelnde ihn auf Englisch suchen würden, z. B. Casting, Garbage Collection, Deadlock.
2. Zusammengesetzte Fachbegriffe bleiben vollständig englisch, z. B. Access Token, Connection String, Event Listener.
3. Bei substantivierten IT-Verben bleibt das Kernwort englisch, z. B. «beim Parsing der Datei», «während des Renderings».
4. Begriffe aus Infrastruktur, Code und Datentypen bleiben englisch, z. B. Repository, Pull Request, Pipeline, Gateway, Cluster, Endpoint, Request, Cache, Queue, Timeout, Array, String, Exception, Thread.
5. Verwende eingedeutschte Verben und übliche Artikel: deployt, gemergt, gepusht, geklont; das Repository, der Commit, die Pipeline.
6. Wirkt eine Übersetzung sperrig oder künstlich, bleibt der englische Begriff.
7. Bei CMI etablierte deutsche Begriffe aus dem Glossar gehen vor, z. B. Mandant, Benutzende, Seite, Schnittstelle für die Anbindung von Fremdsystemen.

## Stil

1. Nenne die Kernaussage zuerst, schreibe kurze Sätze und formuliere aktiv.
2. Verzichte auf Floskeln, Füllwörter und Aufwertungswörter (z. B. «Zusammenfassend», «grundsätzlich», «umfassend»).
3. Setze Gedankenstriche sparsam («–»), ohne Kaskaden und ohne Geviertstrich.

## Richtig und falsch

1. Richtig: «Der Endpoint meldet den Zustand.» / Falsch: «Der Endpunkt meldet den Zustand.»
2. Richtig: «Der Request wird abgelehnt.» / Falsch: «Die Anfrage wird abgelehnt.»
3. Richtig: «Der Cache wird geleert.» / Falsch: «Die Zwischenspeicherung wird geleert.»
4. Richtig: «Die Queue ist voll.» / Falsch: «Die Warteschlange ist voll.»
5. Richtig: `fix(auth): Token-Ablauf korrekt prüfen` / Falsch: `fix(auth): fix token expiry check`

Pflege nur per PR in cmi-github-infrastructure.
