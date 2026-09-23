import json, os
from generar import pagina, escribir, RAIZ
from datos_proyectos import PROYECTOS

# ---------- Galería /proyectos/ ----------
tarjetas = []
for slug, p in PROYECTOS.items():
    mini = p["miniatura"].replace("../../", "../")
    tarjetas.append(f'''
      <a class="tarjeta-proyecto" href="{slug}/" data-tipo="{p['tipo']}">
        <div class="miniatura"><img src="{mini}" alt="{p['titulo']}" loading="lazy" width="600" height="375"></div>
        <div class="cuerpo">
          <div class="chips"><span class="chip {p['chip']}">{p['chip_texto']}</span><span class="chip">{p['tipo']}</span></div>
          <h3>{p['titulo']}</h3>
          <p>{p['resumen']}</p>
          <span class="ver">Ver el sistema →</span>
        </div>
      </a>''')

cuerpo_galeria = f'''
  <section class="seccion" style="padding-top:var(--s-8)">
    <div class="contenedor">
      <div class="seccion-cabecera">
        <p class="etiqueta">Proyectos</p>
        <h2>Sistemas en uso, no maquetas</h2>
        <p>Siete piezas: cuatro para clientes reales, una herramienta propia, una demostración y el sistema que publica mis propias redes. Cada una rotulada como lo que es.</p>
      </div>
      <div class="proyectos-grid tres">{''.join(tarjetas)}
      </div>
      <div class="centro" style="margin-top:var(--s-7)">
        <a class="btn btn-primario" href="../#contacto">Hablemos de tu proceso</a>
      </div>
    </div>
  </section>
'''
escribir(
    os.path.join(RAIZ, "proyectos", "index.html"),
    pagina(
        rel="../",
        titulo="Proyectos — MPAI Technologies",
        descripcion="Siete sistemas: cuatro para clientes reales, una herramienta propia, una demostración y el sistema que publica mis propias redes.",
        url_canon="https://mpaitechnologies.es/proyectos/",
        cuerpo=cuerpo_galeria,
        activo="proyectos",
    ),
)

# ---------- Fichas /proyectos/<slug>/ ----------
for slug, p in PROYECTOS.items():
    hecho_html = "".join(f"<li>{h}</li>" for h in p["hecho"])
    cita_html = f'''
      <div class="peldano" style="margin-top:var(--s-6);border-color:var(--acento)">
        <span class="n">Caso real</span>
        <p style="color:var(--blanco);font-size:15px;margin-top:var(--s-2)">{p['cita']}</p>
      </div>''' if p.get("cita") else ""

    pases = [{"src": g["src"].replace("../../", "../../"), "pie": g["pie"]} for g in p["galeria"]]
    datos_json = json.dumps({"titulo": p["titulo"], "pases": pases}, ensure_ascii=False)

    galeria_grid = "".join(f'''
        <button class="tarjeta-proyecto" style="text-align:left" data-galeria="datos-{slug}" data-pase="{i}">
          <div class="miniatura"><img src="{g['src']}" alt="{g['pie']}" loading="lazy" width="600" height="375"></div>
          <div class="cuerpo"><p style="font-size:14px">{g['pie']}</p></div>
        </button>''' for i, g in enumerate(p["galeria"]))

    videos_html = ""
    if p.get("videos"):
        videos_html = '<div class="seccion-cabecera" style="margin-top:var(--s-7)"><p class="etiqueta">En vídeo</p></div><div class="proyectos-grid">' + "".join(
            f'''<div><video controls preload="none" playsinline poster="{v['poster']}" style="border:1px solid var(--linea);border-radius:var(--radio-grande)"><source src="{v['src']}" type="video/mp4"></video><p style="margin-top:var(--s-2);color:var(--gris);font-size:14px">{v['titulo']}</p></div>'''
            for v in p["videos"]
        ) + "</div>"

    cuerpo = f'''
  <section class="seccion" style="padding-top:var(--s-8)">
    <div class="contenedor">
      <p class="etiqueta"><a href="../" style="color:var(--acento)">← Todos los proyectos</a></p>
      <div class="chips" style="margin-top:var(--s-5)"><span class="chip {p['chip']}">{p['chip_texto']}</span><span class="chip">{p['tipo']}</span></div>
      <h1 style="font-size:clamp(30px,5vw,48px);margin-top:var(--s-3);max-width:760px">{p['titulo']}</h1>
      <p style="color:var(--gris);font-size:19px;margin-top:var(--s-4);max-width:640px">{p['problema']}</p>

      <div class="proyectos-grid" style="margin-top:var(--s-7)">{galeria_grid}
      </div>

      <div style="max-width:720px;margin-top:var(--s-8)">
        <p class="etiqueta">Qué se hizo</p>
        <ul style="margin-top:var(--s-4);padding-left:20px;display:grid;gap:var(--s-3);color:#d5d5da;font-size:16px">{hecho_html}</ul>
        <p class="etiqueta" style="margin-top:var(--s-7)">Resultado</p>
        <p style="margin-top:var(--s-3);font-size:17px">{p['resultado']}</p>
        {cita_html}
      </div>
      {videos_html}
      <div style="margin-top:var(--s-8)">
        <a class="btn btn-primario" href="https://wa.me/34931525368?text=Hola%2C%20he%20visto%20{slug}%20en%20la%20web%20y%20quiero%20algo%20parecido" target="_blank" rel="noopener">{p['cta']}</a>
      </div>
    </div>
  </section>
  <script type="application/json" id="datos-{slug}">{datos_json}</script>
'''
    escribir(
        os.path.join(RAIZ, "proyectos", slug, "index.html"),
        pagina(
            rel="../../",
            titulo=f"{p['titulo']} — Proyectos MPAI Technologies",
            descripcion=p["resumen"],
            url_canon=f"https://mpaitechnologies.es/proyectos/{slug}/",
            cuerpo=cuerpo,
            activo="proyectos",
        ),
    )

print("Listo.")
