/* Scroll-triggered reveal via IntersectionObserver. Unlike the Streamlit app,
   this is a plain static page with no innerHTML/iframe sandboxing quirks, so a
   normal <script src="js/reveal.js"> works directly against `document`. */
(function () {
  document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('reveal-ready');

    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          entry.target.classList.toggle('is-visible', entry.isIntersecting);
        });
      },
      { threshold: 0.15 }
    );

    document.querySelectorAll('.scroll-reveal').forEach((el) => io.observe(el));
  });
})();
