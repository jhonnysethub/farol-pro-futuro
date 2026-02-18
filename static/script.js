// static/script.js (VERSÃO FINAL E CORRETA)

function toggleMoreInfo(buttonElement) {
  // Pega o ID a partir do atributo 'data-id' do botão que foi clicado
  const cursoId = buttonElement.dataset.id;

  // Encontra o div de detalhes correspondente
  const moreInfoDiv = document.getElementById(`more-info-${cursoId}`);
  const isVisible = moreInfoDiv.style.display !== "none";

  // Alterna a visibilidade do div
  moreInfoDiv.style.display = isVisible ? "none" : "block";

  // Atualiza o texto do botão que foi clicado
  buttonElement.innerHTML = isVisible
    ? "MAIS INFORMAÇÕES ▼"
    : "MENOS INFORMAÇÕES ▲";
}

// Efeitos visuais (opcional, mas recomendado)
document.addEventListener("DOMContentLoaded", function () {
  const inputs = document.querySelectorAll("input, textarea, select");
  inputs.forEach((input) => {
    input.addEventListener("focus", function () {
      this.style.boxShadow = "0 0 0 3px rgba(232, 141, 103, 0.25)"; // Usando a cor primária com transparência
      this.style.transition = "box-shadow 0.2s";
    });

    input.addEventListener("blur", function () {
      this.style.boxShadow = "none";
    });
  });
});
