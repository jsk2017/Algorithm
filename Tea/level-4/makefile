CC := /home/jeb/Desktop/llvm-4.0/build/bin/clang
CFLAGS := -s -mllvm -fla -mllvm -sub -mllvm -bcf
OUT := tea-level-4
SRC := main.c

.PHONY:clean
clean:	*.o
	rm -rf *.o

.PHONY:build
build: $(SRC)
	$(CC) $(CFLAGS) $^ -o $(OUT)