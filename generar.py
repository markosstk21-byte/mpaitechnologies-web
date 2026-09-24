#!/usr/bin/env python3
"""Genera las páginas secundarias de mpaitechnologies.es a partir de piezas
comunes (cabecera, pie, script) para no repetir HTML a mano en cada archivo."""
import os

RAIZ = os.path.dirname(os.path.abspath(__file__))

def cabecera(rel, activo=""):
    def cls(nombre):
        return ' style="color:var(--blanco)"' if nombre == activo else ""
    return f'''<header class="cabecera">
  <div class="contenedor cabecera-fila">
    <a href="{rel}#top" class="cabecera-logo"><span class="punto" aria-hidden="true"></span>MPAI Technologies</a>
    <nav class="cabecera-nav" aria-label="Principal">
      <a href="{rel}#como-funciona"{cls('funciona')}>Cómo funciona</a>
      <a href="{rel}proyectos/"{cls('proyectos')}>Proyectos</a>
      <a href="{rel}#sectores"{cls('sectores')}>Sectores</a>
      <a href="{rel}#precios"{cls('precios')}>Precios</a>
    </nav>
    <div class="cabecera-acciones">
      <a class="btn btn-primario" href="{rel}#contacto">Reservar llamada</a>
      <button class="btn btn-secundario cabecera-menu-boton" data-action="abrir-menu" aria-label="Abrir menú">☰</button>
    </div>
  </div>
</header>

<div class="menu-movil" role="dialog" aria-modal="true" aria-label="Menú">
  <div class="menu-movil-cabecera">
    <span class="cabecera-logo"><span class="punto" aria-hidden="true"></span>MPAI Technologies</span>
    <button class="btn btn-secundario" data-action="cerrar-menu" aria-label="Cerrar menú">✕</button>
  </div>
  <nav>
    <a href="{rel}#como-funciona" data-action="cerrar-menu">Cómo funciona</a>
    <a href="{rel}proyectos/" data-action="cerrar-menu">Proyectos</a>
    <a href="{rel}#sectores" data-action="cerrar-menu">Sectores</a>
    <a href="{rel}#precios" data-action="cerrar-menu">Precios</a>
    <a href="{rel}#contacto" data-action="cerrar-menu">Contacto</a>
  </nav>
  <a class="btn btn-primario btn-bloque" href="{rel}#contacto" data-action="cerrar-menu">Reservar llamada</a>
</div>
'''

def pie(rel):
    return f'''<footer>
  <div class="contenedor">
    <div class="footer-grid">
      <div>
        <h4>MPAI Technologies</h4>
        <p>Consultoría de automatización y agentes de IA para pymes españolas. Marco Pavón Cobo, profesional autónomo.</p>
      </div>
      <div>
        <h4>Contacto</h4>
        <a href="https://wa.me/34931525368">WhatsApp — 931 525 368</a>
        <a href="mailto:info@mpaitechnologies.es">info@mpaitechnologies.es</a>
        <a href="mailto:marco@mpaitechnologies.es">marco@mpaitechnologies.es</a>
        <p>Sant Fost de Campsentelles, Barcelona</p>
      </div>
      <div>
        <h4>Navegación</h4>
        <a href="{rel}proyectos/">Proyectos</a>
        <a href="{rel}#sectores">Sectores</a>
        <a href="{rel}#precios">Precios</a>
        <a href="{rel}Checklist de implantacion segura.html">Checklist de implantación</a>
        <a href="{rel}aviso-legal/">Aviso legal</a>
        <a href="{rel}privacidad/">Privacidad</a>
        <a href="{rel}cookies/">Cookies</a>
      </div>
    </div>
    <div class="footer-legal">
      <span>© 2026 MPAI Technologies — Marco Pavón Cobo · NIF 46717689C</span>
      <span><a href="{rel}aviso-legal/" style="color:var(--gris)">Aviso legal</a> · <a href="{rel}privacidad/" style="color:var(--gris)">Privacidad</a> · <a href="{rel}cookies/" style="color:var(--gris)">Cookies</a></span>
    </div>
  </div>
</footer>

<a class="wa-flotante" href="https://wa.me/34931525368" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">
  <svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.85 9.85 0 0 0 4.74 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.8 14.03c-.25.7-1.24 1.28-2.02 1.45-.55.11-1.26.2-3.66-.79-3.07-1.27-5.05-4.4-5.2-4.6-.15-.2-1.24-1.65-1.24-3.15s.78-2.23 1.06-2.53c.26-.28.58-.35.77-.35h.55c.18 0 .42-.03.65.5.25.6.85 2.08.92 2.23.07.15.12.33.02.53-.1.2-.15.32-.3.5-.15.18-.31.4-.44.53-.15.15-.31.31-.13.6.18.3.8 1.32 1.72 2.14 1.18 1.05 2.18 1.38 2.48 1.53.3.15.47.13.65-.08.18-.2.75-.88.95-1.18.2-.3.4-.25.67-.15.28.1 1.75.82 2.05.97.3.15.5.23.57.35.08.13.08.73-.17 1.43z"/></svg>
</a>
'''

def visor(rel):
    return '''<div class="visor" role="dialog" aria-modal="true" aria-label="Pantallas del proyecto">
  <div class="visor-cabecera">
    <div><span class="etiqueta suave">Proyecto</span><h3 class="visor-titulo" style="margin-top:6px"></h3></div>
    <div style="display:flex;align-items:center;gap:var(--s-4)"><span class="visor-posicion etiqueta suave"></span><button class="btn btn-secundario" data-action="cerrar-visor" aria-label="Cerrar">✕</button></div>
  </div>
  <div class="visor-cuerpo">
    <button class="visor-flecha" data-action="visor-prev" aria-label="Anterior">←</button>
    <img src="" alt="">
    <button class="visor-flecha" data-action="visor-next" aria-label="Siguiente">→</button>
  </div>
  <p class="visor-pie"></p>
</div>
'''

def pagina(rel, titulo, descripcion, url_canon, cuerpo, activo="", extra_head=""):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url_canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="{url_canon}">
<meta property="og:image" content="https://mpaitechnologies.es/assets/vista-previa.jpg">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{rel}assets/logo-mpai.png">
<link rel="stylesheet" href="{rel}css/estilos.css">
{extra_head}</head>
<body>
<a href="#contenido" class="solo-lectores">Ir al contenido</a>
{cabecera(rel, activo)}
<main id="contenido">
{cuerpo}
</main>
{pie(rel)}
{visor(rel)}
<script src="{rel}js/app.js"></script>
</body>
</html>
'''

def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    print("escrito:", os.path.relpath(ruta, RAIZ))

if __name__ == "__main__":
    print("Este módulo se importa desde otros scripts de generación.")
