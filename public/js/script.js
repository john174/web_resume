const images = [
  {
    src: 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg',
    alt: 'SQL'
  },
  {
    src: 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg',
    alt: 'Python'
  },
  {
    src: 'https://pandas.pydata.org/static/img/pandas_mark.svg',
    alt: 'Pandas'
  },
  {
    src: 'https://matplotlib.org/_static/logo2.svg',
    alt: 'Matplotlib'
  },
  {
    src: 'https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png',
    alt: 'Streamlit'
  },
  {
    src: 'https://docs.getdbt.com/img/dbt-logo.svg',
    alt: 'dbt'
  },
  {
    src: 'https://redash.io/assets/images/elements/redash-logo.svg',
    alt: 'Redash'
  },
  {
    src: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Grafana_logo.svg/1024px-Grafana_logo.svg.png?20230113183101',
    alt: 'Grafana'
  },
  {
    src: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg/640px-Microsoft_Office_Excel_%282019%E2%80%93present%29.svg.png',
    alt: 'Excel'
  },
  {
    src: 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg',
    alt: 'Docker'
  }
];

const carousel = document.getElementById('carousel');

images.forEach(({ src, alt }) => {
  const img = document.createElement('img');
  img.src = src;
  img.alt = alt;
  carousel.appendChild(img);
});

// Duplicate images for seamless scroll
carousel.innerHTML += carousel.innerHTML;

