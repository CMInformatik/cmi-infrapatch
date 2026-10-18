---
paths:
  - "**/*.md"
---

# Glossar CMI

## Zweck

Einheitliche Schreibweise und Bedeutung der CMI-Begriffe; dieses Glossar ist führend, Repo-Glossare ergänzen nur Repo-Spezifisches.

## Allgemein

| Begriff | Schreibweise | Bedeutung bei CMI | Herkunft |
| --- | --- | --- | --- |
| Mandant | «Mandant»; `Tenant`/`tenantId` nur als Code-Key | Kundeninstallation mit eigener Datenbank, eigenem KPF und eigenen Lizenzen | Wiki EN 3906928641, 5802393619; PR 18462 Metatool-Glossar |
| Benutzende | «Benutzende»; «Benutzer:in» nur im Singular; nicht «User» | Personen, die eine CMI-Lösung bedienen | Wiki cmiag 1508442113, 4233691155 |
| Entwickelnde | «Entwickelnde»; «Entwickler:in» im Singular; nicht «Developer» | Personen, die Software entwickeln | analog Wiki cmiag 4233691155 |
| Modell | «Modell», nicht «Model» | Ebene, die Aussehen und Verhalten aller Standardobjekte und Scripts definiert | Hilfe 26.0 |
| Lösung, Service | «Lösung» oder «Service», nicht «Produkt» | Angebot von CMI | Wiki cmiag 4141907972 |
| Fachanwendung | «Fachanwendung», nicht «App» | Fachlich abgegrenzte Anwendung der CMI-Lösung | Wiki cmiag 1508442113 |
| Webanwendung | «Webanwendung», nicht «Web-App» | Technische Anwendung im Browser (nicht fachlich gemeint) | Entscheid Sprachregelung 01.10.2026 |
| Seite | «Seite» für Bildschirmseiten und Navigation, nicht «Page»; «Page» nur für das Layout-Element im Modell | Seite der Oberfläche | Wiki cmiag 1508442113 |
| Card | «Card», nicht «Cardpage» | Karte der Oberfläche | Wiki cmiag 1508442113 |
| Client, Service | englisch; «Dienst» und «Hintergrunddienst» nicht verwenden | Programm bzw. Serverkomponente | Wiki cmiag 4141907972; Bestandssuche 04.10.2026 |
| Endpoint | «Endpoint», auch in Logs | Adresse, über die ein Service per HTTP erreichbar ist | Wiki EN 5800919058; Logging-Richtlinie LOG-05 |
| Interface | nur Code-Typ; «Schnittstelle» für die Anbindung von Fremdsystemen | Code-Typ bzw. Anbindung | Entscheid Sprachregelung 01.10.2026 (Bestand: Interface 175, Schnittstelle 126) |
| Workspace | englisch; CWS = Custom Workspace (kundenspezifischer Workspace); im Infrastruktur-Kontext «Terraform-Workspace» ausschreiben | Ohne Zusatz der CMI-Workspace (Einheit im Code) | Wiki cmiag 527149; Wiki EN 5579112469, 6039502857; Bestandssuche 04.10.2026; Review PR 232 |
| Plugin | «Plugin», nicht «Plug-in» | MetaTool-Plugin, Claude-Plugin | Wiki EN 525740, 6016401411; Bestandssuche 04.10.2026 |
| Worker | englisch | Eigener Prozess für Code ausserhalb des Hauptprozesses | Wiki EN 5827133469 |
| Modul | «Modul»; sonst «Terraform-Modul» bzw. «Code-Modul» | Ohne Zusatz das lizenzpflichtige CMI-Modul (`M_*`) | Wiki DOK 5948243986; Bestandssuche 04.10.2026 |
| KPF | «KPF» | Kundenspezifisches Parameterfile | Hilfe 26.0 |
| Geschäft | «Geschäft», Synonym «Dossier»; `Geschaeft` nur als Code-Key | Zentrales Fachobjekt der Geschäftsverwaltung, Basistyp «abstraktes Geschäft» | Wiki mt 525707, DOK 73695247; Bestandssuche 04.10.2026; Review PR 232 |
| Aktivität | «Aktivität»; `Aktivitaet` nur als Code-Key | Fachobjekt von CMI Aufgaben | Bestandssuche 04.10.2026 |
| Lizenz | «Lizenz»; `Licence`/`License` nur als Code-Key | Nutzungsberechtigung für ein Modul | Bestandssuche 04.10.2026 |
| Kontakt | «Kontakt»; `Contact` nur als Code-Key | Person oder Organisation im Kontaktverzeichnis | Bestandssuche 04.10.2026 |
| Releasenotes | zusammen | Dokumentation der Änderungen eines Releases | Wiki cmiag 1508442113 |
| KI+ | «KI+», nicht «CMI KI+» | Name der Lösung; extern «KI+ von CMI» | Wiki cmiag 1508442113 |

## Modell und Aufbau

| Begriff | Schreibweise | Bedeutung bei CMI | Herkunft |
| --- | --- | --- | --- |
| Metatool | «Metatool» | Ebene mit dem grössten Teil des Programmcodes, für alle Anwendungen gleich | Hilfe 26.0 |
| TypeDefinition | «TypeDefinition» | Abstrakte Vorlage für Objekte eines Typs | Hilfe 26.0 |
| Supertype | «Supertype» | TypeDefinition, von der Datenfelder und Assoziationen geerbt werden | Hilfe 26.0 |
| Assoziation | «Assoziation» | Verbindung zu einer TypeDefinition, Stammdatenliste oder einem Register | Hilfe 26.0 |
| Layout | «Layout» | Maskendesign je TypeDefinition | Hilfe 26.0 |
| Header | «Header» | Oberer Bereich der Detailansicht | Hilfe 26.0 |
| Page | «Page» | Seite im Inhaltsverzeichnis der Detailansicht | Hilfe 26.0 |
| Sektion | «Sektion» | Container für zusammengehörige Layout-Elemente | Hilfe 26.0 |
| Spalte | «Spalte» | Horizontale Aufteilung einer Sektion | Hilfe 26.0 |
| Register | «Register» | Flache oder hierarchische Begriffsliste mit Aktenzeichen | Hilfe 26.0 |
| Registereintrag | «Registereintrag», Synonym «Registraturposition» | Einzelnes Objekt eines Registers | Hilfe 26.0; Review PR 232 |
| Separator | «Separator» | Trennzeichen der Hierarchieebenen im Aktenzeichen | Hilfe 26.0 |
| Tree | «Tree» | Hierarchische Darstellung, Synonym Baum | Hilfe 26.0 |
| Stammdatenliste | «Stammdatenliste» | Sammlung von Listeneinträgen mit «Beschreibung» und «inaktiv» | Hilfe 26.0 |
| Displayname | «Displayname» | Anzeigename eines Objekts, im KPF anpassbar | Hilfe 26.0 |
| Umbenennung | «Umbenennung» | Umbenennen von Feldern und TypeDefinitions im KPF | Hilfe 26.0 |

## Felder und Suche

| Begriff | Schreibweise | Bedeutung bei CMI | Herkunft |
| --- | --- | --- | --- |
| Datenfeld | «Datenfeld» | Direkt auf einer TypeDefinition definiertes Feld | Hilfe 26.0 |
| Textfeld, Nummernfeld | «Textfeld», «Nummernfeld» | Unterarten des Datenfelds | Hilfe 26.0 |
| Datumsfeld | «Datumsfeld»; «Von-Datum», «Bis-Datum» | Zeitspanne mit frühestem und spätestem Zeitpunkt | Hilfe 26.0 |
| Booleanfeld | «Booleanfeld» | Werte true, false, null | Hilfe 26.0 |
| Abfragemöglichkeit | «Abfragemöglichkeit»; Werte `Never`, `OnDemand`, `PerDefault` unverändert | Legt fest, ob und wie ein Datenfeld in der Suche verfügbar ist | Hilfe 26.0 |
| Abfragestile | `DropDown`, `MultipleChoiceAll`, `MultipleChoiceAny`, `SimpleText`, `SubQuery` unverändert | Art der Abfrage eines Feldes | Hilfe 26.0 |
| Numerator | «Numerator» | Zähler auf Registern, wie oft ein Registereintrag zugewiesen wurde | Hilfe 26.0 |

## Verhalten

| Begriff | Schreibweise | Bedeutung bei CMI | Herkunft |
| --- | --- | --- | --- |
| Löschverhalten | «Löschverhalten»; Werte `Restrict`, `NullifyOrCascade` unverändert | Verhalten beim Löschen von Assoziationen | Hilfe 26.0 |
| Dokumentverhalten | «Dokumentverhalten» | Eigenschaften der TypeDefinition «Dokument» auf Ebene Modell | Hilfe 26.0 |
| Checkout/Checkin | «Checkout», «Checkin» | Dokument aus- und einchecken; Checkin erstellt eine Version | Hilfe 26.0 |
| Versionierung | «Versionierung» | Alle Versionen eines Dokuments | Hilfe 26.0 |
| Rendering | «Rendering» | Zweite Version eines Dokuments in anderem Format | Hilfe 26.0 |
| Scripts | «Validate-Script», «Change-Script», «Menü-Script»; die Art immer nennen | Script vor dem Speichern, bei Feldänderung bzw. per Menü-Button; «Script» allein bezeichnet in der Lösung auch andere Scripts | Hilfe 26.0; Review PR 232 |

## Fachbegriffe

| Begriff | Schreibweise | Bedeutung bei CMI | Herkunft |
| --- | --- | --- | --- |
| Traktandum | «Traktandum», Plural «Traktanden»; nicht «Traktande» | Einzelner Punkt der Traktandenliste einer Sitzung | Bestandssuche 04.10.2026 |
| Sitzung | «Sitzung»; nicht «Meeting» | Zusammenkunft eines Gremiums | Bestandssuche 04.10.2026 |
| Traktandierung | «Traktandierung» | Geschäft zur Traktandenliste einer Sitzung hinzufügen | Hilfe 26.0 |
| Sitzungstraktandierung | «Sitzungstraktandierung» | Offizielle Schreibweise | Wiki cmiag 1508442113 |
| Traktandumsnotiz | «Traktandumsnotiz» | Offizielle Schreibweise | Wiki cmiag 1508442113 |
| Beschlussnummernvergabe | «Beschlussnummernvergabe» | Offizielle Schreibweise | Wiki cmiag 1508442113 |
| Dossiertyp | «Dossiertyp» | Offizielle Schreibweise | Wiki cmiag 1508442113 |
| Facettierung | «Facettierung» | Offizielle Schreibweise | Wiki cmiag 1508442113 |
| Wizard | «Wizard», «Neuwizard», «Erstellungswizard»; Wiki-Schreibweise geht der Hilfe («Neu-Wizard») vor | Unterstützt Schritt für Schritt beim Erstellen eines Objekts | Wiki cmiag 1508442113; Hilfe 26.0 |
| Benutzergruppen | «Benutzergruppen» | Gruppen aus beliebig vielen Einzelrechten | Hilfe 26.0 |
| Webservices | «Webservices» | Stellen Inhalte für einen anderen Mandanten oder ein Fremdsystem bereit | Hilfe 26.0 |
| Server-Service | «Server-Service» | Serverkomponente, Windows-Service auf dem Applikationsserver | Hilfe 26.0 |
| AIS-Begriffe | «Tektonik», «Magazinverwaltung», «Akzessionen», «Provenienzen» | Fachbegriffe des Archivinformationssystems | Hilfe 26.0 |
| Reportdesigner | zusammen | Werkzeug zum Erstellen von Reports | Hilfe 26.0 |

## Produktnamen

| Regel | Schreibweise |
| --- | --- |
| Lösungsnamen ohne Bindestrich | CMI Lösungsplattform, CMI AIS, CMI Angebote, CMI API, CMI Archiv, CMI Aufgaben, CMI Bau, CMI Behörden, CMI Beschaffungen, CMI BrainCONNECT, CMI Bürger, CMI Cloud, CMI Dossier, CMI Forms, CMI Hunde, CMI iCampus, CMI KES, CMI Kontakte, CMI LehrerOffice, CMI Migrationstools, CMI Passivierung, CMI Protokoll, CMI Schule, CMI Scolaris, CMI Sitzungen, CMI Sitzungsgeld, CMI SPD, CMI Tomba, CMI Unterricht, CMI Verträge, CMI Zivilstand |
| Zugehörigkeit mit Bindestrich | CMI-Lösung, CMI-Fachlösung, CMI-Team, CMI-Wiki |
| EN-EN getrennt | Desktop Client, Web Client, Mobile Client, Login Services |
| Produktname = Fachbegriff | CMI Aufgaben = Aktivitäten; CMI Protokoll = Sitzungsmanagement; CMI Sitzungen = Sitzungsvorbereitung; CMI Dossier = Allgemeine Geschäftsverwaltung; CMI Behörden = Behördenverzeichnis; CMI Verträge = Vertragsverwaltung |

Quelle Produktnamen: Wiki cmiag 1508442113 (Schreibweise), Hilfe 26.0 (Fachbegriffe).
