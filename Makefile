include $(wildcard mk/*.mk)

.PHONY: runtime-version
runtime-version:
	@printf 'runtime-version-ok\n'
