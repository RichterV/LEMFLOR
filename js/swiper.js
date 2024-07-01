var swiper = new Swiper('.swiper', {
    pagination: {
      el: '.swiper-pagination',
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    scrollbar: {
      el: '.swiper-scrollbar',
    },
    autoplay: {
      delay: 5000, // Tempo em milissegundos (5 segundos)
      disableOnInteraction: false, // Continua a rotação automática mesmo após interação do usuário
    },
  });