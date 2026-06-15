#!/usr/bin/env python3
"""Génère des maquettes notaires en série, en réutilisant le CSS de soude.html.
Honnêteté : pas d'avis ni de tarifs inventés, horaires génériques "sur rendez-vous".
Chaque maquette met en avant les 3 briques modernes absentes : RDV / estimation / annonces en ligne.
"""
import re, pathlib

MOCK = pathlib.Path(__file__).resolve().parents[2] / "mockups"
CSS = re.search(r"<style>.*?</style>", (MOCK / "soude.html").read_text(encoding="utf-8"), re.S).group(0)

BODY = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@ETUDE@@ — Notaire à @@VILLE@@</title>
<meta name="description" content="@@ETUDE@@, notaire à @@VILLE@@. Droit immobilier, droit de la famille, droit des sociétés et gestion de patrimoine. Prise de rendez-vous, estimation et annonces en ligne.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
@@CSS@@
</head>
<body>

<header class="nav">
  <div class="nav-inner">
    <a href="#top" class="brand"><b>@@BRAND@@</b><span>Office Notarial · @@VILLE@@</span></a>
    <nav class="nav-links">
      <a href="#etude">L'Étude</a>
      <a href="#expertise">Domaines d'expertise</a>
      <a href="#contact" class="btn btn-primary nav-cta">Prendre rendez-vous</a>
    </nav>
    <button class="burger" aria-label="Menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
  </div>
</header>

<a id="top"></a>
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Notaires à votre service · @@VILLE@@</p>
      <h1>@@BRAND@@ vous accompagne dans <em>vos projets de vie</em>.</h1>
      <p class="lead">@@INTRO@@</p>
      <div class="hero-actions">
        <a href="#contact" class="btn btn-primary">Prendre rendez-vous →</a>
        <a href="tel:@@TELHREF@@" class="btn btn-light">📞 @@TEL@@</a>
      </div>
      <p class="hero-note">✦ <b>Sur rendez-vous</b> · @@ADRESSE@@, @@CP@@ @@VILLE@@</p>
    </div>
    <div class="ph hero-photo ph-1">
      <span class="tag">photo à fournir</span>
      <span class="lbl">Façade de l'Étude / portrait des notaires</span>
    </div>
  </div>
</section>

<div class="wrap pillars">
  <div class="pillars-grid">
    <div class="pillar">
      <div class="ic">📅</div><span class="new">Nouveau</span>
      <h3>Prise de rendez-vous</h3>
      <p>Réservez votre rendez-vous en quelques clics, 24h/24, sans appeler. Choisissez le motif, le créneau, et recevez une confirmation immédiate.</p>
      <a href="#contact" class="lk" onclick="alert('Maquette de démonstration — ici se branche le module de prise de rendez-vous en ligne (agenda de l\\'Étude).');return false;">Réserver un créneau →</a>
    </div>
    <div class="pillar">
      <div class="ic">📈</div><span class="new">Nouveau</span>
      <h3>Estimation en ligne</h3>
      <p>Offrez à vos clients une première estimation de leur bien à partir des références notariales du marché, puis affinez-la avec un notaire.</p>
      <a href="#contact" class="lk" onclick="alert('Maquette de démonstration — ici se branche l\\'outil d\\'estimation immobilière en ligne.');return false;">Estimer un bien →</a>
    </div>
    <div class="pillar">
      <div class="ic">🏠</div><span class="new">Nouveau</span>
      <h3>Annonces immobilières</h3>
      <p>Mettez en avant les biens à vendre de l'Étude. Une vente sécurisée, du compromis à l'acte authentique, avec le même interlocuteur.</p>
      <a href="#contact" class="lk" onclick="alert('Maquette de démonstration — ici se branche le flux d\\'annonces immo-notaires.');return false;">Voir les annonces →</a>
    </div>
  </div>
  <p class="note">💡 <b>Exemple — à connecter.</b> Ces trois services en ligne (rendez-vous, estimation, annonces) sont les briques modernes absentes du site actuel. Ils seront raccordés aux outils réels de l'Étude lors de la mise en ligne.</p>
</div>

<section id="etude">
  <div class="wrap about-grid about">
    <div class="ph about-photo ph-2"><span class="tag">photo à fournir</span><span class="lbl">Accueil / salle de signature de l'Étude</span></div>
    <div>
      <p class="eyebrow">L'Étude</p>
      <h2>Une équipe à votre écoute, au service de vos projets</h2>
      <p>L'Étude accompagne particuliers, professionnels et institutions à chaque étape de leur vie et de leurs projets immobiliers et patrimoniaux, avec rigueur et pédagogie.</p>
      <p>De la première question à la signature de l'acte authentique, vous gardez le même interlocuteur, à @@VILLE@@.</p>
      <p class="sig">« Le notaire est la pierre angulaire de vos transactions. »</p>
      <a href="#contact" class="btn btn-primary" style="margin-top:12px">Contactez l'Étude →</a>
    </div>
  </div>
</section>

<section id="expertise">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Nos compétences</p><h2>Domaines d'expertise</h2>
      <p>De l'immobilier à la transmission patrimoniale, l'Étude vous conseille sur les plans juridique et fiscal.</p></div>
    <div class="domains-grid">
      <div class="domain" id="immobilier"><div class="ic">🏛️</div><h3>Droit immobilier</h3>
        <ul><li>Vente, avant-contrat, conseils patrimoniaux</li><li>Baux d'habitation ou commerciaux</li><li>Copropriété, prêts authentiques, sûretés</li><li>Promotion immobilière (VEFA)</li></ul></div>
      <div class="domain"><div class="ic">👨‍👩‍👧</div><h3>Droit de la famille</h3>
        <ul><li>PACS, mariage, divorce, adoption</li><li>Contrat de mariage, régime matrimonial</li><li>Testament, succession, donation</li><li>Protection du conjoint survivant</li></ul></div>
      <div class="domain"><div class="ic">🏢</div><h3>Droit des sociétés</h3>
        <ul><li>Constitution de société, création de SCI</li><li>Baux commerciaux</li><li>Secrétariat juridique</li><li>Transmission d'entreprise</li></ul></div>
      <div class="domain"><div class="ic">💼</div><h3>Gestion de patrimoine</h3>
        <ul><li>Stratégie patrimoniale sur mesure</li><li>Organisation de la transmission</li><li>Optimisation juridique et fiscale</li><li>Accompagnement des particuliers et pros</li></ul></div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="cta-band">
    <p class="eyebrow" style="color:var(--amber)">Prise de rendez-vous</p>
    <h2>Prenez rendez-vous en quelques clics</h2>
    <p>Réservez votre créneau en ligne 24h/24, ou contactez-nous directement. Un notaire vous rappelle pour préparer votre dossier.</p>
    <a href="#contact" class="btn btn-primary" onclick="alert('Maquette de démonstration — ici se branche le module de prise de rendez-vous en ligne.');return false;">Choisir un créneau →</a>
    <p style="margin-top:18px;font-size:.85rem;opacity:.85">ou par téléphone au <a href="tel:@@TELHREF@@" style="color:#fff;text-decoration:underline">@@TEL@@</a></p>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Nous trouver</p><h2>Contactez votre Office Notarial à @@VILLE@@</h2>
      <p>L'Étude vous accueille sur rendez-vous. Prenez rendez-vous ou écrivez-nous.</p></div>
    <div class="info-grid">
      <div class="info-card">
        <h3>Coordonnées</h3>
        <div class="info-row"><span class="k">📍</span><span class="v"><b>Adresse</b>@@ADRESSE@@, @@CP@@ @@VILLE@@<br><a href="https://www.google.com/maps/search/?api=1&query=@@MAPSQ@@" target="_blank" rel="noopener">Voir sur Google Maps →</a></span></div>
        <div class="info-row"><span class="k">📞</span><span class="v"><b>Téléphone</b><a href="tel:@@TELHREF@@">@@TEL@@</a></span></div>
        <div class="info-row"><span class="k">✉️</span><span class="v"><b>Email</b><a href="mailto:@@EMAIL@@">@@EMAIL@@</a></span></div>
        <div class="info-row"><span class="k">🕑</span><span class="v"><b>Horaires</b>Du lundi au vendredi, sur rendez-vous <span style="color:var(--ink-soft)">(à confirmer)</span></span></div>
      </div>
      <div class="info-card">
        <h3>Demande de rendez-vous</h3>
        <form onsubmit="alert('Maquette de démonstration — le formulaire sera connecté à la messagerie de l\\'Étude.');return false;">
          <div class="form-field"><label>Nom &amp; prénom</label><input type="text" placeholder="Votre nom"></div>
          <div class="form-field"><label>Email</label><input type="email" placeholder="vous@exemple.fr"></div>
          <div class="form-field"><label>Téléphone</label><input type="tel" placeholder="06 00 00 00 00"></div>
          <div class="form-field"><label>Sujet</label><select><option>Prise de rendez-vous</option><option>Droit immobilier</option><option>Droit de la famille</option><option>Droit des sociétés</option><option>Autre</option></select></div>
          <div class="form-field"><label>Message</label><textarea rows="3" placeholder="Décrivez votre demande"></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Envoyer ma demande</button>
        </form>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div><div class="brand"><b style="font-size:1.6rem;font-family:'Cormorant Garamond',serif">@@BRAND@@</b></div>
        <p class="fp" style="margin-top:12px">Office Notarial à @@VILLE@@.<br>Au service de vos projets immobiliers, familiaux et patrimoniaux.</p></div>
      <div><h4>Expertise</h4><a href="#immobilier">Droit immobilier</a><a href="#expertise">Droit de la famille</a><a href="#expertise">Droit des sociétés</a><a href="#expertise">Gestion de patrimoine</a></div>
      <div><h4>L'Étude</h4><a href="#etude">Notre équipe</a><a href="#contact">Prendre rendez-vous</a><a href="tel:@@TELHREF@@">@@TEL@@</a><a href="mailto:@@EMAIL@@">@@EMAIL@@</a></div>
    </div>
    <div class="foot-bottom"><span>© <span id="yr"></span> @@ETUDE@@ · @@ADRESSE@@, @@CP@@ @@VILLE@@</span><span>Sur rendez-vous</span></div>
  </div>
</footer>

<div class="float-cta"><a href="#contact" class="btn btn-primary">Prendre rendez-vous →</a></div>
<script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
<!-- maquette de prospection Atelier Web — non officielle -->
</body>
</html>"""

import urllib.parse

PROSPECTS = [
  dict(slug="paris-associes-macon", etude="SARL Paris & Associés", brand="Paris & Associés",
       ville="Mâcon", cp="71001", adresse="150 rue Rambuteau", tel="03 85 29 00 82",
       telhref="+33385290082", email="parisetassocies@notaires.fr",
       intro="L'Étude Paris & Associés, à Mâcon, vous assiste dans les grandes étapes de votre vie ainsi que dans tous vos projets immobiliers et patrimoniaux."),
  dict(slug="pluriel-paris", etude="Pluriel Notaires & Associés", brand="Pluriel Notaires",
       ville="Paris 7ᵉ", cp="75007", adresse="26 rue Vaneau", tel="01 64 06 71 31",
       telhref="+33164067131", email="contact@pluriel.notaires.fr",
       intro="Au cœur du 7e arrondissement, l'Étude Pluriel vous accompagne dans vos moments de vie de couple, de famille et dans vos projets immobiliers et patrimoniaux."),
  dict(slug="ballester-latourdupin", etude="Ballester & Associés", brand="Ballester & Associés",
       ville="La Tour-du-Pin", cp="38110", adresse="52 rue Pierre Vincendon", tel="04 74 83 56 00",
       telhref="+33474835600", email="christelle.ballester@notaires.fr",
       intro="À La Tour-du-Pin, l'Étude Ballester & Associés vous conseille en droit immobilier, droit de la famille, droit des sociétés et gestion de patrimoine."),
  dict(slug="notaires-pasteur-saint-denis", etude="Office Notarial Notaires Pasteur", brand="Notaires Pasteur",
       ville="Saint-Denis", cp="97400", adresse="44 rue Pasteur", tel="02 62 90 14 14",
       telhref="+262262901414", email="notaires.44ruepasteur@notaires-pasteur.notaires.fr",
       intro="Étude historique de Saint-Denis de La Réunion, Notaires Pasteur vous accompagne en droit de la famille, immobilier, entreprise et conseil patrimonial."),
  dict(slug="notr1pact-combs", etude="Not'r 1 Pact — Petit & Thiriet", brand="Not'r 1 Pact",
       ville="Combs-la-Ville", cp="77380", adresse="Combs-la-Ville", tel="01 60 60 60 60",
       telhref="+33160606060", email="accueil@77103.notaires.fr",
       intro="À Combs-la-Ville, Maîtres François-Xavier Petit et Claire Thiriet vous accompagnent en droit immobilier, droit de la famille et transmission patrimoniale.",
       skip_tel=True),
  dict(slug="boiron-montoux-dermaut-gresy", etude="SCP Boiron-Montoux & Dermaut", brand="Boiron-Montoux & Dermaut",
       ville="Grésy-sur-Isère", cp="73460", adresse="107 rue de la Lauzière", tel="04 79 37 90 08",
       telhref="+33479379008", email="accueil@1712.notaires.fr",
       intro="En Savoie, l'Étude Boiron-Montoux & Dermaut vous conseille en droit immobilier, droit de la famille, droit des sociétés et gestion de patrimoine."),
  dict(slug="poirier-associes-les-ulis", etude="Poirier & Associés", brand="Poirier & Associés",
       ville="Les Ulis", cp="91940", adresse="Immeuble le Trigone, route de Gometz", tel="01 64 86 55 80",
       telhref="+33164865580", email="accueil@poirieretassocies.notaires.fr",
       intro="Aux Ulis, l'Étude Poirier & Associés vous accompagne dans vos projets immobiliers, familiaux et patrimoniaux."),
  dict(slug="decaux-fargues-saint-cere", etude="Decaux, Fargues & Associés", brand="Decaux & Fargues",
       ville="Saint-Céré", cp="46400", adresse="182 avenue Gaston Monnerville", tel="05 65 38 09 53",
       telhref="+33565380953", email="decaux@notaires.fr",
       intro="À Saint-Céré, dans le Lot, l'Étude Decaux & Fargues vous conseille en droit immobilier, droit de la famille et transmission patrimoniale."),
]

for p in PROSPECTS:
    html = BODY.replace("@@CSS@@", CSS)
    html = (html.replace("@@ETUDE@@", p["etude"]).replace("@@BRAND@@", p["brand"])
                .replace("@@VILLE@@", p["ville"]).replace("@@CP@@", p["cp"])
                .replace("@@ADRESSE@@", p["adresse"]).replace("@@TEL@@", p["tel"])
                .replace("@@TELHREF@@", p["telhref"]).replace("@@EMAIL@@", p["email"])
                .replace("@@INTRO@@", p["intro"])
                .replace("@@MAPSQ@@", urllib.parse.quote(f"{p['adresse']} {p['cp']} {p['ville']}")))
    out = MOCK / f"{p['slug']}.html"
    out.write_text(html, encoding="utf-8")
    print("écrit:", out.name)
print("OK", len(PROSPECTS), "maquettes")
