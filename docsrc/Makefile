# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= ../run pybin sphinx-build
SPHINXAPIDOC  ?= ../run sphinx-apidoc
SOURCEDIR     = docsrc
BUILDDIR      = ../docs_build
GHPAGESDIR    = ../docs

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "../$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

api:
	@SPHINX_APIDOC_OPTIONS=members $(SPHINXAPIDOC)\
            --output-dir=$(SOURCEDIR)/gen -eEfMT carbondesign\
            carbondesign/templatetags/ carbondesign/tests/\
            carbondesign/tests.py carbondesign/apps.py\
            carbondesign/tags/base.py

github:
	@make html
	@cp -a "$(BUILDDIR)/html/." "$(GHPAGESDIR)"


.PHONY: help Makefile api github

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile api
	@$(SPHINXBUILD) -M $@ "../$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
