.PHONY: srpm

srpm:
	dnf install -y rpmdevtools rpmlint
	mkdir -p $(outdir)
	spectool -g -R httpie-desktop.spec
	rpmbuild -bs httpie-desktop.spec \
		--define "_sourcedir $(PWD)" \
		--define "_specdir $(PWD)" \
		--define "_builddir $(PWD)" \
		--define "_srcrpmdir $(outdir)" \
		--define "_rpmdir $(PWD)"
