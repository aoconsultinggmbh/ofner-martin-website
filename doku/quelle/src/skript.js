/* ============================================================================
   PRAXIS DR. OFNER-MARTIN, Skript der Gesamtvorschau
   Jeder Block prüft zuerst, ob sein Element existiert.
   ============================================================================ */
(function () {
  'use strict';

  /* ------------------------------------------------------ Menü (Burger) */
  var menue = document.getElementById('menue');
  var burger = document.querySelector('[data-menue-auf]');
  var schleier = document.querySelector('.menue-schleier');
  if (menue && burger) {
    var zuKnopf = menue.querySelector('[data-menue-zu]');
    var auf = function () {
      menue.setAttribute('data-offen', '');
      if (schleier) schleier.setAttribute('data-offen', '');
      burger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      requestAnimationFrame(function () { (zuKnopf || menue.querySelector('a')).focus(); });
    };
    var zu = function (fokus) {
      if (!menue.hasAttribute('data-offen')) return;
      menue.removeAttribute('data-offen');
      if (schleier) schleier.removeAttribute('data-offen');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      if (fokus) burger.focus();
    };
    burger.addEventListener('click', auf);
    if (zuKnopf) zuKnopf.addEventListener('click', function () { zu(true); });
    if (schleier) schleier.addEventListener('click', function () { zu(true); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') zu(true); });
    menue.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { zu(false); }); });
    window.matchMedia('(min-width:1501px)').addEventListener('change', function () { zu(false); });
  }

  /* ------------------------------------------ Seitenwechsel in einer Datei
     Adressen der Form #/kuerzel oder #/kuerzel/anker. Jede Unterseite ist ein
     <main class="seite"> mit data-seite, data-titel und data-besch. */
  var seiten = Array.prototype.slice.call(document.querySelectorAll('main.seite'));
  function zeige(kuerzel, anker) {
    var ziel = null;
    seiten.forEach(function (s) {
      var treffer = s.dataset.seite === kuerzel;
      if (treffer) ziel = s;
      s.hidden = !treffer;
    });
    if (!ziel) return false;
    document.title = ziel.dataset.titel || document.title;
    var b = document.querySelector('meta[name="description"]');
    if (b && ziel.dataset.besch) b.setAttribute('content', ziel.dataset.besch);
    var aktiv = ziel.dataset.menue || kuerzel;
    document.querySelectorAll('[data-ziel]').forEach(function (a) {
      if (a.dataset.ziel === aktiv || a.dataset.ziel === kuerzel) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
    var el = anker ? document.getElementById(kuerzel + '--' + anker) : null;
    if (el) { el.scrollIntoView(); } else { window.scrollTo(0, 0); }
    return true;
  }
  function ausAdresse() {
    var h = location.hash || '';
    if (h.indexOf('#/') !== 0) { if (!h) zeige('start'); return; }
    var stueck = h.slice(2).split('/');
    if (!zeige(stueck[0] || 'start', stueck[1])) zeige('start');
  }
  window.addEventListener('hashchange', ausAdresse);
  ausAdresse();

  /* ------------------------------------ Sprechzeiten, Anzeige "jetzt offen"
     Ortszeit Karlsdorf-Neuthard (Europe/Berlin), unabhängig von der Zeitzone
     des Geräts. Die Zeiten stehen nur hier und müssen zum JSON-LD passen.
     Gesetzliche Feiertage in Baden-Württemberg werden berechnet. Urlaub und
     Fortbildung gehören in AUSNAHMEN. */
  var SPRECHZEITEN = {
    1: [['08:00', '19:00']],
    2: [['08:00', '19:00']],
    3: [['08:00', '19:00']],
    4: [['08:00', '19:00']],
    5: [['08:30', '14:00']],
    6: [],
    0: []
  };
  /* Format "JJJJ-MM-TT": "Grund" */
  var AUSNAHMEN = {};
  var TAGE = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
  var KURZ = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'];
  var MONATE = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'];
  var speicher = {};

  function osterSonntag(j) {
    var a = j % 19, b = Math.floor(j / 100), c = j % 100, d = Math.floor(b / 4), e = b % 4;
    var f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3), h = (19 * a + b - d - g + 15) % 30;
    var i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451);
    return Date.UTC(j, Math.floor((h + l - 7 * m + 114) / 31) - 1, ((h + l - 7 * m + 114) % 31) + 1);
  }
  function schluessel(ms) {
    var d = new Date(ms), m = d.getUTCMonth() + 1, t = d.getUTCDate();
    return d.getUTCFullYear() + '-' + (m < 10 ? '0' + m : m) + '-' + (t < 10 ? '0' + t : t);
  }
  function feiertage(j) {
    if (speicher[j]) return speicher[j];
    var T = 86400000, o = osterSonntag(j), l = {};
    l[schluessel(Date.UTC(j, 0, 1))] = 'Neujahr';
    l[schluessel(Date.UTC(j, 0, 6))] = 'Heilige Drei Könige';
    l[schluessel(o - 2 * T)] = 'Karfreitag';
    l[schluessel(o + T)] = 'Ostermontag';
    l[schluessel(Date.UTC(j, 4, 1))] = 'Tag der Arbeit';
    l[schluessel(o + 39 * T)] = 'Christi Himmelfahrt';
    l[schluessel(o + 50 * T)] = 'Pfingstmontag';
    l[schluessel(o + 60 * T)] = 'Fronleichnam';
    l[schluessel(Date.UTC(j, 9, 3))] = 'Tag der Deutschen Einheit';
    l[schluessel(Date.UTC(j, 10, 1))] = 'Allerheiligen';
    l[schluessel(Date.UTC(j, 11, 25))] = '1. Weihnachtstag';
    l[schluessel(Date.UTC(j, 11, 26))] = '2. Weihnachtstag';
    return (speicher[j] = l);
  }
  function grund(s) {
    if (AUSNAHMEN[s]) return AUSNAHMEN[s];
    var n = feiertage(parseInt(s.slice(0, 4), 10))[s];
    return n ? n + ', Feiertag in Baden-Württemberg' : null;
  }
  function ortszeit() {
    var f = new Intl.DateTimeFormat('de-DE', { timeZone: 'Europe/Berlin', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hour12: false });
    var t = {};
    f.formatToParts(new Date()).forEach(function (p) { t[p.type] = p.value; });
    var ms = Date.UTC(+t.year, +t.month - 1, +t.day);
    return { ms: ms, tag: new Date(ms).getUTCDay(), minuten: (parseInt(t.hour, 10) % 24) * 60 + parseInt(t.minute, 10), datum: t.year + '-' + t.month + '-' + t.day };
  }
  function min(u) { var s = u.split(':'); return +s[0] * 60 + +s[1]; }
  function uhr(m) { var h = Math.floor(m / 60), r = m % 60; return h + ':' + (r < 10 ? '0' + r : r) + ' Uhr'; }
  function zeitenFuer(ms) { return grund(schluessel(ms)) ? [] : (SPRECHZEITEN[new Date(ms).getUTCDay()] || []); }
  function naechste(j) {
    var heute = zeitenFuer(j.ms);
    for (var i = 0; i < heute.length; i++) if (j.minuten < min(heute[i][0])) return { wann: 'heute um', zeit: min(heute[i][0]) };
    for (var n = 1; n <= 30; n++) {
      var ms = j.ms + n * 86400000, z = zeitenFuer(ms);
      if (z.length) {
        var d = new Date(ms);
        return { wann: n === 1 ? 'morgen um' : (n < 7 ? 'am ' + TAGE[d.getUTCDay()] + ' um' : 'am ' + d.getUTCDate() + '. ' + MONATE[d.getUTCMonth()] + ' um'), zeit: min(z[0][0]) };
      }
    }
    return null;
  }
  function feiertagVoraus(j) {
    for (var n = 1; n <= 45; n++) {
      var ms = j.ms + n * 86400000, d = new Date(ms);
      if (!(SPRECHZEITEN[d.getUTCDay()] || []).length) continue;
      var g = grund(schluessel(ms));
      if (g) return KURZ[d.getUTCDay()] + ', ' + d.getUTCDate() + '. ' + MONATE[d.getUTCMonth()] + ': geschlossen (' + g + ')';
    }
    return '';
  }

  var status = document.querySelector('[data-sprechzeiten]');
  function aktualisieren() {
    var j = ortszeit(), zeiten = zeitenFuer(j.ms), gHeute = grund(j.datum), offen = null;
    zeiten.forEach(function (z) { if (j.minuten >= min(z[0]) && j.minuten < min(z[1])) offen = z; });
    var n = naechste(j);
    var kurz, lang;
    if (offen) {
      kurz = 'Jetzt geöffnet';
      lang = 'Die Praxis hat heute geöffnet bis ' + uhr(min(offen[1])) + '.';
    } else if (gHeute) {
      kurz = 'Heute geschlossen';
      lang = 'Heute geschlossen: ' + gHeute + '.' + (n ? ' Wir sind ' + n.wann + ' ' + uhr(n.zeit) + ' wieder für Sie da.' : '');
    } else {
      kurz = n ? 'Geschlossen, öffnet ' + n.wann.replace(' um', '') + ' ' + uhr(n.zeit).replace(' Uhr', '') : 'Geschlossen';
      lang = n ? 'Zurzeit geschlossen. Die Praxis öffnet ' + n.wann + ' ' + uhr(n.zeit) + '.' : 'Zurzeit geschlossen.';
    }
    document.querySelectorAll('[data-status-kurz]').forEach(function (e) { e.textContent = kurz; });
    document.querySelectorAll('[data-status-lang]').forEach(function (e) { e.textContent = lang; });
    document.querySelectorAll('[data-offen-anzeige]').forEach(function (e) { if (offen) e.setAttribute('data-offen', ''); else e.removeAttribute('data-offen'); });
    /* Heute in allen Zeitentabellen markieren */
    document.querySelectorAll('[data-wochentag]').forEach(function (tr) {
      if (tr.getAttribute('data-wochentag').split(',').indexOf(String(j.tag)) > -1) tr.setAttribute('data-heute', ''); else tr.removeAttribute('data-heute');
    });
    if (status) {
      var liste = status.querySelector('[data-status-liste]');
      liste.innerHTML = '';
      [1, 2, 3, 4, 5, 6, 0].forEach(function (t) {
        var zt = SPRECHZEITEN[t] || [], li = document.createElement('li'), a = document.createElement('span'), b = document.createElement('span');
        if (t === j.tag) li.setAttribute('data-heute', '');
        a.textContent = TAGE[t];
        b.textContent = t === j.tag && gHeute ? 'geschlossen' : (zt.length ? zt.map(function (z) { return z[0] + '–' + z[1]; }).join(', ') + ' Uhr' : 'geschlossen');
        li.appendChild(a); li.appendChild(b); liste.appendChild(li);
      });
      var fh = status.querySelector('[data-status-feiertag]'), hin = feiertagVoraus(j);
      fh.textContent = hin; fh.hidden = !hin;
    }
  }
  aktualisieren();
  setInterval(aktualisieren, 30000);

  if (status) {
    var sKnopf = status.querySelector('.status__knopf'), sPanel = status.querySelector('.status__panel');
    var sZu = function () { sPanel.hidden = true; sKnopf.setAttribute('aria-expanded', 'false'); };
    sKnopf.addEventListener('click', function () {
      var ist = sKnopf.getAttribute('aria-expanded') === 'true';
      sPanel.hidden = ist; sKnopf.setAttribute('aria-expanded', ist ? 'false' : 'true');
    });
    document.addEventListener('click', function (e) { if (!status.contains(e.target)) sZu(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && sKnopf.getAttribute('aria-expanded') === 'true') { sZu(); sKnopf.focus(); } });
  }

  /* --------------------------- Karte und Videos erst nach Einwilligung */
  function laden(halter) {
    if (halter.getAttribute('data-geladen') === 'ja') return;
    var r = document.createElement('iframe');
    r.src = halter.getAttribute('data-quelle');
    r.title = halter.getAttribute('data-titel') || 'Eingebetteter Inhalt';
    r.loading = 'lazy';
    r.referrerPolicy = 'strict-origin-when-cross-origin';
    r.setAttribute('allowfullscreen', '');
    if (halter.getAttribute('data-einbettung') === 'video') r.setAttribute('allow', 'encrypted-media; picture-in-picture; fullscreen');
    halter.setAttribute('data-geladen', 'ja');
    halter.innerHTML = '';
    halter.appendChild(r);
  }
  var einbettungen = document.querySelectorAll('[data-einbettung]');
  function pruefen() {
    einbettungen.forEach(function (h) {
      if (window.aoEinwilligung && window.aoEinwilligung.erlaubt(h.getAttribute('data-einbettung'))) laden(h);
    });
  }
  einbettungen.forEach(function (h) {
    var k = h.querySelector('[data-laden]');
    if (k) k.addEventListener('click', function () {
      if (window.aoEinwilligung) window.aoEinwilligung.setze(h.getAttribute('data-einbettung'), true);
      laden(h);
    });
  });
  document.addEventListener('ao:einwilligung', pruefen);
  pruefen();

  /* ------------------------------------- Online-Terminbuchung (Dr. Flex)
     Das Buchungsfenster von Dr. Flex wird erst nach Zustimmung geladen.
     Vorher erscheint ein Hinweis mit Telefonnummer als Alternative. */
  var DRFLEX = 'https://dr-flex.de/embed.js?medicalPracticeId=56548';
  var flexDialog = document.getElementById('termin-dialog');
  var flexGeladen = false;
  function flexStarten() {
    if (typeof window.toggleDrFlexAppointments === 'function') { window.toggleDrFlexAppointments(); return; }
    if (flexGeladen) return;
    flexGeladen = true;
    var s = document.createElement('script');
    s.src = DRFLEX; s.async = true;
    s.onload = function () { if (typeof window.toggleDrFlexAppointments === 'function') window.toggleDrFlexAppointments(); };
    s.onerror = function () { flexGeladen = false; };
    document.head.appendChild(s);
  }
  document.querySelectorAll('[data-termin]').forEach(function (k) {
    k.addEventListener('click', function (e) {
      e.preventDefault();
      if (window.aoEinwilligung && window.aoEinwilligung.erlaubt('termin')) { flexStarten(); return; }
      if (flexDialog && flexDialog.showModal) flexDialog.showModal();
    });
  });
  if (flexDialog) {
    flexDialog.querySelector('[data-termin-ja]').addEventListener('click', function () {
      if (window.aoEinwilligung) window.aoEinwilligung.setze('termin', true);
      flexDialog.close();
      flexStarten();
    });
    flexDialog.querySelectorAll('[data-dialog-zu]').forEach(function (b) { b.addEventListener('click', function () { flexDialog.close(); }); });
  }

  /* ------------------------------------------------ Galerie mit Lupe */
  var lupe = document.getElementById('lupe');
  if (lupe) {
    var lupeBild = lupe.querySelector('img');
    document.querySelectorAll('[data-gross]').forEach(function (b) {
      b.addEventListener('click', function () {
        lupeBild.src = b.getAttribute('data-gross');
        lupeBild.alt = b.querySelector('img').alt;
        lupe.showModal();
      });
    });
    lupe.querySelector('.lupe__zu').addEventListener('click', function () { lupe.close(); });
    lupe.addEventListener('click', function (e) { if (e.target === lupe) lupe.close(); });
  }

  /* ---------------------------------------- Formulare (Entwurf, sendet nichts) */
  document.querySelectorAll('[data-formular]').forEach(function (f) {
    var t = f.querySelector('textarea[maxlength]'), z = f.querySelector('[data-zaehler]');
    if (t && z) t.addEventListener('input', function () { z.textContent = t.value.length + '/' + t.getAttribute('maxlength'); });
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true, erstes = null;
      f.querySelectorAll('[required]').forEach(function (feld) {
        var fehler = document.getElementById(feld.id + '-fehler');
        var gut = feld.type === 'checkbox' ? feld.checked : feld.checkValidity() && feld.value.trim() !== '';
        feld.setAttribute('aria-invalid', gut ? 'false' : 'true');
        if (fehler) fehler.hidden = gut;
        if (!gut) { ok = false; erstes = erstes || feld; }
      });
      if (!ok) { erstes.focus(); return; }
      var danke = f.parentNode.querySelector('.danke');
      f.hidden = true;
      if (danke) { danke.hidden = false; danke.focus(); }
    });
  });

  /* ------------------------------------------------ Jahreszahl */
  document.querySelectorAll('[data-jahr]').forEach(function (el) { el.textContent = String(new Date().getFullYear()); });
})();
