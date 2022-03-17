# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class PaginationNavTest(SimpleTestCase):
    maxDiff = None

    def test_empty(self):
        template = """
{% load carbondesign %}
{% PaginationNav pager=None %}
"""
        expected = """
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_first_page(self):
        template = """
{% load carbondesign %}
{% PaginationNav pager=page_first id="uid" %}
"""
        expected = """
<nav class="bx--pagination-nav" aria-label="pagination"
    data-pagination-nav>
  <ul class="bx--pagination-nav__list">
<li class="bx--pagination-nav__list-item">
  <button
      class="bx--pagination-nav__page bx--pagination-nav__page--direction bx--pagination-nav__page--disabled"
      data-page-previous aria-disabled="true">
    <span class="bx--pagination-nav__accessibility-label">Previous page</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--pagination-nav__icon" width="5" height="8" viewBox="0 0 5 8"
        aria-hidden="true">
      <path d="M5 8L0 4 5 0z"></path>
    </svg>
  </button>
</li>
<li class="bx--pagination-nav__list-item">
  <button class="bx--pagination-nav__page bx--pagination-nav__page--active bx--pagination-nav__page--disabled" data-page="1"
      data-page-button data-page-active="true" aria-current="page" aria-disabled="true">
    <span class="bx--pagination-nav__accessibility-label">page</span>
    1
  </button>
</li>
<li class="bx--pagination-nav__list-item">
  <button class="bx--pagination-nav__page" data-page="2"
      data-page-button id="uid">
    <span class="bx--pagination-nav__accessibility-label">page</span>
    2
  </button>
</li>
<li class="bx--pagination-nav__list-item">
  <button class="bx--pagination-nav__page" data-page="3"
      data-page-button id="uid">
    <span class="bx--pagination-nav__accessibility-label">page</span>
    3
  </button>
</li>
<li class="bx--pagination-nav__list-item">
  <button class="bx--pagination-nav__page" data-page="4"
      data-page-button id="uid">
    <span class="bx--pagination-nav__accessibility-label">page</span>
    4
  </button>
</li>
<li class="bx--pagination-nav__list-item">
  <button class="bx--pagination-nav__page" data-page="5"
      data-page-button id="uid">
    <span class="bx--pagination-nav__accessibility-label">page</span>
    5
  </button>
</li>
<li class="bx--pagination-nav__list-item">
  <button class="bx--pagination-nav__page" data-page="6"
      data-page-button id="uid">
    <span class="bx--pagination-nav__accessibility-label">page</span>
    6
  </button>
</li>
<li class="bx--pagination-nav__list-item">
  <button
      class="bx--pagination-nav__page bx--pagination-nav__page--direction bx--pagination-nav__page--disabled"
      data-page-previous aria-disabled="true">
    <span class="bx--pagination-nav__accessibility-label">Previous page</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--pagination-nav__icon" width="5" height="8" viewBox="0 0 5 8"
        aria-hidden="true">
      <path d="M5 8L0 4 5 0z"></path>
    </svg>
  </button>
</li>
  </ul>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
