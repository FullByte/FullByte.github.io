# Good Software

=== "EN"

    **Good software is trustable, stable, and secure.**

    It is not enough for code to just "work". Good software earns the user's trust by being reliable, protecting their data, and behaving predictably. We achieve this by being transparent about our engineering practices, rigorous in our testing, and honest about our system's capabilities.

=== "DE"

    **Gute Software ist vertrauenswürdig, stabil und sicher.**

    Es reicht nicht aus, dass Code einfach nur „funktioniert“. Gute Software verdient das Vertrauen der Nutzer durch Zuverlässigkeit, Datensicherheit und vorhersehbares Verhalten. Wir erreichen dies durch transparente Entwicklungspraktiken, rigoroses Testen und Ehrlichkeit über die Fähigkeiten unseres Systems.

## Transparency & Trust
=== "EN"

    We believe that trust is built through transparency. We clearly define **how** we secure data, **how** we ensure availability, and **how** we handle failures. We do not hide behind obscurity; we rely on proven standards and defensible architecture.

=== "DE"

    Wir glauben, dass Vertrauen durch Transparenz entsteht. Wir definieren klar, **wie** wir Daten sichern, **wie** wir Verfügbarkeit gewährleisten und **wie** wir mit Ausfällen umgehen. Wir verstecken uns nicht hinter Unklarheiten; wir setzen auf bewährte Standards und eine verteidigungsfähige Architektur.

## Limits & Scope
=== "EN"

    Every piece of software has limits. We are explicit about what our systems are **not** designed to do. Misusing a system outside its intended scope—such as using a standard web app for high-frequency trading or life-critical control systems—leads to failure and unhappy customers. We define these operational boundaries clearly so that we deliver excellence within them.

=== "DE"

    Jede Software hat Grenzen. Wir machen explizit deutlich, wofür unsere Systeme **nicht** ausgelegt sind. Die missbräuchliche Nutzung eines Systems außerhalb seines vorgesehenen Bereichs – wie z. B. die Nutzung einer Standard-Web-App für Hochfrequenzhandel oder lebenswichtige Steuerungssysteme – führt zu Ausfällen und unzufriedenen Kunden. Wir definieren diese operativen Grenzen klar, um innerhalb dieser Grenzen Exzellenz zu liefern.

## How to use this document
=== "EN"

    This guide serves as our engineering standard. It is organised by topic, with a specific focus on **General Engineering Principles**, **Web Applications on Azure**, and **GitHub-based Deployment**.

    Each chapter contains:
    *   **General**: Universal principles that apply regardless of the technology stack. **Start here.**
    *   **Azure**: Concrete implementation guidance for our primary cloud platform.
    *   **GitHub**: Operational details for our deployment and security automation pipelines.

    Use the **General** sections as your baseline for every project. Use the **Azure** and **GitHub** sections as the mandatory standard when working with our default stack.

=== "DE"

    Dieser Leitfaden dient als unser technischer Standard. Er ist nach Themen gegliedert, mit besonderem Fokus auf **Allgemeine Entwicklungsprinzipien**, **Webanwendungen auf Azure** und **Deployment mit GitHub**.

    Jedes Kapitel enthält:
    *   **Allgemein**: Universelle Prinzipien, die unabhängig vom Technologie-Stack gelten. **Hier beginnen.**
    *   **Azure**: Konkrete Implementierungsrichtlinien für unsere primäre Cloud-Plattform.
    *   **GitHub**: Operative Details für unsere Deployment- und Sicherheitsautomatisierung.

    Nutze die **Allgemeinen** Abschnitte als Basis für jedes Projekt. Nutze die **Azure**- und **GitHub**-Abschnitte als verbindlichen Standard, wenn du mit unserem Standard-Stack arbeitest.

## Core Principles

=== "EN"

    Principles that apply regardless of technology.

=== "DE"

    Prinzipien, die unabhängig von der Technologie gelten.

**General**
=== "EN"

    - **CIA Triad**
      - **Confidentiality**: Only authorised parties access data (access control, encryption).
      - **Integrity**: Data and systems remain accurate and unaltered (checksums, signing, audit logs).
      - **Availability**: Systems and data are available when needed (redundancy, resilience, DDoS mitigation).
    - **Least Privilege**: Users and services get only the minimum permissions required for their role or task.
    - **Defense in Depth**: Combine multiple layers (network, identity, application, data) so a single failure does not compromise the whole system.
    - **Keep it simple**: Prefer simple, understandable designs and processes over complex ones. Simpler systems are easier to secure, operate, and audit. Avoid unnecessary abstraction, duplication of concepts, or tooling that does not pull its weight.

=== "DE"

    - **CIA-Triade (Schutzziele)**
      - **Vertraulichkeit (Confidentiality)**: Nur autorisierte Parteien haben Zugriff auf Daten (Zugriffskontrolle, Verschlüsselung).
      - **Integrität (Integrity)**: Daten und Systeme bleiben korrekt und unverändert (Prüfsummen, Signaturen, Audit-Logs).
      - **Verfügbarkeit (Availability)**: Systeme und Daten sind verfügbar, wenn sie benötigt werden (Redundanz, Resilienz, DDoS-Schutz).
    - **Least Privilege (Geringstes Privileg)**: Nutzer und Dienste erhalten nur die minimalen Berechtigungen, die für ihre Rolle oder Aufgabe erforderlich sind.
    - **Defense in Depth (Verteidigung in der Tiefe)**: Kombination mehrerer Schutzschichten (Netzwerk, Identität, Anwendung, Daten), damit ein einzelner Fehler nicht das gesamte System kompromittiert.
    - **Keep it simple (Einfachheit)**: Bevorzuge einfache, verständliche Designs und Prozesse gegenüber komplexen. Einfachere Systeme sind leichter zu sichern, zu betreiben und zu prüfen. Vermeide unnötige Abstraktion, Duplizierung von Konzepten oder Tools, die ihren Aufwand nicht rechtfertigen.

#### Principles -> example minimum requirements to define

=== "EN"

    - **Confidentiality**
      - All internet-facing endpoints use TLS 1.3.
      - Secrets are only stored in a vault, never in source control.
      - Access to production data is role-based and logged.
    - **Integrity**
      - Pull requests require review before merge to protected branches.
      - CI verifies tests and static checks before deployment.
      - Critical configuration changes are tracked in version control.
    - **Availability**
      - Define target uptime and alerting thresholds per critical service.
      - Define backup cadence and recovery objectives (RPO/RTO).
      - Perform restore tests on a fixed schedule.
    - **Least Privilege**
      - No shared admin accounts for normal operations.
      - Admin access is limited, time-bound where possible, and auditable.
      - Permissions are reviewed periodically.
    - **Defense in Depth**
      - Use at least identity controls, network controls, and application controls.
      - Exposed services are protected by WAF and monitoring.
      - Logging and alerting are enabled for security-relevant events.
    - **Keep it simple**
      - Minimise number of environments, tools, and custom role variants.
      - Prefer one standard deployment path and one standard rollback path.
      - Remove controls/processes that add complexity without measurable value.

=== "DE"

    - **Vertraulichkeit**
      - Alle öffentlich zugänglichen Endpunkte nutzen TLS 1.3.
      - Geheimnisse (Secrets) werden nur in einem Vault gespeichert, niemals in der Versionsverwaltung.
      - Der Zugriff auf Produktionsdaten ist rollenbasiert und protokolliert.
    - **Integrität**
      - Pull Requests erfordern ein Review vor dem Merge in geschützte Branches.
      - CI verifiziert Tests und statische Prüfungen vor dem Deployment.
      - Kritische Konfigurationsänderungen werden in der Versionsverwaltung nachverfolgt.
    - **Verfügbarkeit**
      - Ziel-Uptime und Alarmierungsschwellen pro kritischem Service definieren.
      - Backup-Turnus und Wiederherstellungsziele (RPO/RTO) definieren.
      - Restore-Tests nach festem Zeitplan durchführen.
    - **Least Privilege**
      - Keine geteilten Admin-Accounts für den normalen Betrieb.
      - Admin-Zugriff ist begrenzt, zeitlich beschränkt (wo möglich) und auditierbar.
      - Berechtigungen werden regelmäßig überprüft.
    - **Defense in Depth**
      - Nutzung von mindestens Identitätskontrollen, Netzwerkkontrollen und Anwendungskontrollen.
      - Exponierte Dienste sind durch WAF und Monitoring geschützt.
      - Logging und Alerting sind für sicherheitsrelevante Ereignisse aktiviert.
    - **Keep it simple**
      - Anzahl der Umgebungen, Tools und benutzerdefinierten Rollenvarianten minimieren.
      - Einen Standard-Deployment-Pfad und einen Standard-Rollback-Pfad bevorzugen.
      - Kontrollen/Prozesse entfernen, die Komplexität ohne messbaren Mehrwert hinzufügen.

## Identity & Access

=== "EN"

    Secure identity management is the foundation of access control.

=== "DE"

    Sicheres Identitätsmanagement ist das Fundament der Zugriffskontrolle.

**General**
=== "EN"

    - Use a central identity provider for users and service accounts; avoid local accounts for application access.
    - Enforce **Multi-Factor Authentication (MFA)** for human users.
    - Apply **Least Privilege**: grant only the roles and permissions needed for each identity.
    - Prefer **managed identities** or short-lived tokens for applications so credentials are not stored in config.

=== "DE"

    - Nutze einen zentralen Identitätsanbieter (IdP) für Nutzer und Service-Konten; vermeide lokale Accounts für den Zugriff.
    - Erzwinge **Multi-Faktor-Authentifizierung (MFA)** für alle menschlichen Benutzer.
    - Wende das Prinzip des **geringsten Privilegs** an: Vergib nur die Rollen und Berechtigungen, die für die jeweilige Identität erforderlich sind.
    - Bevorzuge **Managed Identities** oder kurzlebige Tokens für Anwendungen, damit keine Zugangsdaten in der Konfiguration gespeichert werden müssen.

**Azure**
=== "EN"

    - **Microsoft Entra ID (Azure AD)**: Use for user and service identities. Enforce MFA via Conditional Access.
    - Assign only required **Azure roles** (e.g. Contributor, Reader) and scope them to resource groups or resources. Prefer **managed identities** for apps (e.g. App Service, Functions) so no passwords are stored.
    - Use **Conditional Access** for location, device, or risk-based access where appropriate.

=== "DE"

    - **Microsoft Entra ID (Azure AD)**: Verwende es für Benutzer- und Dienstidentitäten. Erzwinge MFA über Conditional Access.
    - Weise nur erforderliche **Azure-Rollen** (z. B. Contributor, Reader) zu und beschränke ihren Geltungsbereich auf Ressourcengruppen oder Ressourcen. Bevorzuge **Managed Identities** für Apps (z. B. App Service, Functions), um das Speichern von Passwörtern zu vermeiden.
    - Nutze **Conditional Access** für standort-, geräte- oder risikobasierten Zugriff, wo dies sinnvoll ist.

**GitHub**
=== "EN"

    - Use **GitHub** as the identity for CI/CD: authenticate Actions with OIDC or fine-grained tokens where possible instead of long-lived secrets.
    - Restrict repository and organisation access with teams and least-privilege permissions; require 2FA for organisation members.

=== "DE"

    - Nutze **GitHub** als Identität für CI/CD: Authentifiziere Actions über OIDC oder fein granulare Tokens anstelle von langlebigen Secrets.
    - Beschränke den Zugriff auf Repositories und Organisationen durch Teams und Least-Privilege-Berechtigungen; fordere 2FA für Organisationsmitglieder.

## User Management

=== "EN"

    Effective user and role modeling ensures secure isolation and maintainability.

=== "DE"

    Effektive Nutzer- und Rollenmodellierung gewährleistet sichere Isolierung und Wartbarkeit.

**General**
=== "EN"

    - **Users**: Represent human or system actors. Identify them via a single source of truth (e.g. IdP); avoid duplicate or local user stores that can get out of sync.
    - **Roles**: Define permissions by role (e.g. Viewer, Editor, Admin) rather than per-user. Assign users to roles; keep the set of roles small and well-defined so that access reviews and audits are straightforward.
    - **Groups**: Use groups to assign roles to many users at once and to reflect organisational structure (e.g. “Developers”, “Support”). Prefer group-based role assignment over individual grants so onboarding/offboarding is consistent.
    - **Tenants (customers)**: In multi-tenant systems, **tenant isolation** is critical. Every data access and configuration must be scoped by tenant (e.g. tenant ID in queries, row-level or resource-level isolation). Never allow cross-tenant data access unless explicitly designed (e.g. admin view with audit). Design tenant boundaries early; retrofitting isolation is error-prone and risky.
    - **Principle of least privilege**: Each role should have the minimum permissions needed; limit cross-tenant or global admin capabilities to a small, audited set of identities.
    - **Lifecycle**: Define how users are created, updated, disabled, and removed; how role and group membership changes; and how tenant onboarding/offboarding works. Document and automate where possible.

=== "DE"

    - **Nutzer**: Repräsentieren menschliche oder System-Akteure. Identifizieren Sie diese über eine einzige Quelle der Wahrheit (z. B. IdP); vermeiden Sie doppelte oder lokale Nutzerspeicher, die asynchron werden können.
    - **Rollen**: Definieren Sie Berechtigungen pro Rolle (z. B. Betrachter, Bearbeiter, Admin) statt pro Nutzer. Weisen Sie Nutzer Rollen zu; halten Sie die Menge an Rollen klein und klar definiert, damit Audits einfach bleiben.
    - **Gruppen**: Nutzen Sie Gruppen, um Rollen vielen Nutzern gleichzeitig zuzuweisen und die Organisationsstruktur abzubilden (z. B. „Entwickler“, „Support“). Bevorzuge gruppenbasierte Zuweisungen gegenüber individuellen Rechten, um On- und Offboarding konsistent zu halten.
    - **Mandanten (Kunden)**: In Multi-Tenant-Systemen ist die **Mandantenisolierung** kritisch. Jeder Datenzugriff muss auf den Mandanten beschränkt sein (z. B. Tenant-ID in Abfragen, Row-Level-Security). Erlauben Sie niemals mandantenübergreifenden Zugriff, es sei denn, dies ist explizit vorgesehen (z. B. Admin-Ansicht mit Audit). Planen Sie Mandantengrenzen frühzeitig ein; nachträgliche Isolierung ist fehleranfällig und riskant.
    - **Prinzip des geringsten Privilegs**: Jede Rolle sollte nur die minimal notwendigen Berechtigungen haben; beschränken Sie mandantenübergreifende oder globale Admin-Rechte auf wenige, auditierte Identitäten.
    - **Lebenszyklus**: Definieren Sie, wie Nutzer erstellt, aktualisiert, deaktiviert und entfernt werden; wie sich Rollen- und Gruppenmitgliedschaften ändern; und wie das Onboarding/Offboarding von Mandanten funktioniert. Dokumentieren und automatisieren Sie, wo möglich.

**Azure**
=== "EN"

    - **Entra ID (Azure AD)**: Use **users** and **groups** for human access; use **app roles** or **groups** for application-level authorisation (e.g. “Admin”, “Reader” in your app). For multi-tenant SaaS, use **Entra ID tenants** per customer or **B2B** guest users in a single tenant; document whether you use single-tenant (one directory per customer) or multi-tenant (one directory, tenant ID in app data).
    - **Azure RBAC**: Use **custom roles** only when built-in roles are insufficient; scope assignments to resource groups or resources so one customer’s Azure resources are not visible to another. For “tenant = customer”, use separate resource groups or subscriptions per tenant and assign Azure roles accordingly.
    - **Managed identities**: Prefer managed identities for app-to-Azure access; avoid service accounts with long-lived secrets. Use **user-assigned** identities when the same identity is shared across components.

=== "DE"

    - **Entra ID (Azure AD)**: Nutzen Sie **Nutzer** und **Gruppen** für menschlichen Zugriff; nutzen Sie **App Roles** oder **Gruppen** für Autorisierung auf Anwendungsebene. Für SaaS nutzen Sie **Entra ID Tenants** pro Kunde oder **B2B**-Gastnutzer in einem einzelnen Tenant; dokumentieren Sie, ob Sie Single-Tenant (ein Verzeichnis pro Kunde) oder Multi-Tenant (ein Verzeichnis, Tenant-ID in App-Daten) nutzen.
    - **Azure RBAC**: Nutzen Sie **Custom Roles** nur, wenn integrierte Rollen nicht ausreichen; beschränken Sie Zuweisungen auf Ressourcengruppen, damit die Ressourcen eines Kunden für andere nicht sichtbar sind.
    - **Managed Identities**: Bevorzugen Sie Managed Identities für den Zugriff von Apps auf Azure-Ressourcen; vermeiden Sie Service Accounts mit langlebigen Secrets. Nutzen Sie **User-Assigned Identities**, wenn dieselbe Identität von mehreren Komponenten geteilt wird.

**GitHub**
=== "EN"

    - **Organisations and repos**: Use **teams** to group people and assign repository and org permissions (Read, Write, Admin). Prefer team-based access so adding/removing someone is one change.
    - **Roles**: Use the built-in roles (Member, Admin, etc.) and repository roles; avoid over-customising unless necessary. For “tenant = customer”, you may use separate organisations or repos per customer and grant access via teams; document the chosen model.
    - **Fine-grained permissions**: Prefer **fine-grained** personal access tokens and **OIDC** for Actions so each integration has minimal scope.

=== "DE"

    - **Organisationen und Repos**: Nutzen Sie **Teams**, um Personen zu gruppieren und Berechtigungen zuzuweisen. Bevorzuge teambasierten Zugriff, damit das Hinzufügen/Entfernen einer Person nur eine Änderung erfordert.
    - **Rollen**: Nutzen Sie die integrierten Rollen (Member, Admin etc.); vermeiden Sie Überanpassung, wenn nicht notwendig.
    - **Fine-grained Permissions**: Bevorzuge **feingranulare** Personal Access Tokens und **OIDC** für Actions, damit jede Integration nur minimalen Zugriff hat.

## Frontend vs. Backend

=== "EN"

    Clear trust boundaries between client and server prevent security bypasses.

    Keep the trust boundary clear: frontend is user-controlled, backend is policy-enforced.

=== "DE"

    Klare Vertrauensgrenzen zwischen Client und Server verhindern Sicherheitsumgehungen.

    Die Vertrauensgrenze muss klar sein: Das Frontend wird vom Benutzer kontrolliert, das Backend setzt die Richtlinien durch.

**General**
=== "EN"

    - **Frontend responsibilities**
      - Enforce safe rendering (XSS prevention), strict input validation on UI level, and secure session/token handling.
      - Never embed secrets (API keys with privileged scope, signing keys, DB credentials) in frontend code.
      - Use secure browser defaults where relevant (CSP, `HttpOnly`/`Secure` cookies, same-site strategy).
    - **Backend responsibilities**
      - Treat all client input as untrusted, even if frontend validates it.
      - Enforce authentication, authorisation, tenant isolation, rate limits, and audit logging server-side.
      - Centralise security-critical decisions in backend services, not in client logic.
    - **Typical No-Gos**
      - “Hidden UI button = access control” (it is not).
      - Trusting tenant/user IDs from client without server-side checks.
      - Returning excessive data fields to frontend “just in case”.

=== "DE"

    - **Frontend-Verantwortlichkeiten**
      - Sicheres Rendering erzwingen (XSS-Prävention), strenge Eingabevalidierung auf UI-Ebene und sicheres Session/Token-Handling.
      - Niemals Geheimnisse (API-Keys mit erweiterten Rechten, Signaturschlüssel, DB-Zugangsdaten) im Frontend-Code einbetten.
      - Sichere Browser-Standards nutzen (CSP, `HttpOnly`/`Secure` Cookies, Same-Site-Strategie).
    - **Backend-Verantwortlichkeiten**
      - Alle Client-Eingaben als nicht vertrauenswürdig behandeln, selbst wenn das Frontend validiert.
      - Authentifizierung, Autorisierung, Mandantenisolierung, Ratenbegrenzung und Audit-Logging serverseitig durchsetzen.
      - Sicherheitskritische Entscheidungen zentral im Backend treffen, nicht in der Client-Logik.
    - **Typische No-Gos**
      - „Versteckter Button = Zugriffskontrolle“ (das ist keine Sicherheit).
      - Vertrauen auf Mandanten-/Nutzer-IDs vom Client ohne serverseitige Prüfung.
      - Rückgabe übermäßiger Datenfelder an das Frontend „nur für den Fall“.

**Azure**
=== "EN"

    - Put frontend and backend behind appropriate edge controls (WAF, TLS, DDoS controls).
    - Keep backend/private APIs in private networking where possible (Private Endpoints/VNet).
    - Enforce identity and role checks in backend APIs via Entra-integrated auth patterns.

=== "DE"

    - Frontend und Backend hinter geeignete Edge-Kontrollen (WAF, TLS, DDoS-Schutz) stellen.
    - Backend/Private APIs in private Netzwerke legen, wo möglich (Private Endpoints/VNet).
    - Identitäts- und Rollenprüfungen in Backend-APIs über Entra-integrierte Auth-Muster durchsetzen.

**GitHub**
=== "EN"

    - Separate frontend/backend CI jobs and required checks (e.g. frontend lint/e2e, backend SAST/integration/security tests).
    - Require CODEOWNERS review for backend auth/authorization and security-sensitive frontend changes.

=== "DE"

    - Frontend- und Backend-CI-Jobs sowie erforderliche Prüfungen trennen (z. B. Frontend-Lint/E2E, Backend-SAST/Integration/Security-Tests).
    - CODEOWNERS-Review für Backend-Auth/Autorisierung und sicherheitskritische Frontend-Änderungen anfordern.

## Interfaces

=== "EN"

    Well-defined interfaces enable automation and secure interaction across all clients.

    Good software is built on strong, well-defined interfaces. The **API** (Application Programming Interface) is the core of the application, enforcing all logic and security. The **UI** (User Interface) is just one of many possible clients. This approach enables automation, deep linking, and headless usage, but requires strict backend validation.

=== "DE"

    Klar definierte Schnittstellen ermöglichen Automatisierung und sichere Interaktion über alle Clients hinweg.

    Gute Software basiert auf starken, klar definierten Schnittstellen. Die **API** (Application Programming Interface) ist der Kern der Anwendung und setzt alle Logik und Sicherheit durch. Die **UI** (Benutzeroberfläche) ist nur einer von vielen möglichen Clients. Dieser Ansatz ermöglicht Automatisierung, Deep Linking und Headless-Nutzung, erfordert aber strikte Backend-Validierung.

**General**
=== "EN"

    - **API First**: Design the API before the UI. The API must be complete, secure, and documented (e.g., OpenAPI/Swagger).
    - **UI as a Client**: Treat your own UI as an untrusted client. It should not contain business rules that are not also enforced by the API.
    - **Headless Usage**: Enable usage without a GUI via CLI arguments or URL parameters. This supports automation and power users.
    - **Deep Linking**: Allow users to bookmark or share specific states (e.g., filters, search queries) via URL parameters.
    - **UI Hints**: The UI should guide the user (e.g., input masks, validation feedback) but never be the only line of defense.
    - **Risk - Manipulation**: Users can modify URL parameters or API calls to bypass UI restrictions. The backend must validate every input.
    - **Risk - Data Leakage**: Never put secrets (passwords, tokens, PII) in URL parameters, as they are logged in browser history and proxies.
    - **Mitigation**: Validate all inputs on the backend. Use headers/body for secrets. Ensure GET requests are idempotent (read-only).

=== "DE"

    - **API First**: Designe die API vor der UI. Die API muss vollständig, sicher und dokumentiert sein (z. B. OpenAPI/Swagger).
    - **UI als Client**: Behandle deine eigene UI als nicht vertrauenswürdigen Client. Sie sollte keine Geschäftsregeln enthalten, die nicht auch von der API durchgesetzt werden.
    - **Headless-Nutzung**: Ermögliche die Nutzung ohne GUI über CLI-Argumente oder URL-Parameter. Dies unterstützt Automatisierung und Power-User.
    - **Deep Linking**: Erlaube Nutzern, spezifische Zustände (z. B. Filter, Suchanfragen) per URL-Parameter zu bookmarken oder zu teilen.
    - **UI-Hinweise**: Die UI sollte den Nutzer führen (z. B. Eingabemasken, Validierungsfeedback), darf aber nie die einzige Verteidigungslinie sein.
    - **Risiko - Manipulation**: Nutzer können URL-Parameter oder API-Aufrufe ändern, um UI-Beschränkungen zu umgehen. Das Backend muss jede Eingabe prüfen.
    - **Risiko - Datenlecks**: Niemals Geheimnisse (Passwörter, Tokens, PII) in URL-Parameter packen, da diese in Browserverlauf und Proxies protokolliert werden.
    - **Mitigation**: Validiere alle Eingaben im Backend. Nutze Header/Body für Secrets. Stelle sicher, dass GET-Requests idempotent (nur lesend) sind.

## Role Matrix

=== "EN"

    A clear definition of roles and permissions enforces the principle of least privilege.

    Use least privilege by default and keep role scopes explicit.

=== "DE"

    Eine klare Definition von Rollen und Rechten setzt das Prinzip der geringsten Rechte durch.

    Nutze standardmäßig das Prinzip der geringsten Rechte und halte Rollengrenzen explizit.

**General**
=== "EN"

    | Role | Minimum rights | Typical No-Gos |
    | :--- | :--- | :--- |
    | **Admin** | Manage platform configuration, role assignment, critical approvals, incident coordination. | Daily development with admin rights; shared admin accounts; permanent broad access without review. |
    | **Developer** | Read non-production logs/metrics, deploy via approved pipeline, modify code and IaC via PR process. | Direct production database writes; bypassing CI/security checks; storing secrets locally/in repo. |
    | **User** | Access own tenant/account data and allowed product actions only. | Access to admin endpoints, raw exports of other users/tenants, debug/internal data views. |
    | **Support** | View limited customer context, run approved support actions, escalate incidents. | Unrestricted data exports, changing security policy, accessing secrets or payment internals without approval. |
    | **Service Account** | Machine-to-machine scoped permissions for one workload; short-lived credentials/managed identity. | Reusing one service account across many systems; interactive login; wildcard permissions. |

    - **Operational rules**
      - Separate human and machine identities.
      - Time-bound elevated access where possible.
      - Access review on fixed cadence and after role changes.
      - Break-glass access is audited, rare, and post-reviewed.

=== "DE"

    | Rolle | Minimale Rechte | Typische No-Gos |
    | :--- | :--- | :--- |
    | **Admin** | Plattformkonfiguration verwalten, Rollen zuweisen, kritische Genehmigungen, Vorfallkoordination. | Tägliche Entwicklung mit Admin-Rechten; geteilte Admin-Konten; dauerhafter Vollzugriff ohne Review. |
    | **Entwickler** | Nicht-Produktions-Logs lesen, Deployments über Pipelines, Code/IaC-Änderungen via PR. | Direkte Schreibzugriffe auf Produktionsdatenbanken; Umgehen von CI/Sicherheitschecks; lokale Speicherung von Secrets. |
    | **Benutzer** | Zugriff nur auf eigene Mandanten-/Kontodaten und erlaubte Produktaktionen. | Zugriff auf Admin-Endpunkte, Rohdatenexporte anderer Nutzer, Debug-Ansichten. |
    | **Support** | Begrenzter Kundenkontext, genehmigte Support-Aktionen, Eskalation von Vorfällen. | Uneingeschränkte Datenexporte, Ändern von Sicherheitsrichtlinien, Zugriff auf Secrets/Zahlungsdaten ohne Freigabe. |
    | **Service Account** | Maschinen-zu-Maschinen-Zugriff für einen Workload; kurzlebige Credentials/Managed Identity. | Wiederverwendung eines Kontos für viele Systeme; interaktives Login; Wildcard-Berechtigungen. |

    - **Operative Regeln**
      - Trennung von menschlichen und maschinellen Identitäten.
      - Zeitlich begrenzter erhöhter Zugriff, wo möglich.
      - Zugriffsüberprüfung in festem Rhythmus und nach Rollenwechseln.
      - Notfallzugriff (Break-Glass) wird auditiert, ist selten und wird nachbereitet.

**Azure**
=== "EN"

    - Map roles to Entra groups + Azure RBAC scopes (subscription/resource group/resource).
    - Prefer managed identities for services instead of client secrets.
    - Use Privileged Identity Management (PIM) or equivalent for just-in-time elevation.

=== "DE"

    - Rollen auf Entra-Gruppen + Azure RBAC Scopes (Subscription/Ressourcengruppe/Ressource) abbilden.
    - Bevorzuge Managed Identities für Dienste anstelle von Client Secrets.
    - Nutze Privileged Identity Management (PIM) für Just-in-Time-Rechteerweiterung.

**GitHub**
=== "EN"

    - Map roles to GitHub teams and repository permissions (`Read`, `Triage`, `Write`, `Maintain`, `Admin`).
    - Protect critical paths (security, infra, deployment workflows) via CODEOWNERS + required reviews.
    - Restrict who can approve production deployments in protected environments.

=== "DE"

    - Rollen auf GitHub-Teams und Repository-Berechtigungen (`Read`, `Triage`, `Write`, `Maintain`, `Admin`) abbilden.
    - Schütze kritische Pfade (Sicherheit, Infra, Deployment-Workflows) durch CODEOWNERS und erforderliche Reviews.
    - Beschränke, wer Produktions-Deployments in geschützten Umgebungen genehmigen darf.

## Data Design

=== "EN"

    Secure data architecture prevents leaks and ensures strict tenant isolation.

    Data design is security design. If data boundaries are weak, tenant isolation and compliance usually fail later in production.

=== "DE"

    Sichere Datenarchitektur verhindert Lecks und gewährleistet strikte Mandantentrennung.

    Datendesign ist Sicherheitsdesign. Wenn Datengrenzen schwach sind, scheitern Mandantenisolierung und Compliance meist später in der Produktion.

**General**
=== "EN"

    - **Define data classes early**: Classify data before implementation and store the classification in architecture/docs.
    - **Brisante Daten (sensitive/high-impact data)**
      - **Definition**: Data that can cause legal, financial, security, or reputational harm if leaked, modified, or unavailable.
      - **Typical examples**: Personal data (PII), authentication data, API keys/secrets, payment data, health data, internal security logs, customer contracts.
      - **Why this matters**: Brisante data requires stricter access, stronger encryption, tighter logging, shorter exposure windows, and clearer ownership.
    - **Data minimisation**: Only collect/store data that is required for product and legal obligations.
    - **Tenant/customer separation by design**:
      - Every write/read path must be tenant-scoped.
      - Enforce tenant isolation on more than one layer (application + database policy/index/partition).
      - Prevent cross-tenant analytics/export by default; allow only via explicit audited flows.
    - **Database security basics**:
      - Encryption in transit and at rest.
      - Least-privilege database accounts (no shared superuser in runtime).
      - Backup/restore tested and aligned with data classification.
      - Data retention and deletion rules implemented, not only documented.
    - **Marking data sensitivity**:
      - Mark fields/tables/events with labels like `public`, `internal`, `confidential`, `brisant`.
      - Use labels in code, schemas, logs, and export pipelines to enforce handling rules.
      - Define owner/team for each critical data domain.
    - **Typical mistakes to avoid**:
      - Missing tenant filter in one endpoint/query.
      - Storing secrets in business tables or logs.
      - Overly broad DB permissions for app services.
      - Reusing production data in staging without anonymisation.
      - Joining multi-tenant data for reports without access guardrails.
      - Keeping personal data forever because retention/deletion jobs were not implemented.

=== "DE"

    - **Datenklassen früh definieren**: Klassifizieren Sie Daten vor der Implementierung und dokumentieren Sie dies.
    - **Brisante Daten**
      - **Definition**: Daten, deren Leck, Änderung oder Unverfügbarkeit rechtlichen, finanziellen oder rufschädigenden Schaden verursachen kann.
      - **Beispiele**: Personenbezogene Daten (PII), Auth-Daten, API-Keys, Zahlungsdaten, Gesundheitsdaten, Sicherheitslogs, Verträge.
      - **Warum das wichtig ist**: Brisante Daten erfordern strengeren Zugriff, stärkere Verschlüsselung, genaueres Logging und kürzere Aufbewahrung.
    - **Datenminimierung**: Sammeln/Speichern Sie nur Daten, die für Produkt- und rechtliche Zwecke notwendig sind.
    - **Mandantentrennung (Tenant Isolation) per Design**:
      - Jeder Schreib-/Lesezugriff muss auf den Mandanten beschränkt sein.
      - Setzen Sie Isolierung auf mehreren Ebenen durch (Anwendung + Datenbank-Policy/Index/Partition).
      - Verhindern Sie mandantenübergreifende Exporte standardmäßig; erlauben Sie sie nur über explizit auditierte Wege.
    - **Datenbank-Sicherheitsbasics**:
      - Verschlüsselung bei Übertragung und im Ruhezustand.
      - Least-Privilege-Datenbankkonten (kein geteilter Superuser zur Laufzeit).
      - Backup/Restore getestet und auf Datenklassifizierung abgestimmt.
      - Löschregeln implementiert, nicht nur dokumentiert.
    - **Markierung der Sensitivität**:
      - Kennzeichnen Sie Felder/Tabellen mit Labels wie `public`, `internal`, `confidential`, `brisant`.
      - Nutzen Sie diese Labels in Code, Schemata und Logs zur Durchsetzung von Regeln.
      - Definieren Sie Verantwortliche (Owner) für jede kritische Datendomäne.
    - **Typische Fehler**:
      - Fehlender Mandantenfilter in einem Endpunkt.
      - Speicherung von Secrets in Geschäftsdaten oder Logs.
      - Zu weitreichende DB-Berechtigungen für App-Dienste.
      - Nutzung von Produktionsdaten im Staging ohne Anonymisierung.
      - Unbeschränkte mandantenübergreifende Reports.
      - Endlose Speicherung personenbezogener Daten mangels Löschjobs.

##### Practical implementation examples (General)

=== "EN"

    - **Define data classes early**
      - Example: add a `data_classification.md` with required labels for every entity (`public`, `internal`, `confidential`, `brisant`) and an owner.
      - What to check: every table/event in architecture docs has a classification + owner + retention rule.
    - **Brisante data handling**
      - Example: fields like `email`, `phone`, `address`, `payment_ref`, `auth_token_hash` are marked as `brisant` and get stricter policies (access logging, masked exports, shorter retention).
      - What to check: access to brisante fields is role-scoped, audited, and blocked in default exports.
    - **Data minimisation**
      - Example: do not store full birth date when age band is enough; do not store plaintext IP forever if hashed/truncated fulfills the use case.
      - What to check: every stored field has a documented purpose and retention period.
    - **Tenant separation by design**
      - Example: every query includes tenant scope (`WHERE tenant_id = :tenant_id`), backed by DB-level row-level security (where supported) and unique indexes including `tenant_id`.
      - What to check: automated tests for cross-tenant access attempts fail by default.
    - **Encryption in transit and at rest**
      - In transit (TLS): enforce TLS for app-to-DB connections; reject non-TLS connections.
      - At rest: enable provider encryption/TDE and, if needed, customer-managed keys (CMK).
      - What to check: TLS-required parameter is active, certificates are valid/rotated, encryption status is enabled in DB settings.
      - DB technologies that support this (examples):
        - PostgreSQL (TLS in transit; storage/TDE via managed service or platform controls)
        - MySQL/MariaDB (TLS in transit; storage encryption/TDE depending on edition/service)
        - Microsoft SQL Server / Azure SQL (TLS + TDE)
        - MongoDB (TLS + encryption at rest in managed/self-hosted setups)
        - Redis (TLS + at-rest options depending on provider/edition)
    - **Least-privilege DB accounts**
      - Example: separate runtime account (read/write scoped), migration account (schema change only), and break-glass admin account.
      - What to check: app runtime credentials cannot create users, drop databases, or read unrelated tenant data.
    - **Backup/restore and retention**
      - Example: daily backups + PITR enabled, quarterly restore drill, automated deletion job for expired personal data.
      - What to check: latest successful restore test date, retention job status, and deletion evidence.
    - **Marking data sensitivity**
      - Example: schema comments/metadata tags (`classification=brisant`) and code annotations on DTO fields.
      - What to check: logs/exports automatically mask fields tagged as `confidential` or `brisant`.
    - **Typical mistakes and prevention**
      - Example control: static code checks + integration tests detect missing tenant filters in repository/query layer.
      - What to check: PR checklist includes tenant-scope review for data access changes.

**Azure**
=== "EN"

    - Prefer managed data services with built-in security features and enable encryption defaults.
    - Use separate databases/schemas/partitions per tenant where risk/regulatory needs require stronger isolation.
    - Use **Private Endpoints**, firewall rules, and network restrictions so databases are not publicly exposed.
    - Use **Managed Identity** and **Key Vault** for database auth/secrets; rotate credentials/keys with documented process.
    - Enable auditing/diagnostics for database access and security events; send to Log Analytics for retention and investigation.
    - Apply **Azure Policy** and Defender recommendations to detect misconfiguration (public endpoints, weak TLS, missing diagnostic settings).

=== "DE"

    - Bevorzuge Managed Data Services mit eingebauten Sicherheitsfeatures und aktiviere Standardverschlüsselung.
    - Nutze separate Datenbanken/Schemata/Partitionen pro Mandant, wenn Risiken dies erfordern.
    - Nutze **Private Endpoints**, Firewalls und Netzwerkbeschränkungen, um Datenbanken nicht öffentlich zu exponieren.
    - Nutze **Managed Identity** und **Key Vault** für Datenbankzugriffe; rotiere Credentials dokumentiert.
    - Aktiviere Auditing/Diagnose für Datenbankzugriffe und Sicherheitsereignisse (Log Analytics).
    - Wende **Azure Policy** und Defender-Empfehlungen an, um Fehlkonfigurationen zu erkennen.

**GitHub**
=== "EN"

    - Treat database schemas and migrations as code (`/db`, `/migrations`) with PR review and rollback strategy.
    - Add checks in CI for migration safety (backward compatibility, lock/timeout risk, destructive changes).
    - Never commit dumps with real customer data; use synthetic/anonymised fixtures for tests.
    - Store data model/classification docs in repo and require updates when schema changes.

=== "DE"

    - Behandle Datenbankschemata und Migrationen als Code (`/db`, `/migrations`) mit PR-Review und Rollback-Strategie.
    - Füge CI-Prüfungen für Migrationssicherheit hinzu (Abwärtskompatibilität, Lock-Risiken, destruktive Änderungen).
    - Committe niemals Dumps mit echten Kundendaten; nutze synthetische Fixtures für Tests.
    - Speichere Datenmodell-/Klassifizierungsdokumentation im Repo und fordere Updates bei Schemaänderungen.

## Secrets

=== "EN"

    Proper handling of credentials and encryption keys protects sensitive information.

=== "DE"

    Der korrekte Umgang mit Zugangsdaten und Schlüsseln schützt sensible Informationen.

**General**
=== "EN"

    - Never store secrets (API keys, connection strings, certificates) in source code or version control.
    - Use a dedicated secrets store or vault; reference secrets at runtime or in the pipeline, never commit them.
    - Encrypt sensitive data at rest and in transit; enforce **TLS 1.2+** for all external endpoints.

=== "DE"

    - Speichere niemals Geheimnisse (API-Schlüssel, Verbindungszeichenfolgen, Zertifikate) im Quellcode oder in der Versionsverwaltung.
    - Nutze einen dedizierten Secrets-Store oder Vault; referenziere Secrets zur Laufzeit oder in der Pipeline, committe sie nie.
    - Verschlüssele sensible Daten im Ruhezustand und bei der Übertragung; erzwinge **TLS 1.2+** für alle externen Endpunkte.

**Azure**
=== "EN"

    - **Azure Key Vault**: Store API keys, database credentials, and certificates. Grant access via managed identities or Entra ID with minimal permissions. Reference Key Vault from App Service, Functions, or pipelines.
    - Rely on Azure’s default encryption at rest and in transit; configure apps to use TLS 1.2+ only.

=== "DE"

    - **Azure Key Vault**: Speichere API-Schlüssel, Datenbank-Credentials und Zertifikate. Gewähre Zugriff über Managed Identities oder Entra ID mit minimalen Rechten. Referenziere Key Vault aus App Service, Functions oder Pipelines.
    - Verlasse dich auf die Standardverschlüsselung von Azure (Ruhezustand/Übertragung); konfiguriere Apps so, dass sie nur TLS 1.2+ nutzen.

**GitHub**
=== "EN"

    - Use **GitHub Secrets** (and optionally **Environments** with secrets) for deployment credentials and API keys. Never log or echo secrets in workflow output.
    - Ensure **Dependabot** and **Code Scanning** are enabled so dependency and code issues are caught; avoid committing even example or test credentials.

=== "DE"

    - Nutze **GitHub Secrets** (und optional **Environments** mit Secrets) für Deployment-Credentials und API-Keys. Logge oder gib niemals Secrets in der Workflow-Ausgabe aus.
    - Stelle sicher, dass **Dependabot** und **Code Scanning** aktiviert sind, um Abhängigkeits- und Codeprobleme zu finden; vermeide das Einchecken von Beispiel-Credentials.

## Network

=== "EN"

    Network segmentation and defense layers limit the blast radius of attacks.

=== "DE"

    Netzwerksegmentierung und Verteidigungsschichten begrenzen den Schaden bei Angriffen.

**General**
=== "EN"

    - Segment networks and restrict access to backend services; avoid exposing databases or internal APIs directly to the internet.
    - Put a **Web Application Firewall (WAF)** in front of web applications to mitigate common attacks (e.g. OWASP Top 10).
    - Use **HTTPS** everywhere; prefer TLS 1.2+ and automatic certificate management where possible.
    - Consider DDoS mitigation for public-facing production systems.

=== "DE"

    - Segmentiere Netzwerke und beschränke den Zugriff auf Backend-Dienste; vermeide die direkte Exponierung von Datenbanken oder internen APIs ins Internet.
    - Setze eine **Web Application Firewall (WAF)** vor Webanwendungen, um gängige Angriffe (z. B. OWASP Top 10) abzuwehren.
    - Nutze überall **HTTPS**; bevorzuge TLS 1.2+ und automatisches Zertifikatsmanagement.
    - Ziehe DDoS-Schutz für öffentliche Produktionssysteme in Betracht.

**Azure**
=== "EN"

    - Use **Private Endpoints** or **VNet Integration** for Azure Web Apps and backend services (databases, storage) to reduce public internet exposure.
    - Put **Azure Application Gateway** or **Front Door** with **WAF** in front of web apps.
    - Use **WAF policy tuning**: start with detection mode, review false positives, then enforce prevention mode for production.
    - Restrict traffic by source where possible: use **IP allowlists**, access restrictions, and NSG rules for admin/endpoints.
    - Apply **geo/IP restrictions** (country/region filtering) on edge/WAF level when your business model allows it.
    - Use **Azure Firewall** (and Firewall Policy) for centralized egress/ingress control in larger network topologies.
    - Enable **Azure DDoS Protection Standard** for production workloads where appropriate.
    - Azure Web Apps support HTTPS and managed certificates by default; enforce minimum TLS version in configuration.

=== "DE"

    - Nutze **Private Endpoints** oder **VNet-Integration** für Azure Web Apps und Backend-Dienste (Datenbanken, Storage), um die öffentliche Exponierung zu minimieren.
    - Setze **Azure Application Gateway** oder **Front Door** mit **WAF** vor Web Apps.
    - **WAF-Policy-Tuning**: Starte im Erkennungsmodus, prüfe False-Positives und aktiviere dann den Präventionsmodus für die Produktion.
    - Beschränke Traffic nach Quelle, wo möglich: Nutze **IP-Allowlists**, Zugriffsbeschränkungen und NSG-Regeln für Admin-Endpunkte.
    - Wende **Geo/IP-Beschränkungen** (Länderfilter) auf Edge/WAF-Ebene an, wenn das Geschäftsmodell dies erlaubt.
    - Nutze **Azure Firewall** für zentralisierte Egress/Ingress-Kontrolle in größeren Netzwerken.
    - Aktiviere **Azure DDoS Protection Standard** für Produktionsworkloads, wo angemessen.
    - Azure Web Apps unterstützen standardmäßig HTTPS und Managed Certificates; erzwinge die minimale TLS-Version in der Konfiguration.

**GitHub**
=== "EN"

    - GitHub hosts the repository and runners; ensure you do not rely on public runner IPs for allowlisting in Azure. Prefer **GitHub Actions OIDC** with Azure so no long-lived secrets are needed for deployment.

=== "DE"

    - GitHub hostet das Repository und die Runner; verlasse dich nicht auf öffentliche Runner-IPs für Allowlists in Azure. Bevorzuge **GitHub Actions OIDC** mit Azure, damit keine langlebigen Secrets für Deployments nötig sind.

## Domain Trust

=== "EN"

    Correct DNS and email configuration establishes external trust and prevents spoofing.

    Trust is also built through a clean domain and email setup. Customers, spam filters, and security teams check these basics quickly.

=== "DE"

    Korrekte DNS- und E-Mail-Konfiguration schafft externes Vertrauen und verhindert Spoofing.

    Vertrauen wird auch durch ein sauberes Domain- und E-Mail-Setup aufgebaut. Kunden, Spamfilter und Sicherheitsteams prüfen diese Grundlagen schnell.

**General**
=== "EN"

    - **Domain ownership and DNS hygiene**
      - Keep registrar, DNS provider, and domain contacts up to date.
      - Protect domain accounts with MFA and strict role-based access.
      - Document all critical DNS records and who owns them.
    - **Web domain checks**
      - HTTPS is enforced on all public endpoints; certificates are valid and auto-renewed.
      - Redirect HTTP to HTTPS and disable weak TLS/ciphers.
      - Use a canonical domain strategy (e.g. `www` or apex) and permanent redirects.
      - Ensure security headers are set where relevant (e.g. HSTS, X-Content-Type-Options, CSP as applicable).
    - **Email domain checks**
      - Configure and validate **SPF**, **DKIM**, and **DMARC** for all sending domains.
      - Start DMARC with monitoring (`p=none`), review reports, then move to stricter policy (`quarantine`/`reject`) when stable.
      - Ensure sender alignment (`From` domain aligns with SPF/DKIM domains).
      - Use dedicated subdomains for transactional/bulk mail if needed (e.g. `mail.example.com`).
    - **Operational checks**
      - Test deliverability and spam placement regularly (seed tests, DMARC aggregate reports, bounce/complaint rates).
      - Monitor certificate expiry, DNS changes, and suspicious record changes.
      - Keep an incident playbook for domain hijack, certificate failure, or email spoofing.

=== "DE"

    - **Domainbesitz und DNS-Hygiene**
      - Halten Sie Registrar-, DNS-Provider- und Domainkontakte aktuell.
      - Schützen Sie Domainkonten mit MFA und striktem rollenbasiertem Zugriff.
      - Dokumentieren Sie alle kritischen DNS-Einträge und deren Besitzer.
    - **Web-Domain-Checks**
      - HTTPS wird auf allen öffentlichen Endpunkten erzwungen; Zertifikate sind gültig und auto-erneuert.
      - Leite HTTP auf HTTPS um und deaktiviere schwache TLS-Ciphers.
      - Nutze eine kanonische Domain-Strategie (z. B. `www` oder Apex) und permanente Weiterleitungen.
      - Setze relevante Security-Header (HSTS, X-Content-Type-Options, CSP).
    - **E-Mail-Domain-Checks**
      - Konfiguriere und validiere **SPF**, **DKIM** und **DMARC** für alle sendenden Domains.
      - Starte DMARC im Monitoring (`p=none`), prüfe Berichte und wechsle dann zu strengerer Richtlinie (`quarantine`/`reject`), wenn stabil.
      - Stelle die Absender-Ausrichtung (Alignment) sicher (`From`-Domain stimmt mit SPF/DKIM überein).
      - Nutze dedizierte Subdomains für Transaktions-/Massen-Mails (z. B. `mail.beispiel.de`).
    - **Operative Checks**
      - Teste Zustellbarkeit und Spam-Platzierung regelmäßig (Seed-Tests, DMARC-Reports, Bounce/Complaint-Raten).
      - Überwache Zertifikatsablauf, DNS-Änderungen und verdächtige Record-Änderungen.
      - Halte ein Incident-Playbook für Domain-Hijacking, Zertifikatsfehler oder E-Mail-Spoofing bereit.

**Azure**
=== "EN"

    - Use **Azure DNS** (or equivalent) with RBAC and MFA-protected admin access.
    - For web apps, bind custom domains in **Azure App Service** and use managed certificates or automated renewal.
    - If using **Azure Front Door/Application Gateway**, ensure the custom domain and certificate chain are correctly configured end-to-end.
    - For email providers integrated with Azure workloads, verify required DNS records (SPF/DKIM/DMARC, MX, CNAME/TXT) and monitor DMARC reports.

=== "DE"

    - Nutze **Azure DNS** (oder gleichwertig) mit RBAC und MFA-geschütztem Admin-Zugriff.
    - Binde für Web Apps Custom Domains in **Azure App Service** und nutze Managed Certificates.
    - Wenn **Azure Front Door/Application Gateway** genutzt wird, stelle sicher, dass die Custom Domain und Zertifikatskette End-to-End korrekt sind.
    - Für in Azure integrierte E-Mail-Provider: Überprüfe DNS-Records (SPF/DKIM/DMARC, MX) und überwache DMARC-Reports.

**GitHub**
=== "EN"

    - If using **GitHub Pages** or GitHub-managed domains, verify custom domain ownership and required DNS records.
    - Protect repository and organization settings that can affect domains, environments, or deployment destinations.
    - Keep DNS and domain configuration changes auditable via pull requests/IaC where possible.
    - For CI/CD-generated notifications or release emails, use verified sender domains and avoid untrusted noreply patterns for customer communication.

=== "DE"

    - Bei **GitHub Pages** oder GitHub-managed Domains: Verifiziere den Domainbesitz und erforderliche DNS-Records.
    - Schütze Repository- und Organisationseinstellungen, die Domains oder Deployments betreffen.
    - Halte DNS- und Domainkonfigurationsänderungen über PRs/IaC auditierbar.
    - Nutze für CI/CD-generierte Benachrichtigungen verifizierte Absenderdomains und vermeide untrusted Noreply-Muster.

### DNS+Mail Baseline v1 (operational template)

=== "EN"

    Use this as a starting point and adapt values to your provider and domain model.

    | Record | Example value | Check interval | Owner |
    | :--- | :--- | :--- | :--- |
    | `A` / `AAAA` (`app.example.com`) | `app.example.com -> 203.0.113.10` (or provider-managed target) | Weekly + after infrastructure changes | Platform / Cloud Ops |
    | `CNAME` (`www.example.com`) | `www.example.com -> app.example.com` | Weekly | Platform / Cloud Ops |
    | `CAA` (`example.com`) | `0 issue "letsencrypt.org"` (plus chosen CA) | Monthly | Security + Platform |
    | TLS certificate (`app.example.com`) | Valid chain, auto-renew enabled, min TLS policy enforced | Daily automated expiry check + monthly manual review | Platform / SRE |
    | `MX` (`example.com`) | `10 mx1.mailprovider.com`, `20 mx2.mailprovider.com` | Monthly + after mail provider changes | IT / Messaging |
    | `TXT` SPF (`example.com`) | `v=spf1 include:mailprovider.com -all` | Monthly | IT / Messaging + Security |
    | DKIM selector (`selector1._domainkey.example.com`) | `v=DKIM1; k=rsa; p=...` | Monthly + on key rotation | IT / Messaging |
    | `TXT` DMARC (`_dmarc.example.com`) | `v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@example.com; adkim=s; aspf=s` | Weekly report review + monthly policy review | Security |
    | Sender domain alignment | `From: example.com` aligns with SPF/DKIM domains | Weekly + after sender changes | Security + Messaging |
    | Reverse DNS (sending IPs) | Sending IP PTR matches sending domain/provider requirement | Monthly | Messaging / Email Provider Owner |
    | DNS change audit trail | All DNS changes via PR/IaC with reviewer approval | Continuous (every change) | Platform + Security |
    | External trust check | DMARC aggregate report health, bounce rate, complaint rate, domain reputation trend | Weekly | Security + Support |

    **Recommended acceptance checks before go-live**
    - No certificate expiry warning in the next 30 days.
    - SPF valid (single policy, no `+all`, below DNS lookup limits).
    - DKIM signing active for all production sender domains.
    - DMARC policy active and reports received.
    - Test emails pass SPF/DKIM/DMARC and land in inbox for major providers.
    - Domain and DNS admin accounts are MFA-protected and access-reviewed.

=== "DE"

    Nutze dies als Startpunkt und passe Werte an deinen Provider an.

    | Eintrag | Beispielwert | Prüfintervall | Besitzer |
    | :--- | :--- | :--- | :--- |
    | `A` / `AAAA` (`app.bsp.de`) | `app.bsp.de -> 203.0.113.10` | Wöchentlich + nach Infra-Änderungen | Plattform / Cloud Ops |
    | `CNAME` (`www.bsp.de`) | `www.bsp.de -> app.bsp.de` | Wöchentlich | Plattform / Cloud Ops |
    | `CAA` (`bsp.de`) | `0 issue "letsencrypt.org"` | Monatlich | Security + Plattform |
    | TLS Zertifikat | Gültige Kette, Auto-Renew, min. TLS Policy | Täglicher Auto-Check + monatl. manuell | Plattform / SRE |
    | `MX` (`bsp.de`) | `10 mx1.mailprovider.com` | Monatlich + nach Providerwechsel | IT / Messaging |
    | `TXT` SPF (`bsp.de`) | `v=spf1 include:mailprovider.com -all` | Monatlich | IT / Messaging + Security |
    | DKIM Selektor | `v=DKIM1; k=rsa; p=...` | Monatlich + bei Key-Rotation | IT / Messaging |
    | `TXT` DMARC | `v=DMARC1; p=quarantine; rua=...` | Wöchentlicher Report-Review | Security |
    | Absender-Alignment | `From: bsp.de` passt zu SPF/DKIM | Wöchentlich | Security + Messaging |
    | Reverse DNS (IPs) | Sende-IP PTR passt zu Domain | Monatlich | Messaging / E-Mail Provider |
    | DNS Audit Trail | Alle Änderungen via PR/IaC | Kontinuierlich | Plattform + Security |
    | Externer Vertrauenscheck | DMARC-Report-Gesundheit, Reputation | Wöchentlich | Security + Support |

    **Empfohlene Abnahme-Checks vor Go-Live**
    - Keine Zertifikatsablaufwarnung in den nächsten 30 Tagen.
    - SPF gültig (eine Policy, kein `+all`, unter DNS-Lookup-Limits).
    - DKIM-Signierung für alle Produktions-Sendedomains aktiv.
    - DMARC-Policy aktiv und Reports werden empfangen.
    - Test-E-Mails bestehen SPF/DKIM/DMARC und landen im Posteingang großer Provider.
    - Domain- und DNS-Admin-Konten sind MFA-geschützt und zugriffsgeprüft.

## SDLC

=== "EN"

    Security must be integrated into every stage of the software development process.

=== "DE"

    Sicherheit muss in jede Phase des Softwareentwicklungsprozesses integriert werden.

**General**
=== "EN"

    - **Shift Left**: Integrate security early (requirements, design, code, pull requests), not only at release or in production.
    - **SAST (Static Application Security Testing)**: Analyse source or bytecode for vulnerabilities (injection, hardcoded secrets).
    - **DAST (Dynamic Application Security Testing)**: Test running applications for exploitable issues.
    - **SCA (Software Composition Analysis)**: Scan dependencies for known CVEs and license risks; keep dependencies updated.
    - **Secure CI/CD**: No secrets in repos; use pipeline secrets and environment protection (e.g. approvals for production). Run security scans in the pipeline and block deployment on critical findings when policy requires it.
    - **Branch & commit hygiene**: Branch protection, required reviews, and optionally signed commits for main/production branches.

=== "DE"

    - **Shift Left**: Integriere Sicherheit frühzeitig (Anforderungen, Design, Code, PRs), nicht erst beim Release oder in der Produktion.
    - **SAST (Static Application Security Testing)**: Analysiere Quellcode auf Schwachstellen (Injection, hardcodierte Secrets).
    - **DAST (Dynamic Application Security Testing)**: Teste laufende Anwendungen auf ausnutzbare Probleme.
    - **SCA (Software Composition Analysis)**: Scanne Abhängigkeiten auf bekannte CVEs und Lizenzrisiken; halte Abhängigkeiten aktuell.
    - **Sichere CI/CD**: Keine Secrets in Repos; nutze Pipeline-Secrets und Umgebungsschutz (z. B. Genehmigungen für Produktion). Führe Sicherheitsscans in der Pipeline aus und blockiere das Deployment bei kritischen Funden.
    - **Branch- & Commit-Hygiene**: Branch Protection, erforderliche Reviews und optional signierte Commits für Main-/Produktions-Branches.

**Azure**
=== "EN"

    - Use **Microsoft Defender for Cloud** and **Defender for DevOps** (where available) for posture and pipeline integration; act on recommendations for Azure resources and repos.

=== "DE"

    - Nutze **Microsoft Defender for Cloud** und **Defender for DevOps** (wo verfügbar) für Sicherheitslage und Pipeline-Integration; reagiere auf Empfehlungen für Azure-Ressourcen und Repos.

**GitHub**
=== "EN"

    - **Branch protection rules**: Require pull request reviews, status checks, and optionally signed commits before merging to default/protected branches.
    - **CodeQL** (GitHub Advanced Security): Enable for SAST. Run in Actions and fail or warn on policy-defined findings.
    - **Dependabot**: Enable version updates and security updates; enable **Dependency graph** and **Dependabot alerts**.
    - **Secret leak detection**
      - Enable **GitHub Secret Scanning** and **Push Protection** (where available) to block leaked credentials before they land in the repository.
      - Add one additional scanner in CI for defence in depth (e.g. **Gitleaks** or **TruffleHog**) and fail the build on verified secrets.
    - **Additional GitHub-integrated analysis tools (examples)**
      - **Semgrep**: rules-based SAST in GitHub Actions.
      - **SonarCloud**: code quality and security hotspots integrated with PR checks.
      - **Snyk**: SCA and container scanning integrated with GitHub PR feedback.
      - **Checkov**: IaC security scanning for Terraform/Bicep/CloudFormation in Actions.
    - **Environments**: Use for staging/production with protection rules and required reviewers so only approved workflows deploy.

=== "DE"

    - **Branch Protection Rules**: Fordere PR-Reviews, Statusprüfungen und optional signierte Commits vor dem Merge an.
    - **CodeQL** (GitHub Advanced Security): Aktiviere für SAST. Führe in Actions aus und warne oder blockiere bei richtlinienrelevanten Funden.
    - **Dependabot**: Aktiviere Versions- und Sicherheitsupdates; aktiviere **Dependency Graph** und **Dependabot Alerts**.
    - **Secret Leak Detection**
      - Aktiviere **GitHub Secret Scanning** und **Push Protection**, um geleakte Credentials zu blockieren, bevor sie im Repository landen.
      - Füge einen zusätzlichen Scanner in CI für Defense in Depth hinzu (z. B. **Gitleaks** oder **TruffleHog**) und lasse den Build bei verifizierten Secrets fehlschlagen.
    - **Zusätzliche GitHub-integrierte Analysetools (Beispiele)**
      - **Semgrep**: Regelbasiertes SAST in GitHub Actions.
      - **SonarCloud**: Codequalität und Sicherheits-Hotspots integriert in PR-Checks.
      - **Snyk**: SCA und Container-Scanning integriert in GitHub-PR-Feedback.
      - **Checkov**: IaC-Sicherheitsscanning für Terraform/Bicep/CloudFormation in Actions.
      - **Umgebungen (Environments)**: Nutze sie für Staging/Produktion mit Schutzregeln und erforderlichen Reviewern, damit nur genehmigte Workflows deployen.

## Testing

=== "EN"

    Comprehensive testing ensures reliability and prevents regressions before release.

=== "DE"

    Umfassendes Testen sichert Zuverlässigkeit und verhindert Regressionen vor dem Release.

**General**
=== "EN"

    - **Unit tests**: Cover critical business logic, edge cases, and error handling; run on every change.
    - **Integration tests**: Verify components and external services (APIs, databases, queues) work together; use test doubles where appropriate.
    - **End-to-end (e2e) tests**: Validate critical user flows in an environment close to production.
    - **Regression tests**: Every production bug should result in a test that prevents recurrence.
    - **Property-based tests** (where useful): Validate invariants across many generated inputs (e.g. parser rules, data transformation invariants).
    - **Fuzzing**: Feed unexpected/random input to parsers, API endpoints, and protocol handlers to detect crashes, hangs, and unsafe behavior early.
    - **Security testing**: Include SAST/SCA in the pipeline; add DAST or penetration tests for high-risk or public-facing apps.
    - **Test quality practices**
      - Keep tests deterministic and isolated (avoid flaky timing/network dependencies).
      - Use meaningful assertions and test names that explain expected behavior.
      - Define minimum expectations per layer (unit/integration/e2e) and review gaps regularly.
    - Define a clear test strategy (what runs when, who maintains tests) and require passing tests before merge or release.

=== "DE"

    - **Unit-Tests**: Abdeckung von kritischer Geschäftslogik, Randfällen und Fehlerbehandlung; Ausführung bei jeder Änderung.
    - **Integrationstests**: Verifizierung, dass Komponenten und externe Dienste (APIs, DBs, Queues) zusammenarbeiten.
    - **End-to-End (E2E) Tests**: Validierung kritischer Benutzerabläufe in einer produktionsnahen Umgebung.
    - **Regressionstests**: Jeder Produktionsbug sollte zu einem Test führen, der das erneute Auftreten verhindert.
    - **Property-Based Tests** (wo sinnvoll): Validierung von Invarianten über viele generierte Eingaben (z. B. Parser-Regeln).
    - **Fuzzing**: Füttern von Parsern/APIs mit unerwarteten/zufälligen Eingaben, um Crashes oder unsicheres Verhalten früh zu erkennen.
    - **Sicherheitstests**: SAST/SCA in der Pipeline; DAST oder Penetrationstests für hochriskante/öffentliche Apps.
    - **Testqualitäts-Praktiken**
      - Halte Tests deterministisch und isoliert (vermeide instabile Timing/Netzwerk-Abhängigkeiten - „Flaky Tests“).
      - Nutze aussagekräftige Assertions und Testnamen, die das erwartete Verhalten erklären.
      - Definiere Mindesterwartungen pro Ebene (Unit/Integration/E2E) und überprüfe Lücken regelmäßig.
    - Definiere eine klare Teststrategie (was läuft wann, wer wartet Tests) und fordere bestandene Tests vor Merge oder Release.

**Azure**
=== "EN"

    - Run tests in **CI** before deployment. Use **staging slots** (e.g. App Service deployment slots) to validate releases before swapping to production; run smoke or e2e tests against the staging slot.
    - Use **Azure Monitor** and **Application Insights** to observe test and production behaviour and catch regressions.

=== "DE"

    - Führe Tests in **CI** vor dem Deployment aus. Nutze **Staging Slots** (z. B. App Service Deployment Slots), um Releases zu validieren, bevor auf Produktion gewechselt wird (Swap); führe Smoke- oder E2E-Tests gegen den Slot aus.
    - Nutze **Azure Monitor** und **Application Insights**, um Test- und Produktionsverhalten zu beobachten und Regressionen zu finden.

**GitHub**
=== "EN"

    - **GitHub Actions**: Run unit, integration, and e2e tests in workflows; attach test results (e.g. JUnit XML) for visibility.
    - Use **branch protection** to require that status checks (including test jobs) pass before merging. Use **matrix builds** to test across relevant runtimes or environments.
    - Add dedicated jobs for **fuzzing** and longer-running security/integration tests on schedule (e.g. nightly) if they are too heavy for every PR.
    - Publish test artifacts and reports (coverage, flaky-test report, fuzzing findings) so trends are visible over time.

=== "DE"

    - **GitHub Actions**: Führe Unit-, Integrations- und E2E-Tests in Workflows aus; hänge Testergebnisse (z. B. JUnit XML) für Sichtbarkeit an.
    - Nutze **Branch Protection**, um das Bestehen von Statusprüfungen (inkl. Test-Jobs) vor dem Merge zu erzwingen.
    - Füge dedizierte Jobs für **Fuzzing** und länger laufende Security/Integration-Tests per Zeitplan (z. B. nächtlich) hinzu, wenn sie für jeden PR zu schwergewichtig sind.
    - Veröffentliche Testartefakte und Berichte (Coverage, Flaky-Test-Report), um Trends sichtbar zu machen.

## Staging

=== "EN"

    A production-like environment validates releases and reduces deployment risks.

    A **staging** environment is a copy of (or as close as possible to) production used to validate releases before they reach users. Keep the promotion path simple: build → deploy to staging → validate → promote to production.

=== "DE"

    Eine produktionsnahe Umgebung validiert Releases und reduziert Deployment-Risiken.

    Eine **Staging**-Umgebung ist eine Kopie (oder so nah wie möglich an) der Produktion, um Releases zu validieren, bevor sie die Nutzer erreichen. Halte den Promotion-Pfad einfach: Build → Deploy auf Staging → Validieren → Promote auf Produktion.

**General**
=== "EN"

    - **Purpose**: Staging is where you run smoke tests, e2e tests, and manual checks against a production-like setup. It reduces the risk of broken or insecure releases reaching production.
    - **Promotion flow**: Deploy the same artifact (or same commit) to staging first; only after validation (automated and/or manual) promote to production. Avoid “building twice” or different code paths for staging vs production.
    - **Data**: Do not use production data in staging. Use anonymised or synthetic data; if you copy production data, follow a strict process and ensure it is not exposed (e.g. different URLs, access control). Document how staging data is created and refreshed.
    - **Configuration**: Staging should mirror production in structure (same services, same topology) but use separate config (URLs, keys, feature flags) so staging never affects production resources or users.
    - **Keep it simple**: One staging environment is often enough. Add more (e.g. dev, QA, preprod) only if the team and release cadence justify it; each extra environment adds cost and drift risk.

=== "DE"

    - **Zweck**: Im Staging laufen Smoke-Tests, E2E-Tests und manuelle Checks gegen ein produktionsnahes Setup. Es reduziert das Risiko, kaputte oder unsichere Releases in die Produktion zu bringen.
    - **Promotion-Flow**: Deploye dasselbe Artefakt (oder denselben Commit) zuerst auf Staging; erst nach Validierung (automatisiert und/oder manuell) promote es auf Produktion. Vermeide „zweimal bauen“ oder unterschiedliche Codepfade für Staging vs. Produktion.
    - **Daten**: Nutze keine Produktionsdaten im Staging. Verwende anonymisierte oder synthetische Daten; wenn du Produktionsdaten kopierst, befolge einen strikten Prozess und sorge dafür, dass sie nicht exponiert sind (z. B. andere URLs, Zugriffskontrolle). Dokumentiere, wie Staging-Daten erstellt und aktualisiert werden.
    - **Konfiguration**: Staging sollte die Produktionsstruktur spiegeln (gleiche Dienste, gleiche Topologie), aber separate Konfigurationen nutzen (URLs, Keys, Feature Flags), damit Staging niemals Produktionsressourcen oder -nutzer beeinflusst.
    - **Keep it simple**: Eine Staging-Umgebung reicht oft aus. Füge mehr hinzu (z. B. Dev, QA, Preprod), nur wenn das Team und der Release-Takt es rechtfertigen; jede extra Umgebung erhöht Kosten und Drift-Risiko.

**Azure**
=== "EN"

    - **Deployment slots**: For **Azure Web Apps**, use **deployment slots** (e.g. “staging”) for blue-green or staged rollout. Deploy to the staging slot, run smoke/e2e tests, then **swap** to production. Slots share the same app but can have different app settings (e.g. connection strings to a staging database).
    - **Separate staging app**: For more isolation or when slots are not enough, use a separate **App Service** (or resource group) for staging with its own config and data stores. Use the same IaC and pipeline so staging and production stay aligned.
    - **Environments**: Treat “Staging” and “Production” as distinct in your pipeline (e.g. different Azure targets, different approval gates).

=== "DE"

    - **Deployment Slots**: Für **Azure Web Apps** nutze **Deployment Slots** (z. B. „Staging“) für Blue-Green- oder gestaffelte Rollouts. Deploye auf den Staging-Slot, führe Smoke/E2E-Tests aus, dann **Swap** auf Produktion. Slots teilen dieselbe App, können aber unterschiedliche Einstellungen haben (z. B. Connection Strings zu einer Staging-DB).
    - **Separate Staging-App**: Für mehr Isolation oder wenn Slots nicht reichen, nutze einen separaten **App Service** (oder Ressourcengruppe) mit eigener Config und Datenspeichern. Nutze dasselbe IaC und Pipeline, damit Staging und Produktion synchron bleiben.
    - **Umgebungen**: Behandle „Staging“ und „Produktion“ als getrennt in deiner Pipeline (z. B. unterschiedliche Azure-Ziele, unterschiedliche Approval-Gates).

**GitHub**
=== "EN"

    - **Environments**: Use GitHub **Environments** (e.g. “Staging”, “Production”) so deployments are tracked and protection rules (e.g. required reviewers for Production) apply. Deploy to Staging first; require manual approval or automated checks before deploying to Production.
    - **Branch strategy**: Tie environments to a simple branch model so the path from commit to production is auditable (e.g. trunk-based: `main` -> Staging, release tag -> Production; or GitFlow with a protected `release/*` path).
    - **Branch security best practices**
      - Protect `main` and release branches: required PR reviews, required status checks, no direct pushes, no force pushes, and no branch deletion.
      - Require green checks for tests, SAST, SCA, and secret scanning before merge.
      - Use CODEOWNERS for critical paths (security, infra, deployment workflows) so the right reviewers are always included.
      - Restrict who can trigger production deployments and require environment approvals.

=== "DE"

    - **Environments**: Nutze GitHub **Environments** (z. B. „Staging“, „Production“), damit Deployments getrackt werden und Schutzregeln (z. B. erforderliche Reviewer für Produktion) greifen. Deploye zuerst auf Staging; fordere manuelle Genehmigung oder automatisierte Checks vor dem Deployment auf Produktion.
    - **Branch-Strategie**: Verknüpfe Umgebungen mit einem einfachen Branch-Modell, damit der Pfad vom Commit zur Produktion auditierbar ist (z. B. Trunk-Based: `main` -> Staging, Release-Tag -> Produktion; oder GitFlow mit geschütztem `release/*`-Pfad).
    - **Branch-Sicherheit Best Practices**
      - Schütze `main`- und Release-Branches: erforderliche PR-Reviews, Statusprüfungen, keine direkten Pushes, keine Force Pushes, kein Löschen von Branches.
      - Erfordere grüne Checks für Tests, SAST, SCA und Secret Scanning vor dem Merge.
      - Nutze CODEOWNERS für kritische Pfade (Sicherheit, Infra, Deployment-Workflows), damit immer die richtigen Reviewer dabei sind.
      - Beschränke, wer Produktions-Deployments auslösen kann, und fordere Environment-Approvals.

## Open Source

=== "EN"

    Safe usage of open source requires license compliance and vulnerability management.

=== "DE"

    Die sichere Nutzung von Open Source erfordert Lizenz-Compliance und Schwachstellenmanagement.

**General**
=== "EN"

    - **License compliance**: Know the licenses of all dependencies (including transitive); ensure they are compatible with your use and distribution (e.g. GPL, MIT, Apache).
    - **Software Bill of Materials (SBOM)**: Generate and maintain an SBOM for audit and vulnerability management; align with SCA and dependency scanning.
    - **Vulnerability handling**: Track and patch known vulnerabilities in dependencies; have a process for evaluating and disclosing issues in your own code (e.g. security advisories).
    - **Contributing**: If you use or contribute to open source, follow the project’s contribution guidelines and license terms; document your own policy for accepting or releasing OSS.

=== "DE"

    - **Lizenz-Compliance**: Kenne die Lizenzen aller Abhängigkeiten (inkl. transitiver); stelle sicher, dass sie mit deiner Nutzung und Distribution kompatibel sind (z. B. GPL, MIT, Apache).
    - **Software Bill of Materials (SBOM)**: Generiere und pflege eine Stückliste (SBOM) für Audits und Schwachstellenmanagement; stimme dies mit SCA und Dependency Scanning ab.
    - **Schwachstellen-Management**: Tracke und patche bekannte Sicherheitslücken in Abhängigkeiten; habe einen Prozess für die Bewertung und Offenlegung eigener Code-Probleme (z. B. Security Advisories).
    - **Beitragen**: Wenn du Open Source nutzt oder dazu beiträgst, befolge die Richtlinien und Lizenzbedingungen des Projekts; dokumentiere deine eigene Policy für die Freigabe von OSS.

**Azure**
=== "EN"

    - Azure services and SDKs have their own licenses; when you ship software that depends on them, document and comply with those terms. Use **Defender for Cloud** and dependency scanning to stay aware of issues in OSS you use.

=== "DE"

    - Azure-Dienste und SDKs haben eigene Lizenzen; wenn du Software auslieferst, die davon abhängt, dokumentiere und befolge diese Bedingungen. Nutze **Defender for Cloud** und Dependency Scanning, um über Probleme in genutztem OSS informiert zu bleiben.

**GitHub**
=== "EN"

    - Add a **LICENSE** file to your repository so others know the terms. Use **Dependabot** and **Dependency graph** for visibility and alerts on dependencies.
    - Document **contributing guidelines** (e.g. CONTRIBUTING.md) and, if you accept contributions, use a **Contributor License Agreement (CLA)** or equivalent if required by your organisation.
    - Use **GitHub Security Advisories** to disclose and manage vulnerabilities in your own projects; link to your security policy (e.g. SECURITY.md).

=== "DE"

    - Füge eine **LICENSE**-Datei zu deinem Repository hinzu. Nutze **Dependabot** und **Dependency Graph** für Sichtbarkeit und Warnungen zu Abhängigkeiten.
    - Dokumentiere **Richtlinien für Mitwirkende** (z. B. CONTRIBUTING.md) und nutze ggf. ein **Contributor License Agreement (CLA)**.
    - Nutze **GitHub Security Advisories**, um Sicherheitslücken in eigenen Projekten offenzulegen und zu verwalten; verlinke auf deine Security-Policy (z. B. SECURITY.md).

## Communication

=== "EN"

    Transparent communication builds trust with users and stakeholders.

=== "DE"

    Transparente Kommunikation baut Vertrauen bei Nutzern und Stakeholdern auf.

**General**
=== "EN"

    - **Changelogs**: Maintain a machine- or human-readable changelog (e.g. CHANGELOG.md) with notable changes per version. Use a consistent format (e.g. Keep a Changelog) and **semantic versioning** where it fits (major.minor.patch).
    - **Release notes**: Publish clear release notes for users or stakeholders: what changed, what to do (e.g. upgrade steps, breaking changes), and where to get help.
    - **Clear communication**: Communicate proactively about security updates, incidents, and maintenance: what happened, impact, and what you are doing. Document processes for incident communication and user/stakeholder updates.

=== "DE"

    - **Changelogs**: Pflege ein maschinen- oder menschenlesbares Änderungsprotokoll (z. B. CHANGELOG.md) mit nennenswerten Änderungen pro Version. Nutze ein konsistentes Format (z. B. „Keep a Changelog“) und **Semantic Versioning** (Major.Minor.Patch).
    - **Release Notes**: Veröffentliche klare Release-Notizen für Nutzer: was sich geändert hat, was zu tun ist (z. B. Upgrade-Schritte, Breaking Changes) und wo es Hilfe gibt.
    - **Klare Kommunikation**: Kommuniziere proaktiv über Sicherheitsupdates, Vorfälle und Wartung: was passiert ist, die Auswirkungen und was unternommen wird.

**Azure**
=== "EN"

    - Document infrastructure and configuration changes (e.g. in runbooks or ADR); when you change Azure resources that affect users, include that in release or operations communication.

=== "DE"

    - Dokumentiere Infrastruktur- und Konfigurationsänderungen (z. B. in Runbooks oder ADRs); wenn du Azure-Ressourcen änderst, die Nutzer betreffen, kommuniziere dies.

**GitHub**
=== "EN"

    - Use **Releases** to publish versioned artifacts and attach release notes; link or paste changelog content there.
    - Keep **CHANGELOG.md** (or equivalent) in the repo and update it as part of the release process.
    - Use **GitHub Security Advisories** and a **SECURITY.md** policy to communicate how to report vulnerabilities and how you respond.

=== "DE"

    - Nutze **Releases**, um versionierte Artefakte zu veröffentlichen und Release Notes anzuhängen.
    - Halte **CHANGELOG.md** im Repo aktuell und aktualisiere es als Teil des Release-Prozesses.
    - Nutze **GitHub Security Advisories** und eine **SECURITY.md**-Policy, um zu kommunizieren, wie man Schwachstellen meldet und wie reagiert wird.

## Operations

=== "EN"

    Observability and defined incident processes ensure system availability and rapid recovery.

=== "DE"

    Beobachtbarkeit und definierte Vorfallprozesse sichern Systemverfügbarkeit und schnelle Wiederherstellung.

**General**
=== "EN"

    - **Observability**: Collect metrics, logs, and traces so you can detect failures, performance issues, and security events.
    - **Alerting**: Define alerts for availability, errors, authentication failures, and anomalies; route them to the right people and runbooks.
    - **Incident response**: Document how to respond to incidents (who does what, escalation); retain logs and evidence for post-incident review and compliance.

=== "DE"

    - **Observability**: Sammle Metriken, Logs und Traces, um Ausfälle, Performance-Probleme und Sicherheitsvorfälle zu erkennen.
    - **Alerting**: Definiere Alarme für Verfügbarkeit, Fehler, Authentifizierungsfehler und Anomalien; route sie zu den richtigen Personen und Runbooks.
    - **Incident Response**: Dokumentiere, wie auf Vorfälle reagiert wird (wer macht was, Eskalation); bewahre Logs und Beweise für Post-Incident-Review und Compliance auf.

**Azure**
=== "EN"

    - **Azure Monitor**: Central place for metrics and logs; set up alerts for availability, errors, and security-relevant events.
    - **Application Insights**: Use for application performance and dependency tracking; correlate with security events where useful.
    - **Log Analytics**: Query and retain logs for incident response and compliance; integrate with Defender for Cloud where applicable.
    - **Microsoft Defender for Cloud (formerly Security Center)**: Use for security posture, recommendations, threat detection, and regulatory compliance views; enable plans for relevant resource types.
    - **Act on recommendations**: define ownership/SLA for Defender recommendations (e.g. critical in days, high in weeks) and track exceptions with documented risk acceptance.
    - **Alerting strategy**: configure alerts for authentication failures, WAF blocks/spikes, firewall denies, deployment failures, unusual geographies, and impossible travel patterns.
    - **Audit trail**: keep Azure Activity Log, resource diagnostic logs, and access logs retained according to policy; ensure logs are tamper-resistant and searchable.
    - **Policy and audit checks**: use Azure Policy + initiatives to continuously audit standards (e.g. no public storage, required tags, private endpoints, TLS minimums), and review drift regularly.

=== "DE"

    - **Azure Monitor**: Zentraler Ort für Metriken und Logs; richte Alerts für Verfügbarkeit, Fehler und Sicherheitsereignisse ein.
    - **Application Insights**: Für Anwendungsperformance und Dependency-Tracking; korreliere mit Sicherheitsereignissen, wo sinnvoll.
    - **Log Analytics**: Abfrage und Aufbewahrung von Logs für Incident Response und Compliance; integriere mit Defender for Cloud.
    - **Microsoft Defender for Cloud**: Für Sicherheitslage, Empfehlungen, Bedrohungserkennung und regulatorische Compliance-Ansichten.
    - **Handle nach Empfehlungen**: Definiere Ownership/SLA für Defender-Empfehlungen (z. B. kritisch in Tagen, hoch in Wochen) und verfolge Ausnahmen mit dokumentierter Risikoakzeptanz.
    - **Alerting-Strategie**: Konfiguriere Alarme für Auth-Fehler, WAF-Blocks/Spikes, Firewall-Denies, Deployment-Fehler, ungewöhnliche Geografien und unmögliche Reisemuster.
    - **Audit Trail**: Bewahre Azure Activity Log, Ressourcen-Diagnoselogs und Access Logs richtlinienkonform auf; stelle sicher, dass sie manipulationssicher und durchsuchbar sind.
    - **Policy & Audit Checks**: Nutze Azure Policy + Initiativen, um Standards kontinuierlich zu prüfen (z. B. kein öffentlicher Storage, erforderliche Tags, private Endpoints), und überprüfe Drift regelmäßig.

**GitHub**
=== "EN"

    - Use **Actions** status and **Deployments** to see pipeline and deployment outcomes; configure notifications (e.g. Slack, email) for failures.
    - **GitHub Advanced Security** (CodeQL, Dependabot, secret scanning): Review and act on alerts; integrate with your incident or security process where needed.

=== "DE"

    - Nutze **Actions**-Status und **Deployments**, um Pipeline- und Deployment-Ergebnisse zu sehen; konfiguriere Benachrichtigungen (z. B. Slack, E-Mail) für Fehler.
    - **GitHub Advanced Security** (CodeQL, Dependabot, Secret Scanning): Überprüfe und reagiere auf Warnungen; integriere sie bei Bedarf in deinen Incident- oder Sicherheitsprozess.

## Deployment

=== "EN"

    Automated, secure pipelines ensure consistent and reliable software delivery.

=== "DE"

    Automatisierte, sichere Pipelines gewährleisten konsistente und zuverlässige Softwareauslieferung.

**General**
=== "EN"

    - Never store deployment credentials in the repository; use a secrets store or pipeline secrets.
    - Protect production: use environment restrictions, required approvals, and only deploy after tests and security checks pass.
    - Run SAST, SCA, and (where applicable) container or DAST checks in the pipeline; block or gate deployment on policy-defined findings.
    - Document deployment steps and rollback procedures.

=== "DE"

    - Speichere niemals Deployment-Credentials im Repository; nutze einen Secrets-Store oder Pipeline-Secrets.
    - Schütze die Produktion: Nutze Umgebungseinschränkungen, erforderliche Genehmigungen und deploye nur nach bestandenen Tests und Sicherheitschecks.
    - Führe SAST, SCA und (wo anwendbar) Container- oder DAST-Checks in der Pipeline aus; blockiere Deployments bei kritischen Funden.
    - Dokumentiere Deployment-Schritte und Rollback-Prozeduren.

**Azure**
=== "EN"

    - Deploy to **Azure Web Apps**, **Functions**, or other targets via CI/CD; use **deployment slots** for blue-green or staged rollouts. Use **managed identities** and **Key Vault** so the pipeline and app do not rely on stored passwords.

=== "DE"

    - Deploye auf **Azure Web Apps**, **Functions** oder andere Ziele via CI/CD; nutze **Deployment Slots** für Blue-Green- oder gestaffelte Rollouts. Nutze **Managed Identities** und **Key Vault**, damit Pipeline und App keine gespeicherten Passwörter benötigen.

**GitHub**
=== "EN"

    - **GitHub Secrets**: Store Azure credentials (e.g. service principal) or use **OIDC** with Azure AD so Actions assume a role without long-lived secrets. Use secrets only in workflows, never in repo content.
    - **Environments**: Use (e.g. “Staging”, “Production”) with protection rules and required reviewers before deployment.
    - **Pipeline security gates**: Run tests, **CodeQL**, **Dependabot** checks, secret scanning, and optional container/IaC scans in GitHub Actions; use required status checks so only reviewed, passing builds deploy.
    - **Deployment best practices**
      - Build once, deploy the same artifact to Staging and then Production (avoid rebuilding between environments).
      - Use immutable versioning (commit SHA/tag) and keep release notes linked to that version.
      - Keep rollback simple: defined rollback workflow, known previous-good artifact, and clear ownership.
      - Keep production deployment rights minimal and auditable.

=== "DE"

    - **GitHub Secrets**: Speichere Azure-Credentials (z. B. Service Principal) oder nutze **OIDC** mit Azure AD, damit Actions eine Rolle ohne langlebige Secrets annehmen. Nutze Secrets nur in Workflows, nie im Repo-Inhalt.
    - **Environments**: Nutze sie (z. B. „Staging“, „Production“) mit Schutzregeln und erforderlichen Reviewern vor dem Deployment.
    - **Pipeline Security Gates**: Führe Tests, **CodeQL**, **Dependabot**-Checks, Secret Scanning und optionale Container/IaC-Scans in Actions aus; nutze erforderliche Statuschecks, damit nur genehmigte, bestandene Builds deployen.
    - **Deployment Best Practices**
      - Einmal bauen, dasselbe Artefakt auf Staging und dann Produktion deployen (vermeide Rebuilds zwischen Umgebungen).
      - Nutze unveränderliche Versionierung (Commit SHA/Tag) und verlinke Release Notes damit.
      - Halte Rollbacks einfach: definierter Rollback-Workflow, bekanntes funktionierendes Artefakt und klare Verantwortung.
      - Halte Produktions-Deployment-Rechte minimal und auditierbar.

## IaC & Config

=== "EN"

    Infrastructure defined as code ensures reproducibility and auditability.

    Define infrastructure and server configuration in version-controlled, reviewable code so changes are repeatable, auditable, and consistent. Keep it simple: use a small set of tools and patterns that the team can maintain.

=== "DE"

    Als Code definierte Infrastruktur sichert Wiederholbarkeit und Auditierbarkeit.

    Definiere Infrastruktur und Serverkonfiguration in versioniertem, reviewbarem Code, damit Änderungen wiederholbar, auditierbar und konsistent sind. Halte es einfach: Nutze ein kleines Set an Tools und Mustern, die das Team warten kann.

**General**
=== "EN"

    - **Infrastructure as Code (IaC)**: Describe servers, networks, databases, and other infrastructure in declarative or scripted definitions (e.g. Terraform, Pulumi, CloudFormation, ARM, Bicep). Store them in version control; run them via CI/CD so every change is reviewed and logged. Avoid one-off manual changes; treat “clicking in the portal” as the exception, not the rule.
    - **System configuration (cookbooks / config management)**: For OS and application configuration on VMs or containers (e.g. installed packages, config files, users), use **configuration as code**: scripts, playbooks, or cookbooks (e.g. Ansible, Chef, Puppet, or versioned scripts). Idempotency and clear ordering reduce drift and make rollbacks predictable. Document the relationship between IaC (what is provisioned) and config management (how it is configured).
    - **Single source of truth**: Keep infrastructure and config definitions in one place (e.g. one repo or a clear split). Avoid duplicating the same resource in multiple tools or manual runbooks that contradict the code.
    - **Review and test**: Apply the same quality bar as application code: peer review, linting, and where possible automated checks (e.g. plan/diff before apply). Use separate staging or sandbox subscriptions/folders to test IaC changes before production.
    - **Secrets and parameters**: Never hardcode secrets in IaC or cookbooks. Use parameters, environment variables, or a secrets store (e.g. Key Vault) and reference them at apply/runtime.

=== "DE"

    - **Infrastructure as Code (IaC)**: Beschreibe Server, Netzwerke, Datenbanken und andere Infrastruktur deklarativ (z. B. Terraform, Pulumi, Bicep). Speichere sie in der Versionsverwaltung; führe sie über CI/CD aus, damit jede Änderung geprüft und protokolliert wird. Vermeide manuelle Änderungen; betrachte „Klicken im Portal“ als Ausnahme, nicht die Regel.
    - **Systemkonfiguration**: Für OS- und Anwendungskonfiguration auf VMs oder Containern nutze **Configuration as Code**: Skripte, Playbooks oder Cookbooks (z. B. Ansible, Chef, Puppet). Idempotenz und klare Reihenfolge reduzieren Drift und machen Rollbacks vorhersehbar.
    - **Single Source of Truth**: Halte Infrastruktur- und Konfigurationsdefinitionen an einem Ort (z. B. ein Repo). Vermeide Duplizierung derselben Ressource in mehreren Tools oder manuellen Runbooks.
    - **Review und Test**: Wende denselben Qualitätsstandard an wie bei Anwendungscode: Peer Review, Linting und automatisierte Checks (Plan/Diff vor Apply). Nutze separate Staging- oder Sandbox-Subscriptions, um IaC-Änderungen zu testen.
    - **Secrets und Parameter**: Hardcode niemals Secrets in IaC. Nutze Parameter, Umgebungsvariablen oder einen Secrets-Store (z. B. Key Vault) und referenziere sie zur Laufzeit.

**Azure**
=== "EN"

    - **IaC**: Use **Bicep** or **ARM** (Azure native) or **Terraform** (multi-cloud or team preference) to define resource groups, Web Apps, databases, networking, and RBAC. Store definitions in version control; run `bicep build` / `terraform plan` and `apply` from the pipeline with a secure state backend (e.g. Azure Storage with locking).
    - **Configuration**: For VMs, use **Azure Desired State Configuration (DSC)**, **Custom Script Extension**, or Ansible/Chef/Puppet from a pipeline. For PaaS (App Service, Functions), keep config in **App Configuration** or **Key Vault** and set app settings via IaC or pipeline so changes are traceable.
    - **Policies**: Use **Azure Policy** (defined as code) to enforce organisational rules (e.g. allowed regions, required tags, no public storage). Keep policy definitions in the same repo as other IaC.

=== "DE"

    - **IaC**: Nutze **Bicep** oder **ARM** (Azure Native) oder **Terraform** (Multi-Cloud), um Ressourcengruppen, Web Apps, Datenbanken, Networking und RBAC zu definieren. Speichere Definitionen in Versionsverwaltung; führe `build`/`plan`/`apply` aus der Pipeline mit sicherem State-Backend (z. B. Azure Storage mit Locking) aus.
    - **Konfiguration**: Für VMs nutze **Azure DSC**, **Custom Script Extension** oder Ansible/Chef aus einer Pipeline. Für PaaS (App Service, Functions) halte Config in **App Configuration** oder **Key Vault** und setze App Settings via IaC, damit Änderungen nachvollziehbar sind.
    - **Policies**: Nutze **Azure Policy** (als Code definiert), um Organisationsregeln durchzusetzen (z. B. erlaubte Regionen, erforderliche Tags). Halte Policy-Definitionen im selben Repo wie andere IaC.

**GitHub**
=== "EN"

    - **Store IaC and config in the repo**: Keep Bicep, Terraform, or Ansible playbooks in the repository (e.g. `/infra`, `/terraform`, `/ansible`). Use **branch protection** and required reviews so infrastructure changes go through the same process as code.
    - **Run from Actions**: Use GitHub Actions to run `terraform plan` on PR and `apply` on merge (or to a specific environment). Store **remote state** in Azure Storage or another backend; use OIDC or stored credentials in GitHub Secrets with minimal scope. Never commit state files or secrets.
    - **Documentation**: Document how to run IaC and config locally or in CI (e.g. README in the infra folder, required env vars, and how to request access to state).

=== "DE"

    - **IaC und Config im Repo speichern**: Halte Bicep, Terraform oder Ansible-Playbooks im Repository (z. B. `/infra`). Nutze **Branch Protection** und erforderliche Reviews, damit Infrastrukturänderungen denselben Prozess durchlaufen wie Code.
    - **Ausführung über Actions**: Nutze GitHub Actions, um `terraform plan` bei PR und `apply` bei Merge auszuführen. Speichere **Remote State** sicher; nutze OIDC für Zugriff. Committe niemals State-Files oder Secrets.
    - **Dokumentation**: Dokumentiere, wie IaC lokal oder in CI ausgeführt wird (z. B. README im Infra-Ordner).

## Documentation

=== "EN"

    Clear documentation reduces risk and speeds up onboarding and compliance.

    Good documentation reduces risk, speeds onboarding, and supports compliance. Document what matters for operating, securing, and changing the system; keep it up to date and in one place.

=== "DE"

    Klare Dokumentation reduziert Risiken und beschleunigt Onboarding sowie Compliance.

    Gute Dokumentation reduziert Risiken, beschleunigt das Onboarding und unterstützt Compliance. Dokumentiere, was für Betrieb, Sicherheit und Änderung des Systems wichtig ist.

**General**
=== "EN"

    - **What to document**: **Architecture** (components, data flow, boundaries); **APIs** (contracts, auth, examples); **Operations** (deployment, rollback, scaling, backups); **Runbooks** (incident response, common tasks); **Decisions** (ADRs — why we chose X); **Security** (threat model, secrets handling, compliance). Prioritise what the team and auditors actually use.
    - **Single source of truth**: Prefer one canonical place (e.g. docs in the repo, or a linked docs site) so information does not scatter across wikis, slides, and chat. Link from code or config to docs where it helps (e.g. README in each service).
    - **Keep it current**: Outdated docs are worse than none. Treat documentation as part of the product: update it when you change behaviour, and add “update docs” to the definition of done for features and infra changes.
    - **Format and structure**: Use a consistent format (e.g. Markdown) and a simple structure (README, docs folder, or docs-as-code with a static generator). Use clear headings, lists, and code snippets; avoid long prose where a table or diagram is clearer. Keep it simple so contributors know where to add or change content.
    - **Onboarding**: New team members (and auditors) should find how to get access, run the app locally, run tests, and understand the high-level architecture without hunting. A single “Getting started” or “README” that stays accurate is valuable.

=== "DE"

    - **Was zu dokumentieren ist**: **Architektur** (Komponenten, Datenfluss, Grenzen); **APIs** (Verträge, Auth, Beispiele); **Betrieb** (Deployment, Rollback, Skalierung, Backups); **Runbooks** (Incident Response, häufige Aufgaben); **Entscheidungen** (ADRs — warum wir X gewählt haben); **Sicherheit** (Bedrohungsmodell, Secrets-Handling, Compliance). Priorisiere, was das Team und Prüfer tatsächlich nutzen.
    - **Single Source of Truth**: Bevorzuge einen kanonischen Ort (z. B. Docs im Repo oder eine verlinkte Doku-Site), damit Informationen nicht über Wikis, Folien und Chats verstreut sind.
    - **Aktuell halten**: Veraltete Doku ist schlimmer als keine. Behandle Dokumentation als Teil des Produkts: Aktualisiere sie, wenn du Verhalten änderst, und füge „Update Docs“ zur Definition of Done hinzu.
    - **Format und Struktur**: Nutze ein konsistentes Format (z. B. Markdown) und eine einfache Struktur (README, Docs-Ordner oder Docs-as-Code). Nutze klare Überschriften, Listen und Code-Snippets; vermeide lange Prosa, wo eine Tabelle oder ein Diagramm klarer ist.
    - **Onboarding**: Neue Teammitglieder (und Auditoren) sollten finden, wie sie Zugriff erhalten, die App lokal ausführen und die High-Level-Architektur verstehen können, ohne zu suchen. Ein einziges „Getting Started“ oder „README“, das korrekt ist, ist wertvoll.

**Azure**
=== "EN"

    - Document **resource layout** (subscriptions, resource groups, naming), **networking** (VNet, subnets, private endpoints), and **identity** (who has what role, which managed identities exist). Keep this in the repo next to IaC or in a dedicated architecture doc. Reference Azure compliance and shared responsibility where relevant for audits.
    - **Runbooks**: Document how to scale, restart, fail over, or recover key Azure resources; how to rotate secrets in Key Vault; and how to respond to Defender for Cloud alerts. Link runbooks from your incident or alerting tool.

=== "DE"

    - Dokumentiere **Ressourcen-Layout** (Subscriptions, Ressourcengruppen, Naming), **Networking** (VNet, Subnets, Private Endpoints) und **Identität** (wer hat welche Rolle, welche Managed Identities existieren). Halte dies im Repo neben IaC oder in einem dedizierten Architektur-Dokument.
    - **Runbooks**: Dokumentiere, wie man skaliert, neustartet, Failover durchführt oder wichtige Azure-Ressourcen wiederherstellt; wie man Secrets im Key Vault rotiert; und wie man auf Defender for Cloud Alerts reagiert.

**GitHub**
=== "EN"

    - **README**: Every repo should have a README with purpose, how to build/run/test, and where to find more (docs, CONTRIBUTING, SECURITY). Keep it short and accurate.
    - **CONTRIBUTING.md / SECURITY.md**: Describe how to contribute and how to report vulnerabilities; link from README. Update when your process changes.
    - **Docs in repo**: Use a `/docs` folder (or similar) for architecture, ADRs, and runbooks so they are versioned with the code. Optionally use **GitHub Pages** or an external site for rendered docs; ensure the source remains the single source of truth and is linked from the repo.

=== "DE"

    - **README**: Jedes Repo sollte eine README haben mit Zweck, Bau-/Run-/Test-Anleitung und weiterführenden Links (Docs, CONTRIBUTING, SECURITY). Halte sie kurz und präzise.
    - **CONTRIBUTING.md / SECURITY.md**: Beschreibe, wie man beiträgt und Schwachstellen meldet. Aktualisiere bei Prozessänderungen.
    - **Docs im Repo**: Nutze einen `/docs`-Ordner (oder ähnlich) für Architektur, ADRs und Runbooks, damit sie mit dem Code versioniert sind. Optional **GitHub Pages** für gerenderte Docs nutzen; Quelle bleibt Single Source of Truth.

## AI Coding

=== "EN"

    AI tools increase speed but require human verification and strict security boundaries.

    AI tools can improve speed, but they also introduce new quality, security, and compliance risks. Treat AI output like external code: useful, but never trusted by default.

=== "DE"

    KI-Tools erhöhen die Geschwindigkeit, erfordern aber menschliche Überprüfung und strikte Sicherheitsgrenzen.

    KI-Tools können die Geschwindigkeit erhöhen, führen aber auch neue Qualitäts-, Sicherheits- und Compliance-Risiken ein. Behandle KI-Output wie externen Code: nützlich, aber standardmäßig nie vertrauenswürdig.

**General**
=== "EN"

    - **Human accountability**: Engineers remain responsible for correctness, security, and compliance of all AI-generated code.
    - **No sensitive input in prompts**: Do not paste production secrets, personal data, internal credentials, or confidential customer details into AI prompts.
    - **Verification-first workflow**: Verify APIs, commands, versions, and security settings against official docs before merging.
    - **Mandatory review for critical changes**: Require explicit human review for auth, crypto, tenant isolation, payments, and infrastructure/security configuration.
    - **Testing for AI-generated changes**: Add/extend unit, integration, and regression tests; for risky input surfaces, include fuzzing or robustness tests.
    - **Dependency discipline**: AI suggestions for new packages must pass license/security checks and be justified.
    - **Traceability**: Document substantial AI-assisted decisions in PR description and link to resulting tests/docs.

=== "DE"

    - **Menschliche Verantwortung**: Ingenieure bleiben verantwortlich für Korrektheit, Sicherheit und Compliance allen KI-generierten Codes.
    - **Kein sensitiver Input in Prompts**: Füge keine Produktions-Secrets, personenbezogene Daten, internen Credentials oder vertrauliche Kundendetails in KI-Prompts ein.
    - **Verifikation zuerst**: Überprüfe APIs, Befehle, Versionen und Sicherheitseinstellungen gegen offizielle Dokumentation vor dem Merge.
    - **Verpflichtendes Review für kritische Änderungen**: Fordere explizites menschliches Review für Auth, Krypto, Mandantenisolierung, Zahlungen und Infrastruktur-/Sicherheitskonfiguration.
    - **Testen von KI-generierten Änderungen**: Erweitere Unit-, Integrations- und Regressionstests; bei risikoreichen Eingabeoberflächen nutze Fuzzing oder Robustheitstests.
    - **Abhängigkeits-Disziplin**: KI-Vorschläge für neue Pakete müssen Lizenz-/Sicherheitschecks bestehen und begründet sein.
    - **Rückverfolgbarkeit**: Dokumentiere substanzielle KI-assistierte Entscheidungen in der PR-Beschreibung und verlinke auf resultierende Tests/Docs.

**Azure**
=== "EN"

    - Keep AI-generated infrastructure changes under IaC + review (Bicep/Terraform), never direct portal-only changes.
    - Verify Azure-specific security settings proposed by AI (RBAC scope, Key Vault access model, private endpoints, Defender recommendations) before rollout.
    - For AI features hosted in Azure, define data handling rules (retention, logging minimisation, tenant isolation, PII handling) and validate against customer requirements.

=== "DE"

    - Halte KI-generierte Infrastrukturänderungen unter IaC + Review (Bicep/Terraform), niemals direkte Portal-only Änderungen.
    - Verifiziere Azure-spezifische Sicherheitseinstellungen, die von KI vorgeschlagen wurden (RBAC-Scope, Key-Vault-Zugriffsmodell, Private Endpoints), vor dem Rollout.
    - Für KI-Features, die in Azure gehostet werden, definiere Datenhandhabungsregeln (Retention, Logging-Minimierung, Mandantenisolierung, PII) und validiere gegen Kundenanforderungen.

**GitHub**
=== "EN"

    - Use branch protection and required checks so AI-generated code cannot bypass review.
    - Run CodeQL, secret scanning, Dependabot, and tests on every PR containing AI-assisted changes.
    - Use CODEOWNERS for sensitive paths (auth, infra, CI/CD workflows, security config) to enforce expert review.
    - Keep PR templates explicit: include a checkbox for AI-assisted contribution and required validation steps completed.

=== "DE"

    - Nutze Branch Protection und erforderliche Checks, damit KI-generierter Code kein Review umgehen kann.
    - Führe CodeQL, Secret Scanning, Dependabot und Tests bei jedem PR aus, der KI-assistierte Änderungen enthält.
    - Nutze CODEOWNERS für sensitive Pfade (Auth, Infra, CI/CD, Security Config), um Experten-Review zu erzwingen.
    - Halte PR-Templates explizit: Füge eine Checkbox für KI-assistierten Beitrag und abgeschlossene Validierungsschritte hinzu.

## Code Quality

=== "EN"

    Maintainable and readable code ensures long-term software health.

    Good software is maintainable, readable, and adaptable. Code quality is not just about "it works," but "it can be changed safely."

=== "DE"

    Wartbarer und lesbarer Code sichert die langfristige Gesundheit der Software.

    Gute Software ist wartbar, lesbar und anpassbar. Code-Qualität bedeutet nicht nur „es funktioniert“, sondern „es kann sicher geändert werden“.

**General**
=== "EN"

    - **Clean Code Principles**:
      - **Naming**: Use descriptive, consistent naming conventions. Code should read like a sentence.
      - **Functions**: Keep functions small and focused on a single task (Single Responsibility Principle).
      - **Comments**: Code should explain *what* and *how*; comments should explain *why*. Avoid redundant comments.
    - **Architecture Patterns**:
      - Adopt a clear architecture (e.g., Hexagonal, Clean Architecture, or MVC) to separate concerns (UI, Business Logic, Data Access).
      - **DRY (Don't Repeat Yourself)**: Abstract common logic, but beware of premature abstraction.
      - **KISS (Keep It Simple, Stupid)**: Simple solutions are easier to maintain and debug than complex ones.
    - **API Design**:
      - Follow standard conventions (e.g., RESTful status codes, standard headers).
      - Use versioning for public APIs to avoid breaking changes.
      - Return meaningful error messages (e.g., RFC 7807 Problem Details).
    - **Tooling**:
      - Use **Linters** (e.g., ESLint, Pylint) and **Formatters** (e.g., Prettier, Black) to enforce style automatically.
      - Configuration for these tools must be part of the repository.

=== "DE"

    - **Clean Code Prinzipien**:
      - **Benennung**: Nutze deskriptive, konsistente Namenskonventionen. Code sollte sich wie ein Satz lesen.
      - **Funktionen**: Halte Funktionen klein und fokussiert auf eine Aufgabe (Single Responsibility Principle).
      - **Kommentare**: Code sollte *was* und *wie* erklären; Kommentare sollten *warum* erklären. Vermeide redundante Kommentare.
    - **Architekturmuster**:
      - Wähle eine klare Architektur (z. B. Hexagonal, Clean Architecture oder MVC), um Verantwortlichkeiten zu trennen (UI, Geschäftslogik, Datenzugriff).
      - **DRY (Don't Repeat Yourself)**: Abstrahiere gemeinsame Logik, aber hüte dich vor voreiliger Abstraktion.
      - **KISS (Keep It Simple, Stupid)**: Einfache Lösungen sind leichter zu warten und zu debuggen als komplexe.
    - **API-Design**:
      - Folge Standardkonventionen (z. B. RESTful Statuscodes, Standard-Header).
      - Nutze Versionierung für öffentliche APIs, um Breaking Changes zu vermeiden.
      - Gib aussagekräftige Fehlermeldungen zurück (z. B. RFC 7807 Problem Details).
    - **Tooling**:
      - Nutze **Linter** (z. B. ESLint, Pylint) und **Formatter** (z. B. Prettier, Black), um Stil automatisch durchzusetzen.
      - Konfiguration für diese Tools muss Teil des Repositories sein.

**Azure**
=== "EN"

    - **SDK usage**: Prefer official Azure SDKs over raw HTTP calls for better resilience, retry logic, and authentication support.
    - **Managed Services**: Prefer leveraging platform capabilities (e.g., Event Grid for decoupled messaging) over building custom "glue" code.

=== "DE"

    - **SDK-Nutzung**: Bevorzuge offizielle Azure SDKs gegenüber rohen HTTP-Calls für bessere Resilienz, Retry-Logik und Auth-Support.
    - **Managed Services**: Bevorzuge Plattformfähigkeiten (z. B. Event Grid für entkoppeltes Messaging) gegenüber dem Bau von eigenem „Glue“-Code.

**GitHub**
=== "EN"

    - **Enforce consistency**: Run linters and formatters in **GitHub Actions**; fail the build on violations.
    - **Code Review**: Use **PR Templates** to remind reviewers to check for readability and architecture, not just functionality.
    - **Tech Debt**: Use issues or specific tags to track technical debt visibility.

=== "DE"

    - **Konsistenz erzwingen**: Führe Linter und Formatter in **GitHub Actions** aus; lasse den Build bei Verstößen fehlschlagen.
    - **Code Review**: Nutze **PR-Templates**, um Reviewer an Lesbarkeit und Architektur zu erinnern, nicht nur an Funktionalität.
    - **Tech Debt**: Nutze Issues oder spezifische Tags, um technische Schulden sichtbar zu machen.

## Accessibility

=== "EN"

    Inclusive design ensures software is usable by everyone and meets legal standards.

    Software must be usable by everyone, including people with disabilities. This is not optional; it is a legal requirement (e.g., BFSG 2025 in Germany) and a quality mark.

=== "DE"

    Inklusives Design stellt sicher, dass Software für alle nutzbar ist und rechtliche Standards erfüllt.

    Software muss für jeden nutzbar sein, auch für Menschen mit Einschränkungen. Dies ist keine Option, sondern eine rechtliche Anforderung (z. B. BFSG 2025 in Deutschland) und ein Qualitätsmerkmal.

**General**
=== "EN"

    - **Standards**: Target **WCAG 2.1 Level AA** (or higher) compliance.
    - **Semantics**: Use proper HTML5 semantic elements (`<nav>`, `<main>`, `<button>` vs. `<div>`) to ensure screen reader compatibility.
    - **Navigation**: Ensure the entire application is operable via **keyboard only** (visible focus indicators, logical tab order).
    - **Visuals**:
      - Ensure sufficient **color contrast** for text and UI elements.
      - Do not use color alone to convey information (use icons/text labels too).
    - **Internationalization (i18n)**:
      - Design for multiple languages and locales from the start (RTL support, date/number formatting).
      - Externalize all user-facing strings into resource files.

=== "DE"

    - **Standards**: Ziele auf **WCAG 2.1 Level AA** (oder höher).
    - **Semantik**: Nutze korrekte semantische HTML5-Elemente (`<nav>`, `<main>`, `<button>` vs. `<div>`) für Screenreader-Kompatibilität.
    - **Navigation**: Stelle sicher, dass die gesamte Anwendung **nur per Tastatur** bedienbar ist (sichtbarer Fokus, logische Tab-Reihenfolge).
    - **Visuelles**:
      - Stelle ausreichenden **Farbkontrast** für Text und UI-Elemente sicher.
      - Nutze Farbe nicht als alleinigen Informationsträger (verwende zusätzlich Icons/Text).
    - **Internationalisierung (i18n)**:
      - Plane von Anfang an für mehrere Sprachen und Regionen (RTL-Support, Datums-/Zahlenformate).
      - Lagere alle sichtbaren Texte in Ressourcendateien aus.

**Azure**
=== "EN"

    - **AI Services**: Use **Azure AI Services** (e.g., Computer Vision for image alt text, Speech-to-Text) to enhance accessibility features in your app.
    - **Content Delivery**: Use Azure CDN/Front Door to deliver localized content with low latency.

=== "DE"

    - **AI Services**: Nutze **Azure AI Services** (z. B. Computer Vision für Bildbeschreibungen, Speech-to-Text), um Barrierefreiheitsfunktionen in deiner App zu verbessern.
    - **Content Delivery**: Nutze Azure CDN/Front Door, um lokalisierte Inhalte mit niedriger Latenz auszuliefern.

**GitHub**
=== "EN"

    - **Automated Testing**: Integrate accessibility testing tools (e.g., **axe-core**, **pa11y**) into your CI/CD pipeline to catch basic errors (missing alt text, bad contrast).
    - **Manual Review**: Include accessibility checks in PR templates and release reviews.

=== "DE"

    - **Automatisiertes Testen**: Integriere A11y-Testing-Tools (z. B. **axe-core**, **pa11y**) in deine CI/CD-Pipeline, um Basisfehler zu finden (fehlende Alt-Texte, schlechter Kontrast).
    - **Manuelles Review**: Füge Barrierefreiheits-Checks zu PR-Templates und Release-Reviews hinzu.

## Performance

=== "EN"

    Efficient software respects user resources and reduces operational costs.

    Performance is a feature. Efficient software respects user time and resources (battery, bandwidth) and reduces operational costs/carbon footprint.

=== "DE"

    Effiziente Software respektiert Nutzerressourcen und senkt Betriebskosten.

    Performance ist ein Feature. Effiziente Software respektiert die Zeit und Ressourcen der Nutzer (Batterie, Bandbreite) und reduziert Betriebskosten sowie den CO₂-Fußabdruck.

**General**
=== "EN"

    - **Frontend Performance**:
      - Monitor **Core Web Vitals** (LCP, CLS, INP).
      - Optimize assets: Lazy load images/modules, minimize bundle sizes, use modern formats (WebP/AVIF).
    - **Backend Efficiency**:
      - **Caching**: Implement caching strategies at multiple layers (browser, CDN, application, database).
      - **Database**: Optimize queries, use indexes effectively, and avoid N+1 query problems.
    - **Green Coding**:
      - Optimize for energy efficiency: reduce unnecessary data transfer and processing.
      - Scale down resources when not in use (auto-scaling).

=== "DE"

    - **Frontend-Performance**:
      - Überwache **Core Web Vitals** (LCP, CLS, INP).
      - Optimiere Assets: Lazy-Loading für Bilder/Module, Bundle-Größen minimieren, moderne Formate (WebP/AVIF).
    - **Backend-Effizienz**:
      - **Caching**: Implementiere Caching-Strategien auf mehreren Ebenen (Browser, CDN, App, Datenbank).
      - **Datenbank**: Optimiere Abfragen, nutze Indizes effektiv, vermeide N+1-Abfrageprobleme.
    - **Green Coding**:
      - Optimiere auf Energieeffizienz: Reduziere unnötige Datenübertragung und -verarbeitung.
      - Skaliere Ressourcen herunter, wenn sie nicht genutzt werden (Auto-Scaling).

**Azure**
=== "EN"

    - **Caching**: Use **Azure Cache for Redis** for high-speed data access; use **Azure Front Door** or **CDN** for static content caching.
    - **Auto-scaling**: Configure auto-scaling rules for App Services and AKS to match demand and reduce waste.
    - **Monitoring**: Use **Application Insights** to identify bottlenecks and slow dependencies.

=== "DE"

    - **Caching**: Nutze **Azure Cache for Redis** für schnellen Datenzugriff; nutze **Azure Front Door** oder **CDN** für statisches Content-Caching.
    - **Auto-Scaling**: Konfiguriere Auto-Scaling-Regeln für App Services und AKS, um Ressourcenbedarf anzupassen und Verschwendung zu vermeiden.
    - **Monitoring**: Nutze **Application Insights**, um Engpässe und langsame Abhängigkeiten zu identifizieren.

**GitHub**
=== "EN"

    - **Performance Budgets**: Use tools (e.g., **Lighthouse CI**) in GitHub Actions to fail builds that exceed bundle size or performance thresholds.
    - **Load Testing**: Schedule regular load tests (e.g., via k6) to verify system behavior under stress.

=== "DE"

    - **Performance Budgets**: Nutze Tools (z. B. **Lighthouse CI**) in GitHub Actions, um Builds bei Überschreitung von Größen- oder Performance-Grenzen fehlschlagen zu lassen.
    - **Lasttests**: Plane regelmäßige Lasttests (z. B. via k6), um das Systemverhalten unter Stress zu verifizieren.

## FinOps

=== "EN"

    Cost awareness and optimization align technical decisions with business value.

    Cost efficiency is a key quality metric. Good software delivers value without waste. In the cloud, every architectural decision has a direct price tag. FinOps is not just about saving money; it is about **understanding** where money goes (unit economics) and making conscious trade-offs.

=== "DE"

    Kostenbewusstsein und Optimierung richten technische Entscheidungen am Geschäftswert aus.

    Kosteneffizienz ist ein zentrales Qualitätsmerkmal. Gute Software liefert Wert ohne Verschwendung. In der Cloud hat jede Architekturentscheidung ein Preisschild. FinOps bedeutet nicht nur Geld sparen, sondern zu **verstehen**, wohin das Geld fließt (Unit Economics) und bewusste Abwägungen zu treffen.

**General**
=== "EN"

    - **Unit Economics**:
      - Understand the cost per user, per tenant, or per transaction.
      - Architecture must support cost attribution (e.g., via tagging or separate resources).
    - **Cost Awareness in Design**:
      - Choose the right service model (Serverless vs. Dedicated) based on load patterns.
      - Avoid over-provisioning "just in case"; design for scaling instead.
    - **Lifecycle Management**:
      - Automate the deletion of temporary resources (e.g., ephemeral environments, old logs, backups beyond retention).
      - Use storage tiering (Hot -> Cool -> Archive) for data that ages.
    - **Green Software**:
      - Optimize for **carbon intensity**: Run heavy batch jobs when the grid is green (if possible).
      - Reduce data transfer: Sending less data over the network saves energy and cost.

=== "DE"

    - **Unit Economics**:
      - Verstehe die Kosten pro Nutzer, Mandant oder Transaktion.
      - Die Architektur muss Kostenzuordnung unterstützen (z. B. via Tags oder separate Ressourcen).
    - **Kostenbewusstsein im Design**:
      - Wähle das richtige Servicemodell (Serverless vs. Dedicated) basierend auf Lastmustern.
      - Vermeide Überprovisionierung „nur für den Fall“; designe stattdessen für Skalierung.
    - **Lebenszyklus-Management**:
      - Automatisiere das Löschen temporärer Ressourcen (ephemere Umgebungen, alte Logs, Backups über Retention hinaus).
      - Nutze Storage Tiering (Hot -> Cool -> Archive) für alternde Daten.
    - **Green Software**:
      - Optimiere auf **Kohlenstoffintensität**: Führe schwere Batch-Jobs aus, wenn das Stromnetz grün ist (wo möglich).
      - Reduziere Datentransfer: Weniger Daten über das Netzwerk zu senden, spart Energie und Kosten.

**Azure**
=== "EN"

    - **Cost Analysis & Budgets**:
      - Use **Azure Cost Management** to set budgets and alerts at the subscription and resource group level.
      - Tag every resource with `Owner`, `Environment`, `CostCenter`, and `Application`.
    - **Architectural Fit**:
      - Use **Consumption Plans** (Functions, Logic Apps) for sporadic workloads to pay only for execution.
      - Use **Reserved Instances** or **Savings Plans** for predictable, steady-state workloads (databases, VMs).
      - Use **Spot Instances** for interruptible batch jobs or stateless nodes in AKS.
    - **Cleanup**:
      - Use **Azure Policy** to deny creation of expensive SKUs in non-production environments.
      - Implement automated scripts (e.g., Azure Automation runbooks) to shut down dev/test VMs at night.

=== "DE"

    - **Kostenanalyse & Budgets**:
      - Nutze **Azure Cost Management**, um Budgets und Alarme auf Subscription- und Ressourcengruppen-Ebene zu setzen.
      - Tagge jede Ressource mit `Owner`, `Environment`, `CostCenter` und `Application`.
    - **Architektonische Passgenauigkeit**:
      - Nutze **Consumption Plans** (Functions, Logic Apps) für sporadische Workloads (Pay-per-Execution).
      - Nutze **Reserved Instances** oder **Savings Plans** für vorhersagbare Dauerlast (Datenbanken, VMs).
      - Nutze **Spot Instances** für unterbrechbare Batch-Jobs oder Stateless Nodes in AKS.
    - **Aufräumen**:
      - Nutze **Azure Policy**, um teure SKUs in Nicht-Produktionsumgebungen zu verbieten.
      - Implementiere automatisierte Skripte (z. B. Azure Automation Runbooks), um Dev/Test-VMs nachts herunterzufahren.

**GitHub**
=== "EN"

    - **CI/CD Costs**:
      - Monitor **GitHub Actions** minutes; use caching to speed up builds and reduce billable time.
      - Use self-hosted runners for heavy workloads if they are cheaper than GitHub-hosted runners.
    - **Reporting**:
      - Integrate cost reports into the development dashboard. Engineers should see the cost impact of their changes.

=== "DE"

    - **CI/CD-Kosten**:
      - Überwache **GitHub Actions**-Minuten; nutze Caching, um Builds zu beschleunigen und billable time zu reduzieren.
      - Nutze Self-Hosted Runner für schwere Workloads, wenn sie günstiger sind als GitHub-Hosted Runner.
    - **Reporting**:
      - Integriere Kostenberichte in das Entwicklungs-Dashboard. Ingenieure sollten den Kosteneinfluss ihrer Änderungen sehen.

## Compliance

=== "EN"

    Adhering to standards ensures legal conformity and builds customer trust.

=== "DE"

    Die Einhaltung von Standards sichert Rechtskonformität und baut Kundenvertrauen auf.

**General**
=== "EN"

    Relevant frameworks for legal compliance and customer trust requirements (especially for the German/EU market):

    | Standard | Scope | When it matters |
    | :--- | :--- | :--- |
    | **ISO/IEC 27001** | Information Security Management System (ISMS): processes, risk analysis, organisational security. | Handling sensitive or regulated data; customer and partner expectations. |
    | **GDPR (DSGVO)** | EU data protection: minimisation, transparency, consent, rights of data subjects. | Any processing of personal data in the EU; mandatory, not optional. |
    | **TISAX** | Assessment and exchange of security information (e.g. automotive). | Customers in automotive or similar regulated supply chains. |
    | **BSI IT-Grundschutz** | German BSI standard for baseline information security (modular). | German public sector or customers requiring BSI alignment. |

    Compliance must be documented and auditable. GDPR is a legal obligation you fulfil and document. For other frameworks, align with what your customers and contracts actually require.

    **Important: platform assurance is not your automatic certification**
    - If you use certified platforms, you can inherit parts of their control environment (sometimes called indirect/inherited assurance).
    - This does **not** mean your application is automatically certified or compliant.
    - You still need your own controls, evidence, and customer-facing transparency for what you operate (configuration, identities, code, data processing, incident handling).

    **What is typically inherited vs. what remains your responsibility**

    | Area | Mostly inherited from platform/provider | Your responsibility |
    | :--- | :--- | :--- |
    | Physical datacenter security | Building access control, hardware lifecycle, environmental controls | Select region/provider, verify scope, keep contracts/evidence |
    | Core cloud infrastructure | Hypervisor/platform hardening, base network backbone controls | Secure service configuration, tenant isolation, key/secret handling |
    | Managed service baseline controls | Service-level controls as audited by provider | App-layer controls, least privilege, logging/alerting setup |
    | Compliance reports and attestations | Provider certificates/reports (in scope) | Map provider controls to your system and close remaining gaps |
    | Privacy/compliance tooling | Built-in platform features | Lawful basis, retention, deletion, DSAR process, customer commitments |

    **How to present this to customers (trust + transparency)**
    - Share a short responsibility matrix: `Provider control` / `Your control` / `Evidence`.
    - Share only scope-valid claims (e.g. “hosted on Azure, which maintains ISO 27001 for in-scope services”).
    - Avoid ambiguous statements like “our app is ISO-certified” unless your own org/app scope was audited accordingly.
    - Keep customer-ready evidence package updated (architecture, runbooks, scan reports, incident process, platform attestations).

=== "DE"

    Relevante Frameworks für rechtliche Compliance und Kundenvertrauensanforderungen (besonders für den DE/EU-Markt):

    | Standard | Scope | Wann relevant |
    | :--- | :--- | :--- |
    | **ISO/IEC 27001** | ISMS (Information Security Management System): Prozesse, Risikoanalyse, organisatorische Sicherheit. | Umgang mit sensiblen oder regulierten Daten; Kunden- und Partnererwartungen. |
    | **DSGVO (GDPR)** | EU-Datenschutz: Minimierung, Transparenz, Einwilligung, Betroffenenrechte. | Jede Verarbeitung personenbezogener Daten in der EU; gesetzlich verpflichtend, nicht optional. |
    | **TISAX** | Austausch von Prüfergebnissen zur Informationssicherheit (z. B. Automotive). | Kunden in der Automobilindustrie oder ähnlichen regulierten Lieferketten. |
    | **BSI IT-Grundschutz** | Standard des BSI für Basissicherheit (modular). | Öffentlicher Sektor in Deutschland oder Kunden, die BSI-Ausrichtung fordern. |

    Compliance muss dokumentiert und auditierbar sein. DSGVO ist eine gesetzliche Pflicht, die du erfüllst und dokumentierst. Bei anderen Frameworks: Richte dich danach, was deine Kunden und Verträge tatsächlich verlangen.

    **Wichtig: Plattformsicherheit ist nicht deine automatische Zertifizierung**
    - Wenn du zertifizierte Plattformen nutzt, kannst du Teile ihres Kontrollumfelds erben (sog. indirekte/geerbte Assurance).
    - Das bedeutet **nicht**, dass deine Anwendung automatisch zertifiziert oder compliant ist.
    - Du benötigst weiterhin eigene Kontrollen, Nachweise und Transparenz für das, was du betreibst (Konfiguration, Identitäten, Code, Datenverarbeitung, Incident Handling).

    **Was typischerweise geerbt wird vs. was deine Verantwortung bleibt**

    | Bereich | Meist geerbt von Plattform/Provider | Deine Verantwortung |
    | :--- | :--- | :--- |
    | Physische Rechenzentrumssicherheit | Gebäudezutritt, Hardware-Lifecycle, Umweltkontrollen | Regionswahl, Scope-Verifikation, Verträge/Nachweise vorhalten |
    | Cloud-Basisinfrastruktur | Hypervisor-/Plattformhärtung, Basis-Netzwerkkontrollen | Sichere Servicekonfiguration, Mandantenisolierung, Key/Secret-Handling |
    | Managed Service Basiskontrollen | Service-Level-Kontrollen (vom Provider auditiert) | App-Layer-Kontrollen, Least Privilege, Logging/Alerting-Setup |
    | Compliance-Berichte & Attestate | Provider-Zertifikate (im Scope) | Mapping der Provider-Kontrollen auf dein System & Schließen von Lücken |
    | Datenschutz-/Compliance-Tools | Eingebaute Plattformfeatures | Rechtsgrundlage, Löschung, Betroffenenanfragen, Kundenverpflichtungen |

    **Wie man dies Kunden präsentiert (Vertrauen + Transparenz)**
    - Teile eine kurze Verantwortungsmatrix: `Provider-Kontrolle` / `Deine Kontrolle` / `Nachweis`.
    - Mache nur scope-valide Aussagen (z. B. „gehostet auf Azure, das ISO 27001 für die genutzten Dienste unterhält“).
    - Vermeide mehrdeutige Aussagen wie „unsere App ist ISO-zertifiziert“, es sei denn, dein eigener Org/App-Scope wurde auditiert.
    - Halte ein kundenfertiges Nachweispaket aktuell (Architektur, Runbooks, Scan-Berichte, Incident-Prozess, Plattform-Attestate).

**Azure**
=== "EN"

      - Azure maintains broad compliance programs and attestations (for in-scope services), commonly including: **ISO/IEC 27001**, **ISO/IEC 27017**, **ISO/IEC 27018**, **SOC 1/2/3**, **PCI DSS**, and **CSA STAR**.
      - What you can legitimately claim in customer conversations:
          - Your solution runs on Azure services that are covered by specific provider attestations.
          - You apply Azure security features (e.g. Entra ID, Key Vault, private networking, Defender controls) as part of your own control set.
          - You can provide provider evidence references plus your own implementation evidence.
      - What you still must prove yourself:
          - Correct service configuration, RBAC model, tenant isolation, secure CI/CD, data lifecycle, and incident response.
          - Contractual and legal controls around customer data processing and retention.
      - Practical trust artifacts from Azure side:
          - Service scope check (is each used Azure service covered by required standard).
          - Shared-responsibility mapping per control.
          - References to official Microsoft compliance documentation/report availability.

=== "DE"

      - Azure unterhält umfassende Compliance-Programme (für Dienste im Scope), häufig inkl.: **ISO/IEC 27001**, **ISO/IEC 27017**, **ISO/IEC 27018**, **SOC 1/2/3**, **PCI DSS** und **CSA STAR**.
      - Was du legitim behaupten kannst:
          - Deine Lösung läuft auf Azure-Diensten, die durch spezifische Provider-Attestate abgedeckt sind.
          - Du wendest Azure-Sicherheitsfeatures (z. B. Entra ID, Key Vault, Private Networking) als Teil deines Kontrollsets an.
          - Du kannst Provider-Nachweise plus deine eigenen Implementierungsnachweise bereitstellen.
      - Was du selbst beweisen musst:
          - Korrekte Servicekonfiguration, RBAC-Modell, Mandantenisolierung, sichere CI/CD, Datenlebenszyklus und Incident Response.
          - Vertragliche und rechtliche Kontrollen rund um Kundendatenverarbeitung.
      - Praktische Vertrauens-Artefakte (Azure-Seite):
          - Service-Scope-Check (ist jeder genutzte Dienst abgedeckt?).
          - Shared-Responsibility-Mapping.
          - Verweise auf offizielle Microsoft-Compliance-Doku.

**GitHub**
=== "EN"

      GitHub also provides audited compliance programs/attestations for its platform scope, commonly including: **SOC 1 Type 2**, **SOC 2 Type 2**, **SOC 3**, **ISO/IEC 27001**, **ISO/IEC 27701**, **ISO/IEC 27018**, and **CSA STAR** (scope depends on product/features/plan).
      
      What you can claim:
      - Your source control and CI/CD process runs on GitHub services with defined compliance attestations.
      - You enforce repository-level security controls (branch protection, reviews, Dependabot, code scanning, secret scanning).
      
      What remains yours:
      - Secure workflow design, permissions model, secrets governance, release approvals, and response process for findings.
      - Correct use of GitHub features and evidence retention for your own audits/customer reviews.
      
      Practical trust artifacts from GitHub side:
      - Repository/org security settings export or documented baseline.
      - Evidence of enabled controls (e.g. CodeQL/Dependabot/secret scanning status, branch rules).
      - References to GitHub compliance reports available for your plan.

=== "DE"

      GitHub bietet ebenfalls auditierte Compliance-Programme (je nach Plan/Scope), z. B.: **SOC 1/2/3**, **ISO 27001**, **ISO 27701** und **CSA STAR**.
      
      Was du behaupten kannst:
      - Dein Versionskontroll- und CI/CD-Prozess läuft auf GitHub-Diensten mit definierten Attestaten.
      - Du erzwingst Repository-Sicherheitskontrollen (Branch Protection, Reviews, Dependabot, Scanning).
      
      Was deins bleibt:
      - Sicheres Workflow-Design, Berechtigungsmodell, Secrets-Governance, Release-Freigaben und Reaktion auf Findings.
      - Korrekte Nutzung von GitHub-Features und Nachweisführung für eigene Audits.
      
      Praktische Vertrauens-Artefakte (GitHub-Seite):
      - Export der Repo/Org-Sicherheitseinstellungen.
      - Nachweis aktivierter Kontrollen (CodeQL/Dependabot-Status).
      - Verweise auf GitHub-Compliance-Berichte.

## German Market

=== "EN"

    Specific requirements for data privacy and location are critical for German customers.

    What often matters to customers in Germany:

    | Topic | Why it matters |
    | :--- | :--- |
    | **Data privacy (GDPR)** | Legal obligation and strong expectation; violations are heavily penalised. |
    | **Transparency & control** | Contractual and audit requirements; data processing agreements and clear documentation. |
    | **Data residency (EU/DE)** | Avoidance of US Cloud Act and similar extra-EU access; preference for EU/EEA or German regions. |
    | **Penetration tests & reports** | Evidence of “real” security, not only checklists. |
    | **Evidence and assurances** | Customers often want concrete proof (security reports, architecture transparency, incident process), whether or not formal certification is used. |
    | **SLAs** | Clear commitments on availability and response times. |

    Use **Azure regions in the EU/EEA** (e.g. Germany, West Europe) and GitHub’s data residency options where required; document your choices and compliance posture.

=== "DE"

    Spezifische Anforderungen an Datenschutz und -ort sind für deutsche Kunden entscheidend.

    Was für Kunden in Deutschland oft zählt:

    | Thema | Warum es wichtig ist |
    | :--- | :--- |
    | **Datenschutz (DSGVO)** | Gesetzliche Pflicht und starke Erwartung; Verstöße werden schwer sanktioniert. |
    | **Transparenz & Kontrolle** | Vertrags- und Auditanforderungen; Auftragsverarbeitungsverträge (AVV) und klare Doku. |
    | **Datenstandort (EU/DE)** | Vermeidung von US Cloud Act und ähnlichem Drittstaat-Zugriff; Präferenz für EU/EWR oder deutsche Regionen. |
    | **Pentests & Berichte** | Nachweis „echter“ Sicherheit, nicht nur Checklisten. |
    | **Nachweise & Zusicherungen** | Kunden wollen oft konkrete Beweise (Sicherheitsberichte, Architekturtransparenz, Incident-Prozess), unabhängig von formaler Zertifizierung. |
    | **SLAs** | Klare Zusagen zu Verfügbarkeit und Reaktionszeiten. |

    Nutze **Azure-Regionen in der EU/EWR** (z. B. Germany West Central, West Europe) und GitHubs Data Residency Optionen, wo nötig; dokumentiere Entscheidungen und Compliance-Status.

## Trust Plan

=== "EN"

    A structured approach to transparency builds lasting customer relationships.

=== "DE"

    Ein strukturierter Ansatz für Transparenz baut dauerhafte Kundenbeziehungen auf.

**General**
=== "EN"

    1. **Ask customers what matters most**: Capture concrete trust requirements early (e.g. data residency, incident notification timelines, pentest frequency, evidence format, SLA targets).
    2. **Translate requirements into minimum controls**: Define baseline controls that map to those requirements (identity, secrets, logging, staging, backup/restore, change control).
    3. **Implement and document controls**: Apply the general and platform-specific controls (Azure, GitHub), and document ownership, operation, and evidence for each control.
    4. **Define measurable service commitments**: Set and publish practical SLO/SLA targets, support model, escalation path, and incident communication process.
    5. **Collect evidence continuously**: Keep policies, runbooks, access reviews, scan reports, deployment logs, backup/restore test results, and incident postmortems.
    6. **Review with customers regularly**: Revisit trust requirements in quarterly or release-based reviews and adapt controls when customer needs or risk changes.

=== "DE"

    1. **Frage Kunden, was zählt**: Erfasse konkrete Vertrauensanforderungen früh (z. B. Datenstandort, Meldefristen, Pentest-Frequenz, SLA-Ziele).
    2. **Übersetze Anforderungen in minimale Kontrollen**: Definiere Basiskontrollen, die diese Anforderungen erfüllen (Identität, Secrets, Logging, Staging, Backup, Change Control).
    3. **Implementiere und dokumentiere**: Wende die allgemeinen und plattformspezifischen Kontrollen an und dokumentiere Ownership, Betrieb und Nachweise.
    4. **Definiere messbare Zusagen**: Setze und veröffentliche praktische SLO/SLA-Ziele, Supportmodell, Eskalationspfad und Kommunikationsprozesse.
    5. **Sammle Nachweise kontinuierlich**: Halte Policies, Runbooks, Access Reviews, Scan-Berichte, Deployment-Logs, Restore-Tests und Incident-Post-Mortems bereit.
    6. **Regelmäßiges Kunden-Review**: Prüfe Vertrauensanforderungen in vierteljährlichen oder release-basierten Reviews und passe Kontrollen bei Bedarf an.

## Security Baseline

=== "EN"

    A defined baseline ensures a consistent minimum security standard across projects.

    Use this as a practical template; tailor the thresholds to your product and customer expectations.

=== "DE"

    Eine definierte Baseline sichert einen konsistenten Mindestsicherheitsstandard über Projekte hinweg.

    Nutze dies als Vorlage; passe die Schwellenwerte an dein Produkt und Kundenerwartungen an.

**General**
=== "EN"

    **Identity & access**
    - MFA required for all human access to production-related systems.
    - RBAC is enforced; no broad admin role for day-to-day work.
    - Access reviews are performed on a fixed cadence (e.g. quarterly).
    
    **Secrets & data protection**
    - Secrets are stored only in approved secret stores.
    - TLS 1.2+ is enforced externally; encryption at rest is enabled.
    - Production data is never used in staging without anonymisation and approval.
    - Domain/email trust controls are configured: valid cert lifecycle, SPF, DKIM, and DMARC.
    
    **Secure delivery**
    - Protected branches require PR review and passing checks.
    - CI runs test + security checks (SAST/SCA at minimum).
    - High-risk input surfaces (e.g. file upload/parsing endpoints) are covered by fuzzing or equivalent robustness tests.
    - Critical findings block release until addressed or explicitly risk-accepted.
    
    **Operations & resilience**
    - Central logging and alerting are enabled for auth failures, deployment failures, and major anomalies.
    - Backup/restore process is defined, with RPO/RTO targets and restore test cadence.
    - Incident response roles, escalation path, and communication templates are documented.
    
    **Transparency & documentation**
    - Changelog and release notes are maintained.
    - Security contact/reporting path is public (e.g. SECURITY.md).
    - Core architecture, runbooks, and key decisions are documented and current.

=== "DE"

    **Identität & Zugriff**
    - MFA für jeden menschlichen Zugriff auf produktionsrelevante Systeme.
    - RBAC erzwungen; keine breite Admin-Rolle für tägliche Arbeit.
    - Zugriffsreviews in festem Rhythmus (z. B. vierteljährlich).
    
    **Secrets & Datenschutz**
    - Secrets nur in zugelassenen Stores gespeichert.
    - TLS 1.2+ extern erzwungen; Verschlüsselung im Ruhezustand aktiv.
    - Produktionsdaten nie im Staging ohne Anonymisierung und Freigabe.
    - Domain-/E-Mail-Vertrauenskontrollen: Zertifikatslifecycle, SPF, DKIM, DMARC.
    
    **Sichere Auslieferung**
    - Geschützte Branches erfordern PR-Review und Checks.
    - CI führt Test + Security-Checks (min. SAST/SCA) aus.
    - Kritische Eingabeoberflächen (z. B. File Upload) durch Fuzzing/Robustheitstests abgedeckt.
    - Kritische Funde blockieren Release bis zur Behebung oder Risikoakzeptanz.
    
    **Betrieb & Resilienz**
    - Zentrales Logging/Alerting für Auth-Fehler, Deploy-Fehler und Anomalien.
    - Backup/Restore definiert mit RPO/RTO und Test-Turnus.
    - Incident-Rollen, Eskalationspfad und Kommunikationstemplates dokumentiert.
    
    **Transparenz & Doku**
    - Changelog und Release Notes gepflegt.
    - Security Contact/Meldeweg öffentlich (z. B. SECURITY.md).
    - Kernarchitektur, Runbooks und Entscheidungen dokumentiert/aktuell.

**Azure**
=== "EN"

    - Entra ID + Conditional Access + MFA for administrative access.
    - Key Vault for secrets; managed identities preferred over static credentials.
    - Private networking where required, WAF for internet-facing apps, and Defender for Cloud recommendations tracked.
    - Staging slot or separate staging environment is required before production promotion.
    - Custom domain + certificate setup is documented and monitored (expiry/renewal).

=== "DE"

    - Entra ID + Conditional Access + MFA für administrativen Zugriff.
    - Key Vault für Secrets; Managed Identities bevorzugt.
    - Private Networking wo nötig, WAF für öffentliche Apps, Defender-Empfehlungen getrackt.
    - Staging-Slot oder separate Umgebung vor Produktion erforderlich.
    - Custom Domain + Zertifikats-Setup dokumentiert und überwacht.

**GitHub**
=== "EN"

    - Branch protection, required reviews, and required status checks are enabled.
    - GitHub Secrets or OIDC is used for cloud access; no cloud credentials in repository.
    - Dependabot and CodeQL (or equivalent) are enabled; alert ownership is defined.
    - Secret leak controls are enabled (GitHub Secret Scanning/Push Protection and/or CI scanner such as Gitleaks).
    - Environments (Staging/Production) include protection rules for production releases.
    - Domain-related deployment/config changes are reviewed via PR and tracked.

=== "DE"

    - Branch Protection, erforderliche Reviews und Statuschecks aktiviert.
    - GitHub Secrets oder OIDC für Cloud-Zugriff; keine Cloud-Credentials im Repo.
    - Dependabot und CodeQL (oder äquivalent) aktiv; Alert-Ownership definiert.
    - Secret Leak Controls aktiv (GitHub Secret Scanning/Push Protection und/oder CI-Scanner).
    - Environments (Staging/Production) mit Schutzregeln für Produktions-Releases.
    - Domain-bezogene Deployment/Config-Änderungen via PR reviewt und getrackt.

## Implementation Examples

=== "EN"

    Concrete examples and search terms to help implement these standards.

    Use this as a practical layer on top of the chapter text. For each chapter, you get: a concrete example, implementation advice, and search terms.

    | Chapter | Example | How to implement / what to consider | Search terms |
    | :--- | :--- | :--- | :--- |
    | **Core Principles** | Map key components to CIA in ADRs. | Keep 1-2 explicit controls per CIA goal per critical component; review quarterly. | `CIA triad practical controls`, `security architecture ADR template` |
    | **Identity & Access** | MFA + conditional access for admins. | Central IdP, no shared admin accounts, periodic access review. | `Azure Entra Conditional Access MFA`, `least privilege access review` |
    | **User Management, Roles, Groups & Tenants** | Roles `User/Support/Developer/Admin` defined. | Enforce tenant boundary in authz + data access layer; test cross-tenant denial. | `multi-tenant authorization patterns`, `tenant isolation best practices` |
    | **Frontend vs. Backend Security Responsibilities** | Frontend validates UX, backend enforces policy. | Never trust client-provided role/tenant IDs; server-side authz mandatory. | `frontend backend security responsibilities`, `server-side authorization` |
    | **Interfaces: API, UI & Headless** | API-First design with OpenAPI docs. | UI is just a client; support deep linking but validate all params on backend. | `api first design`, `headless automation security`, `deep linking security` |
    | **Rollenmatrix** | Role table with minimum rights + no-gos. | Add owner for each role, approval path for privilege changes, JIT admin where possible. | `RBAC role matrix template`, `JIT privileged access` |
    | **Data, Databases & Secure Design** | Fields tagged as `brisant` + masking rules. | Apply classification in schema/code/logging/export; enforce tenant-scoped queries. | `data classification model`, `row level security tenant isolation` |
    | **Data & Secrets** | Secrets only in Key Vault/GitHub Secrets. | Runtime secret retrieval, no plaintext secrets in repo/logs, rotate periodically. | `secret management best practices`, `GitHub secret scanning push protection` |
    | **Network & Infrastructure** | Public frontend, private backend/DB. | Use private endpoints/VNet + WAF + firewall rules; block direct DB internet access. | `Azure private endpoint app service`, `WAF tuning detect prevent mode` |
    | **Domain & Email Trust Setup** | SPF+DKIM+DMARC active with monitoring. | Start DMARC `p=none`, then tighten after report quality stabilizes. | `SPF DKIM DMARC setup`, `DMARC policy rollout` |
    | **Secure Development Lifecycle (SDLC)** | PR pipeline with tests + SAST + SCA + secret scan. | Required status checks block merge; define ownership/SLA for findings. | `CodeQL GitHub Actions setup`, `SCA vulnerability SLA policy` |
    | **Testing** | Every production bug gets regression test. | Define test pyramid, flake budget, fuzzing for risky parsers/endpoints. | `test pyramid practical`, `fuzz testing API endpoints` |
    | **Staging Concept** | Build once, promote same artifact. | No rebuild between staging/prod; use artifact hash/tag and approval gates. | `build once deploy many`, `release promotion strategy` |
    | **Open Source** | SBOM maintained + dependency cadence. | Track CVEs by severity/owner/SLA; enforce license policy in CI. | `SBOM generation CI`, `open source license compliance policy` |
    | **Changelogs & Communication** | Release notes include risk and rollback notes. | Keep standard template for release + incident communication. | `keep a changelog`, `incident communication template` |
    | **Monitoring & Operations** | Alerts for auth failures, WAF spikes, deploy failures. | Route alerts to on-call with runbook links; review noisy alerts monthly. | `SRE alert quality`, `runbook driven operations` |
    | **Deployment (CI/CD)** | Production deploy requires protected environment approval. | Separate staging/prod environments; minimal production deployment rights. | `GitHub environments required reviewers`, `deployment approval workflow` |
    | **Infrastructure as Code & System Configuration** | `terraform plan` on PR, apply on protected branch only. | Detect drift, ban manual changes except tracked break-glass path. | `terraform drift detection`, `policy as code Azure` |
    | **Good Documentation** | `/docs` includes architecture, runbooks, ADRs. | Make docs update part of DoD and PR checklist for relevant changes. | `docs as code best practices`, `ADR examples` |
    | **AI-Assisted Coding** | AI-generated PRs flagged + human review for sensitive paths. | Prohibit secrets/PII in prompts; same security gates as manual code. | `secure ai coding policy`, `prompt data leakage prevention` |
    | **Code Quality & Architecture** | Linter/Formatter enforced in CI + PR Template checks architecture. | Use ESLint/Prettier (or equivalent); define layer boundaries (e.g. API vs Domain). | `clean architecture principles`, `automated code formatting CI` |
    | **Accessibility (A11y) & UX** | WCAG 2.1 AA target + automated axe-core scan. | Keyboard navigation, semantic HTML, proper contrast; test with screen reader. | `WCAG 2.1 checklist`, `accessibility testing automation` |
    | **Performance & Efficiency** | Core Web Vitals monitoring + caching strategy. | Image optimization (WebP), lazy loading, database indexing, CDN usage. | `web performance optimization`, `green coding best practices` |
    | **FinOps & Cost Efficiency** | Tagging strategy + budget alerts. | Use Azure Cost Management; optimize SKU choice (Spot/Reserved); automate cleanup. | `azure cost management best practices`, `finops unit economics` |
    | **Compliance & Standards** | Shared-responsibility matrix per control family. | Do not overclaim inherited certifications; map provider vs your controls explicitly. | `shared responsibility compliance matrix`, `cloud inherited controls` |
    | **German Market Requirements** | Data residency statement + transparency commitments. | Prepare customer-ready evidence pack (security controls, logging, incident flow). | `GDPR data residency SaaS`, `security questionnaire response template` |
    | **Practical Plan for Trust & Transparency** | Quarterly customer trust review. | Track actions with owner/date/evidence link; publish progress. | `customer trust program`, `security governance review cadence` |
    | **Minimum Security Baseline (Example)** | Baseline controls have owner/due date/evidence. | Review baseline status on fixed cadence; escalate overdue essentials. | `security baseline template`, `control ownership model` |

=== "DE"

    Konkrete Beispiele und Suchbegriffe zur Umsetzung dieser Standards.

    Nutze dies als praktische Ebene über dem Kapiteltext. Für jedes Kapitel erhältst du: ein konkretes Beispiel, Implementierungshinweise und Suchbegriffe.

    | Kapitel | Beispiel | Implementierung / Zu beachten | Suchbegriffe |
    | :--- | :--- | :--- | :--- |
    | **Core Principles** | Mappe Schlüsselkomponenten auf CIA in ADRs. | Halte 1-2 explizite Kontrollen pro CIA-Ziel pro kritischer Komponente; vierteljährlich prüfen. | `CIA triad practical controls`, `security architecture ADR template` |
    | **Identity & Access** | MFA + Conditional Access für Admins. | Zentraler IdP, keine geteilten Admin-Accounts, periodisches Access-Review. | `Azure Entra Conditional Access MFA`, `least privilege access review` |
    | **User Management, Roles...** | Rollen `User/Support/Developer/Admin` definiert. | Setze Mandantengrenze in Authz + Datenzugriffsschicht durch; teste Cross-Tenant-Verweigerung. | `multi-tenant authorization patterns`, `tenant isolation best practices` |
    | **Frontend vs. Backend...** | Frontend validiert UX, Backend erzwingt Policy. | Vertraue nie Client-seitigen Rollen/Tenant-IDs; serverseitige Authz obligatorisch. | `frontend backend security responsibilities`, `server-side authorization` |
    | **Interfaces: API, UI & Headless** | API-First-Design mit OpenAPI-Doku. | UI ist nur ein Client; unterstütze Deep Linking, aber validiere alle Parameter im Backend. | `api first design`, `headless automation security`, `deep linking security` |
    | **Rollenmatrix** | Rollentabelle mit Minimalrechten + No-Gos. | Füge Owner für jede Rolle hinzu, Genehmigungspfad für Rechteänderungen, JIT-Admin wo möglich. | `RBAC role matrix template`, `JIT privileged access` |
    | **Data, Databases...** | Felder getaggt als `brisant` + Maskierungsregeln. | Wende Klassifizierung in Schema/Code/Logging/Export an; erzwinge mandantenbezogene Abfragen. | `data classification model`, `row level security tenant isolation` |
    | **Data & Secrets** | Secrets nur in Key Vault/GitHub Secrets. | Runtime-Secret-Abruf, keine Klartext-Secrets in Repo/Logs, periodische Rotation. | `secret management best practices`, `GitHub secret scanning push protection` |
    | **Network & Infrastructure** | Öffentliches Frontend, privates Backend/DB. | Nutze Private Endpoints/VNet + WAF + Firewall-Regeln; blockiere direkten DB-Internetzugriff. | `Azure private endpoint app service`, `WAF tuning detect prevent mode` |
    | **Domain & Email Trust...** | SPF+DKIM+DMARC aktiv mit Monitoring. | Starte DMARC `p=none`, verschärfe nach Stabilisierung der Berichtsqualität. | `SPF DKIM DMARC setup`, `DMARC policy rollout` |
    | **SDLC** | PR-Pipeline mit Tests + SAST + SCA + Secret Scan. | Erforderliche Statuschecks blockieren Merge; definiere Ownership/SLA für Funde. | `CodeQL GitHub Actions setup`, `SCA vulnerability SLA policy` |
    | **Testing** | Jeder Produktionsbug erhält Regressionstest. | Definiere Testpyramide, Flaky-Budget, Fuzzing für riskante Parser/Endpunkte. | `test pyramid practical`, `fuzz testing API endpoints` |
    | **Staging Concept** | Einmal bauen, dasselbe Artefakt promoten. | Kein Rebuild zwischen Staging/Prod; nutze Artefakt-Hash/Tag und Approval-Gates. | `build once deploy many`, `release promotion strategy` |
    | **Open Source** | SBOM gepflegt + Update-Turnus. | Tracke CVEs nach Schweregrad/Owner/SLA; erzwinge Lizenzpolicy in CI. | `SBOM generation CI`, `open source license compliance policy` |
    | **Changelogs & Communication** | Release Notes enthalten Risiko- und Rollback-Infos. | Halte Standardtemplate für Release- + Incident-Kommunikation bereit. | `keep a changelog`, `incident communication template` |
    | **Monitoring & Operations** | Alarme für Auth-Fehler, WAF-Spikes, Deploy-Fehler. | Route Alarme an On-Call mit Runbook-Links; prüfe laute Alarme monatlich. | `SRE alert quality`, `runbook driven operations` |
    | **Deployment (CI/CD)** | Produktions-Deploy erfordert Protected-Env-Approval. | Trenne Staging/Prod-Umgebungen; minimale Produktions-Deploy-Rechte. | `GitHub environments required reviewers`, `deployment approval workflow` |
    | **IaC & Config** | `terraform plan` im PR, Apply nur auf geschütztem Branch. | Erkenne Drift, verbiete manuelle Änderungen außer getracktem Break-Glass-Pfad. | `terraform drift detection`, `policy as code Azure` |
    | **Good Documentation** | `/docs` enthält Architektur, Runbooks, ADRs. | Mache Doku-Update zum Teil der DoD und PR-Checkliste für relevante Änderungen. | `docs as code best practices`, `ADR examples` |
    | **AI-Assisted Coding** | KI-generierte PRs geflaggt + Human-Review. | Verbiete Secrets/PII in Prompts; dieselben Security-Gates wie manueller Code. | `secure ai coding policy`, `prompt data leakage prevention` |
    | **Code Quality & Architecture** | Linter/Formatter in CI erzwungen + PR-Check. | Nutze ESLint/Prettier (oder äquiv.); definiere Schichtgrenzen (API vs. Domäne). | `clean architecture principles`, `automated code formatting CI` |
    | **Accessibility & UX** | WCAG 2.1 AA Ziel + autom. Axe-Core-Scan. | Tastaturnavigation, semantisches HTML, Kontrast; Test mit Screenreader. | `WCAG 2.1 checklist`, `accessibility testing automation` |
    | **Performance & Efficiency** | Core Web Vitals Monitoring + Caching. | Bildoptimierung (WebP), Lazy Loading, DB-Indizierung, CDN-Nutzung. | `web performance optimization`, `green coding best practices` |
    | **FinOps & Cost Efficiency** | Tagging-Strategie + Budget-Alerts. | Nutze Azure Cost Management; optimiere SKU-Wahl (Spot/Reserved); automatisiere Cleanup. | `azure cost management best practices`, `finops unit economics` |
    | **Compliance & Standards** | Shared-Responsibility-Matrix pro Kontrollfamilie. | Übernehme keine geerbten Zertifikate blind; mappe Provider vs. deine Kontrollen explizit. | `shared responsibility compliance matrix`, `cloud inherited controls` |
    | **German Market Requirements** | Data-Residency-Statement + Transparenz. | Bereite kundenfertiges Nachweispaket vor (Sicherheitskontrollen, Logging, Incident-Flow). | `GDPR data residency SaaS`, `security questionnaire response template` |
    | **Practical Plan for Trust...** | Vierteljährliches Kundenvertrauens-Review. | Tracke Aktionen mit Owner/Datum/Beweislink; veröffentliche Fortschritt. | `customer trust program`, `security governance review cadence` |
    | **Minimum Security Baseline** | Basis-Kontrollen haben Owner/Fälligkeit/Beweis. | Prüfe Basis-Status in festem Turnus; eskaliere überfällige Essentials. | `security baseline template`, `control ownership model` |

## Checklist

=== "EN"

    A summary checklist to track compliance with these standards.

    Rating scale used below:
    - **Effort**: `Low` | `Medium` | `High`
    - **Cost**: `Low` | `Medium` | `High`
    - **Importance**: `Nice-to-have` | `Important` | `Essential`

    **General**
    - [ ] CIA, Least Privilege, Defense in Depth, and **Keep it simple** reflected in design and operations `[Effort: Medium | Cost: Low | Importance: Essential]`
    - [ ] Identity: central IdP, MFA, least privilege, no secrets in config `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] User management: roles and groups defined; tenant (customer) isolation designed and enforced where multi-tenant `[Effort: High | Cost: Medium | Importance: Essential]`
    - [ ] Interfaces: API-First approach; API documented; Headless usage supported; Deep linking enabled but validated `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] Data model and database design enforce tenant isolation; brisante data is classified, owned, and handled by policy `[Effort: High | Cost: Medium | Importance: Essential]`
    - [ ] Data & secrets: vault or secret store, TLS 1.2+ `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] Domain & email trust: valid certificates, SPF, DKIM, DMARC, and monitoring for expiry/spoofing `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] Network: segmentation, WAF, HTTPS `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] SDLC: Shift Left, SAST/SCA (and DAST where applicable), branch protection `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] Testing: unit/integration/e2e, regression tests, and security tests; fuzzing/property-based tests used where risk justifies it `[Effort: High | Cost: Medium | Importance: Essential]`
    - [ ] Staging: promotion flow (build → staging → validate → production); no production data in staging; config documented `[Effort: Medium | Cost: Medium | Importance: Important]`
    - [ ] IaC and system configuration: infra and config in version control; reviewed and applied via pipeline; no secrets in definitions `[Effort: High | Cost: Medium | Importance: Important]`
    - [ ] Good documentation: architecture, APIs, runbooks, ADRs; single source of truth; kept up to date; onboarding path clear `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] Open source: license compliance, SBOM/dependency scanning, vulnerability handling, contribution policy `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] Changelogs & communication: changelog, release notes, clear security/incident communication `[Effort: Low | Cost: Low | Importance: Important]`
    - [ ] Monitoring & alerting; incident response documented `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] CI/CD: no secrets in repo, approvals, scans in pipeline `[Effort: Medium | Cost: Low | Importance: Essential]`
    - [ ] GDPR and data residency considered; German market requirements documented where relevant `[Effort: High | Cost: Medium | Importance: Essential]`
    - [ ] AI-assisted coding policy defined (allowed use, forbidden input, required review/test gates) `[Effort: Low | Cost: Low | Importance: Important]`
    - [ ] Code Quality: Linter/Formatter configured in CI; Architecture patterns (e.g. Hexagonal/Clean) respected `[Effort: Medium | Cost: Low | Importance: Essential]`
    - [ ] Accessibility: WCAG 2.1 AA compliance target; automated a11y tests in pipeline; keyboard navigation verified `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] Performance: Core Web Vitals monitored; caching strategy defined; assets optimized `[Effort: Medium | Cost: Medium | Importance: Important]`
    - [ ] Customer trust requirements captured and mapped to concrete minimum controls `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] Minimum security baseline defined, owned, and reviewed periodically `[Effort: Medium | Cost: Low | Importance: Essential]`
    - [ ] Evidence collection process defined for transparency (not only for formal audits) `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] FinOps: Budgets/Alerts set; Resources tagged; Lifecycle policies active (e.g. storage tiering) `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] Compliance: Shared-responsibility matrix documented; inherited controls mapped `[Effort: Low | Cost: Low | Importance: Important]`

    **Azure**
    - [ ] Entra ID and MFA; least-privilege roles and managed identities; user/group/tenant model documented `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] Secrets in Azure Key Vault; TLS 1.2+ enforced `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] Database/network exposure reduced (private endpoints/firewalls), DB audit logs enabled, and Defender/Policy findings addressed `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] Custom domain, DNS records, and certificate renewal configured and monitored `[Effort: Low | Cost: Low | Importance: Important]`
    - [ ] Private connectivity and/or WAF where appropriate; DDoS considered for production `[Effort: High | Cost: High | Importance: Essential]`
    - [ ] WAF policy tuned (detect -> prevent), with false-positive review process `[Effort: Medium | Cost: Medium | Importance: Important]`
    - [ ] IP/geo restrictions and firewall rules applied where business/security requires `[Effort: Medium | Cost: Medium | Importance: Important]`
    - [ ] Staging: deployment slots or separate staging app; same IaC as production `[Effort: Medium | Cost: Medium | Importance: Important]`
    - [ ] IaC: Bicep/ARM/Terraform in repo; state in secure backend; policies as code `[Effort: High | Cost: Medium | Importance: Important]`
    - [ ] Azure Monitor, Application Insights, and Defender for Cloud in use; alerts configured `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] Defender for Cloud recommendations are triaged with owners, SLAs, and risk-acceptance process `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] Audit logging retained (Activity Log + diagnostics) and regularly reviewed `[Effort: Medium | Cost: Medium | Importance: Essential]`
    - [ ] Deployment via CI/CD with slots and Key Vault references `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] Docs: resource layout, networking, identity, runbooks documented `[Effort: Low | Cost: Low | Importance: Important]`

    **GitHub**
    - [ ] Branch protection, required reviews and status checks; 2FA for org members `[Effort: Low | Cost: Low | Importance: Essential]`
    - [ ] Teams and roles used for access; tenant/customer model (if applicable) documented `[Effort: Low | Cost: Low | Importance: Important]`
    - [ ] GitHub Secrets or OIDC for deployment; no secrets in repo `[Effort: Low | Cost: Low | Importance: Essential]`
    - [ ] Schema/migration changes are reviewed and tested; no real customer DB dumps in repo `[Effort: Low | Cost: Low | Importance: Essential]`
    - [ ] Domain/deployment destination changes are controlled via PR + reviews `[Effort: Low | Cost: Low | Importance: Important]`
    - [ ] Environments (e.g. Staging, Production) with protection rules and required reviewers `[Effort: Low | Cost: Low | Importance: Important]`
    - [ ] CodeQL and Dependabot enabled; security scans in pipeline `[Effort: Low | Cost: Low | Importance: Essential]`
    - [ ] Secret scanning and push protection enabled; optional CI secret scanner (e.g. Gitleaks) integrated `[Effort: Low | Cost: Low | Importance: Essential]`
    - [ ] Branch security: no direct push/force push on protected branches; CODEOWNERS for critical paths `[Effort: Low | Cost: Low | Importance: Essential]`
    - [ ] AI-assisted PRs are flagged and pass the same required checks/reviews as all other changes `[Effort: Low | Cost: Low | Importance: Important]`
    - [ ] Staging/production flow documented (build once, promote artifact, rollback path tested) `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] IaC and config stored in repo; Actions run plan/apply with secure state `[Effort: Medium | Cost: Low | Importance: Important]`
    - [ ] LICENSE, CONTRIBUTING.md, SECURITY.md; README and docs up to date; Releases and CHANGELOG maintained `[Effort: Low | Cost: Low | Importance: Important]`

=== "DE"

    Eine zusammenfassende Checkliste zur Verfolgung der Einhaltung dieser Standards.

    Bewertungsskala:
    - **Aufwand**: `Niedrig` | `Mittel` | `Hoch`
    - **Kosten**: `Niedrig` | `Mittel` | `Hoch`
    - **Wichtigkeit**: `Nice-to-have` | `Wichtig` | `Essentiell`

    **Allgemein**
    - [ ] CIA, Least Privilege, Defense in Depth und **Einfachheit** in Design und Betrieb reflektiert `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] Identität: Zentraler IdP, MFA, Least Privilege, keine Secrets in Config `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Nutzermanagement: Rollen/Gruppen definiert; Mandantentrennung (Tenant Isolation) durchgesetzt `[Aufwand: Hoch | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Schnittstellen: API-First-Ansatz; API dokumentiert; Headless-Nutzung unterstützt; Deep Linking aktiviert aber validiert `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Datenmodell und DB-Design erzwingen Mandantentrennung; brisante Daten klassifiziert und geschützt `[Aufwand: Hoch | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Daten & Secrets: Vault/Secret Store genutzt, TLS 1.2+ `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Domain & E-Mail-Vertrauen: Gültige Zertifikate, SPF, DKIM, DMARC, Monitoring `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Netzwerk: Segmentierung, WAF, HTTPS `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] SDLC: Shift Left, SAST/SCA (ggf. DAST), Branch Protection `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Testing: Unit/Integration/E2E, Regression, Security-Tests; Fuzzing wo nötig `[Aufwand: Hoch | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Staging: Promotion-Flow (Build -> Staging -> Prod); keine Produktionsdaten; Config dokumentiert `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Wichtig]`
    - [ ] IaC & Config: Infra/Config versioniert; via Pipeline reviewt/ausgeführt; keine Secrets im Code `[Aufwand: Hoch | Kosten: Mittel | Wichtigkeit: Wichtig]`
    - [ ] Gute Doku: Architektur, APIs, Runbooks, ADRs; Single Source of Truth; aktuell; Onboarding klar `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Open Source: Lizenz-Compliance, SBOM, Schwachstellen-Handling, Contributing Policy `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Changelogs & Kommunikation: Changelog, Release Notes, klare Vorfallkommunikation `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Monitoring & Alerting; Incident Response dokumentiert `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] CI/CD: Keine Secrets im Repo, Approvals, Scans in Pipeline `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] DSGVO und Datenstandort berücksichtigt; deutsche Marktanforderungen dokumentiert `[Aufwand: Hoch | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] KI-Coding-Richtlinie definiert (erlaubte Nutzung, verbotener Input, Review-Pflicht) `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Code-Qualität: Linter/Formatter in CI; Architekturmuster respektiert `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] Barrierefreiheit: WCAG 2.1 AA Ziel; Auto-Tests in Pipeline; Tastaturnavigation verifiziert `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Performance: Core Web Vitals überwacht; Caching definiert; Assets optimiert `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Wichtig]`
    - [ ] Kundenvertrauensanforderungen erfasst und auf Mindestkontrollen gemappt `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Minimale Sicherheitsbaseline definiert, besessen und periodisch geprüft `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] Nachweissammlungsprozess für Transparenz definiert `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] FinOps: Budgets/Alerts gesetzt; Ressourcen getaggt; Lifecycle-Policies aktiv `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Compliance: Shared-Responsibility-Matrix dokumentiert; geerbte Kontrollen gemappt `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`

    **Azure**
    - [ ] Entra ID und MFA; Least-Privilege-Rollen; Managed Identities; Tenant-Modell dokumentiert `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Secrets im Key Vault; TLS 1.2+ erzwungen `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] DB/Netzwerk-Exponierung reduziert (Private Endpoints), Audit-Logs an, Defender-Funde behoben `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Custom Domain, DNS, Zertifikate konfiguriert und überwacht `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Private Connectivity / WAF wo nötig; DDoS für Produktion erwogen `[Aufwand: Hoch | Kosten: Hoch | Wichtigkeit: Essentiell]`
    - [ ] WAF-Policy getunt (Detect -> Prevent); False-Positive-Prozess `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Wichtig]`
    - [ ] IP/Geo-Beschränkungen angewandt wo nötig `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Wichtig]`
    - [ ] Staging: Deployment Slots oder separate App; gleiches IaC wie Prod `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Wichtig]`
    - [ ] IaC: Bicep/Terraform im Repo; sicheres State-Backend; Policy as Code `[Aufwand: Hoch | Kosten: Mittel | Wichtigkeit: Wichtig]`
    - [ ] Monitor, App Insights, Defender genutzt; Alerts konfiguriert `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Defender-Empfehlungen triagiert mit Owner/SLA `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Audit-Logging aufbewahrt und geprüft `[Aufwand: Mittel | Kosten: Mittel | Wichtigkeit: Essentiell]`
    - [ ] Deployment via CI/CD mit Slots und Key Vault Referenzen `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Doku: Ressourcenlayout, Netzwerk, Identität, Runbooks `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`

    **GitHub**
    - [ ] Branch Protection, Reviews, Statuschecks; 2FA für Org `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] Teams/Rollen genutzt; Tenant-Modell dokumentiert `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] GitHub Secrets oder OIDC; keine Secrets im Repo `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] Schema/Migrationsänderungen reviewt/getestet; keine Kundendumps im Repo `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] Domain/Deployment-Zieländerungen via PR kontrolliert `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Environments (Staging/Prod) mit Schutzregeln `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] CodeQL & Dependabot aktiv; Scans in Pipeline `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] Secret Scanning & Push Protection aktiv; CI-Scanner integriert `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] Branch-Sicherheit: kein direkter Push auf Protected Branches; CODEOWNERS für kritische Pfade `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Essentiell]`
    - [ ] KI-PRs geflaggt und geprüft `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] Staging/Prod-Flow dokumentiert (Build Once) `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] IaC/Config im Repo; Actions führen Plan/Apply sicher aus `[Aufwand: Mittel | Kosten: Niedrig | Wichtigkeit: Wichtig]`
    - [ ] LICENSE, CONTRIBUTING, SECURITY, README aktuell; Releases/Changelog gepflegt `[Aufwand: Niedrig | Kosten: Niedrig | Wichtigkeit: Wichtig]`
