include gmsl

GENERATED_FILES = \
	raw/zbp02detail.txt \
	raw/zbp03detail.txt \
	raw/zbp04detail.txt \
	raw/zbp05detail.txt \
	raw/zbp06detail.txt \
	raw/zbp07detail.txt \
	raw/zbp08detail.txt \
	raw/zbp09detail.txt \
	raw/zbp10detail.txt \
	raw/zbp11detail.txt \
	raw/zbp12detail.txt \
	raw/zbp13detail.txt \
	raw/zbp94detail.txt \
	raw/zbp95detail.txt \
	raw/zbp96detail.txt \
	raw/zbp97detail.txt \
	raw/zbp98detail.txt \
	raw/zbp99detail.txt \
	raw/zbp00detail.txt \
	raw/zbp01detail.txt 

SHELL = /bin/bash

all: $(GENERATED_FILES)
	mkdir -p converted

.PHONY: all clean

clean:
	rm -rf -- $(GENERATED_FILES) build
#generates zips. TARGET OF THE RULE (FIRST PART) is the $@
zips/%.zip: 
	mkdir -p $(dir $@) #isn't this the same as zips?
	#I guess this warrants a bugfix in 2094
	if [[ `expr $(call substr,$(notdir $@),4,5) + 0` -gt "1" && `expr $(call substr,$(notdir $@),4,5) + 0` -lt "94" ]]; then \
	    curl -o $@ "ftp://ftp.census.gov/econ20$(call substr,$(notdir $@),4,5)/CBP_CSV/$(notdir $@)"; \
	else \
	    curl -o $@ "ftp://ftp.census.gov/Econ2001_And_Earlier/CBP_CSV/$(notdir $@)"; \
	fi 

raw/%.txt: zips/%.zip
	unzip -L $<
	touch $(notdir $(basename $<)).txt
	mkdir -p $(dir $@)
	mv $(notdir $(basename $<)).txt $(dir $@)
