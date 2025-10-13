(function () {
  // Toasts: small, accessible notifications
  const container = document.getElementById('toast-container');
  if (!container) return;

  const levelMap = {
    '50': 'bg-red-700 text-white',   // CRITICAL
    '40': 'bg-red-600 text-white',   // ERROR
    '30': 'bg-yellow-600 text-black',// WARNING
    '25': 'bg-blue-600 text-white',  // INFO
    '20': 'bg-green-600 text-white'  // SUCCESS
  };

  function buildToast(text, level = '25', timeout = 5000) {
    const levelClass = levelMap[String(level)] || 'bg-gray-800 text-white';
    const toast = document.createElement('div');
    toast.className = `max-w-md w-full pointer-events-auto rounded-md shadow-lg ${levelClass} px-4 py-3 flex items-start gap-3 transition-opacity duration-200`;
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');

    const messageP = document.createElement('div');
    messageP.className = 'text-sm';
    messageP.innerText = text;

    const closeBtn = document.createElement('button');
    closeBtn.className = 'ml-4 text-white opacity-90 hover:opacity-100 focus:outline-none';
    closeBtn.setAttribute('aria-label', 'Close notification');
    closeBtn.innerHTML = '\u00d7';
    closeBtn.addEventListener('click', () => removeToast(toast));

    toast.appendChild(messageP);
    toast.appendChild(closeBtn);

    // auto-dismiss
    let timer = setTimeout(() => removeToast(toast), timeout);

    // pause on hover
    toast.addEventListener('mouseenter', () => clearTimeout(timer));
    toast.addEventListener('mouseleave', () => (timer = setTimeout(() => removeToast(toast), timeout)));

    return toast;
  }

  function removeToast(node) {
    if (!node) return;
    node.style.opacity = '0';
    setTimeout(() => node.remove(), 220);
  }

  // initialize existing messages rendered server-side
  const initial = document.getElementById('initial-messages');
  if (initial) {
    const children = Array.from(initial.children);
    children.forEach(div => {
      const text = div.dataset.messageText || div.getAttribute('data-message-text') || div.textContent || '';
      const level = div.dataset.messageLevel || '25';
      const toast = buildToast(text, level);
      container.appendChild(toast);
    });
    initial.remove();
  }

  // Public API
  window.showToast = function (text, level = '25', timeout = 5000) {
    const toast = buildToast(text, String(level), timeout);
    container.appendChild(toast);
  };
})();
