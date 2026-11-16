"""Captura a página inteira em desktop/tablet/mobile via iframe (headless Chrome não reduz abaixo de ~500px).
Uso: python shoot.py <pasta_saida> <arquivo.html>
Requer: Chrome instalado e `pip install pillow`."""
import sys, os, glob, subprocess, pathlib
from PIL import Image

out = pathlib.Path(sys.argv[1]).resolve(); out.mkdir(parents=True, exist_ok=True)
page = pathlib.Path(sys.argv[2]).resolve().as_uri()
CHROME = next((p for p in [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                           r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                           "/usr/bin/google-chrome", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
               if os.path.exists(p)), "chrome")
# (nome, largura, altura máxima da captura, altura de cada fatia)
SIZES = [("d", 1440, 9400, 1100), ("s", 1024, 10200, 1300), ("t", 820, 11000, 1300), ("m", 390, 16000, 1500)]

for n, w, h, step in SIZES:
    frame = out / f"f_{n}.html"
    frame.write_text(f'<body style="margin:0;background:#888"><iframe src="{page}" '
                     f'style="width:{w}px;height:{h}px;border:0;display:block"></iframe>', encoding="utf-8")
    shot = out / f"{n}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--virtual-time-budget=6000", f"--window-size={max(w, 600)},{h}",
                    f"--screenshot={shot}", frame.as_uri()], capture_output=True)
    im = Image.open(shot).crop((0, 0, w, h))
    for f in glob.glob(str(out / f"{n}_*.png")): os.remove(f)
    for i, y in enumerate(range(0, h, step)):
        im.crop((0, y, w, min(y + step, h))).save(out / f"{n}_{i:02d}.png")
    print(n, w, "ok")
