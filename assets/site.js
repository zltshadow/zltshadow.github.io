const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('open', open);
});
navigation?.addEventListener('click', event => {
  if (event.target.closest('a')) {
    menuButton.setAttribute('aria-expanded', 'false');
    navigation.classList.remove('open');
  }
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    const wasOpen = menuButton?.getAttribute('aria-expanded') === 'true';
    menuButton?.setAttribute('aria-expanded', 'false');
    navigation?.classList.remove('open');
    if (wasOpen) menuButton.focus();
  }
});
document.querySelector('.print-button')?.addEventListener('click', () => window.print());
const search = document.querySelector('#paper-search');
const year = document.querySelector('#year-filter');
const filterButtons = [...document.querySelectorAll('[data-filter]')];
let authorshipFilter = 'all';
function filterPapers() {
  const query = search.value.trim().toLowerCase();
  const selectedYear = year.value;
  let visible = 0;
  document.querySelectorAll('.publication').forEach(paper => {
    const matches = (authorshipFilter === 'all' || paper.dataset.lead === 'true')
      && (selectedYear === 'all' || selectedYear === paper.dataset.year)
      && paper.dataset.search.includes(query);
    paper.hidden = !matches;
    if (matches) visible++;
  });
  document.querySelector('#result-count').textContent = `Showing ${visible} of 17 publications`;
  document.querySelector('#no-results').hidden = visible !== 0;
}
if (search) {
  search.addEventListener('input', filterPapers);
  year.addEventListener('change', filterPapers);
  filterButtons.forEach(button => button.addEventListener('click', () => {
    authorshipFilter = button.dataset.filter;
    filterButtons.forEach(item => {
      const active = item === button;
      item.classList.toggle('active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    filterPapers();
  }));
}
