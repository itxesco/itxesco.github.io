<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Início</title>
    <meta name="description" content="Página inicial do site de Itxesco - Ensino, Pesquisa, Extensão e mais.">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet" />
  </head>
  <body class="bg-[#F5F5F5] text-[#4B5563] font-sans min-h-screen flex flex-col">

    <!-- Barra de navegação -->
    <nav class="bg-[#003865] text-white p-4 shadow-md">
      <div class="container mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
        <span class="text-lg font-semibold">Prof. Dr. Francisco Nascimento</span>
        <div class="space-x-4 text-sm">
          <a href="/" class="hover:underline">Início</a>
          <a href="/pages/baixar/ensino.html" class="hover:underline">Publicações</a>
          <a href="/pages/baixar/baixar.html" class="hover:underline">Downloads</a>
          <a href="/pages/baixar/sobre.html" class="hover:underline">Sobre</a>
          <a href="/pages/baixar/linksuteis.html" class="hover:underline">Links úteis</a>
        </div>
      </div>
    </nav>

    <!-- Conteúdo principal -->
    <main class="flex-grow">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 justify-items-center px-4 py-8">

        <!-- Ensino -->
        <div class="text-center">
          <a href="pages/index/index_ensino.html">
            <img src="imagens/index_pics/ensino.jpeg" alt="Atividades de Ensino" title="Ensino"
              class="w-full max-w-xs h-[300px] object-cover rounded shadow-md hover:scale-105 transition-transform duration-300">
          </a><br>
          <strong><a href="pages/index/index_ensino.html" class="text-blue-700 hover:underline">Ensino</a></strong>
        </div>

        <!-- Pesquisa -->
        <div class="text-center">
          <a href="pages/index/index_pesquisa.html">
            <img src="imagens/index_pics/pesquisa.jpeg" alt="Atividades de Pesquisa" title="Interesses de Pesquisa"
              class="w-full max-w-xs h-[300px] object-cover rounded shadow-md hover:scale-105 transition-transform duration-300">
          </a><br>
          <strong><a href="pages/index/index_pesquisa.html" class="text-blue-700 hover:underline">Pesquisa</a></strong>
        </div>

        <!-- Extensão -->
        <div class="text-center">
          <a href="pages/index/index_extensao.html">
            <img src="imagens/index_pics/extensao.jpeg" alt="Atividades de Extensão" title="Atividades de Extensão Universitária"
              class="w-full max-w-xs h-[300px] object-cover rounded shadow-md hover:scale-105 transition-transform duration-300">
          </a><br>
          <strong><a href="pages/index/index_extensao.html" class="text-blue-700 hover:underline">Extensão</a></strong>
        </div>

        <!-- HQ -->
        <div class="text-center">
          <a href="pages/index/index_hq.html">
            <img src="imagens/index_pics/hiperfocos.png" alt="Sobre Histórias em Quadrinhos" title="Hiperfocos"
              class="w-full max-w-xs h-[300px] object-cover rounded shadow-md hover:scale-105 transition-transform duration-300">
          </a><br>
          <strong><a href="pages/index/index_hq.html" class="text-blue-700 hover:underline">Histórias em Quadrinhos</a></strong>
        </div>

        <!-- TEA -->
        <div class="text-center">
          <a href="pages/index/index_tea_adultos.html">
            <img src="imagens/index_pics/cyclope_tea.png" alt="Autismo em Adultos" title="Autismo em Adultos"
              class="w-full max-w-xs h-[300px] object-cover rounded shadow-md hover:scale-105 transition-transform duration-300">
          </a><br>
          <strong><a href="pages/index/index_tea_adultos.html" class="text-blue-700 hover:underline">Autismo em Adultos</a></strong>
        </div>

        <!-- RPG -->
        <div class="text-center">
          <a href="pages/index/index_rpg.html">
            <img src="imagens/index_pics/dragaod20.jpeg" alt="Jogos de RPG e Educação" title="Jogos de RPG"
              class="w-full max-w-xs h-[300px] object-cover rounded shadow-md hover:scale-105 transition-transform duration-300">
          </a><br>
          <strong><a href="pages/index/index_rpg.html" class="text-blue-700 hover:underline">RPG</a></strong>
        </div>

      </div>
    </main>

    <!-- Rodapé fixo -->
    <footer class="bg-[#003865] text-white text-sm text-center py-4">
      <p>2018 Francisco de Assis Nascimento Jr. — Site Pessoal</p>
    </footer>

  </body>
</html>
