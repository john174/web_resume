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
    src: 'https://redash.io/assets/images/redash-logo.svg',
    alt: 'Redash'
  },
  {
    src: 'https://grafana.com/static/img/grafana_logo.svg',
    alt: 'Grafana'
  },
  {
    src: 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Microsoft_Office_Excel_%282013%E2%80%932019%29.svg',
    alt: 'Excel'
  },
  {
    src: 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg',
    alt: 'Docker'
  }
];

const carousel = document.getElementById('carousel');
const angle = 360 / images.length;

images.forEach((data, i) => {
  const img = document.createElement('img');
  img.src = data.src;
  img.alt = data.alt;
  img.style.transform = `rotateY(${i * angle}deg) translateZ(300px)`;
  carousel.appendChild(img);
});
