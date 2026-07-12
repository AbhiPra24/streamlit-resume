/* Lightweight canvas radar chart — static-site equivalent of the Plotly
   Scatterpolar chart in app/components/skills.py. Keep SKILLS in sync
   manually with app/data/resume.py's "skills" dict (name -> proficiency). */
(function () {
  const SKILLS = [
    { name: 'AI & LLM Infrastructure', value: 88 },
    { name: 'Frameworks & Languages', value: 92 },
    { name: 'DevOps & Infrastructure', value: 83 },
    { name: 'Databases & Security', value: 78 },
    { name: 'Protocols & APIs', value: 87 },
  ];

  function drawRadar(canvas) {
    const ctx = canvas.getContext('2d');
    const dpr = window.devicePixelRatio || 1;
    const size = Math.min(canvas.parentElement.clientWidth, 560);
    canvas.width = size * dpr;
    canvas.height = size * dpr;
    canvas.style.width = size + 'px';
    canvas.style.height = size + 'px';
    ctx.scale(dpr, dpr);

    const cx = size / 2;
    const cy = size / 2;
    const radius = size / 2 - 100;
    const n = SKILLS.length;
    const angleStep = (Math.PI * 2) / n;
    const rings = 5;

    ctx.clearRect(0, 0, size, size);

    // Grid rings + spokes.
    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.lineWidth = 1;
    for (let r = 1; r <= rings; r++) {
      const ringRadius = (radius * r) / rings;
      ctx.beginPath();
      for (let i = 0; i <= n; i++) {
        const angle = -Math.PI / 2 + i * angleStep;
        const x = cx + ringRadius * Math.cos(angle);
        const y = cy + ringRadius * Math.sin(angle);
        i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
      }
      ctx.stroke();
    }
    for (let i = 0; i < n; i++) {
      const angle = -Math.PI / 2 + i * angleStep;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + radius * Math.cos(angle), cy + radius * Math.sin(angle));
      ctx.stroke();
    }

    // Data polygon.
    ctx.beginPath();
    SKILLS.forEach((s, i) => {
      const angle = -Math.PI / 2 + i * angleStep;
      const r = (radius * s.value) / 100;
      const x = cx + r * Math.cos(angle);
      const y = cy + r * Math.sin(angle);
      i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
    });
    ctx.closePath();
    ctx.fillStyle = 'rgba(0, 212, 255, 0.15)';
    ctx.fill();
    ctx.strokeStyle = '#00d4ff';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Data point markers.
    SKILLS.forEach((s, i) => {
      const angle = -Math.PI / 2 + i * angleStep;
      const r = (radius * s.value) / 100;
      const x = cx + r * Math.cos(angle);
      const y = cy + r * Math.sin(angle);
      ctx.beginPath();
      ctx.arc(x, y, 4, 0, Math.PI * 2);
      ctx.fillStyle = '#8b5cf6';
      ctx.fill();
    });

    // Axis labels — wrap on " & " so long labels stay narrow near the canvas edge.
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#e2e8f0';
    ctx.textBaseline = 'middle';
    SKILLS.forEach((s, i) => {
      const angle = -Math.PI / 2 + i * angleStep;
      const labelR = radius + 22;
      const x = cx + labelR * Math.cos(angle);
      const y = cy + labelR * Math.sin(angle);
      ctx.textAlign = Math.abs(Math.cos(angle)) < 0.2 ? 'center' : Math.cos(angle) > 0 ? 'left' : 'right';

      const lines = s.name.split(' & ');
      if (lines.length === 2) {
        ctx.fillText(lines[0] + ' &', x, y - 7);
        ctx.fillText(lines[1], x, y + 7);
      } else {
        ctx.fillText(s.name, x, y);
      }
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('skills-radar');
    if (!canvas) return;
    drawRadar(canvas);
    window.addEventListener('resize', () => drawRadar(canvas));
  });
})();
