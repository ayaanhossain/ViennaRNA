LATEX_CMD=/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error

all: refman.pdf

pdf: refman.pdf

refman.pdf: clean refman.tex
	$(LATEX_CMD) refman
	/usr/bin/makeindex refman.idx
	bibtex refman
	$(LATEX_CMD) refman
	$(LATEX_CMD) refman
	latex_count=8 ; \
	while egrep -s 'Rerun (LaTeX|to get cross-references right)' refman.log && [ $$latex_count -gt 0 ] ;\
	    do \
	      echo "Rerunning latex...." ;\
	      $(LATEX_CMD) refman ;\
	      latex_count=`expr $$latex_count - 1` ;\
	    done
	/usr/bin/makeindex refman.idx
	$(LATEX_CMD) refman


clean:
	rm -f *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *.brf *.blg *.bbl refman.pdf
