---
name: fontes-premium
description: Sistema de tipografia premium para landing pages (pareamento de fontes, escala responsiva e teste visual). Use ao escolher, trocar ou aplicar fontes em uma LP, ao pedir um visual "premium/editorial/luxo", ou ao corrigir tamanhos e proporções de texto em desktop, tablet e mobile.
---

# Fontes premium para landing page

Baseada em duas referências: "Font Pairing Formula" (regras de combinação) e "Font Pairings that prove opposites attract" (contraste de estilo/peso/largura).

## 1. Fórmula de combinação

| Combinação | Resultado |
|---|---|
| Serif + Sans | ✅ clássico, seguro (títulos serif, texto sans) |
| Serif + Script | ✅ elegante (script só como acento) |
| Sans + Sans | ✅ só se houver forte contraste de peso/largura (ex.: condensada pesada + sans leve) |
| Sans + Script | ✅ marca/títulos de impacto |
| Sans + Serif | ✅ |
| Script + Script | ❌ nunca: ilegível e briga por atenção |
| Serif + Serif | ❌ nunca: parece erro, sem hierarquia |

**Princípio "opposites attract":** cada par precisa de contraste claro em pelo menos 2 eixos: estilo (serif/sans/script), peso (fino/pesado), largura (condensada/larga), inclinação (romana/itálica).

## 2. Papéis (máx. 4 vozes, 3 por tela)

| Papel | Uso | Regra |
|---|---|---|
| Serif display | h1, h2, h3, frases de destaque, FAQ | peso 500; itálico para a palavra-chave |
| Sans de texto | parágrafos, eyebrow, botões, UI | 400–700; entrelinha 1.6–1.7 |
| Script | UM acento por seção (palavra-chave do hero, nome do método, frase de fechamento) | nunca em parágrafo; nunca abaixo de ~40px; sem letter-spacing |
| Impact condensada | números, datas, preços, nome da marca, títulos curtos em caixa-alta | só CAIXA-ALTA e textos curtos; letter-spacing +.02 a +.08em |

## 3. Pares prontos (equivalentes Google Fonts gratuitos)

Referência → equivalente livre:
- Times New Roman Condensed + Akzidenz-Grotesk → **Playfair Display + Work Sans**
- Lavonia Classy + August (script + condensada) → **Pinyon Script + Bebas Neue**
- Libre Baskerville + Work Sans → **Libre Baskerville + Work Sans** (original, gratuito)
- Mirador + Outfit (serif + sans) → **Playfair Display + Outfit**
- Cy Grotesk + Monument → **Space Grotesk + Archivo (800)**
- Amoresa + Perandory → **Pinyon Script / Cormorant Garamond + Cormorant SC**

Padrão usado em LP premium escura/dourada (testado): 
`Playfair Display (400/500/600 + itálico 400/500)`, `Work Sans (400–700)`, `Pinyon Script`, `Bebas Neue`.

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Work+Sans:wght@400;500;600;700&family=Bebas+Neue&family=Pinyon+Script&display=swap" rel="stylesheet">
```
```css
:root{
  --serif:'Playfair Display',Georgia,serif;
  --sans:'Work Sans',system-ui,sans-serif;
  --script:'Pinyon Script','Snell Roundhand',cursive;
  --impact:'Bebas Neue','Arial Narrow',Impact,sans-serif;
}
```

## 4. Escala responsiva testada (clamp)

Cada fonte tem tamanho óptico diferente: compense.

| Elemento | Fonte | clamp |
|---|---|---|
| h1 hero | serif 500, lh 1.02, ls -.02em | `clamp(34px,6.4vw,100px)`; mobile `clamp(34px,10.4vw,52px)` |
| palavra script no h1 | script | `1.22em` do h1, lh .8, `padding:0 .12em .1em 0` |
| h2 | serif 500, lh 1.08, ls -.012em | `clamp(30px,4.8vw,62px)` |
| nome do método (VIDA) | impact, lh .8, ls .03em | `clamp(110px,26vw,340px)` |
| subtítulo script do método | script, `margin:-.28em 0 22px` (encosta no impact) | `clamp(40px,8vw,104px)`, `white-space:nowrap` |
| títulos de card | impact caixa-alta, lh 1 | `clamp(40px,4.4vw,60px)` |
| data / preço grande | impact | `clamp(76px,17vw,250px)` / preço `96px` (mobile `76px`) |
| fechamento script | script, lh 1.15 | `clamp(44px,7.5vw,104px)`; mobile `40px` |
| frases serif de apoio | serif, lh 1.25–1.35 | `clamp(20px,2.3vw,28px)` |
| FAQ (summary) | serif | `clamp(19px,2vw,24px)` |
| corpo | sans, lh 1.65 | 17px (mobile 16.5px) |
| botão | sans 700 caixa-alta | 14px ls .1em; mobile 13px ls .06em, `text-align:center` |

Regras de proporção:
- Impact (Bebas) parece ~15% menor que serif no mesmo px: use tamanho maior.
- Serif display de alto contraste (Playfair) é largo: reduza ~10–15% vs. Fraunces/Georgia e use `letter-spacing` mais próximo de 0.
- Script precisa de respiro: `line-height ≥ 1.1` e `padding` direito para a serifa final não ser cortada (obrigatório com `background-clip:text` em degradê).
- Texto em degradê (`background-clip:text`) → `-webkit-text-fill-color:transparent`.
- Nunca deixe a ordem das seções mudar entre breakpoints; só mude colunas → 1 coluna.

## 5. Como testar (obrigatório antes de entregar)

O Chrome headless não reduz a janela abaixo de ~500px, então a captura "mobile" direta vaza. Use um iframe com a largura exata do aparelho:

`python .claude/skills/fontes-premium/scripts/shoot.py <pasta_saida> <arquivo.html>`

Gera páginas inteiras e fatias legíveis (`d_00.png`, `t_00.png`, `m_00.png`...) em 1440 (desktop), 1024, 820 (tablet) e 390 (mobile). Requer Pillow (`pip install pillow`) e Chrome. Depois leia as fatias e confira: quebras de linha feias, sobreposição script/impact, corte de serifas, botões com texto quebrado, cards sobrepostos, ordem das seções.

## 6. Checklist

- [ ] Nenhum par script+script ou serif+serif
- [ ] Script só em 1 acento por seção e ≥ 40px
- [ ] Impact só em caixa-alta/números
- [ ] Contraste do texto em degradê dourado sobre fundo escuro
- [ ] h1 em no máx. 3 linhas desktop / 4 mobile
- [ ] Sem scroll horizontal em 390px
- [ ] `font-display:swap` e preconnect do Google Fonts
