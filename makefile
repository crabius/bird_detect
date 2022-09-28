all:
	#run to download
	rm -rf ./input ./train ./test ./val
	mkdir ./input ./input/kea
	python3 download_birds.py
	mv ./train/kea/* ./train/
	rmdir ./train/kea
	mv ./test/kea/* ./test/
	rmdir ./test/kea
	mv ./val/kea/* ./val/
	rmdir ./val/kea
	tree train test val
move:
	#move to the labelling directory
	rm -rf ../OpenLabeling-master/main/train
	rm -rf ../OpenLabeling-master/main/test
	rm -rf ../OpenLabeling-master/main/val
	cp -r ./train ../OpenLabeling-master/main/
	cp -r ./test ../OpenLabeling-master/main/
	cp -r ./val ../OpenLabeling-master/main/
	tree ../OpenLabeling-master/main/
