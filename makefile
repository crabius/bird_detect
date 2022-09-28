download:
	#run to download
	rm -rf ./input
	mkdir ./input/kea
	python3 download.py
clean:
	#run after download
	mv ./train/kea/* ./train/
	rmdir ./train/kea
	mv ./test/kea/* ./test/
	rmdir ./test/kea
	mv ./val/kea/* ./val/
	rmdir ./val/kea
