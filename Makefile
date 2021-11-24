# LaTeX Makefile v1.0 -- LaTeX + PDF figures + PNG figures

MAIN=Slides.tex
LATEX=rubber --pdf
SHELL=/bin/bash
INCLUDES=includes.tex
HANDOUTDIR=Handouts_pdf
FILES_AUX=$(wildcard *.aux *.blg *.out *.bbl *.log *.vrb *.dvi *.nav *.snm *.toc)
FILES_PDF=$(wildcard *.pdf)

.PHONY: all handout clean remove_includes create_include build

remove_includes:
	rm -f ${INCLUDES}

all: remove_includes
	@echo Making $@ $(LATEX)
	@touch includes.tex
	${LATEX} --jobname=Slides_$@ ${MAIN}

separate: remove_includes	intro	remove_includes programming	remove_includes numericalerrors remove_includes linear remove_includes intint remove_includes ode remove_includes pde remove_includes optimization

intro programming1 programming2 numericalerrors interpolation integration linear1 linear2 linear3 optimization ode1 ode2 pde: remove_includes create_include
	@echo Building slides $@
	@echo "\\includeonlylecture{"$@"}"> ${INCLUDES} 
	@echo ${JOBNAME} ${MAIN}
	${LATEX} --jobname=Slides_$@ ${MAIN}

programming : remove_includes 
	@echo Building slides $@
	@echo "\\includeonlylecture{"programming1,programming2"}"> ${INCLUDES} 
	@echo ${JOBNAME} ${MAIN}
	${LATEX} --jobname=Slides_$@ ${MAIN}

linear : remove_includes 
	@echo Building slides $@
	@echo "\\includeonlylecture{"linear1,linear2,linear3"}"> ${INCLUDES} 
	@echo ${JOBNAME} ${MAIN}
	${LATEX} --jobname=Slides_$@ ${MAIN}

intint : remove_includes 
	@echo Building slides $@
	@echo "\\includeonlylecture{"interpolation,integration"}"> ${INCLUDES} 
	@echo ${JOBNAME} ${MAIN}
	${LATEX} --jobname=Slides_$@ ${MAIN}

ode : remove_includes 
	@echo Building slides $@
	@echo "\\includeonlylecture{"ode1,ode2"}"> ${INCLUDES} 
	@echo ${JOBNAME} ${MAIN}
	${LATEX} --jobname=Slides_$@ ${MAIN}

clean:
	rm -f $(FILES_AUX)

cleaner: clean
	rm -f $(FILES_PDF)

store_handouts:
	@if [ ! -d $(HANDOUTDIR) ]; then mkdir $(HANDOUTDIR);	fi
	@rename 's/Slides/Handouts/' Slides_*.pdf
	@mv Handouts*.pdf $(HANDOUTDIR)/
	#find . -maxdepth 1 -name 'Slides*.pdf' -exec sh -c 'echo $0' {} \;
	#-exec bash -c ' mv $0 ${0/Slides/Handouts}' {} \;