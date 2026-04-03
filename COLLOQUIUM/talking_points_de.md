# PhD-Verteidigung Präsentation - Stichpunkte Leitfaden

**Bolometrie-Diagnostik und Echtzeit-Strahlungsrückkopplungskontrolle am Wendelstein 7-X**

---

## TITELFOLIE

- Willkommen zu meiner PhD-Verteidigung über Bolometrie-Diagnostik und Echtzeit-Strahlungsrückkopplungskontrolle am Wendelstein 7-X
- Diese Arbeit adressiert zwei kritische Herausforderungen für zukünftige Fusionsreaktoren: (1) Schutz plasmazugewandter Komponenten durch kontrollierte Strahlung, und (2) Erreichen stabiler Ablösung bei hohen Strahlungsfraktionen (f_rad≥85%)
- Drei Hauptbeiträge: Implementierung des ersten bolometer-basierten Echtzeit-Feedbacks am W7-X, Optimierung der Kanalauswahl durch systematische Sensitivitätsanalyse, und Validierung der MFR-Tomographie mit radial abhängiger Anisotropie-Gewichtung

---

## INHALTSVERZEICHNIS

- Präsentationsstruktur: (1) Motivation - Fusionsenergie und W7-X-Herausforderungen, (2) Bolometer-Diagnostiksystem - 94 Kanäle mit ~5cm räumlicher Auflösung, (3) Echtzeit-Feedback - erreichte f_rad≥85% mit Faktor ≥2 Wärmelast-Reduktion, (4) LOS-Sensitivität - identifizierte optimale Kanalkonfigurationen, (5) Tomographie - MFR mit RDA für 2D-Strahlungsrekonstruktion, (6) Schlussfolgerungen und zukünftige Arbeiten

---

## MOTIVATION

### Kernfusion: Energieherausforderung

- Kernfusion durch D-T-Reaktionen bietet saubere, reichlich vorhandene Energie - Deuterium aus Meerwasser, Tritium gezüchtet aus Lithium
- Lawson-Kriterium: n_e·τ_E·T ≥ 3×10²¹ keV·s/m³ definiert Bedingungen für Netto-Energiegewinn (Q>1)
- Erfordert extreme Bedingungen: T~10-20 keV (100-200 Millionen °C) und Einschlusszeit τ_E~1-10s
- Magnetischer Einschluss nutzt starke Felder (2,5T am W7-X), um heißes Plasma von Materialwänden fernzuhalten
- Stellaratoren wie W7-X erreichen Dauerstrichbetrieb durch 3D-geformte Spulen, im Gegensatz zu gepulsten Tokamaks

### Wendelstein 7-X

- W7-X ist der weltweit größte und fortschrittlichste Stellarator: R=5,5m, a=0,53m, B=2,5T, optimiert für Dauerstrichbetrieb
- Hauptherausforderung: Management der Wärmelasten auf plasmazugewandten Komponenten während langer Pulse (bis zu 30 Minuten geplant)
- Inseldivertor-Konzept: 5 helikale Inselketten fangen Wärmefluss ab, Verbindungslängen 100-1000m (10-100× länger als Tokamaks)
- Ablösungsstrategie: Leistung in Abschälschicht und Rand abstrahlen, um Divertor-Wärmelasten von ~10 MW/m² auf <5 MW/m² zu reduzieren
- Ziel: stabile Ablösung bei f_rad≥85-90% ohne Plasmadisruption erreichen, während Kernleistung erhalten bleibt
- Dies erfordert Echtzeitkontrolle der Strahlungsverteilung - Motivation für Bolometer-Feedbacksystem

### Plasmastrahlung

- Plasmastrahlungsmechanismen: (1) Bremsstrahlung (frei-frei-Übergänge, ~T_e^(1/2)), (2) Linienstrahlung (gebunden-gebunden, temperaturabhängig), (3) Rekombination (frei-gebunden)
- Verunreinigungseinspeisung-Strategie: Injektion von niedrig-Z (N₂) oder hoch-Z (Ne, Ar) Gasen zur Verstärkung der Randstrahlung bei Vermeidung von Kernkontamination
- Kohlenstoff und Sauerstoff sind intrinsische Verunreinigungen aus Wandwechselwirkungen - Kohlenstoff dominiert um Faktor 10²× über Sauerstoff am W7-X
- Strahlungskühlungsfunktion P_rad/(V·n_e·n_imp) hat Maxima bei unterschiedlichen Temperaturen für jede Verunreinigung: C Maximum ~10-50 eV (Rand), O Maximum ~100 eV
- Transport am W7-X: neoklassische Basislinie mit anomalen Beiträgen von Turbulenz (ITG, TEM-Moden)
- Anomaler Transport erhöht Diffusion um Faktor 10-100 über neoklassisch, kritisch für Verunreinigungstransport-Modellierung
- Strahlungsfraktion f_rad = P_rad/P_ECRH muss ausbalanciert sein: f_rad<70% unzureichend für Divertorschutz, f_rad>95% riskiert Kernkühlung und Einschlussdegradation
- Optimales Betriebsfenster: f_rad=85-90% erreicht Ablösung bei Erhalt der Plasmastabilität

---

## KERN-BOLOMETER AM W7-X

### Bolometer-Diagnostik (Hardware)

- Bolometer messen totale Plasmastrahlungsleistung (breitbandig, 0,2-600 nm) durch resistive Heizung von Metallabsorbern
- Metallwiderstand-Design: dünner Goldfilm (1,5 μm) auf Glimmersubstrat, absorbiert Strahlung → Temperaturerhöhung → Widerstandsänderung
- Wheatstone-Brücken-Konfiguration: AC-Anregung (5V, kHz) eliminiert 1/f-Rauschen, differentielle Messung verdoppelt Signal
- Drei Kamera-Arrays bieten umfassende Plasmaabdeckung: HBC (32 Kanäle, horizontal), VBCl/r (2×31 Kanäle, vertikal)
- Insgesamt 94 Kanäle installiert, 61 funktional in OP1.2b-Kampagne (einige beschädigt durch ECRH-Streustrahlung)
- Jeder Kanal integriert Strahlung entlang der Sichtlinie - nutzt Geometriematrix T und Etendue K_M zur Rekonstruktion der 2D-Verteilung
- Räumliche Auflösung ~5 cm an magnetischer Achse, bestimmt durch Etendue-Breite und Beobachtungsgeometrie

### Leistung

- Kalibrierung ist kritisch für absolute Leistungsmessungen - drei Methoden verwendet: (1) Laser, (2) elektrische ohmsche Heizung, (3) in-situ während Betrieb
- In-situ ohmsche Heizungskalibrierung: U_cal=1,2-2,5V für 1,6s anlegen, Stromevolution I(t) messen, R_M, τ_M, κ_M aus exponentiellem Abfall extrahieren
- Kalibrierungsparameter (OP1.2b Median): R_M=0,987±0,011 Ω, κ_M=0,724±0,055 A², τ_M=110,57±4,93 ms, bemerkenswert stabil über 1182 Experimente
- Etendue K_M quantifiziert geometrische Lichtsammeleffizienz: berücksichtigt Detektor-Apertur-Geometrie, partielle Abschattung, winkelabhängige Transmission
- Zeitauflösung konfigurierbar: {0,4, 0,8, 1,6, 3,2, 6,4, 12,8} ms Abtastung verfügbar, 1,6ms für Feedback verwendet (balanciert Geschwindigkeit vs Rauschen)
- Leistungsmetriken: SNR>1000 bei hoher Strahlung, Rauschen σ_ΔU=0,339±12,586 μV, Gauß-Fehler 1,6 μW, Drift 0,057±27,621 μV/s
- Sehnen-Helligkeit P_ch = P_M/K_M liefert radiale Profilinformation - zeigt Strahlungsverteilung von Kern bis SOL
- Absorptionseffizienz nahe Einheit (>95%) über 0,2-600 nm Wellenlängenbereich - wahrhaft breitbandige Messung

---

## ECHTZEIT-FEEDBACK

### Inseldivertor-Konfiguration

- W7-X nutzt Inseldivertor-Konzept: 5 helikale Inselketten (m/n=5/5 Moden) bilden natürliche Divertor-Ziele, 10 Divertor-Module insgesamt
- Verbindungslängen L_c=100-1000m (10-100× länger als Tokamaks) ermöglichen effiziente Strahlungskühlung entlang Feldlinien
- Standardkonfiguration: Rotationstransformation ι/2π=1 an magnetischer Achse, optimiert für Einschluss
- Gaseinspeisung: 10 Piezoventile für präzise Kontrolle, Heliumstrahlventile für schnelle Injektion (Antwortzeit ~50ms)
- X-Punkte sind Strahlungs-Hotspots: Faktor 2-5× höhere Emissivität aufgrund von Verunreinigungsakkumulation und niedrigen Temperaturen
- Bolometer-Kameras strategisch auf X-Punkte ausgerichtet für optimale Sensitivität gegenüber Ablösungsübergängen

### System-Implementierung

- Erste bolometer-basierte Feedback-Implementierung am W7-X (OP1.2b-Kampagne, 2018) - vorherige Systeme nutzten Interferometrie
- Hardware: NI 6321 DAQ-Karte (16-bit, 250 kS/s), PID-Regler in LabVIEW implementiert, parallele Verarbeitung für niedrige Latenz
- Zwei Vorhersage-Proxies entwickelt: P_pred^(1) geometriegewichtet (nutzt mehrere Kanäle mit räumlichen Gewichten), P_pred^(2) Einzelkanal (einfachste Implementierung)
- Optimale Kanalauswahl: VBC S={61,65,73,78,86} erreicht ≥85% Vorhersagegenauigkeit für P_ECRH, beobachtet Separatrix/SOL-Region
- Alternative Konfiguration: HBC S={4,7,8,20,23,27} für horizontale Abdeckung, nützlich wenn VBC-Kanäle ausfallen
- PID-Parameter: K_p=0,5-2,0 (proportionale Verstärkung), K_i=0,1-0,5 (integrale Verstärkung), K_d=0 (keine derivative Aktion - zu rauschempfindlich)
- Sollwert: f_rad^target=85-90% balanciert Divertorschutz (erfordert ≥85%) gegen Kernkühlung-Risiko (vermeidet >95%)

### Latenz-Analyse

- Akquisitionslatenz: 13,6ms minimal (1,6ms Abtastung + 12ms Verarbeitung), gemessen durch Laserdioden-Validierung
- FIFO-Glättung: ~8ms zusätzliche Verzögerung (M=10 Samples × 1,6ms Abtastperiode) reduziert Rauschen
- Gesamtschleifenlatenz: 150-400ms (plasmadominiert durch Gasventil-Antwort ~50-200ms und Verunreinigungstransport ~100-300ms)
- Abtastrate-Kompromiss: 1,6ms optimal balanciert Geschwindigkeit (schnelle Antwort) vs Rauschen (höhere Abtastraten verstärken Rauschen)
- Laserdioden-Validierung: 13,6ms Akquisitionslatenz experimentell bestätigt durch kontrollierte Lichtpulse
- Zukünftige Verbesserungen: <10ms Akquisition möglich mit Hardware-Upgrade, prädiktive Algorithmen könnten Gesamtlatenz auf ~50-100ms reduzieren

### XP20181010.32 Erfolge

- Durchbruch-Experiment: Erste stabile Ablösung mit Wasserstoff-Einspeisung (vorherige Versuche nutzten Neon/Stickstoff)
- Dauer: 9,2s Feedback-Kontrolle, P_ECRH=6,23 MW, Gesamtenergie 55 MJ in Plasma deponiert
- Strahlungsfraktion: f_rad≥85% anhaltend aufrechterhalten, Spitzen bis 100% während Ablösungsübergängen
- Wärmelast-Reduktion: Faktor ≥2× erreicht (von ~10 MW/m² auf <5 MW/m²), kritisch für Divertor-Lebensdauer
- C²⁺-Spektroskopie-Signatur: Erscheint ab f_rad~50%, zeigt Beginn der Ablösung, vollständige Ablösung bei f_rad>90%
- Vorhersagegenauigkeit: P_pred^(1) verfolgt P_rad innerhalb 10-15% über gesamte Entladung, validiert Proxy-Konzept
- Plasmaenergie: W_dia~0,8-1,0 MJ trotz hoher Strahlung aufrechterhalten, zeigt Kernleistung erhalten bleibt
- Reaktorrelevanz: Demonstriert Szenario anwendbar auf ITER/DEMO - hohe Strahlung ohne Einschlussdegradation

### Diskussion

- **Bolometer-Vorteile:** Direkte P_rad-Messung (keine Modellannahmen), breitbandig (alle Wellenlängen), schnell (1,6ms Zeitauflösung)
- **Robustheit:** Unabhängig von Verunreinigungsmix (misst totale Strahlung), funktioniert mit C, N₂, Ne, Ar-Einspeisung
- **Räumliche Information:** Kanäle unterscheiden Kern vs Rand vs SOL-Strahlung, ermöglicht gezielte Kontrolle
- **Physikalische Verbindung:** Strahlung IST der Ablösungsmechanismus - direkteste mögliche Messung für Feedback
- **Gasinjektions-Optimierung:** 50-200ms Ventil-Antwortzeit optimal für Plasma-Zeitskalen, schneller würde Rauschen verstärken
- **PID-Tuning-Herausforderung:** Parameter entladungsspezifisch, komplex zu optimieren, erfordert Erfahrung oder ML-Ansätze
- **Latenz-Limitierung:** 150-400ms Gesamtschleife begrenzt Bandbreite auf ~2-5 Hz, ausreichend für Ablösungskontrolle
- **Zukünftige Verbesserungen:** <10ms Akquisition möglich, prädiktive Kontrolle könnte Latenz kompensieren, ML für automatisches PID-Tuning
- **Direkteste Methode:** Bolometer-Feedback ist direkteste verfügbare Methode für Strahlungskontrolle - keine Zwischenmodelle erforderlich
- **Breite Anwendbarkeit:** Konzept direkt anwendbar auf ITER, DEMO, und zukünftige Stellaratoren - universelle Lösung

---

## LOS-SENSITIVITÄT

### LOS-Sensitivität (Motivation)

- Zentrale Frage: Welche Bolometer-Kanäle sind am sensitivsten für Plasmaparameteränderungen und warum?
- Ziel: Optimale Kanalauswahl für (1) Echtzeit-Feedback-Kontrolle und (2) Tomographie-Rekonstruktion identifizieren
- Datensatz: 45 Entladungspaare aus OP1.2b, Parameterbereich P_ECRH=3,5-6,5 MW, f_rad=0,3-1,0, verschiedene Verunreinigungen (N₂, Ne)
- Sechs Evaluierungsmetriken entwickelt, um verschiedene Aspekte der Kanalsensitivität zu quantifizieren
- Systematischer Ansatz: Kanal-für-Kanal-Vergleich über alle Entladungspaare, räumliche Kartierung der Sensitivität

### Methodik

- Sechs Metriken definiert: (1) Korrelation ρ_c (lineare Beziehung), (2) gewichtete Abweichung σ_w (zeitgewichteter Fehler), (3) mittlere Abweichung σ_m (durchschnittlicher Fehler)
- Fortsetzung: (4) FFT-Korrelation ρ_FFT (Frequenzbereichsähnlichkeit), (5) Fisher-Information I_F (Informationsgehalt), (6) χ² (Anpassungsgüte)
- Analyse-Workflow: Für jedes Entladungspaar, berechne alle Metriken für jeden Kanal, aggregiere über Paare, identifiziere konsistente Muster
- Räumliche Kartierung: Sensitivität vs. ρ_pol (normalisierter poloidaler Fluss) zeigt, wo Kanäle beobachten
- Optimale Kanalanzahl: Systematische Variation m=1-20 zeigt m=3-5 ausreichend für Feedback (Kompromiss zwischen Redundanz und Komplexität)
- Hauptergebnis: Separatrix/SOL-beobachtende Kanäle (ρ_pol~0,95-1,05) zeigen höchste Sensitivität über alle Metriken

### Ergebnisse

- Beste Kanäle identifiziert: VBC S={61,65,73,78,86} (beobachten Separatrix/SOL-Region), HBC S={4,7,8,20,23,27} (Rand-Fokus)
- Sensitivität korreliert stark mit Strahlungsgradienten - Kanäle, die Regionen mit steilen ∂P_rad/∂ρ beobachten, sind am sensitivsten
- Kernkanäle (ρ_pol<0,8) zeigen niedrigere Sensitivität aufgrund flacher Strahlungsprofile - weniger Information über Plasmaänderungen
- Randkanäle (ρ_pol~0,95-1,05) optimal für Feedback - erfassen Verunreinigungstransport und Strahlungsänderungen zuerst
- Validierung: Experimentelle Feedback-Leistung mit ausgewählten Kanälen bestätigt Vorhersagen - stabile f_rad-Kontrolle erreicht

---

## TOMOGRAPHIE

### Tomographie (Motivation)

- Ziel: 2D-Strahlungsverteilung P_rad(R,Z) aus 1D-Sehnen-Helligkeitsmessungen rekonstruieren
- Herausforderung: Unterbestimmtes inverses Problem - 61 Messungen, ~4500 Gitterzellen, unendlich viele Lösungen möglich
- Lösung: Minimum Fisher Regularization (MFR) mit radial abhängiger Anisotropie-Gewichtung (RDA)
- MFR-Prinzip: Maximiere Entropie (Glätte) bei Erfüllung von Datenkonstraints - bevorzugt physikalisch plausible Lösungen
- Validierung durch (1) synthetische Phantome mit bekannter Wahrheit und (2) experimentelle Daten mit unabhängigen P_rad-Messungen

### MFR mit RDA

- Gitter-Konfiguration: 30×150 Zellen (radial×poloidal), Domäne 1,3²V_P umfasst Plasma + SOL + Divertor
- Anisotropie-Gewichtung: k_ani(ρ) variiert radial - {2,0, 0,3} Standard (Kern anisotrop, Rand isotrop), {5,0, 0,5} hochanisotrop (starke Flussflächenausrichtung)
- Physikalische Motivation: Strahlung folgt Flussflächen im Kern (anisotrop), wird isotrop im SOL/Divertor (kurze Verbindungslängen)
- Konvergenz: N_T=10-20 Iterationen ausreichend für χ²<1,5, typisch ~15 Iterationen für experimentelle Daten
- Regularisierung: Glättung entlang Flussflächen im Kern, isotrope Glättung im Rand - balanciert Physik und Datenkonstraints
- Implementierung: Python mit NumPy/SciPy, optimiert für Geschwindigkeit (~1s pro Rekonstruktion), parallelisierbar für Echtzeit

### Validierung

- Phantom-Benchmarks: 59 synthetische Tests mit verschiedenen Strahlungsmustern (Kern-dominiert, Rand-dominiert, gemischt)
- Phantom-Leistung: Rekonstruktionsqualität ρ_c>0,85 (Korrelation mit Wahrheit), χ²<2,5 (Anpassungsgüte), typisch ρ_c~0,90-0,95
- Experimentelle Tests: 4 Entladungen aus OP1.2b, P_2D (integriert über Gitter) innerhalb 10-20% von P_rad (unabhängige Messung)
- Vergleich mit anderen Methoden: MFR+RDA übertrifft Standard-MFR (isotrop) und Tikhonov-Regularisierung - bessere räumliche Auflösung und Genauigkeit
- Räumliche Auflösung: ~5cm an magnetischer Achse, begrenzt durch Bolometer-Kanalgeometrie und Etendue-Breite
- Robustheit: Stabil gegen Rauschen (SNR>100), fehlende Kanäle (bis zu 30% Ausfall), und Kalibrierungsfehler (±10%)
- ~2-5s/Frame CPU, GPU könnte <100ms
- Zukunft: Echtzeit-Tomographie möglich

---

## SCHLUSSFOLGERUNGEN

### Haupterfolge

- Drei Hauptbeiträge bilden ein integriertes System für W7-X-Strahlungsmanagement:
- (1) Echtzeit-Feedback: Erste bolometer-basierte Implementierung am W7-X, erreichte f_rad≥85% mit Faktor ≥2× Divertor-Wärmelast-Reduktion
- (2) LOS-Optimierung: Systematische Analyse von 45 Entladungspaaren identifizierte optimale Kanalauswahl, m=3-5 Kanäle ausreichend für robuste Kontrolle
- (3) Tomographie: MFR+RDA-Methode validiert durch 59 Phantom-Tests und 4 experimentelle Entladungen, liefert 2D-Strahlungsverteilung
- Integration: Feedback-System nutzt optimierte Kanäle aus LOS-Analyse, Tomographie validiert räumliche Strahlungsverteilung
- Reaktorrelevanz: Direkt anwendbar auf ITER und DEMO für Divertorschutz und Langpuls-Operationen

### Zusammenfassung

- **Feedback-System:** 13,6ms Akquisitionslatenz (minimal), 150-400ms Gesamtschleife, PID-Regler mit dual-Proxy-Vorhersage
- **Benchmark-Experiment:** XP20181010.32 - 9,2s Dauer, P_ECRH=6,23 MW, f_rad≥85% aufrechterhalten, Faktor ≥2× Wärmelast-Reduktion, keine Disruption
- **Diagnostik-Leistung:** 94 Kanäle installiert (61 funktional in OP1.2b), Kalibrierungsstabilität <5% über 1182 Experimente, SNR>1000
- **LOS-Sensitivität:** Separatrix/SOL-beobachtende Kanäle (ρ_pol~0,95-1,05) optimal, VBC übertrifft HBC für Randsensitivität, mehrere Kanal-Sets erreichen ≥85% Genauigkeit
- **Ablösungsphysik:** C²⁺-Signatur erscheint bei f_rad~50%, vollständige Ablösung bei f_rad>90%, kritische Region bei ρ_pol≈0,95
- **STRAHL-Modellierung:** Kohlenstoff dominiert um Faktor 10²× über Sauerstoff, C³⁺/C²⁺-Verhältnis kritisch an LCFS für Strahlungsverteilung
- **Tomographie-Qualität:** Rekonstruktionen erreichen ρ_c>0,85, χ²<2,5, P_2D innerhalb 10-20% von P_rad, zeigen X-Punkt-Lokalisierung und Inselketten-Struktur
- **Leistungsbilanz:** P_2D^(Kern) stabil für quasi-stationäre Phasen, Standard-MFR unterschätzt um 15-25% (SOL-Beitrag fehlt)
- **Validierung:** OP1.2b-Kampagne 2018, 1182 Experimente analysiert, 45 Entladungspaare für LOS-Studie, 4 für Tomographie-Validierung

---

## AUSBLICK

### Zukünftige Arbeiten

- **Hardware-Upgrades:** (1) Akquisitionssystem-Upgrade auf <10ms Latenz für schnellere Feedback-Antwort, (2) Erweiterte Kanalabdeckung für bessere räumliche Auflösung
- **Software-Verbesserungen:** Prädiktive Algorithmen zur Antizipation von Strahlungsänderungen, maschinelles Lernen für adaptive Kontrolle
- **ML-Anwendungen:** (1) PID-Parameter-Optimierung für verschiedene Plasmaregime, (2) automatische Kanalauswahl basierend auf Plasmazustand, (3) Gas-Injektions-Timing-Optimierung
- **Modellierungs-Validierung:** STRAHL+EMC3-EIRENE 3D-Kopplung für vollständige Verunreinigungstransport-Simulation, Validierung gegen OP2.1-Daten
- **Kammermodelle:** Verfeinerung von Zwei/Drei-Kammer-Modellen für Verunreinigungstransport, Entwicklung von Skalierungsgesetzen für verschiedene Betriebsregime
- **Tomographie-Erweiterung:** Erweiterte Phantom-Bibliothek (>50 Tests), GPU-Beschleunigung für <100ms/Frame-Rekonstruktion
- **Echtzeit-Tomographie:** Integration in Feedback-System für räumliche Strahlungskontrolle, MARFE-Früherkennung und -Vermeidung
- **Parameter-Optimierung:** Bayes'sche Optimierung oder Gittersuche für k_ani(ρ)-Profil, adaptive Anisotropie basierend auf Plasmazustand
- **ITER/DEMO-Anwendung:** Direkt übertragbare Methoden, P_fus~500 MW, f_rad≥95% erforderlich, q_div<10 MW/m² Ziel
- **Andere Geräte:** Anwendbar auf LHD (Stellarator), ITER, DEMO, SPARC (Tokamaks) - universelle Strahlungskontroll-Strategie
- **Vision:** Vollautomatisches, adaptives, prädiktives Strahlungsmanagement-System für zukünftige Fusionsreaktoren

---

## ABSCHLUSS

### Danksagung

- Vielen Dank für Ihre Aufmerksamkeit - "Sin é, a chairde" (Irisch-Gälisch: "Das ist es, Freunde")
- Fragen sind willkommen zu allen Aspekten: Feedback-Implementierung, LOS-Sensitivitätsanalyse, Tomographie-Methodik, experimentelle Ergebnisse
- Diskussionsthemen: (1) Latenzreduktions-Strategien, (2) alternative Regularisierungsmethoden, (3) Parameter-Optimierungsansätze, (4) ITER/DEMO-Anwendbarkeit
- Danksagung: W7-X-Betriebsteam, IPP-Greifswald-Kollegen, EUROfusion-Konsortium, Helmholtz-Gemeinschaft, Universität Greifswald

---

## BACKUP-FOLIEN - Übersicht

- Backup-Folien liefern detaillierte technische Information für tiefgehende Fragen
- Abgedeckte Themen: Plasmaphysik, STRAHL-Modellierung, Diagnostik-Details, LOS-Sensitivitätsmetriken, Tomographie-Vergleiche, DAQ-Latenz
- Verfügbar, um spezifische Fragen zu Methodik, Implementierungsdetails oder alternativen Ansätzen zu adressieren

---

*Ende des Hauptpräsentations-Leitfadens*

---

# DETAILLIERTE BACKUP-FOLIEN STICHPUNKTE

## PLASMAPHYSIK

### Plasmatransport am W7-X
- Drei Transportmechanismen: klassisch, neoklassisch, anomal
- W7-X-Optimierung für niedrige Kollisionalitätsregime
- Anomaler Transport dominiert um Größenordnung
- Verunreinigungstransport ladungsabhängig

### Verunreinigungstransport und Strahlung
- Anomale Diffusion D_an~0,3-3 m²/s dominiert
- Neoklassische Konvektion erzeugt Einwärts-Pinch für hoch-Z
- DEMO-Ziel: f_rad>0,95 mit 70/30 Kern/SOL-Aufteilung
- Kontrollherausforderung: Balance Schutz vs Einschluss

### Plasmaverunreinigungen
- Kohlenstoff dominant: 10²× höher als Sauerstoff
- Ionisationsstufen variieren mit Temperatur
- Strahlungsverteilung entwickelt sich mit f_rad
- Kern/SOL-Umkehr bei hoher f_rad

### Verunreinigungseffekte und Transportsensitivität
- Brennstoffverdünnung beeinflusst Lawson-Kriterium
- Diffusionssensitivität: 120% Spitzenanstieg mit niedrigerem D
- Separatrix-Profil kritisch für Ablösung
- STRAHL validiert experimentelle Trends

### Plasmaablösung
- Schwelle: T_e < 5 eV am Target
- Volumetrische Verluste dominieren
- Strahlungsverstärkungs-Rückkopplungsschleife
- W7-X erreichte f_rad=100% Ablösung

## MODELLIERUNG & ANALYSE

### Verunreinigungseinspeisung-Modelle
- Zwei-Kammer- und Drei-Kammer-Modelle
- Erfassen grundlegende Zeitskalen: Wand, Plasma, SOL
- R²>0,85 Korrelation mit Experimenten
- Zukunft: Integration mit 3D-Codes

### Plasma-Leistungsbilanz
- Energieerhaltung: P_bal ≈ 0
- Kombinierte Unsicherheiten ±1-2 MW
- Gefäßwärmelast 15-25% von P_rad
- Tomographie verbessert Stabilität

## DIAGNOSTIK-DETAILS

### Detektorsensitivität: Etendue
- K̃_M quantifiziert Lichtsammeleffizienz
- Einheiten: mm⁻³ (inverse Volumen)
- Räumliche Auflösung ~4-5 cm an Achse
- Kritisch für absolute Leistungsmessungen

### Temperaturdrift-Einfluss
- Hauptsystematischer Fehler in langen Pulsen
- Graukörperstrahlung skaliert mit T⁴
- Lineare Korrektur für langsame Drifts
- Zukunft: temperaturabhängige Kalibrierung

### In-Situ-Kalibrierung
- Essentiell wegen ±5-10% Variationen
- Drei Parameter: R_M, τ_M, κ_M
- OP1.2b: außergewöhnliche Stabilität über 1182 Experimente
- Kabelkorrektur verhindert systematische Fehler

### Detektorleistungs-Statistiken
- SNR>1000 bei hoher Strahlung
- Rauschen: 0,339±12,586 μV
- Minimale Degradation beobachtet
- Erfüllt alle fusionsgerechten Anforderungen

### Bolometer-Gleichungs-Ableitung
- AC-Anregung entfernt 1/f-Rauschen
- Wheatstone-Brücke: ΔU ∝ ΔR_M
- Leistungsbilanz: Heizung vs Kühlung
- Trade-off: τ und κ invers verwandt

### Messalgorithmus
- Drei Stufen: Initialisierung, Kalibrierung, Messung
- Echtzeit-Feedback via NI 6321 DAQ
- FIFO-Puffer verhindert Datenverlust
- Latenzoptimierung: 13,6ms Minimum

## STRAHL-MODELLIERUNG

### STRAHL-Grundlagen
- 1D-Verunreinigungstransport-Code
- Flussflächen-gemittelte Größen
- Zeitabhängige Evolution
- Löst Kontinuität für jedes Z

### STRAHL-Verunreinigungstransport-Modellierung
- Leitende Gleichung mit D und v
- Kohlenstoffdominanz validiert
- Kritische Ladungszustände: C³⁺/C²⁺
- Strahlungsverschiebung mit f_rad

### STRAHL-Parametervariationen
- Systematische Sensitivitätsstudie
- Kernstrahlung stabil ±10%
- Rand variiert ±30-50%
- C³⁺/C²⁺ am empfindlichsten

### STRAHL: Strahlungsfraktions-Abhängigkeit
- f_rad=90% vs 100% Vergleich
- Spitze verschiebt sich von SOL zu LCFS
- Kern/SOL-Verhältnis ändert sich 0,3→0,7
- Validiert Feedback-Kanalauswahl

## LOS-SENSITIVITÄTS-DETAILS

### Kamerageometrie-Sensitivität
- Aperturpositionierungs-Unsicherheiten
- Vorwärtsmodellierung <1% Unterschied
- Fertigungstoleranzen akzeptabel
- Validiert Ingenieurdesign

### Segmentierung und Sichtlinien-Kegel
- N=8 optimal für Genauigkeit vs Berechnung
- Voller Kegel vs infinitesimale Projektion
- Richtige Segmentierung essentiell
- Jedes Segment gewichtet durch Etendue

### Tomographie: RDA vs RGS Vergleich
- RDA: absolute Differenzen, erhält Gradienten
- RGS: relative Gradienten, verstärkt Merkmale
- RDA gewählt für Robustheit
- RGS nützlich für Post-Shot-Analyse

### Tomographie: Künstliche Kameras
- VBCm und MIRh konzeptuelle Designs
- 4-Kamera verbessert um 15-20%
- Trade-off: Kosten vs Verbesserung
- Aktuelle 3-Kamera ausreichend

### Phantom-Tomographie: Grenzfälle
- Invertierte Anisotropie testet Grenzen
- Homogene Verteilung validiert keine Artefakte
- Grenzfälle offenbaren Beschränkungen
- Leiten Betriebsparameter

### LOS-Sensitivitätsbewertung (Kreuzkorrelation)
- Zeitliche Ähnlichkeitsmetrik
- Große Fehlerbalken: ±40%
- X-Punkt-Kanäle am schlechtesten
- Kritisch für Echtzeitkontrolle

### LOS-Sensitivitätsbewertung (Mittlere Abweichung)
- Varianz-basierte Qualität
- Fehlerbalken 10× größer als gewichtet
- Kernkanäle konsistent
- Rand optimal für Feedback

### LOS-Sensitivitätsbewertung (FFT-Korrelation)
- Spektralanalyse-Ansatz
- Identifiziert oszillatorisches Verhalten
- Ergänzt Zeitbereich
- Leitet Reglerentwurf

### LOS-Sensitivität: Plasmaparameter
- P_ECRH-Korrelation: höher besser
- Optimale f_rad: 0,4-0,75
- T_e~1,3 keV ideal
- Validiert hohe f_rad-Szenarien

### DAQ-Latenz
- Laser-basierte Charakterisierung
- Abtastzeiten: 0,8-3,2ms getestet
- Minimum: 13,6ms erreicht
- Totale Schleife: 150-400ms ausreichend

---

**Dokument für PhD-Verteidigung vorbereitet**
**Gesamt-Abschnitte: 60+ Frames mit umfassenden Stichpunkten**
**Nutzen Sie diesen Leitfaden für konsistente Botschaften und technische Genauigkeit während der gesamten Präsentation**