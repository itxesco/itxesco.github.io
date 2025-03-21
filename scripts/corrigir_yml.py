import os

def corrigir_yaml_front_matter(conteudo):
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
    return conteudo

# Caminho da pasta onde estão os arquivos .md
root_dir = "./pages"

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            caminho = os.path.join(subdir, file)
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()
            novo_conteudo = corrigir_yaml_front_matter(conteudo)
            if novo_conteudo != conteudo:
                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(novo_conteudo)
                print(f"✔ YAML corrigido em: {caminho}")
