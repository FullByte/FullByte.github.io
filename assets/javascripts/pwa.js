// PWA Installation and Service Worker Registration
document.addEventListener('DOMContentLoaded', function() {
    // Register service worker
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js')
                .then(registration => {
                    console.log('SW registered: ', registration);
                })
                .catch(registrationError => {
                    console.log('SW registration failed: ', registrationError);
                });
        });
    }

    // PWA Install Prompt
    let deferredPrompt;
    
    window.addEventListener('beforeinstallprompt', (e) => {
        // Prevent Chrome 67 and earlier from automatically showing the prompt
        e.preventDefault();
        // Stash the event so it can be triggered later
        deferredPrompt = e;
        // Show install button
        showInstallButton();
    });

    function showInstallButton() {
        const installButton = document.createElement('button');
        installButton.innerHTML = '📱 Install App';
        installButton.className = 'md-button md-button--primary pwa-install-button';
        installButton.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            border-radius: 50px;
            padding: 10px 20px;
            background: var(--md-primary-fg-color);
            color: var(--md-primary-bg-color);
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            font-size: 14px;
            display: none;
        `;

        installButton.addEventListener('click', async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                if (outcome === 'accepted') {
                    console.log('User accepted the install prompt');
                    installButton.style.display = 'none';
                } else {
                    console.log('User dismissed the install prompt');
                }
                deferredPrompt = null;
            }
        });

        document.body.appendChild(installButton);
        
        // Show button after a delay
        setTimeout(() => {
            installButton.style.display = 'block';
        }, 3000);
    }

    // Handle PWA installation
    window.addEventListener('appinstalled', (evt) => {
        console.log('PWA was installed');
        const installButton = document.querySelector('.pwa-install-button');
        if (installButton) {
            installButton.style.display = 'none';
        }
    });
});
