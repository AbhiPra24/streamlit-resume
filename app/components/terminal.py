"""Interactive terminal component with typewriter animation."""
import streamlit as st
import streamlit as _st


TERMINAL_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { background: transparent; height: 100%; }

  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

  .terminal {
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    background: #0d1117;
    border-radius: 14px;
    border: 1px solid rgba(0,212,255,0.18);
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.03), inset 0 1px 0 rgba(255,255,255,0.04);
  }

  .t-header {
    background: #161b22;
    padding: 11px 16px;
    display: flex;
    align-items: center;
    gap: 7px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    user-select: none;
  }
  .dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
  .dr { background: #ff5f57; box-shadow: 0 0 4px rgba(255,95,87,0.4); }
  .dy { background: #febc2e; box-shadow: 0 0 4px rgba(254,188,46,0.4); }
  .dg { background: #28c840; box-shadow: 0 0 4px rgba(40,200,64,0.4); }
  .t-title {
    color: #6e7681;
    font-size: 12px;
    margin-left: 10px;
    letter-spacing: 0.04em;
  }

  .t-body {
    padding: 20px 22px;
    min-height: 320px;
    max-height: 400px;
    overflow-y: auto;
    scroll-behavior: smooth;
    line-height: 1.9;
    font-size: 13.5px;
  }
  .t-body::-webkit-scrollbar { width: 4px; }
  .t-body::-webkit-scrollbar-track { background: transparent; }
  .t-body::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }

  .line { display: block; }

  .prompt-host { color: #00d4ff; font-weight: 500; }
  .prompt-sep  { color: #6e7681; }
  .prompt-path { color: #10b981; }
  .prompt-sym  { color: #6e7681; }
  .cmd-text    { color: #e6edf3; }

  .cursor {
    display: inline-block;
    width: 7px; height: 15px;
    background: #00d4ff;
    vertical-align: middle;
    margin-left: 1px;
    border-radius: 1px;
    animation: blink 1s step-end infinite;
  }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

  .out { padding-left: 6px; }
</style>
</head>
<body>
<div class="terminal">
  <div class="t-header">
    <div class="dot dr"></div>
    <div class="dot dy"></div>
    <div class="dot dg"></div>
    <span class="t-title">abhipra24@portfolio — bash — 120×30</span>
  </div>
  <div class="t-body" id="tbody"></div>
</div>

<script>
const SEQUENCES = [
  { type:'cmd',  text:'whoami' },
  { type:'out',  text:'abhipra24', color:'#00d4ff' },
  { type:'cmd',  text:'cat title.txt' },
  { type:'out',  text:'Senior SDET & AI Automation Engineer', color:'#a78bfa' },
  { type:'cmd',  text:'experience --years' },
  { type:'out',  text:'[+] 5 years @ ChargePoint (Gurugram, India)', color:'#10b981' },
  { type:'out',  text:'[+] Programmer Analyst @ Cognizant', color:'#10b981' },
  { type:'cmd',  text:'ls skills/' },
  { type:'out',  text:'Python/   Playwright/   FastAPI/   MCP/   Docker/', color:'#f9c74f' },
  { type:'out',  text:'Jenkins/  Burp-Suite/   LangChain/ Pytest/ Streamlit/', color:'#f9c74f' },
  { type:'cmd',  text:'./init_ai_stack.sh' },
  { type:'out',  text:'[✓] MCP Server — exposing private docs to LLMs…', color:'#10b981' },
  { type:'out',  text:'[✓] Gemini CLI agent initialized…', color:'#10b981' },
  { type:'out',  text:'[✓] DevUtils & ARM running on :8080', color:'#10b981' },
  { type:'out',  text:'[✓] Playwright headless suite ready', color:'#10b981' },
  { type:'cmd',  text:'git log --oneline -5' },
  { type:'out',  text:'a1b2c3d  feat: AI agent ecosystem & MCP servers', color:'#8b5cf6' },
  { type:'out',  text:'e4f5g6h  feat: 40% faster regression w/ LLM CI analysis', color:'#8b5cf6' },
  { type:'out',  text:'i7j8k9l  feat: Playwright framework (-25% manual effort)', color:'#8b5cf6' },
  { type:'out',  text:'m1n2o3p  feat: DevUtils toolbox for EV charging systems', color:'#8b5cf6' },
  { type:'out',  text:'q4r5s6t  init: Selenium+Java automation @ Cognizant', color:'#8b5cf6' },
  { type:'cmd',  text:'echo "Open to exciting opportunities!"' },
  { type:'out',  text:'Open to exciting opportunities!', color:'#00d4ff' },
];

const CHAR_DELAY   = 45;
const CHAR_JITTER  = 35;
const LINE_PAUSE   = 280;

const tbody = document.getElementById('tbody');

function sleep(ms){ return new Promise(r=>setTimeout(r,ms)); }

function makePromptEl(){
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

function makeOutEl(text, color){
  const el = document.createElement('div');
  el.className = 'line out';
  el.style.color = color || '#8b949e';
  el.textContent = text;
  tbody.appendChild(el);
  tbody.scrollTop = tbody.scrollHeight;
}

async function run(){
  await sleep(600);
  for(const seq of SEQUENCES){
    if(seq.type === 'cmd'){
      const {cmdEl, curEl} = makePromptEl();
      for(const ch of seq.text){
        cmdEl.textContent += ch;
        tbody.scrollTop = tbody.scrollHeight;
        await sleep(CHAR_DELAY + Math.random()*CHAR_JITTER);
      }
      curEl.remove();
      await sleep(LINE_PAUSE);
    } else {
      await sleep(80);
      makeOutEl(seq.text, seq.color);
      await sleep(100);
    }
  }
  // Final blinking cursor
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

run();
</script>
</body>
</html>
"""


def render_terminal() -> None:
    """Render the interactive fake terminal with typewriter animation."""
    st.markdown(
        """
        <div class="section-header" id="terminal">
            <span style="font-size:1.3rem;">🖥️</span>
            <span class="section-header-text">Interactive Terminal</span>
            <div class="section-header-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    _st.iframe(srcdoc=TERMINAL_HTML, height=460, scrolling=False)
