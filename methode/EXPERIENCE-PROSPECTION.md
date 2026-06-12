# Expérience de prospection — quel segment attaquer en premier ?

> Démarche **scientifique** (expérience contrôlée) pour décider, *avec des données et pas à l'intuition*,
> quel(s) segment(s) prospecter en priorité pour la vente de sites web aux professions juridiques (et au-delà).
> Auteur : Benjamin Delpech. Statut : **conception (ce soir) — aucun contact encore.**

## 1. Hypothèse

> Le **score d'opportunité** d'un prospect (= facilité à lui vendre une refonte = gravité de son site ×
> accessibilité du décideur × capacité à payer × levier) **varie selon le segment**.
> Un (ou deux) segment(s) domine(nt) et mérite(nt) la priorité de prospection.

Sous-hypothèses à tester :
- H1 — Les **mandataires/administrateurs judiciaires** ont le meilleur **levier « chaleur »** (intro via maman / réseau CNAJMj) mais un faible **potentiel récurrent** (désignés, pas d'upsell pub).
- H2 — Les **avocats / notaires / experts-comptables** ont un meilleur **potentiel récurrent** (choisis → upsell pub/SEO) mais une chaleur plus faible.
- H3 — Les **PME locales** ont la **gravité de site** la plus forte (sites les plus datés) → argument facile, mais hors moat juridique.

## 2. Variables

| Rôle | Variable |
|---|---|
| **Indépendante** (ce qu'on fait varier) | **Segment** : 5 niveaux — Mandataires/admin. judiciaires · Avocats · Notaires · Experts-comptables · PME locales |
| **Contrôlées** (identiques pour tous) | La **même grille** de scoring · le **même évaluateur** (toi) · **n égal** par segment · **mêmes critères d'inclusion** · même fenêtre de temps |
| **Dépendante — ce soir** | **Score d'opportunité /12** (proxy de « facilité à argumenter ») |
| **Dépendante — plus tard** | Taux de prise de **RDV**, puis taux de **signature** (la vraie mesure) |
| **Covariable** à noter | **Région** (France / Genève-local) — pour ne pas confondre « segment » et « géographie » |

## 3. Biais à neutraliser (le cœur de la rigueur)

- **Biais de sélection** (cherry-picker uniquement les pires sites pour se rassurer) → **critères d'inclusion figés AVANT** de chercher ; tirage le plus représentatif possible du segment.
- **Biais de confirmation** (noter plus sévèrement le segment qu'on aime moins) → grille à **items objectifs 0-2** ; idéalement scorer **sans regarder le segment** (masquer la colonne) puis révéler.
- **Biais / dérive d'évaluateur** → grille avec **définitions écrites** de chaque score, tout scoré dans **la même session**.
- **Échantillon déséquilibré** → **même n par segment** (recommandé : **5 prospects × 5 segments = 25**).
- **Confondant géographique** → région notée en covariable ; éviter que « PME locales = Genève » et « juridique = France » biaise la comparaison.

## 4. Matériel (l'instrument expérimental)

### 4.a — Grille de scoring d'opportunité (IDENTIQUE pour tous les prospects)

Chaque axe noté **0 / 1 / 2**. Total **/12**. *Plus le score est haut, plus la vente est « facile/forte ».*

| # | Axe | 0 | 1 | 2 |
|---|---|---|---|---|
| **A** | **Gravité du site actuel** *(le problème = l'argument)* | Site moderne/correct | Daté mais fonctionnel | Cassé / pas responsive / pas de CTA / absent |
| **B** | **Problème métier visible** *(un vrai pain à pointer)* | Rien d'évident | Pain diffus | Pain criant (recrutement affiché, prise de RDV absente, espace client cassé, e-réputation faible) |
| **C** | **Décideur accessible** | Introuvable | Nom trouvé, contact indirect | Nom + contact directs, 1 seul référent, taille humaine |
| **D** | **Capacité à payer** *(CA/taille, proxy)* | < 200 k€ / solo fragile | 200-500 k€ | ≥ 500 k€ / plusieurs employés / implantations |
| **E** | **Levier spécifique** *(chaleur / moat)* | Froid, aucun levier | Un levier faible | Intro possible (maman/réseau) **ou** backend Gemweb standard (scale) **ou** proximité locale forte |
| **F** | **Potentiel récurrent / LTV** | One-shot (désigné, pas d'upsell) | Maintenance/contenu possible | Profession **choisie** → upsell pub/SEO réel |

**Bandes de décision :**
- **10-12 🟢** — prospect prioritaire (1ʳᵉ vague de contact)
- **6-9 🟡** — bon, 2ᵉ vague
- **≤ 5 ⚪** — écarter

> Note : A/B/C/D mesurent la **facilité de vente immédiate** ; E/F mesurent la **valeur long terme**. Un score bas en F
> n'élimine pas (mandataire = peu de récurrent mais forte chaleur) — c'est tout l'intérêt de voir les profils par segment.

### 4.b — Sources de données (pour remplir la grille)
- **Mandataires / admin. judiciaires** : annuaire **CNAJMj** (cnajmj.fr)
- **Notaires** : **notaires.fr** / annuaire des offices
- **Avocats** : annuaires des **Ordres** (barreaux)
- **Experts-comptables** : annuaire **OEC** (Ordre des experts-comptables)
- **PME locales** : Google Maps, mairie/CCI, répertoires locaux
- **CA / dirigeants** (capacité à payer + décideur) : **pappers.fr**, societe.com, LinkedIn, « <nom> + chiffre d'affaires » sur Google

### 4.c — Le tableau (1 ligne par prospect)

| Prospect | Segment | Région | Site (URL) | A | B | C | D | E | F | **Score /12** | Argument-clé (1 phrase) | *(plus tard)* Contacté · RDV · Signé |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 5. Méthode (procédure)

1. Définir les **critères d'inclusion** par segment (ex : CA ≥ 200 k€, a un site existant, en France ou Genève selon segment).
2. Tirer **5 prospects par segment** (= 25) le plus représentativement possible (pas que les pires).
3. Pour chaque prospect : ouvrir le site, remplir **A→F** avec la grille → **Score /12** + 1 phrase d'argument-clé.
4. Scorer **sans regarder le segment** si possible (anti-biais), puis révéler.
5. Calculer le **score moyen par segment** + la dispersion.

## 6. Mesure & analyse (plus tard)
- **Ce soir** : on s'arrête à l'**instrument + le design** (cette page). Éventuellement 1-2 lignes « test » pour valider que la grille est utilisable.
- **Étape suivante** : remplir les 25 lignes → comparer les **moyennes par segment** → choisir le(s) segment(s) gagnant(s).
- **Validation réelle** : contacter le segment gagnant, mesurer **taux de RDV** puis **signature** (la grille « score d'opportunité » n'est qu'un *proxy* à confirmer par le terrain).

## 7. Observations — Passe 1 (recherche web, 11/06/2026 soir, 5 agents)

> ⚠️ **Statut = collecte, pas conclusion.** Score = *proxy de facilité d'argumentaire*, à confirmer par le terrain (taux de RDV/signature).
> Biais connus : (a) 5 agents = 5 évaluateurs → variance ; (b) la **chaleur via maman** (mandataires) n'est PAS dans le score ; (c) capacité à payer (D) estimée, non vérifiée au registre.

### Synthèse par segment
| Rang | Segment | n | Score moyen /12 | Meilleur prospect (score) | Lecture |
|---|---|---|---|---|---|
| 1 | Notaires | 5 | **9.8** | de Poulpiquet (Nice), Soudé (Paris 9e), Not'r 1 Pact (77) — 11 | CA élevé (D=2) + récurrent fort (F=2) ; pain = fonctionnalités manquantes (RDV/annonces/estimation), pas l'esthétique |
| 2 | PME locales Champel | 5 | **9.6** | Institut Sylvie Janus (~250 m) — 11 | Proximité forte (E=2) + récurrent pub (F=2) + sites datés/buggés ; tous à <700 m du 14 rue Crespin |
| 3 | Avocats | 5 | 8.4 | Cabinet KOY, Perpignan — 11 | Solos/petits cabinets (Perpignan/La Rochelle) ; pain récurrent = aucune prise de RDV en ligne ; profession choisie → upsell SEO |
| 4 | Experts-comptables | 5 | 8.4 | GCL Montauban — 11 | Souvent déjà un site correct → plus upsell SEO/pub que refonte d'urgence |
| 5 | Mandataires judiciaires | 5 | 8.0 | Verrecchia/MJ13, Salon-de-Provence — 10 | Sites Gemweb années 2000 = **levier de scale** (réseau CNAJMj) ; MAIS récurrent faible (F≈1) + le score sous-pondère la chaleur via maman |

### Détail — Mandataires / administrateurs judiciaires (moy. 8.0)
| Prospect | Région | Site | A B C D E F | Score | Argument-clé |
|---|---|---|---|---|---|
| Eric Verrecchia / MJ13 | Salon-de-Provence | mj13.fr | 2 2 2 1 2 1 | **10** | Site années 2000 (tables+GIF), pas responsive, pas de contact en home — Gemweb 4.3.0 |
| SELARL Philae | Bordeaux/Pau | philaemj.fr | 2 2 1 1 2 1 | **9** | Portail 2010, jsessionid dans l'URL, pas de tél visible — Gemweb 4.3.0 |
| Mandaction | Hauts-de-France | mandaction.fr | 2 1 2 2 1 1 | **9** | Réseau 12 mandataires/8 études mais site daté + navigation confuse |
| MJA / ADN.MJ | National (Paris…) | mjassocies.eu | 0 0 2 2 1 1 | 6 | Déjà moderne — peu de levier (angle = unifier marque etudejp.fr/mjassocies.eu) |
| AJILINK | National | ajilink.fr | 0 1 1 2 1 1 | 6 | Réseau récent au site moderne — décideur peu accessible |

### Détail — Avocats (moy. 8.4)
| Prospect | Région | Site | A B C D E F | Score | Argument-clé |
|---|---|---|---|---|---|
| Cabinet KOY | Perpignan | koyavocat-perpignan.fr | 2 2 2 1 2 2 | **11** | Images cassées, pas responsive, pas de RDV — cible immo/copro solvable |
| Cabinet Parayre | Perpignan | avocat-parayre-perpignan.fr | 2 2 2 0 2 1 | 9 | « Lorem ipsum » encore en place — site bâclé jamais fini |
| GRARD Avocat | La Rochelle | grard-avocat.fr | 1 1 2 1 2 2 | 9 | Solo en croissance déjà conscient de l'acquisition (RDV sur avocat.fr) |
| Lexiroc | La Rochelle/Rochefort | lexiroc.com | 1 2 1 2 1 1 | 8 | ~9 avocats, 2 sites, mais aucune prise de RDV en ligne |
| Citellia Avocats | La Rochelle | citellia-avocats.fr | 0 0 2 1 1 1 | 5 | Déjà moderne (bouton RDV) — contre-exemple, au mieux upsell SEO |

### Détail — Notaires (moy. 9.8)
| Prospect | Région | Site | A B C D E F | Score | Argument-clé |
|---|---|---|---|---|---|
| SCP de Poulpiquet | Nice | depoulpiquet-associes-nice.notaires.fr | 2 2 1 2 2 2 | **11** | Étude >150 ans, site daté, avertissement IE, 0 annonce immo |
| Me Xavier Soudé | Paris 9e | soude.notaires.fr | 2 2 2 2 1 2 | **11** | Site « 2015 », pas de RDV/annonces/estimation, décideur joignable |
| Not'r 1 Pact | Combs-la-Ville (77) | notr1pact.notaires.fr | 1 2 2 2 2 2 | **11** | 2 notaires joignables, image moderne mais 0 annonce/estimation/RDV |
| Belle Notaires | Bailleul/Nieppe (59) | belle-notaires.fr | 1 1 1 2 1 2 | 8 | Déjà équipée mais actus figées 2020-21 — upsell SEO/contenu |
| Étude Notara | Lyon 7e | notara.notaires.fr | 0 1 2 2 1 2 | 8 | Moderne, 175 avis 5/5 — angle upsell fonctionnalités (RDV/estimation) |

### Détail — Experts-comptables (moy. 8.4)
| Prospect | Région | Site | A B C D E F | Score | Argument-clé |
|---|---|---|---|---|---|
| GCL Montauban (D. Barthe) | Montauban | gclnet.fr/cabinets/montauban | 2 2 2 1 2 2 | **11** | Site daté + placeholders pour un positionnement « conseil premium » |
| Revalen | Quimper | revalen.fr | 1 2 1 1 1 2 | 8 | Se dit « digital » mais email @gmail, aucun dirigeant nommé |
| Barrandon & Associés | Limoges | barrandon.fr | 1 1 2 2 1 1 | 8 | ~20 collab. (paie), RDV+espace client OK mais design traditionnel |
| ABC Gestion 87 | Limoges | abcgestion87.fr | 0 1 2 1 2 2 | 8 | Déjà moderne (CTA création d'entreprise) — upsell SEO/acquisition |
| FCC Conseil | Roubaix | fcconseil.com | 0 1 1 2 1 2 | 7 | Vitrine moderne + app — angle pub/SEO sectoriel (santé/pharma) |

### Détail — PME locales Genève Champel (moy. 9.6) — autour du 14 rue Crespin, 1206
| Prospect | Type | Dist. | Site | A B C D E F | Score | Argument-clé |
|---|---|---|---|---|---|---|
| Institut Sylvie Janus | Beauté | ~250 m | institutsylviejanus.com | 2 2 2 1 2 2 | **11** | 40+ ans, site daté, 0 réservation/tarif, gérante joignable direct |
| Opticent | Opticien | ~300 m | opticent.ch | 2 1 1 2 2 2 | **10** | Site « moderne » truffé de Lorem ipsum/images de dev |
| Bistrot Dumas | Resto (Bib Gourmand) | ~650 m | lebistrotdumas.ch | 2 2 1 2 1 2 | **10** | Michelin 2025 mais AUCUNE réservation en ligne ni prix |
| Comme un rêve | Beauté | ~400 m | comme-un-reve.com | 2 1 1 1 2 2 | 9 | Bugs d'encodage (« � »), aucune photo ni tarif |
| Gianni & Laura | Resto/pizzeria | ~700 m | giannielaura.ch | 1 1 1 2 1 2 | 8 | Déjà résa en ligne — upsell ads + clean-up |

## 8. Conclusion (provisoire — à valider par le terrain)
> **Le proxy favorise Notaires (9.8) et PME Champel (9.6).** Mais le score **ne mesure pas la conversion réelle ni la chaleur** :
> - **1ère vente la plus probable** = **mandataires via maman** (chaleur hors-score) + levier scale Gemweb.
> - **Volume + récurrent** = **PME Champel** (à pied, méthode vidéo 2) et **Notaires** (CA + upsell).
> **Prochaine étape (passe 2)** : choisir 1-2 segments, **contacter**, et mesurer le **vrai** taux de RDV → c'est ça qui tranche, pas le proxy.
