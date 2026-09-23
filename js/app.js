// MPAI Technologies — interacción de la web (sin dependencias externas)
'use strict';

/* ---------- Menú móvil ---------- */
(function menuMovil() {
  const abrir = document.querySelector('[data-action="abrir-menu"]');
  const cerrar = document.querySelector('[data-action="cerrar-menu"]');
  const menu = document.querySelector('.menu-movil');
  if (!abrir || !menu) return;
  const cierra = () => { menu.classList.remove('abierto'); document.body.style.overflow = ''; };
  abrir.addEventListener('click', () => { menu.classList.add('abierto'); document.body.style.overflow = 'hidden'; });
  cerrar?.addEventListener('click', cierra);
  menu.querySelectorAll('a').forEach((a) => a.addEventListener('click', cierra));
})();

/* ---------- FAQ (usa <details>, esto solo cierra los demás al abrir uno) ---------- */
(function faqExclusivo() {
  const items = document.querySelectorAll('.faq-item');
  items.forEach((item) => {
    item.addEventListener('toggle', () => {
      if (item.open) items.forEach((otro) => { if (otro !== item) otro.open = false; });
    });
  });
})();

/* ---------- Circuito animado (flujo real de respaldo de Instagram) ---------- */
(function circuito() {
  const svg = document.querySelector('#circuito-svg');
  const leyenda = document.querySelector('#circuito-leyenda');
  const boton = document.querySelector('[data-action="ver-circuito"]');
  if (!svg || !leyenda) return;

  const nodos = [
    { id: 'n1', x: 70, texto: '19:15', sub: 'cada día', desc: 'Cada día a las 19:15 se comprueba si la pieza de hoy ya salió en Instagram.' },
    { id: 'n2', x: 210, texto: 'Registro', sub: 'leer', desc: 'Consulta el registro de publicaciones del día en GitHub.' },
    { id: 'n3', x: 350, texto: 'Calendario', sub: 'leer', desc: 'Consulta qué pieza tocaba publicar hoy.' },
    { id: 'n4', x: 490, texto: '¿Rescatar?', sub: 'decisión', desc: 'Compara ambos: si el cron de GitHub ya publicó, no hace nada.', decision: true },
    { id: 'n5', x: 630, texto: 'Disparar', sub: 'GitHub', desc: 'Lanza el mismo flujo de publicación por API, como si fuera el cron.' },
    { id: 'n6', x: 770, texto: 'Esperar', sub: '6 min', desc: 'Espera a que la publicación tenga tiempo de completarse.' },
    { id: 'n7', x: 910, texto: 'Releer', sub: 'registro', desc: 'Vuelve a mirar el registro: no da por bueno un aviso sin comprobarlo.' },
    { id: 'n8', x: 1050, texto: '¿Publicó?', sub: 'decisión', desc: 'Solo si el registro cambió de verdad se considera un rescate real.', decision: true },
    { id: 'n9', x: 1190, texto: 'Avisar', sub: 'correo', desc: 'Un correo distinto según lo que pasó: rescatado, fallo de GitHub, o arrancó y no publicó nada.' },
  ];
  const y = 60;
  const w = 1260, h = 130;
  svg.setAttribute('viewBox', `0 0 ${w} ${h}`);

  const svgns = 'http://www.w3.org/2000/svg';
  const crear = (tag, attrs) => {
    const el = document.createElementNS(svgns, tag);
    Object.entries(attrs).forEach(([k, v]) => el.setAttribute(k, v));
    return el;
  };

  // líneas
  for (let i = 0; i < nodos.length - 1; i++) {
    svg.appendChild(crear('line', {
      class: 'circuito-linea', x1: nodos[i].x + 22, y1: y, x2: nodos[i + 1].x - 22, y2: y,
    }));
  }
  // nodos
  nodos.forEach((n) => {
    const g = crear('g', { class: 'circuito-nodo', id: 'g-' + n.id });
    g.appendChild(crear('rect', {
      x: n.x - 22, y: y - 20, width: 44, height: n.decision ? 44 : 40, rx: n.decision ? 22 : 4,
      transform: n.decision ? `rotate(0 ${n.x} ${y})` : '',
    }));
    const t1 = crear('text', { x: n.x, y: y + h / 2 + 4, 'text-anchor': 'middle' });
    t1.textContent = n.texto;
    const t2 = crear('text', { x: n.x, y: y + h / 2 + 18, 'text-anchor': 'middle', class: 'sub' });
    t2.textContent = n.sub;
    g.appendChild(t1); g.appendChild(t2);
    svg.appendChild(g);
  });
  const paquete = crear('circle', { class: 'circuito-paquete', r: 6, cx: nodos[0].x, cy: y });
  svg.appendChild(paquete);

  let animando = false;
  async function recorrer() {
    if (animando) return;
    animando = true;
    boton && (boton.disabled = true);
    document.querySelectorAll('.circuito-nodo').forEach((g) => g.classList.remove('activo'));
    for (let i = 0; i < nodos.length; i++) {
      const n = nodos[i];
      document.getElementById('g-' + n.id)?.classList.add('activo');
      paquete.setAttribute('cx', n.x);
      leyenda.innerHTML = `<strong>${n.texto}.</strong> ${n.desc}`;
      await esperar(950);
    }
    leyenda.innerHTML = '<strong>Recorrido completo.</strong> Este es el flujo real que respalda la publicación diaria en Instagram si el disparador principal se retrasa.';
    animando = false;
    boton && (boton.disabled = false);
  }
  const esperar = (ms) => new Promise((r) => setTimeout(r, ms));
  boton?.addEventListener('click', recorrer);

  // clic/tacto en un nodo suelto también explica su paso
  nodos.forEach((n) => {
    document.getElementById('g-' + n.id)?.addEventListener('click', () => {
      leyenda.innerHTML = `<strong>${n.texto}.</strong> ${n.desc}`;
    });
  });

  // arranque automático si el visitante no ha pedido "no reducir movimiento"
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const io = new IntersectionObserver((entradas) => {
    entradas.forEach((e) => {
      if (e.isIntersecting && !reduce) { recorrer(); io.disconnect(); }
    });
  }, { threshold: .4 });
  io.observe(svg);
})();

/* ---------- Chat del agente (guionizado) ---------- */
(function chatAgente() {
  const hilo = document.querySelector('#chat-hilo');
  const opciones = document.querySelector('#chat-opciones');
  const reiniciar = document.querySelector('[data-action="reiniciar-chat"]');
  if (!hilo || !opciones) return;

  const guiones = {
    papeles: {
      pregunta: '¿Qué papeles me faltan para hacer la renta?',
      pasos: [
        { tipo: 'paso', texto: 'Mirando tu expediente…' },
        { tipo: 'agente', texto: 'Te falta el certificado de retenciones del segundo pagador y el recibo del plan de pensiones. El resto ya lo tenemos.' },
        { tipo: 'paso', texto: 'Consultando la agenda del despacho…' },
        { tipo: 'agente', texto: 'Cuando los tengas, ¿te viene bien el jueves a las 10:00 con María? Te reservo el hueco.' },
      ],
    },
    plazo: {
      pregunta: '¿Cuándo vence el modelo 303 de este trimestre?',
      pasos: [
        { tipo: 'paso', texto: 'Consultando el calendario fiscal…' },
        { tipo: 'agente', texto: 'El plazo general termina el 20 de octubre. Si domicilias el pago, el límite es el 15 de octubre.' },
        { tipo: 'agente', texto: '¿Quieres que te lo confirme por escrito un asesor, por si tu caso tiene alguna particularidad?' },
      ],
    },
    dificil: {
      pregunta: 'Me han abierto una inspección, ¿qué hago?',
      pasos: [
        { tipo: 'paso', texto: 'Detectando que el caso necesita criterio profesional…' },
        { tipo: 'humano', texto: 'Esto lo lleva directamente un asesor: te transfiero a Marta ahora mismo y le paso todo tu expediente para que no repitas nada.' },
      ],
    },
  };

  function limpiar() { hilo.innerHTML = ''; }
  function burbuja(tipo, texto) {
    const div = document.createElement('div');
    div.className = 'burbuja ' + tipo;
    div.textContent = texto;
    hilo.appendChild(div);
    hilo.scrollTop = hilo.scrollHeight;
  }
  const esperar = (ms) => new Promise((r) => setTimeout(r, ms));

  async function ejecutar(clave) {
    const guion = guiones[clave];
    if (!guion) return;
    opciones.querySelectorAll('button').forEach((b) => (b.disabled = true));
    limpiar();
    burbuja('cliente', guion.pregunta);
    await esperar(500);
    for (const paso of guion.pasos) {
      await esperar(700);
      burbuja(paso.tipo, paso.texto);
    }
    opciones.querySelectorAll('button').forEach((b) => (b.disabled = false));
  }

  opciones.querySelectorAll('[data-chat]').forEach((b) => {
    b.addEventListener('click', () => ejecutar(b.getAttribute('data-chat')));
  });
  reiniciar?.addEventListener('click', () => {
    limpiar();
    burbuja('agente', 'Hola, soy el asistente del despacho. Elige una pregunta de ejemplo abajo para ver cómo respondo.');
  });
  // estado inicial
  burbuja('agente', 'Hola, soy el asistente del despacho. Elige una pregunta de ejemplo abajo para ver cómo respondo.');
})();

/* ---------- Calculadora de ahorro ---------- */
(function calculadora() {
  const personas = document.querySelector('#calc-personas');
  const horas = document.querySelector('#calc-horas');
  const coste = document.querySelector('#calc-coste');
  const salida = document.querySelector('#calc-resultado');
  const salidaSub = document.querySelector('#calc-resultado-sub');
  const escalonEl = document.querySelector('#calc-escalon');
  if (!personas || !horas || !coste || !salida) return;

  function escalon(horasSemana) {
    if (horasSemana <= 3) return ['Nivel 1 — Automatización sin IA', 'Reglas claras, sin modelo de por medio: el escalón más barato.'];
    if (horasSemana <= 8) return ['Nivel 2 o 3 — Clasificar, extraer o responder con tus documentos', 'Ya compensa leer texto libre o consultar tu documentación.'];
    return ['Nivel 4 — Agente con acciones', 'El volumen justifica que el sistema también escriba en tus programas.'];
  }

  function actualizar() {
    const p = Number(personas.value);
    const h = Number(horas.value);
    const c = Number(coste.value);
    const horasAno = p * h * 47; // semanas laborables aprox., fuera de vacaciones
    const euros = Math.round(horasAno * c);
    document.querySelector('#calc-personas-v').textContent = p;
    document.querySelector('#calc-horas-v').textContent = h + ' h/semana';
    document.querySelector('#calc-coste-v').textContent = c + ' €/h';
    salida.textContent = horasAno.toLocaleString('es-ES') + ' h/año';
    salidaSub.textContent = '≈ ' + euros.toLocaleString('es-ES') + ' € al año en tiempo, con tus propios números';
    const [titulo, texto] = escalon(h);
    escalonEl.innerHTML = `<strong>${titulo}.</strong> ${texto}`;
  }
  [personas, horas, coste].forEach((el) => el.addEventListener('input', actualizar));
  actualizar();
})();

/* ---------- Visor de proyectos (si la página lo trae) ---------- */
(function visor() {
  const capa = document.querySelector('.visor');
  if (!capa) return;
  const img = capa.querySelector('img');
  const pie = capa.querySelector('.visor-pie');
  const titulo = capa.querySelector('.visor-titulo');
  const posicion = capa.querySelector('.visor-posicion');
  let pases = [];
  let i = 0;

  function pintar() {
    const p = pases[i];
    img.src = p.src;
    img.alt = p.alt || '';
    pie.textContent = p.pie || '';
    posicion.textContent = `${i + 1} / ${pases.length}`;
  }
  function abrir(lista, nombre, inicio) {
    pases = lista; i = inicio || 0; titulo.textContent = nombre;
    capa.classList.add('abierto');
    document.body.style.overflow = 'hidden';
    pintar();
  }
  function cerrar() { capa.classList.remove('abierto'); document.body.style.overflow = ''; }
  function mover(paso) { i = (i + paso + pases.length) % pases.length; pintar(); }

  document.querySelectorAll('[data-galeria]').forEach((disparador) => {
    disparador.addEventListener('click', () => {
      const datos = JSON.parse(document.getElementById(disparador.getAttribute('data-galeria')).textContent);
      const inicio = Number(disparador.getAttribute('data-pase')) || 0;
      abrir(datos.pases, datos.titulo, inicio);
    });
  });
  capa.querySelector('[data-action="cerrar-visor"]')?.addEventListener('click', cerrar);
  capa.querySelector('[data-action="visor-prev"]')?.addEventListener('click', () => mover(-1));
  capa.querySelector('[data-action="visor-next"]')?.addEventListener('click', () => mover(1));
  document.addEventListener('keydown', (e) => {
    if (!capa.classList.contains('abierto')) return;
    if (e.key === 'Escape') cerrar();
    if (e.key === 'ArrowRight') mover(1);
    if (e.key === 'ArrowLeft') mover(-1);
  });
})();
