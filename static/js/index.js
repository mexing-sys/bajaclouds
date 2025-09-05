function createParticles() {
            const container = document.body;
            const colors = ['#00ff88', '#ff6b00', '#fff'];

            setInterval(() => {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.background = colors[Math.floor(Math.random() * colors.length)];
                particle.style.animationDuration = (Math.random() * 3 + 4) + 's';
                particle.style.zIndex = '5';

                container.appendChild(particle);

                setTimeout(() => {
                    if (particle.parentNode) particle.parentNode.removeChild(particle);
                }, 7000);
            }, 500);
        }

        document.addEventListener('DOMContentLoaded', function() {
            createParticles();

        });