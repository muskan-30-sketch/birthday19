import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday",
    page_icon="\U0001F56F\ufe0f",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default chrome (menu, footer, header, and default padding)
# so the page reads as a standalone site rather than an app embedded in a frame.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,500;0,9..144,600;1,9..144,500&family=Karla:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#15111A;
    --bg-card:#221A25;
    --bg-card-2:#2B2130;
    --text:#EDE3E0;
    --text-soft:#9C8A94;
    --gold:#C9A050;
    --rose:#8E2E3E;
    --line:#3A2E38;
    --shadow: 0 20px 50px -20px rgba(0,0,0,0.6);
  }

  *{ margin:0; padding:0; box-sizing:border-box; }

  html{ scroll-behavior:smooth; }

  body{
    background:var(--bg);
    color:var(--text);
    font-family:'Karla', sans-serif;
    font-weight:400;
    overflow-x:hidden;
    position:relative;
  }

  body::before{
    content:'';
    position:fixed;
    inset:0;
    background:
      radial-gradient(circle at 15% 20%, rgba(201,160,80,0.045), transparent 40%),
      radial-gradient(circle at 85% 70%, rgba(142,46,62,0.10), transparent 45%);
    pointer-events:none;
    z-index:0;
  }

  h1,h2,h3{ font-family:'Fraunces', serif; font-weight:500; letter-spacing:-0.01em; }

  .eyebrow{
    font-family:'JetBrains Mono', monospace;
    font-size:0.72rem;
    letter-spacing:0.18em;
    text-transform:uppercase;
    color:var(--gold);
    display:inline-block;
    margin-bottom:14px;
  }

  section{ position:relative; z-index:1; padding:120px 24px; max-width:900px; margin:0 auto; }

  /* ---------- FIREFLIES ---------- */
  .fireflies{ position:fixed; inset:0; pointer-events:none; z-index:0; overflow:hidden; }
  .firefly{
    position:absolute;
    width:3px; height:3px;
    background:var(--gold);
    border-radius:50%;
    box-shadow:0 0 8px 2px rgba(201,160,80,0.55);
    animation: drift 14s ease-in-out infinite;
    opacity:0;
  }
  @keyframes drift{
    0%{ opacity:0; transform:translate(0,0); }
    10%{ opacity:0.9; }
    50%{ transform:translate(30px,-60px); }
    90%{ opacity:0.7; }
    100%{ opacity:0; transform:translate(-20px,-120px); }
  }

  /* ---------- HERO ---------- */
  .hero{
    min-height:100svh;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:24px;
    max-width:100%;
  }

  .candle-wrap{
    position:relative;
    height:150px;
    display:flex;
    align-items:flex-end;
    justify-content:center;
    margin-bottom:36px;
    cursor:pointer;
  }

  .candle{
    width:22px;
    height:90px;
    background:linear-gradient(180deg, #F0E4D0, #DCCBAF);
    border-radius:4px;
    position:relative;
    box-shadow: inset -4px 0 8px rgba(0,0,0,0.15);
  }
  .candle::before, .candle::after{
    content:'';
    position:absolute;
    left:0; right:0;
    height:4px;
    background:var(--rose);
    opacity:0.5;
  }
  .candle::before{ top:22px; }
  .candle::after{ top:52px; }

  .wick{
    position:absolute;
    top:-10px; left:50%;
    transform:translateX(-50%);
    width:2px; height:10px;
    background:#3a2f1f;
  }

  .flame{
    position:absolute;
    top:-42px; left:50%;
    transform:translateX(-50%);
    width:16px; height:32px;
    border-radius:50% 50% 50% 50% / 60% 60% 40% 40%;
    background:radial-gradient(circle at 50% 70%, #fff6da 0%, var(--gold) 45%, #d9660f 100%);
    box-shadow:0 0 24px 6px rgba(232,166,87,0.55), 0 0 60px 20px rgba(232,166,87,0.15);
    animation: flicker 2.4s ease-in-out infinite;
    transform-origin:50% 100%;
    transition: opacity 0.4s ease, transform 0.4s ease;
  }
  .flame.out{ opacity:0; transform:translateX(-50%) scale(0.2); }

  @keyframes flicker{
    0%,100%{ transform:translateX(-50%) rotate(-2deg) scaleY(1); }
    25%{ transform:translateX(-50%) rotate(2deg) scaleY(1.05); }
    50%{ transform:translateX(-52%) rotate(-1deg) scaleY(0.96); }
    75%{ transform:translateX(-48%) rotate(3deg) scaleY(1.02); }
  }

  .hint{
    font-family:'JetBrains Mono', monospace;
    font-size:0.68rem;
    color:var(--text-soft);
    letter-spacing:0.1em;
    text-transform:uppercase;
    margin-top:10px;
    opacity:0.7;
  }

  .hero h1{
    font-size:clamp(2.6rem, 7vw, 4.6rem);
    line-height:1.05;
    max-width:800px;
  }
  .hero h1 em{
    font-style:italic;
    color:var(--gold);
    font-weight:500;
  }

  .hero p{
    margin-top:22px;
    font-size:1.05rem;
    color:var(--text-soft);
    max-width:480px;
    line-height:1.7;
  }

  .mystery-note{
    margin-top:26px !important;
    display:inline-block;
    font-family:'JetBrains Mono', monospace;
    font-size:0.78rem !important;
    letter-spacing:0.03em;
    color:var(--gold) !important;
    background:rgba(201,160,80,0.08);
    border:1px dashed var(--gold);
    border-radius:8px;
    padding:12px 18px;
    line-height:1.6 !important;
    max-width:420px !important;
  }

  .scroll-cue{
    position:absolute;
    bottom:36px;
    left:50%;
    transform:translateX(-50%);
    width:1px;
    height:44px;
    background:linear-gradient(180deg, var(--gold), transparent);
  }
  .scroll-cue::after{
    content:'';
    position:absolute;
    left:50%; top:0;
    transform:translateX(-50%);
    width:5px; height:5px;
    border-radius:50%;
    background:var(--gold);
    animation:cue 1.8s ease-in-out infinite;
  }
  @keyframes cue{
    0%{ top:0; opacity:1; }
    100%{ top:40px; opacity:0; }
  }

  /* ---------- REVEAL ---------- */
  .reveal{
    opacity:0;
    transform:translateY(32px);
    transition: opacity 0.9s cubic-bezier(.2,.7,.2,1), transform 0.9s cubic-bezier(.2,.7,.2,1);
  }
  .reveal.in{ opacity:1; transform:translateY(0); }

  /* ---------- TIMELINE ---------- */
  .timeline-header{ text-align:center; margin-bottom:80px; }
  .timeline-header h2{ font-size:clamp(1.8rem, 4vw, 2.6rem); }
  .timeline-header p{ color:var(--text-soft); margin-top:12px; max-width:520px; margin-inline:auto; }

  .timeline{
    position:relative;
    padding-left:0;
  }

  .timeline-line{
    position:absolute;
    left:23px;
    top:0;
    bottom:0;
    width:1px;
    background:var(--line);
    overflow:hidden;
  }
  .timeline-line-fill{
    position:absolute;
    left:0; top:0;
    width:100%;
    height:0%;
    background:linear-gradient(180deg, var(--gold), var(--rose));
    transition:height 0.2s linear;
    box-shadow:0 0 12px rgba(232,166,87,0.5);
  }

  .entry{
    position:relative;
    padding-left:64px;
    margin-bottom:64px;
  }
  .entry:last-child{ margin-bottom:0; }

  .entry-dot{
    position:absolute;
    left:14px;
    top:6px;
    width:20px; height:20px;
    border-radius:50%;
    background:var(--bg);
    border:1px solid var(--line);
    display:flex;
    align-items:center;
    justify-content:center;
    transition: border-color 0.4s ease, box-shadow 0.4s ease;
  }
  .entry-dot::after{
    content:'';
    width:7px; height:7px;
    border-radius:50%;
    background:var(--line);
    transition: background 0.4s ease;
  }
  .entry.in .entry-dot{
    border-color:var(--gold);
    box-shadow:0 0 14px rgba(232,166,87,0.45);
  }
  .entry.in .entry-dot::after{ background:var(--gold); }

  .entry-date{
    font-family:'JetBrains Mono', monospace;
    font-size:0.7rem;
    letter-spacing:0.12em;
    text-transform:uppercase;
    color:var(--gold);
    display:block;
    margin-bottom:8px;
  }

  .entry h3{
    font-size:1.5rem;
    margin-bottom:10px;
    font-weight:500;
  }

  .entry p{
    color:var(--text-soft);
    line-height:1.75;
    font-size:1rem;
    max-width:520px;
  }

  /* ---------- QUALITIES ---------- */
  .qualities{ background:transparent; }
  .qualities-header{ text-align:center; margin-bottom:56px; }
  .qualities-header h2{ font-size:clamp(1.8rem, 4vw, 2.6rem); }
  .qualities-header p{ color:var(--text-soft); margin-top:12px; }

  .quality-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));
    gap:18px;
  }

  .quality-card{
    background:var(--bg-card);
    border:1px solid var(--line);
    border-radius:14px;
    padding:28px 24px;
    transition: transform 0.35s ease, border-color 0.35s ease, background 0.35s ease;
  }
  .quality-card:hover{
    transform:translateY(-6px);
    border-color:var(--gold);
    background:var(--bg-card-2);
  }

  .quality-card .mark{
    font-family:'Fraunces', serif;
    font-style:italic;
    font-size:1.6rem;
    color:var(--rose);
    display:block;
    margin-bottom:12px;
  }

  .quality-card h3{
    font-size:1.1rem;
    margin-bottom:8px;
    font-weight:500;
  }

  .quality-card p{
    color:var(--text-soft);
    font-size:0.92rem;
    line-height:1.6;
  }

  .quality-card.editable{
    border-style:dashed;
    opacity:0.7;
  }

  /* ---------- NOTES ---------- */
  .notes-header{ text-align:center; margin-bottom:56px; }
  .notes-header h2{ font-size:clamp(1.8rem, 4vw, 2.6rem); }
  .notes-header p{ color:var(--text-soft); margin-top:12px; }

  .notes-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));
    gap:20px;
  }

  .note{
    background:var(--bg-card);
    border:1px solid var(--line);
    border-radius:2px;
    padding:22px;
    font-family:'Fraunces', serif;
    font-style:italic;
    font-size:1.05rem;
    line-height:1.6;
    color:var(--text);
    position:relative;
    transform:rotate(var(--r, 0deg));
    transition:transform 0.3s ease, box-shadow 0.3s ease;
  }
  .note:nth-child(odd){ --r:-1.2deg; }
  .note:nth-child(even){ --r:1.4deg; }
  .note:hover{ transform:rotate(0deg) translateY(-4px); box-shadow:var(--shadow); }
  .note::before{
    content:'';
    position:absolute;
    top:-6px; left:50%;
    transform:translateX(-50%) rotate(-8deg);
    width:34px; height:12px;
    background:rgba(232,166,87,0.35);
  }

  /* ---------- MESSAGE / LETTER ---------- */
  .letter-wrap{
    text-align:center;
  }
  .letter-wrap .eyebrow{ display:block; }
  .letter-wrap > p.lead{
    color:var(--text-soft);
    max-width:480px;
    margin:14px auto 40px;
    line-height:1.7;
  }

  .envelope{
    max-width:480px;
    margin:0 auto;
    background:var(--bg-card);
    border:1px solid var(--line);
    border-radius:10px;
    padding:40px 34px;
    text-align:left;
    position:relative;
  }
  .envelope::before{
    content:'';
    position:absolute;
    top:0; left:0; right:0;
    height:3px;
    background:linear-gradient(90deg, var(--gold), var(--rose));
    border-radius:10px 10px 0 0;
  }

  .envelope p.placeholder{
    font-family:'Fraunces', serif;
    font-style:italic;
    color:var(--text-soft);
    font-size:1.05rem;
    line-height:1.8;
    opacity:0.75;
  }

  .envelope .sign{
    margin-top:26px;
    font-family:'JetBrains Mono', monospace;
    font-size:0.75rem;
    letter-spacing:0.1em;
    text-transform:uppercase;
    color:var(--gold);
  }

  /* ---------- FOOTER ---------- */
  footer{
    text-align:center;
    padding:60px 24px 90px;
    color:var(--text-soft);
    font-family:'JetBrains Mono', monospace;
    font-size:0.7rem;
    letter-spacing:0.12em;
    text-transform:uppercase;
    opacity:0.6;
  }

  @media (max-width:600px){
    section{ padding:80px 20px; }
    .entry{ padding-left:52px; }
    .timeline-line{ left:19px; }
    .entry-dot{ left:10px; }
  }

  @media (prefers-reduced-motion: reduce){
    *{ animation-duration:0.01ms !important; animation-iteration-count:1 !important; transition-duration:0.01ms !important; scroll-behavior:auto !important; }
  }
</style>
</head>
<body>

<div class="fireflies" id="fireflies"></div>

<!-- ===================== HERO ===================== -->
<section class="hero">
  <div class="candle-wrap" id="candleWrap">
    <div class="flame" id="flame"></div>
    <div class="wick"></div>
    <div class="candle"></div>
  </div>
  <span class="hint" id="candleHint">tap the flame</span>

  <h1>happy birthday<br><em>to the sweetest soul.</em></h1>
  <p>You don't know it, but you're one of the nicest people I've ever met in my life. This is a small, unofficial timeline of us — from a classroom you weren't even in, to a place you never expected me to show up.</p>
  <p class="mystery-note">also — sorry for making you confused, in the matter of&hellip; well, that stays a mystery.</p>

  <div class="scroll-cue"></div>
</section>

<!-- ===================== TIMELINE ===================== -->
<section id="timeline">
  <div class="timeline-header reveal">
    <span class="eyebrow">an unofficial timeline</span>
    <h2>How it happened</h2>
    <p>Not a straight line. Not even a planned one. Just five moments that mattered more than I said out loud at the time.</p>
  </div>

  <div class="timeline">
    <div class="timeline-line"><div class="timeline-line-fill" id="lineFill"></div></div>

    <div class="entry reveal">
      <div class="entry-dot"></div>
      <span class="entry-date">where it started</span>
      <h3>Eleventh class</h3>
      <p>Different sections. No real reason our paths should have crossed. But somehow there was already something there — small, unannounced, easy to miss if you weren't paying attention.</p>
    </div>

    <div class="entry reveal">
      <div class="entry-dot"></div>
      <span class="entry-date">the decision</span>
      <h3>Becoming friends</h3>
      <p>One of the better calls I've made. Still don't regret it. We started talking — nothing dramatic, just the beginning of something I didn't know yet I'd want to keep.</p>
    </div>

    <div class="entry reveal">
      <div class="entry-dot"></div>
      <span class="entry-date">small talk, at first</span>
      <h3>The first real conversation</h3>
      <p>It didn't start big. Just "Hey," a few words here and there. Then somewhere after school hours, the small talk stopped being small — we just kept talking.</p>
    </div>

    <div class="entry reveal">
      <div class="entry-dot"></div>
      <span class="entry-date">the turning point</span>
      <h3>When we actually got close</h3>
      <p>We started writing to each other. Started liking each other. Never said it out loud. Just a quiet kind of confusion neither of us tried very hard to solve.</p>
    </div>

    <div class="entry reveal">
      <div class="entry-dot"></div>
      <span class="entry-date">the one I won't forget</span>
      <h3>I changed schools to find you</h3>
      <p>I took the step. Changed schools — and you came to my college to meet me. Out of everything, this is the memory that stayed the clearest. It still does.</p>
    </div>
  </div>
</section>

<!-- ===================== QUALITIES ===================== -->
<section class="qualities">
  <div class="qualities-header reveal">
    <span class="eyebrow">what makes you, you</span>
    <h2>A few things I never say enough</h2>
    <p>Edit or add to these — this is just a start.</p>
  </div>

  <div class="quality-grid">
    <div class="quality-card reveal">
      <span class="mark">&mdash;</span>
      <h3>A good soul</h3>
      <p>The kind of person who makes things easier just by being around. Not performative kindness — the real, quiet kind.</p>
    </div>
    <div class="quality-card reveal">
      <span class="mark">&mdash;</span>
      <h3>Confident</h3>
      <p>You walk into things like you already belong there. It's one of the first things I noticed, and it hasn't stopped being true.</p>
    </div>
    <div class="quality-card reveal">
      <span class="mark">&mdash;</span>
      <h3>And, honestly</h3>
      <p>I really like you. Simple as that. No better way to say it.</p>
    </div>
    <div class="quality-card editable reveal">
      <span class="mark">+</span>
      <h3>Honest, and sharp with it</h3>
      <p>You say what's true, not what's easy. And that mind of yours — always a step ahead, always thinking it through before you speak.</p>
    </div>
  </div>
</section>

<!-- ===================== NOTES ===================== -->
<section id="notes">
  <div class="notes-header reveal">
    <span class="eyebrow">little notes</span>
    <h2>Things worth writing down</h2>
    <p>Swap these for your own — think of them as sticky notes, not paragraphs.</p>
  </div>

  <div class="notes-grid">
    <div class="note reveal">"Good morning" used to be the whole conversation. Now it's just how we start every one.</div>
    <div class="note reveal">You showed up at my college. I still think about that.</div>
    <div class="note reveal">We never said it out loud back then. I think we both knew anyway.</div>
    <div class="note reveal">Still one of the best decisions — becoming friends with you.</div>
  </div>
</section>

<!-- ===================== MESSAGE ===================== -->
<section id="message">
  <div class="letter-wrap reveal">
    <span class="eyebrow">the last part</span>
    <h2>One more thing</h2>

    <div class="envelope">
      <p class="placeholder">Happy birthday. I don't say this enough, so let me say it properly here — you're one of the most confident people I know, and it's never loud about it, it's just how you carry yourself. You're honest, even when it would be easier not to be. And that mind of yours, always thinking things through, always a step ahead — it's one of my favourite things about you.<br><br>Above all of that, though — you're just so cute, and being around you feels like a good condition to be in. That's really it. That's the whole thing.<br><br>Here's to another year of you being exactly you.</p>
      <div class="sign">— from me, to you</div>
    </div>
  </div>
</section>

<footer>made with a little bit of everything &middot; happy birthday</footer>

<script>
  // Reduced motion check
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Fireflies
  if(!reduceMotion){
    const container = document.getElementById('fireflies');
    const count = window.innerWidth < 600 ? 12 : 24;
    for(let i=0;i<count;i++){
      const f = document.createElement('div');
      f.className = 'firefly';
      f.style.left = Math.random()*100 + 'vw';
      f.style.top = (40 + Math.random()*55) + 'vh';
      f.style.animationDelay = (Math.random()*14) + 's';
      f.style.animationDuration = (10 + Math.random()*10) + 's';
      container.appendChild(f);
    }
  }

  // Candle interaction
  const flame = document.getElementById('flame');
  const candleWrap = document.getElementById('candleWrap');
  const candleHint = document.getElementById('candleHint');
  let lit = true;
  candleWrap.addEventListener('click', () => {
    lit = !lit;
    flame.classList.toggle('out', !lit);
    candleHint.textContent = lit ? 'tap the flame' : 'make a wish';
  });

  // Scroll reveal
  const revealEls = document.querySelectorAll('.reveal, .entry');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        entry.target.classList.add('in');
      }
    });
  }, { threshold: 0.2 });
  revealEls.forEach(el => io.observe(el));

  // Timeline fill line
  const timelineSection = document.getElementById('timeline');
  const lineFill = document.getElementById('lineFill');
  function updateLine(){
    const rect = timelineSection.getBoundingClientRect();
    const vh = window.innerHeight;
    const total = rect.height;
    const scrolled = Math.min(Math.max(vh*0.5 - rect.top, 0), total);
    const pct = (scrolled/total) * 100;
    lineFill.style.height = pct + '%';
  }
  window.addEventListener('scroll', updateLine);
  window.addEventListener('resize', updateLine);
  updateLine();
</script>

</body>
</html>
"""

# height is generous since the page scrolls internally; scrolling is enabled
# so all sections (hero, timeline, qualities, notes, message) are reachable.
components.html(HTML_CONTENT, height=2000, scrolling=True)
