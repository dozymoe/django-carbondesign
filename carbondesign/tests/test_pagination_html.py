# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class PaginationHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Pagination pager=page_first id="uid" %}
"""
        expected = """
<div class="bx--pagination" data-pagination data-page-name="page"
    data-pagesize-name="pagesize">
  <div class="bx--pagination__left">
    <label id="select-uid-pagination-count-label" class="bx--pagination__text"
        for="select-uid-pagination-count">
      Items per page:
    </label>
    <div class="bx--select bx--select--inline bx--select__item-count">
      <select class="bx--select-input" id="select-uid-pagination-count"
          aria-label="select number of items per page" tabindex="0"
          data-items-per-page>
<option class="bx--select-option" selected>10</option>
<option class="bx--select-option">20</option>
<option class="bx--select-option">30</option>
<option class="bx--select-option">40</option>
<option class="bx--select-option">50</option>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <span class="bx--pagination__text">
<span data-displayed-item-range>1 – 10</span>
 of <span data-total-items>100</span> items
    </span>
  </div>
  <div class="bx--pagination__right">
    <div class="bx--select bx--select--inline bx--select__page-number">
      <select class="bx--select-input" id="select-uid-pagination-page"
          aria-label="select page number to view" tabindex="0"
          data-page-number-input>
<option class="bx--select-option" selected>1</option>
<option class="bx--select-option">2</option>
<option class="bx--select-option">3</option>
<option class="bx--select-option">4</option>
<option class="bx--select-option">5</option>
<option class="bx--select-option">6</option>
<option class="bx--select-option">7</option>
<option class="bx--select-option">8</option>
<option class="bx--select-option">9</option>
<option class="bx--select-option">10</option>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <label id="select-uid-pagination-page-label" class="bx--pagination__text"
        for="select-uid-pagination-page">
      of 10 pages
    </label>
    <button class="bx--pagination__button bx--pagination__button--backward"
        tabindex="0" data-page-backward aria-label="previous page">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M20 24L10 16 20 8z"></path>
      </svg>
    </button>
    <button class="bx--pagination__button bx--pagination__button--forward"
        tabindex="0" data-page-forward aria-label="next page">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M12 8L22 16 12 24z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_disabled(self):
        template = """
{% load carbondesign %}
{% Pagination pager=page_first id="uid" disabled=True %}
"""
        expected = """
<div class="bx--pagination" data-pagination data-page-name="page"
    data-pagesize-name="pagesize">
  <div class="bx--pagination__left">
    <label id="select-uid-pagination-count-label" class="bx--pagination__text"
        for="select-uid-pagination-count">
      Items per page:
    </label>
    <div class="bx--select bx--select--inline bx--select__item-count">
      <select class="bx--select-input" id="select-uid-pagination-count"
          aria-label="select number of items per page" tabindex="0"
          data-items-per-page>
<option class="bx--select-option" selected>10</option>
<option class="bx--select-option">20</option>
<option class="bx--select-option">30</option>
<option class="bx--select-option">40</option>
<option class="bx--select-option">50</option>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <span class="bx--pagination__text">
<span data-displayed-item-range>1 – 10</span>
 of <span data-total-items>100</span> items
    </span>
  </div>
  <div class="bx--pagination__right">
    <div class="bx--select bx--select--inline bx--select__page-number">
      <select class="bx--select-input" id="select-uid-pagination-page"
          aria-label="select page number to view" tabindex="0"
          data-page-number-input>
<option class="bx--select-option" selected>1</option>
<option class="bx--select-option">2</option>
<option class="bx--select-option">3</option>
<option class="bx--select-option">4</option>
<option class="bx--select-option">5</option>
<option class="bx--select-option">6</option>
<option class="bx--select-option">7</option>
<option class="bx--select-option">8</option>
<option class="bx--select-option">9</option>
<option class="bx--select-option">10</option>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <label id="select-uid-pagination-page-label" class="bx--pagination__text"
        for="select-uid-pagination-page">
      of 10 pages
    </label>
    <button class="bx--pagination__button bx--pagination__button--backward bx--pagination__button--no-index"
        tabindex="0" data-page-backward aria-label="previous page">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M20 24L10 16 20 8z"></path>
      </svg>
    </button>
    <button class="bx--pagination__button bx--pagination__button--forward bx--pagination__button--no-index"
        tabindex="0" data-page-forward aria-label="next page">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M12 8L22 16 12 24z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
