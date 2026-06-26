// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Computer Science Class 11',
  tagline: 'Your complete CS textbook — powered by Robo AI',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://faizanalijutt0786-maker.github.io',
  baseUrl: '/computer-science-11-year/',

  organizationName: 'faizanalijutt0786-maker',
  projectName: 'computer-science-11-year',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/docusaurus-social-card.jpg',
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'CS Class 11',
        logo: {
          alt: 'CS Class 11',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Chapters',
          },
          {
            to: '/about-author',
            label: 'About Author',
            position: 'left',
          },
          {
            href: 'https://github.com/faizanalijutt0786-maker/computer-science-11-year',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Textbook',
            items: [
              {
                label: 'Chapter 1 — Intro to Software Development',
                to: '/docs/computer-science-11/chapter-1',
              },
            ],
          },
          {
            title: 'About',
            items: [
              {
                label: 'About the Author',
                to: '/about-author',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/faizanalijutt0786-maker/computer-science-11-year',
              },
            ],
          },
          {
            title: 'Connect',
            items: [
              {
                label: 'LinkedIn',
                href: 'https://linkedin.com/in/faizanalijutt',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Faizan Ali. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
