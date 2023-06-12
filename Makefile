liquid-staking.pdf: *.tex *.bib *.sty algorithms/*.tex
	xelatex liquid-staking.tex && \
	bibtex liquid-staking && \
	xelatex liquid-staking.tex && \
	xelatex liquid-staking.tex && \
	rm -rf *.aux *.log *.out;

minimal:
	xelatex liquid-staking.tex

clean:
	$(RM)  *.log *.aux \
	*.cfg *.glo *.idx *.toc \
	*.ilg *.ind *.out *.lof \
	*.lot *.bbl *.blg *.gls *.cut *.hd \
	*.dvi *.ps *.thm *.tgz *.zip *.rpi \
	*.d *.fls *.*.make *.fdb_latexmk *.run.xml \
	*.synctex.gz *.bcf
	$(RM) liquid-staking.pdf

