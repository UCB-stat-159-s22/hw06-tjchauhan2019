.PHONY: html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	bash -ic 'cd _build/html; python -m http.server'

.PHONY: html
html:
	jupyter-book build .

.PHONY: env
env:
	mamba env create -f environment.yml -p ~/envs/ligo
	bash -ic 'conda activate ligo;python -m ipykernel install --user --name ligo --display-name "ligo"'

.PHONY : clean
clean :
	rm -rf audio/*.wav
	rm -rf figurs/*.png
	rm -rf _build/