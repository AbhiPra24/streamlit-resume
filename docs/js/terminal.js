/* Terminal typewriter animation — ported verbatim from app/components/terminal.py's
   TERMINAL_HTML <script> block. Keep the SEQUENCES array in sync manually if the
   Streamlit app's terminal script changes. */
(function () {
  const SEQUENCES = [
    { type: 'cmd',  text: 'whoami' },
    { type: 'out',  text: 'abhipra24', color: '#00d4ff' },
    { type: 'cmd',  text: 'cat title.txt' },
    { type: 'out',  text: 'Senior SDET & AI Automation Engineer', color: '#a78bfa' },
    { type: 'cmd',  text: 'experience --years' },
    { type: 'out',  text: '[+] 5 years @ ChargePoint (Gurugram, India)', color: '#10b981' },
    { type: 'out',  text: '[+] Programmer Analyst @ Cognizant', color: '#10b981' },
    { type: 'cmd',  text: 'ls skills/' },
    { type: 'out',  text: 'Python/   Playwright/   FastAPI/   MCP/   Docker/', color: '#f9c74f' },
    { type: 'out',  text: 'Jenkins/  Burp-Suite/   LangChain/ Pytest/ Streamlit/', color: '#f9c74f' },
    { type: 'cmd',  text: './init_ai_stack.sh' },
    { type: 'out',  text: '[✓] MCP Server — exposing private docs to LLMs…', color: '#10b981' },
    { type: 'out',  text: '[✓] Gemini CLI agent initialized…', color: '#10b981' },
    { type: 'out',  text: '[✓] DevUtils & ARM running on :8080', color: '#10b981' },
    { type: 'out',  text: '[✓] Playwright headless suite ready', color: '#10b981' },
    { type: 'cmd',  text: 'git log --oneline -5' },
    { type: 'out',  text: 'a1b2c3d  feat: AI agent ecosystem & MCP servers', color: '#8b5cf6' },
    { type: 'out',  text: 'e4f5g6h  feat: 40% faster regression w/ LLM CI analysis', color: '#8b5cf6' },
    { type: 'out',  text: 'i7j8k9l  feat: Playwright framework (-25% manual effort)', color: '#8b5cf6' },
    { type: 'out',  text: 'm1n2o3p  feat: DevUtils toolbox for EV charging systems', color: '#8b5cf6' },
    { type: 'out',  text: 'q4r5s6t  init: Selenium+Java automation @ Cognizant', color: '#8b5cf6' },
    { type: 'cmd',  text: 'echo "Open to exciting opportunities!"' },
    { type: 'out',  text: 'Open to exciting opportunities!', color: '#00d4ff' },
  ];

  const CHAR_DELAY = 45;
  const CHAR_JITTER = 35;
  const LINE_PAUSE = 280;

  function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

  function makePromptEl(tbody) {
    const el = document.createElement('div');
    el.className = 'line';
    el.innerHTML =
      '<span class="prompt-host">abhipra24</span>' +
      '<span class="prompt-sep">@</span>' +
      '<span class="prompt-path">portfolio</span>' +
      '<span class="prompt-sep">:~$ </span>' +
      '<span class="cmd-text" id="ct"></span>' +
      '<span class="cursor" id="cur"></span>';
    tbody.appendChild(el);
    return { cmdEl: el.querySelector('#ct'), curEl: el.querySelector('#cur') };
  }

  function makeOutEl(tbody, text, color) {
    const el = document.createElement('div');
    el.className = 'line out';
    el.style.color = color || '#8b949e';
    el.textContent = text;
    tbody.appendChild(el);
    tbody.scrollTop = tbody.scrollHeight;
  }

  async function run(tbody) {
    await sleep(600);
    for (const seq of SEQUENCES) {
      if (seq.type === 'cmd') {
        const { cmdEl, curEl } = makePromptEl(tbody);
        for (const ch of seq.text) {
          cmdEl.textContent += ch;
          tbody.scrollTop = tbody.scrollHeight;
          await sleep(CHAR_DELAY + Math.random() * CHAR_JITTER);
        }
        curEl.remove();
        await sleep(LINE_PAUSE);
      } else {
        await sleep(80);
        makeOutEl(tbody, seq.text, seq.color);
        await sleep(100);
      }
    }
    const final = document.createElement('div');
    final.className = 'line';
    final.innerHTML =
      '<span class="prompt-host">abhipra24</span>' +
      '<span class="prompt-sep">@</span>' +
      '<span class="prompt-path">portfolio</span>' +
      '<span class="prompt-sep">:~$ </span>' +
      '<span class="cursor"></span>';
    tbody.appendChild(final);
    tbody.scrollTop = tbody.scrollHeight;
  }

  document.addEventListener('DOMContentLoaded', () => {
    const tbody = document.getElementById('tbody');
    if (tbody) run(tbody);
  });
})();
