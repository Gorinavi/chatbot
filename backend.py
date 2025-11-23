import streamlit as st
import random
import string
import time
from typing import List


def _generate_random_sentence(min_words: int = 8, max_words: int = 20) -> str:
   word_pool: List[str] = [
       "context", "analysis", "system", "language", "architecture", "pattern",
       "stream", "pipeline", "robust", "scalable", "dynamic", "agent",
       "feedback", "iteration", "reasoning", "optimization", "latency",
       "interface", "integration", "baseline", "alignment", "generation",
   ]
   n = random.randint(min_words, max_words)
   words = [random.choice(word_pool) for _ in range(n)]
   sentence = " ".join(words)
   return sentence.capitalize() + "."


def _generate_random_paragraph(min_sentences: int = 2, max_sentences: int = 4) -> str:
   s = random.randint(min_sentences, max_sentences)
   return " ".join(_generate_random_sentence() for _ in range(s))


def result(text: str) -> str:
   delay = random.uniform(1.2, 2.5)
   time.sleep(delay)

   base = _generate_random_paragraph()
   if len(text.strip()) > 80:
       extra = "\n\n" + _generate_random_paragraph(3, 5)
   else:
       extra = "\n\n" + _generate_random_sentence(10, 18)

   return base + extra
