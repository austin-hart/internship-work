test-all:
	cd livedataservice/ && make run-tests && cd ..

lint-all:
	cd livedataservice/ && make lint && cd ..