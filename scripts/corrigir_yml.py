import os

def gerar_front_matter_default(nome_arquivo):
    nome_base = os.path.splitext(os.path.basename(nome_arquivo))[0]
    title = nome_base.replace("_", " ").title()
    return f"""---
title: "{title}"
layout: page
---
"""

def corrigir_yaml_front_matter(conteudo, nome_arquivo):
    if conteudo.startswith("---"):
        partes = conteudo.split("---", 2)
        if len(partes) >= 3:
            yaml = partes[1]
            markdown = partes[2]

            linhas_corrigidas = []
            for linha in yaml.splitlines():
                if ":" in linha and not linha.strip().startswith("#"):
                    chave, valor = linha.split(":", 1)
                    valor = valor.strip()
                    if not (valor.startswith('"') and valor.endswith('"')) and (":" in valor or '"' in valor or "'" in valor):
                        valor = f'"{valor}"'
                    linhas_corrigidas.append(f"{chave.strip()}: {valor}")
                else:
                    linhas_corrigidas.append(linha)

            yaml_corrigido = "\n".join(linhas_corrigidas)
            return f"---\n{yaml_corrigido}\n---\n{markdown.lstrip()}"
        else:
            # YAML mal formatado: reescreve com default
            return gerar_front_matter_default(nome_arquivo) + conteudo.replace("---", "").strip()
    else:
        # Não tem front matter: adiciona
        return gerar_front_matter_default(nome_arquivo) + "\n" + conteudo

def processar_arquivos_md(diretorio_raiz="."):
    for subdir, _, files in os.walk(diretorio_raiz):
        for file in files:
            if file.endswith(".md"):
                caminho = os.path.join(subdir, file)
                with open(caminho, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                novo_conteudo = corrigir_yaml_front_matter(conteudo, caminho)

                if novo_conteudo != conteudo:
                    with open(caminho, "w", encoding="utf-8") as f:
                        f.write(novo_conteudo)
                    print(f"✔ Corrigido: {caminho}")
                else:
                    print(f"✓ OK: {caminho}")

# 🏁 Altere aqui o caminho se quiser rodar fora da raiz
processar_arquivos_md("./pages")
