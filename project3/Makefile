#Settings
TARGET_EXEC := main
TARGET_DIR := bin
BUILD_DIR := build
SRC_DIRS := src

LEXER := $(shell find $(SRC_DIRS) -name '*.l') 
LEXERC := $(LEXER:.l=.c)
PARSER := $(shell find $(SRC_DIRS) -name '*.y') 
PARSERC := $(PARSER:.y=.c)

SRC := $(shell find $(SRC_DIRS) -name '*.c') $(LEXERC) $(PARSERC)
OBJS := $(SRC:%=$(BUILD_DIR)/%.o)
DEPS := $(OBJS:.o=.d)

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

CC := clang
CFLAGS := $(INC_FLAGS) -MMD -MP -std=c23 -O3 -Wall -Wextra
LDLIBS :=
LDFLAGS :=
CDEFS :=

#Colors
ifndef VIM
	RED := \033[38;2;255;0;0m
	YELLOW := \033[38;2;255;255;0m
	GREEN := \033[38;2;21;204;4m
	NC := \033[0m
endif

#Building
$(TARGET_DIR)/$(TARGET_EXEC): $(PARSERC) $(LEXERC) $(OBJS)
	@mkdir -p $(dir $@)
	@$(CC) $(OBJS) -o $(TARGET_DIR)/$(TARGET_EXEC) $(LDFLAGS) $(LDLIBS) && \
		printf '\n  $(GREEN)Compiled binary$(NC): %s\n' $@

$(PARSERC): $(PARSER) $(LEXERC)
	@printf '  $(YELLOW)Generating Parser$(NC): bison %s\n' $(PARSER)
	@bison $(PARSER)
	@mv *.c *.h src

$(LEXERC): $(LEXER)
	@printf '  $(YELLOW)Generating Lexer$(NC): flex %s\n' $(LEXER)
	@flex $(LEXER)
	@mv *.c *.h src

$(BUILD_DIR)/%.c.o: %.c
	@mkdir -p $(dir $@)
	@printf '  $(YELLOW)Compiling$(NC): %s\n' $@
	@$(CC) $(CFLAGS) $(CDEFS) -c $< -o $@

#Commands
.PHONY: clean run
clean: 
	@printf '  $(RED)rm -r$(NC) %s %s src/Parser.{c,h} src/Lexer.{c,h}\n' $(BUILD_DIR)/ $(TARGET_DIR)/
	@rm -r build/ bin/ src/Parser.{c,h} src/Lexer.{c,h} 2>/dev/null || true

run: $(TARGET_DIR)/$(TARGET_EXEC)
	@./$(TARGET_DIR)/$(TARGET_EXEC)

-include $(DEPS)
