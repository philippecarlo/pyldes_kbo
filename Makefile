all: one two
.PHONY: all

one:
	cd cegekaKBO/cegeka_kbo_pagination && python3.10 -m unittest kbo_pagination_default.py
two:
	cd cegekaKBO/cegeka_kbo_substring && python3.10 -m unittest kbo_substring_default.py

clean:
	rm -f one two three