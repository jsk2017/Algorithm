# modify CC to your own obfuscator-llvm location!

CC := /home/jeb/Desktop/llvm-4.0/build/bin/clang
CFLAGS := -s -mllvm -fla -mllvm -sub -mllvm -bcf
OUT := rc4-level-1
SRC := main.c

# default: $(OUT) 
.PHONY:build
build: $(SRC)
	$(CC) $(CFLAGS) $^ -o $@ 

.PHONY:clean
clean:	*.o
	rm -rf *.o
