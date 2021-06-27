.PHONY: help
help:
	@true

.PHONY: test
test:
	./resource/check
	./resource/in
	./resource/out
