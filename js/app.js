// MPAI Technologies — interacción de la web (sin dependencias externas)
'use strict';
document.documentElement.classList.add('js');

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

const reduceMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const esperar = (ms) => new Promise((r) => setTimeout(r, reduceMovimiento ? Math.min(ms, 150) : ms));

/* ---------- Aparición suave al hacer scroll ---------- */
(function aparicion() {
  const els = document.querySelectorAll('.aparece');
  if (!('IntersectionObserver' in window)) { els.forEach((e) => e.classList.add('visible')); return; }
  const io = new IntersectionObserver((entradas) => {
    entradas.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
  }, { threshold: .05, rootMargin: '0px 0px -40px 0px' });
  els.forEach((e) => io.observe(e));
})();

/* ---------- FAQ: botón «Descubre» por pregunta ---------- */
(function faqDescubre() {
  const botones = document.querySelectorAll('[data-action="faq"]');
  const cerrar = (b) => {
    b.setAttribute('aria-expanded', 'false');
    b.querySelector('.faq-boton-texto').textContent = 'Descubre';
    document.getElementById(b.getAttribute('aria-controls')).hidden = true;
    b.closest('.faq-tarjeta').classList.remove('abierta');
  };
  botones.forEach((b) => {
    b.addEventListener('click', () => {
      const abierta = b.getAttribute('aria-expanded') === 'true';
      botones.forEach(cerrar);
      if (abierta) return;
      b.setAttribute('aria-expanded', 'true');
      b.querySelector('.faq-boton-texto').textContent = 'Ocultar';
      document.getElementById(b.getAttribute('aria-controls')).hidden = false;
      b.closest('.faq-tarjeta').classList.add('abierta');
    });
  });
})();

/* ---------- Circuito (flujo real de respaldo de Instagram) ---------- */
(function circuito() {
  const flujo = document.querySelector('#flujo');
  const leyenda = document.querySelector('#circuito-leyenda');
  const estado = document.querySelector('#circuito-estado');
  const boton = document.querySelector('[data-action="ver-circuito"]');
  if (!flujo) return;
  const nodos = [...flujo.querySelectorAll('.flujo-nodo')];
  const finalOk = document.querySelector('.final.ok');
  const texto = (n) => ({ t: n.querySelector('strong').textContent, d: n.querySelector('.flujo-desc').textContent });
  const pintarLeyenda = (titulo, desc) => {
    leyenda.textContent = '';
    const b = document.createElement('strong'); b.textContent = titulo + ' ';
    leyenda.append(b, desc);
  };
  const ponerEstado = (clase, txt) => { estado.className = 'circuito-estado ' + clase; estado.textContent = txt; };

  let animando = false;
  async function recorrer() {
    if (animando) return;
    animando = true;
    if (boton) boton.disabled = true;
    nodos.forEach((n) => n.classList.remove('activo', 'hecho'));
    finalOk?.classList.remove('encendido');
    ponerEstado('en-marcha', 'en marcha');
    for (let k = 0; k < nodos.length; k++) {
      if (k > 0) { nodos[k - 1].classList.remove('activo'); nodos[k - 1].classList.add('hecho'); }
      nodos[k].classList.add('activo');
      const { t, d } = texto(nodos[k]);
      pintarLeyenda(`${k + 1}/9 · ${t}`, d);
      await esperar(1100);
    }
    nodos[nodos.length - 1].classList.remove('activo');
    nodos[nodos.length - 1].classList.add('hecho');
    finalOk?.classList.add('encendido');
    ponerEstado('completado', 'completado');
    pintarLeyenda('Recorrido completo.', 'Publicación rescatada y comprobada antes de avisar. Es el flujo real que respalda mis publicaciones diarias.');
    if (boton) { boton.disabled = false; boton.textContent = '↻ Ver otra vez'; }
    animando = false;
  }
  boton?.addEventListener('click', recorrer);

  // tocar un paso lo ilumina y lo explica
  nodos.forEach((n) => {
    n.querySelector('.flujo-boton').addEventListener('click', () => {
      if (animando) return;
      nodos.forEach((o) => o.classList.remove('activo'));
      n.classList.add('activo');
      const { t, d } = texto(n);
      pintarLeyenda(`${Number(n.dataset.paso) + 1}/9 · ${t}`, d);
    });
  });

  // arranca solo la primera vez que se ve (si no se ha pedido reducir movimiento)
  if (!reduceMovimiento && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entradas) => {
      entradas.forEach((e) => { if (e.isIntersecting) { recorrer(); io.disconnect(); } });
    }, { threshold: .35 });
    io.observe(flujo);
  }
})();

/* ---------- Chat del agente (guionizado) ---------- */
(function chatAgente() {
  const hilo = document.querySelector('#chat-hilo');
  const opciones = document.querySelector('#chat-opciones');
  const estadoChat = document.querySelector('#chat-estado');
  const pasosLista = document.querySelectorAll('.agente-pasos li');
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

  // qué tarjeta de la izquierda se ilumina según el tipo de mensaje
  const tarjetaPorTipo = { paso: 0, agente: 1, humano: 2 };
  const marcarPaso = (idx) => pasosLista.forEach((li, k) => li.classList.toggle('activo', k === idx));

  function burbuja(tipo, texto) {
    const div = document.createElement('div');
    div.className = 'burbuja ' + tipo;
    div.textContent = texto;
    hilo.appendChild(div);
    hilo.scrollTop = hilo.scrollHeight;
    return div;
  }
  async function escribiendo(ms) {
    const div = document.createElement('div');
    div.className = 'burbuja escribiendo';
    div.setAttribute('aria-label', 'Escribiendo');
    for (let k = 0; k < 3; k++) div.appendChild(document.createElement('span'));
    hilo.appendChild(div);
    hilo.scrollTop = hilo.scrollHeight;
    if (estadoChat) estadoChat.textContent = 'escribiendo…';
    await esperar(ms);
    div.remove();
    if (estadoChat) estadoChat.textContent = 'en línea';
  }

  let ocupado = false;
  async function ejecutar(clave) {
    const guion = guiones[clave];
    if (!guion || ocupado) return;
    ocupado = true;
    opciones.querySelectorAll('button').forEach((b) => (b.disabled = true));
    hilo.textContent = '';
    burbuja('cliente', guion.pregunta);
    await esperar(500);
    for (const paso of guion.pasos) {
      marcarPaso(tarjetaPorTipo[paso.tipo]);
      if (paso.tipo === 'paso') { await esperar(400); burbuja('paso', paso.texto); await esperar(700); }
      else { await escribiendo(1000); burbuja(paso.tipo, paso.texto); await esperar(500); }
    }
    opciones.querySelectorAll('button').forEach((b) => (b.disabled = false));
    ocupado = false;
  }

  opciones.querySelectorAll('[data-chat]').forEach((b) => {
    b.addEventListener('click', () => ejecutar(b.getAttribute('data-chat')));
  });
  burbuja('agente', 'Hola, soy el asistente del despacho. Toca una de las preguntas de abajo y mira cómo respondo.');
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
