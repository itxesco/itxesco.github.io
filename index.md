<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Início</title>
    <meta name="description" content="Página inicial do site de Itxesco - Ensino, Pesquisa, Extensão e mais." />
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  </head>
  <body class="bg-[#F5F5F5] text-[#4B5563] font-sans leading-relaxed min-h-screen flex flex-col">

    <!-- Navbar fixa no topo -->
    <header class="bg-[#003865] text-white shadow-md py-4">
      <nav class="max-w-6xl mx-auto flex justify-between items-center px-4">
        <h1 class="text-xl font-semibold">Itxesco</h1>
        <ul class="flex space-x-6 text-sm sm:text-base">
          <li><a href="/index.html" class="hover:underline">Início</a></li>
          <li><a href="/pages/sobre.html" class="hover:underline">Sobre</a></li>
          <li><a href="/pages/ensino/ensino.html" class="hover:underline">Ensino</a></li>
          <li><a href="/pages/autismo/autismo.html" class="hover:underline">TEA</a></li>
        </ul>
      </nav>
    </header>

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

        <!-- Hiperfocos / Quadrinhos -->
        <div class="text-center">
          <a href="pages/index/index_hq.html">
            <img src="imagens/index_pics/hiperfocos.png" alt="Sobre Histórias em Quadrinhos" title="Hiperfocos"
              class="w-full max-w-xs h-[300px] object-cover rounded shadow-md hover:scale-105 transition-transform duration-300">
          </a><br>
          <strong><a href="pages/index/index_hq.html" class="text-blue-700 hover:underline">Histórias em Quadrinhos</a></strong>
        </div>

        <!-- Autismo -->
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
    <footer class="bg-[#003865] text-white text-center py-3 text-sm">
      <p>&copy; 2024 Francisco Nascimento | Projeto Itxesco</p>
    </footer>

  </body>
</html>
