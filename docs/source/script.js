function createPetal() {
  const petal = document.createElement('div');
  petal.classList.add('petal');
  petal.textContent = '🌸'; // You can change this to any character or image
  petal.style.left = Math.random() * window.innerWidth + 'px';
  petal.style.animationDuration = Math.random() * 3 + 2 + 's';
  petal.style.opacity = Math.random();
  petal.style.fontSize = Math.random() * 20 + 10 + 'px';

  document.getElementById('petalContainer').appendChild(petal);

  setTimeout(() => {
    petal.remove();
  }, 5000);
}

setInterval(createPetal, 100);
