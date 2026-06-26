import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

const features = [
  {
    emoji: '📚',
    title: '10 Complete Chapters',
    description:
      'Every chapter of the Class 11 CS curriculum — structured, clean, and easy to navigate on any device.',
  },
  {
    emoji: '🤖',
    title: 'Robo AI Assistant',
    description:
      'Ask Robo any question and get an answer sourced directly from the book — no hallucinations, no guessing.',
  },
  {
    emoji: '✅',
    title: 'Free to Start',
    description:
      'Chapter 1 is always free. Unlock the full book and Robo AI with a single one-time payment.',
  },
];

function Feature({emoji, title, description}) {
  return (
    <div className={clsx('col col--4', styles.featureCard)}>
      <div className={styles.featureEmoji}>{emoji}</div>
      <Heading as="h3" className={styles.featureTitle}>{title}</Heading>
      <p className={styles.featureDesc}>{description}</p>
    </div>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title="Class 11 Computer Science"
      description="Your complete Class 11 CS textbook with Robo AI assistant — answers from the book, zero hallucinations.">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <Heading as="h1" className={styles.heroTitle}>
            {siteConfig.title}
          </Heading>
          <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className="button button--secondary button--lg"
              to="/docs/computer-science-11/chapter-1">
              Start Reading — Chapter 1 →
            </Link>
          </div>
        </div>
      </header>

      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              {features.map((props, idx) => (
                <Feature key={idx} {...props} />
              ))}
            </div>
          </div>
        </section>

        <section className={styles.authorTeaser}>
          <div className="container">
            <div className={styles.authorTeaserInner}>
              <div className={styles.authorTeaserText}>
                <Heading as="h2">Written by an AI Expert</Heading>
                <p>
                  This book is authored by <strong>Faizan Ali</strong>, an Agentic AI Full Stack
                  Developer and Computer Science graduate specialising in AI Agents, RAG, MCP, and
                  Workflow Automation. His goal: make advanced AI concepts genuinely easy for
                  11th class students.
                </p>
                <Link className="button button--outline button--primary" to="/about-author">
                  About the Author →
                </Link>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
