
run: main.py display.py draw.py matrix.py parser.py
	python main.py
	open face.png

clean:
	rm *.pyc
	rm *~
